"""Contrôles documentaires DOM-004, sans exécution d'un skill.

python backlog/03-nouveaux-domaines/dom-004-annexes/dom-004-controles.py
Ajouter --baseline <instantane.json> pour contrôler les travaux préexistants.
Ajouter --output <rapport.json> pour conserver un relevé, jamais une preuve de droit.
L'instantané facultatif est un objet {"files": {chemin: sha256}, "git_head": ...}.
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
REPORT = ANNEXES / 'dom-004-resultats.json'
COMMON = {'DOM-004', 'PILOTE-003', 'BASE-005', 'BASE-006'}
LOT_DOCS = [HERE / 'dom-004-banque.md'] + [ANNEXES / ('dom-004-' + n + '.md') for n in (
    'decoupage-banque', 'verification', 'frictions-utilisateurs')]
FRICTION_SOURCE = HERE / 'sources/banques-frictions-2026-10-16.txt'
FRICTION_RELAYS = [HERE / name for name in (
    'dom-005-assurance.md', 'dom-005-annexes/dom-005-decoupage-assurance.md',
    'dom-016-successions-donations.md', 'dom-024-dettes-surendettement.md',
    'suites/enf-004-saisie-compte.md', 'suites/ins-008-assurance-emprunteur.md',
    'suites/ins-011-assurance-vie-beneficiaire.md', 'suites/ins-012-rachat-assurance-vie.md')]
ALLOWED = {
    'backlog/README.md',
    'backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md',
    *(p.relative_to(ROOT).as_posix() for p in LOT_DOCS),
    'backlog/03-nouveaux-domaines/dom-004-annexes/dom-004-controles.py',
    'backlog/03-nouveaux-domaines/dom-004-annexes/dom-004-resultats.json',
    *(p.relative_to(ROOT).as_posix() for p in FRICTION_RELAYS),
    FRICTION_SOURCE.relative_to(ROOT).as_posix(),
    'backlog/03-nouveaux-domaines/dom-005-annexes/dom-005-controles.py',
    'backlog/03-nouveaux-domaines/dom-005-annexes/dom-005-resultats.json',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    return {
        p.relative_to(ROOT).as_posix(): digest(p)
        for p in ROOT.rglob('*') if p.is_file()
        and '.git' not in p.relative_to(ROOT).parts
        and '__pycache__' not in p.parts
        and p != REPORT
    }


def frontmatter(path):
    return yaml.safe_load(path.read_text(encoding='utf-8').split('---', 2)[1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--concurrent', action='append', default=[],
                        help='Motif glob de fichiers modifiés par un autre lot pendant la tâche.')
    args = parser.parse_args()
    checks = {}

    def record(name, problems, **facts):
        checks[name] = {'status': 'failed' if problems else 'passed',
                        **facts, 'problems': problems}

    stories, problems = {}, []
    for p in sorted((ROOT / 'backlog').rglob('*.md')):
        txt = p.read_text(encoding='utf-8')
        if not txt.startswith('---\n'):
            continue
        try:
            fm = yaml.safe_load(txt.split('---', 2)[1])
            ident = fm['id']
            if ident in stories:
                problems.append(f'duplicate: {ident}')
            for key in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
                if key not in fm:
                    problems.append(f'{ident}: missing {key}')
            if not isinstance(fm.get('dependances'), list):
                problems.append(f'{ident}: dependencies must be a list')
                fm['dependances'] = []
            stories[ident] = (p, fm)
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{p.relative_to(ROOT)}: {exc}')
    for ident, (_, fm) in stories.items():
        for dep in fm['dependances']:
            if dep not in stories:
                problems.append(f'{ident}: missing dependency {dep}')
    active, done = set(), set()

    def visit(ident):
        if ident in active:
            problems.append(f'dependency cycle at {ident}')
            return
        if ident in done or ident not in stories:
            return
        active.add(ident)
        for dep in stories[ident][1]['dependances']:
            visit(dep)
        active.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    statuses = Counter(x[1]['statut'] for x in stories.values())
    record('backlog_frontmatter_and_dependencies', problems,
           total=len(stories), statuses=dict(statuses))

    proposals = sorted((HERE / 'suites').glob('bnk-*.md'))
    for p in proposals:
        ALLOWED.add(p.relative_to(ROOT).as_posix())
    expected = {f'BNK-{i:03}' for i in range(1, 20)}
    actual = {k for k in stories if k.startswith('BNK-')}
    problems = []
    if actual != expected or len(proposals) != 19:
        problems.append('Expected exactly BNK-001..BNK-019 and 19 files')
    required = ('Objectif et résultat attendu', 'Périmètre et fichiers',
                'Pièces et informations nécessaires', 'Sortie attendue',
                'Travail attendu', 'Références métier et sources à rechercher',
                "Critères d'acceptation", 'Vérification', 'Hors périmètre')
    targets, future_owners, unmarked, skills = {}, {}, [], {}
    for p in proposals:
        txt = p.read_text(encoding='utf-8')
        fm = frontmatter(p)
        ident = fm['id']
        if fm.get('statut') != 'proposee' or fm.get('nature') != 'implementation':
            problems.append(f'{ident}: expected implementation/proposee')
        if not COMMON <= set(fm['dependances']):
            problems.append(f'{ident}: missing common dependency')
        for heading in required:
            if f'## {heading}\n' not in txt:
                problems.append(f'{ident}: missing section {heading}')
        if '- Cas normal :' not in txt or '- Cas limite :' not in txt:
            problems.append(f'{ident}: missing scenarios')
        if '**attendus, non exécutés**' not in txt:
            problems.append(f'{ident}: scenarios not marked as not executed')
        rows = re.findall(r'^- `([^`]+)`([^\n]*)', txt, re.M)
        if not rows:
            problems.append(f'{ident}: no file targets')
        for name, suffix in rows:
            targets.setdefault(name, []).append(ident)
            exists = (ROOT / name).is_file()
            if '(à créer)' in suffix:
                future_owners.setdefault(name, []).append(ident)
                if exists:
                    problems.append(f'{ident}: future file already exists {name}')
            elif not exists:
                unmarked.append((ident, name))
            match = re.match(r'banking-legal/skills/([^/]+)/SKILL\.md$', name)
            if match:
                skills[ident] = match.group(1)
    for name, owners in future_owners.items():
        if len(owners) != 1:
            problems.append(f'{name}: multiple owners {owners}')
    def ancestors(ident, seen=None):
        seen = set() if seen is None else seen
        for dep in stories[ident][1]['dependances']:
            if dep not in seen and dep in stories:
                seen.add(dep)
                ancestors(dep, seen)
        return seen

    for ident, name in unmarked:
        if name not in future_owners:
            problems.append(f'{ident}: missing file without creating story {name}')
        elif future_owners[name][0] not in ancestors(ident):
            problems.append(f'{ident}: {name} created by a story it does not depend on')
    record('bounded_proposals', problems, count=len(proposals),
           file_targets=len(targets),
           future_files=[{'path': p, 'owner': o[0]} for p, o in future_owners.items()])

    breakdown = (ANNEXES / 'dom-004-decoupage-banque.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| (\d) \| \[(BNK-\d{3})\]\(\.\./suites/([^)]+)\) \| `([^`]+)` \| [^|]+ \| ([^|]+) \|$',
                      breakdown, re.M)
    problems = []
    if {r[1] for r in rows} != expected:
        problems.append('Breakdown table does not list exactly BNK-001..019')
    for rank, ident, filename, skill, deps in rows:
        path, fm = stories[ident]
        if path.name != filename:
            problems.append(f'{ident}: table links {filename}, file is {path.name}')
        if skills.get(ident) != skill:
            problems.append(f'{ident}: table skill {skill} differs from SKILL.md target')
        listed = set() if deps.strip() == 'Aucune' else {d.strip() for d in deps.split(',')}
        business = set(fm['dependances']) - COMMON - {'BASE-008'}
        if listed != business:
            problems.append(f'{ident}: table dependencies {sorted(listed)} != {sorted(business)}')
        expected_priority = 'P3' if rank == '4' else 'P2'
        if fm['priorite'] != expected_priority:
            problems.append(f'{ident}: rank {rank} expects {expected_priority}')
    record('breakdown_table_consistency', problems, rows=len(rows))

    matrix = (ANNEXES / 'dom-004-frictions-utilisateurs.md').read_text(encoding='utf-8')
    friction_rows = re.findall(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$', matrix, re.M)
    problems = []
    if [int(row[0]) for row in friction_rows] != list(range(1, 100)):
        problems.append('Friction matrix must list each input point 1..99 exactly once in order')
    for number, situation, owners, result in friction_rows:
        links = re.findall(r'\[([A-Z]+-\d{3})\]\(([^)]+)\)', owners)
        if not links or not situation.strip() or not result.strip():
            problems.append(f'Friction {number}: missing owner, situation or result')
        for ident, target in links:
            if ident not in stories or (ANNEXES / target).resolve() != stories[ident][0].resolve():
                problems.append(f'Friction {number}: invalid owner link {ident}: {target}')
    if not FRICTION_SOURCE.is_file():
        problems.append('Missing archived user input')
    else:
        source = FRICTION_SOURCE.read_text(encoding='utf-8')
        # Numbered friction entries use escaped Markdown dots; later numbered
        # practical steps restart at 1 and are deliberately kept separately.
        numbered_part = source.split('## 10.', 1)[0]
        source_numbers = re.findall(r'^(\d+)\\\.', numbered_part, re.M)
        if [int(n) for n in source_numbers] != list(range(1, 100)):
            problems.append('Archived input does not contain the original 99 numbered points')
    record('user_frictions_traceability', problems, points=len(friction_rows),
           source_sha256=digest(FRICTION_SOURCE) if FRICTION_SOURCE.is_file() else None,
           note='Structural traceability only; no legal or functional validation')

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'banking-legal').exists():
        problems.append('banking-legal directory exists: no plugin may be created by DOM-004')
    names = [p['name'] for p in market['plugins']]
    if any('banking' in n for n in names):
        problems.append('banking plugin listed in marketplace')
    record('no_plugin_created', problems, marketplace_plugins=len(names))

    lot = LOT_DOCS + proposals + FRICTION_RELAYS + [ROOT / 'backlog/README.md',
                                  ROOT / 'backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md']
    problems, count = [], 0
    for p in lot:
        raw = p.read_bytes()
        txt = raw.decode('utf-8')
        if not raw.endswith(b'\n') or raw.endswith(b'\n\n') or raw.startswith(b'\xef\xbb\xbf'):
            problems.append(f'{p.name}: final newline or UTF-8 BOM')
        if b'\r' in raw:
            problems.append(f'{p.name}: CR line ending')
        if any(line.rstrip() != line for line in txt.splitlines()):
            problems.append(f'{p.name}: trailing whitespace')
        if '�' in txt:
            problems.append(f'{p.name}: replacement character')
        for label, target in re.findall(r'\[([^\]\n]+)\]\(([^)]+)\)', txt):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            count += 1
            dest = unquote(target.split('#', 1)[0])
            if not (p.parent / dest).exists():
                problems.append(f'{p.name}: broken link {label}: {target}')
    record('links_and_format', problems, markdown_files=len(lot), local_links=count)

    problems = []
    for p in LOT_DOCS + proposals + FRICTION_RELAYS:
        width = None
        for line in p.read_text(encoding='utf-8').splitlines():
            if not line.startswith('|'):
                width = None
                continue
            cells = len(re.sub(r'`[^`]*`', '', line).split('|')) - 2
            if width is None:
                width = cells
            elif cells != width:
                problems.append(f'{p.name}: table row width {cells} != {width}')
    record('table_column_counts', problems)

    index = (ROOT / 'backlog/ETAT.md').read_text(encoding='utf-8')
    base003 = (ROOT / 'backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md').read_text(encoding='utf-8')
    problems = []
    for name in ('decoupage-banque', 'verification'):
        if f'(03-nouveaux-domaines/dom-004-annexes/dom-004-{name}.md)' not in index:
            problems.append(f'Index missing {name}')
    match = re.search(r'\| Total \| (\d+) \|', index)
    if not match or int(match.group(1)) != len(stories):
        problems.append(f'Index total differs from {len(stories)}')
    match = re.search(r'\| À faire \| (\d+) \|', index)
    if not match or int(match.group(1)) != statuses['proposee']:
        problems.append(f"Index proposee count differs from {statuses['proposee']}")
    if '(../../03-nouveaux-domaines/dom-004-annexes/dom-004-decoupage-banque.md)' not in base003:
        problems.append('BASE-003 matrix row does not link the breakdown')
    for p in proposals:
        if f'(../suites/{p.name})' not in breakdown:
            problems.append(f'Proposal missing from breakdown: {p.name}')
    if stories['DOM-004'][1]['statut'] != 'terminee':
        problems.append('DOM-004 not terminee')
    if stories['PILOTE-003'][1]['statut'] != 'terminee':
        problems.append('Pilot prerequisite not satisfied')
    record('index_matrix_and_prerequisites', problems)

    figures = []
    for p in LOT_DOCS + proposals + FRICTION_RELAYS:
        for number, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            for hit in re.findall(r'\b\d+\s*(?:jours?|mois|ans?|semaines?|€|euros?)\b', line):
                figures.append({'file': p.name, 'line': number, 'text': hit})
    checks['figures_for_manual_review'] = {
        'status': 'manual-review', 'count': len(figures), 'occurrences': figures,
        'note': 'Durées ou montants à relire : chaque occurrence doit être un fait fictif, jamais une règle.'}

    now = snapshot()
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding='utf-8'))
        before = baseline['files']
        changes = sorted(k for k in before.keys() | now.keys() if before.get(k) != now.get(k))
        concurrent = [k for k in changes if k not in ALLOWED
                      and any(PurePosixPath(k).match(g) for g in args.concurrent)]
        violations = [k for k in changes if k not in ALLOWED and k not in concurrent]
        preserved = [k for k in before if k not in ALLOWED and now.get(k) == before[k]]
        record('scope_vs_task_baseline', violations, baseline_git_head=baseline.get('git_head'),
               lot_changes=[k for k in changes if k in ALLOWED],
               concurrent_patterns=args.concurrent, concurrent_changes=concurrent,
               preserved_files=len(preserved), report_excluded_from_own_comparison=True,
               note=('Les fichiers du lot partagés (index, BASE-003) peuvent aussi porter '
                     'des changements concurrents ; le contrôle ne les attribue pas.'))
    else:
        checks['scope_vs_task_baseline'] = {
            'status': 'not-run', 'reason': 'Provide --baseline to compare pre-existing uncommitted work.'}

    json_paths = [p for p in ROOT.rglob('*.json') if '.git' not in p.relative_to(ROOT).parts]
    problems = []
    for p in json_paths:
        try:
            json.loads(p.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError) as exc:
            problems.append(f'{p.relative_to(ROOT)}: {exc}')
    record('repository_json_sanity', problems, files=len(json_paths))
    lint = subprocess.run([sys.executable, '-X', 'utf8', 'scripts/lint-tool-scope.py'],
                          cwd=ROOT, capture_output=True, encoding='utf-8')
    record('cookbook_tool_scope_lint', [] if lint.returncode == 0 else [lint.stderr or lint.stdout],
           exit_code=lint.returncode)
    whitespace = subprocess.run(['git', 'diff', '--check'], cwd=ROOT,
                                capture_output=True, encoding='utf-8')
    record('git_diff_check', [] if whitespace.returncode == 0 else [whitespace.stdout or whitespace.stderr],
           exit_code=whitespace.returncode)

    report = {
        'story': 'DOM-004', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'cadrage documentaire bancaire ; aucun plugin créé ni validation juridique',
        'checks': checks,
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in lot + [Path(__file__), FRICTION_SOURCE]},
        'not_run': ['recherche juridique externe', 'calcul de délai, de décompte ou de montant',
                    'création ou exécution de skill', 'installation/recette client',
                    'lecteur réel ou indépendant', 'connexion/envoi/publication'],
        'commands': [
            [sys.executable, '-X', 'utf8', str(Path(__file__).relative_to(ROOT)), *sys.argv[1:]],
            'python -X utf8 scripts/lint-tool-scope.py (appelé par le contrôleur)',
            'git diff --check (appelé par le contrôleur)',
        ],
        'execution_notes': [
            'Relevé actualisé lors de l’intégration des 99 frictions utilisateur et des huit nouvelles propositions BNK/INS.',
            'Contrôle de périmètre exécuté seulement si un instantané --baseline est fourni ; voir le résultat dédié.',
            'Montants fictifs et affirmations du texte utilisateur ne valent pas règles vérifiées ; scénarios métier non exécutés.',
        ],
    }
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    for key, val in checks.items():
        print(f"{key}: {val['status']}")
        for problem in val.get('problems', []):
            print(f'  {problem}')
    raise SystemExit(1 if any(x['status'] == 'failed' for x in checks.values()) else 0)


if __name__ == '__main__':
    main()
