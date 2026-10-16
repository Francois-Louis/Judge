"""Contrôles documentaires EXIST-009 ; aucune exécution ou validation juridique.

Usage : python -X utf8 backlog/02-plugins-existants/exist-009-controles.py
Options : --baseline <json début de tâche> --output <rapport.json>
L'instantané contient {"files": {chemin relatif: sha256}, "git_head": ...}.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / 'exist-009-resultats.json'
PACKAGE = ROOT / 'legal-clinic'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    return {p.relative_to(ROOT).as_posix(): digest(p)
            for p in ROOT.rglob('*') if p.is_file()
            and '.git' not in p.relative_to(ROOT).parts
            and '__pycache__' not in p.parts and p != REPORT}


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
                problems.append(f'Duplicate: {ident}')
            for key in ('titre', 'statut', 'priorite', 'nature', 'dependances'):
                if key not in fm:
                    problems.append(f'{ident}: missing {key}')
            if not isinstance(fm.get('dependances'), list):
                problems.append(f'{ident}: dependencies must be a list')
                fm['dependances'] = []
            stories[ident] = (p, fm)
        except (KeyError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'{p.name}: {exc}')
    active, done = set(), set()

    def visit(ident):
        if ident not in stories:
            problems.append(f'Missing dependency: {ident}')
            return
        if ident in active:
            problems.append(f'Cycle: {ident}')
            return
        if ident in done:
            return
        active.add(ident)
        for dep in stories[ident][1]['dependances']:
            visit(dep)
        active.remove(ident)
        done.add(ident)

    for ident in stories:
        visit(ident)
    record('frontmatter_and_dependencies', problems, stories=len(stories))

    proposals = sorted((HERE / 'suites').glob('cln-*.md'))
    lot = [HERE / f'exist-009-{suffix}.md' for suffix in (
        'clinique-juridique', 'inventaire-clinique', 'decoupage-clinique', 'verification')]
    lot += proposals + [ROOT / 'backlog/README.md']
    allowed = {p.relative_to(ROOT).as_posix() for p in lot + [Path(__file__), REPORT]}
    problems, future = [], {}
    if {k for k in stories if k.startswith('CLN-')} != {f'CLN-{i:03}' for i in range(1, 24)} or len(proposals) != 23:
        problems.append('Expected exactly 23 proposals CLN-001..023')
    required = ('Objectif et résultat attendu', 'Périmètre et fichiers',
                'Entrées nécessaires', 'Travail attendu',
                "Sources à rechercher lors de l'implémentation",
                "Critères d'acceptation", 'Vérification', 'Hors périmètre')
    for p in proposals:
        txt = p.read_text(encoding='utf-8')
        fm = yaml.safe_load(txt.split('---', 2)[1])
        ident = fm['id']
        if fm['statut'] != 'proposee' or fm['nature'] != 'implementation':
            problems.append(f'{ident}: expected implementation/proposee')
        if not {'EXIST-009', 'PILOTE-003', 'BASE-005', 'BASE-006'} <= set(fm['dependances']):
            problems.append(f'{ident}: missing prerequisite')
        for title in required:
            if f'## {title}\n' not in txt:
                problems.append(f'{ident}: missing {title}')
        if '- Cas normal :' not in txt or '- Cas limite :' not in txt:
            problems.append(f'{ident}: missing scenarios')
        targets = re.findall(r'^- `((?:legal-clinic|managed-agent-cookbooks)/[^`]+)`([^\n]*)', txt, re.M)
        if not targets:
            problems.append(f'{ident}: no targets')
        for target, suffix in targets:
            if not (ROOT / target).is_file() and 'à créer' not in suffix:
                problems.append(f'{ident}: missing unmarked target {target}')
            if 'à créer' in suffix:
                future.setdefault(target, []).append(ident)
                if (ROOT / target).exists():
                    problems.append(f'{ident}: future target already exists {target}')
    problems += [f'{p}: multiple owners {owners}' for p, owners in future.items() if len(owners) != 1]
    record('bounded_proposals', problems, count=len(proposals), future_owners=future)

    inventory = (HERE / 'exist-009-inventaire-clinique.md').read_text(encoding='utf-8')
    skill_part, other_part = inventory.split('## Les vingt autres fichiers du plugin', 1)
    other_part = other_part.split('## Chargement des bandes et dépendances de contenu', 1)[0]
    listed = {'skills/' + name for name in re.findall(r'^\| `([^`]+)` \|', skill_part, re.M)}
    listed.update(re.findall(r'^\| `([^`]+)` \|', other_part, re.M))
    files = sorted(p for p in PACKAGE.rglob('*') if p.is_file())
    actual = {p.relative_to(PACKAGE).as_posix() for p in files}
    problems = []
    if listed != actual:
        problems.append({'missing': sorted(actual-listed), 'extra': sorted(listed-actual)})
    skills = list(PACKAGE.glob('skills/*/SKILL.md'))
    agents = list(PACKAGE.glob('agents/*.md'))
    if (len(files), len(skills), len(agents)) != (36, 16, 0):
        problems.append('Expected 36 package files, 16 skills, no agent')
    recipe_refs = [p.relative_to(ROOT).as_posix() for p in (ROOT/'managed-agent-cookbooks').rglob('*')
                   if p.is_file() and 'legal-clinic' in p.read_text(encoding='utf-8')]
    if recipe_refs:
        problems.append('New cookbook references: review inventory and scope')
    record('inventory_exact_coverage', problems, package_files=len(files), skills=len(skills), agents=len(agents), cookbook_references=recipe_refs)
    targeted = set()
    for proposal in proposals:
        targeted.update(re.findall(r'`(legal-clinic/skills/[^`]+/SKILL.md)`', proposal.read_text(encoding='utf-8')))
    record('all_skills_have_future_targets', sorted(p.relative_to(ROOT).as_posix() for p in skills if p.relative_to(ROOT).as_posix() not in targeted))

    shared = {
        'references/shared/research-citation-method.md': 'references/research-citation-method.md',
        'references/isolation.md': 'references/isolation.md',
        'references/company-profile-template.md': 'references/company-profile-template.md',
        'references/dashboard-template.md': 'references/dashboard-template.md',
        'scripts/judge_store.py': 'scripts/judge_store.py',
    }
    same = {dst: (PACKAGE/dst).read_bytes() == (ROOT/src).read_bytes() for dst, src in shared.items()}
    record('shared_copies', [p for p, ok in same.items() if not ok], identical=same, method_version='1.0.0')

    index = (ROOT / 'backlog/README.md').read_text(encoding='utf-8')
    dec = (HERE / 'exist-009-decoupage-clinique.md').read_text(encoding='utf-8')
    problems = [p.name for p in proposals if f'(suites/{p.name})' not in dec]
    for suffix in ('inventaire-clinique', 'decoupage-clinique', 'verification'):
        if f'(02-plugins-existants/exist-009-{suffix}.md)' not in index:
            problems.append(f'Missing index: {suffix}')
    for ident in ('EXIST-009', 'BASE-003', 'BASE-005', 'PILOTE-003'):
        if stories[ident][1]['statut'] != 'terminee':
            problems.append(f'{ident}: prerequisite/status not complete')
    record('index_and_prerequisites', problems)

    problems, links = [], 0
    for p in lot:
        raw = p.read_bytes()
        txt = raw.decode('utf-8')
        if not raw.endswith(b'\n') or raw.startswith(b'\xef\xbb\xbf') or '\ufffd' in txt:
            problems.append(f'{p.name}: encoding/newline')
        if any(line != line.rstrip() for line in txt.splitlines()):
            problems.append(f'{p.name}: trailing whitespace')
        for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', txt):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            links += 1
            destination = unquote(target.split('#', 1)[0])
            if (p.parent / destination).resolve() == REPORT.resolve() and not REPORT.exists():
                continue  # Rapport créé à la fin de cette première exécution.
            if not (p.parent / destination).exists():
                problems.append(f'{p.name}: broken link {target}')
    record('links_and_format', problems, markdown_files=len(lot), local_links=links)

    # Repérages hérités : preuve de lecture locale, pas conformité ou recette runtime.
    markers = {}
    for label, pattern in [
        ('bands_and_federal', r'plausibility|federal.always|always.loaded|CA\.md|IL\.md'),
        ('ABA', r'ABA|Model Rules'),
        ('pedagogy_keys', r'pedagogy_default|pedagogy_posture'),
        ('queue_path', r'references/review-queue\.yaml'),
    ]:
        hits = []
        for path in files:
            if path.suffix != '.md':
                continue
            positions = [i for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1) if re.search(pattern, line, re.I)]
            if positions:
                hits.append({'path': path.relative_to(ROOT).as_posix(), 'lines': positions})
        markers[label] = hits
    record('legacy_loading_and_roles_located', [k for k, hits in markers.items() if not hits], locations=markers)

    ledger = yaml.safe_load((PACKAGE/'deadlines.yaml').read_text(encoding='utf-8'))
    extra_keys = sorted(set(ledger)-{'deadlines'})
    model_queue = yaml.safe_load((PACKAGE/'skills/supervisor-review-queue/references/review-queue.yaml').read_text(encoding='utf-8'))
    templates = PACKAGE/'skills/client-intake/references/intake-templates'
    missing = [name for name in ('immigration.md','housing.md','family.md','consumer.md') if not (templates/name).exists()]
    all_fm = {p.parent.name: yaml.safe_load(p.read_text(encoding='utf-8').split('---', 2)[1]) for p in skills}
    aliases = sorted(name for name, fm in all_fm.items() if fm.get('user-invocable') is False)
    problems = []
    if not any(k.startswith('<!--') for k in extra_keys):
        problems.append('Update inventory: inherited HTML key not observed')
    if model_queue != {'queue': [], 'approved': [], 'log': []}:
        problems.append('Review queue model differs from documented empty model')
    if len(missing) != 4:
        problems.append('Update inventory: announced templates now present')
    if aliases != ['form-generation','plain-language-letters']:
        problems.append('Invocable/alias count differs')
    record('known_models_and_missing_templates', problems, deadline_extra_keys=extra_keys,
           missing_announced_templates=missing, deprecated_aliases=aliases,
           invocable_skills=len(skills)-len(aliases), queue_model_empty=True,
           corrections_assigned_to=['CLN-012','CLN-015','CLN-021'])

    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding='utf-8'))['files']
        before = {k: v for k, v in baseline.items() if k != REPORT.relative_to(ROOT).as_posix()}
        now = snapshot()
        changed = sorted(k for k in before.keys() | now.keys() if before.get(k) != now.get(k))
        outside = [p for p in changed if p not in allowed]
        checks['scope_vs_task_baseline'] = {
            'status': 'observed-concurrent-changes' if outside else 'passed',
            'lot_changed_files': [p for p in changed if p in allowed],
            'other_changed_files': outside,
            'note': 'Other differences observed during this task are not attributed to EXIST-009; no claim of an unchanged entire workspace.',
            'preserved_files': sum(now.get(k) == v for k, v in before.items() if k not in allowed),
        }
        protected = {k: v for k, v in before.items()
                     if not k.startswith('backlog/') or
                     re.match(r'backlog/02-plugins-existants/(?:exist-00[1-8]-|suites/)', k)}
        record('protected_inputs_unchanged', [k for k, v in protected.items() if now.get(k) != v],
               files_checked=len(protected),
               package_preserved=all(now.get(p.relative_to(ROOT).as_posix()) == before.get(p.relative_to(ROOT).as_posix()) for p in files))
    else:
        checks['scope_vs_task_baseline'] = {'status': 'not-run', 'reason': 'Provide --baseline; existing git changes are not attributed to this task.'}

    json_files = [p for p in ROOT.rglob('*.json') if '.git' not in p.relative_to(ROOT).parts]
    problems = []
    for p in json_files:
        try:
            json.loads(p.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError) as exc:
            problems.append(f'{p.relative_to(ROOT)}: {exc}')
    record('repository_json_sanity', problems, files=len(json_files))
    for name, command in (
        ('cookbook_tool_scope_lint', [sys.executable, '-X', 'utf8', 'scripts/lint-tool-scope.py']),
        ('git_diff_check', ['git', 'diff', '--check']),
    ):
        run = subprocess.run(command, cwd=ROOT, capture_output=True, encoding='utf-8')
        record(name, [] if run.returncode == 0 else [run.stdout or run.stderr],
               exit_code=run.returncode, output=run.stdout.splitlines())

    report = {
        'story': 'EXIST-009', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'cadrage et relecture documentaire fictive ; aucun skill exécuté ou droit validé',
        'checks': checks,
        'package_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in files},
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in lot + [Path(__file__)]},
        'not_run': ['recherche juridique externe', 'acte/délai réel', 'exécution de skill',
                    'installation/recette client', 'lecteur indépendant', 'connexion authentifiée/envoi/dépôt/paiement/publication/déploiement'],
        'command': 'python -X utf8 backlog/02-plugins-existants/exist-009-controles.py --baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-009-resultats.json',
        'notes': ['Les différences git préexistantes ne sont pas des changements EXIST-009 ; voir comparaison à l’instantané de début de tâche.',
                  'Aucune validation de schéma plugin/client : aucun fichier de paquet modifié.',
                  'Bandes, règles ABA, contrats pédagogiques et modèles repérés localement ; aucune source externe consultée ni raisonnement juridique validé.'],
    }
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    for name, result in checks.items():
        print(f"{name}: {result['status']}")
        for problem in result.get('problems', []):
            print(f'  {problem}')
    return int(any(c['status'] == 'failed' for c in checks.values()))


if __name__ == '__main__':
    raise SystemExit(main())
