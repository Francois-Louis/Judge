#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE for BASE-008, 2026-10-15.
"""Filesystem stage of the hub workflow, AFTER trust review and approval.

No network or source execution. install-log.yaml is JSON (a YAML subset),
schema 1. Unknown/legacy journals fail closed; no journal from another hub is
accepted. Python >= 3.12. Not a sandbox against concurrent hostile processes.
"""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import uuid

from judge_store import Store, check_chain, checked_tree, digest


NAMESPACE = "judge-fr-eu"
BUILTINS = {
    "ai-governance-legal", "commercial-legal", "corporate-legal", "employment-legal",
    "ip-legal", "law-student", "legal-builder-hub", "legal-clinic",
    "litigation-legal", "privacy-legal", "product-legal", "regulatory-legal",
}


def tree_hash(path):
    check_chain(path)
    checksum = hashlib.sha256()
    for item in sorted(checked_tree(path)):
        if item.is_file():
            checksum.update(item.relative_to(path).as_posix().encode() + b"\0")
            checksum.update(hashlib.sha256(item.read_bytes()).digest())
    return checksum.hexdigest()


def skill_name(path):
    text = path.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not frontmatter:
        raise ValueError("SKILL.md requires frontmatter")
    names = re.findall(r"^name: *([a-z0-9-]+) *$", frontmatter[1], re.M)
    if len(names) != 1:
        raise ValueError("require one plain kebab-case frontmatter name")
    return text, names[0]


class Hub:
    def __init__(self, home):
        self.home = Path(home).absolute()
        self.config = Store(self.home / ".claude/plugins/config/judge-fr-eu/legal-builder-hub")
        self.skills = Store(self.home / ".claude/skills")

    @contextmanager
    def lock(self):
        lock = self.config.path("lifecycle-lock")
        lock.parent.mkdir(parents=True, exist_ok=True)
        lock.mkdir()  # An interrupted/parallel operation must be reviewed first.
        try:
            yield
        finally:
            lock.rmdir()

    def identity(self, name):
        if (not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,50}", name)
                or name.startswith(NAMESPACE + "-") or name in BUILTINS):
            raise ValueError("expected an unprefixed community skill slug")
        return NAMESPACE + "-" + name

    def journal(self):
        raw = self.config.read("install-log.yaml")
        if raw is None:
            return {"schema": 1, "namespace": NAMESPACE, "events": []}
        data = json.loads(raw)
        if (data.get("schema") != 1 or data.get("namespace") != NAMESPACE
                or not isinstance(data.get("events"), list)):
            raise ValueError("foreign/unsupported hub journal")
        return data

    def log(self, data, name, action, state, path, sha, metadata=None, **extra):
        data["events"].append({
            "skill": name, "installed_name": self.identity(name),
            "namespace": NAMESPACE, "action": action, "state": state,
            "path": str(path), "sha": sha,
            "tree_sha256": tree_hash(path) if path.exists() else None,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "metadata": metadata or {}, **extra,
        })
        target = self.config.path("install-log.yaml")
        text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        if target.exists():
            self.config.replace("install-log.yaml", text, digest(target))
        else:
            self.config.create("install-log.yaml", text)

    def installed(self, data, name):
        path = self.skills.path(self.identity(name))
        events = [e for e in data["events"] if e.get("skill") == name]
        if not events:
            raise ValueError("not installed by this fork hub")
        last = events[-1]
        if (last.get("namespace") != NAMESPACE
                or last.get("installed_name") != self.identity(name)
                or last.get("path") != str(path)
                or last.get("state") not in {"enabled", "disabled"}):
            raise ValueError("foreign path, identity or inactive journal entry")
        if tree_hash(path) != last.get("tree_sha256"):
            raise ValueError("installation changed since review; preserve and compare local edits")
        filename = "SKILL.md" if last["state"] == "enabled" else "SKILL.md.disabled"
        if skill_name(path / filename)[1] != self.identity(name):
            raise ValueError("installed skill identity mismatch")
        return path, last

    def stage(self, source, name):
        source = Path(source).absolute()
        check_chain(source)
        if not source.is_dir():
            raise ValueError("source must be a reviewed skill directory")
        tree_hash(source)  # Reject descendant links/junctions before copytree.
        text, original_name = skill_name(source / "SKILL.md")
        if original_name != name:
            raise ValueError("source skill identity mismatch")
        destination = self.config.path("staging/" + uuid.uuid4().hex)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
        front, body = text.split("---", 2)[1:]
        front = re.sub(r"(?m)^name: *[a-z0-9-]+ *$", "name: " + self.identity(name), front)
        (destination / "SKILL.md").write_text("---" + front + "---" + body, encoding="utf-8")
        return destination

    def apply(self, action, name, source=None, sha=None, metadata=None):
        with self.lock():
            return self._apply(action, name, source, sha, metadata)

    def _apply(self, action, name, source, sha, metadata):
        identity = self.identity(name)
        data = self.journal()
        target = self.skills.path(identity)
        if action in {"install", "update"} and not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", sha or ""):
            raise ValueError("pin an exact commit SHA")
        if action == "install":
            if target.exists():
                raise FileExistsError(target)
            prior = [e for e in data["events"] if e.get("skill") == name]
            if prior and prior[-1].get("state") != "uninstalled":
                raise ValueError("journal already records an installation; review missing files")
            staged = self.stage(source, name)
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                self.skills.path(identity)
                if target.exists():
                    raise FileExistsError(target)
                staged.rename(target)
                try:
                    self.log(data, name, action, "enabled", target, sha, metadata)
                except Exception:
                    target.rename(staged)
                    raise
            finally:
                if staged.exists():
                    shutil.rmtree(staged)
            return target

        target, last = self.installed(data, name)
        metadata = last.get("metadata", {}) if metadata is None else metadata
        if action in {"update", "rollback"}:
            if last["state"] != "enabled":
                raise ValueError("enable the skill before updating or rolling back")
            if action == "update":
                staged = self.stage(source, name)
                next_sha = sha
            else:
                if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", sha or ""):
                    raise ValueError("rollback requires an exact saved SHA")
                matches = [e for e in data["events"] if e.get("skill") == name
                           and e.get("backup_sha") == sha]
                if not matches:
                    raise ValueError("backup not recorded by this fork hub")
                backup_event = matches[-1]
                staged = self.config.path(f"backups/{identity}/{sha}")
                if (backup_event.get("backup_path") != str(staged)
                        or tree_hash(staged) != backup_event.get("backup_tree_sha256")
                        or skill_name(staged / "SKILL.md")[1] != identity):
                    raise ValueError("backup identity, path or contents changed")
                metadata = backup_event.get("backup_metadata", {})
                next_sha = sha
            backup = self.config.path(f"backups/{identity}/{last['sha']}")
            if backup.exists():
                if action == "update":
                    shutil.rmtree(staged)
                raise FileExistsError(backup)
            backup.parent.mkdir(parents=True, exist_ok=True)
            target.rename(backup)
            try:
                staged.rename(target)
                self.log(data, name, action, "enabled", target, next_sha, metadata,
                         backup_path=str(backup), backup_sha=last["sha"],
                         backup_tree_sha256=last["tree_sha256"],
                         backup_metadata=last.get("metadata", {}))
            except Exception:
                if target.exists():
                    target.rename(staged)
                backup.rename(target)
                raise
            finally:
                if action == "update" and staged.exists():
                    shutil.rmtree(staged)
            return target

        if action in {"disable", "enable"}:
            wanted = "enabled" if action == "enable" else "disabled"
            if last["state"] == wanted:
                raise ValueError("already " + wanted)
            pairs = []
            # Keep hooks and agents inactive along with SKILL.md.
            for item in sorted(checked_tree(target)):
                rel = item.relative_to(target).as_posix()
                active = rel.removesuffix(".disabled")
                if (active == "SKILL.md" or active == "hooks/hooks.json"
                        or (active.startswith("agents/") and active.endswith(".md"))):
                    renamed = (item.with_suffix(item.suffix + ".disabled") if action == "disable"
                               else item.with_name(item.name.removesuffix(".disabled")))
                    if renamed.exists():
                        raise FileExistsError(renamed)
                    pairs.append((item, renamed))
            completed = []
            try:
                for before, after in pairs:
                    before.rename(after)
                    completed.append((before, after))
                self.log(data, name, action, wanted, target, last["sha"], metadata)
            except Exception:
                for before, after in reversed(completed):
                    after.rename(before)
                raise
            return target

        if action == "uninstall":
            # Move into private staging until journal is durable. Never delete
            # user configuration or another installation's skill directory.
            staged = self.config.path("staging/" + uuid.uuid4().hex)
            staged.parent.mkdir(parents=True, exist_ok=True)
            target.rename(staged)
            try:
                self.log(data, name, action, "uninstalled", target, last["sha"], metadata)
            except Exception:
                staged.rename(target)
                raise
            shutil.rmtree(staged)
            return target
        raise ValueError("unknown lifecycle action")


def main():
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["install", "update", "rollback", "disable", "enable", "uninstall"])
    parser.add_argument("skill", help="upstream community slug, without judge-fr-eu prefix")
    parser.add_argument("--source", type=Path, help="reviewed, staged candidate; never executed")
    parser.add_argument("--sha", help="reviewed commit, or recorded rollback commit")
    parser.add_argument("--metadata", type=Path, help="reviewed license/freshness/registry facts as JSON")
    parser.add_argument("--approved", action="store_true", help="set only after the workflow's human approval")
    parser.add_argument("--home", type=Path, default=Path.home(), help="fake home for offline fixtures")
    args = parser.parse_args()
    try:
        if not args.approved:
            raise ValueError("complete trust review and explicit approval before filesystem stage")
        if args.action in {"install", "update"} and args.source is None:
            raise ValueError("reviewed source required")
        metadata = json.loads(args.metadata.read_text(encoding="utf-8")) if args.metadata else None
        if metadata is not None and not isinstance(metadata, dict):
            raise ValueError("metadata must be an object")
        target = Hub(args.home).apply(args.action, args.skill, args.source, args.sha, metadata)
        print(json.dumps({"action": args.action, "path": str(target), "namespace": NAMESPACE}))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
