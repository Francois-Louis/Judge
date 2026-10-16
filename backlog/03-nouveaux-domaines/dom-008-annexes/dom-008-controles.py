"""Contrôles documentaires DOM-008, sans exécution d'un skill.

python backlog/03-nouveaux-domaines/dom-008-annexes/dom-008-controles.py
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
REPORT = ANNEXES / 'dom-008-resultats.json'
COMMON = {'DOM-008', 'PILOTE-003', 'BASE-005', 'BASE-006', 'BASE-008'}
COUNT = 10
LOT_DOCS = [HERE / 'dom-008-transports.md'] + [ANNEXES / ('dom-008-' + n + '.md') for n in (
    'decoupage-transports', 'verification')]
BASE003 = ROOT / 'backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md'
INDEX = ROOT / 'backlog/ETAT.md'
GENERATOR = ROOT / 'backlog/etat.py'
ALLOWED = {
    BASE003.relative_to(ROOT).as_posix(),
    INDEX.relative_to(ROOT).as_posix(),
    GENERATOR.relative_to(ROOT).as_posix(),
    *(p.relative_to(ROOT).as_posix() for p in LOT_DOCS),
    'backlog/03-nouveaux-domaines/dom-008-annexes/dom-008-controles.py',
    'backlog/03-nouveaux-domaines/dom-008-annexes/dom-008-resultats.json',
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

    proposals = sorted((HERE / 'suites').glob('tpt-*.md'))
    for p in proposals:
        ALLOWED.add(p.relative_to(ROOT).as_posix())
    expected = {f'TPT-{i:03}' for i in range(1, COUNT + 1)}
    actual = {k for k in stories if k.startswith('TPT-')}
    problems = []
    if actual != expected or len(proposals) != COUNT:
        problems.append(f'Expected exactly TPT-001..TPT-{COUNT:03} and {COUNT} files')
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
        criteria = txt.split("## Critères d'acceptation\n", 1)[-1].split('\n## ', 1)[0]
        if 'BASE-013' not in criteria:
            problems.append(f'{ident}: missing BASE-013 warning criterion')
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
            match = re.match(r'transport-legal/skills/([^/]+)/SKILL\.md$', name)
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

    breakdown = (ANNEXES / 'dom-008-decoupage-transports.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| (\d) \| \[(TPT-\d{3})\]\(\.\./suites/([^)]+)\) \| `([^`]+)` \| [^|]+ \| ([^|]+) \|$',
                      breakdown, re.M)
    problems = []
    if {r[1] for r in rows} != expected or len(rows) != COUNT:
        problems.append(f'Breakdown table does not list exactly TPT-001..{COUNT:03}')
    for rank, ident, filename, skill, deps in rows:
        if ident not in stories:
            continue
        path, fm = stories[ident]
        if path.name != filename:
            problems.append(f'{ident}: table links {filename}, file is {path.name}')
        if skills.get(ident) != skill:
            problems.append(f'{ident}: table skill {skill} differs from SKILL.md target')
        listed = set() if deps.strip() == 'Aucune' else {d.strip() for d in deps.split(',')}
        business = set(fm['dependances']) - COMMON
        if listed != business:
            problems.append(f'{ident}: table dependencies {sorted(listed)} != {sorted(business)}')
        expected_priority = 'P3' if rank == '4' else 'P2'
        if fm['priorite'] != expected_priority:
            problems.append(f'{ident}: rank {rank} expects {expected_priority}')
    record('breakdown_table_consistency', problems, rows=len(rows))

    problems = []
    verification = (ANNEXES / 'dom-008-verification.md').read_text(encoding='utf-8')
    for scenario in ('## Dossier fictif A', '## Dossier fictif B', '## Dossier fictif C'):
        if scenario not in verification:
            problems.append(f'Verification misses {scenario}')
    record('story_routing_scenarios', problems, legal_validation=False,
           business_scenarios_executed=False,
           note='Présence des dossiers seulement ; routage relu séparément par le rédacteur.')

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'transport-legal').exists():
        problems.append('transport-legal directory exists: no plugin may be created by DOM-008')
    names = [p['name'] for p in market['plugins']]
    if 'judge-fr-eu-transport-legal' in names:
        problems.append('transport plugin listed in marketplace')
    record('no_plugin_created', problems, marketplace_plugins=len(names))

    lot = LOT_DOCS + proposals + [BASE003]
    problems, count = [], 0
    for p in lot + [Path(__file__), GENERATOR]:
        raw = p.read_bytes()
        txt = raw.decode('utf-8')
        if not raw.endswith(b'\n') or raw.endswith(b'\n\n') or raw.startswith(b'\xef\xbb\xbf'):
            problems.append(f'{p.name}: final newline or UTF-8 BOM')
        if b'\r' in raw:
            problems.append(f'{p.name}: CR line ending')
        if any(line.rstrip() != line for line in txt.splitlines()):
            problems.append(f'{p.name}: trailing whitespace')
        if chr(0xFFFD) in txt:
            problems.append(f'{p.name}: replacement character')
        if p.suffix != '.md':
            continue
        for label, target in re.findall(r'\[([^\]\n]+)\]\(([^)]+)\)', txt):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            count += 1
            dest = unquote(target.split('#', 1)[0])
            if not (p.parent / dest).exists():
                problems.append(f'{p.name}: broken link {label}: {target}')
    record('links_and_format', problems, markdown_files=len(lot), local_links=count)

    problems = []
    for p in LOT_DOCS + proposals:
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

    index = INDEX.read_text(encoding='utf-8')
    base003 = BASE003.read_text(encoding='utf-8')
    problems = []
    for name in ('decoupage-transports', 'verification'):
        if f'(03-nouveaux-domaines/dom-008-annexes/dom-008-{name}.md)' not in index:
            problems.append(f'Index missing {name}')
    match = re.search(r'\| Total \| (\d+) \|', index)
    if not match or int(match.group(1)) != len(stories):
        problems.append(f'Index total differs from {len(stories)}')
    match = re.search(r'\| À faire \| (\d+) \|', index)
    if not match or int(match.group(1)) != statuses['proposee']:
        problems.append(f"Index proposee count differs from {statuses['proposee']}")
    if '"TPT": ' not in GENERATOR.read_text(encoding='utf-8'):
        problems.append('Index generator does not name the TPT family')
    generated = subprocess.run([sys.executable, '-X', 'utf8', str(GENERATOR), '--check'],
                               cwd=ROOT, capture_output=True, encoding='utf-8')
    if generated.returncode != 0:
        problems.append('ETAT.md is not up to date with backlog/etat.py')
    row = [line for line in base003.splitlines() if line.startswith('| Transports et voyages — ')]
    if len(row) != 1 or '(../../03-nouveaux-domaines/dom-008-annexes/dom-008-decoupage-transports.md)' not in row[0] \
            or 'TPT-001' not in row[0]:
        problems.append('BASE-003 matrix row does not link the breakdown and TPT-001')
    for p in proposals:
        if f'(../suites/{p.name})' not in breakdown:
            problems.append(f'Proposal missing from breakdown: {p.name}')
    if stories['DOM-008'][1]['statut'] != 'terminee':
        problems.append('DOM-008 not terminee')
    if stories['PILOTE-003'][1]['statut'] != 'terminee':
        problems.append('Pilot prerequisite not satisfied')
    record('index_matrix_and_prerequisites', problems)

    figures = []
    for p in LOT_DOCS + proposals:
        for number, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            for hit in re.findall(r'\b\d+\s*(?:jours?|mois|ans?|semaines?|heures?|€|euros?|%)', line):
                figures.append({'file': p.name, 'line': number, 'text': hit})
    checks['figures_for_manual_review'] = {
        'status': 'manual-review', 'count': len(figures), 'occurrences': figures,
        'note': 'Occurrences à relire : aucune durée, aucun seuil ni montant ne doit être présenté comme une règle.'}

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
               preserved_files=len(preserved), report_excluded_from_own_comparison=True)
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
        'story': 'DOM-008', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'cadrage documentaire transports et voyages ; aucun plugin créé ni validation juridique',
        'checks': checks,
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p)
                       for p in lot + [INDEX, GENERATOR, Path(__file__)]},
        'not_run': ['recherche juridique externe', 'calcul de délai, de seuil ou de montant',
                    'création ou exécution de skill', 'installation/recette client',
                    'lecteur réel ou indépendant', 'connexion/envoi/publication'],
        'commands': [
            [sys.executable, '-X', 'utf8', str(Path(__file__).relative_to(ROOT)), *sys.argv[1:]],
            'python -X utf8 backlog/etat.py --check (appelé par le contrôleur)',
            'python -X utf8 scripts/lint-tool-scope.py (appelé par le contrôleur)',
            'git diff --check (appelé par le contrôleur)',
        ],
        'execution_notes': [
            'Contrôles dans le checkout de travail ; aucun paquet créé ou installé.',
            'Périmètre comparé à un instantané avant tâche si --baseline est fourni ; les fichiers préexistants hors lot doivent rester identiques.',
            'Références de transport citées comme pistes non ouvertes ; scénarios métier non exécutés.',
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
