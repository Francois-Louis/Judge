"""Contrôles documentaires EXIST-011 ; aucune exécution ou validation juridique.

Usage : python -X utf8 backlog/02-plugins-existants/exist-011-annexes/exist-011-controles.py
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


ROOT = Path(__file__).resolve().parents[3]
ANNEXES = Path(__file__).resolve().parent
HERE = ANNEXES.parent
REPORT = ANNEXES / 'exist-011-resultats.json'
PACKAGE = ROOT / 'legal-builder-hub'


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

    proposals = sorted((HERE / 'suites').glob('hub-*.md'))
    lot = [HERE / 'exist-011-gestion-des-skills.md'] + [ANNEXES / f'exist-011-{suffix}.md' for suffix in (
        'inventaire-hub', 'decoupage-hub', 'verification')]
    lot += proposals + [ROOT / 'backlog/README.md']
    lot += [ANNEXES / name for name in ('exist-011-simulation.py', 'exist-011-simulation-resultats.json', 'exist-011-scenarios.json')]
    allowed = {p.relative_to(ROOT).as_posix() for p in lot + [Path(__file__), REPORT]}
    problems, future = [], {}
    if {k for k in stories if k.startswith('HUB-')} != {f'HUB-{i:03}' for i in range(1, 21)} or len(proposals) != 20:
        problems.append('Expected exactly 20 proposals HUB-001..020')
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
        if not {'EXIST-011', 'PILOTE-003', 'BASE-005', 'BASE-006', 'BASE-008', 'BASE-009'} <= set(fm['dependances']):
            problems.append(f'{ident}: missing prerequisite')
        for title in required:
            if f'## {title}\n' not in txt:
                problems.append(f'{ident}: missing {title}')
        if '- Cas normal :' not in txt or '- Cas limite :' not in txt:
            problems.append(f'{ident}: missing scenarios')
        targets = re.findall(r'^- `((?:legal-builder-hub|managed-agent-cookbooks)/[^`]+)`([^\n]*)', txt, re.M)
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

    inventory = (ANNEXES / 'exist-011-inventaire-hub.md').read_text(encoding='utf-8')
    skill_part, remainder = inventory.split('## L’agent livré', 1)
    agent_part, other_part = remainder.split('## Les dix-neuf autres fichiers du plugin', 1)
    other_part = other_part.split('## Dépendances de contenu et frontières', 1)[0]
    listed = {'skills/' + name for name in re.findall(r'^\| `([^`]+)` \|', skill_part, re.M)}
    for section in (agent_part, other_part):
        listed.update(re.findall(r'^\| `([^`]+)` \|', section, re.M))
    files = sorted(p for p in PACKAGE.rglob('*') if p.is_file())
    actual = {p.relative_to(PACKAGE).as_posix() for p in files}
    problems = []
    if listed != actual:
        problems.append({'missing': sorted(actual-listed), 'extra': sorted(listed-actual)})
    skills = list(PACKAGE.glob('skills/*/SKILL.md'))
    agents = list(PACKAGE.glob('agents/*.md'))
    if (len(files), len(skills), len(agents)) != (30, 10, 1):
        problems.append('Expected 30 package files, 10 skills, one agent')
    invocable = [p for p in skills if yaml.safe_load(p.read_text(encoding='utf-8').split('---', 2)[1]).get('user-invocable', True)]
    if len(invocable) != 9:
        problems.append('Expected nine invocable skills and one non-invocable reference')
    recipe_refs = [p.relative_to(ROOT).as_posix() for p in (ROOT/'managed-agent-cookbooks').rglob('*')
                   if p.is_file() and any(token in p.read_text(encoding='utf-8') for token in ('legal-builder-hub', 'registry-sync'))]
    if recipe_refs:
        problems.append('New cookbook references: review inventory and scope')
    record('inventory_exact_coverage', problems, package_files=len(files), skills=len(skills), invocable=len(invocable), agents=len(agents), cookbook_references=recipe_refs)
    targeted = set()
    for proposal in proposals:
        targeted.update(re.findall(r'`(legal-builder-hub/skills/[^`]+/SKILL.md)`', proposal.read_text(encoding='utf-8')))
    record('all_skills_have_future_targets', sorted(p.relative_to(ROOT).as_posix() for p in skills if p.relative_to(ROOT).as_posix() not in targeted))
    targeted_agents = set()
    for proposal in proposals:
        targeted_agents.update(re.findall(r'`(legal-builder-hub/agents/[^`]+)`', proposal.read_text(encoding='utf-8')))
    record('all_agents_have_future_targets', sorted(p.relative_to(ROOT).as_posix() for p in agents if p.relative_to(ROOT).as_posix() not in targeted_agents))

    shared = {
        'references/shared/research-citation-method.md': 'references/research-citation-method.md',
        'references/isolation.md': 'references/isolation.md',
        'references/company-profile-template.md': 'references/company-profile-template.md',
        'references/dashboard-template.md': 'references/dashboard-template.md',
        'scripts/judge_store.py': 'scripts/judge_store.py',
    }
    same = {dst: (PACKAGE/dst).read_bytes() == (ROOT/src).read_bytes() for dst, src in shared.items()}
    record('shared_copies', [p for p, ok in same.items() if not ok], identical=same, method_version='1.0.0')

    index = (ROOT / 'backlog/ETAT.md').read_text(encoding='utf-8')
    dec = (ANNEXES / 'exist-011-decoupage-hub.md').read_text(encoding='utf-8')
    problems = [p.name for p in proposals if f'(../suites/{p.name})' not in dec]
    for suffix in ('inventaire-hub', 'decoupage-hub', 'verification'):
        if f'(02-plugins-existants/exist-011-annexes/exist-011-{suffix}.md)' not in index:
            problems.append(f'Missing index: {suffix}')
    for ident in ('EXIST-011', 'BASE-003', 'BASE-005', 'PILOTE-003'):
        if stories[ident][1]['statut'] != 'terminee':
            problems.append(f'{ident}: prerequisite/status not complete')
    count = re.search(r'\| Total \| (\d+) \|', index)
    proposed = re.search(r'\| À faire \| (\d+) \|', index)
    if not count or int(count[1]) != len(stories):
        problems.append('Stale backlog total count')
    if not proposed or int(proposed[1]) != sum(fm['statut'] == 'proposee' for _, fm in stories.values()):
        problems.append('Stale backlog proposed count')
    record('index_and_prerequisites', problems)

    observations, problems = {}, []
    for rel in ('references/allowlist-default.yaml', 'skills/registry-browser/references/registries.yaml'):
        data = yaml.safe_load((PACKAGE / rel).read_text(encoding='utf-8'))
        unexpected = [k for k in data if k.startswith('<!--')]
        observations[rel] = {'keys': list(data), 'html_pseudo_comment_keys': unexpected,
                             'registries': data.get('registries'), 'mode': data.get('mode')}
        if len(unexpected) != 1:
            problems.append(f'{rel}: inherited YAML finding changed; refresh inventory')
    record('inherited_yaml_findings_recorded', problems, observations=observations,
           scope='Parseable YAML with extra key; observation only, not schema validation or repair')

    required_existing = {
        'agents/registry-sync.md': 'Install or apply anything. It reports;',
        'skills/auto-updater/SKILL.md': 'There is no "auto" mode.',
        'skills/customize/SKILL.md': 'There is no automatic-apply mode.',
        'README.md': 'There is no auto-apply mode.',
    }
    record('base009_existing_no_auto_statements', [rel for rel, phrase in required_existing.items()
           if phrase not in re.sub(r'\s+', ' ', (PACKAGE / rel).read_text(encoding='utf-8'))],
           scope='Existing statements located, not runtime enforcement tested')

    simulation = json.loads((ANNEXES / 'exist-011-simulation-resultats.json').read_text(encoding='utf-8'))
    expected_checks = {'customized_update_preserved', 'internal_identity_refused', 'filesystem_cli_requires_workflow_flag'}
    problems = []
    if set(simulation['checks']) != expected_checks or any(c['status'] != 'passed' for c in simulation['checks'].values()):
        problems.append('Recorded filesystem fixture did not pass all expected checks')
    if simulation['helper_sha256'] != digest(PACKAGE / 'scripts/community_store.py'):
        problems.append('Recorded simulation refers to another helper version')
    if simulation.get('network') or simulation.get('real_home_accessed') or not simulation.get('temporary_tree_removed'):
        problems.append('Unexpected simulation scope or cleanup state')
    preservation = simulation['checks']['customized_update_preserved']
    if (preservation['installed_before'] != preservation['installed_after']
            or not preservation['journal_unchanged'] or not preservation['candidate_unchanged']
            or preservation['events'] != ['install'] or preservation['backup_created']):
        problems.append('Recorded fixture does not preserve all customized files and journal')
    record('recorded_filesystem_simulation', problems, helper_sha256=simulation['helper_sha256'],
           checks=simulation['checks'], scope='Recorded offline fixture, not rerun by this documentary controller')

    fixture = json.loads((ANNEXES / 'exist-011-scenarios.json').read_text(encoding='utf-8'))['discovery_fixture']
    display = fixture['expected_display']
    problems = []
    if (fixture['requested_jurisdiction'] != 'FR'
            or fixture['candidate']['declared_jurisdiction'] != 'US-CA'
            or display['fit_for_requested_scope'] != 'Hors portée France demandée'
            or display['security_scan'] != 'Non exécuté'):
        problems.append('Discovery fixture lost explicit US scope or observation limits')
    if not all(ident in stories for ident in fixture['reviewed_proposals']):
        problems.append('Unknown proposal in documentary fixture')
    record('documentary_discovery_fixture', problems, expected_display=display,
           scope='Specification fixture reviewed; no actual browser, model or legal QA execution')

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
    for label, pattern in [('trust_modes', r'permissive|restrictive'), ('qa_override', r'override|advisory'), ('pinning', r'commit|tag'), ('notifications', r'schedule|Weekly|passively|Stop hook'), ('journal', r'install-log|metadata'), ('jurisdiction', r'jurisdiction|non-US|US framework')]:
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
            'note': 'Other differences observed during this task are not attributed to EXIST-011; no claim of an unchanged entire workspace.',
            'preserved_files': sum(now.get(k) == v for k, v in before.items() if k not in allowed),
        }
        protected = {k: v for k, v in before.items()
                     if k.startswith('legal-builder-hub/') or
                     re.match(r'backlog/02-plugins-existants/(?:(?:exist-00[1-9]-|exist-010-)|suites/)', k)}
        record('protected_inputs_unchanged', [k for k, v in protected.items() if now.get(k) != v],
               files_checked=len(protected),
               scope='Hub package and prior EXIST stories/suites; unrelated concurrent changes reported separately',
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
        'story': 'EXIST-011', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'scope': 'cadrage et relecture documentaire et fixture filesystem en faux home ; aucun skill exécuté ou droit validé',
        'checks': checks,
        'package_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in files},
        'lot_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in lot + [Path(__file__)]},
        'not_run': ['recherche juridique externe', 'acte/délai réel', 'exécution de skill',
                    'installation/recette client', 'lecteur indépendant', 'connexion authentifiée/envoi/dépôt/paiement/publication/déploiement'],
        'command': 'python -X utf8 backlog/02-plugins-existants/exist-011-annexes/exist-011-controles.py --baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-011-annexes/exist-011-resultats.json',
        'notes': ['Les différences git préexistantes ne sont pas des changements EXIST-011 ; voir comparaison à l’instantané de début de tâche.',
                  'Aucune validation de schéma plugin/client : aucun fichier de paquet modifié.',
                  'Contradictions héritées repérées localement ; simulation du helper hors ligne ; aucune règle produit actuelle ou juridique validée.'],
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
