# BASE-001 — Relevé de l’audit du fork

Relevé établi le **15 octobre 2026 (Europe/Paris)** dans le checkout
`C:\Users\fltou\Desktop\Judge`, avec Git `2.55.0.windows.2`.
Branche examinée : `main` ; HEAD : `4a6c651889c97cc9140580363c73e0eb17379c2b`.
Au départ, `git status --short` ne signalait que `?? backlog/` : le backlog
existait déjà dans l’espace de travail, sans être suivi par Git.

## Conclusion et portée

Dans la configuration effective observée, `git push` depuis `main` vise
**`git@github.com:Francois-Louis/Judge.git`, branche `main`**. Aucun remote
`upstream`, autre destinataire de push ou hook Git actif n’a été trouvé.
Un commit reste local ; ce push met à jour le fork et ne crée pas à lui seul
de PR vers le dépôt d’origine.

Le seul workflow GitHub présent est le contrôle CLA. Il agit sur des PR ou
commentaires existants et peut écrire des signatures dans le dépôt qui
exécute le workflow. Les autres mécanismes sont des scripts à lancer ou des
instructions de skills/agents à invoquer ; ils ne se déclenchent pas par un
push Git. Certains contactent des services tiers ou remplacent des fichiers
installés, ce qui demande une politique de mise à jour pour les adaptations.

Cet audit porte sur les fichiers et la configuration Git effective de cette
session. Il ne certifie ni l’état des réglages GitHub, ni l’absence de GitHub
Apps, webhooks, règles serveur, tâches planifiées sur la machine ou agents
déjà déployés. Les configurations privées de Claude et de SSH, les clés et
les secrets n’ont pas été inspectés. Aucun test de connexion SSH ni appel
authentifié au fork n’a été effectué. La configuration d’un autre poste,
un argument explicite à `git push` ou une configuration ultérieure peut
changer la destination. Le lien public avec l’origine reste à traiter dans
[BASE-002](../base-002-choix-lien-fork.md).

**Aucun push, aucune création de PR, aucun déploiement et aucune modification
distante n’ont été effectués.** Seules des lectures publiques de documentation
et du code de l’action CLA ont utilisé le réseau.

## 1. Git : destinations et suivi

Les observations suivantes proviennent des commandes de lecture exécutées
dans ce checkout, sans afficher de configuration d’authentification.

| Élément | Valeur observée | Effet |
|---|---|---|
| Remote unique | `origin` | Aucun remote `upstream` |
| URL de lecture effective | `git@github.com:Francois-Louis/Judge.git` | Lecture du fork |
| URL de push effective, toutes URL comprises | `git@github.com:Francois-Louis/Judge.git` | Écriture du fork |
| `remote.origin.fetch` | `+refs/heads/*:refs/remotes/origin/*` | Suivi local des branches du fork |
| `branch.main.remote` | `origin` | Remote suivi par `main` |
| `branch.main.merge` | `refs/heads/main` | Branche suivie : `origin/main` |
| `git for-each-ref` | `main -> origin/main`, sans avance/retard affiché | Comparaison avec la référence locale, sans interrogation distante |
| Origine des quatre valeurs configurées ci-dessus | portée `local`, fichier `.git/config` | Aucune surcharge correspondante globale/système observée |
| `remote.*.pushurl`, `remote.*.push`, `remote.*.mirror` | Absents | Pas de push séparé, de refspec de push ou de miroir configuré |
| `branch.*.pushRemote`, `remote.pushDefault`, `push.*` | Absents | Comportement Git par défaut, dont `push.default=simple` |
| `url.*.insteadOf`, `url.*.pushInsteadOf`, `include*` | Absents dans la configuration effective | Pas de réécriture d’URL ou d’inclusion observée |
| `core.hooksPath`, `core.sshCommand`, `ssh.variant`, `remote.*.receivepack/uploadpack/proxy` | Absents | Pas de substitution de transport par ces clés |
| Variables `GIT_*` / `SSH_*` présentes | Seulement `GIT_PAGER` ; valeur non reproduite | Aucun remplacement de transport par ces variables dans la session |

`git push`, `git push origin` et `git push origin main` ont ainsi la même
destination depuis `main`, avec l’état actuel. Une branche future sans suivi
peut être refusée par le mode `simple` ; cela ne la redirige pas vers l’origine.
La sélection du remote et le mode `simple` ont été confrontés à la
[documentation officielle de git-push](https://git-scm.com/docs/git-push).

Le répertoire effectif `.git/hooks/` contient uniquement les 14 fichiers
`*.sample` fournis comme exemples, dont `pre-push.sample` et
`post-update.sample` : aucun hook activé sans ce suffixe. Les anciens
répertoires de définition de remotes `.git/remotes` et `.git/branches` sont
absents. Ces exemples ne sont pas exécutés comme hooks par Git.

## 2. GitHub Actions et instructions de contribution

### Workflow unique : `.github/workflows/cla.yaml`

| Mécanisme | Déclencheur / destination | Écritures ou limites |
|---|---|---|
| `CLA Assistant` | `pull_request_target` : `opened`, `closed`, `synchronize` ; `issue_comment` : `created` | Pas de déclencheur `push`, `schedule` ou `workflow_dispatch` |
| Condition de l’étape | Toute occurrence `pull_request_target`, ou commentaire contenant `recheck` / la phrase de signature | Un événement peut lancer le job sans que l’étape s’exécute |
| Action externe | `iainmcgin/cla-github-action@3e58ace6af840f66fcd80f68c08d76559140df5e` | Code tiers épinglé ; aucun `run`, checkout ou script local appelé |
| Document présenté | `https://github.com/${{ github.repository }}/blob/main/CLA.md` | Sur le fork : `Francois-Louis/Judge/blob/main/CLA.md` |
| Signatures | `signatures/cla.json`, branche `cla-signatures`, dans le dépôt d’exécution | Création/mise à jour du fichier par API ; existence et protection de la branche distante non vérifiées |
| Jeton et permissions déclarées | `secrets.GITHUB_TOKEN` ; `actions`, `contents`, `pull-requests`, `statuses` en écriture | Capacités demandées ; disponibilité réelle dépend des réglages GitHub |
| Destinataire distant alternatif de signatures | Aucun input `remote-repository-name` ou `remote-organization-name`, aucun PAT fourni dans le workflow | Pas de redirection des signatures vers le dépôt d’origine dans ce fichier |

La lecture du code tiers épinglé confirme le chemin `action.yml` → Node 24 →
`dist/index.js`. Les sources `src/persistence/persistence.ts`,
`src/pullrequest/pullRequestComment.ts`, `src/pullRerunRunner.ts` et
`src/main.ts` montrent des écritures du fichier de signatures, des commentaires,
une possible relance du contrôle et le verrouillage d’une PR sur événement
`closed` avec l’option par défaut. Le code ne conditionne pas ce verrouillage
à une fusion effective. Il ne crée pas de PR ; la branche de signatures doit
être disponible pour que l’écriture réussisse. Les destinations par défaut
sont celles du contexte GitHub d’exécution, pas celles du checkout local.
Sources consultées au SHA exact :
[déclaration de l’action](https://github.com/iainmcgin/cla-github-action/blob/3e58ace6af840f66fcd80f68c08d76559140df5e/action.yml),
[persistance](https://github.com/iainmcgin/cla-github-action/blob/3e58ace6af840f66fcd80f68c08d76559140df5e/src/persistence/persistence.ts),
[point d’entrée](https://github.com/iainmcgin/cla-github-action/blob/3e58ace6af840f66fcd80f68c08d76559140df5e/src/main.ts).
Le bundle distribué a été consulté sans être exécuté ; ce n’est pas un audit
complet de ses dépendances.

Si une PR vers l’origine existe déjà, un push sur sa branche source peut
actualiser cette PR et déclencher les contrôles du dépôt cible. Cela est
distinct d’une création de PR ; l’existence de telles PR n’a pas été vérifiée.

### Textes hérités

- [CLA.md](../../../CLA.md) désigne Anthropic PBC et le projet Claude for Legal.
  Sa présence ne contacte aucun service ; le workflow peut inviter à le signer.
- [CONTRIBUTING.md](../../../CONTRIBUTING.md), « Before your first PR », demande
  cette signature comme préalable général. Cette consigne est héritée et
  ne définit pas une politique propre au fork.
- [README.md](../../../README.md), « Contributing », conseille « Fork, edit, PR ».
  C’est une instruction manuelle, sans commande de création de PR.
- [LICENSE](../../../LICENSE) et les attributions sont distincts du contrôle
  automatisé de signature ; aucun texte de licence n’est modifié par cet audit.

## 3. Scripts présents : lancement explicite

Les cinq fichiers exécutables applicatifs trouvés hors `.git` sont dans
`scripts/`. Aucun n’est appelé par le workflow CLA.

| Script examiné | Destination et effet à l’exécution | Lien avec Git |
|---|---|---|
| [deploy-managed-agent.sh](../../../scripts/deploy-managed-agent.sh) | `POST /v1/skills` : archive des skills ; `POST /v1/agents` : workers puis orchestrateur. API par défaut `https://api.anthropic.com`, remplaçable par `ANTHROPIC_API_BASE` ; authentification `ANTHROPIC_API_KEY` | Lit `remote.origin.url` pour construire le tag `Judge/<rôle>` sauf surcharge `REPO_SLUG` ; cela ne choisit pas un dépôt à modifier. Aucun push/PR |
| Même script, `--dry-run` | Résout les manifestes et écrit des fichiers temporaires ; ses branches de code évitent les appels API et l’exigence de clé | Pas de publication ; mode lu, non exécuté pendant cet audit |
| [orchestrate.py](../../../scripts/orchestrate.py) | Client `anthropic.Anthropic()` : lit un flux de session, appelle `sessions.steer` pour les IDs fournis par `AGENT_IDS`, journal local `./out/handoff-audit.jsonl` | Peut déclencher du travail distant et un relais de notification via un agent ; aucun client GitHub ou push/PR. Point d’entrée SDK dépendant de l’environnement, non vérifié à distance |
| [test-cookbooks.sh](../../../scripts/test-cookbooks.sh) | Appelle le lint puis le déploiement des cinq cookbooks avec `--dry-run`, contrôle le JSON résolu | Contrôle local, pas une publication ; code des scripts appelés lu |
| [lint-tool-scope.py](../../../scripts/lint-tool-scope.py) | Lit les `agent.yaml`, vérifie les droits des orchestrateurs | Contrôle local sans réseau ; exécuté avec succès sur les cinq cookbooks |
| [validate.py](../../../scripts/validate.py) | Valide une sortie JSON contre un schéma JSON/YAML passé en argument | Aucun déploiement ni synchronisation. Son code concerne les sorties de workers, malgré la mention plus générale de validation dans `CONTRIBUTING.md` |

## 4. Skills, agents et connecteurs : instructions à interpréter

Ces fichiers décrivent un comportement à exécuter par un hôte disposant des
outils et des accès requis. Une cadence écrite dans un Markdown n’est pas la
preuve d’une tâche planifiée active. Aucune activation ni exécution de skill
ou d’agent n’a été faite ici.

| Mécanisme examiné | Destination | Écriture / risque d’écrasement |
|---|---|---|
| Hub : [registry-browser](../../../legal-builder-hub/skills/registry-browser/SKILL.md) | Registres de la watchlist ; défaut `github.com/legalopsconsulting/lpm-skills` | Cache `references/registry-cache.json` ; watchlist du profil sur confirmation. Aucun push vers les registres |
| Hub : [skill-installer](../../../legal-builder-hub/skills/skill-installer/SKILL.md) | Source communautaire choisie ; installation locale sous `~/.claude/skills/`, ou dans un plugin existant si proposé | Copies de fichiers, profil et `install-log.yaml` ; revue et accord prescrits. Pas de PR vers la source |
| Hub : [auto-updater](../../../legal-builder-hub/skills/auto-updater/SKILL.md) | Registre enregistré pour chaque skill installé par le hub | Remplacement des fichiers installés après diff, QA et accord humain ; sauvegarde `~/.claude/skills/.backups/[skill]-[old-sha]/`, mise à jour du SHA dans le profil ; rollback prévu |
| Hub : [registry-sync](../../../legal-builder-hub/agents/registry-sync.md) | Registres du profil ; notification Slack selon configuration, sinon restitution locale selon la documentation du hub | Annonce une cadence hebdomadaire ; texte contradictoire évoquant des mises à jour appliquées si auto-update activé |
| Hub : [skill-manager](../../../legal-builder-hub/skills/skill-manager/SKILL.md), wrappers `disable` / `uninstall` | Skills communautaires recensés dans `install-log.yaml` | Renommage ou suppression locale sur confirmation ; refuse les plugins internes ; aucun push |
| Installation/mise à jour du marketplace, [README](../../../README.md) et [QUICKSTART](../../../QUICKSTART.md) | Chemin du checkout ajouté manuellement ; sources relatives `./<plugin>` dans [.claude-plugin/marketplace.json](../../../.claude-plugin/marketplace.json) | Installation ou remplacement du paquet/cache ; aucune source GitHub de synchronisation automatique déclarée dans ce manifeste |
| `*/skills/cold-start-interview/SKILL.md` et modèles `*/CLAUDE.md` | `~/.claude/plugins/config/claude-for-legal/<plugin>/`, profil partagé `company-profile.md` | Écriture/migration de profils ; espace de noms encore commun avec l’original, à traiter dans BASE-004 |

L’auto-updater interdit explicitement le mode automatique, alors que son
argument-hint, son introduction, `registry-sync` et `customize` conservent
des formulations d’application automatique. Cette contradiction est un
risque dans des instructions interprétées ; les protections décrites ne
constituent pas un verrou logiciel. Elle n’active aucune mise à jour par Git.

### Autres agents livrés

Les dix définitions `*/agents/*.md` ont été examinées. Toutes leurs
destinations dépendent de profils et de connecteurs fournis par l’utilisateur.
La ligne `registry-sync` est détaillée ci-dessus ; les neuf autres sont :

| Agent (`<plugin>/agents/<nom>.md`, noté ci-dessous `plugin/nom.md`) | Entrées / destinations et écritures prévues |
|---|---|
| `commercial-legal/deal-debrief.md` | Dépôt de contrats connecté ; ajoute au `deviation-log.yaml` du profil |
| `commercial-legal/playbook-monitor.md` | Lit ce journal ; remplace `playbook-proposals.md`, écrit le journal de suivi et notifie ; modification du profil seulement après confirmation par changement |
| `commercial-legal/renewal-watcher.md` | Registre de renouvellements, éventuel rafraîchissement CLM, notification au canal du profil |
| `corporate-legal/dataroom-watcher.md` | VDR Box/Datasite/Intralinks ; statut de checklist et notification configurée |
| `employment-legal/leave-tracker.md` | `leave-register.yaml`, outils de recherche connectés, rapport/alertes ; précise qu’une planification nécessite une intégration séparée |
| `ip-legal/ip-renewal-watcher.md` | Registre PI, outils Anaqua/CPA/AltLegal déclarés et notification configurée |
| `litigation-legal/docket-watcher.md` | Trellis/CourtListener ; rapports `./out/docket-report-<date>.md`, `./out/deadlines.yaml`, notification configurée |
| `product-legal/launch-watcher.md` | Jira/Linear ; rapport et notification configurée |
| `regulatory-legal/reg-change-monitor.md` | Flux de la watchlist par WebFetch ; synthèse et notification configurée |

Les permissions génériques telles que `mcp__ironclad__*` sont larges : la
description d’une tâche de lecture ne garantit pas que ses outils ne puissent
pas écrire. Aucun de ces agents ne prescrit une synchronisation du dépôt
Git ou la création d’une PR vers son origine.

### Cinq cookbooks et leurs workers

Les cinq `agent.yaml` et les seize `subagents/*.yaml` présents ont été
examinés. Ils réutilisent les prompts/skills du checkout lors du déploiement.

| Cookbook | Sources externes déclarées / effet prévu |
|---|---|
| `reg-monitor` | Flux réglementaires de la watchlist via `web_fetch`, limité aux hôtes configurés dans `feed-reader.yaml` (Federal Register, SEC, GPO, Regulations.gov, Europa et Gov.uk), Google Drive déclaré ; digest et synthèse des écarts dans `./out/` |
| `renewal-watcher` | Ironclad, Google Drive, iManage, DocuSign déclarés ; lecteur MCP Ironclad/Drive activé, iManage désactivé ; alertes dans `./out/` |
| `diligence-grid` | Box, Google Drive, iManage, Definely déclarés ; lecteur Box/Drive activé, iManage désactivé ; grilles CSV et synthèse dans `./out/` |
| `launch-radar` | Linear, Atlassian, Asana, Google Drive déclarés ; lecteur MCP Linear/Atlassian/Asana ; note dans `./out/` |
| `docket-watcher` | Trellis, CourtListener, Google Drive déclarés ; lecteur MCP Trellis/CourtListener ; rapport et échéances dans `./out/` |

Les URL des serveurs sont des variables `${…_MCP_URL}`, non des destinations
effectives vérifiées. Les orchestrateurs accordent des outils locaux de
lecture ; les writers disposent de `write` et parfois `edit`. Certains
lecteurs accordent un `mcp_toolset` entier : des écritures distantes restent
possibles selon les outils exposés par ce serveur. Le code de relais
`orchestrate.py` peut aiguiller une demande de notification, mais ne fournit
pas à lui seul un serveur Slack ni une planification.

Les treize `.mcp.json` sont des déclarations HTTP vers des services tiers
(notamment Slack, Drive, CLM, VDR, outils de recherche et CoCounsel), sans
serveur GitHub déclaré. Les dix `hooks/hooks.json` présents contiennent tous
`{"hooks": {}}` ; aucun hook de plugin n’y exécute de commande. Ces hooks
de plugins sont distincts des hooks Git de `.git/hooks/`.

## 5. Adaptations locales à protéger

| Opération future | Ce qui peut être remplacé | Précaution proposée |
|---|---|---|
| `auto-updater --apply` / rollback | Tout fichier du skill communautaire installé, y compris une adaptation locale ; le rollback restaure une sauvegarde antérieure | Comparer à la version installée réelle, sauvegarder les adaptations et relire le diff avant application |
| Mise à jour/réinstallation d’un plugin | Contenu du paquet et modèles `CLAUDE.md` dans le cache | Conserver les adaptations dans le fork versionné ; séparer identité du marketplace et chemins de profils via BASE-004 |
| Configuration du fork sous le nom hérité | Profil partagé, profils par domaine ou migration depuis un ancien cache | Décider les nouveaux chemins et une migration sans écrasement dans BASE-004 ; ne pas supposer l’isolation actuelle |
| Copie d’une nouvelle version amont, fusion/rebase ou remplacement de dossiers | Fichiers adaptés dans le checkout ; pertes possibles en cas de remplacement forcé | Revue d’un diff sur une branche dédiée. Aucun script de ce type trouvé ; aucun remote amont configuré |
| Nouvelle exécution d’agents | Propositions commerciales remplacées explicitement, rapports et registres générés | Séparer contenus générés et adaptations, conserver leur historique utile |
| Redéploiement d’un cookbook | Réexporte les skills/prompts du checkout vers l’API ; le script crée de nouveaux agents, sans mettre à jour automatiquement les anciens | Relire les payloads en dry-run et gérer explicitement les IDs déployés |

## 6. Corrections minimales proposées, non appliquées

1. **CLA du fork :** retirer le workflow hérité et adapter les sections de
   contribution pour viser explicitement des PR vers `Francois-Louis/Judge`,
   sans exiger automatiquement une signature au bénéfice d’Anthropic.
   Conserver `CLA.md` comme document historique identifié et préserver les
   attributions/licences. Proposition bornée dans
   [BASE-007](../base-007-cla-contributions-fork.md), au statut `proposee`.
   Un éventuel CLA propre au fork serait une décision séparée.
2. **Mises à jour du hub :** dans le découpage d’
   [EXIST-011](../../02-plugins-existants/exist-011-gestion-des-skills.md), prévoir
   une tâche qui aligne `registry-sync`, `customize` et les formulations
   résiduelles d’`auto-updater` sur la revue et l’accord par mise à jour.
3. **Isolation des adaptations :** laisser les changements de noms, de
   manifestes et de chemins à [BASE-004](../base-004-identite-configurations-mises-a-jour.md).
   La destination de push actuelle ne justifie aucune modification Git.

## 7. Vérifications et reproduction

Commandes de lecture effectivement utilisées, à relancer depuis la racine :

```powershell
git status --short
git --version
git rev-parse HEAD
git branch --show-current
git remote -v
git remote get-url --all origin
git remote get-url --push --all origin
git config --show-origin --show-scope --get-regexp '^(remote\..*\.(url|pushurl|push|fetch|mirror|receivepack|uploadpack|proxy)|branch\..*\.(remote|merge|pushremote)|remote\.pushdefault|push\..*|url\..*\.(insteadof|pushinsteadof)|core\.(hookspath|sshcommand)|ssh\.variant|include.*|alias\.(push|p))$'
git for-each-ref '--format=%(refname:short) -> %(upstream:short) [%(upstream:track)]' refs/heads
git rev-parse --git-dir
python -X utf8 scripts/lint-tool-scope.py
```

La sélection de configuration ne lit pas les jetons/credentials ; les URL
ont en outre été filtrées avant affichage pour masquer d’éventuels identifiants
ou paramètres sensibles. Ne pas publier une sortie brute d’une autre machine.
Les hooks, remotes historiques, noms des variables de transport, fichiers de
workflow, scripts, JSON de hooks/MCP et manifestes ont aussi été inventoriés
directement avec PowerShell/Python et `rg`.

Résultats : lint réussi pour les cinq orchestrateurs ; cohérence des liens
locaux et des statuts du backlog contrôlée après rédaction. Pas de test
nécessitant une clé API, pas de déploiement, pas d’installation ni de commande
`git push`, même en dry-run. Les réglages GitHub et les destinations privées
des connecteurs restent expressément hors de la preuve locale.
