#!/usr/bin/env python3
"""CRIM-001: detached package checks and optional fixture invocations.

Adapted from the CONSO-001 maintenance harness. Disposable HOME/config only;
no personal authentication imported. No OS sandbox or legal success inferred.
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
PLUGIN = 'criminal-legal'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude', type=Path)
    parser.add_argument('--run-fixtures', action='store_true')
    args = parser.parse_args()
    cli = str(args.claude.resolve()) if args.claude else shutil.which('claude')
    fixtures = json.loads((HERE / 'fixtures.json').read_text(encoding='utf-8'))
    report = {
        'story': 'CRIM-001', 'checked_at': datetime.now(timezone.utc).isoformat(),
        'timezone': 'Europe/Paris', 'source_revision': subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'commands': [], 'checks': {}, 'fixtures': {}, 'reader': 'non-execute',
        'isolation': 'Disposable paths under the same Windows account; no OS sandbox.',
    }
    with tempfile.TemporaryDirectory(prefix='judge-crim001-') as temporary:
        work = Path(temporary)
        artifact = work / 'market' / PLUGIN
        shutil.copytree(ROOT / PLUGIN, artifact,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        checker = work / 'tools/check-plugin-package.py'
        checker.parent.mkdir()
        shutil.copyfile(ROOT / 'scripts/check-plugin-package.py', checker)
        project = work / 'project'
        project.mkdir()
        env = {k: v for k, v in os.environ.items()
               if not k.upper().startswith(('CLAUDE', 'ANTHROPIC', 'MCP_', 'JUDGE_'))}
        for variable, directory in [('HOME', 'home'), ('USERPROFILE', 'home'),
                                    ('CLAUDE_CONFIG_DIR', 'config'), ('TEMP', 'tmp'), ('TMP', 'tmp')]:
            (work / directory).mkdir(exist_ok=True)
            env[variable] = str(work / directory)
        env['PYTHONUTF8'] = '1'

        def redact(value):
            for original, replacement in [(str(work), '<RECETTE>'), (str(ROOT), '<CHECKOUT>'),
                                          (str(Path.home()), '<HOME>')]:
                for spelling in (original, original.replace('\\', '/'),
                                 original.replace('\\', '\\\\')):
                    value = value.replace(spelling, replacement)
            return value

        def run(label, command, cwd=artifact, timeout=60):
            try:
                proc = subprocess.run(list(map(str, command)), cwd=cwd, env=env,
                                      capture_output=True, text=True, encoding='utf-8',
                                      errors='replace', timeout=timeout)
                record = {'label': label, 'args': list(map(str, command)),
                          'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
                if label == 'auth-status':
                    auth = json.loads(proc.stdout)
                    report['client_ready'] = auth.get('loggedIn') is True
                    record['stdout'] = json.dumps({k: auth.get(k) for k in
                                                    ('loggedIn', 'authMethod', 'apiProvider')})
            except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
                record = {'label': label, 'state': 'non-execute-ou-interrompu', 'error': str(exc)}
            record = json.loads(redact(json.dumps(record, ensure_ascii=False)))
            report['commands'].append(record)
            return record

        inventory = lambda: {p.relative_to(artifact).as_posix(): sha(p)
                             for p in sorted(artifact.rglob('*')) if p.is_file()}
        report['package'] = inventory()
        report['checker_sha256'] = sha(checker)
        archive = Path(shutil.make_archive(str(work / PLUGIN), 'zip', artifact))
        report['archive'] = {'sha256': sha(archive), 'bytes': archive.stat().st_size,
                             'retention': 'disposable archive; inventory retained'}
        copies = {'LICENSE': 'LICENSE', 'scripts/judge_store.py': 'scripts/judge_store.py',
                  'references/isolation.md': 'references/isolation.md',
                  'references/company-profile-template.md': 'references/company-profile-template.md',
                  'references/dashboard-template.md': 'references/dashboard-template.md',
                  'references/shared/research-citation-method.md': 'references/research-citation-method.md'}
        report['copies'] = {dst: {'source_sha256': sha(ROOT / src),
                                  'embedded_sha256': sha(artifact / dst)} for dst, src in copies.items()}
        report['checks']['copies_identical'] = all(v['source_sha256'] == v['embedded_sha256']
                                                  for v in report['copies'].values())
        command = [sys.executable, checker, artifact]
        if cli:
            command += ['--schema', '--claude', cli]
        structure = run('package', command)
        stdout = structure.get('stdout', '')
        report['checks']['structure_without_errors'] = 'STRUCTURE ECHEC' not in stdout and 'STRUCTURE ' in stdout
        report['structure'] = 'incomplet' if 'STRUCTURE INCOMPLET' in stdout else 'voir-trace'
        report['schema'] = 'reussi' if 'SCHEMA OK' in stdout else 'non-reussi-ou-non-execute'
        manifest = json.loads((artifact / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        entry = next(e for e in market['plugins'] if e['source'] == './' + PLUGIN)
        report['checks']['marketplace_matches'] = all(entry[k] == manifest[k]
                                                      for k in ('name', 'description', 'author'))
        if cli:
            run('client-version', [cli, '--version'])
            run('marketplace-schema', [cli, 'plugin', 'validate', ROOT / '.claude-plugin/marketplace.json'])
            detached = artifact.parent / '.claude-plugin/marketplace.json'
            detached.parent.mkdir()
            detached.write_text(json.dumps(dict(market, plugins=[entry]), ensure_ascii=False,
                                            indent=2) + '\n', encoding='utf-8')
            run('local-marketplace-add', [cli, 'plugin', 'marketplace', 'add', artifact.parent])
            installed = run('local-plugin-install', [cli, 'plugin', 'install', manifest['name'] + '@judge-fr-eu'])
            report['checks']['local_installation'] = installed.get('exit_code') == 0
            run('local-plugin-list', [cli, 'plugin', 'list'])
            run('auth-status', [cli, 'auth', 'status'])
        for case, fixture in fixtures.items():
            report['fixtures'][case] = {'status': 'non-execute', 'resources_read': [],
                                        'reason': 'Authenticated disposable client unavailable.'}
            if not (args.run_fixtures and cli and report.get('client_ready')):
                continue
            prompt = '/judge-fr-eu-criminal-legal:summons-reading ' + fixture['input']
            result = run(case, [cli, '-p', prompt, '--plugin-dir', str(artifact),
                               '--setting-sources', 'project',
                               '--strict-mcp-config', '--tools', 'Read,Glob,Grep,Skill',
                               '--allowedTools', 'Read Glob Grep Skill', '--disallowedTools',
                               'Write Edit NotebookEdit Bash Agent Task WebFetch WebSearch',
                               '--output-format', 'stream-json', '--verbose', '--max-budget-usd', '2',
                               '--no-session-persistence'], cwd=project, timeout=60)
            # Keep actual tool events and output, never manufacture fixture responses.
            report['fixtures'][case] = {'status': 'tentative-voir-trace', 'legal_review': 'non-execute',
                                        'exit_code': result.get('exit_code')}
        report['checks']['package_unchanged'] = report['package'] == inventory()
    (HERE / 'resultats-paquet.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                                               encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('checks', 'structure', 'schema', 'fixtures')},
                     ensure_ascii=True, indent=2))
    if not all(report['checks'].values()):
        return 1
    return 2 if report['structure'] == 'incomplet' or report['schema'] != 'reussi' else 0


if __name__ == '__main__':
    sys.exit(main())
