#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Modified by Judge FR/UE for BASE-008, 2026-10-15: recognize both command namespaces in inventories.
"""BASE-004 design evidence, not an installer or a profile migration tool.

Without arguments: simulate the proposed policy using disposable fake profiles.
--inventory: list repository references as TSV on stdout, without changing files.
Only the simulation writes data, exclusively under its TemporaryDirectory.
"""

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
UPSTREAM = "claude-for-legal"
FORK = "judge-fr-eu"


def inventory():
    marketplace = json.loads(
        (REPO / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
    )
    # Directory keys remain stable after BASE-008; recognize historical and
    # migrated command namespaces when regenerating the inventory.
    names = [p["source"].removeprefix("./") for p in marketplace["plugins"]
             if p["source"].startswith("./")
             and not p["source"].startswith("./external_plugins/")]
    patterns = {
        "nom-origine": re.compile(re.escape(UPSTREAM)),
        "profil": re.compile(r"plugins/config/"),
        "cache": re.compile(r"plugins/cache/"),
        "installation": re.compile(r"(?:/plugin|claude plugin)\s"),
        "commande-domaine": re.compile(
            r"/(?:judge-fr-eu-)?(?:" + "|".join(map(re.escape, names)) + r"):"
        ),
        "skills-partages": re.compile(r"\.claude/skills/"),
        "sorties-relatives": re.compile(r"\./(?:out|outputs|logs)/"),
        "deploiement": re.compile(r"\b(?:REPO_SLUG|SKILL_TITLE_PREFIX)\b"),
    }
    # Includes untracked backlog-era source files; ignores Git-ignored files.
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=REPO,
    ).decode("utf-8").split("\0")
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(["fichier", "categories", "lignes", "lignes_nom_origine"])
    for name in sorted(set(paths)):
        if (not name or name.startswith("backlog/")
                or name == "scripts/check-base004-isolation.py"):
            continue
        path = REPO / name
        if not path.is_file() or path.suffix not in {
            ".md", ".json", ".yaml", ".yml", ".py", ".sh", ".gitignore"
        }:
            continue
        found = {}
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for category, pattern in patterns.items():
                if pattern.search(line):
                    found.setdefault(category, []).append(number)
        if found:
            lines = sorted({n for numbers in found.values() for n in numbers})
            writer.writerow([name, ";".join(sorted(found)),
                             ",".join(map(str, lines)),
                             ",".join(map(str, found.get("nom-origine", [])))])


class FakeStore:
    """Minimal policy model. Never used by shipped skills or with real profiles."""

    def __init__(self, root):
        self.root = root.resolve()
        self.events = []

    def path(self, relative):
        candidate = self.root / relative
        if Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise ValueError("absolute path or traversal refused")
        # Refuse links/junctions even if they happen to stay within this root.
        for part in (candidate, *candidate.parents):
            if part.is_symlink() or part.is_junction():
                raise ValueError("linked path refused")
            if part == self.root:
                break
        target = candidate.resolve()
        if not target.is_relative_to(self.root):
            raise ValueError("outside namespace")
        return target

    def read(self, relative):
        path = self.path(relative)
        self.events.append(("read", path))
        return path.read_text(encoding="utf-8") if path.exists() else None

    def create(self, relative, content):
        path = self.path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation also refuses an existing, empty destination.
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        self.events.append(("write", path))


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def simulate():
    with tempfile.TemporaryDirectory(prefix="judge-base004-") as directory:
        home = Path(directory)
        config = home / ".claude/plugins/config"
        original = FakeStore(config / UPSTREAM)
        fork = FakeStore(config / FORK)
        profile = "employment-legal/CLAUDE.md"
        matter = "employment-legal/matters/demo/matter.md"
        original.create(profile, "US_ONLY_SENTINEL\nJurisdiction: California\n")
        original.create("company-profile.md", "US_COMPANY_SENTINEL\n")
        original.create(matter, "US_MATTER_SENTINEL\n")
        # Simulate the legacy cache auto-import trap with a populated profile.
        cache = home / ".claude/plugins/cache" / UPSTREAM / "employment-legal/1.0.2"
        cache.mkdir(parents=True)
        (cache / "CLAUDE.md").write_text("US_CACHE_SENTINEL\n", encoding="utf-8")
        original_before = snapshot(original.root)
        cache_before = snapshot(cache)
        original.events.clear()

        require(fork.read(profile) is None, "missing fork profile used a fallback")
        require(fork.read("company-profile.md") is None, "shared profile fallback")
        print("PASS absent fork profile: no original or legacy cache import")

        fork.create(profile, "FR_ONLY_SENTINEL\nJurisdiction: France\n")
        fork.create("company-profile.md", "FR_COMPANY_SENTINEL\n")
        fork.create(matter, "FR_MATTER_SENTINEL\n")
        require("FR_ONLY_SENTINEL" in fork.read(profile), "wrong fork profile")
        require("FR_COMPANY_SENTINEL" in fork.read("company-profile.md"), "wrong company")
        require("FR_MATTER_SENTINEL" in fork.read(matter), "wrong matter")
        require(original.events == [], "fork operation accessed original store")
        fork_events = list(fork.events)
        require("US_ONLY_SENTINEL" in original.read(profile), "wrong original profile")
        require("US_COMPANY_SENTINEL" in original.read("company-profile.md"), "wrong original company")
        require("US_MATTER_SENTINEL" in original.read(matter), "wrong original matter")
        require(fork.events == fork_events, "original operation accessed fork store")
        print("PASS two profiles, company files and identical matter slugs: isolated reads")

        fork_before = snapshot(fork.root)
        try:
            fork.create(profile, "MUST_NOT_OVERWRITE\n")
        except FileExistsError:
            pass
        else:
            raise RuntimeError("existing fork profile overwritten")
        require(snapshot(fork.root) == fork_before, "collision modified fork files")
        print("PASS existing destination: refused, contents unchanged")

        for relative in ("../claude-for-legal/employment-legal/CLAUDE.md", str(cache / "CLAUDE.md")):
            try:
                fork.read(relative)
            except ValueError:
                pass
            else:
                raise RuntimeError("cross-namespace path accepted")
        print("PASS traversal and absolute legacy cache path: refused before reading")

        # A newly installed package version cannot become a profile source.
        next_cache = home / ".claude/plugins/cache" / FORK / "judge-fr-eu-employment-legal/0.2.0"
        next_cache.mkdir(parents=True)
        (next_cache / "CLAUDE.md").write_text("PACKAGE_TEMPLATE\n", encoding="utf-8")
        fork.create("employment-legal/outputs/demo.md", "FR_OUTPUT_SENTINEL\n")
        require(fork.read(profile) == "FR_ONLY_SENTINEL\nJurisdiction: France\n", "update replaced profile")
        require(all(snapshot(fork.root)[p] == digest for p, digest in fork_before.items()),
                "update modified existing fork data")
        require(snapshot(original.root) == original_before, "original data changed")
        require(snapshot(cache) == cache_before, "legacy cache changed")
        require(all(path.is_relative_to(fork.root) for _, path in fork.events),
                "fork accessed another namespace")
        require(all(path.is_relative_to(original.root) for _, path in original.events),
                "original accessed another namespace")
        print("PASS new package version and fork output: both profiles and original cache unchanged")
        print(f"PASS audit: {len(fork.events)} fork accesses confined to {FORK}")
    print("Temporary fixtures removed. No installed plugin or real profile accessed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", action="store_true", help="print repository reference inventory as TSV")
    args = parser.parse_args()
    if args.inventory:
        inventory()
    else:
        simulate()


if __name__ == "__main__":
    main()
