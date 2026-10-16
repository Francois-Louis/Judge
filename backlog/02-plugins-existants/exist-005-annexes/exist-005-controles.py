"""Contrôles documentaires EXIST-005, sans exécution d'un skill.

python backlog/02-plugins-existants/exist-005-annexes/exist-005-controles.py
Ajouter --baseline <instantane.json> pour contrôler les travaux préexistants.
Ajouter --output <rapport.json> pour conserver un relevé, jamais une preuve de droit.
L'instantané facultatif est un objet {"files": {chemin: sha256}, "git_head": ...}.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[3]
ANNEXES = Path(__file__).resolve().parent
HERE = ANNEXES.parent
REPORT = ANNEXES / 'exist-005-resultats.json'
ALLOWED = {
    'backlog/README.md',
    'backlog/02-plugins-existants/exist-005-gouvernance-ia.md',
    *('backlog/02-plugins-existants/exist-005-annexes/' + name for name in (
        'exist-005-inventaire-ia.md',
        'exist-005-decoupage-ia.md', 'exist-005-verification.md',
        'exist-005-controles.py', 'exist-005-resultats.json',
    )),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    return {
        p.relative_to(ROOT).as_posix(): digest(p)
        for p in ROOT.rglob('*') if p.is_file()
        and '.git' not in p.relative_to(ROOT).parts
        and '__pycache__' not in p.parts
        and p != REPORT
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = {}

    def record(name, problems, **facts):
        checks[name] = {'status': 'failed' if problems else 'passed',
                        **facts, 'problems': problems}

    stories, problems = {}, []
    for p in sorted((ROOT / 'backlog').rglob('*.md')):
        txt = p.read_text(encoding='utf-8')
        if not txt.startswith('---\n'):
            continue
        try:
            fm = yaml.safe_load(txt.split('---', 2)[1])
            ident = fm['id']
            if ident in stories:
                problems.append(f'duplicate: {ident}')
            for key in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
                if key not in fm:
                    problems.append(f'{ident}: missing {key}')
            if not isinstance(fm.get('dependances'), list):
                problems.append(f'{ident}: dependencies must be a list')
                fm['dependances'] = []
            stories[ident] = (p, fm)
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{p.relative_to(ROOT)}: {exc}')
    for ident, (_, fm) in stories.items():
        for dep in fm['dependances']:
            if dep not in stories:
                problems.append(f'{ident}: missing dependency {dep}')
    active, done = set(), set()

    def visit(ident):
        if ident in active:
            problems.append(f'dependency cycle at {ident}')
            return
        if ident in done or ident not in stories:
            return
        active.add(ident)
        for dep in stories[ident][1]['dependances']:
            visit(dep)
        active.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    record('backlog_frontmatter_and_dependencies', problems,
           total=len(stories), statuses=dict(Counter(x[1]['statut'] for x in stories.values())))

    proposals = sorted((HERE / 'suites').glob('ia-*.md'))
    lot = [HERE / 'exist-005-gouvernance-ia.md'] + [ANNEXES / ('exist-005-' + n + '.md') for n in (
        'inventaire-ia', 'decoupage-ia', 'verification')]
    lot += proposals + [ROOT / 'backlog/README.md']
    for p in proposals:
        ALLOWED.add(p.relative_to(ROOT).as_posix())
    expected = {f'IA-{i:03}' for i in range(1, 21)}
    actual = {k for k in stories if k.startswith('IA-')}
    problems = []
    if actual != expected or len(proposals) != 20:
        problems.append('Expected exactly IA-001..IA-020 and 20 files')
    targets, future_owners = set(), {}
    required = ('Objectif et résultat attendu', 'Périmètre et fichiers',
                'Entrées nécessaires', 'Travail attendu',
                "Sources à rechercher lors de l'implémentation",
                "Critères d'acceptation", 'Vérification', 'Hors périmètre')
    for p in proposals:
        txt = p.read_text(encoding='utf-8')
        fm = yaml.safe_load(txt.split('---', 2)[1])
        ident = fm['id']
        if fm.get('statut') != 'proposee' or fm.get('nature') != 'implementation':
            problems.append(f'{ident}: expected implementation/proposee')
        if not {'EXIST-005', 'PILOTE-003', 'BASE-005', 'BASE-006'} <= set(fm['dependances']):
            problems.append(f'{ident}: missing common dependency')
        for heading in required:
            if f'## {heading}\n' not in txt:
                problems.append(f'{ident}: missing section {heading}')
        if '- Cas normal :' not in txt or '- Cas limite :' not in txt:
            problems.append(f'{ident}: missing scenarios')
        rows = re.findall(r'^- `(ai-governance-legal/[^`]+)`([^\n]*)', txt, re.M)
        if not rows:
            problems.append(f'{ident}: no file targets')
        for name, suffix in rows:
            targets.add(name)
            exists = (ROOT / name).is_file()
            if not exists and 'à créer' not in suffix:
                problems.append(f'{ident}: unmarked missing file {name}')
            if 'à créer' in suffix:
                future_owners.setdefault(name, []).append(ident)
                if exists:
                    problems.append(f'{ident}: future file already exists {name}')
    for name, owners in future_owners.items():
        if len(owners) != 1:
            problems.append(f'{name}: multiple owners {owners}')
    record('bounded_proposals', problems, count=len(proposals), file_targets=len(targets),
           future_files=[{'path': p, 'owner': owners[0]} for p, owners in future_owners.items()])

    package = ROOT / 'ai-governance-legal'
    files = sorted(p for p in package.rglob('*') if p.is_file())
    skills = sorted(package.glob('skills/*/SKILL.md'))
    inv = (ANNEXES / 'exist-005-inventaire-ia.md').read_text(encoding='utf-8')
    skill_text, other_text = inv.split('## Les treize autres fichiers', 1)
    listed = {'skills/' + x for x in re.findall(r'^\| `([^`]+/SKILL.md)` \|', skill_text, re.M)}
    listed.update(re.findall(r'^\| `([^`]+)` \|', other_text.split('## Dépendances de contenu', 1)[0], re.M))
    names = {p.relative_to(package).as_posix() for p in files}
    problems = []
    if listed != names:
        problems.append({'missing': sorted(names-listed), 'extra': sorted(listed-names)})
    if len(files) != 23 or len(skills) != 10:
        problems.append('Expected 23 package files and 10 skills')
    record('inventory_exact_coverage', problems, package_files=len(files), skills=len(skills),
           agents=len(list(package.glob('agents/*.md'))),
           hooks=len(list(package.glob('hooks/*'))))

    shared = {
        'references/shared/research-citation-method.md': 'references/research-citation-method.md',
        'references/isolation.md': 'references/isolation.md',
        'references/company-profile-template.md': 'references/company-profile-template.md',
        'references/dashboard-template.md': 'references/dashboard-template.md',
        'scripts/judge_store.py': 'scripts/judge_store.py',
    }
    identical = {dst: (package/dst).read_bytes() == (ROOT/src).read_bytes()
                 for dst, src in shared.items()}
    record('shared_copies', [p for p, ok in identical.items() if not ok],
           method_version='1.0.0', identical=identical)

    problems, count = [], 0
    for p in lot:
        raw = p.read_bytes()
        txt = raw.decode('utf-8')
        if not raw.endswith(b'\n') or raw.startswith(b'\xef\xbb\xbf'):
            problems.append(f'{p.name}: missing final newline or UTF-8 BOM')
        if any(line.rstrip() != line for line in txt.splitlines()):
            problems.append(f'{p.name}: trailing whitespace')
        if '\ufffd' in txt:
            problems.append(f'{p.name}: replacement character')
        for label, target in re.findall(r'\[([^\]\n]+)\]\(([^)]+)\)', txt):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            count += 1
            dest = unquote(target.split('#', 1)[0])
            if not (p.parent / dest).exists():
                problems.append(f'{p.name}: broken link {label}: {target}')
    record('links_and_format', problems, markdown_files=len(lot), local_links=count)

    index = (ROOT / 'backlog/ETAT.md').read_text(encoding='utf-8')
    dec = (ANNEXES / 'exist-005-decoupage-ia.md').read_text(encoding='utf-8')
    problems = []
    for p in proposals:
        if f'(../suites/{p.name})' not in dec:
            problems.append(f'Proposal missing from breakdown: {p.name}')
    for name in ('decoupage-ia', 'inventaire-ia', 'verification'):
        if f'(02-plugins-existants/exist-005-annexes/exist-005-{name}.md)' not in index:
            problems.append(f'Index missing {name}')
    if stories['EXIST-005'][1]['statut'] != 'terminee':
        problems.append('EXIST-005 not terminee')
    if stories['PILOTE-003'][1]['statut'] != 'terminee':
        problems.append('Pilot prerequisite not satisfied')
    record('index_and_prerequisites', problems, proposals_indexed=len(proposals))

    now = snapshot()
    changed = subprocess.check_output(
        ['git', 'diff', '--name-only', '-z', 'HEAD', '--', '.', ':!backlog'], cwd=ROOT
    ).decode().split('\0')
    record('tracked_outside_backlog_vs_head', [name for name in changed if name])

    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding='utf-8'))
        before = {k: v for k, v in baseline['files'].items() if k != REPORT.relative_to(ROOT).as_posix()}
        changes = sorted(k for k in before.keys() | now.keys() if before.get(k) != now.get(k))
        violations = [k for k in changes if k not in ALLOWED]
        preserved = [k for k in before if k not in ALLOWED and now.get(k) == before[k]]
        record('scope_vs_task_baseline', violations, changed_files=changes,
               preserved_files=len(preserved), report_excluded_from_own_comparison=True)
    else:
        checks['scope_vs_task_baseline'] = {
            'status': 'not-run', 'reason': 'Provide --baseline to compare pre-existing uncommitted work.'}

    json_paths = [p for p in ROOT.rglob('*.json') if '.git' not in p.relative_to(ROOT).parts]
    problems = []
    for p in json_paths:
        try:
            json.loads(p.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError) as exc:
            problems.append(f'{p.relative_to(ROOT)}: {exc}')
    record('repository_json_sanity', problems, files=len(json_paths))
    lint = subprocess.run([sys.executable, '-X', 'utf8', 'scripts/lint-tool-scope.py'],
                          cwd=ROOT, capture_output=True, encoding='utf-8')
    record('cookbook_tool_scope_lint', [] if lint.returncode == 0 else [lint.stderr or lint.stdout],
           exit_code=lint.returncode, output=lint.stdout.splitlines())
    whitespace = subprocess.run(['git', 'diff', '--check'], cwd=ROOT,
                                capture_output=True, encoding='utf-8')
    record('git_diff_check', [] if whitespace.returncode == 0 else [whitespace.stdout or whitespace.stderr],
           exit_code=whitespace.returncode)

    report = {
        'story': 'EXIST-005', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'cadrage documentaire ; aucune adaptation de plugin ni validation juridique',
        'checks': checks,
        'package_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in files},
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in lot + [Path(__file__)]},
        'not_run': ['recherche juridique externe', 'classification définitive',
                    'calcul de délai réel', 'exécution de skill', 'installation/recette client',
                    'lecteur indépendant', 'connexion/envoi/publication/déploiement'],
        'commands': [
            'python backlog/02-plugins-existants/exist-005-annexes/exist-005-controles.py --baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-005-annexes/exist-005-resultats.json',
            'python -X utf8 scripts/lint-tool-scope.py (appelé par le contrôleur)',
            'git diff --check (appelé par le contrôleur)',
        ],
        'execution_notes': [
            "Premier lint sans mode UTF-8 : erreur d'affichage cp1252 du caractère coche, corrigée par python -X utf8 sans modification du script existant.",
            "Premier contrôle des liens avant création du rapport JSON : liens vers le rapport absents ; contrôle final exécuté avec le rapport présent.",
            'Validation des schémas plugin/client non exécutée : aucun fichier de paquet modifié dans ce lot de cadrage.',
        ],
    }
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    for key, val in checks.items():
        print(f"{key}: {val['status']}")
        for problem in val.get('problems', []):
            print(f'  {problem}')
    raise SystemExit(1 if any(x['status'] == 'failed' for x in checks.values()) else 0)


if __name__ == '__main__':
    main()
