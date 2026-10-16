#!/usr/bin/env python3
"""COM-001: package/schema and guarded-storage evidence, never LLM execution.

Run from any directory: python controles.py [--claude path/to/claude.exe].
All CLI state and helper fixtures are disposable. No personal profile or auth
configuration is copied. The optional local installation does not invoke skills.
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


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude', type=Path)
    args = parser.parse_args()
    result = {'story': 'COM-001', 'checked_at': datetime.now(timezone.utc).isoformat(),
              'timezone': 'Europe/Paris', 'skill_execution': 'non-execute',
              'reader': 'non-execute', 'commands': [], 'checks': {}}
    result['source_revision'] = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    with tempfile.TemporaryDirectory(prefix='judge-com001-') as temporary:
        sandbox = Path(temporary)
        artifact = sandbox / 'market' / 'commercial-legal'
        shutil.copytree(ROOT / 'commercial-legal', artifact,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        tool = sandbox / 'tools' / 'check-plugin-package.py'
        tool.parent.mkdir()
        shutil.copy2(ROOT / 'scripts' / tool.name, tool)
        env = {k: v for k, v in os.environ.items()
               if not k.upper().startswith(('CLAUDE', 'ANTHROPIC', 'MCP_', 'JUDGE_'))}
        for variable, directory in [('HOME', 'home'), ('USERPROFILE', 'home'),
                                    ('CLAUDE_CONFIG_DIR', 'config'), ('TEMP', 'tmp'), ('TMP', 'tmp')]:
            (sandbox / directory).mkdir(exist_ok=True)
            env[variable] = str(sandbox / directory)
        env['PYTHONIOENCODING'] = 'utf-8'

        def run(label, command, *, cwd=artifact, data=None):
            try:
                proc = subprocess.run(list(map(str, command)), cwd=cwd, env=env,
                                      input=data, text=True, encoding='utf-8', errors='replace',
                                      capture_output=True, timeout=60)
                record = {'label': label, 'args': list(map(str, command)),
                          'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
            except (OSError, subprocess.TimeoutExpired) as exc:
                record = {'label': label, 'state': 'non-execute-ou-interrompu', 'error': str(exc)}
            # Keep paths portable and do not retain account identifiers.
            if label == 'auth-status' and record.get('stdout', '').lstrip().startswith('{'):
                auth = json.loads(record['stdout'])
                record['stdout'] = json.dumps({k: auth.get(k) for k in
                                                ('loggedIn', 'authMethod', 'apiProvider')})
            record = json.loads(json.dumps(record).replace(
                json.dumps(str(sandbox))[1:-1], '<RECETTE>').replace(
                json.dumps(str(ROOT))[1:-1], '<CHECKOUT>'))
            result['commands'].append(record)
            return record

        result['package'] = {p.relative_to(artifact).as_posix(): sha(p)
                             for p in sorted(artifact.rglob('*')) if p.is_file()}
        archive = Path(shutil.make_archive(str(sandbox / 'commercial-legal'), 'zip', artifact))
        result['archive'] = {'name': archive.name, 'sha256': sha(archive),
                             'bytes': archive.stat().st_size, 'retention': 'jetable ; inventaire conserve'}
        source_method = ROOT / 'references/research-citation-method.md'
        method = artifact / 'references/shared/research-citation-method.md'
        result['method'] = {'source_sha256': sha(source_method), 'embedded_sha256': sha(method)}
        result['checks']['method_identical'] = sha(source_method) == sha(method)
        for name, original in [('isolation.md', ROOT / 'references/isolation.md'),
                               ('judge_store.py', ROOT / 'scripts/judge_store.py')]:
            copy = artifact / ('scripts' if name.endswith('.py') else 'references') / name
            result['checks'][name + '_identical'] = sha(copy) == sha(original)
        for link in ['references/isolation.md', 'references/shared/research-citation-method.md',
                     'references/orientation-commerciale.md', 'scripts/judge_store.py']:
            result['checks']['local:' + link] = (artifact / link).is_file()
        manifest = json.loads((artifact / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        entry = next(p for p in market['plugins'] if p['name'] == manifest['name'])
        result['checks']['marketplace_matches'] = all(entry[k] == manifest[k]
                                                       for k in ['name', 'description', 'author'])
        checker_args = [sys.executable, tool, artifact]
        cli = args.claude or shutil.which('claude')
        if cli:
            checker_args += ['--schema', '--claude', cli]
        checked = run('detached-package', checker_args)
        result['checks']['no_structure_errors'] = ('exit_code' in checked and
                                                  'ECHEC ' not in checked['stdout'])
        result['checks']['structure_review_count'] = checked.get('stdout', '').count('A_RELIRE ')
        result['schema'] = 'reussi' if 'SCHEMA OK' in checked.get('stdout', '') else 'non-valide'
        # An original-distribution sentinel must not become the fork profile.
        home = sandbox / 'home'
        original = home / '.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md'
        original.parent.mkdir(parents=True)
        original.write_text('ORIGINAL-SENTINEL\n', encoding='utf-8')
        sentinel_hash = sha(original)
        helper = artifact / 'scripts/judge_store.py'
        missing = run('missing-profile', [sys.executable, helper, 'read', 'CLAUDE.md', '--home', home])
        payload = json.loads(missing['stdout'])
        result['checks']['missing_stays_missing'] = (payload['status'] == 'interview-required'
                                                      and payload['content'] is None)
        result['checks']['missing_read_did_not_create_profile'] = not (
            home / '.claude/plugins/config/judge-fr-eu/commercial-legal/CLAUDE.md').exists()
        refused = run('traversal-refused', [sys.executable, helper, 'read', '../company-profile.md',
                                            '--home', home])
        result['checks']['traversal_refused'] = refused.get('exit_code') == 1
        result['checks']['original_preserved'] = sha(original) == sentinel_hash
        if cli:
            run('cli-version', [cli, '--version'])
            run('marketplace-schema', [cli, 'plugin', 'validate', ROOT / '.claude-plugin/marketplace.json'])
            # Local-only marketplace copy; installation requires no account or publication.
            detached_market = dict(market, plugins=[entry])
            market_path = artifact.parent / '.claude-plugin/marketplace.json'
            market_path.parent.mkdir()
            market_path.write_text(json.dumps(detached_market, ensure_ascii=False, indent=2)+'\n',
                                   encoding='utf-8')
            run('local-marketplace-add', [cli, 'plugin', 'marketplace', 'add', artifact.parent])
            run('local-plugin-install', [cli, 'plugin', 'install', manifest['name'] + '@judge-fr-eu'])
            run('local-plugin-list', [cli, 'plugin', 'list'])
            run('auth-status', [cli, 'auth', 'status'])
        else:
            result['cli'] = 'absente du PATH ; fournir --claude pour tester le schema'
        result['checks']['package_unchanged_by_checks'] = result['package'] == {
            p.relative_to(artifact).as_posix(): sha(p) for p in sorted(artifact.rglob('*')) if p.is_file()}
        result['isolation_limit'] = ('Variables et repertoire jetables sous le meme compte Windows ; '
                                     'pas de sandbox OS ni de skill execute. Suppression des donnees de test en fin de controle.')
    target = HERE / 'resultats-paquet.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(target)
    print(json.dumps({'checks': result['checks'], 'schema': result['schema']}, ensure_ascii=True))
    if not all(value is True for key, value in result['checks'].items()
               if key != 'structure_review_count'):
        return 1
    return 2 if result['checks']['structure_review_count'] or result['schema'] != 'reussi' else 0


if __name__ == '__main__':
    sys.exit(main())
