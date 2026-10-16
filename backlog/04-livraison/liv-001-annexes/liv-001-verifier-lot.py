"""Vérification de l'artefact LIV-001, sans session de modèle ni publication.

python -X utf8 backlog/04-livraison/liv-001-annexes/liv-001-verifier-lot.py --zip <lot.zip> \
    --work <dossier-neuf-hors-checkout> --claude <claude.exe> \
    --output backlog/04-livraison/liv-001-annexes/liv-001-resultats.json

Étapes : extraction de l'archive dans un dossier neuf ; contrôle de
l'inventaire ; comparaison au paquet testé par BASE-011 ; recherche de
chemins actifs de l'origine ; contrôleur BASE-006 avec schéma officiel ;
validation du marketplace du lot ; installation dans une configuration client
jetable (CLAUDE_CONFIG_DIR, HOME et USERPROFILE temporaires, variables de la
session appelante retirées, mises à jour automatiques désactivées) ;
comparaison de la copie installée. Aucune commande de skill n'est invoquée :
cela exige une session authentifiée par l'utilisateur.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
PLUGIN = 'judge-fr-eu-employment-legal'
MARKET = 'judge-fr-eu'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def tree(base):
    return {p.relative_to(base).as_posix(): digest(p.read_bytes())
            for p in sorted(base.rglob('*')) if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--claude', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    work = args.work.resolve()
    if work == ROOT or ROOT in work.parents or work.exists():
        sys.exit('refused: work directory must be new and outside the checkout')
    checks, commands = {}, []

    def record(name, problems, **facts):
        checks[name] = {'status': 'failed' if problems else 'passed', **facts, 'problems': problems}

    zip_bytes = args.zip.read_bytes()
    extract = work / 'extract'
    with zipfile.ZipFile(args.zip) as archive:
        names = archive.namelist()
        bad = [n for n in names if n.startswith('/') or '..' in Path(n).parts or '\\' in n]
        if bad:
            sys.exit(f'refused: unsafe archive entries {bad}')
        archive.extractall(extract)
    roots = {n.split('/', 1)[0] for n in names}
    lot = extract / roots.pop()
    inventory = json.loads((lot / 'lot-inventory.json').read_text(encoding='utf-8'))
    actual = {k: v for k, v in tree(lot).items() if k != 'lot-inventory.json'}
    record('archive_matches_inventory',
           [] if actual == inventory['files'] else [{'missing': sorted(set(inventory['files']) - set(actual)),
                                                     'extra': sorted(set(actual) - set(inventory['files'])),
                                                     'different': sorted(k for k in actual if inventory['files'].get(k) not in (None, actual[k]))}],
           zip_sha256=digest(zip_bytes), files=len(actual), source=inventory['source'],
           plugins=inventory['plugins'], roots=sorted(roots) + [lot.name])

    market = json.loads((lot / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    package = lot / 'employment-legal'
    manifest = json.loads((package / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    problems = []
    if [p['name'] for p in market['plugins']] != [PLUGIN] or market['name'] != MARKET:
        problems.append('lot marketplace must list only the delivered plugin under judge-fr-eu')
    for field in ('name', 'description', 'author'):
        if market['plugins'][0][field] != manifest[field]:
            problems.append(f'{field} differs between marketplace and manifest')
    others = [d.name for d in lot.iterdir() if d.is_dir() and d.name not in {'.claude-plugin', 'employment-legal'}]
    if others:
        problems.append(f'unexpected directories {others}')
    record('lot_scope', problems, marketplace=market['name'], plugin=manifest['name'],
           version=manifest['version'], top_level=sorted(p.name for p in lot.iterdir()))

    base011 = json.loads((ROOT / 'backlog/00-fondations/base-011-annexes/base-011-resultats.json').read_text(encoding='utf-8'))
    tested = base011['package']['files']
    now = tree(package)
    changed = sorted(k for k in now if tested.get(k) != now[k])
    allowed = {'.claude-plugin/plugin.json', 'README.md', 'NOTICE'}
    record('same_skills_as_base011', [c for c in changed if c not in allowed] +
           sorted(set(tested) - set(now)), base011_revision=base011['source_revision'],
           changed_metadata=changed, unchanged=len(now) - len(changed))

    pattern = re.compile(r'config/claude-for-legal|plugins/cache/claude-for-legal|@claude-for-legal')
    hits = []
    for path in package.rglob('*'):
        if path.is_file():
            for number, line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
                if pattern.search(line):
                    hits.append(f'{path.relative_to(lot).as_posix()}:{number}: {line.strip()[:160]}')
    record('no_active_origin_paths', hits)

    def run(name, argv, env=None):
        result = subprocess.run(argv, capture_output=True, encoding='utf-8', errors='replace', env=env)
        shown = [str(a).replace(str(work), '<work>').replace(str(ROOT), '<checkout>') for a in argv]
        commands.append({'step': name, 'argv': shown, 'exit': result.returncode,
                         'stdout': result.stdout.replace(str(work), '<work>')[-3000:],
                         'stderr': result.stderr.replace(str(work), '<work>')[-2000:]})
        return result

    checker = run('check-plugin-package', [sys.executable, '-X', 'utf8', str(ROOT / 'scripts/check-plugin-package.py'),
                                           str(package), '--schema', '--claude', str(args.claude)])
    schema_ok = 'SCHEMA OK' in checker.stdout
    record('package_checker_schema', [] if schema_ok else ['schema not OK'],
           exit=checker.returncode, structure_line=next((l for l in checker.stdout.splitlines() if 'STRUCTURE' in l.upper()), None),
           note='Structure INCOMPLET with A_RELIRE items is the known BASE-006 manual-review state, not a schema failure.')

    env = {k: v for k, v in os.environ.items() if not k.upper().startswith(('CLAUDE', 'ANTHROPIC'))}
    home = work / 'home'
    home.mkdir()
    env.update({'CLAUDE_CONFIG_DIR': str(work / 'config'), 'HOME': str(home), 'USERPROFILE': str(home),
                'DISABLE_AUTOUPDATER': '1', 'CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC': '1'})
    claude = str(args.claude)
    version = run('client-version', [claude, '--version'], env)
    validate = run('validate-lot-marketplace', [claude, 'plugin', 'validate', str(lot / '.claude-plugin/marketplace.json')], env)
    validate_plugin = run('validate-plugin', [claude, 'plugin', 'validate', str(package)], env)
    before = sorted(p.relative_to(work).as_posix() for p in (work / 'config').rglob('*')) if (work / 'config').exists() else []
    add = run('marketplace-add', [claude, 'plugin', 'marketplace', 'add', str(lot)], env)
    install = run('plugin-install', [claude, 'plugin', 'install', f'{PLUGIN}@{MARKET}', '--scope', 'user'], env)
    listing = run('plugin-list', [claude, 'plugin', 'list'], env)
    markets = run('marketplace-list', [claude, 'plugin', 'marketplace', 'list'], env)
    problems = [c['step'] for c in commands[-7:] if c['exit'] != 0]
    if PLUGIN not in listing.stdout or '0.2.1' not in listing.stdout:
        problems.append('installed plugin or version not listed')
    if 'claude-for-legal' in listing.stdout + markets.stdout:
        problems.append('origin marketplace or plugin present')
    record('isolated_install', problems, client=version.stdout.strip(), config_before_add=before,
           validate_marketplace_exit=validate.returncode, validate_plugin_exit=validate_plugin.returncode)

    installed = [p.parent.parent for p in (work / 'config').rglob('plugin.json')
                 if p.parent.name == '.claude-plugin' and json.loads(p.read_text(encoding='utf-8')).get('name') == PLUGIN]
    problems = []
    if len(installed) != 1:
        problems.append(f'expected one installed copy, found {len(installed)}')
    else:
        copy = tree(installed[0])
        if copy != now:
            problems.append({'missing': sorted(set(now) - set(copy)), 'extra': sorted(set(copy) - set(now)),
                             'different': sorted(k for k in copy if now.get(k) not in (None, copy[k]))})
    config_files = sorted(p.relative_to(work).as_posix() for p in (work / 'config').rglob('*') if p.is_file())
    profile_dirs = sorted(p.relative_to(work).as_posix() for p in home.rglob('*'))
    if any('judge-fr-eu/employment-legal' in p for p in profile_dirs):
        problems.append('a profile was created by installation')
    record('installed_copy', problems,
           installed_path=str(installed[0].relative_to(work)) if len(installed) == 1 else None,
           config_files=[f for f in config_files if 'cache' not in f], home_entries=profile_dirs)

    report = {
        'story': 'LIV-001', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'artifact': {'name': args.zip.name, 'sha256': digest(zip_bytes), 'files': len(actual)},
        'checks': checks, 'commands': commands,
        'not_run': ['invocation of a skill in an authenticated model session',
                    'scenarios H01-H16 on the 0.2.1 artifact (BASE-011 ran them on identical skill files)',
                    'independent reader', 'real symbolic-link refusal (WinError 1314 on this workstation)',
                    'push, tag, release or any remote publication'],
        'isolation': 'disposable CLAUDE_CONFIG_DIR, HOME and USERPROFILE; same Windows account; checkout readable',
    }
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for key, value in checks.items():
        print(f"{key}: {value['status']}")
        for problem in value['problems']:
            print(f'  {problem}')
    raise SystemExit(1 if any(v['status'] == 'failed' for v in checks.values()) else 0)


if __name__ == '__main__':
    main()
