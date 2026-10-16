#!/usr/bin/env python3
"""Check that every modified plugin has a higher version than the base ref.

Claude Code caches an installed plugin by the `version` of its
`.claude-plugin/plugin.json`: a pushed change without a version bump does not
reach users who update the marketplace. This compares the working tree
(committed, staged, unstaged and untracked files) with a base ref, origin/main
by default, and fails for each modified first-party plugin whose version did
not increase. New plugins pass. Run it before `git push origin main`.

Usage: python scripts/check-version-bump.py [--base <ref>]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ".claude-plugin/plugin.json"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True,
                          text=True, encoding="utf-8").stdout


def version_key(version):
    parts = re.findall(r"\d+", version.split("-")[0].split("+")[0])
    return tuple(int(p) for p in parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", default="origin/main", help="ref to compare against (default: origin/main)")
    base = parser.parse_args().base
    try:
        git("rev-parse", "--verify", "--quiet", base + "^{commit}")
    except subprocess.CalledProcessError:
        print(f"ERROR: unknown base ref {base!r}", file=sys.stderr)
        return 2

    changed = set(git("diff", "--name-only", base).splitlines())
    changed |= set(git("ls-files", "--others", "--exclude-standard").splitlines())
    plugins = sorted(p.parent.parent.name for p in ROOT.glob("*/" + MANIFEST))

    failures = 0
    for plugin in plugins:
        files = [f for f in changed if f.startswith(plugin + "/")]
        if not files:
            continue
        current = json.loads((ROOT / plugin / MANIFEST).read_text(encoding="utf-8"))["version"]
        try:
            previous = json.loads(git("show", f"{base}:{plugin}/{MANIFEST}"))["version"]
        except subprocess.CalledProcessError:
            print(f"OK   {plugin}: new plugin at {current}")
            continue
        if version_key(current) > version_key(previous):
            print(f"OK   {plugin}: {previous} -> {current} ({len(files)} file(s) changed)")
        else:
            failures += 1
            print(f"FAIL {plugin}: {len(files)} file(s) changed but version stays {current} "
                  f"(base {previous}); bump {plugin}/{MANIFEST}")
    if not failures:
        print(f"Version bump check passed against {base}.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
