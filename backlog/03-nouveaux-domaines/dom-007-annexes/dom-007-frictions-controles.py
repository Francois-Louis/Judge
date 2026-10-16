"""Contrôles documentaires du complément santé, sans validation juridique.

--source compare la copie au fichier joint ; --output conserve le relevé.
Les relevés historiques du cadrage initial ne sont pas réécrits.
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
SOURCE = DOMAIN / 'sources/sante-frictions-2026-10-16.txt'
MATRIX = ANNEXES / 'dom-007-frictions-utilisateurs.md'
RELAYS = [
    DOMAIN / 'dom-012-protection-sociale.md',
    DOMAIN / 'dom-025-handicap-autonomie.md',
    DOMAIN / 'dom-029-discriminations.md',
    DOMAIN / 'dom-035-responsabilite-dommages.md',
    DOMAIN / 'suites/ins-004-lire-garantie.md',
    DOMAIN / 'suites/ins-009-complementaire-sante.md',
    ROOT / 'backlog/02-plugins-existants/exist-003-donnees-personnelles.md',
    ROOT / 'backlog/01-pilote-travail/pilote-001-annexes/pilote-001-decoupage-travail.md',
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
    text = raw.decode('utf-8')
    points = [(int(n), title.split('. ', 1)[0]) for n, title in
              re.findall(r'^(\d+)\\\. (.*)$', text, re.M)]
    problems = []
    if [n for n, _ in points] != list(range(1, 156)):
        problems.append('Source numbering mismatch')
    if args.source and raw != args.source.read_bytes():
        problems.append('Source differs from attachment bytes')
    record('source_integrity', problems, points=len(points),
           sha256=hashlib.sha256(raw).hexdigest(),
           attachment_compared=bool(args.source))

    matrix = MATRIX.read_text(encoding='utf-8')
    rows = [line.split('|')[1:-1] for line in matrix.splitlines()
            if re.match(r'^\| \d+ \|', line)]
    problems = []
    if [int(row[0].strip()) for row in rows] != [n for n, _ in points]:
        problems.append('Matrix numbers must match source once, in order')
    titles = dict(points)
    for row in rows:
        if len(row) != 4 or any(not cell.strip() for cell in row):
            problems.append(f'Incomplete row: {row}')
            continue
        if row[1].strip() != titles[int(row[0].strip())]:
            problems.append(f'Friction title differs: {row[0]}')
        if '](' not in row[2]:
            problems.append(f'Missing owner: {row[0]}')
    for marker in ('### Section 12', '### Section 13', '### Section 14',
                   '### Section 15', '31/62', 'à découper', 'Mon espace santé'):
        if marker not in matrix:
            problems.append(f'Missing coverage: {marker}')
    record('matrix_coverage', problems, rows=len(rows))

    stories, problems = {}, []
    for path in (ROOT / 'backlog').rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        if not content.startswith('---\n'):
            continue
        try:
            meta = yaml.safe_load(content.split('---', 2)[1])
            ident = meta['id']
            if ident in stories:
                problems.append(f'Duplicate ID: {ident}')
            stories[ident] = meta
            for key in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
                if key not in meta:
                    problems.append(f'{ident}: missing {key}')
            if not isinstance(meta.get('dependances'), list):
                problems.append(f'{ident}: dependencies must be a list')
                meta['dependances'] = []
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{path}: {exc}')
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
        for dep in stories[ident]['dependances']:
            visit(dep)
        active.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    record('metadata_and_dependencies', problems, stories=len(stories))

    proposals = sorted((DOMAIN / 'suites').glob('san-*.md'))
    problems, owned = [], []
    if [p.name[4:7] for p in proposals] != [f'{n:03}' for n in range(1, 20)]:
        problems.append('Expected SAN-001 to SAN-019')
    for path in proposals:
        content = path.read_text(encoding='utf-8')
        ident = f'SAN-{path.name[4:7]}'
        if stories[ident]['statut'] != 'proposee':
            problems.append(f'{ident}: unexpectedly selected or delivered')
        for marker in ('BASE-006', 'BASE-013', '**attendus, non exécutés**',
                       'dom-007-frictions-utilisateurs.md'):
            if marker not in content:
                problems.append(f'{ident}: missing {marker}')
        if int(path.name[4:7]) >= 13:
            for marker in ('- Cas normal :', '- Cas limite :', 'Sans source lue'):
                if marker not in content:
                    problems.append(f'{ident}: missing {marker}')
            paths = re.findall(r'^- `(health-legal/(?:skills|references)/[^`]+)`',
                               content, re.M)
            if len(paths) != 2:
                problems.append(f'{ident}: expected one skill and one reference')
            owned.extend(paths)
            for target in paths:
                if (ROOT / target).exists():
                    problems.append(f'{ident}: future path exists: {target}')
    for target, count in Counter(owned).items():
        if count != 1:
            problems.append(f'Duplicate future owner: {target}')
    record('bounded_proposals', problems, proposals=len(proposals),
           new_skills=len(owned) // 2)

    lot = [MATRIX, ANNEXES / 'dom-007-decoupage-sante.md',
           ANNEXES / 'dom-007-frictions-verification.md', Path(__file__),
           DOMAIN / 'dom-007-sante.md', *proposals, *RELAYS]
    problems, links = [], 0
    for path in lot:
        content = path.read_text(encoding='utf-8')
        if path in RELAYS:
            # Shared files can contain unrelated, unfinished changes.
            # Check only the health appendix owned by this task.
            marker = '## Complément des frictions santé'
            if marker not in content:
                problems.append(f'{path.name}: missing relay')
                continue
            content = marker + content.split(marker, 1)[1]
            content = re.split(r'\n## ', content, maxsplit=1)[0]
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
                problems.append(f'{path.name}: inconsistent table width')
            width = cells
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            links += 1
            if not (path.parent / target.split('#', 1)[0]).exists():
                problems.append(f'{path.name}: broken link {target}')
    for path in RELAYS:
        if '## Complément des frictions santé' not in path.read_text(encoding='utf-8'):
            problems.append(f'{path.name}: missing relay')
    record('links_format_and_relays', problems, local_links=links, files=len(lot))

    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    problems = []
    if (ROOT / 'health-legal').exists() or any('health-legal' in p['name']
                                            for p in market['plugins']):
        problems.append('Backlog integration must not ship health plugin')
    record('no_plugin_created', problems)
    report = dict(date='2026-10-16', timezone='Europe/Paris', checks=checks,
                  validation_context=args.context,
                  scope='Intégration documentaire ; aucun résultat juridique validé',
                  not_run=['recherche juridique', 'scénarios exécutables et skills',
                           'installation client', 'lecture indépendante',
                           'calcul ou démarche externe'])
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
