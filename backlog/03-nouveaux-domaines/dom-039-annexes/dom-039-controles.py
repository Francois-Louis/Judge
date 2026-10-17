"""Contrôles documentaires DOM-039, sans validation du droit ni exécution de skill.

Depuis la racine : python -X utf8 <ce fichier> [--output <rapport.json>].
La numérotation contrôlée est celle du lot de cadrage à 42 suites.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[3]
ANNEXES = Path(__file__).resolve().parent
HERE = ANNEXES.parent
COMMON = {
    'DOM-039', 'PILOTE-003', 'BASE-005', 'BASE-006', 'BASE-008',
    'BASE-013', 'BASE-014', 'BASE-019',
}
EXPECTED = {f'IND-{n:03}' for n in range(1, 43)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = {}

    def record(name, problems, **facts):
        checks[name] = dict(status='failed' if problems else 'passed',
                            problems=problems, **facts)

    stories, problems = {}, []
    for path in sorted((ROOT / 'backlog').rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---\n'):
            continue
        try:
            fm = yaml.safe_load(text.split('---', 2)[1])
            if not isinstance(fm, dict) or 'id' not in fm:
                continue  # méthode de référence ou autre document sans story
            ident = fm['id']
            if ident in stories:
                problems.append(f'Identifiant dupliqué : {ident}')
            if not isinstance(fm.get('dependances'), list):
                problems.append(f'{ident} : dépendances non listées')
                fm['dependances'] = []
            stories[ident] = (path, fm)
        except (IndexError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{path.relative_to(ROOT)} : {exc}')
    for ident, (_, fm) in stories.items():
        for dep in fm['dependances']:
            if dep not in stories:
                problems.append(f'{ident} : dépendance absente {dep}')
    active, done = set(), set()

    def visit(ident):
        if ident in active:
            problems.append(f'Cycle de dépendances : {ident}')
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
    record('identifiants_dependances_cycles', problems, stories=len(stories))

    proposals = sorted((HERE / 'suites').glob('ind-*.md'))
    problems, skills = [], {}
    if len(proposals) != 42 or {sid for sid in stories if sid.startswith('IND-')} != EXPECTED:
        problems.append('Le lot doit contenir exactement IND-001 à IND-042')
    for path in proposals:
        text = path.read_text(encoding='utf-8')
        fm = yaml.safe_load(text.split('---', 2)[1])
        ident = fm['id']
        if fm['statut'] != 'proposee' or fm['nature'] != 'implementation':
            problems.append(f'{ident} : doit rester une proposition d’implémentation')
        if not COMMON <= set(fm['dependances']):
            problems.append(f'{ident} : socle de dépendances incomplet')
        if ident != 'IND-001' and 'IND-001' not in fm['dependances']:
            problems.append(f'{ident} : ne dépend pas du créateur de paquet')
        for heading in ('Objectif et résultat attendu', 'Périmètre et fichiers',
                        'Pièces et informations nécessaires', 'Travail attendu et sortie',
                        'Références métier à vérifier', "Critères d'acceptation",
                        'Vérification', 'Hors périmètre et état'):
            if f'## {heading}\n' not in text:
                problems.append(f'{ident} : section absente {heading}')
        targets = re.findall(r'^- `([^`]+)` \(à créer', text, re.M)
        if len(targets) != 2 or any((ROOT / target).exists() for target in targets):
            problems.append(f'{ident} : deux fichiers métier futurs attendus')
        match = re.search(r'self-employed-legal/skills/([^/]+)/SKILL\.md', text)
        if match:
            skills[ident] = match.group(1)
        else:
            problems.append(f'{ident} : cible de skill absente')
        if '- Cas normal :' not in text or '- Cas limite :' not in text or '**attendus, non exécutés**' not in text:
            problems.append(f'{ident} : scénarios ou portée absents')
    if len(set(skills.values())) != len(skills):
        problems.append('Un nom de skill est partagé entre plusieurs tâches')

    breakdown = (ANNEXES / 'dom-039-decoupage-independants.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| ([1-4]) \| \[(IND-\d{3})\]\(\.\./suites/([^)]+)\) \| `([^`]+)` \| [^|]+ \| ([^|]+) \|$', breakdown, re.M)
    if len(rows) != 42 or {row[1] for row in rows} != EXPECTED:
        problems.append('La table de découpage ne référence pas exactement les 42 suites')
    for rank, ident, filename, skill, business_deps in rows:
        if ident not in stories:
            continue
        path, fm = stories[ident]
        listed = set() if business_deps.strip() == 'Aucune' else set(business_deps.strip().split(', '))
        if path.name != filename or skills.get(ident) != skill:
            problems.append(f'{ident} : incohérence fichier/skill dans la table')
        if listed != set(fm['dependances']) - COMMON:
            problems.append(f'{ident} : dépendances métier incohérentes')
        if fm['priorite'] != ('P3' if rank == '4' else 'P2'):
            problems.append(f'{ident} : priorité incohérente avec le rang')
    record('suites_et_decoupage', problems, proposals=len(proposals), skills=len(skills))

    coverage = (ANNEXES / 'dom-039-couverture-demandes.md').read_text(encoding='utf-8')
    section = coverage.split('## Points formalités attribués à DOM-039', 1)[1].split('## Données personnelles', 1)[0]
    covered = set()
    for cell in re.findall(r'^\| ([\d, ]+) \|', section, re.M):
        covered.update(int(number) for number in re.findall(r'\d+', cell))
    required = {5, 7, *range(11, 18), *range(19, 25), 29, 30, *range(33, 55),
                56, 59, 64, 69, 70, 79, 80, 81, *range(86, 99)}
    record('couverture_formalites',
           [f'Points manquants : {sorted(required - covered)}'] if required - covered else [],
           covered_points=sorted(covered),
           note='Couverture documentaire du besoin, pas de validation de règle ni de fonctionnalité.')

    sources = [
        ROOT / 'backlog/02-plugins-existants/exist-002-annexes/exist-002-frictions-utilisateurs.md',
        ROOT / 'backlog/02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md',
        HERE / 'dom-012-annexes/dom-012-frictions-utilisateurs.md',
    ]
    documents = [HERE / 'dom-039-micro-entreprise.md', *sorted(ANNEXES.glob('*.md')), *proposals]
    support = [ROOT / 'backlog/etat.py',
               ROOT / 'backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md',
               Path(__file__)]
    problems, links = [], 0
    for path in documents + support:
        raw = path.read_bytes()
        text = raw.decode('utf-8')
        if not raw.endswith(b'\n') or raw.startswith(b'\xef\xbb\xbf') or '\ufffd' in text:
            problems.append(f'{path.name} : encodage ou fin de fichier')
        if any(line.rstrip() != line for line in text.splitlines()):
            problems.append(f'{path.name} : espaces de fin de ligne')
        if path.suffix != '.md':
            continue
        for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            links += 1
            if not (path.parent / unquote(target.split('#', 1)[0])).exists():
                problems.append(f'{path.name} : lien absent {target}')
        width = None
        for line in text.splitlines():
            if not line.startswith('|'):
                width = None
                continue
            current = len(line.split('|')) - 2
            if width is not None and current != width:
                problems.append(f'{path.name} : colonnes de tableau incohérentes')
            width = current
    record('liens_format_tableaux', problems, local_links=links, documents=len(documents))

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'self-employed-legal').exists():
        problems.append('Un paquet self-employed-legal a été créé')
    if any(p['name'] == 'judge-fr-eu-self-employed-legal' for p in market['plugins']):
        problems.append('Le plugin proposé a été inscrit au marketplace')
    record('aucun_plugin_livre', problems, marketplace_plugins=len(market['plugins']))

    result = subprocess.run([sys.executable, '-X', 'utf8', 'backlog/etat.py', '--check'],
                            cwd=ROOT, capture_output=True, encoding='utf-8')
    problems = [] if result.returncode == 0 else [result.stdout + result.stderr]
    index = (ROOT / 'backlog/ETAT.md').read_text(encoding='utf-8')
    for ident in EXPECTED:
        if f'[{ident}]' not in index:
            problems.append(f'Index : {ident} absent')
    record('index_genere', problems, statuses=dict(Counter(fm['statut'] for _, fm in stories.values())))

    report = dict(
        story='DOM-039', date='2026-10-17', timezone='Europe/Paris',
        scope='Cadrage documentaire ; aucune source juridique ni scénario de skill exécuté.',
        checks=checks,
        fingerprints={p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in sorted(set(documents + support + sources))},
    )
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                               encoding='utf-8', newline='\n')
    for name, check in checks.items():
        print(f"{name}: {check['status']}")
        for problem in check['problems']:
            print(f'  {problem}')
    return int(any(check['status'] == 'failed' for check in checks.values()))


if __name__ == '__main__':
    sys.exit(main())
