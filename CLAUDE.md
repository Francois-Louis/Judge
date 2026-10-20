<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

# CLAUDE.md

## Relecture : prise en charge par l'utilisateur

- Depuis le 17 octobre 2026, l'utilisateur relit lui-même tous les livrables.
  Ne pas maintenir une story ouverte uniquement pour attendre une relecture
  humaine, juridique, indépendante ou par un lecteur non juriste.
- Si seule cette relecture reste à faire, clore la story en consignant la
  prise en charge par l'utilisateur. Ne pas déclarer sa relecture effectuée
  ni un critère de compréhension vérifié sans résultat observé.
- Les défauts connus, tests non exécutés et autres critères non satisfaits
  restent à traiter ; cette consigne ne vaut pas validation technique.

## Git : terminer par un commit et un push

- Travailler directement sur `main`, sans branche de travail ni pull request,
  sauf demande explicite contraire de l'utilisateur.
- Pour toute tâche qui modifie le dépôt, vérifier le diff et exécuter les
  contrôles pertinents, puis terminer par un `git commit` et un
  `git push origin main`. Cette consigne autorise ces actions sans redemander
  confirmation à chaque tâche.
- Inclure uniquement les changements de la tâche dans le commit. Préserver
  les modifications préexistantes et ne pas les embarquer sans instruction.
- Si le commit ou le push échoue, signaler le blocage et ce qui reste à faire.
  Ne pas forcer le push ni écraser l'historique distant.

## Économie : aller à l'essentiel

- Recette payante (`scripts/recette-stories.py`, appel réel au client
  `claude`, workflow ou agents en parallèle) : jamais sans accord explicite de
  l'utilisateur, avec le nombre de cas et une estimation (environ 0,50 USD
  par cas). Une seule série complète ; après correction, rejouer seulement
  les cas en défaut (`--case`), sauf défaut touchant presque tous les cas.
  Indiquer le coût réellement dépensé dans le récapitulatif.
- Lectures minimales : ne pas réétudier la story précédente (diffs complets,
  `ETAT.md`, journaux) ; un seul exemple ciblé suffit pour le gabarit.
- Sources volumineuses filtrées localement ; seuls les passages utiles entrent
  dans le contexte. Sorties de commande bornées, jamais de dump de dizaines
  de Ko, pas de relecture d'un fichier déjà lu ou venant d'être écrit.
- Sorties de recette : recherche ciblée des défauts connus et des points
  obligatoires d'abord, lecture complète des seuls cas suspects.

Guidance for working on this repo. `judge-fr-eu` is the fork Claude Code plugin
marketplace — eighteen internal legal plugins and five
managed-agent cookbooks. Most work here is editing prompt content (skills,
agents, hooks), plugin metadata, or cookbook config — not application code.

BASE-008 uses `judge-fr-eu-<domain>` as every published identifier; source
directories and the 134 inherited skill names stay unchanged; CONSO-001,
BNK-001, ENF-001, CRIM-001, FUN-001, INS-001, DOU-001, DOU-002, DOU-003, DOU-004, DOU-005, DOU-006 and DOU-009 add one skill each (147 total). Only the fork config root is
active. Every entry point loads the packaged storage contract. Sync
`scripts/judge_store.py` and `references/isolation.md` byte-for-byte into all
eighteen packages after changes, and include LICENSE/NOTICE. The vendor source
is preserved but excluded from this marketplace. This is technical isolation;
legal adaptation and live-client validation remain separate results.

Run `python scripts/test-base008-isolation.py` for detached-package filesystem
and hub lifecycle tests. Cookbook dry-runs require Bash, jq, Python/PyYAML;
`bash scripts/test-cookbooks.sh` supplies disposable deployment IDs without
network calls. The orchestrator storage test also needs jsonschema; a missing
tool is reported as skipped, never as passed. Shell scripts use the first
working `python3`/`python` (override with `PYTHON`), since Windows may expose a
non-functional Store stub as `python3`. Real deployments require an explicit fresh `JUDGE_DEPLOYMENT_ID`.

For the fork's France/EU adaptation, follow the
[BASE-003 domain architecture](backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md).
Each task has one primary domain plugin; proposed plugins and skills are not
implemented features. Ship required references inside each adapted plugin,
including a versioned copy of the shared research/citation method from
`references/research-citation-method.md` (BASE-005). Copy it unchanged into
`<plugin>/references/shared/research-citation-method.md` and make adapted skills
load that local copy; root references are editing sources, not runtime dependencies.
The architecture describes the target contract, not a claim that
existing packages already meet it.

For legal research during maintenance/adaptation, follow
[official source access](references/legal-source-access.md). A web-tool 403,
JavaScript challenge or empty 202 is not a reason to stop all research. Use
`python scripts/legal_sources.py travail <article> --legifrance-id <id>` for
the official labour-code reproduction, or `python scripts/legal_sources.py eu
<CELEX>` for EUR-Lex/CELLAR. `legi-versions <article>... | --reference <file>`
reports future versions and end dates of labour-code articles from the LEGI
stock and every later daily delta (about 3 GB, run in the background). Record each route and read the actual text/version;
transport success does not certify legal applicability. For other French
sources, `dila-list <FUND>` and `dila-read <archive-url> <exact-id>` provide
public DILA archives/XML without an API subscription (bounded single-archive
reads, not a complete corpus search). `juri-read <CASS|INCA|CAPP|JADE|CONSTIT>
<id>` reads one decision by identifier from that fund's stock and later deltas
(maintenance only, BASE-018). PISTE is optional and the user reports
subscription is unavailable; do not make research depend on it. This is a maintenance tool,
not a runtime dependency of installed plugins. Do not use inherited approval
prompts to request repeated permission for an already-authorized official-source
lookup; reserve only the conclusions whose sources remain unverified.

## Layout

```
.claude-plugin/marketplace.json   # the marketplace manifest — one entry per plugin
<plugin>/                         # 18 first-party plugins (commercial-legal, privacy-legal, ...)
  .claude-plugin/plugin.json      # plugin manifest (name, version, description, author)
  .mcp.json                       # MCP servers the plugin connects to
  CLAUDE.md                       # practice-profile TEMPLATE (see "Plugin CLAUDE.md" below)
  README.md                       # per-plugin docs
  skills/<name>/SKILL.md          # one skill per directory
  agents/<name>.md                # subagent definitions
  hooks/hooks.json                # hook config (most plugins ship an empty stub)
  .gitignore
external_plugins/<vendor>/        # vendor-maintained plugins (CoCounsel)
managed-agent-cookbooks/<name>/   # CMA agent.yaml + subagents/ + steering-examples.json
scripts/                          # validate.py, lint-tool-scope.py, orchestrate.py,
                                  # deploy-managed-agent.sh, test-cookbooks.sh
references/                       # shared templates (company-profile, dashboard)
```

## Validation — run before opening a PR

This repo follows the same conventions `anthropics/claude-plugins-official`
enforces in CI. Run the equivalent checks locally:

```bash
# 1. Marketplace + per-plugin schema validation (source of truth)
claude plugin validate .claude-plugin/marketplace.json
for d in */; do [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"; done
claude plugin validate external_plugins/cocounsel-legal

# 2. Cookbook tool-scope lint (orchestrators must not over-grant tools)
python3 scripts/lint-tool-scope.py

# 3. JSON/YAML sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
```

For France/EU adaptation lots, also follow the
[BASE-006 validation checklist](references/package-validation.md). Run
`python scripts/check-plugin-package.py <installed-plugin-root>` against the
single installed/extracted artifact, outside the checkout, and use `--schema`
to request the official validator separately. When `claude` is not on the
PATH, pass `--claude <path>` or set `JUDGE_CLAUDE_CLI` (e.g. the binary bundled
with the Claude desktop app). This bounded static check needs
PyYAML; it does not execute a skill or validate legal reasoning. Missing tools,
manual-review findings, and unexecuted scenarios must remain explicit in the
lot's report. Controller fixtures: `python scripts/test-check-plugin-package.py`.

Before building a lot, re-read every official source linked from the
delivered plugins' business references and record it in their `Relecture`
column (`AAAA-MM-JJ · issue · voie`, BASE-014). `scripts/build-lot.py` requires
`--relecture-depuis <start of lot preparation>` and refuses stale, missing or
unintegrated reviews; check earlier with `python scripts/source_reviews.py
<plugin> --depuis <date>`. Fixtures: `python scripts/test-source-reviews.py`.

### Marketplace invariants (I1–I11)

`claude-plugins-official` layers these on top of the schema check. They apply
here too — the ones most likely to trip a contributor:

- **I1** — `plugins[]` should be alpha-sorted by name (case-insensitive).
  *Currently a known warning: the array is in a curated display order. If you
  add a plugin, ask before re-sorting the whole array.*
- **I2** — no duplicate plugin names.
- **I3** — `description` 10–2000 chars, no leading/trailing whitespace.
- **I8** — every vendored `source` (`"./<dir>"`) must point at a directory that
  contains `.claude-plugin/plugin.json`.
- **I9** — `source` paths/URLs must contain no shell metacharacters or `..`.
- **I10** — no hidden Unicode (zero-width chars, bidi controls) in
  `name`/`description`.
- **I11** — `name` must match `^[a-z0-9][a-z0-9-]{1,63}$`.

### Frontmatter requirements

Every `agents/*.md` needs `name` and `description`. Every
`skills/<name>/SKILL.md` needs `description`. Every `commands/*.md` needs
`description`. Multi-line descriptions use `>` block scalars and that's fine —
`claude plugin validate` parses them correctly.

## Conventions

### Keep `marketplace.json` in sync with `plugin.json`

For first-party plugins, `marketplace.json`'s `name`, `description`, and
`author` should match the plugin's own `.claude-plugin/plugin.json` field for
field. If you change a plugin's description in one place, change it in the
other.

### Bump the plugin version on every shipped change

Claude Code caches installed plugins by `version`: without a bump, a pushed
skill or agent never reaches users who update the marketplace. Any commit that
changes files under `<plugin>/` raises that plugin's `version` in
`<plugin>/.claude-plugin/plugin.json` (patch by default, minor for a new skill
or adapted domain). Also update the expected version in
`scripts/test-base008-isolation.py` and any version quoted in the plugin
description. Before pushing, run `python scripts/check-version-bump.py`
(compares with `origin/main`, `--base <ref>` otherwise).

### Skill names in prose must be canonical

When a `SKILL.md` (especially `customize` or `cold-start-interview`) tells the
user "run `/foo`," `foo` must be the actual `skills/<foo>/` directory name.
Short forms like `/triage` for `/use-case-triage` look right in prose but are
dead commands — the user types them and nothing happens. Refs to Claude Code
built-ins (`/mcp`, `/plugin`) and to other plugins (`/<other-plugin>:<skill>`)
are fine.

### Plugin CLAUDE.md is a template, not project context

Each `<plugin>/CLAUDE.md` is a practice-profile template that the
`cold-start-interview` skill copies to `~/.claude/plugins/config/judge-fr-eu/<domain>/CLAUDE.md`
on the user's machine. It is *not* loaded as project context when the plugin is
installed — `claude plugin validate` warns about this and the warning is
expected. Don't "fix" it by moving the content into a skill.

### `external_plugins/` is vendor-maintained

Plugins under `external_plugins/` are built and maintained by the vendor
(README.md has the policy). Don't change vendor-authored content without
checking with them first; whitespace normalization and formatting are usually
fine since the vendor lands changes via PR rather than mirroring a fork.

### NOTICE files

Root and plugin `NOTICE` files record one dated entry per story that changes
files outside `backlog/`: plugin files, references, scripts. Backlog files are
not listed; the story itself records them.

### Formatting

- 2-space indent in all JSON and `.mcp.json` files.
- Final newline at end of every text file.
- No trailing whitespace.
- Markdown tables: pipe-aligned columns are nice but not required; just keep
  the column count consistent.

## Cookbooks

Each `managed-agent-cookbooks/<name>/` has `agent.yaml` (the orchestrator),
`subagents/*.yaml` (the leaves), `steering-examples.json`, and `README.md`. Two
rules that `scripts/lint-tool-scope.py` enforces:

1. The orchestrator gets local-only tools (`read`, `grep`, `glob`,
   `agent_toolset`); MCP and write tools belong to specific subagent leaves.
2. The README's security table and the `agent.yaml` comments must match what
   the YAML actually grants. Don't claim a tool a subagent doesn't have.

## Things to leave alone

- Per-plugin `.gitignore` files differ slightly across plugins. Probably
  intentional; ask before unifying.
- `hooks/hooks.json` is missing in two plugins. Hooks are optional; the missing
  files are not a bug.
- Root `references/` are editing sources. BASE-008 embeds the company/dashboard templates, shared method and storage boundary in every internal package. Keep shipped copies synchronized explicitly.
