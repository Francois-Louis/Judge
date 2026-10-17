#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""BASE-006: bounded static checks against ONE installed/extracted plugin.

Requires PyYAML, like lint-tool-scope.py. No checkout lookup, network, installer,
profile access or execution of package code. See references/package-validation.md.
Exit 0: static checks passed; 1: defects; 2: incomplete checks/manual review.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    yaml = None


BUILTINS = {"mcp", "plugin", "help", "clear", "compact"}
NAME = re.compile(r"[a-z0-9][a-z0-9-]{1,63}\Z")
COMMAND = re.compile(r"/((?:[a-z0-9][a-z0-9-]*:)?[a-z0-9][a-z0-9-]*)(?:\s.*)?\Z")
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
DEFINITION = re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>]+>|\S+)", re.M)
CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
METHOD = "references/shared/research-citation-method.md"


class Checker:
    def __init__(self, root: Path):
        self.supplied_root = root.absolute()
        self.root = root.resolve()
        self.errors: list[str] = []
        self.reviews: list[str] = []
        self.markdown_count = 0

    def label(self, path):
        return path.relative_to(self.root).as_posix()

    def error(self, path, message):
        self.errors.append(f"{self.label(path)}: {message}")

    def review(self, path, message):
        self.reviews.append(f"{self.label(path)}: {message}")

    def local_path(self, origin, target, *, package_relative=False):
        target = unquote(target.strip("<>"))
        if not target or target.startswith("#"):
            return
        if target.startswith("${CLAUDE_PLUGIN_ROOT}/"):
            target = target.removeprefix("${CLAUDE_PLUGIN_ROOT}/")
            package_relative = True
        if target.startswith("//") or re.match(r"^[A-Za-z]:[\\/]", target):
            self.error(origin, f"chemin externe au paquet: {target}")
            return
        parsed = urlsplit(target)
        if parsed.scheme in {"https", "http", "mailto", "tel"}:
            return  # Availability/content belongs to the scenario review.
        if parsed.scheme:
            self.review(origin, f"URI à qualifier manuellement: {target}")
            return
        if any(token in target for token in ("~", "$", "*", "<", ">", "{", "}")):
            self.review(origin, f"chemin dynamique/profil à éprouver: {target}")
            return
        relative = parsed.path.replace("\\", "/")
        base = self.root if package_relative else origin.parent
        candidate = (base / relative).resolve()
        if not candidate.is_relative_to(self.root):
            self.error(origin, f"référence hors paquet: {target}")
        elif not candidate.exists():
            self.error(origin, f"référence absente du paquet: {target}")

    def frontmatter(self, path, text):
        lines = text.splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            self.error(path, "frontmatter absent ou non fermé")
            return {}
        try:
            data = yaml.safe_load("\n".join(lines[1:lines.index("---", 1)]))
        except yaml.YAMLError as exc:
            self.error(path, f"frontmatter YAML invalide: {exc}")
            return {}
        if not isinstance(data, dict):
            self.error(path, "frontmatter attendu sous forme d'objet")
            return {}
        return data

    def command(self, path, command, name, available):
        namespace, separator, short = command.partition(":")
        if separator and namespace != name:
            self.review(path, f"commande d'un autre plugin à qualifier: /{command}")
        elif (short if separator else namespace) not in available:
            if not separator and command in BUILTINS:
                return
            if (path.relative_to(self.root).as_posix() == "references/company-profile-template.md"
                    and command == "cold-start-interview"):
                self.review(path, "modèle partagé : /cold-start-interview absent ; vérifier que le parcours ne charge pas ce modèle")
            else:
                self.error(path, f"commande inexistante dans le paquet: /{command}")

    def run(self):
        if (self.supplied_root.is_symlink()
                or (hasattr(self.supplied_root, "is_junction") and self.supplied_root.is_junction())):
            self.errors.append("artefact: racine liée/jonction interdite")
            return
        if not self.root.is_dir():
            self.errors.append("artefact: répertoire absent")
            return
        # Reject links/junctions before reading anything, including broken links.
        paths = []
        pending = [self.root]
        while pending:
            directory = pending.pop()
            for path in sorted(directory.iterdir()):
                if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
                    self.error(path, "lien/jonction interdit dans l'artefact isolé")
                elif path.is_dir():
                    pending.append(path)
                else:
                    paths.append(path)
        if self.errors:
            return
        documents = {}
        for path in paths:
            if path.suffix == ".json":
                try:
                    documents[path] = json.loads(path.read_text(encoding="utf-8"))
                except (ValueError, UnicodeError) as exc:
                    self.error(path, f"JSON invalide: {exc}")
        manifest_path = self.root / ".claude-plugin/plugin.json"
        manifest = documents.get(manifest_path)
        if not isinstance(manifest, dict):
            self.error(manifest_path, "manifeste JSON objet requis")
            manifest = {}
        for field in ("name", "version", "description"):
            if not isinstance(manifest.get(field), str) or not manifest[field].strip():
                self.error(manifest_path, f"champ texte requis: {field}")
        name = manifest.get("name", "")
        if not isinstance(name, str) or not NAME.fullmatch(name):
            self.error(manifest_path, "nom de plugin non canonique")
        # Only file-valued entry points; inline hooks/MCP objects need schema review.
        for field in ("skills", "commands", "agents", "hooks", "mcpServers"):
            values = manifest.get(field, [])
            for value in values if isinstance(values, list) else [values]:
                if isinstance(value, str):
                    self.local_path(manifest_path, value, package_relative=True)
                    self.review(manifest_path, f"point d'entrée explicite {field} à confronter au schéma: {value}")
        for required in ("README.md", "CLAUDE.md", METHOD):
            if not (self.root / required).is_file():
                self.error(self.root / required, "fichier requis par le contrat BASE-003/005")
        available = set()
        for path in paths:
            rel = path.relative_to(self.root)
            if len(rel.parts) == 3 and rel.parts[0] == "skills" and rel.name == "SKILL.md":
                available.add(rel.parts[1])
            if len(rel.parts) == 2 and rel.parts[0] == "commands" and rel.suffix == ".md":
                available.add(rel.stem)
        for path in sorted(paths):
            if path.suffix != ".md":
                continue
            self.markdown_count += 1
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(self.root)
            is_skill = len(rel.parts) == 3 and rel.parts[0] == "skills" and rel.name == "SKILL.md"
            is_agent = len(rel.parts) == 2 and rel.parts[0] == "agents"
            is_command = len(rel.parts) == 2 and rel.parts[0] == "commands"
            if is_skill or is_agent or is_command:
                data = self.frontmatter(path, text)
                for field in ("name", "description") if is_agent else ("description",):
                    if not isinstance(data.get(field), str) or not data[field].strip():
                        self.error(path, f"frontmatter: champ texte requis {field}")
                if is_skill and "name" in data and data["name"] != path.parent.name:
                    self.error(path, "name du skill différent de son répertoire")
            if rel.as_posix() == METHOD:
                data = self.frontmatter(path, text)
                for field in ("id", "version", "origine", "source_edition"):
                    if not isinstance(data.get(field), str) or not data[field].strip():
                        self.error(path, f"méthode: métadonnée requise {field}")
            for match in (*LINK.finditer(text), *DEFINITION.finditer(text)):
                self.local_path(path, match[1])
            for match in CODE.finditer(text):
                token = match[1].strip()
                command = COMMAND.fullmatch(token)
                if command:
                    self.command(path, command[1], name, available)
                elif rel.as_posix() == METHOD:
                    # BASE-005 carries provenance and illustrative paths, explicitly
                    # not runtime imports. Its actual Markdown links remain checked.
                    continue
                elif (token.startswith(("./", "../", "${CLAUDE_PLUGIN_ROOT}/", "~/"))
                      or re.match(r"^(?:references|skills|agents|commands)/", token)):
                    # One literal path per code span. Prose/dynamic expressions
                    # are signalled instead of being guessed/resolved in checkout.
                    if any(c.isspace() for c in token):
                        self.review(path, f"expression de chemin à relire: {token}")
                    else:
                        self.local_path(path, token)
            for command in re.findall(r"^#{1,6}\s+/([a-z0-9][a-z0-9:-]*)\s*$", text, re.M):
                self.command(path, command, name, available)


def resolve_cli(explicit: Path | None) -> tuple[str | None, str]:
    """Pick the claude binary: --claude, then JUDGE_CLAUDE_CLI, then PATH."""
    origin = "--claude"
    if explicit is None and os.environ.get("JUDGE_CLAUDE_CLI"):
        explicit, origin = Path(os.environ["JUDGE_CLAUDE_CLI"]), "JUDGE_CLAUDE_CLI"
    if explicit is not None:
        if explicit.is_file():
            return str(explicit), origin
        return None, f"CLI indiquée introuvable ({origin}): {explicit}"
    found = shutil.which("claude")
    if found:
        return found, "PATH"
    return None, "CLI claude absente du PATH ; utiliser --claude ou JUDGE_CLAUDE_CLI"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="racine du seul plugin installé/extrait")
    parser.add_argument("--schema", action="store_true", help="appeler aussi claude plugin validate")
    parser.add_argument("--claude", type=Path,
                        help="binaire claude pour --schema (sinon JUDGE_CLAUDE_CLI, puis PATH)")
    args = parser.parse_args()
    if yaml is None:
        print("NON_EXECUTE structure: PyYAML absent (python -m pip install PyYAML)")
        return 2
    checker = Checker(args.artifact)
    try:
        checker.run()
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"NON_EXECUTE structure: {exc}")
        return 2
    for message in sorted(set(checker.errors)):
        print(f"ECHEC {message}")
    for message in sorted(set(checker.reviews)):
        print(f"A_RELIRE {message}")
    state = "ECHEC" if checker.errors else "INCOMPLET" if checker.reviews else "OK"
    print(f"STRUCTURE {state}: {checker.markdown_count} fichiers Markdown; contrôle statique borné")
    schema_failed = schema_missing = False
    executable, origin = resolve_cli(args.claude) if args.schema else (None, "")
    if args.schema and executable and not checker.errors and checker.root.is_dir():
        print(f"SCHEMA CLI: {executable} ({origin})", flush=True)
        try:
            result = subprocess.run([executable, "plugin", "validate", str(checker.root)],
                                    cwd=checker.root, check=False, timeout=120)
            schema_failed = result.returncode != 0
            print(f"SCHEMA {'ECHEC' if schema_failed else 'OK'}: code {result.returncode}")
        except (OSError, subprocess.TimeoutExpired) as exc:
            schema_missing = True
            print(f"SCHEMA NON_EXECUTE/INTERROMPU: {exc}")
    else:
        schema_missing = args.schema
        reason = origin if args.schema and not executable else "non demandé ou structure en échec"
        print(f"SCHEMA NON_EXECUTE: {reason}")
    print("EXECUTION_SKILL NON_EXECUTEE; COMPORTEMENT_JURIDIQUE NON_EVALUE")
    return 1 if checker.errors or schema_failed else 2 if checker.reviews or schema_missing else 0


if __name__ == "__main__":
    sys.exit(main())
