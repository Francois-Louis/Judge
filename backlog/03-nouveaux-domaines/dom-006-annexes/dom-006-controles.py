"""Contrôles statiques du cadrage DOM-006, sans validation du droit.

python -X utf8 backlog/03-nouveaux-domaines/dom-006-annexes/dom-006-controles.py
Utiliser --output <fichier.json> pour enregistrer le relevé initial du lot.
Un relevé daté n'est pas à réécrire lors d'une extension ultérieure.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[3]
ANNEXES = Path(__file__).resolve().parent
HERE = ANNEXES.parent
COMMON = {'DOM-006', 'PILOTE-003', 'BASE-005', 'BASE-006'}
EXPECTED = {f'LOG-{n:03}' for n in range(1, 12)}
STORY = HERE / 'dom-006-logement.md'
BREAKDOWN = ANNEXES / 'dom-006-decoupage-logement.md'
REPORT = ANNEXES / 'dom-006-resultats.json'
SHARED = [
    ROOT / 'backlog/ETAT.md', ROOT / 'backlog/etat.py',
    ROOT / 'backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md',
    HERE / 'suites/enf-005-expulsion.md',
    ROOT / 'backlog/02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md',
]


def run(*command):
    return subprocess.run(command, cwd=ROOT, capture_output=True, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--context', default='working-tree',
                        help='Contexte de validation indiqué dans le relevé.')
    parser.add_argument('--concurrent', action='append', default=[],
                        help='Glob de chemins hors lot observés en cours de tâche.')
    args = parser.parse_args()
    checks = {}

    def record(name, problems, **facts):
        checks[name] = {'status': 'failed' if problems else 'passed',
                        **facts, 'problems': problems}

    stories, problems = {}, []
    for path in sorted((ROOT / 'backlog').rglob('*.md')):
        txt = path.read_text(encoding='utf-8')
        if not txt.startswith('---\n'):
            continue
        try:
            fm = yaml.safe_load(txt.split('---', 2)[1])
            ident = fm['id']
            if ident in stories:
                problems.append(f'Duplicate ID: {ident}')
            for key in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
                if key not in fm:
                    problems.append(f'{ident}: missing {key}')
            if not isinstance(fm.get('dependances'), list):
                problems.append(f'{ident}: dependencies must be a list')
                fm['dependances'] = []
            stories[ident] = (path, fm)
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{path.relative_to(ROOT)}: {exc}')

    active, done = set(), set()

    def visit(ident):
        if ident not in stories:
            problems.append(f'Missing dependency: {ident}')
            return
        if ident in active:
            problems.append(f'Dependency cycle: {ident}')
            return
        if ident in done:
            return
        active.add(ident)
        for dep in stories[ident][1]['dependances']:
            visit(dep)
        active.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    record('backlog_metadata_dependencies', problems, total=len(stories),
           statuses=dict(Counter(fm['statut'] for _, fm in stories.values())))

    proposals = sorted((HERE / 'suites').glob('log-*.md'))
    problems, skills, owners, reused = [], {}, {}, []
    actual = {ident for ident in stories if ident.startswith('LOG-')}
    if actual != EXPECTED or len(proposals) != 11:
        problems.append('Expected exactly LOG-001..011 and eleven files')
    required = ('Objectif et résultat attendu', 'Périmètre et fichiers',
                'Pièces et informations nécessaires', 'Sortie attendue',
                'Travail attendu', 'Références métier et sources à rechercher',
                "Critères d'acceptation", 'Vérification', 'Hors périmètre')
    for path in proposals:
        txt = path.read_text(encoding='utf-8')
        fm = yaml.safe_load(txt.split('---', 2)[1])
        ident = fm['id']
        if fm['statut'] != 'proposee' or fm['nature'] != 'implementation':
            problems.append(f'{ident}: expected implementation/proposee')
        if not COMMON <= set(fm['dependances']):
            problems.append(f'{ident}: missing common dependency')
        for heading in required:
            if f'## {heading}\n' not in txt:
                problems.append(f'{ident}: missing section {heading}')
        for marker in ('- Cas normal :', '- Cas limite :', '**attendus, non exécutés**',
                       'BASE-006', 'BASE-013', 'Phrase finale' if ident not in
                       {'LOG-009', 'LOG-010'} else 'phrase finale'):
            if marker not in txt:
                problems.append(f'{ident}: missing {marker}')
        targets = re.findall(r'^- `([^`]+)`([^\n]*)', txt, re.M)
        skill_targets = []
        for name, suffix in targets:
            target = ROOT / name
            if '(à créer)' in suffix:
                owners.setdefault(name, []).append(ident)
                if target.exists():
                    problems.append(f'{ident}: future file already exists: {name}')
            elif not target.is_file():
                reused.append((ident, name))
            match = re.fullmatch(r'housing-legal/skills/([^/]+)/SKILL\.md', name)
            if match:
                skill_targets.append(match[1])
        if len(skill_targets) != 1:
            problems.append(f'{ident}: expected one skill target')
        else:
            skills[ident] = skill_targets[0]
    for name, ids in owners.items():
        if len(ids) != 1:
            problems.append(f'{name}: multiple creating stories: {ids}')

    def ancestors(ident, seen=None):
        seen = set() if seen is None else seen
        for dep in stories[ident][1]['dependances']:
            if dep in stories and dep not in seen:
                seen.add(dep)
                ancestors(dep, seen)
        return seen

    for ident, name in reused:
        if name not in owners or owners[name][0] not in ancestors(ident):
            problems.append(f'{ident}: no dependency creates {name}')
    record('bounded_proposals_and_future_files', problems, count=len(proposals),
           skills=skills, future_file_owners=owners)

    txt = BREAKDOWN.read_text(encoding='utf-8')
    rows = re.findall(r'^\| (\d) \| \[(LOG-\d{3})\]\(\.\./suites/([^)]+)\) \| `([^`]+)` \| [^|]+ \| ([^|]+) \|$', txt, re.M)
    problems = []
    if {r[1] for r in rows} != EXPECTED or len(rows) != 11:
        problems.append('Breakdown must list each proposal exactly once')
    for rank, ident, filename, skill, deps in rows:
        path, fm = stories[ident]
        if path.name != filename or skills.get(ident) != skill:
            problems.append(f'{ident}: file or skill mismatch in breakdown')
        listed = set() if deps.strip() == 'Aucune' else {d.strip() for d in deps.split(',')}
        if listed != set(fm['dependances']) - COMMON - {'BASE-008'}:
            problems.append(f'{ident}: business dependencies mismatch')
        if fm['priorite'] != ('P3' if rank == '4' else 'P2'):
            problems.append(f'{ident}: priority mismatch')
    record('breakdown_consistency', problems, rows=len(rows))

    lot = [STORY, BREAKDOWN, ANNEXES / 'dom-006-verification.md',
           Path(__file__), *proposals, *SHARED]
    problems, links = [], 0
    for path in lot:
        raw = path.read_bytes()
        txt = raw.decode('utf-8')
        if not raw.endswith(b'\n') or raw.endswith(b'\n\n') or raw.startswith(b'\xef\xbb\xbf'):
            problems.append(f'{path.name}: final newline or BOM')
        if any(line.rstrip() != line for line in txt.splitlines()) or '\ufffd' in txt:
            problems.append(f'{path.name}: whitespace or replacement character')
        if path.suffix != '.md':
            continue
        width = None
        for line in txt.splitlines():
            if not line.startswith('|'):
                width = None
                continue
            cells = len(re.sub(r'`[^`]*`', '', line).split('|')) - 2
            if width is not None and cells != width:
                problems.append(f'{path.name}: table width mismatch')
            width = cells
        for label, target in re.findall(r'\[([^\]\n]+)\]\(([^)]+)\)', txt):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            links += 1
            if not (path.parent / unquote(target.split('#', 1)[0])).exists():
                problems.append(f'{path.name}: broken link {label}: {target}')
    record('links_format_and_tables', problems, files=len(lot), local_links=links)

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'housing-legal').exists() or any('housing' in p['name'] for p in market['plugins']):
        problems.append('DOM-006 must not create or register a plugin')
    record('no_plugin_created', problems, marketplace_plugins=len(market['plugins']))

    index_check = run(sys.executable, '-X', 'utf8', 'backlog/etat.py', '--check')
    index = SHARED[0].read_text(encoding='utf-8')
    problems = [] if index_check.returncode == 0 else [index_check.stdout or index_check.stderr]
    for path in [STORY, *proposals, BREAKDOWN, ANNEXES / 'dom-006-verification.md', REPORT]:
        if path.relative_to(ROOT / 'backlog').as_posix() not in index:
            problems.append(f'Index missing {path.name}')
    if stories['DOM-006'][1]['statut'] != 'terminee' or stories['PILOTE-003'][1]['statut'] != 'terminee':
        problems.append('DOM-006 or pilot status mismatch')
    if '(../../03-nouveaux-domaines/dom-006-annexes/dom-006-decoupage-logement.md)' not in SHARED[2].read_text(encoding='utf-8'):
        problems.append('BASE-003 missing breakdown link')
    for path, marker in ((SHARED[3], '(log-009-delais-clause-resolutoire.md)'),
                         (SHARED[4], '(../../03-nouveaux-domaines/suites/log-011-justificatifs-candidature.md)')):
        if marker not in path.read_text(encoding='utf-8'):
            problems.append(f'{path.name}: missing housing relay')
    record('index_matrix_relays_and_pilot', problems)

    allowed = {p.relative_to(ROOT).as_posix() for p in [*lot, REPORT]}
    diff = run('git', '-c', 'core.quotepath=false', 'diff', '--name-only', 'HEAD', '--')
    untracked = run('git', '-c', 'core.quotepath=false', 'ls-files', '--others', '--exclude-standard')
    changed = sorted(set(diff.stdout.splitlines()) | set(untracked.stdout.splitlines()))
    concurrent = [p for p in changed if p not in allowed
                  and any(PurePosixPath(p).match(pattern) for pattern in args.concurrent)]
    problems = [p for p in changed if p not in allowed and p not in concurrent]
    for result in (diff, untracked):
        if result.returncode:
            problems.append(result.stderr)
    record('git_task_scope', problems, lot_files=[p for p in changed if p in allowed],
           concurrent_files=concurrent, concurrent_patterns=args.concurrent,
           note=('Checkout propre observé avant édition ; changements DOM-007 apparus '
                 'en parallèle. Le contrôle des chemins ne remplace pas la relecture '
                 'du diff et du contenu indexé des fichiers partagés.'))

    problems, json_files = [], 0
    for path in ROOT.rglob('*.json'):
        if '.git' in path.relative_to(ROOT).parts:
            continue
        json_files += 1
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError) as exc:
            problems.append(f'{path.relative_to(ROOT)}: {exc}')
    record('repository_json_sanity', problems, files=json_files)
    for name, command in (
        ('cookbook_tool_scope_lint', [sys.executable, '-X', 'utf8', 'scripts/lint-tool-scope.py']),
        ('git_diff_check', ['git', 'diff', '--check']),
    ):
        result = run(*command)
        record(name, [] if result.returncode == 0 else [result.stdout or result.stderr],
               exit_code=result.returncode)

    report = {
        'story': 'DOM-006', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': run('git', 'rev-parse', 'HEAD').stdout.strip(),
        'scope': 'cadrage documentaire logement ; aucun plugin ni règle juridique validée',
        'validation_context': args.context,
        'checks': checks,
        'lot_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in lot},
        'not_run': ['recherche juridique externe', 'scénarios exécutables de skills',
                    'installation ou invocation client', 'lecteur réel ou indépendant',
                    'validation de schéma ou de paquet housing absent',
                    'calcul de délai ou montant juridique', 'envoi ou saisine'],
        'command': [sys.executable, '-X', 'utf8', str(Path(__file__).relative_to(ROOT)), *sys.argv[1:]],
    }
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                               encoding='utf-8', newline='\n')
    for name, result in checks.items():
        print(f"{name}: {result['status']}")
        for problem in result['problems']:
            print(f'  {problem}')
    return 1 if any(r['status'] == 'failed' for r in checks.values()) else 0


if __name__ == '__main__':
    raise SystemExit(main())
