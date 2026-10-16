"""Contrôles documentaires des frictions véhicules, sans validation juridique.

python -X utf8 backlog/03-nouveaux-domaines/dom-023-annexes/dom-023-frictions-controles.py
Option --output <rapport.json> : conserver un relevé daté.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'backlog/03-nouveaux-domaines'
ANN = Path(__file__).resolve().parent
SOURCE = BASE / 'sources/vehicules-frictions-2026-10-16.txt'
SOURCE_SHA = 'd2f18240d1c45912b6df094cc1f34de573d59af35182c1842fba61300c7d23f7'
MARKER = '## Complément des frictions véhicules — 16 octobre 2026'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = {}

    def record(name, problems, **facts):
        checks[name] = {'status': 'failed' if problems else 'passed',
                        **facts, 'problems': problems}

    raw_source = SOURCE.read_bytes()
    actual_sha = hashlib.sha256(raw_source).hexdigest()
    record('source_integrity', [] if actual_sha == SOURCE_SHA else ['Source modifiée'],
           sha256=actual_sha, bytes=len(raw_source))
    source = raw_source.decode('utf-8').split('## 11.')[0]
    items = {int(n): text for n, text in re.findall(r'^(\d+)\\\. (.+)$', source, re.M)}
    matrix_path = ANN / 'dom-023-frictions-utilisateurs.md'
    matrix = matrix_path.read_text(encoding='utf-8')
    rows = re.findall(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$', matrix, re.M)
    problems = []
    expected = set(range(1, 196))
    if set(items) != expected or [int(r[0]) for r in rows] != list(range(1, 196)):
        problems.append('Source ou matrice différente des 195 points ordonnés sans doublon')
    for number, title, owners, result in rows:
        original = items.get(int(number), '').split('. ', 1)[0].replace('&#x20;', '').replace('|', '/')
        if title.strip() != original:
            problems.append(f'Point {number} : titre différent de la source')
        if not re.search(r'\[[A-Z]+-\d{3}\]\(', owners) or not result.strip():
            problems.append(f'Point {number} : propriétaire ou résultat manquant')
    deadlines = matrix.split('## Échéances du tableau utilisateur (§11)', 1)[-1].split('\n## ', 1)[0]
    deadline_rows = [line for line in deadlines.splitlines() if line.startswith('|')][2:]
    if len(deadline_rows) != 16:
        problems.append('Les 16 lignes du tableau d’échéances ne sont pas toutes reprises')
    record('friction_traceability', problems, points=len(rows), deadline_rows=len(deadline_rows))

    stories, problems = {}, []
    for path in (ROOT / 'backlog').rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        if not re.match(r'^---\s*\n', text):
            continue
        fm = yaml.safe_load(text.split('---', 2)[1])
        if not isinstance(fm, dict) or 'id' not in fm:
            continue
        ident = fm['id']
        if ident in stories:
            problems.append(f'Identifiant dupliqué : {ident}')
        stories[ident] = (path, fm)
        if not isinstance(fm.get('dependances'), list):
            problems.append(f'{ident} : dépendances non listées')
    visiting, done = set(), set()

    def visit(ident):
        if ident in visiting:
            problems.append(f'Cycle : {ident}')
            return
        if ident in done:
            return
        visiting.add(ident)
        for dep in stories[ident][1].get('dependances', []):
            if dep not in stories:
                problems.append(f'{ident} : dépendance absente {dep}')
            else:
                visit(dep)
        visiting.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    record('story_ids_and_dependency_graph', problems, stories=len(stories))

    vehicle = {ident: value for ident, value in stories.items() if ident.startswith('VEH-')}
    problems = []
    if set(vehicle) != {f'VEH-{n:03}' for n in range(1, 21)}:
        problems.append('Le lot ne contient pas exactement VEH-001 à VEH-020')
    targets = {}
    for ident, (path, fm) in vehicle.items():
        text = path.read_text(encoding='utf-8')
        for field in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
            if field not in fm:
                problems.append(f'{ident} : champ absent {field}')
        if fm.get('statut') != 'proposee' or fm.get('nature') != 'implementation':
            problems.append(f'{ident} : statut/nature inattendu')
        for heading in ('Objectif et résultat attendu', 'Périmètre et fichiers',
                        'Pièces et informations nécessaires', 'Sortie attendue',
                        'Travail attendu', 'Références métier et sources à rechercher',
                        "Critères d'acceptation", 'Vérification', 'Hors périmètre'):
            if f'## {heading}\n' not in text:
                problems.append(f'{ident} : section absente {heading}')
        for token in ('- Cas normal :', '- Cas limite :', '**attendus, non exécutés**', 'BASE-013'):
            if token not in text:
                problems.append(f'{ident} : marqueur absent {token}')
        if int(ident[-3:]) <= 12 and MARKER not in text:
            problems.append(f'{ident} : complément absent')
        for target in re.findall(r'^- `([^`]+)`[^\n]*\(à créer\)', text, re.M):
            if target in targets or (ROOT / target).exists():
                problems.append(f'{ident} : propriétaire futur dupliqué ou fichier déjà créé {target}')
            targets[target] = ident
    breakdown = (ANN / 'dom-023-decoupage-vehicules.md').read_text(encoding='utf-8')
    table = re.findall(r'^\| (\d) \| \[(VEH-\d{3})\]\(\.\./suites/([^)]+)\) \| `([^`]+)` \| [^|]+ \| ([^|]+) \|$', breakdown, re.M)
    if len(table) != 20 or {r[1] for r in table} != set(vehicle):
        problems.append('Table de découpage incomplète ou dupliquée')
    common = {'DOM-023', 'PILOTE-003', 'BASE-005', 'BASE-006', 'BASE-008'}
    for rank, ident, filename, skill, deps in table:
        path, fm = vehicle[ident]
        business = set() if deps.strip() == 'Aucune' else {d.strip() for d in deps.split(',')}
        if path.name != filename or set(fm['dependances']) != common | business:
            problems.append(f'{ident} : chemin ou dépendances différents du découpage')
        if f'`vehicle-legal/skills/{skill}/SKILL.md`' not in path.read_text(encoding='utf-8'):
            problems.append(f'{ident} : skill cible différent du découpage')
        if fm.get('priorite') != ('P3' if rank == '4' else 'P2'):
            problems.append(f'{ident} : priorité différente du rang')
    record('vehicle_proposals_and_breakdown', problems, proposals=len(vehicle), future_targets=len(targets))

    neighbor_paths = [BASE / f'dom-{n:03}-{slug}.md' for n, slug in (
        (4, 'banque'), (9, 'douanes'), (10, 'administratif'), (11, 'fiscalite'))]
    neighbor_paths += [next((BASE / 'suites').glob(prefix + '-*.md')) for prefix in (
        'bnk-005', 'ins-003', 'ins-004', 'ins-015', 'ins-021')]
    problems = [str(p.relative_to(ROOT)) for p in neighbor_paths if MARKER not in p.read_text(encoding='utf-8')]
    record('neighbor_requirements', problems, owners=len(neighbor_paths))

    docs = [BASE / 'dom-023-vehicules-garages.md', ANN / 'dom-023-decoupage-vehicules.md',
            matrix_path, ANN / 'dom-023-frictions-verification.md']
    docs += [path for path, _ in vehicle.values()]
    problems, links = [], 0
    for path in docs + neighbor_paths:
        text = path.read_text(encoding='utf-8')
        if path in neighbor_paths:
            text = text.split(MARKER, 1)[-1].split('\n## ', 1)[0]
        if any(line.rstrip() != line for line in text.splitlines()) or '\ufffd' in text:
            problems.append(f'{path.name} : espaces finaux ou encodage')
        width = None
        for line in text.splitlines():
            if not line.startswith('|'):
                width = None
                continue
            columns = line.count('|') - 1
            if width is not None and columns != width:
                problems.append(f'{path.name} : largeur du tableau incohérente')
            width = columns
        for label, target in re.findall(r'\[([^\]\n]+)\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            links += 1
            destination = unquote(target.split('#', 1)[0])
            # Le rapport optionnel est produit après ce contrôle.
            if destination == 'dom-023-frictions-resultats.json':
                continue
            if not (path.parent / destination).is_file():
                problems.append(f'{path.name} : lien cassé {label} → {target}')
    record('lot_links_format_and_tables', problems, documents=len(docs) + len(neighbor_paths), links=links)

    index = subprocess.run([sys.executable, '-X', 'utf8', 'backlog/etat.py', '--check'],
                           cwd=ROOT, capture_output=True, encoding='utf-8')
    record('generated_backlog_index', [] if index.returncode == 0 else [index.stdout + index.stderr])
    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'vehicle-legal').exists() or any('vehicle' in p['name'] for p in market['plugins']):
        problems.append('Plugin véhicules créé ou publié par le cadrage')
    record('no_vehicle_plugin_created', problems, marketplace_plugins=len(market['plugins']))
    report = {
        'story': 'DOM-023', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'scope': 'Complément documentaire automobile ; aucune validation juridique ou exécution métier',
        'checks': checks,
        'not_run': ['recherche juridique', 'validation des tarifs et délais', 'exécution des scénarios métier',
                    'implémentation de skill', 'recette paquet/client', 'lecteur indépendant', 'envoi ou dépôt'],
    }
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    for name, result in checks.items():
        print(f"{name}: {result['status']}")
        for problem in result['problems']:
            print(f'  {problem}')
    return int(any(check['status'] == 'failed' for check in checks.values()))


if __name__ == '__main__':
    raise SystemExit(main())
