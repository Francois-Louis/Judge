#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""PILOTE-004: replay packaged helper operations on disposable candidate data.

These are explicit fixture operations, NOT execution of the skill by a model.
No client installation, legal validation or participant comprehension is tested.
Optional --evidence FILE records actual accesses, contents and fingerprints.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ".claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md"
SHORT = ("# Préférences de lecture d'embauche\n\n"
         "## Faits et préférences de revue d'embauche\n\n"
         "| Champ | Valeur confirmée |\n|---|---|\n| Format | texte court |\n")
TABLE = SHORT.replace("| Format | texte court |", "| Format | tableau |")
REPORT = {"scope": "helper embarqué sur fixtures ; aucune exécution de skill",
          "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "client": {"claude": shutil.which("claude"), "executed": False},
          "scenarios": []}


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


class CandidateStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_package = tempfile.TemporaryDirectory(prefix="judge-pilote004-package-")
        cls.package = Path(cls.temporary_package.name) / "employment-legal"
        shutil.copytree(ROOT / "employment-legal", cls.package,
                        ignore=shutil.ignore_patterns("__pycache__"))
        cls.package_before = snapshot(cls.package)
        REPORT["artifact"] = {"files": cls.package_before}
        for relative in ("scripts/judge_store.py", "references/shared/research-citation-method.md"):
            source = ROOT / ("scripts/judge_store.py" if relative.startswith("scripts/")
                             else "references/research-citation-method.md")
            if (cls.package / relative).read_bytes() != source.read_bytes():
                raise AssertionError(f"embedded copy changed: {relative}")

    @classmethod
    def tearDownClass(cls):
        REPORT["artifact"]["unchanged"] = snapshot(cls.package) == cls.package_before
        cls.temporary_package.cleanup()

    def setUp(self):
        self.temporary_home = tempfile.TemporaryDirectory(prefix="judge-pilote004-home-")
        self.addCleanup(self.temporary_home.cleanup)
        self.home = Path(self.temporary_home.name)
        self.profile = self.home / PROFILE
        # Fixture preparation is deliberately outside the helper under test.
        witnesses = {
            ".claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md": "ORIGINAL_US_PROFILE",
            ".claude/plugins/config/judge-fr-eu/company-profile.md": "COMPANY_DO_NOT_READ",
            ".claude/plugins/config/judge-fr-eu/employment-legal/matters/autre-salarie/matter.md": "OTHER_EMPLOYEE",
        }
        for relative, content in witnesses.items():
            path = self.home / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        self.witnesses = snapshot(self.home)
        self.record = {"test": self.id().split(".")[-1], "calls": []}
        REPORT["scenarios"].append(self.record)

    def tearDown(self):
        after = snapshot(self.home)
        self.record["after"] = after
        self.record["witnesses_unchanged"] = all(after.get(p) == h for p, h in self.witnesses.items())
        self.record["package_unchanged"] = snapshot(self.package) == self.package_before
        self.assertTrue(self.record["witnesses_unchanged"])
        self.assertTrue(self.record["package_unchanged"])
        self.assertLessEqual(set(after) - set(self.witnesses), {PROFILE})
        # Every successful access must be exactly to the candidate profile or
        # its temporary sibling during atomic replacement, never a witness.
        allowed = {str(self.profile), str(self.profile) + ".judge-pending"}
        for call in self.record["calls"]:
            if call["result"]:
                for event in call["result"]["events"]:
                    self.assertIn(event["path"], allowed)

    def cli(self, *arguments, content=None, ok=True):
        command = [sys.executable, str(self.package / "scripts/judge_store.py"),
                   *arguments, "--home", str(self.home)]
        run = subprocess.run(command, input=content, text=True, encoding="utf-8",
                             capture_output=True, timeout=15, cwd=self.home,
                             env={**os.environ, "PYTHONUTF8": "1"})
        result = json.loads(run.stdout) if run.returncode == 0 else None
        self.record["calls"].append({"command": command, "stdin": content,
                                     "exit_code": run.returncode, "stderr": run.stderr,
                                     "result": result})
        self.assertEqual(run.returncode, 0 if ok else 1, run.stderr)
        return result if ok else run.stderr

    def seed(self, content):
        self.profile.parent.mkdir(parents=True, exist_ok=True)
        self.profile.write_bytes(content.encode("utf-8"))
        self.record["before_content"] = content
        self.record["before"] = snapshot(self.home)

    def test_H12_absent_profile_read_does_not_persist(self):
        before = snapshot(self.home)
        self.record["before"] = before
        read = self.cli("read", "CLAUDE.md")
        self.assertEqual(read["status"], "interview-required")
        self.assertIsNone(read["content"])
        self.assertEqual(read["events"], [{"operation": "read", "path": str(self.profile)}])
        self.assertEqual(snapshot(self.home), before)

    def test_explicit_short_then_table_only_changes_format(self):
        company = ".claude/plugins/config/judge-fr-eu/company-profile.md"
        (self.home / company).unlink()  # Disposable fixture: no shared profile.
        del self.witnesses[company]
        self.record["before"] = snapshot(self.home)
        self.assertIsNone(self.cli("read", "CLAUDE.md")["content"])
        self.cli("create", "CLAUDE.md", content=SHORT)
        short = self.cli("read", "CLAUDE.md")
        self.assertEqual(short["content"], SHORT)
        self.cli("replace", "CLAUDE.md", "--expected-sha256", short["sha256"], content=TABLE)
        table = self.cli("read", "CLAUDE.md")
        self.assertEqual(table["content"], TABLE)
        self.assertEqual(table["content"].replace("| Format | tableau |", "| Format | texte court |"),
                         short["content"])
        self.assertEqual(set(snapshot(self.home)) - set(self.witnesses), {PROFILE})

    def edit_existing(self, before, after):
        self.seed(before)
        read = self.cli("read", "CLAUDE.md")
        self.assertEqual(read["content"], before)
        self.cli("replace", "CLAUDE.md", "--expected-sha256", read["sha256"], content=after)
        reread = self.cli("read", "CLAUDE.md")
        self.assertEqual(reread["content"], after)
        self.assertEqual(self.profile.read_bytes(), after.encode("utf-8"))

    def test_partial_profile_preserves_answers_and_language(self):
        before = ("# Profil partiel\n<!-- SETUP PAUSED AT: rôle -->\n"
                  "| Rôle / besoin | candidat ; offre reçue |\n"
                  "| Format / langue | texte court ; français |\n"
                  "| Travail / dates | Lyon ; début à confirmer |\n")
        self.edit_existing(before, before.replace("texte court ; français", "tableau ; français"))

    def test_US_profile_without_candidate_section_is_preserved(self):
        before = ("# Legacy practice profile\n## Hiring rules\n"
                  "At-will example, exempt and non-compete defaults: NOT FR SOURCES\n"
                  "## Outputs\nATTORNEY WORK PRODUCT\n"
                  "## Matter workspaces\nEnabled: yes ; active: inconnu\n")
        # Fixed expected patch, not a claim that a model ignored these defaults.
        self.edit_existing(before, before + "\n" + TABLE)

    def test_professional_placeholders_remain_untouched(self):
        before = ("# Profil\n## Who we are\n[PLACEHOLDER — Company]\n"
                  "<!-- SETUP PAUSED AT: handbook -->\n" + SHORT)
        self.edit_existing(before, before.replace("| Format | texte court |", "| Format | tableau |"))

    def test_exclusive_create_refuses_profile_appearing_after_read(self):
        self.cli("read", "CLAUDE.md")
        self.seed("# Réponses apparues entre-temps\nNe pas effacer.\n")
        before = snapshot(self.home)
        self.cli("create", "CLAUDE.md", content=SHORT, ok=False)
        self.assertEqual(snapshot(self.home), before)

    def test_stale_fingerprint_refuses_and_reread_preserves_new_answer(self):
        self.seed(SHORT)
        read = self.cli("read", "CLAUDE.md")
        concurrent = SHORT + "\nRéponse confirmée entre-temps : annexe manquante.\n"
        self.seed(concurrent)
        before = snapshot(self.home)
        error = self.cli("replace", "CLAUDE.md", "--expected-sha256", read["sha256"],
                         content=TABLE, ok=False)
        self.assertIn("changed since review", error)
        self.assertEqual(snapshot(self.home), before)
        fresh = self.cli("read", "CLAUDE.md")
        expected = concurrent.replace("| Format | texte court |", "| Format | tableau |")
        self.cli("replace", "CLAUDE.md", "--expected-sha256", fresh["sha256"], content=expected)
        self.assertEqual(self.cli("read", "CLAUDE.md")["content"], expected)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path)
    arguments, remaining = parser.parse_known_args()
    suite = unittest.main(argv=[sys.argv[0], *remaining], exit=False)
    REPORT["result"] = {"tests": suite.result.testsRun,
                        "failures": len(suite.result.failures),
                        "errors": len(suite.result.errors),
                        "skipped": len(suite.result.skipped)}
    if arguments.evidence:
        arguments.evidence.write_text(json.dumps(REPORT, ensure_ascii=False, indent=2) + "\n",
                                      encoding="utf-8")
    sys.exit(not suite.result.wasSuccessful())
