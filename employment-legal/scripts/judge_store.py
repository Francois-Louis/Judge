#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE for BASE-008, 2026-10-15.
"""Confined durable storage. Copied unchanged into each internal plugin.

Python >= 3.12, standard library only. No cache discovery or profile import.
This guards local operations; it is not an OS sandbox against concurrent
hostile filesystem changes. Do not run while another process edits this tree.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import re
import stat
import sys


NAMESPACE = "judge-fr-eu"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_chain(path):
    """Inspect lexical ancestors BEFORE resolve(), including dangling links."""
    for item in (*reversed(path.parents), path):
        if item.is_symlink() or item.is_junction():
            raise ValueError(f"link/junction refused: {item}")
        if item.exists():
            info = item.lstat()
            if getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise ValueError(f"reparse point refused: {item}")
            if stat.S_ISREG(info.st_mode) and info.st_nlink > 1:
                raise ValueError(f"hard link refused: {item}")


def checked_tree(path):
    """Enumerate only after checking each directory; never descend a junction."""
    check_chain(path)
    pending = [path]
    result = []
    while pending:
        item = pending.pop()
        check_chain(item)
        result.append(item)
        if item.is_dir():
            children = sorted(item.iterdir())
            for child in children:
                check_chain(child)
            pending.extend(reversed(children))
    return result


class Store:
    def __init__(self, root):
        self.root = Path(root).absolute()
        check_chain(self.root)
        self.events = []

    def path(self, relative):
        raw = str(relative)
        if (not raw or "\\" in raw or PureWindowsPath(raw).drive
                or raw.startswith("/") or any(
                    not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]*", part)
                    or part.endswith((".", " "))
                    or part.split(".")[0].upper() in {
                        "CON", "PRN", "AUX", "NUL", *[f"COM{i}" for i in range(1, 10)],
                        *[f"LPT{i}" for i in range(1, 10)]}
                    for part in raw.split("/"))):
            raise ValueError("unsafe relative path")
        target = self.root / raw
        check_chain(target)
        if not target.resolve().is_relative_to(self.root.resolve()):
            raise ValueError("outside storage root")
        return target

    def record(self, operation, path):
        self.events.append({"operation": operation, "path": str(path)})

    def read(self, relative):
        target = self.path(relative)
        self.record("read", target)
        return target.read_text(encoding="utf-8") if target.exists() else None

    def list(self, relative):
        target = self.path(relative)
        items = checked_tree(target) if target.exists() else []
        self.record("list", target)
        return [item.relative_to(self.root).as_posix() for item in items]

    def create(self, relative, content):
        target = self.path(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        check_chain(target)
        with target.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        self.record("create", target)
        return target

    def replace(self, relative, content, expected):
        target = self.path(relative)
        if digest(target) != expected:
            raise ValueError("file changed since review; refusing replacement")
        # Atomic replace via an exclusively created sibling; never truncate the
        # existing profile if interrupted while preparing the new contents.
        temporary = self.create(relative + ".judge-pending", content)
        try:
            check_chain(target)
            if digest(target) != expected:
                raise ValueError("file changed since review")
            os.replace(temporary, target)
        finally:
            temporary.unlink(missing_ok=True)
        self.record("replace", target)
        return target

    def append(self, relative, content):
        target = self.path(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        check_chain(target)
        with target.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        self.record("append", target)
        return target

    def move(self, relative, destination):
        source, target = self.path(relative), self.path(destination)
        if target.exists():
            raise FileExistsError(target)
        # Inspect an entire directory before moving it, including links inside.
        checked_tree(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        source.rename(target)
        self.record("move-from", source)
        self.record("move-to", target)
        return target


def plugin_domain():
    manifest = Path(__file__).absolute().parents[1] / ".claude-plugin/plugin.json"
    name = json.loads(manifest.read_text(encoding="utf-8"))["name"]
    if not name.startswith(NAMESPACE + "-"):
        raise ValueError("this helper requires a Judge FR/UE package")
    return name.removeprefix(NAMESPACE + "-")


def main():
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["path", "list", "read", "create", "replace", "append", "move"])
    parser.add_argument("relative")
    parser.add_argument("--destination")
    parser.add_argument("--expected-sha256")
    parser.add_argument("--shared", action="store_true", help="only company-profile.md")
    parser.add_argument("--home", type=Path, default=Path.home(), help="fake home for offline fixtures")
    args = parser.parse_args()
    try:
        base = args.home.absolute() / ".claude/plugins/config" / NAMESPACE
        if args.shared and args.relative != "company-profile.md":
            raise ValueError("shared access is limited to company-profile.md")
        if args.shared and args.operation == "move":
            raise ValueError("shared profile cannot be moved")
        store = Store(base if args.shared else base / plugin_domain())
        target = store.path(args.relative)
        result = {"path": str(target)}
        if args.operation == "read":
            result["content"] = store.read(args.relative)
            result["status"] = ("present" if result["content"] is not None else
                                "interview-required" if args.relative in {"CLAUDE.md", "company-profile.md"} else "missing")
        elif args.operation == "list":
            result["items"] = store.list(args.relative)
        elif args.operation in {"create", "replace", "append"}:
            content = sys.stdin.read()
            if args.operation == "replace":
                store.replace(args.relative, content, args.expected_sha256)
            else:
                getattr(store, args.operation)(args.relative, content)
        elif args.operation == "move":
            target = store.move(args.relative, args.destination or "")
            result["destination"] = str(target)
        result["events"] = store.events
        if target.is_file():
            result["sha256"] = digest(target)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
