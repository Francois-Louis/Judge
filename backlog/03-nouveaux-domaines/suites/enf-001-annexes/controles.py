"""ENF-001: detached artifact, shared copies and maintenance checks.

Does not install a plugin or evaluate model/legal behavior. Use recette.py
separately for client fixtures. All artifacts are created outside the checkout.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude', required=True, type=Path)
    args = parser.parse_args()
    workspace = Path(tempfile.mkdtemp(prefix='judge-enf001-check-'))
    package = workspace / 'enforcement-legal'
    shutil.copytree(ROOT / 'enforcement-legal', package)
    checker = workspace / 'check-plugin-package.py'
    shutil.copyfile(ROOT / 'scripts/check-plugin-package.py', checker)
    env = dict(os.environ, PYTHONUTF8='1')

    def run(command, cwd=ROOT):
        completed = subprocess.run([str(x) for x in command], cwd=cwd, env=env,
                                   capture_output=True, encoding='utf-8',
                                   errors='replace', timeout=240)
        output = completed.stdout + completed.stderr
        for original, replacement in [(str(workspace), '<workspace>'),
                                      (str(ROOT), '<checkout>'),
                                      (str(Path.home()), '<home>')]:
            output = output.replace(original, replacement)
        return {'returncode': completed.returncode, 'output': output}

    copies = {}
    for source, target in [
        ('LICENSE', 'LICENSE'),
        ('scripts/judge_store.py', 'scripts/judge_store.py'),
        ('references/isolation.md', 'references/isolation.md'),
        ('references/company-profile-template.md', 'references/company-profile-template.md'),
        ('references/dashboard-template.md', 'references/dashboard-template.md'),
        ('references/research-citation-method.md', 'references/shared/research-citation-method.md'),
    ]:
        a, b = (ROOT / source).read_bytes(), (package / target).read_bytes()
        copies[target] = {'source_sha256': hashlib.sha256(a).hexdigest(),
                          'artifact_sha256': hashlib.sha256(b).hexdigest(), 'identical': a == b}
    results = {'copies': copies, 'checks': {}}
    # Keep concurrent, untracked domain work out of this story's evidence.
    # Copy the Git index plus this new package into a separate maintenance
    # tree, and retain the committed marketplace plus ENF-001 only.
    snapshot = workspace / 'maintenance'
    snapshot.mkdir()
    subprocess.run(['git', 'checkout-index', '--all',
                    '--prefix=' + snapshot.as_posix() + '/'], cwd=ROOT, check=True)
    shutil.copytree(package, snapshot / 'enforcement-legal', dirs_exist_ok=True)
    committed = subprocess.run(['git', 'show', 'HEAD:.claude-plugin/marketplace.json'],
                               cwd=ROOT, check=True, capture_output=True).stdout
    market = json.loads(committed)
    current = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    entry = next(p for p in current['plugins'] if p['source'] == './enforcement-legal')
    if not any(p['source'] == entry['source'] for p in market['plugins']):
        market['plugins'].append(entry)
    (snapshot / '.claude-plugin/marketplace.json').write_text(
        json.dumps(market, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    results['isolation_marketplace_plugins'] = [p['name'] for p in market['plugins']]
    commands = {
        'package': ([sys.executable, checker, package, '--schema', '--claude', args.claude.resolve()], package),
        'marketplace_schema': ([args.claude.resolve(), 'plugin', 'validate', snapshot / '.claude-plugin/marketplace.json'], snapshot),
        'source_reviews': ([sys.executable, ROOT / 'scripts/source_reviews.py', 'enforcement-legal', '--depuis', '2026-10-17'], ROOT),
        'isolation': ([sys.executable, snapshot / 'scripts/test-base008-isolation.py'], snapshot),
        'tool_scope': ([sys.executable, ROOT / 'scripts/lint-tool-scope.py'], ROOT),
        'version_bump': ([sys.executable, ROOT / 'scripts/check-version-bump.py'], ROOT),
    }
    for name, (command, cwd) in commands.items():
        results['checks'][name] = run(command, cwd)
        print(name, results['checks'][name]['returncode'], flush=True)
    inventory = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in package.rglob('*') if p.is_file()}
    results['artifact_inventory'] = inventory
    archive = Path(shutil.make_archive(str(workspace / 'enforcement-legal-0.1.0'), 'zip', workspace, 'enforcement-legal'))
    results['archive_sha256'] = hashlib.sha256(archive.read_bytes()).hexdigest()
    results['artifact_path'] = str(package)
    results['archive_path'] = str(archive)
    (HERE / 'validation.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Evidence: validation.json', flush=True)
    return int(not all(c['identical'] for c in copies.values()) or
               any(r['returncode'] != (2 if k == 'package' else 0)
                   for k, r in results['checks'].items()))


if __name__ == '__main__':
    sys.exit(main())
