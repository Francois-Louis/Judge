"""Contrôles documentaires DOM-001, sans exécution d'un skill.

python backlog/03-nouveaux-domaines/dom-001-controles.py
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


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / 'dom-001-resultats.json'
COMMON = {'DOM-001', 'PILOTE-003', 'BASE-005', 'BASE-006'}
LOT_DOCS = [HERE / ('dom-001-' + n + '.md') for n in (
    'consommation', 'decoupage-consommation', 'verification', 'frictions-utilisateurs')]
SOURCE = HERE / 'sources/consommation-frictions-2026-10-16.txt'
SOURCE_SHA256 = 'c2727d33f1af56307efc85c59e763bd38fe1aa3b44d677ed080e7227c5f9bea5'
ALLOWED = {
    'backlog/README.md',
    'backlog/00-fondations/base-003-dossier-architecture.md',
    *(p.relative_to(ROOT).as_posix() for p in LOT_DOCS),
    SOURCE.relative_to(ROOT).as_posix(),
    'backlog/03-nouveaux-domaines/dom-001-controles.py',
    'backlog/03-nouveaux-domaines/dom-001-resultats.json',
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

    proposals = sorted((HERE / 'suites').glob('conso-*.md'))
    for p in proposals:
        ALLOWED.add(p.relative_to(ROOT).as_posix())
    expected = {f'CONSO-{i:03}' for i in range(1, 21)}
    actual = {k for k in stories if k.startswith('CONSO-')}
    problems = []
    if actual != expected or len(proposals) != 20:
        problems.append('Expected exactly CONSO-001..CONSO-020 and 20 files')
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
            match = re.match(r'consumer-legal/skills/([^/]+)/SKILL\.md$', name)
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

    breakdown = (HERE / 'dom-001-decoupage-consommation.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| (\d) \| \[(CONSO-\d{3})\]\(suites/([^)]+)\) \| `([^`]+)` \| [^|]+ \| ([^|]+) \|$',
                      breakdown, re.M)
    problems = []
    if {r[1] for r in rows} != expected:
        problems.append('Breakdown table does not list exactly CONSO-001..020')
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

    friction = (HERE / 'dom-001-frictions-utilisateurs.md').read_text(encoding='utf-8')
    friction_rows = re.findall(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$', friction, re.M)
    problems, owners = [], set()
    if [int(row[0]) for row in friction_rows] != list(range(1, 156)):
        problems.append('Expected 155 unique, ordered friction rows, numbered 1..155')
    primary = {}
    for number, label, owner_cell, result in friction_rows:
        links = re.findall(r'\[([A-Z]+-\d{3})\]\(([^)]+)\)', owner_cell)
        if not links:
            problems.append(f'Friction {number}: missing linked owner')
        primary[int(number)] = links[0][0] if links else None
        for ident, target in links:
            owners.add(ident)
            if ident not in stories or (HERE / target).resolve() != stories[ident][0].resolve():
                problems.append(f'Friction {number}: invalid owner/link {ident}: {target}')
    # Frontières sensibles : assurance, télécoms, tentative amiable et banque.
    for number, ident in {80: 'DOM-005', 93: 'DOM-022', 142: 'EXIST-006',
                          145: 'BNK-001', 146: 'BNK-001', 147: 'BNK-001',
                          148: 'BNK-006', 149: 'BNK-006'}.items():
        if primary.get(number) != ident:
            problems.append(f'Friction {number}: expected primary owner {ident}')
    if not {f'CONSO-{i:03}' for i in range(15, 21)} <= owners:
        problems.append('New CONSO proposals are not all linked from the friction matrix')
    for p in proposals:
        if '(../dom-001-frictions-utilisateurs.md)' not in p.read_text(encoding='utf-8'):
            problems.append(f'{p.name}: missing return link to consumption frictions')
    source_hash = digest(SOURCE) if SOURCE.is_file() else None
    if source_hash != SOURCE_SHA256:
        problems.append('User source missing or not identical to the supplied attachment')
    if SOURCE.is_file():
        numbers = [int(n) for n in re.findall(r'^(\d+)\\\.', SOURCE.read_text(encoding='utf-8'), re.M)]
        if numbers != list(range(1, 156)):
            problems.append('Archived user source does not contain exactly points 1..155')
    if '(sources/consommation-frictions-2026-10-16.txt)' not in friction:
        problems.append('Friction matrix does not link its archived user source')
    record('user_friction_coverage', problems, rows=len(friction_rows),
           owners=sorted(owners), source_sha256=source_hash,
           legal_validation=False, business_scenarios_executed=False)

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'consumer-legal').exists():
        problems.append('consumer-legal directory exists: no plugin may be created by DOM-001')
    names = [p['name'] for p in market['plugins']]
    if any('consumer' in n for n in names):
        problems.append('consumer plugin listed in marketplace')
    record('no_plugin_created', problems, marketplace_plugins=len(names))

    lot = LOT_DOCS + proposals + [ROOT / 'backlog/README.md',
                                  ROOT / 'backlog/00-fondations/base-003-dossier-architecture.md']
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

    index = (ROOT / 'backlog/README.md').read_text(encoding='utf-8')
    base003 = (ROOT / 'backlog/00-fondations/base-003-dossier-architecture.md').read_text(encoding='utf-8')
    problems = []
    for name in ('decoupage-consommation', 'verification', 'frictions-utilisateurs'):
        if f'(03-nouveaux-domaines/dom-001-{name}.md)' not in index:
            problems.append(f'Index missing {name}')
    match = re.search(r'contient (\d+) stories', index)
    if not match or int(match.group(1)) != len(stories):
        problems.append(f'Index total differs from {len(stories)}')
    match = re.search(r'les (\d+) autres sont `proposee`', index)
    if not match or int(match.group(1)) != statuses['proposee']:
        problems.append(f"Index proposee count differs from {statuses['proposee']}")
    if '(../03-nouveaux-domaines/dom-001-decoupage-consommation.md)' not in base003:
        problems.append('BASE-003 matrix row does not link the breakdown')
    for p in proposals:
        if f'(suites/{p.name})' not in breakdown:
            problems.append(f'Proposal missing from breakdown: {p.name}')
    if stories['DOM-001'][1]['statut'] != 'terminee':
        problems.append('DOM-001 not terminee')
    if stories['PILOTE-003'][1]['statut'] != 'terminee':
        problems.append('Pilot prerequisite not satisfied')
    record('index_matrix_and_prerequisites', problems)

    figures = []
    for p in LOT_DOCS + proposals:
        for number, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            for hit in re.findall(r'\b\d+\s*(?:jours?|mois|ans?|semaines?|€|euros?)\b', line):
                figures.append({'file': p.name, 'line': number, 'text': hit})
    checks['figures_for_manual_review'] = {
        'status': 'manual-review', 'count': len(figures), 'occurrences': figures,
        'note': 'Occurrences à relire : données fictives ou allégations utilisateur explicitement non vérifiées ; aucune règle validée.'}

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
        'story': 'DOM-001', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'intégration documentaire des 155 frictions consommation ; aucun plugin créé ni validation juridique',
        'checks': checks,
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in lot + [SOURCE, Path(__file__)]},
        'not_run': ['recherche juridique externe', 'calcul de délai ou de montant',
                    'création ou exécution de skill', 'installation/recette client',
                    'lecteur réel ou indépendant', 'connexion/envoi/publication'],
        'commands': [
            [sys.executable, '-X', 'utf8', str(Path(__file__).relative_to(ROOT)), *sys.argv[1:]],
            'python -X utf8 scripts/lint-tool-scope.py (appelé par le contrôleur)',
            'git diff --check (appelé par le contrôleur)',
        ],
        'execution_notes': [
            'Relevé actualisé pour 155 frictions, 14 suites complétées et six propositions CONSO-015 à CONSO-020.',
            'Instantané de début de cette intégration pris avant toute écriture du lot ; les travaux préexistants hors lot sont comparés par empreinte si --baseline est fourni.',
            'Le texte utilisateur est conservé octet pour octet ; son empreinte est celle de la pièce jointe, sans validation du droit ou des statistiques.',
            'Les scénarios documentaires emploient des pièces fictives ; les scénarios métier restent non exécutés.',
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
