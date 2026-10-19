#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE for BASE-008, 2026-10-15.
"""Offline evidence on DETACHED migrated packages, never on personal profiles.

No LLM execution, Claude installation or remote deployment. Run with Python
3.12+ and PyYAML. Cookbook audit tests additionally require jsonschema.
"""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MARKET = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class MigratedPackages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = tempfile.TemporaryDirectory(prefix="judge-base008-packages-")
        cls.packages = {}
        for entry in MARKET["plugins"]:
            domain = entry["source"].removeprefix("./")
            artifact = Path(cls.artifacts.name) / domain
            shutil.copytree(ROOT / domain, artifact, ignore=shutil.ignore_patterns("__pycache__"))
            cls.packages[domain] = artifact
        hub_scripts = cls.packages["legal-builder-hub"] / "scripts"
        # Load the actual shipped copies, outside the checkout.
        cls.store_module = module("base008_packaged_store", hub_scripts / "judge_store.py")
        sys.modules["judge_store"] = cls.store_module
        cls.hub_module = module("base008_packaged_hub", hub_scripts / "community_store.py")
        cls.checker = module("base008_package_checker", ROOT / "scripts/check-plugin-package.py")

    @classmethod
    def tearDownClass(cls):
        cls.artifacts.cleanup()

    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory(prefix="judge-base008-home-")
        self.addCleanup(self.fixture.cleanup)
        self.home = Path(self.fixture.name)
        self.original = self.home / ".claude/plugins/config/claude-for-legal"
        self.original.mkdir(parents=True)
        (self.original / "company-profile.md").write_text("ORIGINAL_COMPANY", encoding="utf-8")
        self.hub = self.hub_module.Hub(self.home)

    def cli(self, domain, *args, content=None, ok=True, package=None):
        result = subprocess.run(
            [sys.executable, str((package or self.packages[domain]) / "scripts/judge_store.py"),
             *args, "--home", str(self.home)], input=content, text=True,
            encoding="utf-8", capture_output=True, timeout=15,
            env={**os.environ, "PYTHONUTF8": "1"}, cwd=self.home)
        self.assertEqual(result.returncode, 0 if ok else 1, result.stderr)
        return json.loads(result.stdout) if ok else result.stderr

    def candidate(self, version="one"):
        path = self.home / ("candidate-" + version)
        path.mkdir()
        (path / "SKILL.md").write_text(
            "---\nname: demo\ndescription: A disposable community skill\n---\n" + version + "\n", encoding="utf-8")
        (path / "hooks").mkdir()
        (path / "hooks/hooks.json").write_text("{}", encoding="utf-8")
        (path / "agents").mkdir()
        (path / "agents/worker.md").write_text("fixture", encoding="utf-8")
        return path

    def test_manifest_contract_and_144_skill_names(self):
        self.assertEqual(MARKET["name"], "judge-fr-eu")
        self.assertEqual(MARKET["owner"]["name"], "Judge FR/UE maintainers")
        self.assertEqual(len(MARKET["plugins"]), 18)
        count = 0
        for entry in MARKET["plugins"]:
            domain = entry["source"][2:]
            package = self.packages[domain]
            manifest = json.loads((package / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
            for field in ("name", "description", "author"):
                self.assertEqual(entry[field], manifest[field])
            self.assertEqual(manifest["name"], "judge-fr-eu-" + domain)
            expected_author = "Judge FR/UE maintainers" if domain in {"banking-legal", "consumer-legal", "enforcement-legal", "criminal-legal", "funeral-legal", "insurance-legal", "customs-legal"} else "Anthropic"
            self.assertEqual(manifest["author"]["name"], expected_author)
            expected_version = {"employment-legal": "0.4.0", "commercial-legal": "0.2.4",
                                "banking-legal": "0.1.3", "consumer-legal": "0.1.2", "enforcement-legal": "0.1.1", "criminal-legal": "0.1.2", "funeral-legal": "0.1.1", "insurance-legal": "0.1.1", "customs-legal": "0.4.0"}.get(domain, "0.1.3")
            self.assertEqual(manifest["version"], expected_version)
            self.assertEqual((package / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
            self.assertTrue((package / "NOTICE").is_file())
            self.assertEqual((package / "scripts/judge_store.py").read_bytes(), (ROOT / "scripts/judge_store.py").read_bytes())
            self.assertEqual((package / "references/isolation.md").read_bytes(), (ROOT / "references/isolation.md").read_bytes())
            self.assertEqual((package / "references/shared/research-citation-method.md").read_bytes(),
                             (ROOT / "references/research-citation-method.md").read_bytes())
            skills = list((package / "skills").glob("*/SKILL.md"))
            count += len(skills)
            for path in skills:
                data = self.checker.yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
                self.assertEqual(data["name"], path.parent.name)
        self.assertEqual(count, 144)

    def test_detached_package_structure(self):
        for domain, package in self.packages.items():
            with self.subTest(domain=domain):
                checker = self.checker.Checker(package)
                checker.run()
                self.assertEqual(checker.errors, [])
                # Dynamic paths and cross-plugin calls remain manual-review
                # findings, NOT a claim of executing those prompt instructions.

    def test_all_documented_qualified_commands_resolve(self):
        available = {"judge-fr-eu-" + d: {p.parent.name for p in (a / "skills").glob("*/SKILL.md")}
                     for d, a in self.packages.items()}
        paths = [ROOT / "README.md", ROOT / "QUICKSTART.md"]
        paths += [p for a in self.packages.values() for p in a.rglob("*.md")]
        for path in paths:
            for name, skill in re.findall(r"(?<![a-z0-9-])(judge-fr-eu-[a-z0-9-]+):([a-z0-9-]+)", path.read_text(encoding="utf-8")):
                self.assertIn(name, available, str(path))
                self.assertIn(skill, available[name], f"{path}: {name}:{skill}")

    def test_all_entrypoints_load_boundary_and_no_legacy_access(self):
        for domain, package in self.packages.items():
            entries = [*package.glob("skills/*/SKILL.md"), *package.glob("agents/*.md")]
            for path in entries:
                text = path.read_text(encoding="utf-8")
                self.assertIn("${CLAUDE_PLUGIN_ROOT}/references/isolation.md", text, str(path))
                self.assertNotRegex(text, r"plugins/(config|cache)/claude-for-legal/")
                self.assertNotRegex(text, r"(?<!judge-fr-eu-)\b" + re.escape(domain) + r":")
            setup_path = package / "skills/cold-start-interview/SKILL.md"
            if domain in {"banking-legal", "consumer-legal", "enforcement-legal", "criminal-legal", "funeral-legal", "insurance-legal", "customs-legal"}:
                self.assertFalse(setup_path.exists())
                self.assertEqual({p.parent.name for p in package.glob("skills/*/SKILL.md")},
                                 {"banking-legal": {"payment-dispute"}, "consumer-legal": {"non-delivery-claim"},
                                  "enforcement-legal": {"enforcement-act-reading"},
                                  "criminal-legal": {"summons-reading"},
                                  "funeral-legal": {"funeral-quote-review"},
                                  "insurance-legal": {"claim-denial-review"},
                                  "customs-legal": {"import-document-checklist", "overseas-shipment-documents", "traveller-goods-documents", "customs-notice-review"}}[domain])
                continue  # First domain slices have no setup or durable storage workflow.
            setup = setup_path.read_text(encoding="utf-8")
            self.assertIn("Judge FR/UE setup boundary", setup)
            self.assertNotIn("plugins/cache/", setup)

    def test_real_storage_cli_all_domains_and_missing_cache_trap(self):
        cache = self.home / ".claude/plugins/cache/claude-for-legal/employment-legal/1.0.2"
        cache.mkdir(parents=True)
        (cache / "CLAUDE.md").write_text("DO_NOT_IMPORT_US_CACHE", encoding="utf-8")
        for domain in self.packages:
            with self.subTest(domain=domain):
                original_domain = self.original / domain
                (original_domain / "matters/demo").mkdir(parents=True)
                (original_domain / "CLAUDE.md").write_text("ORIGINAL_PROFILE", encoding="utf-8")
                (original_domain / "matters/demo/matter.md").write_text("ORIGINAL_MATTER", encoding="utf-8")
                original_before = snapshot(self.original)
                self.assertEqual(self.cli(domain, "read", "CLAUDE.md")["status"], "interview-required")
                marker = "FR_" + domain + "\n<!-- SETUP PAUSED AT: footprint -->\nAnswer: preserve\n"
                self.cli(domain, "create", "CLAUDE.md", content=marker)
                self.cli(domain, "create", "matters/demo/matter.md", content="FR_MATTER")
                result = self.cli(domain, "read", "CLAUDE.md")
                self.assertEqual(result["content"], marker)
                self.assertTrue(all("config\\judge-fr-eu\\" in e["path"] or "config/judge-fr-eu/" in e["path"]
                                    for e in result["events"]))
                self.cli(domain, "create", "CLAUDE.md", content="overwrite", ok=False)
                self.cli(domain, "replace", "CLAUDE.md", "--expected-sha256", "0" * 64, content="overwrite", ok=False)
                self.cli(domain, "append", "matters/demo/history.md", content="FR_EVENT\n")
                self.cli(domain, "move", "matters/demo", "--destination", "matters/_archived/demo")
                self.assertEqual(self.cli(domain, "read", "matters/_archived/demo/matter.md")["content"], "FR_MATTER")
                self.assertEqual(snapshot(self.original), original_before)
        self.assertEqual((cache / "CLAUDE.md").read_text(encoding="utf-8"), "DO_NOT_IMPORT_US_CACHE")

    def test_shared_profile_and_package_update_rollback_preserve_data(self):
        d = "employment-legal"
        self.cli(d, "create", "company-profile.md", "--shared", content="FR_COMPANY")
        self.cli(d, "create", "CLAUDE.md", content="FR_PROFILE\nPersonal threshold: confirmed\n")
        self.cli(d, "create", "outputs/demo.md", content="FR_OUTPUT")
        before = snapshot(self.home / ".claude/plugins/config")
        self.assertEqual(self.cli("privacy-legal", "read", "company-profile.md", "--shared")["content"], "FR_COMPANY")
        self.cli(d, "create", "company-profile.md", "--shared", content="replace", ok=False)
        self.cli(d, "read", "employment-legal/CLAUDE.md", "--shared", ok=False)
        update = self.home / "package-next-version"
        shutil.copytree(self.packages[d], update)
        manifest = update / ".claude-plugin/plugin.json"
        metadata = json.loads(manifest.read_text(encoding="utf-8"))
        major, minor, _ = map(int, metadata["version"].split("."))
        metadata["version"] = f"{major}.{minor + 1}.0"
        manifest.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        (update / "CLAUDE.md").write_text("NEW_PACKAGE_TEMPLATE", encoding="utf-8")
        self.assertIn("Personal threshold", self.cli(d, "read", "CLAUDE.md", package=update)["content"])
        self.assertIn("Personal threshold", self.cli(d, "read", "CLAUDE.md")["content"])
        self.assertEqual(snapshot(self.home / ".claude/plugins/config"), before)

    def test_guard_refuses_traversal_windows_paths_and_existing_destinations(self):
        store = self.store_module.Store(self.home / "fork")
        for raw in ("../original/x", "/absolute", "C:/original/x", "C:relative", "\\\\host\\share", "a\\..\\x", "a//b", "a/./b", "CON", "file:stream", "a/..", "x."):
            with self.subTest(path=raw), self.assertRaises(ValueError):
                store.read(raw)
        store.create("empty.md", "")
        with self.assertRaises(FileExistsError):
            store.create("empty.md", "replace")
        store.create("matters/demo/matter.md", "A")
        store.create("matters/_archived/demo/matter.md", "B")
        self.assertIn("matters/demo/matter.md", store.list("matters"))
        with self.assertRaises(FileExistsError):
            store.move("matters/demo", "matters/_archived/demo")
        self.assertEqual(store.read("matters/_archived/demo/matter.md"), "B")

    def link_fixture(self, kind, destination, target):
        if kind == "junction":
            if os.name != "nt":
                self.skipTest("Windows junction scenario requires Windows")
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(destination), str(target)],
                                    capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            try:
                destination.symlink_to(target, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"OS cannot create a symbolic link: {exc}")
        self.addCleanup(lambda: destination.unlink() if destination.is_symlink() else destination.rmdir())

    def exercise_link_refusals(self, kind):
        outside = self.home / "outside"
        outside.mkdir()
        (outside / "sentinel.md").write_text("UNCHANGED", encoding="utf-8")
        store = self.store_module.Store(self.home / "fork")
        store.root.mkdir()
        linked = store.root / "linked"
        self.link_fixture(kind, linked, outside)
        with self.assertRaises(ValueError):
            store.read("linked/sentinel.md")
        with self.assertRaises(ValueError):
            store.list("linked")
        with self.assertRaises(ValueError):
            self.store_module.Store(linked / "nested")
        candidate = self.candidate()
        child = candidate / "linked"
        self.link_fixture(kind, child, outside)
        with self.assertRaises(ValueError):
            self.hub.apply("install", "demo", candidate, "a" * 40)
        self.assertEqual((outside / "sentinel.md").read_text(encoding="utf-8"), "UNCHANGED")

    def test_symbolic_links_refused(self):
        self.exercise_link_refusals("symlink")

    def test_windows_junctions_refused(self):
        self.exercise_link_refusals("junction")

    def test_hard_links_refused(self):
        store = self.store_module.Store(self.home / "fork")
        store.create("file.md", "KEEP")
        other = self.home / "hard.md"
        os.link(store.root / "file.md", other)
        with self.assertRaises(ValueError):
            store.append("file.md", "MUTATION")
        self.assertEqual(other.read_text(encoding="utf-8"), "KEEP")

    def test_hub_lifecycle_leaves_original_and_durable_data_untouched(self):
        original_skill = self.home / ".claude/skills/demo"
        original_skill.mkdir(parents=True)
        (original_skill / "SKILL.md").write_text("ORIGINAL_SKILL", encoding="utf-8")
        original_log = self.original / "legal-builder-hub/install-log.yaml"
        original_log.parent.mkdir()
        original_log.write_text("ORIGINAL_JOURNAL", encoding="utf-8")
        before = snapshot(self.original)
        self.hub.config.create("CLAUDE.md", "FR_HUB_ANSWERS")
        self.hub.config.create("allowlist.yaml", "FR_ALLOWLIST")
        target = self.hub.apply("install", "demo", self.candidate(), "a" * 40, {"license": "MIT"})
        self.assertIn("name: judge-fr-eu-demo", (target / "SKILL.md").read_text(encoding="utf-8"))
        self.hub.apply("update", "demo", self.candidate("two"), "b" * 40, {"license": "Apache-2.0"})
        backup = self.hub.config.path("backups/judge-fr-eu-demo/" + "a" * 40)
        self.assertTrue(backup.is_dir())
        self.hub.apply("rollback", "demo", sha="a" * 40)
        self.assertEqual(self.hub.journal()["events"][-1]["metadata"], {"license": "MIT"})
        self.assertTrue((target / "SKILL.md").read_text(encoding="utf-8").endswith("one\n"))
        self.hub.apply("disable", "demo")
        for rel in ("SKILL.md", "hooks/hooks.json", "agents/worker.md"):
            self.assertFalse((target / rel).exists())
            self.assertTrue((target / (rel + ".disabled")).exists())
        self.hub.apply("enable", "demo")
        self.hub.apply("disable", "demo")
        self.hub.apply("uninstall", "demo")
        self.assertFalse(target.exists())
        self.assertEqual((original_skill / "SKILL.md").read_text(encoding="utf-8"), "ORIGINAL_SKILL")
        self.assertEqual(snapshot(self.original), before)
        self.assertEqual(self.hub.config.read("CLAUDE.md"), "FR_HUB_ANSWERS")
        self.assertEqual(self.hub.config.read("allowlist.yaml"), "FR_ALLOWLIST")
        self.assertEqual([e["action"] for e in self.hub.journal()["events"]],
                         ["install", "update", "rollback", "disable", "enable", "disable", "uninstall"])

    def test_hub_refuses_existing_destination_unknown_skill_and_original_log(self):
        candidate = self.candidate()
        self.hub.skills.path("judge-fr-eu-demo").mkdir(parents=True)
        with self.assertRaises(FileExistsError):
            self.hub.apply("install", "demo", candidate, "a" * 40)
        for action in ("update", "rollback", "disable", "enable", "uninstall"):
            with self.subTest(action=action), self.assertRaises(ValueError):
                self.hub.apply(action, "demo", candidate, "b" * 40)
        for name in ("../demo", "C:/demo", "judge-fr-eu-demo", "employment-legal"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.hub.apply("install", name, candidate, "a" * 40)
        self.hub.config.create("install-log.yaml", json.dumps({"namespace": "claude-for-legal", "schema": 1, "events": []}))
        with self.assertRaises(ValueError):
            self.hub.apply("disable", "demo")

    def test_hub_local_edits_and_backup_collision_preserved(self):
        first = self.candidate()
        target = self.hub.apply("install", "demo", first, "a" * 40)
        second = self.candidate("two")
        self.hub.config.path("backups/judge-fr-eu-demo/" + "a" * 40).mkdir(parents=True)
        before = snapshot(target)
        with self.assertRaises(FileExistsError):
            self.hub.apply("update", "demo", second, "b" * 40)
        self.assertEqual(snapshot(target), before)
        (target / "SKILL.md").write_text("LOCAL_CUSTOMIZATION", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.hub.apply("uninstall", "demo")
        self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "LOCAL_CUSTOMIZATION")

    def test_hub_rejects_forged_logged_path_and_changed_backup(self):
        target = self.hub.apply("install", "demo", self.candidate(), "a" * 40)
        self.hub.apply("update", "demo", self.candidate("two"), "b" * 40)
        backup = self.hub.config.path("backups/judge-fr-eu-demo/" + "a" * 40)
        (backup / "SKILL.md").write_text("MODIFIED_BACKUP", encoding="utf-8")
        before = snapshot(target)
        with self.assertRaises(ValueError):
            self.hub.apply("rollback", "demo", sha="a" * 40)
        data = self.hub.journal()
        data["events"][-1]["path"] = str(self.original)
        log = self.hub.config.path("install-log.yaml")
        log.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaises(ValueError):
            self.hub.apply("uninstall", "demo")
        self.assertEqual(snapshot(target), before)


class CookbookStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(ROOT / "scripts"))
        cls.paths = module("base008_cookbook_paths", ROOT / "scripts/cookbook_paths.py")

    def test_five_cookbooks_outputs_audit_and_separate_deployments(self):
        with tempfile.TemporaryDirectory(prefix="judge-base008-cookbooks-") as tmp:
            base = Path(tmp)
            original = base / "out"
            original.mkdir()
            (original / "handoff-audit.jsonl").write_text("ORIGINAL_AUDIT", encoding="utf-8")
            before = snapshot(original)
            for role in sorted(self.paths.ROLES):
                a = self.paths.prepare(base, "deployment-a", role)
                b = self.paths.prepare(base, "deployment-b", role)
                a.create("report.md", role + "_A")
                b.create("report.md", role + "_B")
                a.append("handoff-audit.jsonl", "FORK_AUDIT\n")
                self.assertNotEqual(a.root, b.root)
                self.assertEqual(b.read("report.md"), role + "_B")
                with self.assertRaises(FileExistsError):
                    self.paths.prepare(base, "deployment-a", role)
                with self.assertRaises(ValueError):
                    a.create("../../out/report.md", "WRONG")
            self.assertEqual(snapshot(original), before)

    def test_orchestrator_audit_and_report_paths(self):
        try:
            import jsonschema  # noqa: F401
        except ImportError:
            self.skipTest("jsonschema absent: orchestrator test not executed")
        orchestrator = module("base008_orchestrator", ROOT / "scripts/orchestrate.py")
        with tempfile.TemporaryDirectory(prefix="judge-base008-orchestrator-") as tmp:
            with patch.dict(os.environ, {"JUDGE_DEPLOYMENT_ID": "fixture", "SOURCE_AGENT": "reg-monitor"}), patch("pathlib.Path.cwd", return_value=Path(tmp)):
                store = self.paths.prepare(Path(tmp), "fixture", "reg-monitor")
                store.create("report.md", "FR_REPORT")
                good = {"channel": "C12345678", "report_path": self.paths.output_prefix("fixture", "reg-monitor") + "report.md"}
                self.assertTrue(orchestrator._validate_params("slack_send_message", good))
                for path in ("./out/report.md", "./judge-fr-eu-runs/original/reg-monitor/out/report.md", "./judge-fr-eu-runs/fixture/reg-monitor/out/../report.md"):
                    self.assertFalse(orchestrator._validate_params("slack_send_message", {**good, "report_path": path}))
                orchestrator.audit_log({"result": "fixture"})
                self.assertIn("fixture", store.read("handoff-audit.jsonl"))
                self.assertFalse((Path(tmp) / "out").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
