"""Fixture filesystem EXIST-011, hors ligne et exclusivement en faux home.

Exerce le helper BASE-008 existant, pas les prompts du hub ni un client.
Usage : python -X utf8 backlog/02-plugins-existants/exist-011-annexes/exist-011-simulation.py
        [--output rapport.json]
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / 'legal-builder-hub/scripts/community_store.py'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(output=None):
    checks = {}
    temp_parent = Path(tempfile.gettempdir()).resolve()
    scratch = Path(tempfile.mkdtemp(prefix='judge-exist011-', dir=temp_parent)).resolve()

    def verify_scratch():
        if scratch.parent != temp_parent or not scratch.name.startswith('judge-exist011-'):
            raise ValueError('Unexpected fixture path; no recursive cleanup permitted')

    verify_scratch()
    try:
        home = scratch / 'fake-home'
        candidate = scratch / 'candidate'
        incoming = scratch / 'incoming'
        slug = 'fixture-revue'
        for folder, label in ((candidate, 'base fictive'), (incoming, 'nouveau candidat fictif')):
            (folder / 'references').mkdir(parents=True)
            (folder / 'SKILL.md').write_text(
                '---\nname: fixture-revue\ndescription: Fixture documentaire sans outil ni action.\n---\n'
                f'\n# {label}\n\nAucun raisonnement juridique ni instruction externe.\n', encoding='utf-8')
            (folder / 'references/methode.md').write_text(label + '\n', encoding='utf-8')
        metadata = scratch / 'metadata.json'
        metadata.write_text(json.dumps({'fixture': True, 'network': False,
                                       'review_scope': 'offline filesystem only'}), encoding='utf-8')

        def invoke(action, name=slug, source=candidate, sha='1' * 40, approved=True):
            # Arguments séparés, --home obligatoire : jamais de home réel.
            command = [sys.executable, '-B', '-X', 'utf8', str(HELPER), action, name,
                       '--home', str(home), '--source', str(source), '--sha', sha,
                       '--metadata', str(metadata)]
            if approved:
                command.append('--approved')
            return subprocess.run(command, cwd=scratch, capture_output=True, encoding='utf-8')

        installed = invoke('install')
        if installed.returncode:
            raise RuntimeError('Fixture setup failed: ' + installed.stderr)
        target = home / '.claude/skills/judge-fr-eu-fixture-revue'
        journal = home / '.claude/plugins/config/judge-fr-eu/legal-builder-hub/install-log.yaml'
        # Personnalisation après installation, sans falsifier l'empreinte au journal.
        custom = '\nAdaptation locale fictive : consigne France à conserver.\n'
        for p in (target / 'SKILL.md', target / 'references/methode.md'):
            p.write_text(p.read_text(encoding='utf-8') + custom, encoding='utf-8')
        before = {p.relative_to(target).as_posix(): digest(p) for p in target.rglob('*') if p.is_file()}
        journal_before = digest(journal)
        incoming_before = {p.relative_to(incoming).as_posix(): digest(p)
                           for p in incoming.rglob('*') if p.is_file()}
        updated = invoke('update', source=incoming, sha='2' * 40)
        after = {p.relative_to(target).as_posix(): digest(p) for p in target.rglob('*') if p.is_file()}
        incoming_after = {p.relative_to(incoming).as_posix(): digest(p)
                          for p in incoming.rglob('*') if p.is_file()}
        events = json.loads(journal.read_text(encoding='utf-8'))['events']
        backups = home / '.claude/plugins/config/judge-fr-eu/legal-builder-hub/backups'
        preservation = (updated.returncode != 0
                        and 'preserve and compare local edits' in updated.stderr
                        and before == after and journal_before == digest(journal)
                        and incoming_before == incoming_after
                        and [e['action'] for e in events] == ['install']
                        and not backups.exists())
        checks['customized_update_preserved'] = {
            'status': 'passed' if preservation else 'failed',
            'exit_code': updated.returncode, 'message': updated.stderr.strip(),
            'installed_before': before, 'installed_after': after,
            'journal_unchanged': journal_before == digest(journal),
            'candidate_unchanged': incoming_before == incoming_after,
            'events': [e['action'] for e in events], 'backup_created': backups.exists(),
        }
        internal = invoke('install', name='commercial-legal')
        checks['internal_identity_refused'] = {
            'status': 'passed' if internal.returncode != 0
            and 'expected an unprefixed community skill slug' in internal.stderr
            and journal_before == digest(journal) else 'failed',
            'exit_code': internal.returncode, 'message': internal.stderr.strip(),
        }
        unapproved = invoke('install', name='fixture-sans-accord', approved=False)
        checks['filesystem_cli_requires_workflow_flag'] = {
            'status': 'passed' if unapproved.returncode != 0
            and 'complete trust review and explicit approval' in unapproved.stderr
            and journal_before == digest(journal) else 'failed',
            'exit_code': unapproved.returncode, 'message': unapproved.stderr.strip(),
            'limit': '--approved is an attestation by the caller, not independent proof of human approval.',
        }
    finally:
        # Chemin absolu vérifié dans le seul répertoire temporaire nommé ci-dessus.
        verify_scratch()
        shutil.rmtree(scratch)
    result = {
        'story': 'EXIST-011', 'date': '2026-10-16',
        'scope': 'existing BASE-008 filesystem helper; disposable fake home only',
        'helper_sha256': digest(HELPER), 'checks': checks,
        'network': False, 'real_home_accessed': False, 'temporary_tree_removed': not scratch.exists(),
        'not_run': ['hub skill or model invocation', 'actual registry discovery', 'legal accuracy review',
                    'client installation/reload', 'external notification', 'real human approval UX'],
    }
    if output:
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = run(args.output)
    for name, check in report['checks'].items():
        print(f"{name}: {check['status']}")
    raise SystemExit(int(any(c['status'] != 'passed' for c in report['checks'].values())))
