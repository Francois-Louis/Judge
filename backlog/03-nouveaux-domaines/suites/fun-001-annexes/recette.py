"""FUN-001: run actual CLI fixtures on a detached package, without personal data.

Not an OS sandbox: existing authentication/HOME remain accessible to the CLI.
No web, shell, agent or mutation tools; no durable session persistence.
Raw stream, resource accesses, output and errors are retained per fixture.
Usage: python recette.py --claude <binary> --workspace <outside-checkout>
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude', required=True, type=Path)
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--case', action='append')
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    if workspace == ROOT or workspace.is_relative_to(ROOT):
        parser.error('workspace must be outside the checkout')
    workspace.mkdir(parents=True, exist_ok=True)
    package = workspace / 'funeral-legal'
    if package.exists():
        parser.error('use a fresh workspace; existing package refused')
    shutil.copytree(ROOT / 'funeral-legal', package)
    project = workspace / 'project'
    project.mkdir()
    out = HERE / 'executions'
    out.mkdir(exist_ok=True)
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(('CLAUDE', 'ANTHROPIC', 'MCP_'))}
    env['PYTHONUTF8'] = '1'
    fixtures = json.loads((HERE / 'fixtures.json').read_text(encoding='utf-8'))
    cases = args.case or list(fixtures)
    if any(case not in fixtures for case in cases):
        parser.error('unknown fixture')
    inventory = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in package.rglob('*') if p.is_file()}
    (out / 'package.json').write_text(json.dumps(inventory, indent=2) + '\n', encoding='utf-8')

    def run(case):
        prompt = '/judge-fr-eu-funeral-legal:funeral-quote-review ' + fixtures[case]
        command = [str(args.claude.resolve()), '-p', prompt, '--plugin-dir', str(package),
                   '--setting-sources', 'project', '--strict-mcp-config',
                   '--tools', 'Read,Glob,Grep,Skill', '--allowedTools', 'Read Glob Grep Skill',
                   '--disallowedTools', 'Write Edit NotebookEdit Bash Agent Task WebFetch WebSearch',
                   '--output-format', 'stream-json', '--verbose', '--max-budget-usd', '2',
                   '--no-session-persistence']
        try:
            result = subprocess.run(command, cwd=project, env=env, capture_output=True,
                                    encoding='utf-8', errors='replace', timeout=240)
            stdout, stderr, code = result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout or b''
            stderr = exc.stderr or b''
            stdout = stdout.decode('utf-8', errors='replace') if isinstance(stdout, bytes) else stdout
            stderr = stderr.decode('utf-8', errors='replace') if isinstance(stderr, bytes) else stderr
            stderr += '\nTIMEOUT 240s'
            code = None
        # Paths are not needed to replay the fictional scenarios.
        for original, substitute in [(str(workspace), '<workspace>'),
                                      (str(ROOT), '<checkout>'),
                                      (str(Path.home()), '<home>')]:
            for spelling in (original, original.replace('\\', '/'),
                             original.replace('\\', '\\\\')):
                stdout, stderr = stdout.replace(spelling, substitute), stderr.replace(spelling, substitute)
        (out / (case + '.jsonl')).write_text(stdout, encoding='utf-8')
        events = []
        for line in stdout.splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        outputs = [event for event in events if event.get('type') == 'result']
        final = outputs[-1] if outputs else {}
        (out / (case + '.md')).write_text(final.get('result', '') + '\n', encoding='utf-8')
        (out / (case + '-errors.txt')).write_text(stderr, encoding='utf-8')
        status = {'case': case, 'returncode': code, 'subtype': final.get('subtype'),
                  'is_error': final.get('is_error'), 'errors': final.get('errors', []),
                  'initialized': any(e.get('subtype') == 'init' for e in events),
                  'resource_reads': [block.get('input', {}).get('file_path')
                                     for e in events if e.get('type') == 'assistant'
                                     for block in e.get('message', {}).get('content', [])
                                     if block.get('type') == 'tool_use' and block.get('name') == 'Read'],
                  'runtime_status': 'blocked-quota' if any(
                      e.get('type') == 'rate_limit_event' and
                      e.get('rate_limit_info', {}).get('status') == 'rejected'
                      for e in events) else ('completed' if code == 0 and
                                            final.get('subtype') == 'success' and final.get('result') and
                                            not final.get('is_error')
                                            else 'failed-or-incomplete')}
        print(json.dumps(status), flush=True)
        return status

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(run, cases))
    (out / 'results.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    if inventory != {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in package.rglob('*') if p.is_file()}:
        raise RuntimeError('package changed during fixture execution')
    return 0 if all(r['runtime_status'] == 'completed' for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())
