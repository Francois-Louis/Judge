#!/usr/bin/env python3
"""FUN-001: detached package evidence; no personal auth/profile imported.

python controles.py --claude <path/to/claude.exe>
Installation is local to a disposable CLI configuration, not a skill run.
Fixtures remain unexecuted if that configuration has no authenticated client.
"""

import argparse
from datetime import datetime, timezone
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
PLUGIN = 'funeral-legal'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude', type=Path)
    args = parser.parse_args()
    cli = args.claude or shutil.which('claude')
    result = {'story': 'FUN-001', 'checked_at': datetime.now(timezone.utc).isoformat(),
              'timezone': 'Europe/Paris', 'commands': [], 'checks': {},
              'skill_execution': 'non-execute', 'reader': 'non-execute',
              'source_revision': subprocess.check_output(
                  ['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()}
    with tempfile.TemporaryDirectory(prefix='judge-fun001-') as temporary:
        work = Path(temporary)
        artifact = work / 'market' / PLUGIN
        shutil.copytree(ROOT / PLUGIN, artifact,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        checker = work / 'tools/check-plugin-package.py'
        checker.parent.mkdir()
        shutil.copyfile(ROOT / 'scripts/check-plugin-package.py', checker)
        result['checker_sha256'] = sha(checker)
        env = {k: v for k, v in os.environ.items()
               if not k.upper().startswith(('CLAUDE', 'ANTHROPIC', 'MCP_', 'JUDGE_'))}
        for variable, directory in [('HOME', 'home'), ('USERPROFILE', 'home'),
                                    ('CLAUDE_CONFIG_DIR', 'config'), ('TEMP', 'tmp'), ('TMP', 'tmp')]:
            (work / directory).mkdir(exist_ok=True)
            env[variable] = str(work / directory)
        env['PYTHONUTF8'] = '1'

        def run(label, command, cwd=artifact):
            try:
                proc = subprocess.run(list(map(str, command)), cwd=cwd, env=env,
                                      capture_output=True, text=True, encoding='utf-8',
                                      errors='replace', timeout=60)
                record = {'label': label, 'args': list(map(str, command)),
                          'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
                if label == 'auth-status':
                    auth = json.loads(proc.stdout)
                    record['stdout'] = json.dumps({k: auth.get(k) for k in
                                                    ('loggedIn', 'authMethod', 'apiProvider')})
                    result['client_ready'] = auth.get('loggedIn') is True
            except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
                record = {'label': label, 'state': 'non-execute-ou-interrompu', 'error': str(exc)}
            for key in ('stdout', 'stderr', 'error'):
                if key in record:
                    record[key] = record[key].replace(str(work), '<RECETTE>').replace(str(ROOT), '<CHECKOUT>')
            record['args'] = [str(a).replace(str(work), '<RECETTE>').replace(str(ROOT), '<CHECKOUT>')
                              for a in record.get('args', [])]
            result['commands'].append(record)
            return record

        files = lambda: {p.relative_to(artifact).as_posix(): sha(p)
                         for p in sorted(artifact.rglob('*')) if p.is_file()}
        result['package'] = files()
        archive = Path(shutil.make_archive(str(work / PLUGIN), 'zip', artifact))
        result['archive'] = {'name': archive.name, 'sha256': sha(archive),
                             'bytes': archive.stat().st_size, 'retention': 'jetable, inventaire conserve'}
        copies = {'LICENSE': 'LICENSE', 'scripts/judge_store.py': 'scripts/judge_store.py',
                  'references/isolation.md': 'references/isolation.md',
                  'references/company-profile-template.md': 'references/company-profile-template.md',
                  'references/dashboard-template.md': 'references/dashboard-template.md',
                  'references/shared/research-citation-method.md': 'references/research-citation-method.md'}
        result['copies'] = {dst: {'source_sha256': sha(ROOT / src),
                                  'embedded_sha256': sha(artifact / dst)} for dst, src in copies.items()}
        result['checks']['copies_identical'] = all(v['source_sha256'] == v['embedded_sha256']
                                                    for v in result['copies'].values())
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        manifest = json.loads((artifact / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        entry = next(p for p in market['plugins'] if p['name'] == manifest['name'])
        result['checks']['marketplace_matches'] = all(entry[k] == manifest[k]
                                                       for k in ('name', 'description', 'author'))
        command = [sys.executable, checker, artifact]
        if cli:
            command += ['--schema', '--claude', cli]
        checked = run('detached-package', command)
        output = checked.get('stdout', '')
        result['checks']['no_structure_errors'] = (checked.get('exit_code') in (0, 2)
                                                   and 'STRUCTURE ECHEC' not in output)
        result['structure_reviews'] = [line for line in output.splitlines() if line.startswith('A_RELIRE ')]
        result['schema'] = 'reussi' if 'SCHEMA OK' in output else 'non-valide'
        if cli:
            run('cli-version', [cli, '--version'])
            run('marketplace-schema', [cli, 'plugin', 'validate', ROOT / '.claude-plugin/marketplace.json'])
            detached = artifact.parent / '.claude-plugin/marketplace.json'
            detached.parent.mkdir()
            detached.write_text(json.dumps(dict(market, plugins=[entry]), ensure_ascii=False,
                                            indent=2)+'\n', encoding='utf-8')
            run('local-marketplace-add', [cli, 'plugin', 'marketplace', 'add', artifact.parent])
            installed = run('local-plugin-install', [cli, 'plugin', 'install', manifest['name'] + '@judge-fr-eu'])
            result['checks']['local_installation'] = installed.get('exit_code') == 0
            run('local-plugin-list', [cli, 'plugin', 'list'])
            run('auth-status', [cli, 'auth', 'status'])
        result['checks']['package_unchanged'] = result['package'] == files()
        result['runtime_limit'] = ('Aucune authentification importee ou effectuee. Pas de skill invoque ; '
                                   'fixtures Q01-Q12 et lecteur reel non executes. Variables jetables sous '
                                   'le meme compte Windows, pas de sandbox OS.')
    (HERE / 'resultats-paquet.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n',
                                               encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('checks', 'schema', 'structure_reviews', 'skill_execution')},
                     ensure_ascii=True, indent=2))
    if not all(result['checks'].values()):
        return 1
    return 2 if result['structure_reviews'] or result['schema'] != 'reussi' else 0


if __name__ == '__main__':
    sys.exit(main())
