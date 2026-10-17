<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

# Judge FR/UE

**Version technique 0.1.0.** Fork indépendant de Claude for Legal / Anthropic,
maintenu sur [Francois-Louis/Judge](https://github.com/Francois-Louis/Judge),
sans affiliation revendiquée. BASE-008 isole les noms, profils et données ;
le pilote `employment-legal:hiring-review` 0.2.1 est réécrit pour l'embauche
privée en France, recette client faite sur fixtures et lecteur non indépendant,
livré seul dans le [lot LIV-001](backlog/04-livraison/liv-001-annexes/liv-001-notes-version.md) ; `commercial-legal:review`
0.2.0 est réécrit pour l'orientation contractuelle COM-001 sans profil obligatoire,
avec validation client/utilisateur à compléter ; `employment-legal:worker-classification`
0.3.0 qualifie une relation de travail proposée en France avant exécution (TRAV-001) ; les autres
tâches juridiques héritées restent à adapter à la France et à l'UE.
Depuis BASE-013 (méthode commune 1.1.0, paquets 0.1.1, 0.2.1 et 0.3.1), ces tâches
adaptées terminent chaque réponse par une phrase courte nommant le professionnel
compétent, avec un renfort en tête en cas d'urgence, de procédure ou de pénal.
Depuis BASE-016 (méthode commune 1.2.0, paquets 0.1.2, 0.2.2 et 0.3.4), une
décision de justice n'est citée qu'après lecture de ses motifs, par des voies
officielles sans abonnement ; à défaut, la conclusion qui en dépend est réservée.
`consumer-legal:non-delivery-claim` 0.1.0 prépare la fiche, la chronologie et
le brouillon au vendeur pour une commande non livrée (CONSO-001), sans profil
ni envoi ; validation client et lecteur à compléter.
`criminal-legal:summons-reading` 0.1.0 lit une convocation de police ou de
gendarmerie pour un majeur (CRIM-001) : mentions, inconnues, authenticité et
questions au service et à un avocat, sans stockage du dossier ni envoi ;
recette client et lecteur à compléter.
Voir le [démarrage du fork](QUICKSTART.md), les [preuves et limites de validation](references/base008-validation.md),
la [licence](LICENSE) et les [fichiers modifiés](NOTICE).
Les intégrations Cowork/Office et l'exécution distante décrites ci-dessous
proviennent de la documentation amont et restent à vérifier pour ce fork.

Reference agents, skills, and data connectors for the legal workflows we see most — in-house commercial, privacy, product, corporate, employment, litigation, regulatory, AI governance, IP, and the learning side of the practice (law students).

> **New here?** Start with [QUICKSTART.md](QUICKSTART.md) — install in 60 seconds. This README is the full reference.

Everything here is available **two ways from one source**: install it as a [Claude Cowork](https://claude.com/product/cowork) or [Claude Code](https://claude.com/product/claude-code) plugin, or deploy it through the [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) behind your own workflow engine. Same system prompt, same skills — you choose where it runs.

## Getting started in Cowork
- [Install Claude Desktop](https://claude.com/download)
- Get access to Claude Cowork
- Follow the instructions in the video below:

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

> [!IMPORTANT]
> **Every output from these plugins is a draft for attorney review — not legal advice, not a legal conclusion, not a substitute for a lawyer.** They are built with guardrails that reflect that: source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced, and explicit gates before anything is filed, sent, or relied on. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it.
>
> **These plugins do not represent Anthropic's legal positions.** They are tools that help lawyers analyze issues. Where a skill includes a checklist item, a suggested framework, a risk flag, or a characterization of case law or regulatory guidance, that is an aid to the reviewing attorney's own analysis, not a statement of Anthropic's view of the law. The law in many of these areas is unsettled and evolving. The attorney using the plugin — not the plugin, and not Anthropic — is responsible for the legal positions taken in their work product.

What's in the repo:

- **Practice-area plugins** covering in-house, firm, and academic legal work — each one built around a cold-start interview that learns your playbook and a `CLAUDE.md` practice profile that every skill reads from.
- **Managed-agent cookbooks** for the scheduled, eyes-on-the-feed workflows (renewal watcher, docket watcher, regulatory feed monitor, diligence grid, launch radar).
- **MCP connectors** across general productivity (Slack, Google Drive, Box) and legal-specific systems (Ironclad, DocuSign, iManage, Everlaw, CourtListener, and more).
- **[Named agents](#agents)** — end-to-end workflow agents (Vendor Agreement Reviewer, DSAR Responder, Termination Reviewer, Claim Chart Builder, …) with job-style names and a single command to run each one.

## Agents

Each agent is named for the workflow it runs. They're the most common surface — start with the ones that match your work, then tune the underlying skill, the practice profile, and the connectors to how your team does it.

| Agent | What it does | Plugin | Command |
|---|---|---|---|
| **Lire une convocation** | Mentions, qualité inconnue ou indiquée, authenticité et questions ; CRIM-001, sans profil ni stockage | `criminal-legal` | `/judge-fr-eu-criminal-legal:summons-reading` |
| **Commande non livrée** | Fiche, chronologie, pièces et brouillon au vendeur ; CONSO-001, sans profil ni envoi | `consumer-legal` | `/judge-fr-eu-consumer-legal:non-delivery-claim` |
| **Acte de recouvrement ou d’exécution reçu** | Lecture, authenticité, urgence, fiche et questions ; ENF-001 | `enforcement-legal` | `/judge-fr-eu-enforcement-legal:enforcement-act-reading` |
| **Orientation contractuelle** | Qualifie contrat/récit, domaine, achat/vente, pièces et suite ; COM-001, sans profil obligatoire | `commercial-legal` | `/judge-fr-eu-commercial-legal:review` |
| **Revue prestation / NDA / SaaS** | Branches héritées non adaptées France/UE ; COM-002/003/004 proposés, aucun lancement par `review` | `commercial-legal` | — |
| **Amendment Tracer** | Traces how a contract has changed across its base agreement and every amendment | `commercial-legal` | `/judge-fr-eu-commercial-legal:amendment-history` |
| **Renewal Watcher** | Scans the contract register for cancel-by and renewal deadlines | `commercial-legal` | scheduled agent |
| **Deal Debrief** | Weekly sweep of signed agreements with playbook deviations — prompts the attorney to log context while memory is fresh | `commercial-legal` | scheduled agent |
| **Playbook Monitor** | Watches the deviation log and proposes playbook updates when a clause has drifted | `commercial-legal` | scheduled agent |
| **Escalation Router** | Routes contract issues to the right approver and drafts the ask | `commercial-legal` | `/judge-fr-eu-commercial-legal:escalation-flagger` |
| **Tabular Diligence Review** | Tabular review over a data room with one row per document and every cell cited | `corporate-legal` | `/judge-fr-eu-corporate-legal:tabular-review` |
| **Issue Extractor** | Reads VDR documents and extracts issues per house categories and materiality thresholds | `corporate-legal` | `/judge-fr-eu-corporate-legal:diligence-issue-extraction` |
| **Board Consent Drafter** | Drafts unanimous written consents in house format with precedent search | `corporate-legal` | `/judge-fr-eu-corporate-legal:written-consent` |
| **Material Contracts Schedule Builder** | Builds the disclosure schedule from diligence findings against the purchase-agreement threshold | `corporate-legal` | `/judge-fr-eu-corporate-legal:material-contract-schedule` |
| **Entity Compliance Tracker** | Computes filing deadlines across jurisdictions and entity types, runs health audits | `corporate-legal` | `/judge-fr-eu-corporate-legal:entity-compliance` |
| **Closing Checklist Driver** | Tracks every condition, consent, document, and filing blocking close | `corporate-legal` | `/judge-fr-eu-corporate-legal:closing-checklist` |
| **Integration Runbook** | Phased post-closing integration plan with consent tracking and weekly status | `corporate-legal` | `/judge-fr-eu-corporate-legal:integration-management` |
| **Data Room Watcher** | Monitors the VDR for new uploads and posts closing checklist status on schedule | `corporate-legal` | scheduled agent |
| **Termination Reviewer** | Runs a proposed termination against jurisdiction-specific risk flags | `employment-legal` | `/judge-fr-eu-employment-legal:termination-review` |
| **Hire Reviewer** | Reviews offer letters and restrictive covenants with a jurisdiction check | `employment-legal` | `/judge-fr-eu-employment-legal:hiring-review` |
| **Worker Classification Screener** | Qualifier une relation de travail proposée en France (faits, critères, sources, pièces), sans choix automatique du statut | `employment-legal` | `/judge-fr-eu-employment-legal:worker-classification` |
| **Leave Tracker** | Monitors open leaves with FMLA/CFRA/PFL/ADA deadlines and decision-point alerts | `employment-legal` | scheduled agent |
| **Investigation Lead** | Opens, tracks, adds to, and summarizes internal investigation matters | `employment-legal` | `/judge-fr-eu-employment-legal:investigation-open` |
| **Policy Drafter** | Drafts employment policies with state supplements where law differs | `employment-legal` | `/judge-fr-eu-employment-legal:policy-drafting` |
| **International Expansion Planner** | Kicks off EOR-vs-entity planning and outside-counsel briefing for a new country | `employment-legal` | `/judge-fr-eu-employment-legal:expansion-kickoff` |
| **Wage & Hour Q&A** | Jurisdiction-aware employment Q&A for the "quick question" channel | `employment-legal` | `/judge-fr-eu-employment-legal:wage-hour-qa` |
| **DSAR Responder** | Drafts DSAR acknowledgments and substantive responses within statutory timelines | `privacy-legal` | `/judge-fr-eu-privacy-legal:dsar-response` |
| **DPA Reviewer** | Reviews a DPA against your playbook as controller or processor | `privacy-legal` | `/judge-fr-eu-privacy-legal:dpa-review` |
| **PIA Generator** | Generates a Privacy Impact Assessment in house format for a new feature or activity | `privacy-legal` | `/judge-fr-eu-privacy-legal:pia-generation` |
| **Privacy Triager** | Decides whether a processing activity needs a PIA, a mandatory GDPR DPIA, or can proceed | `privacy-legal` | `/judge-fr-eu-privacy-legal:use-case-triage` |
| **Privacy Reg Gap Checker** | Diffs a new or changed regulation against current privacy policy and practice | `privacy-legal` | `/judge-fr-eu-privacy-legal:reg-gap-analysis` |
| **Privacy Policy Monitor** | Sweeps saved PIAs, DPA reviews, and triage results for policy drift | `privacy-legal` | `/judge-fr-eu-privacy-legal:policy-monitor` |
| **Launch Reviewer** | Reviews a product launch against your risk calibration | `product-legal` | `/judge-fr-eu-product-legal:launch-review` |
| **Marketing Claims Checker** | Flags copy that needs substantiation, reframing, or cutting | `product-legal` | `/judge-fr-eu-product-legal:marketing-claims-review` |
| **"Is this a problem?" Triage** | Fast answer for the quick Slack question — pattern-matches your calibration | `product-legal` | `/judge-fr-eu-product-legal:is-this-a-problem` |
| **Launch Watcher** | Watches the launch tracker for upcoming launches that need legal review | `product-legal` | scheduled agent |
| **Reg Feed Watcher** | Polls regulatory feeds and writes the Monday-morning digest | `regulatory-legal` | scheduled agent |
| **On-demand Reg Check** | Check regulatory feeds now and report what's new since last check | `regulatory-legal` | `/judge-fr-eu-regulatory-legal:reg-feed-watcher` |
| **Policy Diff** | Diffs a specific regulatory change against the indexed policy library | `regulatory-legal` | `/judge-fr-eu-regulatory-legal:policy-diff` |
| **Gap Tracker** | Open gaps tracker — what's flagged and not yet closed | `regulatory-legal` | `/judge-fr-eu-regulatory-legal:gaps` |
| **Policy Redrafter** | Marked-up policy redraft closing a gap — a proposal for the policy owner's review, not a direct edit to source documents | `regulatory-legal` | `/judge-fr-eu-regulatory-legal:policy-redraft` |
| **NPRM Comment Tracker** | Review open NPRM comment periods, log decisions, track deadlines | `regulatory-legal` | `/judge-fr-eu-regulatory-legal:comments` |
| **AI Use Case Triager** | Classifies proposed AI use cases against your registry | `ai-governance-legal` | `/judge-fr-eu-ai-governance-legal:use-case-triage` |
| **AI Impact Assessor** | Runs an AIA across the regimes in scope | `ai-governance-legal` | `/judge-fr-eu-ai-governance-legal:aia-generation` |
| **Vendor AI Reviewer** | Reviews vendor AI terms for training-on-data, liability, model-change, and policy gaps | `ai-governance-legal` | `/judge-fr-eu-ai-governance-legal:vendor-ai-review` |
| **AI Reg Gap Checker** | Diffs a new AI regulation against your current governance posture | `ai-governance-legal` | `/judge-fr-eu-ai-governance-legal:reg-gap-analysis` |
| **AI Policy Monitor** | Sweeps saved AIAs, triage results, and vendor reviews for AI-policy drift | `ai-governance-legal` | `/judge-fr-eu-ai-governance-legal:policy-monitor` |
| **Trademark Clearance Screener** | First-pass clearance with knockout check and confusion heuristics | `ip-legal` | `/judge-fr-eu-ip-legal:clearance` |
| **Cease & Desist Drafter** | Drafts or triages a C&D, calibrated to your enforcement posture | `ip-legal` | `/judge-fr-eu-ip-legal:cease-desist` |
| **DMCA Takedown** | Drafts a takedown, triages one received, or drafts a §512(g) counter-notice | `ip-legal` | `/judge-fr-eu-ip-legal:takedown` |
| **OSS Compliance Checker** | Classifies open source licenses against your deployment model | `ip-legal` | `/judge-fr-eu-ip-legal:oss-review` |
| **FTO Triager** | Structured first look at potentially blocking patents — triage, not an opinion | `ip-legal` | `/judge-fr-eu-ip-legal:fto-triage` |
| **Infringement Triager** | Triage across TM / copyright / patent / trade secret — factors, not a finding | `ip-legal` | `/judge-fr-eu-ip-legal:infringement-triage` |
| **IP Clause Reviewer** | Reviews assignment, ownership, license grants, warranties, and indemnities | `ip-legal` | `/judge-fr-eu-ip-legal:ip-clause-review` |
| **IP Portfolio Tracker** | Registrations, renewals, maintenance fees, use declarations | `ip-legal` | `/judge-fr-eu-ip-legal:portfolio` |
| **IP Renewal Watcher** | Scheduled deadline report from the IP portfolio register | `ip-legal` | scheduled agent |
| **Claim Chart Builder** | Element-by-element claim chart, patent or civil cause of action | `litigation-legal` | `/judge-fr-eu-litigation-legal:claim-chart` |
| **Docket Watcher** | Monitors court dockets for filings and deadlines | `litigation-legal` | scheduled agent |
| **Demand Letter Drafter** | Drafts a demand with FRE 408 awareness and a send gate | `litigation-legal` | `/judge-fr-eu-litigation-legal:demand-draft` |
| **Demand Intake** | Pre-drafting context gathering — parties, facts, basis, leverage, privilege | `litigation-legal` | `/judge-fr-eu-litigation-legal:demand-intake` |
| **Demand Received Triage** | Triages an inbound demand — options, portfolio cross-check, handoff | `litigation-legal` | `/judge-fr-eu-litigation-legal:demand-received` |
| **Subpoena Triage** | Classifies, scopes, and plans compliance with a new subpoena | `litigation-legal` | `/judge-fr-eu-litigation-legal:subpoena-triage` |
| **Chronology Builder** | Builds or updates a chronology from declared sources and uploads | `litigation-legal` | `/judge-fr-eu-litigation-legal:chronology` |
| **Deposition Prep** | Builds a deposition outline tied to case theory with docs and impeachment | `litigation-legal` | `/judge-fr-eu-litigation-legal:deposition-prep` |
| **Brief Section Drafter** | Drafts a brief section in house style, consistent with case theory | `litigation-legal` | `/judge-fr-eu-litigation-legal:brief-section-drafter` |
| **Privilege Log Reviewer** | First-pass privilege log review — obvious calls + flags for attorney review | `litigation-legal` | `/judge-fr-eu-litigation-legal:privilege-log-review` |
| **Legal Hold** | Issue, refresh, release, or report on legal holds | `litigation-legal` | `/judge-fr-eu-litigation-legal:legal-hold` |
| **Matter Intake** | Uniform intake for a new matter — writes matter.md, history.md, appends to log | `litigation-legal` | `/judge-fr-eu-litigation-legal:matter-intake` |
| **Matter Briefing** | Deep briefing on one matter — ready for a GC or outside counsel call | `litigation-legal` | `/judge-fr-eu-litigation-legal:matter-briefing` |
| **Portfolio Status** | Risk distribution, upcoming deadlines, stale matters | `litigation-legal` | `/judge-fr-eu-litigation-legal:portfolio-status` |
| **Outside Counsel Status** | Generates weekly status-request drafts across the active portfolio | `litigation-legal` | `/judge-fr-eu-litigation-legal:oc-status` |
| **Bar Prep Coach** | Jurisdiction-aware MBE and essay practice targeted at weak subjects | `law-student` | `/judge-fr-eu-law-student:bar-prep-questions` |
| **Socratic Drill Sergeant** | It asks, you answer, it pushes back — does not give you the answer | `law-student` | `/judge-fr-eu-law-student:socratic-drill` |
| **IRAC Grader** | Grades your IRAC essay on structure, issue-spotting, rules, analysis | `law-student` | `/judge-fr-eu-law-student:irac-practice` |
| **Case Briefer** | Brief a case in your preferred format | `law-student` | `/judge-fr-eu-law-student:case-brief` |
| **Outline Builder** | Build or extend an outline in your format from class notes and casebook | `law-student` | `/judge-fr-eu-law-student:outline-builder` |
| **Cold Call Prep** | Predicts professor's questions and drills them before class | `law-student` | `/judge-fr-eu-law-student:cold-call-prep` |
| **Exam Forecaster** | Analyze past exams from the same professor; forecast likely emphases | `law-student` | `/judge-fr-eu-law-student:exam-forecast` |
| **Legal Writing Critic** | Structural feedback on a draft — never rewrites | `law-student` | `/judge-fr-eu-law-student:legal-writing` |
| **Flashcard Drillmaster** | Generate or drill flashcards — Leitner-style buckets | `law-student` | `/judge-fr-eu-law-student:flashcards` |
| **Study Planner** | Long-term study plan with scheduled sessions, adaptive to session history | `law-student` | `/judge-fr-eu-law-student:study-plan` |
| **Skill Registry Browser** | Search watched registries for community legal skills | `legal-builder-hub` | `/judge-fr-eu-legal-builder-hub:registry-browser` |
| **Skill Installer** | Install a community skill with trust checks and skills-QA | `legal-builder-hub` | `/judge-fr-eu-legal-builder-hub:skill-installer` |
| **Skill QA** | Evaluate a skill against the Legal Skill Design Framework | `legal-builder-hub` | `/judge-fr-eu-legal-builder-hub:skills-qa` |
| **Community Skill Recommender** | Suggest community skills based on recent activity in other plugins | `legal-builder-hub` | `/judge-fr-eu-legal-builder-hub:related-skills-surfacer` |
| **Community Skill Updater** | Check for updates to installed community skills | `legal-builder-hub` | `/judge-fr-eu-legal-builder-hub:auto-updater` |
| **Registry Sync** | Periodic check of watched registries for new and updated skills | `legal-builder-hub` | scheduled agent |

For Managed Agent deployment — `agent.yaml`, leaf-worker subagents, steering-event examples, and per-agent security notes — see **[managed-agent-cookbooks/](./managed-agent-cookbooks)**.

## Repository Layout

```
commercial-legal/         # in-house commercial — vendor/NDA/SaaS review, renewals, escalations
corporate-legal/          # M&A diligence, closing checklists, board consents, entity compliance
employment-legal/         # hire/term review, worker classification, leave, investigations
privacy-legal/            # DPA, DSAR, PIA, privacy triage, policy monitor
product-legal/            # launch review, marketing claims, "is this a problem?" triage
regulatory-legal/         # reg feed watcher, policy diff, gap tracker, NPRM comments
ai-governance-legal/      # AI use-case triage, AIAs, vendor AI review, AI reg gap-check
ip-legal/                 # trademark clearance, FTO, C&D, DMCA, OSS, IP clauses, portfolio
litigation-legal/         # portfolio, matters, holds, demands, depo prep, claim charts
law-student/              # Socratic drilling, outlining, IRAC, bar prep, flashcards
legal-builder-hub/        # community skill discovery and install with a trust gate
external_plugins/         # partner-built plugins maintained by their vendors
  cocounsel-legal/        # Thomson Reuters — Westlaw Deep Research via the CoCounsel Legal MCP
managed-agent-cookbooks/  # Claude Managed Agent cookbooks — one dir per scheduled agent
  diligence-grid/
  docket-watcher/
  launch-radar/
  reg-monitor/
  renewal-watcher/
scripts/                  # deploy-managed-agent.sh · validate.py · orchestrate.py · lint-tool-scope.py · test-cookbooks.sh
.claude-plugin/
  marketplace.json        # plugin registry
```

Each plugin directory has the same shape:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # template practice profile — filled in by /<plugin>:cold-start-interview
  README.md
  skills/                 # skills — each is a /<plugin>:<skill> slash command
  agents/                 # scheduled agents (if any)
  hooks/                  # pre- and post-tool hooks (if any)
```

## Getting Started

### Claude Cowork

In Cowork:

1. Open the **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **Browse plugins** and install the ones you want, **or** upload a custom plugin file (any plugin directory zipped up).

After install, skills fire automatically when relevant, slash commands are available via `/`, and the scheduled agents run on the cadence set in their frontmatter.

### Claude Code

```bash
# Add the marketplace (use the absolute path to this repo or a GitHub URL)
/plugin marketplace add <path-to-this-repo>

# Install a plugin — pick the ones that match your practice
/plugin install judge-fr-eu-commercial-legal@judge-fr-eu --scope user
/plugin install judge-fr-eu-privacy-legal@judge-fr-eu --scope user
/plugin install judge-fr-eu-corporate-legal@judge-fr-eu --scope user

# Restart Claude Code, then run setup for each plugin you installed.
# This writes your practice profile to ~/.claude/plugins/config/judge-fr-eu/<domain>/CLAUDE.md
/judge-fr-eu-commercial-legal:cold-start-interview
/judge-fr-eu-privacy-legal:cold-start-interview
/judge-fr-eu-corporate-legal:cold-start-interview
```

**Run the cold-start interview first for inherited workflows.** CONSO-001
(`consumer-legal`) requires no profile or setup. Every other inherited skill in a plugin reads from the practice profile it writes. Skipping setup is the single most common reason a skill produces generic output. The interview takes 10–20 minutes per plugin and will ask you to point at seed documents (a signed MSA, a playbook, a prior review memo — whatever fits the plugin). More seed material is better; a **quick start** option is available if you want to be productive in 2 minutes and refine later.

**Start by connecting a research tool.** Everything else is better with one, and citations are unverified without one. See [MCP Connectors](#mcp-connectors) below for the full list — CourtListener, Trellis, Descrybe, and Solve Intelligence are the research tools the citation guardrails look for.

Updates require review of the selected fork package and explicit scope. Disable automatic updates for `judge-fr-eu` during validation; see [QUICKSTART.md](QUICKSTART.md).

### Claude Managed Agents

For the scheduled agents — regulatory feed monitor, renewal watcher, docket watcher, diligence grid, launch radar — deploy behind your own orchestrator:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export JUDGE_DEPLOYMENT_ID=demo-2026-10-15
scripts/deploy-managed-agent.sh reg-monitor
scripts/deploy-managed-agent.sh renewal-watcher
scripts/deploy-managed-agent.sh docket-watcher
scripts/deploy-managed-agent.sh diligence-grid
scripts/deploy-managed-agent.sh launch-radar
```

Each template under [`managed-agent-cookbooks/`](./managed-agent-cookbooks) references the same system prompt and skills as its plugin counterpart. The deploy script resolves file references, uploads skills, creates leaf-worker subagents, and POSTs the orchestrator to `/v1/agents`. See [`scripts/orchestrate.py`](./scripts/orchestrate.py) for a reference event loop that routes `handoff_request` events between agents via your own orchestration layer.

> **Research Preview:** subagent delegation (`callable_agents`) is a preview capability and supports a single delegation level. See per-agent READMEs for security tier and handoff guidance.

## How It Fits Together

| | What it is | Where it lives |
|---|---|---|
| **Plugins** | Self-contained practice-area bundles — skills, agents, hooks, and a template practice profile. Install the ones you need. | `<plugin>/` |
| **Skills** | Domain expertise, conventions, and step-by-step methods Claude draws on automatically when relevant — and slash actions you trigger explicitly: `/judge-fr-eu-commercial-legal:review`, `/judge-fr-eu-privacy-legal:dsar-response`, `/judge-fr-eu-litigation-legal:claim-chart`. | `<plugin>/skills/<skill>/SKILL.md` |
| **Agents** | Scheduled or event-driven workflows (renewal watcher, docket watcher, reg-change monitor). Runs in the background, posts to a channel or writes a file. | `<plugin>/agents/` |
| **Practice profile** | Plain-English `CLAUDE.md` describing your playbook, escalation rules, and house style. Every skill reads from it. | `~/.claude/plugins/config/judge-fr-eu/<domain>/CLAUDE.md` |
| **Connectors** | [MCP servers](https://modelcontextprotocol.io/) that wire Claude to your data — CLM, DMS, e-discovery, research platforms, productivity. | `.mcp.json` (per plugin) |
| **Managed-agent cookbooks** | `agent.yaml` + depth-1 subagents + steering examples for headless deployment. | `managed-agent-cookbooks/<slug>/` |

Everything is markdown and JSON. No build step.

## Vertical Plugins

Grouped by where the work sits. Cold-start interviews tailor inherited workflows
to a team. The COM-001 contract orientation starts directly from documents or a
narrative, without a profile or interview.

### Transactional & advisory

| Plugin | What it adds |
|---|---|
| **[criminal-legal](./criminal-legal)** | CRIM-001 `0.1.0` : lire une convocation de police ou de gendarmerie pour un majeur ; un skill sans profil ni stockage, [recette et limites](backlog/03-nouveaux-domaines/suites/crim-001-annexes/verification.md). |
| **[consumer-legal](./consumer-legal)** | CONSO-001 : fiche, chronologie, pièces et brouillon de réclamation pour un bien commandé à distance et non reçu. Un skill sans profil ni envoi ; validation client et lecteur à compléter. |
| **[banking-legal](./banking-legal)** | BNK-001 `0.1.1` : qualifier un paiement contesté et préparer la réclamation pour une opération non autorisée sur un compte personnel ; tromperie et litige commercial orientés. Un skill, sans profil ni stockage ; [recette partielle et limites](backlog/03-nouveaux-domaines/suites/bnk-001-annexes/verification.md). |
| **[enforcement-legal](./enforcement-legal)** | ENF-001 `0.1.0` : lire un acte reçu, vérifier l'authenticité, repérer l'urgence et préparer les questions. Un skill sans profil, calcul de délai ni envoi ; [recette et limites](backlog/03-nouveaux-domaines/suites/enf-001-annexes/verification.md). |
| **[commercial-legal](./commercial-legal)** | Orientation contractuelle COM-001 sans profil obligatoire. Revues, avenants, registres, escalades et agents hérités non adaptés France/UE. |
| **[corporate-legal](./corporate-legal)** | M&A diligence with tabular review and citation-per-cell. Disclosure schedules, closing checklists, written consents, board minutes. Entity compliance tracker. Post-close integration. |
| **[privacy-legal](./privacy-legal)** | Privacy triage (PIA vs DPIA vs proceed), PIA generation, DPA review as controller or processor, DSAR response. Policy monitor watches drift between policy and practice. |
| **[product-legal](./product-legal)** | Launch review against house risk calibration. Marketing claims check. "Is this a problem?" triage for Slack questions. Feature risk assessment. |
| **[employment-legal](./employment-legal)** | Hire and termination review with jurisdiction-specific flags. Worker classification. Leave tracker (FMLA/CFRA/PFL/ADA). Internal investigations. Policy drafting with state supplements. |
| **[ai-governance-legal](./ai-governance-legal)** | AI use-case triage against your registry. Impact assessments across regimes in scope. Vendor AI review. Reg-to-policy gap analysis. |
| **[regulatory-legal](./regulatory-legal)** | Regulatory feed watcher, policy diff, gaps tracker, NPRM comment-period tracker. The Monday-morning digest your team actually reads. |
| **[ip-legal](./ip-legal)** | Trademark clearance, FTO triage, C&D drafting and triage, DMCA takedown and counter-notice, OSS compliance, IP clause review, portfolio tracking. |

### Litigation

| Plugin | What it adds |
|---|---|
| **[litigation-legal](./litigation-legal)** | Works two surfaces. **In-house/portfolio:** matter intake, portfolio status, legal holds, outside counsel status, demands. **Firm/solo:** chronology building, claim charts (patent and civil), deposition prep, privilege log review, brief drafting. |

### Learning & practice

| Plugin | What it adds |
|---|---|
| **[law-student](./law-student)** | Socratic drilling, case briefing, outline building, IRAC grading, cold-call prep, flashcards, bar prep, exam forecasting, study planning. **Learning mode, not answer mode** — it never writes the answer for you. |

### Ecosystem

| Plugin | What it adds |
|---|---|
| **[legal-builder-hub](./legal-builder-hub)** | Community skill discovery and install with a real trust layer — watched registries, a QA framework (`/judge-fr-eu-legal-builder-hub:skills-qa`), SHA-pinned updates, and a mandatory trust check before anything lands in your environment. |

### External / partner-built

Plugins under [`external_plugins/`](./external_plugins) are built and maintained by their vendors. Their sources are preserved for provenance; they are excluded from this fork marketplace and must be obtained from their original distribution. The vendor owns the code, connector and support channel.

| Plugin | Built by | What it adds |
|---|---|---|
| **[cocounsel-legal](./external_plugins/cocounsel-legal)** | Thomson Reuters | Westlaw Deep Research with fully cited reports — caselaw, statutes, regulations, Practical Law, and secondary sources across up to three U.S. jurisdictions per run. Requires a CoCounsel Legal subscription with the MCP connector enabled. Support: cocounselsupport@tr.com. |

## The trust layer for community legal skills

The community is building legal skills fast — registries like LegalOps Consulting's `lpm-skills` and Lawvable already list dozens. But nobody certifies community skills, and a lawyer installing a random skill from GitHub is installing code that runs with access to their matter files, their practice profile, and their research connectors.

`legal-builder-hub` gives the ecosystem the trust layer it's missing:

- **Security review** — hidden-content scan, injection detection, structural trust check on every install
- **Allowlist** — restrictive-by-default source gate (registries, publishers, connectors, licenses)
- **License gate** — deployment-context-aware license policy (personal / firm-internal / product-embedding)
- **Freshness gate** — tracks whether bundled reference content (regulations, statutes, procedures) has passed its verification window, and warns at invocation
- **Re-scan at update** — a skill that was clean at v1.0 and poisoned at v1.1 gets caught
- **Install log** — an auditable record of what's installed, from where, under what license, with what review verdict

The allowlist is restrictive by default. Permissive mode is an explicit choice. A non-lawyer gets routed to their attorney contact, not an "install anyway" button.

Community skills go through the same design review (`/judge-fr-eu-legal-builder-hub:skills-qa`) as the first-party plugins. If you build for lawyers, run the QA against your own skill before publishing. It's the review a lawyer would do if they could read code.

## MCP Connectors

> [!IMPORTANT]
> **Connect a research tool first.** Every plugin ships with legal research connectors already configured — CourtListener, Trellis, Descrybe, Solve Intelligence, and others depending on practice area. You authorize them once, and from then on Claude pulls from authoritative sources and verifies its citations against current databases instead of relying on training knowledge. Citations that come through a research connector are tagged with the source. Citations from model knowledge alone are flagged `[verify]` and, if no research tool is connected at all, the reviewer note above the deliverable records that sources weren't verified so you know to check. The connectors are what make the cites trustworthy — set them up before you set up anything else.

These plugins ship connectors for the systems legal teams live in. A connector gives Claude the ability to read from and (where scoped) write to your data; the skills and commands use them.

| Connector | What it gives Claude | Plugins | Notes |
|---|---|---|---|
| **Slack** | Read channels, search, send messages and canvases | all plugins | Your workspace |
| **Google Drive** | Read docs, sheets, slides; fetch by link | all plugins | Your account |
| **CoCounsel Legal (Thomson Reuters)** | Westlaw Deep Research — cited reports across caselaw, statutes, regulations, Practical Law | `cocounsel-legal` | Customer subscription; OAuth |
| **Box** | Read files and folders in VDRs and matter rooms | `corporate-legal` | Your tenant |
| **Ironclad** | Read the contract register, renewal dates, clauses | `commercial-legal` | Customer subscription |
| **DocuSign / DocuSign CLM** | Envelope status, executed contracts, CLM metadata | `commercial-legal` | Customer subscription |
| **iManage** | Read from the DMS — matter workspaces, document versions | `commercial-legal`, `corporate-legal` | Customer subscription |
| **Everlaw** | E-discovery productions, tagged sets, chronologies | `litigation-legal` | Customer subscription |
| **CourtListener** | Federal dockets and opinions | `ip-legal`, `litigation-legal`, `law-student` | Public; optional API key |
| **Trellis** | State court dockets and motions | `litigation-legal` | Customer subscription |
| **Aurora** | Clinic-style matter management and calendaring | `litigation-legal` | Customer subscription |
| **Definely** | In-document drafting and defined-terms checks | `commercial-legal`, `corporate-legal` | Customer subscription |
| **Lawve AI** | Contract review assist and clause libraries | `legal-builder-hub` | Customer subscription |
| **Descrybe** | Case law research and summarization | `ip-legal`, `law-student` | Customer subscription |
| **Solve Intelligence** | Patent drafting and prosecution | `corporate-legal`, `ip-legal` | Customer subscription |
| **TopCounsel** | Matter routing and outside counsel panel | `commercial-legal`, `corporate-legal`, `litigation-legal` | Customer subscription |
| **Linear** | Launch tracker, issue tracking | `product-legal` | Customer workspace |
| **Atlassian (Jira)** | Launch tracker, issue tracking | `product-legal` | Customer workspace |
| **Asana** | Launch tracker, project tracking | `product-legal` | Customer workspace |

> Connectors marked "customer subscription" need the customer's own account and API key. Configure them in each plugin's `.mcp.json` or via `claude mcp` in your Claude Code setup.

> **Building a connector?** See [CONNECTORS.md](./CONNECTORS.md) for what a good legal MCP server looks like and how to submit yours for inclusion.

## Claude for Microsoft 365

Les intégrations Word/Excel décrites par l'amont restent à vérifier dans ce
fork. `judge-fr-eu-commercial-legal:review` produit désormais une fiche
d'orientation dans la conversation ; il ne promet pas de redline Word ni de
revue prestation/NDA/SaaS. Les autres workflows Office hérités restent non adaptés.

The Excel-facing skills produce workbooks that open cleanly: `judge-fr-eu-corporate-legal:tabular-review` writes a multi-sheet `.xlsx` with a sources sheet, `judge-fr-eu-litigation-legal:claim-chart` writes an element-by-element claim chart with citation columns, `judge-fr-eu-corporate-legal:entity-compliance` writes the compliance register with deadline columns, and `judge-fr-eu-commercial-legal:renewal-tracker` exports the renewal register sorted by cancel-by date.

Install Claude for Microsoft 365 from **[Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/wa200010453)**. Once installed, the skills from any plugin you've enabled are available from the sidebar via `/`, and connectors are reachable from the same surface. A single thread can span Word, Excel, PowerPoint, and Outlook.

For IT admins deploying the add-in against your own cloud (Vertex AI, Bedrock, or an internal gateway) rather than Anthropic's API, see the separate [`claude-for-msft-365-install`](https://github.com/anthropics/financial-services/tree/main/claude-for-msft-365-install) tooling.

## Making It Yours

These are reference templates. They get better when you tune them to how your team works — and the customization mechanism is the plugin itself, not a config file buried in a repo.

- **Run the cold-start interview.** It **is** the customization mechanism. It asks how your practice works, reads your seed documents, and writes your practice profile. Every other skill reads from that profile. A `/judge-fr-eu-commercial-legal:cold-start-interview` with five signed MSAs, your playbook, and your escalation matrix will make the review skills noticeably sharper.
- **Edit the practice profile.** Your profile lives at `~/.claude/plugins/config/judge-fr-eu/<domain>/CLAUDE.md`. Edit it directly for small fixes — a wrong escalation threshold, a new integration, a policy update. It survives plugin updates.
- **Re-run setup.** `/<plugin>:cold-start-interview` again for a full re-interview when your practice shifts materially (new jurisdiction, new CLM, new policy).
- **Swap connectors.** Point `.mcp.json` at your CLM, DMS, e-discovery platform, launch tracker, HRIS. Skills fall back gracefully when a connector isn't configured — no silent no-ops.
- **Bring your playbook and templates.** Drop your terminology, house style, and branded templates into the plugin's `CLAUDE.md` and `references/`. The skills will pick them up.
- **Fork skills for house style.** Every skill is a markdown file under `skills/`. Edit the steps, the gates, the output format.
- **Add scheduled agents.** The agents under `<plugin>/agents/` are markdown with a cron-style schedule. Add your own for the watchers your team needs.

No build step. Everything is markdown and JSON.

## Skill & Command Reference

The full map across all plugins. Inherited workflows start with the cold-start interview.
The consumer and criminal plugins require no setup.

### Police et procédure pénale — CRIM-001

| Command | Skill | Description |
|---|---|---|
| `/judge-fr-eu-criminal-legal:summons-reading` | summons-reading | Lire une convocation pour un majeur ; [périmètre et limites](criminal-legal/README.md), recette client et lecteur à compléter |

### Consommation — CONSO-001

| Command | Skill | Description |
|---|---|---|
| `/judge-fr-eu-consumer-legal:non-delivery-claim` | non-delivery-claim | Préparer une réclamation pour une commande non livrée ; recette client et lecteur à compléter |

### ai-governance-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-ai-governance-legal:cold-start-interview` | cold-start-interview | Cold-start — learns your AI governance practice |
| `/judge-fr-eu-ai-governance-legal:ai-inventory` | ai-inventory | EU AI Act per-system inventory — track each system's role and risk tier |
| `/judge-fr-eu-ai-governance-legal:use-case-triage` | use-case-triage | Classify AI use case — approved, conditional, or no |
| `/judge-fr-eu-ai-governance-legal:aia-generation` | aia-generation | Run an AI impact assessment in house format |
| `/judge-fr-eu-ai-governance-legal:vendor-ai-review` | vendor-ai-review | Review vendor AI terms against governance positions |
| `/judge-fr-eu-ai-governance-legal:reg-gap-analysis` | reg-gap-analysis | Diff a new AI regulation against your governance posture |
| `/judge-fr-eu-ai-governance-legal:policy-monitor` | policy-monitor | Keep the AI policy current with practice |
| `/judge-fr-eu-ai-governance-legal:policy-starter` | policy-starter | Draft a firm AI usage policy from published model policies, adapted to your practice profile |
| `/judge-fr-eu-ai-governance-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |

### legal-builder-hub

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-legal-builder-hub:cold-start-interview` | cold-start-interview | Practice profile interview and starter-pack recommendation |
| `/judge-fr-eu-legal-builder-hub:registry-browser` | registry-browser | Search watched registries for community legal skills |
| `/judge-fr-eu-legal-builder-hub:skill-installer` | skill-installer | Install a community skill with trust checks |
| `/judge-fr-eu-legal-builder-hub:skills-qa` | skills-qa | Evaluate a skill against the Design Framework |
| `/judge-fr-eu-legal-builder-hub:related-skills-surfacer` | related-skills-surfacer | Suggest community skills from activity in other plugins |
| `/judge-fr-eu-legal-builder-hub:auto-updater` | auto-updater | Check for updates to installed community skills |
| `/judge-fr-eu-legal-builder-hub:disable` | skill-manager | Disable a community skill without removing files |
| `/judge-fr-eu-legal-builder-hub:uninstall` | skill-manager | Uninstall a community skill installed via the hub |
| scheduled | registry-sync (agent) | Periodic check of watched registries for updates |

### commercial-legal

COM-001 adapte uniquement l'orientation. Toutes les autres lignes de ce tableau
décrivent des composants hérités non adaptés France/UE ; voir le
[périmètre du paquet](commercial-legal/README.md). L'interview reste facultative
pour l'orientation ponctuelle.

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-commercial-legal:cold-start-interview` | cold-start-interview | Cold-start — learn your commercial contracts practice |
| `/judge-fr-eu-commercial-legal:review` | review | Orienter contrat/récit, domaine et tâche, avec pièces et questions ; aucune revue aval automatique |
| `/judge-fr-eu-commercial-legal:amendment-history` | amendment-history | Trace contract changes across base and amendments |
| `/judge-fr-eu-commercial-legal:renewal-tracker` | renewal-tracker | Show contracts with cancel-by deadlines within 90 days |
| `/judge-fr-eu-commercial-legal:escalation-flagger` | escalation-flagger | Route a contract issue and draft the ask |
| `/judge-fr-eu-commercial-legal:review-proposals` | (internal) | Review and approve pending playbook update proposals |
| `/judge-fr-eu-commercial-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| — | stakeholder-summary | Translates a review into a business-stakeholder summary |
| scheduled | renewal-watcher (agent) | Weekly sweep of the renewal register |
| scheduled | deal-debrief (agent) | Weekly surface of signed agreements with deviations |
| scheduled | playbook-monitor (agent) | Proposes playbook updates when a clause has drifted |

### corporate-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-corporate-legal:cold-start-interview` | cold-start-interview | House cold-start, with optional `--new-deal` kickoff |
| `/judge-fr-eu-corporate-legal:tabular-review` | tabular-review | Tabular review — one row per document, every cell cited |
| `/judge-fr-eu-corporate-legal:diligence-issue-extraction` | diligence-issue-extraction | Extract issues from VDR documents per house thresholds |
| `/judge-fr-eu-corporate-legal:material-contract-schedule` | material-contract-schedule | Build material contracts disclosure schedule |
| `/judge-fr-eu-corporate-legal:closing-checklist` | closing-checklist | What's blocking close with critical path |
| `/judge-fr-eu-corporate-legal:written-consent` | written-consent | Draft board or committee consent in house format |
| `/judge-fr-eu-corporate-legal:entity-compliance` | entity-compliance | Entity compliance tracker across jurisdictions |
| `/judge-fr-eu-corporate-legal:integration-management` | integration-management | Post-closing integration tracker with consent tracking |
| `/judge-fr-eu-corporate-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| — | board-minutes | Drafts board or committee minutes in house format |
| — | deal-team-summary | Aggregates diligence findings into a deal briefing |
| — | ai-tool-handoff | Detects Luminance/Kira, QAs bulk-tool output |
| scheduled | dataroom-watcher (agent) | Monitors VDR uploads and posts checklist status |

### employment-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-employment-legal:cold-start-interview` | cold-start-interview | Cold-start — learns jurisdictions and escalation rules |
| `/judge-fr-eu-employment-legal:wage-hour-qa` | wage-hour-qa | Jurisdiction-aware wage/hour and employment Q&A |
| `/judge-fr-eu-employment-legal:hiring-review` | hiring-review | Review offer letter and restrictive covenants |
| `/judge-fr-eu-employment-legal:termination-review` | termination-review | Termination review with high-risk flag detection |
| `/judge-fr-eu-employment-legal:worker-classification` | worker-classification | Qualifier une relation proposée avant exécution (France) |
| `/judge-fr-eu-employment-legal:policy-drafting` | policy-drafting | Draft employment policy with state supplements |
| `/judge-fr-eu-employment-legal:leave-tracker` | leave-tracker | Check open leaves for deadline alerts |
| `/judge-fr-eu-employment-legal:log-leave` | log-leave | Add a new leave to the leave register |
| `/judge-fr-eu-employment-legal:investigation-open` | internal-investigation | Open a new internal investigation matter |
| `/judge-fr-eu-employment-legal:investigation-add` | internal-investigation | Add data to an open investigation — docs, notes |
| `/judge-fr-eu-employment-legal:investigation-memo` | internal-investigation | Draft or update the privileged investigation memo |
| `/judge-fr-eu-employment-legal:investigation-query` | internal-investigation | Ask questions against an open investigation log |
| `/judge-fr-eu-employment-legal:investigation-summary` | internal-investigation | Draft audience-specific summary from investigation memo |
| `/judge-fr-eu-employment-legal:expansion-kickoff` | international-expansion | Kick off expansion planning for a new country |
| `/judge-fr-eu-employment-legal:expansion-update` | international-expansion | Update status of an in-progress expansion project |
| `/judge-fr-eu-employment-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| — | handbook-updates | Diffs handbook changes and flags state supplement impacts |
| scheduled | leave-tracker (agent) | Weekly monitor of open leaves with hard deadlines |

### ip-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-ip-legal:cold-start-interview` | cold-start-interview | Cold-start — learn your IP practice and posture |
| `/judge-fr-eu-ip-legal:clearance` | clearance | Trademark clearance first pass — knockout + similar marks |
| `/judge-fr-eu-ip-legal:fto-triage` | fto-triage | Freedom-to-operate triage, not an FTO opinion |
| `/judge-fr-eu-ip-legal:invention-intake` | invention-intake | Invention disclosure first-pass screen — novelty, obviousness, §101, bar dates |
| `/judge-fr-eu-ip-legal:cease-desist` | cease-desist | Draft a C&D or triage one you received |
| `/judge-fr-eu-ip-legal:takedown` | takedown | DMCA notice, response triage, or §512(g) counter-notice |
| `/judge-fr-eu-ip-legal:infringement-triage` | infringement-triage | Infringement triage across all four IP rights |
| `/judge-fr-eu-ip-legal:ip-clause-review` | ip-clause-review | Review IP clauses — assignment, license, warranties |
| `/judge-fr-eu-ip-legal:oss-review` | oss-review | Open source license compliance check |
| `/judge-fr-eu-ip-legal:portfolio` | portfolio | Track IP portfolio deadlines and renewals |
| `/judge-fr-eu-ip-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| scheduled | ip-renewal-watcher (agent) | Weekly report of IP portfolio deadlines |

### litigation-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-litigation-legal:cold-start-interview` | cold-start-interview | Cold-start — risk, landscape, house brief style |
| `/judge-fr-eu-litigation-legal:matter-intake` | matter-intake | Intake a new matter — writes matter.md and history |
| `/judge-fr-eu-litigation-legal:matter-briefing` | matter-briefing | Deep briefing on one matter for a call |
| `/judge-fr-eu-litigation-legal:matter-update` | matter-update | Append a dated event to a matter's history |
| `/judge-fr-eu-litigation-legal:portfolio-status` | portfolio-status | Portfolio rollup — risk, deadlines, stale matters |
| `/judge-fr-eu-litigation-legal:matter-close` | matter-close | Close a matter — archive, retain record |
| `/judge-fr-eu-litigation-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| `/judge-fr-eu-litigation-legal:demand-intake` | demand-intake | Pre-drafting context — parties, facts, leverage |
| `/judge-fr-eu-litigation-legal:demand-draft` | demand-draft | Draft demand letter with FRE 408 gate and .docx output |
| `/judge-fr-eu-litigation-legal:demand-received` | demand-received | Triage inbound demand — options, portfolio cross-check |
| `/judge-fr-eu-litigation-legal:subpoena-triage` | subpoena-triage | Triage subpoena — scope, burden, privilege, plan |
| `/judge-fr-eu-litigation-legal:legal-hold` | legal-hold | Issue, refresh, release, or report on legal holds |
| `/judge-fr-eu-litigation-legal:oc-status` | oc-status | Weekly status-request emails to outside counsel |
| `/judge-fr-eu-litigation-legal:claim-chart` | claim-chart | Element chart — patent or civil cause of action |
| `/judge-fr-eu-litigation-legal:chronology` | chronology | Build or update a chronology from sources and uploads |
| `/judge-fr-eu-litigation-legal:deposition-prep` | deposition-prep | Deposition outline tied to case theory |
| `/judge-fr-eu-litigation-legal:privilege-log-review` | privilege-log-review | First-pass privilege log review with flags |
| `/judge-fr-eu-litigation-legal:brief-section-drafter` | brief-section-drafter | Draft a brief section in house style |
| scheduled | docket-watcher (agent) | Monitors court dockets for filings and deadlines |

### privacy-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-privacy-legal:cold-start-interview` | cold-start-interview | Cold-start — learns your privacy practice |
| `/judge-fr-eu-privacy-legal:use-case-triage` | use-case-triage | Determine PIA vs GDPR DPIA vs proceed |
| `/judge-fr-eu-privacy-legal:pia-generation` | pia-generation | Generate a Privacy Impact Assessment in house format |
| `/judge-fr-eu-privacy-legal:dpa-review` | dpa-review | Review a DPA — auto-detects controller vs processor |
| `/judge-fr-eu-privacy-legal:dsar-response` | dsar-response | Walk a DSAR and draft response — verify, locate, assess |
| `/judge-fr-eu-privacy-legal:reg-gap-analysis` | reg-gap-analysis | Diff a regulation against current policy and practice |
| `/judge-fr-eu-privacy-legal:policy-monitor` | policy-monitor | Keep the privacy policy current with practice |
| `/judge-fr-eu-privacy-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |

### product-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-product-legal:cold-start-interview` | cold-start-interview | Cold-start — connects launch tracker, learns calibration |
| `/judge-fr-eu-product-legal:is-this-a-problem` | is-this-a-problem | Fast "is this a problem?" answer for quick questions |
| `/judge-fr-eu-product-legal:launch-review` | launch-review | Full launch review against framework and calibration |
| `/judge-fr-eu-product-legal:marketing-claims-review` | marketing-claims-review | Review marketing copy for claims that need work |
| `/judge-fr-eu-product-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| — | feature-risk-assessment | Deep-dive risk on a single feature when launch review flags |
| scheduled | launch-watcher (agent) | Monitors launch tracker for upcoming reviews |

### regulatory-legal

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-regulatory-legal:cold-start-interview` | cold-start-interview | Cold-start — watchlist, policy index, materiality |
| `/judge-fr-eu-regulatory-legal:reg-feed-watcher` | reg-feed-watcher | Check regulatory feeds now and report what's new |
| `/judge-fr-eu-regulatory-legal:policy-diff` | policy-diff | Diff a regulatory change against the policy library |
| `/judge-fr-eu-regulatory-legal:gaps` | gap-surfacer | Open gaps tracker — what's flagged and not closed |
| `/judge-fr-eu-regulatory-legal:policy-redraft` | policy-redraft | Marked-up policy redraft closing a gap — proposal for the policy owner's review |
| `/judge-fr-eu-regulatory-legal:comments` | (tracker) | Review open NPRM comment periods and deadlines |
| `/judge-fr-eu-regulatory-legal:matter-workspace` | matter-workspace | Manage matter workspaces (practice-level) |
| scheduled | reg-change-monitor (agent) | Scheduled regulatory feed sweep with materiality filter |

### law-student

| Command | Skill | What it does |
|---|---|---|
| `/judge-fr-eu-law-student:cold-start-interview` | cold-start-interview | About-you interview — classes, bar, learning style |
| `/judge-fr-eu-law-student:socratic-drill` | socratic-drill | Socratic drill — it asks, you answer, it pushes back |
| `/judge-fr-eu-law-student:case-brief` | case-brief | Brief a case in your preferred format |
| `/judge-fr-eu-law-student:outline-builder` | outline-builder | Build or extend an outline in your format |
| `/judge-fr-eu-law-student:irac-practice` | irac-practice | Grade IRAC essay — structure, issues, rules, analysis |
| `/judge-fr-eu-law-student:legal-writing` | legal-writing | Structural feedback on your writing — never rewrites |
| `/judge-fr-eu-law-student:cold-call-prep` | cold-call-prep | Predict professor's questions and drill them |
| `/judge-fr-eu-law-student:bar-prep-questions` | bar-prep-questions | MBE or essay questions targeted at weak subjects |
| `/judge-fr-eu-law-student:flashcards` | flashcards | Generate or drill flashcards — Leitner-style |
| `/judge-fr-eu-law-student:exam-forecast` | exam-forecast | Analyze past exams to forecast likely emphases |
| `/judge-fr-eu-law-student:study-plan` | study-plan | Build or update a long-term study plan |
| `/judge-fr-eu-law-student:session` | study-plan | Run a focused N-question session; update the plan |

### CoCounsel (Thomson Reuters)

The vendor source is preserved under `external_plugins/cocounsel-legal/` for provenance. It is excluded from this fork marketplace; install it separately from its original distribution.

## Contributing

Fork contribution guidance updated for BASE-007. Open pull requests against
[Francois-Louis/Judge](https://github.com/Francois-Louis/Judge), checking the
base repository before submitting. A contribution to the original Claude for
Legal project is a separate, voluntary step under its own instructions.

The fork does not require signing the original project's CLA. [CLA.md](CLA.md)
is preserved unchanged as a historical document from Claude for Legal, naming
Anthropic PBC. Existing licenses and attributions remain in place. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the fork's contribution instructions and
the separate review needed if GitHub protections still require a CLA check.

- **New skill** → add it under `<plugin>/skills/<skill-name>/SKILL.md` with the frontmatter the existing skills use (`name`, `description`, `argument-hint`). Keep the description under 1024 characters — it's the trigger signal. The skill is invokable as `/<plugin>:<skill-name>`. Mark pure-reference skills `user-invocable: false`.
- **New agent** → add `<plugin>/agents/<name>.md` with scheduling frontmatter and the system prompt. Add a matching `managed-agent-cookbooks/<name>/` if you want headless deployment.
- **Community skills** → use `/judge-fr-eu-legal-builder-hub:skill-installer` to test a community skill in your environment. The hub runs `/judge-fr-eu-legal-builder-hub:skills-qa` against every skill before installing — it scores the skill against the Legal Skill Design Framework (nine design parameters, three legal failure modes, a trust-surface check) and rejects anything that fails.
- **Validate cookbooks before pushing** → `bash scripts/test-cookbooks.sh` dry-runs every managed-agent cookbook and lints orchestrator tool scope.

## License

Licensed under the [Apache License, Version 2.0](LICENSE).

Copyright 2026 Anthropic PBC.
