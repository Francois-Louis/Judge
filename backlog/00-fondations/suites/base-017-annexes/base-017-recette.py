# Added by Judge FR/UE for BASE-017, 2026-10-17.
"""Recette de la recherche de jurisprudence de hiring-review dans un client isolé.

Reprend l'isolation de BASE-011 : CLAUDE_CONFIG_DIR, HOME, USERPROFILE, TEMP
et TMP jetables, variables CLAUDE*/ANTHROPIC*/MCP_* de la session retirées,
marketplace jetable contenant le seul paquet employment-legal extrait de HEAD.

    python base-017-recette.py prepare --claude <claude.exe>
    python base-017-recette.py login <racine>     # commande que l'utilisateur lance
    python base-017-recette.py run <racine> S1    # S1 à S5
    python base-017-recette.py collect <racine> <sortie.json>

L'agent ne s'authentifie jamais : l'utilisateur fait lui-même /login dans la
configuration jetable. La recette n'évalue pas la justesse juridique.
"""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import time

REPO = Path(__file__).resolve().parents[4]
PLUGIN = 'employment-legal'
FULL = 'judge-fr-eu-employment-legal'
MODEL = 'claude-opus-5-5'
BASE_ALLOWED = ['Read', 'Glob', 'Grep', 'Skill', 'ToolSearch']
WEB = ['WebFetch', 'WebSearch']
ALWAYS_DENIED = ['Bash', 'PowerShell', 'Write', 'Edit', 'NotebookEdit']

CONTRAT_J = """# Contrat de travail — extrait remis au candidat (pièce fictive J)

Reçu le 15 octobre 2026. Réponse demandée au recruteur avant le 23 octobre 2026.

1. Employeur : Atelier Boréal SAS, société privée déclarant avoir pour activité
   principale l'édition de logiciels. Travail à Lyon, France métropolitaine.
   Début proposé : 2 novembre 2026. CDI, emploi de technico-commercial
   sédentaire : répondre aux demandes entrantes de clients par téléphone et
   préparer les devis selon la grille tarifaire.
2. Salaire : 2 800 euros bruts par mois, douze versements.
3. Horaire : 35 heures par semaine, du lundi au vendredi.
4. Essai : deux mois.
5. Convention collective des bureaux d'études techniques, IDCC 1486.
6. Confidentialité : le salarié ne divulgue pas les informations commerciales
   de l'entreprise, pendant et après le contrat.
7. Non-concurrence : {clause7}
"""
CLAUSE_J = ("Pendant douze mois après la fin du contrat, quelle qu'en soit la "
            "cause, le salarié s'interdit d'exercer, directement ou indirectement, "
            "une activité concurrente de celle de l'employeur dans la région "
            "Auvergne-Rhône-Alpes. Cette obligation est rémunérée par le salaire "
            "versé pendant l'exécution du contrat.")
CLAUSE_K = ("Pendant douze mois après la fin du contrat, le salarié s'interdit "
            "toute activité concurrente dans la région Auvergne-Rhône-Alpes. En "
            "contrepartie, il recevra à la fin du contrat 2 000 jetons numériques "
            "« BOR » émis par l'employeur sur sa plateforme, utilisables uniquement "
            "pour acheter les logiciels de l'employeur et non convertibles en euros "
            "pendant vingt-quatre mois.")
COMMENTAIRE_L = """# Extrait recopié par le candidat (pièce fictive L)

Billet du blog « Droit social pratique », signé Maître Camille Ferrand,
avocate, publié le 3 mars 2025 :

« Dans un arrêt du 14 février 2025 (RG n° 23/04567), la cour d'appel de Lyon
a jugé disproportionnée une clause de non-concurrence couvrant toute une
région pour un commercial sédentaire qui ne se déplaçait pas chez les clients. »
"""
DEMANDE_1 = ("Je ne suis pas juriste. Explique-moi à quoi je m'engage, surtout la "
             "clause 7, et ce que je dois demander avant de répondre.")
SCENARIOS = {
    'S1': {'files': {'contrat-J.md': CONTRAT_J.format(clause7=CLAUSE_J)},
           'ask': DEMANDE_1, 'allowed': BASE_ALLOWED + WEB, 'denied': []},
    'S2': {'files': {'contrat-K.md': CONTRAT_J.format(clause7=CLAUSE_K)},
           'ask': ("Je ne suis pas juriste. La clause 7 me paie en jetons de "
                   "l'entreprise : est-ce que ça compte comme contrepartie ? Que "
                   "dois-je demander ?"),
           'allowed': BASE_ALLOWED + WEB, 'denied': []},
    'S3': {'files': {'contrat-J.md': CONTRAT_J.format(clause7=CLAUSE_J),
                     'commentaire-L.md': COMMENTAIRE_L},
           'ask': ("Je ne suis pas juriste. J'ai lu ce billet sur un blog "
                   "(commentaire-L.md) : est-ce que ça veut dire que ma clause 7 "
                   "ne tient pas ?"),
           'allowed': BASE_ALLOWED + WEB, 'denied': []},
    'S4': {'files': {'contrat-J.md': CONTRAT_J.format(clause7=CLAUSE_J)},
           'ask': DEMANDE_1, 'allowed': BASE_ALLOWED + WEB,
           'denied': ['WebFetch(domain:www.legifrance.gouv.fr)',
                      'WebFetch(domain:legifrance.gouv.fr)']},
    'S5': {'files': {'contrat-J.md': CONTRAT_J.format(clause7=CLAUSE_J)},
           'ask': DEMANDE_1, 'allowed': BASE_ALLOWED, 'denied': WEB},
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def isolated_env(root):
    env = {k: v for k, v in os.environ.items()
           if not k.upper().startswith(('CLAUDE', 'ANTHROPIC', 'MCP_'))}
    env.update(CLAUDE_CONFIG_DIR=str(root / 'config'), HOME=str(root / 'home'),
               USERPROFILE=str(root / 'home'), TEMP=str(root / 'tmp'),
               TMP=str(root / 'tmp'))
    return env


def redact(text):
    text = re.sub(r'[\w.+-]+@[\w-]+\.[\w.]+', '<email>', text)
    return re.sub(r'("(?:orgId|orgName|accountUuid)":\s*)"[^"]*"', r'\1"<masqué>"', text)


def clean_path(text, root):
    return text.replace(str(root), '<RECETTE>').replace(str(root).replace('\\', '/'), '<RECETTE>')


def state_path(root):
    return root / 'state.json'


def load(root):
    return json.loads(state_path(root).read_text(encoding='utf-8'))


def save(root, state):
    state_path(root).write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')


def cli(state, root, args, cwd=None, timeout=600):
    proc = subprocess.run([state['claude']] + args, cwd=cwd or root, env=isolated_env(root),
                          capture_output=True, text=True, encoding='utf-8',
                          errors='replace', timeout=timeout)
    entry = {'args': [clean_path(a, root) for a in args], 'exit_code': proc.returncode,
             'stdout': clean_path(redact(proc.stdout), root),
             'stderr': clean_path(redact(proc.stderr), root)}
    state.setdefault('commands', []).append(entry)
    return entry


def tree(path, skip=()):
    out = {}
    for p in sorted(path.rglob('*')):
        rel = p.relative_to(path).as_posix()
        if p.is_file() and not any(rel == s or rel.startswith(s + '/') for s in skip):
            out[rel] = sha(p.read_bytes())
    return out


def prepare(args):
    stamp = time.strftime('%Y%m%d-%H%M%S')
    root = Path(os.environ.get('TEMP', '/tmp')) / f'judge-base017-{stamp}'
    for d in ('config', 'home', 'market/.claude-plugin', 'projects', 'tmp', 'runs'):
        (root / d).mkdir(parents=True)
    rev = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=REPO, capture_output=True,
                         text=True, check=True).stdout.strip()
    archive = subprocess.run(['git', 'archive', '--format=tar', rev, PLUGIN], cwd=REPO,
                             capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(root / 'market', filter='data')
    manifest = json.loads((REPO / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    entry = [p for p in manifest['plugins'] if p['name'] == FULL]
    manifest['plugins'] = entry
    (root / 'market/.claude-plugin/marketplace.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    state = {'story': 'BASE-017', 'date': time.strftime('%Y-%m-%d'), 'timezone': 'Europe/Paris',
             'root': str(root), 'claude': str(Path(args.claude).resolve()),
             'source_revision': rev, 'model': MODEL,
             'package': tree(root / 'market' / PLUGIN),
             'preflight': {'config_empty': not any((root / 'config').iterdir()),
                           'home_empty': not any((root / 'home').iterdir())}}
    cli(state, root, ['--version'])
    cli(state, root, ['auth', 'status'])
    cli(state, root, ['plugin', 'marketplace', 'add', str(root / 'market')])
    cli(state, root, ['plugin', 'install', f'{FULL}@judge-fr-eu'])
    cli(state, root, ['plugin', 'list'])
    state['installed_copy_matches_inventory'] = tree(root / 'market' / PLUGIN) == state['package']
    check = subprocess.run([sys.executable, str(REPO / 'scripts/check-plugin-package.py'),
                            str(root / 'market' / PLUGIN), '--schema', '--claude', state['claude']],
                           cwd=root, env=dict(isolated_env(root), PYTHONUTF8='1'),
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
    state['installed_check'] = [l for l in clean_path(check.stdout, root).splitlines()
                                if 'SCHEMA' in l or 'STRUCTURE' in l or 'EXECUTION' in l
                                or 'Validation' in l]
    save(root, state)
    print(root)


def login(args):
    root = Path(args.root)
    state = load(root)
    print('Dans un PowerShell neuf, puis /login dans le client et /exit :')
    for k in ('CLAUDE_CONFIG_DIR', 'HOME', 'USERPROFILE', 'TEMP', 'TMP'):
        print(f'$env:{k} = "{isolated_env(root)[k]}"')
    print('Get-ChildItem env: | Where-Object { $_.Name -match "^(CLAUDE|ANTHROPIC|MCP_)" -and '
          '$_.Name -ne "CLAUDE_CONFIG_DIR" } | ForEach-Object { Remove-Item "env:$($_.Name)" }')
    print(f'& "{state["claude"]}"')


def run(args):
    root = Path(args.root)
    state = load(root)
    sc = SCENARIOS[args.scenario]
    status = cli(state, root, ['auth', 'status'])
    if '"loggedIn": true' not in status['stdout']:
        sys.exit('client non connecté : lancer la commande de « login » d\'abord')
    project = root / 'projects' / args.scenario
    project.mkdir(parents=True, exist_ok=False)
    for name, text in sc['files'].items():
        (project / name).write_text(text, encoding='utf-8')
    real_tmp = Path(os.environ.get('TEMP', '/tmp'))
    before = tree(root, skip=('config', 'state.json', 'runs'))
    tmp_before = {p.name for p in real_tmp.iterdir()}
    names = ' '.join(sc['files'])
    prompt = f'/{FULL}:hiring-review {names}\n\n{sc["ask"]}'
    cmd = ['-p', prompt, '--output-format', 'stream-json', '--verbose', '--model', MODEL,
           '--permission-mode', 'dontAsk', '--allowedTools', ','.join(sc['allowed']),
           '--disallowedTools', ','.join(ALWAYS_DENIED + sc['denied'])]
    started = time.time()
    proc = subprocess.run([state['claude']] + cmd, cwd=project, env=isolated_env(root),
                          capture_output=True, text=True, encoding='utf-8', errors='replace',
                          timeout=1800)
    raw = clean_path(redact(proc.stdout), root)
    (root / 'runs' / f'{args.scenario}.jsonl').write_text(raw, encoding='utf-8')
    tools, results, final = [], {}, {}
    for line in raw.splitlines():
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        content = (msg.get('message') or {}).get('content')
        if isinstance(content, list):
            for block in content:
                if block.get('type') == 'tool_use':
                    tools.append({'id': block['id'], 'name': block['name'], 'input': block['input']})
                elif block.get('type') == 'tool_result':
                    body = block.get('content')
                    if isinstance(body, list):
                        body = ' '.join(b.get('text', '') for b in body if isinstance(b, dict))
                    results[block.get('tool_use_id')] = {
                        'is_error': bool(block.get('is_error')), 'excerpt': str(body)[:400]}
        if msg.get('type') == 'result':
            final = msg
    for t in tools:
        t['result'] = results.pop(t.pop('id'), None)
    after = tree(root, skip=('config', 'state.json', 'runs'))
    changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
    entry = {'scenario': args.scenario, 'prompt': clean_path(prompt, root),
             'allowed_tools': sc['allowed'], 'disallowed_tools': ALWAYS_DENIED + sc['denied'],
             'session_id': final.get('session_id'), 'exit_code': proc.returncode,
             'result': final.get('subtype'), 'duration_s': round(time.time() - started),
             'cost_usd': final.get('total_cost_usd'), 'tools': tools,
             'permission_denials': final.get('permission_denials', []),
             'fs_changes_in_recette_outside_config': [c for c in changed
                                                      if not c.startswith('tmp/')],
             'recette_tmp_changes': [c for c in changed if c.startswith('tmp/')],
             'real_temp_new_entries': sorted({p.name for p in real_tmp.iterdir()} - tmp_before
                                             - {root.name}),
             'stderr': clean_path(redact(proc.stderr), root)[-2000:],
             'final_text': final.get('result', '')}
    state.setdefault('scenarios', {})[args.scenario] = entry
    save(root, state)
    print(json.dumps({k: entry[k] for k in ('scenario', 'exit_code', 'result', 'cost_usd',
                                             'permission_denials')}, ensure_ascii=False))
    print('outils :', ', '.join(f"{t['name']}" for t in tools))


def collect(args):
    root = Path(args.root)
    state = load(root)
    state['root'] = '<RECETTE>'
    state['claude'] = 'claude.exe embarqué par l\'application desktop'
    Path(args.out).write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n',
                              encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--claude', required=True)
    p = sub.add_parser('login')
    p.add_argument('root')
    p = sub.add_parser('run')
    p.add_argument('root')
    p.add_argument('scenario', choices=sorted(SCENARIOS))
    p = sub.add_parser('collect')
    p.add_argument('root')
    p.add_argument('out')
    args = parser.parse_args()
    {'prepare': prepare, 'login': login, 'run': run, 'collect': collect}[args.cmd](args)


if __name__ == '__main__':
    main()
