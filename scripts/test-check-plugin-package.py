#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Disposable installed-artifact fixtures for BASE-006; no skill execution."""

import contextlib
import importlib.util
import io
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("package_check", SCRIPTS / "check-plugin-package.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InstalledArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="judge-base006-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "installed" / "demo-legal"
        self.write(".claude-plugin/plugin.json", json.dumps({
            "name": "demo-legal", "version": "1.0.0", "description": "Fixture BASE-006"
        }))
        self.write("CLAUDE.md", "# Modèle de profil factice\n")
        self.write("README.md", "# Fixture\nUtiliser `/demo-legal:review`.\n")
        self.write("references/rules.md", "# Pièces à examiner\n")
        self.write("skills/review/SKILL.md", """---
name: review
description: >
  Examiner une pièce fictive.
---
# /review
Charger [les pièces](../../references/rules.md).
Charger `../../references/shared/research-citation-method.md`.
""")
        method = self.root / MODULE.METHOD
        method.parent.mkdir(parents=True)
        # Copy unchanged: provenance/examples in the real BASE-005 method must
        # not become fake runtime dependencies on the checkout.
        shutil.copyfile(SCRIPTS.parent / "references/research-citation-method.md", method)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def check(self):
        checker = MODULE.Checker(self.root)
        checker.run()
        return checker

    def cli(self, *arguments, env=None):
        output = io.StringIO()
        environ = {k: v for k, v in os.environ.items() if k != "JUDGE_CLAUDE_CLI"}
        environ.update(env or {})
        with patch.dict(os.environ, environ, clear=True),                 patch("sys.argv", ["check-plugin-package.py", str(self.root), *arguments]):
            with contextlib.redirect_stdout(output):
                code = MODULE.main()
        return code, output.getvalue()

    def test_standalone_package_with_real_method(self):
        self.assertFalse(self.root.is_relative_to(SCRIPTS.parent))
        checker = self.check()
        self.assertEqual(checker.errors, [])
        self.assertEqual(checker.reviews, [])
        code, output = self.cli()
        self.assertEqual(code, 0)
        self.assertIn("SCHEMA NON_EXECUTE", output)
        self.assertIn("EXECUTION_SKILL NON_EXECUTEE", output)

    def test_removed_embedded_reference_fails_even_if_source_exists(self):
        self.write("references/source-only.md", "# Source non livrée\n")
        source = Path(self.temporary.name) / "checkout" / "source-only.md"
        source.parent.mkdir()
        (self.root / "references/source-only.md").replace(source)
        self.write("skills/review/SKILL.md", "---\ndescription: Revue\n---\n"
                   "Lire [source](../../references/source-only.md).\n")
        code, output = self.cli()
        self.assertEqual(code, 1)
        self.assertIn("référence absente du paquet: ../../references/source-only.md", output)

    def test_typo_command_fails(self):
        self.write("README.md", "Exécuter `/demo-legal:revue-inexistante`.\n")
        code, output = self.cli()
        self.assertEqual(code, 1)
        self.assertIn("commande inexistante dans le paquet: /demo-legal:revue-inexistante", output)

    def test_command_file_and_builtin_are_distinguished(self):
        self.write("commands/diagnostic.md", "---\ndescription: Diagnostic\n---\n# /diagnostic\n")
        self.write("README.md", "Lancer `/diagnostic`, `/plugin` et `/mcp`.\n")
        self.assertEqual(self.check().errors, [])

    def test_other_plugin_is_manual_review(self):
        self.write("README.md", "Orientation facultative : `/other-legal:review`.\n")
        code, output = self.cli()
        self.assertEqual(code, 2)
        self.assertIn("commande d'un autre plugin à qualifier", output)

    def test_escape_and_missing_reference_definition(self):
        self.write("README.md", "[sortie](../checkout/secret.md)\n"
                   "[pièce][preuve]\n[preuve]: references/absent.md\n")
        errors = "\n".join(self.check().errors)
        self.assertIn("référence hors paquet", errors)
        self.assertIn("référence absente du paquet: references/absent.md", errors)

    def test_frontmatter_parse_and_manifest_entry_point(self):
        self.write("skills/review/SKILL.md", "---\ndescription: [inachevée\n---\n")
        manifest = json.loads((self.root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        manifest["agents"] = "./agents/absent.md"
        self.write(".claude-plugin/plugin.json", json.dumps(manifest))
        errors = "\n".join(self.check().errors)
        self.assertIn("frontmatter YAML invalide", errors)
        self.assertIn("référence absente du paquet: ./agents/absent.md", errors)

    def test_dynamic_profile_does_not_pass_silently(self):
        self.write("README.md", "Lire `~/.claude/plugins/config/origine/profil.md`.\n")
        code, output = self.cli()
        self.assertEqual(code, 2)
        self.assertIn("chemin dynamique/profil à éprouver", output)

    def test_schema_tool_absence_is_not_success(self):
        with patch.object(MODULE.shutil, "which", return_value=None):
            code, output = self.cli("--schema")
        self.assertEqual(code, 2)
        self.assertIn("SCHEMA NON_EXECUTE: CLI claude absente", output)
        self.assertNotIn("SCHEMA OK", output)

    def test_schema_invocation_uses_artifact_as_working_directory(self):
        with patch.object(MODULE.shutil, "which", return_value="fake-claude"):
            with patch.object(MODULE.subprocess, "run") as run:
                run.return_value.returncode = 1
                code, output = self.cli("--schema")
        self.assertEqual(code, 1)
        self.assertEqual(run.call_args.kwargs["cwd"], self.root.resolve())
        self.assertEqual(run.call_args.args[0][-1], str(self.root.resolve()))
        self.assertIn("SCHEMA ECHEC", output)

    def test_explicit_cli_path_is_used_without_path_lookup(self):
        fake = Path(self.temporary.name) / "bin" / "claude.exe"
        fake.parent.mkdir()
        fake.write_text("", encoding="utf-8")
        for arguments, env, origin in ((("--claude", str(fake)), None, "--claude"),
                                       ((), {"JUDGE_CLAUDE_CLI": str(fake)}, "JUDGE_CLAUDE_CLI")):
            with self.subTest(origin=origin),                     patch.object(MODULE.shutil, "which", return_value=None) as which,                     patch.object(MODULE.subprocess, "run") as run:
                run.return_value.returncode = 0
                code, output = self.cli("--schema", *arguments, env=env)
            self.assertEqual(run.call_args.args[0][0], str(fake))
            self.assertIn(f"SCHEMA CLI: {fake} ({origin})", output)
            self.assertIn("SCHEMA OK", output)
            which.assert_not_called()
            self.assertEqual(code, 0)

    def test_missing_explicit_cli_is_not_success(self):
        missing = Path(self.temporary.name) / "absent" / "claude.exe"
        with patch.object(MODULE.shutil, "which", return_value="fake-claude"),                 patch.object(MODULE.subprocess, "run") as run:
            code, output = self.cli("--schema", env={"JUDGE_CLAUDE_CLI": str(missing)})
        run.assert_not_called()
        self.assertEqual(code, 2)
        self.assertIn("SCHEMA NON_EXECUTE: CLI indiquée introuvable (JUDGE_CLAUDE_CLI)", output)

    def test_missing_yaml_is_not_success(self):
        with patch.object(MODULE, "yaml", None):
            code, output = self.cli()
        self.assertEqual(code, 2)
        self.assertIn("NON_EXECUTE structure: PyYAML absent", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
