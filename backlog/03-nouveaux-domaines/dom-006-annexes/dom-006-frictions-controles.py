"""Contrôle structurel du complément logement, sans validation juridique.

python -X utf8 backlog/03-nouveaux-domaines/dom-006-annexes/dom-006-frictions-controles.py
--source permet de comparer la copie au fichier utilisateur d'origine.
--output conserve un relevé daté ; ne pas réécrire les relevés historiques.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import yaml


ANNEXES = Path(__file__).resolve().parent
DOMAIN = ANNEXES.parent
ROOT = DOMAIN.parents[1]
SOURCE = DOMAIN / 'sources/logement-frictions-2026-10-16.txt'
MATRIX = ANNEXES / 'dom-006-frictions-utilisateurs.md'
BREAKDOWN = ANNEXES / 'dom-006-decoupage-logement.md'
NEIGHBOURS = [
    'dom-015-construction-travaux.md', 'dom-017-transactions-immobilieres.md',
    'dom-018-copropriete.md', 'dom-019-urbanisme-foncier.md',
    'dom-020-voisinage-servitudes.md', 'dom-021-energie-eau.md',
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--context', default='working-tree')
    args = parser.parse_args()
    checks = {}

    def record(name, problems, **facts):
        checks[name] = dict(status='failed' if problems else 'passed',
                            problems=problems, **facts)

    raw = SOURCE.read_bytes()
    source_text = raw.decode('utf-8')
    inventory = source_text.split('## 10.', 1)[0]
    numbers = [int(n) for n in re.findall(r'^(\d+)\\\.', inventory, re.M)]
    problems = [] if numbers == list(range(1, 127)) else ['Source numbering mismatch']
    if args.source and raw != args.source.read_bytes():
        problems.append('Source copy differs from attachment bytes')
    record('source_integrity', problems, numbered_frictions=len(numbers),
           sha256=hashlib.sha256(raw).hexdigest(),
           attachment_compared=bool(args.source))

    text = MATRIX.read_text(encoding='utf-8')
    rows = re.findall(r'^\| (\d+) \| ([^\n]+)$', text, re.M)
    problems = []
    if [int(n) for n, _ in rows] != numbers:
        problems.append('Matrix must list each source number once in order')
    for n, row in rows:
        cells = row.split('|')
        if len(cells) != 4 or any(not cell.strip() for cell in cells[:3]):
            problems.append(f'Point {n}: missing friction, owner or result')
        if '](' not in cells[1] and 'Domaine au fond' not in cells[1]:
            problems.append(f'Point {n}: owner not identified')
    for marker in ('## Sections non numérotées', 'CTX-016', 'Social',
                   'versions', 'acte requis', 'aucune date limite inventée'):
        if marker not in text:
            problems.append(f'Matrix missing {marker}')
    record('matrix_coverage', problems, rows=len(rows))

    stories, problems = {}, []
    for path in sorted((ROOT / 'backlog').rglob('*.md')):
        content = path.read_text(encoding='utf-8')
        if not content.startswith('---\n'):
            continue
        try:
            meta = yaml.safe_load(content.split('---', 2)[1])
            ident = meta['id']
            if ident in stories:
                problems.append(f'Duplicate ID {ident}')
            for key in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
                if key not in meta:
                    problems.append(f'{ident}: missing {key}')
            if not isinstance(meta.get('dependances'), list):
                problems.append(f'{ident}: dependencies must be a list')
                meta['dependances'] = []
            stories[ident] = (path, meta)
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{path}: {exc}')
    active, done = set(), set()

    def visit(ident):
        if ident not in stories:
            problems.append(f'Missing dependency {ident}')
            return
        if ident in active:
            problems.append(f'Dependency cycle {ident}')
            return
        if ident in done:
            return
        active.add(ident)
        for dependency in stories[ident][1]['dependances']:
            visit(dependency)
        active.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    record('backlog_metadata_dependencies', problems, stories=len(stories))

    proposals = sorted((DOMAIN / 'suites').glob('log-*.md'))
    problems, skills, references = [], [], []
    expected = {f'LOG-{n:03}' for n in range(1, 24)}
    if {i for i in stories if i.startswith('LOG-')} != expected:
        problems.append('Expected LOG-001..023')
    breakdown = BREAKDOWN.read_text(encoding='utf-8')
    for path in proposals:
        content = path.read_text(encoding='utf-8')
        meta = yaml.safe_load(content.split('---', 2)[1])
        ident = meta['id']
        if meta['statut'] != 'proposee' or meta['nature'] != 'implementation':
            problems.append(f'{ident}: must remain proposed implementation')
        if 'matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md)' not in content:
            problems.append(f'{ident}: missing matrix backlink')
        if ident not in breakdown:
            problems.append(f'{ident}: missing breakdown entry')
        if int(ident[-3:]) < 12:
            if 'Scénario **attendu, non exécuté**' not in content:
                problems.append(f'{ident}: missing supplementary scenario')
            continue
        if set(meta['dependances']) != {'DOM-006', 'PILOTE-003', 'BASE-005', 'BASE-006', 'LOG-001'}:
            problems.append(f'{ident}: unexpected dependencies')
        for heading in ('Objectif et résultat attendu', 'Périmètre et fichiers',
                        'Pièces et informations nécessaires', 'Sortie attendue',
                        'Travail attendu', 'Références métier et sources à rechercher',
                        "Critères d'acceptation", 'Vérification', 'Hors périmètre'):
            if f'## {heading}\n' not in content:
                problems.append(f'{ident}: missing {heading}')
        for marker in ('- Cas normal :', '- Cas limite :', 'Sans source lue',
                       '**attendus, non exécutés**', 'BASE-013', 'BASE-006'):
            if marker not in content:
                problems.append(f'{ident}: missing {marker}')
        skill = re.findall(r'^- `(housing-legal/skills/[^`]+/SKILL.md)`', content, re.M)
        reference = re.findall(r'^- `(housing-legal/references/[^`]+)`', content, re.M)
        if len(skill) != 1 or len(reference) != 1:
            problems.append(f'{ident}: expected one skill and one owned reference')
        for target in skill + reference:
            if (ROOT / target).exists():
                problems.append(f'{ident}: future file already exists {target}')
        skills.extend(skill)
        references.extend(reference)
    for target, count in Counter(skills + references).items():
        if count != 1:
            problems.append(f'Duplicate future owner {target}')
    record('bounded_proposals', problems, proposals=len(proposals), new_skills=len(skills))

    lot = [MATRIX, BREAKDOWN, Path(__file__), SOURCE,
           ANNEXES / 'dom-006-frictions-verification.md',
           DOMAIN / 'dom-006-logement.md', *proposals,
           *(DOMAIN / name for name in NEIGHBOURS),
           ROOT / 'backlog/02-plugins-existants/exist-003-donnees-personnelles.md']
    problems, links = [], 0
    for path in lot:
        content = path.read_text(encoding='utf-8')
        if path == SOURCE:
            continue  # Original formatting is deliberately preserved.
        if not path.read_bytes().endswith(b'\n') or content.startswith('\ufeff'):
            problems.append(f'{path.name}: newline or BOM')
        if any(line.rstrip() != line for line in content.splitlines()):
            problems.append(f'{path.name}: trailing whitespace')
        if path.suffix != '.md':
            continue
        width = None
        for line in content.splitlines():
            if not line.startswith('|'):
                width = None
                continue
            cells = len(line.split('|'))
            if width is not None and width != cells:
                problems.append(f'{path.name}: table width mismatch')
            width = cells
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            links += 1
            if not (path.parent / target.split('#', 1)[0]).exists():
                problems.append(f'{path.name}: broken link {target}')
    for path in [DOMAIN / n for n in NEIGHBOURS]:
        content = path.read_text(encoding='utf-8')
        if 'Complément des frictions logement' not in content or 'Scénarios **attendus, non exécutés**' not in content:
            problems.append(f'{path.name}: missing relay or scenarios')
    record('links_format_and_relays', problems, local_links=links, files=len(lot))

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'housing-legal').exists() or any('housing' in p['name'] for p in market['plugins']):
        problems.append('Backlog integration must not ship housing plugin')
    record('no_plugin_created', problems)

    report = dict(date='2026-10-16', timezone='Europe/Paris',
                  scope='complément documentaire ; aucun résultat juridique validé',
                  validation_context=args.context,
                  checks=checks,
                  not_run=['recherche juridique', 'skills et scénarios exécutables',
                           'installation client', 'lecteur indépendant',
                           'calcul juridique ou démarche externe'])
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                               encoding='utf-8', newline='\n')
    for name, result in checks.items():
        print(f"{name}: {result['status']}")
        for problem in result['problems']:
            print(f'  {problem}')
    return int(any(c['status'] == 'failed' for c in checks.values()))


if __name__ == '__main__':
    sys.exit(main())
