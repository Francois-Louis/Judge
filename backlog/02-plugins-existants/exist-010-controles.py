"""Contrôles documentaires EXIST-010 ; aucune exécution ou validation juridique.

Usage : python -X utf8 backlog/02-plugins-existants/exist-010-controles.py
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
import xml.etree.ElementTree as ET

import yaml


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REPORT = HERE / 'exist-010-resultats.json'
PACKAGE = ROOT / 'law-student'


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

    proposals = sorted((HERE / 'suites').glob('etu-*.md'))
    lot = [HERE / f'exist-010-{suffix}.md' for suffix in (
        'formation-juridique', 'inventaire-formation', 'decoupage-formation', 'verification')]
    lot += proposals + [ROOT / 'backlog/README.md']
    support_path = HERE / 'exist-010-support-verification.json'
    lot.append(support_path)
    allowed = {p.relative_to(ROOT).as_posix() for p in lot + [Path(__file__), REPORT]}
    problems, future = [], {}
    if {k for k in stories if k.startswith('ETU-')} != {f'ETU-{i:03}' for i in range(1, 22)} or len(proposals) != 21:
        problems.append('Expected exactly 21 proposals ETU-001..021')
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
        if not {'EXIST-010', 'PILOTE-003', 'BASE-005', 'BASE-006'} <= set(fm['dependances']):
            problems.append(f'{ident}: missing prerequisite')
        for title in required:
            if f'## {title}\n' not in txt:
                problems.append(f'{ident}: missing {title}')
        if '- Cas normal :' not in txt or '- Cas limite :' not in txt:
            problems.append(f'{ident}: missing scenarios')
        targets = re.findall(r'^- `((?:law-student|managed-agent-cookbooks)/[^`]+)`([^\n]*)', txt, re.M)
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

    inventory = (HERE / 'exist-010-inventaire-formation.md').read_text(encoding='utf-8')
    skill_part, other_part = inventory.split('## Les treize autres fichiers du plugin', 1)
    other_part = other_part.split('## Dépendances de contenu et frontières', 1)[0]
    listed = {'skills/' + name for name in re.findall(r'^\| `([^`]+)` \|', skill_part, re.M)}
    listed.update(re.findall(r'^\| `([^`]+)` \|', other_part, re.M))
    files = sorted(p for p in PACKAGE.rglob('*') if p.is_file())
    actual = {p.relative_to(PACKAGE).as_posix() for p in files}
    problems = []
    if listed != actual:
        problems.append({'missing': sorted(actual-listed), 'extra': sorted(listed-actual)})
    skills = list(PACKAGE.glob('skills/*/SKILL.md'))
    agents = list(PACKAGE.glob('agents/*.md'))
    if (len(files), len(skills), len(agents)) != (26, 13, 0):
        problems.append('Expected 26 package files, 13 skills, no agent')
    recipe_refs = [p.relative_to(ROOT).as_posix() for p in (ROOT/'managed-agent-cookbooks').rglob('*')
                   if p.is_file() and any(token in p.read_text(encoding='utf-8') for token in ('law-student',))]
    if recipe_refs:
        problems.append('New cookbook references: review inventory and scope')
    record('inventory_exact_coverage', problems, package_files=len(files), skills=len(skills), agents=len(agents), cookbook_references=recipe_refs)
    targeted = set()
    for proposal in proposals:
        targeted.update(re.findall(r'`(law-student/skills/[^`]+/SKILL.md)`', proposal.read_text(encoding='utf-8')))
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
    dec = (HERE / 'exist-010-decoupage-formation.md').read_text(encoding='utf-8')
    problems = [p.name for p in proposals if f'(suites/{p.name})' not in dec]
    for suffix in ('inventaire-formation', 'decoupage-formation', 'verification'):
        if f'(02-plugins-existants/exist-010-{suffix}.md)' not in index:
            problems.append(f'Missing index: {suffix}')
    for ident in ('EXIST-010', 'BASE-003', 'BASE-005', 'PILOTE-003'):
        if stories[ident][1]['statut'] != 'terminee':
            problems.append(f'{ident}: prerequisite/status not complete')
    count_match = re.search(r'Le backlog contient (\d+) stories', index)
    proposed_match = re.search(r'les (\d+) autres sont `proposee`', index)
    proposed_count = sum(fm['statut'] == 'proposee' for _, fm in stories.values())
    if not count_match or int(count_match[1]) != len(stories):
        problems.append('Backlog total count is stale')
    if not proposed_match or int(proposed_match[1]) != proposed_count:
        problems.append('Backlog proposed count is stale')
    record('index_and_prerequisites', problems)

    # Fidélité documentaire du support, distincte d'une validation de droit.
    support = json.loads(support_path.read_text(encoding='utf-8'))
    verification = (HERE / 'exist-010-verification.md').read_text(encoding='utf-8')
    problems = []
    provenance = support['source_provenance']
    for key in ('source_url', 'retrieved_at', 'archive_member', 'archive_sha256', 'xml_sha256'):
        if not provenance.get(key):
            problems.append(f'Missing source provenance: {key}')
    if (support['reference'] != 'JURITEXT000054167571'
            or support['network_lookup_this_story'] is not False
            or support['documentary_status'] != 'non-verifie'
            or support['applicability'] != 'a-etablir'):
        problems.append('Unexpected support identity or unsupported legal verification claim')
    if len(support['extracts']) != 2:
        problems.append('Expected visa and paragraph 28, no invented facts')
    for excerpt in support['extracts']:
        if hashlib.sha256(excerpt['text'].encode('utf-8')).hexdigest() != excerpt['sha256']:
            problems.append(f"Excerpt digest mismatch: {excerpt['label']}")
        if excerpt['text'] not in verification:
            problems.append(f"Excerpt absent or changed in verification: {excerpt['label']}")
    record('french_decision_support', problems, reference=support['reference'],
           provenance=provenance, legal_applicability='not-validated')
    original = ROOT / support['local_source_at_read']
    if original.is_file():
        source = json.loads(original.read_text(encoding='utf-8'))
        xml_hash = hashlib.sha256(source['xml'].encode('utf-8')).hexdigest()
        parsed = ET.fromstring(source['xml'])
        problems = []
        if xml_hash != provenance['xml_sha256'] or source['reference'] != support['reference']:
            problems.append('Original local XML identity/digest mismatch')
        if parsed.findtext('.//TITRE') != support['title'] or parsed.findtext('.//ECLI') != support['ecli']:
            problems.append('Original local decision metadata mismatch')
        if not all(e['text'] in source['text'] for e in support['extracts']):
            problems.append('Excerpt absent from original local reproduction')
        if not any(a.get('xml_sha256') == xml_hash and a.get('url') == provenance['source_url']
                   and a.get('sha256') == provenance['archive_sha256']
                   and a.get('archive_member') == provenance['archive_member']
                   and a.get('retrieved_at') == provenance['retrieved_at']
                   for a in source['attempts']):
            problems.append('Original local retrieval record differs')
        record('optional_original_local_source', problems,
               path=support['local_source_at_read'], xml_sha256=xml_hash,
               scope='local documentary comparison only, no new network retrieval')
    else:
        checks['optional_original_local_source'] = {
            'status': 'not-run', 'reason': 'Ignored local source unavailable; embedded support remains reviewable.'}

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
    record('links_and_format', problems, markdown_files=sum(p.suffix == '.md' for p in lot), local_links=links)

    # Repérage textuel des hypothèses héritées, jamais validation du droit.
    markers = {}
    for label, pattern in [('US_exams', r'MBE|MEE|MPT|UBE|NextGen'), ('IRAC', r'IRAC'), ('forecast', r'forecast|hobby horses'), ('memory_rules', r'majority rule|model knowledge'), ('history', r'session.history')]:
        hits = []
        for path in files:
            if path.suffix != '.md':
                continue
            positions = [i for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1) if re.search(pattern, line, re.I)]
            if positions:
                hits.append({'path': path.relative_to(ROOT).as_posix(), 'lines': positions})
        markers[label] = hits
    record('legacy_foreign_assumptions_located', [k for k, hits in markers.items() if not hits], locations=markers)

    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding='utf-8'))['files']
        before = {k: v for k, v in baseline.items() if k != REPORT.relative_to(ROOT).as_posix()}
        now = snapshot()
        changed = sorted(k for k in before.keys() | now.keys() if before.get(k) != now.get(k))
        outside = [p for p in changed if p not in allowed]
        checks['scope_vs_task_baseline'] = {
            'status': 'observed-concurrent-changes' if outside else 'passed',
            'baseline_sha256': digest(args.baseline),
            'lot_changed_files': [p for p in changed if p in allowed],
            'other_changed_files': outside,
            'note': 'Other differences observed during this task are not attributed to EXIST-010; no claim of an unchanged entire workspace.',
            'preserved_files': sum(now.get(k) == v for k, v in before.items() if k not in allowed),
        }
        protected = {k: v for k, v in before.items()
                     if not k.startswith('backlog/') or
                     re.match(r'backlog/02-plugins-existants/(?:exist-00[1-9]-|suites/)', k)}
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
        'story': 'EXIST-010', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'cadrage et relecture méthodologique sur consignes fictives et extrait français réel ; aucun skill exécuté ou droit validé',
        'checks': checks,
        'package_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in files},
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in lot + [Path(__file__)]},
        'not_run': ['recherche juridique externe', 'acte/délai réel', 'exécution de skill',
                    'installation/recette client', 'lecteur indépendant', 'connexion authentifiée/envoi/dépôt/paiement/publication/déploiement'],
        'command': 'python -X utf8 backlog/02-plugins-existants/exist-010-controles.py --baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-010-resultats.json',
        'notes': ['Les différences git préexistantes ne sont pas des changements EXIST-010 ; voir comparaison à l’instantané de début de tâche.',
                  'Aucune validation de schéma plugin/client : aucun fichier de paquet modifié.',
                  'Hypothèses étrangères repérées ; reproduction DILA locale lue sans nouvelle consultation réseau ; aucun raisonnement juridique validé.'],
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
