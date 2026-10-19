"""Invoke selected story recipes on detached packages with fictional inputs.

Usage: python scripts/recette-stories.py --claude <binary> --label <new-run>
       --workspace <fresh-directory-outside-checkout> [--story BNK-001]

This is not an OS sandbox: CLI authentication and HOME remain accessible.
Read-only tools, no MCP, shell, agents, writes or durable session persistence.
Execution success is recorded separately from the human verdict on outputs.
Historical runs are never overwritten. A quota rejection stops new requests.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from threading import Event


ROOT = Path(__file__).resolve().parents[1]
DOM = ROOT / 'backlog/03-nouveaux-domaines/suites'
STORIES = {
    'TRAV-002': ('employment-legal', 'wage-hour-qa', ROOT / 'backlog/01-pilote-travail/suites/trav-002-annexes', 'fixtures.json'),
    'COM-001': ('commercial-legal', 'review', ROOT / 'backlog/02-plugins-existants/suites/com-001-annexes', 'pieces-fictives.md'),
    'CONSO-001': ('consumer-legal', 'non-delivery-claim', DOM / 'conso-001-annexes', 'pieces-fictives.md'),
    'CRIM-001': ('criminal-legal', 'summons-reading', DOM / 'crim-001-annexes', 'fixtures.json'),
    'ENF-001': ('enforcement-legal', 'enforcement-act-reading', DOM / 'enf-001-annexes', 'fixtures.json'),
    'BNK-001': ('banking-legal', 'payment-dispute', DOM / 'bnk-001-annexes', 'fixtures.json'),
    'INS-001': ('insurance-legal', 'claim-denial-review', DOM / 'ins-001-annexes', 'fixtures.json'),
    'FUN-001': ('funeral-legal', 'funeral-quote-review', DOM / 'fun-001-annexes', 'fixtures.json'),
    'DOU-001': ('customs-legal', 'import-document-checklist', DOM / 'dou-001-annexes', 'fixtures.json'),
    'DOU-009': ('customs-legal', 'customs-notice-review', DOM / 'dou-009-annexes', 'fixtures.json'),
}


def inventory(package):
    return {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(package.rglob('*')) if p.is_file()}


def fixtures(story):
    _, _, annex, name = STORIES[story]
    source = (annex / name).read_text(encoding='utf-8')
    if name.endswith('.json'):
        return {case: value if isinstance(value, dict) else {'input': value}
                for case, value in json.loads(source).items()}
    parts = re.split(r'^## ([CN]\d{2}) — ([^\n]+)\n', source, flags=re.M)
    cases = {}
    for index in range(1, len(parts), 3):
        case, title, body = parts[index:index + 3]
        body = re.split(r'^## ', body, maxsplit=1, flags=re.M)[0].strip()
        # Expectations are evidence metadata, never instructions fed to the client.
        stimulus, _, expected = body.partition('Attendu :')
        cases[case] = {'input': stimulus.strip(), 'title': title,
                       'expected': expected.strip()}
    if story == 'CONSO-001':
        common = ('Situation fictive. Je ne suis pas juriste. Aide-moi à comprendre '
                  'ma commande et prépare une réclamation que je pourrai relire. '
                  "Ne l'envoie pas.\n\n")
        base = cases['N01']['input']
        for case, value in cases.items():
            inherited = base
            if case == 'N05':
                inherited = inherited.replace('à domicile', 'au point relais R1')
            elif case == 'N07':
                inherited = inherited.replace('par un transporteur proposé au panier',
                                              'par Transport Cèdre, mandaté séparément hors panier')
            elif case == 'N09':
                inherited = inherited.replace('établi à Lyon,\nFrance', 'établi en Belgique')
            elif case == 'N13':
                inherited = inherited.split('P3/P4,')[0]
            if case == 'N11':
                value['input'] = ('P2 : extrait bancaire masqué, carte débitée de 129 € le '
                                  '10 septembre 2026. Achat privé : casque jamais reçu. '
                                  'Déclaration : « cela fait longtemps, j’ai déjà relancé ». '
                                  'Confirmation de commande et courriels absents ; vendeur, '
                                  'date promise et contenu/réception des relances inconnus.')
            elif case in ('N04', 'N05', 'N07', 'N09', 'N10', 'N12', 'N13'):
                # Variants replace base facts; they are not contradictory later documents.
                value['input'] = inherited + '\n\n' + re.sub(
                    r'^Reprendre N01\s*[,;]?\s*(?:avec\s*)?', '', value['input'])
            value['input'] = common + value['input']
        for case, variants in {
            'N04': {'porte': 'Seule variante : déposé devant la porte, aucun voisin mentionné.',
                    'voisin': 'Seule variante : remis au voisin, pas de dépôt devant la porte.'},
            'N07': {'exterieur': 'Seule variante : mandat à Transport Cèdre, extérieur au panier.',
                    'panier': "Seule variante : aucun mandat extérieur ; l'acheteuse a choisi une option du panier."},
        }.items():
            original = cases.pop(case)
            for suffix, detail in variants.items():
                stimulus = original['input']
                if case == 'N04':
                    stimulus = stimulus.replace('« remis devant la porte » ou « remis au voisin »',
                                                '« remis devant la porte »' if suffix == 'porte' else '« remis au voisin »')
                    stimulus = stimulus.replace('Rejouer les deux variantes séparément.', '')
                elif suffix == 'panier':
                    stimulus = common + base + (
                        '\nP5 : capture de la commande montrant la sélection du transporteur '
                        'dans le panier du vendeur. P6 : prise en charge du 20 septembre 2026. '
                        'Aucun mandat de transport extérieur au panier. Colis jamais reçu.')
                cases[case + '-' + suffix] = dict(original, input=stimulus + '\n' + detail)
    else:
        original = cases.pop('C08')
        prefix = original['input'].split('Variante A :')[0]
        for suffix, detail in {
            'A': 'Aucun document, titre ou date fourni.',
            'B': 'P01 : acte fictif intitulé « saisie », décision mentionnée mais non jointe, '
                 'signification déclarée le 15/10/2026 ; copie/preuve complète absente.',
        }.items():
            cases['C08-' + suffix] = dict(original, input=prefix + '\n' + detail)
        for value in cases.values():
            value['input'] = 'Situation fictive, sans profil préalable.\n\n' + value['input']
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude', required=True, type=Path)
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--label', required=True)
    parser.add_argument('--story', action='append', choices=STORIES)
    parser.add_argument('--case', action='append')
    parser.add_argument('--jobs', type=int, default=3, choices=range(1, 5))
    parser.add_argument('--web', action='store_true', help='allow official-source research')
    parser.add_argument('--resume-from', action='append', default=[], metavar='LABEL',
                        help='skip completed cases only when their package and input are identical')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9-]*', args.label):
        parser.error('label must be an alphanumeric directory name with optional hyphens')
    workspace = args.workspace.resolve()
    if workspace == ROOT or workspace.is_relative_to(ROOT) or workspace.exists():
        parser.error('use a fresh workspace outside the checkout')
    cli = args.claude.resolve(strict=True)
    stories = args.story or list(STORIES)
    for story in stories:
        if (STORIES[story][2] / args.label).exists():
            parser.error('run already exists: ' + story)
    selected = {s: {c: f for c, f in fixtures(s).items() if not args.case or c in args.case}
                for s in stories}
    if args.case and set(args.case) - {c for cases in selected.values() for c in cases}:
        parser.error('unknown or unselected case')
    for story in stories:
        current_inventory = inventory(ROOT / STORIES[story][0])
        for label in args.resume_from:
            if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9-]*', label):
                parser.error('invalid resume label')
            previous = STORIES[story][2] / label
            if not (previous / 'results.json').is_file() or not (previous / 'package.json').is_file():
                continue
            metadata = json.loads((previous / 'package.json').read_text(encoding='utf-8'))
            if metadata['package_inventory'] != current_inventory or metadata['web'] != args.web:
                continue
            rows = json.loads((previous / 'results.json').read_text(encoding='utf-8'))
            for row in rows:
                case = row['case']
                if (row['execution_status'] == 'completed' and case in selected[story] and
                        metadata['fixtures'].get(case) == selected[story][case]):
                    del selected[story][case]
    if not any(selected.values()):
        print('All selected cases already completed with identical packages and inputs.')
        return 0
    workspace.mkdir(parents=True)
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(('CLAUDE', 'ANTHROPIC', 'MCP_'))}
    env['PYTHONUTF8'] = '1'
    version = subprocess.check_output([str(cli), '--version'], text=True).strip()
    quota_rejected = Event()
    started = datetime.now(timezone.utc).isoformat()

    def redact(value):
        for original, replacement in [(str(workspace), '<workspace>'), (str(ROOT), '<checkout>'),
                                      (str(Path.home()), '<home>')]:
            for spelling in (original.replace('\\', '\\\\'), original, original.replace('\\', '/')):
                value = value.replace(spelling, replacement)
        return value

    packages = {}
    for story in stories:
        plugin, skill, annex, _ = STORIES[story]
        folder = workspace / story
        package = folder / plugin
        shutil.copytree(ROOT / plugin, package)
        project = folder / 'project'
        project.mkdir()
        output = annex / args.label
        output.mkdir()
        before = inventory(package)
        manifest = json.loads((package / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        metadata = {'story': story, 'started_utc': started, 'client': version,
                    'revision': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                    'plugin': manifest['name'], 'version': manifest['version'],
                    'web': args.web, 'os_sandbox': False, 'package_inventory': before,
                    'fixtures': selected[story], 'verdict': 'output-review-required'}
        (output / 'package.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        packages[story] = package, project, output, before

    def run(item):
        story, case, fixture = item
        plugin, skill, _, _ = STORIES[story]
        package, project, output, _ = packages[story]
        if quota_rejected.is_set():
            record = {'case': case, 'execution_status': 'not-run-quota', 'verdict': 'not-evaluated'}
            return story, record
        tools = 'Read,Glob,Grep,Skill' + (',WebFetch,WebSearch' if args.web else '')
        forbidden = 'Write Edit NotebookEdit Bash Agent Task' + ('' if args.web else ' WebFetch WebSearch')
        command = [str(cli), '-p', '/judge-fr-eu-' + plugin + ':' + skill + ' ' + fixture['input'],
                   '--plugin-dir', str(package), '--setting-sources', 'project', '--strict-mcp-config',
                   '--tools', tools, '--allowedTools', tools.replace(',', ' '),
                   '--disallowedTools', forbidden, '--output-format', 'stream-json', '--verbose',
                   '--max-budget-usd', '2', '--no-session-persistence']
        try:
            result = subprocess.run(command, cwd=project, env=env, capture_output=True,
                                    encoding='utf-8', errors='replace', timeout=240)
            stdout, stderr, code = result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired as exc:
            def decoded(value):
                return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value or ''
            stdout, stderr, code = decoded(exc.stdout), decoded(exc.stderr) + '\nTIMEOUT 240s', None
        stdout, stderr = redact(stdout), redact(stderr)
        (output / (case + '.jsonl')).write_text(stdout, encoding='utf-8')
        (output / (case + '-errors.txt')).write_text(stderr, encoding='utf-8')
        events = []
        for line in stdout.splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        finals = [e for e in events if e.get('type') == 'result']
        final = finals[-1] if finals else {}
        rejected = any(e.get('type') == 'rate_limit_event' and
                       e.get('rate_limit_info', {}).get('status') == 'rejected' for e in events)
        if rejected:
            quota_rejected.set()
        text = final.get('result', '')
        # Keep raw output in JSONL; Markdown exports follow repository whitespace rules.
        markdown = '\n'.join(line.rstrip() for line in text.splitlines()) + '\n'
        (output / (case + '.md')).write_text(markdown, encoding='utf-8')
        calls = [b for e in events if e.get('type') == 'assistant'
                 for b in e.get('message', {}).get('content', []) if b.get('type') == 'tool_use']
        init = next((e for e in events if e.get('subtype') == 'init'), {})
        status = ('blocked-quota' if rejected else 'completed' if code == 0 and
                  final.get('subtype') == 'success' and text and not final.get('is_error') else 'failed-or-incomplete')
        record = {'case': case, 'execution_status': status, 'returncode': code,
                  'subtype': final.get('subtype'), 'is_error': final.get('is_error'),
                  'errors': final.get('errors', []), 'cost_usd': final.get('total_cost_usd'),
                  'permission_denials': final.get('permission_denials', []),
                  'plugins': init.get('plugins', []),
                  'calls': [{'name': b.get('name'), 'input': b.get('input')} for b in calls],
                  'verdict': 'output-review-required' if status == 'completed' else 'not-evaluated'}
        print(json.dumps({'story': story, 'case': case, 'execution_status': status,
                          'cost_usd': record['cost_usd']}), flush=True)
        return story, record

    items = [(s, c, f) for s, cases in selected.items() for c, f in cases.items()]
    results = {s: [] for s in stories}
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        for story, record in executor.map(run, items):
            results[story].append(record)
            (packages[story][2] / 'results.json').write_text(
                json.dumps(results[story], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for story, (package, _, output, before) in packages.items():
        unchanged = before == inventory(package)
        (output / 'integrity.json').write_text(json.dumps({'package_unchanged': unchanged}) + '\n', encoding='utf-8')
        if not unchanged:
            raise RuntimeError('package changed during execution: ' + story)
    return 0 if all(r['execution_status'] == 'completed' for rows in results.values() for r in rows) else 1


if __name__ == '__main__':
    sys.exit(main())
