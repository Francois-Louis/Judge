# Added by Judge FR/UE for BASE-014, 2026-10-17.
"""Check that every official legal source of a plugin's references was re-read.

python scripts/source_reviews.py employment-legal --depuis 2026-10-17

A business reference is any Markdown file under `<plugin>/references/` or
`<plugin>/skills/*/references/`, except `references/shared/` (the shared
BASE-005 method, whose dated readings are drafting landmarks, not sources
applied to a case). Every link to an official legal host (gouv.fr, europa.eu,
courdecassation.fr, conseil-etat.fr, coe.int) must appear in a row of a
Markdown table whose header has a `Relecture` column. That cell reads:

    AAAA-MM-JJ · issue · voie[ · précision]

issue: inchangee | modifiee | abrogee | jurisprudence-nouvelle | inaccessible.
A change (modifiee, abrogee, jurisprudence-nouvelle) must say `intégrée X.Y.Z`,
X.Y.Z being the current version of the reference, and the plugin NOTICE must
mention `<reference file name> X.Y.Z`. An inaccessible source must say
`réserve`: its conclusion stays reserved in the reference. Dates must fall
between --depuis (start of the lot preparation) and today. The check reads
text only: it does not prove that a reading happened or was correct.
"""

import argparse
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re
import sys

ISSUES = {'inchangee', 'modifiee', 'abrogee', 'jurisprudence-nouvelle', 'inaccessible'}
CHANGES = {'modifiee', 'abrogee', 'jurisprudence-nouvelle'}
URL = re.compile(r'https?://([A-Za-z0-9.-]+)[^\s)<>|]*')
LEGAL_HOSTS = ('gouv.fr', 'europa.eu', 'courdecassation.fr', 'conseil-etat.fr', 'coe.int')
VERSION = re.compile(r'(?:Version `|— )(\d+\.\d+\.\d+)')


def is_reference(path):
    """path is relative to the plugin root."""
    parts = PurePosixPath(path).parts
    if not path.endswith('.md') or len(parts) < 2:
        return False
    if parts[0] == 'references':
        return parts[1] != 'shared'
    return parts[0] == 'skills' and len(parts) > 3 and parts[2] == 'references'


def legal_urls(text):
    return {m.group(0) for m in URL.finditer(text)
            if any(m.group(1) == h or m.group(1).endswith('.' + h) for h in LEGAL_HOSTS)}


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def review_rows(text):
    """Yield (row text, Relecture cell) for every table with a Relecture column."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.lstrip().startswith('|') or 'Relecture' not in cells(line):
            continue
        column = cells(line).index('Relecture')
        for row in lines[i + 2:]:
            if not row.lstrip().startswith('|'):
                break
            values = cells(row)
            yield row, values[column] if column < len(values) else ''


def check_reference(path, text, notice, since, today):
    """Return (errors, reviews) for one reference file."""
    errors, reviews, covered = [], [], set()
    match = VERSION.search('\n'.join(text.splitlines()[:12]))
    version = match.group(1) if match else None
    name = PurePosixPath(path).name
    for row, cell in review_rows(text):
        urls = legal_urls(row)
        covered |= urls
        parts = [p.strip() for p in cell.split('·')]
        where = f'{path}: {cell or "(vide)"}'
        if len(parts) < 3 or not parts[2]:
            errors.append(f'relecture incomplète, attendu « date · issue · voie » : {where}')
            continue
        try:
            when = date.fromisoformat(parts[0])
        except ValueError:
            errors.append(f'date de relecture invalide : {where}')
            continue
        issue, extra = parts[1], ' '.join(parts[3:])
        if issue not in ISSUES:
            errors.append(f'issue inconnue « {issue} » : {where}')
        if when < since:
            errors.append(f'source non relue pour ce lot (relecture {when} < {since}) : {where}')
        if when > today:
            errors.append(f'date de relecture future : {where}')
        if issue in CHANGES:
            integrated = re.search(r'intégrée (\d+\.\d+\.\d+)', extra)
            if not integrated or integrated.group(1) != version:
                errors.append(f'{issue} sans mise à jour de la référence (version {version}) : {where}')
            elif f'{name} {version}' not in notice:
                errors.append(f'{issue} sans entrée NOTICE « {name} {version} » : {where}')
        if issue == 'inaccessible' and 'réserve' not in extra:
            errors.append(f'source inaccessible sans réserve consignée : {where}')
        reviews.append({'reference': path, 'reference_version': version, 'date': parts[0],
                        'issue': issue, 'voie': parts[2], 'precision': extra,
                        'sources': sorted(urls)})
    for url in sorted(legal_urls(text) - covered):
        errors.append(f'source sans relecture : {path}: {url}')
    return errors, reviews


def check_plugin(files, plugin, since, today=None):
    """files maps repository paths to bytes. Return (errors, reviews)."""
    today = today or date.today()
    notice = files.get(f'{plugin}/NOTICE', b'').decode('utf-8')
    errors, reviews = [], []
    for path in sorted(files):
        if path.startswith(plugin + '/') and is_reference(path[len(plugin) + 1:]):
            e, r = check_reference(path, files[path].decode('utf-8'), notice, since, today)
            errors += e
            reviews += r
    return errors, reviews


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('plugin', help='Plugin directory at the repository root.')
    parser.add_argument('--depuis', type=date.fromisoformat, required=True,
                        help='Start date of the lot preparation (AAAA-MM-JJ).')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = {p.relative_to(root).as_posix(): p.read_bytes()
             for p in (root / args.plugin).rglob('*') if p.is_file()}
    errors, reviews = check_plugin(files, args.plugin, args.depuis)
    print(json.dumps({'plugin': args.plugin, 'depuis': str(args.depuis), 'errors': errors,
                      'reviews': len(reviews)}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
