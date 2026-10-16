# EXIST-001 — Inventaire du plugin commercial

Relevé du **16 octobre 2026**, sur les fichiers du checkout. Il décrit du
contenu hérité à adapter, pas des fonctionnalités France/UE validées.
Les [empreintes et contrôles](exist-001-resultats.json) donnent la liste exacte
des fichiers. Le [découpage COM](exist-001-decoupage-commercial.md) attribue les
travaux ; la [vérification documentaire](exist-001-verification.md) en éprouve
les frontières sur des pièces fictives.

## Dépendances communes

Les 12 skills et les 3 agents demandent d'abord
`commercial-legal/references/isolation.md`, puis le helper embarqué
`scripts/judge_store.py` pour les données durables. Le profil effectif est
`config/judge-fr-eu/commercial-legal/CLAUDE.md`, hors du paquet ; le
`commercial-legal/CLAUDE.md` du dépôt est seulement son modèle. Le profil
commun `company-profile.md` porte les faits partagés du fork.

Selon la tâche, s'ajoutent le playbook vente/achat, les préférences de revue,
la matrice d'approbation, le rôle, le style, les destinations et le dossier
actif (`matter.md`, `history.md`, `notes.md`, `outputs/`). Ces fichiers ne sont
pas des références juridiques. Une position « ne jamais accepter » reste une
préférence de négociation ; elle ne prouve pas l'illicéité d'une clause.

La méthode BASE-005 `1.0.0` est déjà embarquée dans
`references/shared/research-citation-method.md`, identique à la source racine.
Les workflows hérités ne la chargent pas explicitement. Chaque future tranche
doit la charger et résoudre ses contradictions avec les consignes héritées.
Les références métier nouvelles resteront dans le paquet commercial, sans
installation obligatoire d'un autre domaine.

## Les 12 skills, corps et appels suivis

Les noms techniques sont conservés pour éviter de casser les commandes.
« Réécrire » vise le raisonnement et les sorties ; « retirer » vise les
comportements indiqués, sans suppression du fichier dans ce cadrage.

| Skill sous `commercial-legal/skills/` | Contenu et dépendances particulières | Décision justifiée et suite |
|---|---|---|
| `review/SKILL.md` | Profil, `confirm_routing`, documents et titres d'annexes → `vendor-agreement-review`, `nda-review`, surcouche `saas-msa-review` ; DPA seulement signalé ; puis `escalation-flagger`, résumé, registre, CLM, redline. | Conserver le routage, réécrire la qualification par objet réel, parties et dates ; les titres et mots anglais ne suffisent pas. Séparer B2B/B2C/secteur, annoncer les branches non adaptées. COM-001. |
| `vendor-agreement-review/SKILL.md` | Playbook achat/vente, dossier, valeur de commande, DPA incorporé par URL ; plafond en quatre dimensions, « jurisdiction delta », écarts, redlines, matrice ; CLM, DocuSign, production DOCX supposée. | Conserver clause/pièce/proposition ; réécrire pour une prestation B2B française, dont responsabilité, résiliation, cession, preuve, imprévision et déséquilibre. Retirer le provisoire US, les seuils USD et la déduction juridique à partir des seuls fallbacks. Présentation française « revue d'un contrat de prestation », nom technique inchangé. COM-002. |
| `nda-review/SKILL.md` | Profil → positions NDA du côté choisi, preuve de relecture par avocat, `closing_action`, dossier ; portée réelle au-delà du NDA, tri GREEN/YELLOW/RED, clauses résiduelles, durées et archivage ; CLM. | Conserver le tri court, le questionnaire unilatéral et le contrôle des obligations cachées ; réécrire confidentialité commerciale France/UE, parties divulgatrice/réceptrice, exceptions et secret des affaires à rechercher. Retirer l'équivalence GREEN/signature autorisée. COM-003. |
| `saas-msa-review/SKILL.md` | Appelle toute la revue générale ; positions SaaS et IA ; bon de commande, SLA, DPA/politiques et sous-traitants ; prix, sortie de données, dépréciation ; transmet au registre une structure plus pauvre que celle du tracker. | Conserver la surcouche, réécrire SaaS B2B transfrontalier, versions incorporées, réversibilité et données selon les champs réels. Retirer les raccourcis CA/NY/UK/HIPAA/FTC comme fondement France/UE ; aucune application automatique du droit consommateur. COM-004, avec schéma COM-006. |
| `amendment-history/SKILL.md` | Base et avenants fournis ; deux modes (historique / trace d'une clause), dates, parties et renumérotations ; propose revue/résumé. Intégrations CLM/dépôt explicitement « coming soon ». | Conserver les deux vues d'une même chaîne documentaire ; réécrire signature/prise d'effet/hiérarchie/preuve, retirer l'ordre déduit du nom de fichier comme preuve et la certitude « current controlling language » en cas de conflit. COM-005. Aucun connecteur futur présenté comme disponible. |
| `renewal-tracker/SKILL.md` | Registre durable et modèle YAML local ; modes ingestion, rapport, scan CLM/DocuSign, fenêtres dépassées ; calculs calendaires/ouvrés, marges de transport, reconduction ; dashboard et agent watcher. | Conserver ingestion et suivi, les séparer en COM-006/007. Retirer jours fériés US de remplacement, recul automatique au vendredi et marges 5/10 jours prises pour règles ; ne pas déduire reconduction ou absence de notification du registre seul. |
| `escalation-flagger/SKILL.md` | Matrice, valeur/devise, côté du playbook, constat et date ; rédaction d'une demande, puis instruction de la consigner comme envoyée. | Conserver destinataire et brouillon ; réécrire pour une TPE sans GC aussi bien qu'une équipe. Retirer les seuils d'exemple comme autorité et « envoyé » sans preuve. COM-008. |
| `stakeholder-summary/SKILL.md` | Mémo amont, rôle, côté, style et dossier ; <200 mots, exceptions conditionnelles, contrôle d'une sortie tracker ; rapproche les approbateurs avec les fichiers `escalation-*.md`. | Conserver langage accessible et reprise des réserves ; réécrire pour artisan/indépendant aussi. Retirer brouillon = routage effectué, sortie tracker = preuve d'inscription, et résumé = feu vert de signature. COM-009. |
| `cold-start-interview/SKILL.md` | Modèle de profil et company-profile local ; quick/full, pause/reprise, `--side`, `--redo`, `--check-integrations`, exemples signés, matrice ; écrit profils/préférences, propose scan et débrief. | Conserver personnalisation volontaire ; réécrire l'entrée pour non-juriste sans playbook ni 5–10 contrats. Retirer defaults juridiques US et fausse déduction du périmètre d'installation depuis le cwd, déjà contredits par la frontière BASE-008. COM-013 ; ajustements minimaux d'accès sans profil dans chaque tranche. |
| `customize/SKILL.md` | Profils partagé et commercial, carte des sections, confirmation d'édition et effets aval. | Conserver modification ciblée ; réécrire préférences déclarées versus règles sourcées, pas de réduction des vérifications par simple changement d'appétit pour le risque. COM-013. |
| `matter-workspace/SKILL.md` | Profil → activation, dossier actif et droit de lecture croisée ; `new/list/switch/close/none`, modèles matière/historique ; archivage sans suppression. | Conserver séparation et historique ; réécrire champs France/UE, rôles, dates et accès via helper. Pas de contrôle de conflits ou de conservation prétendument exécuté. COM-014. |
| `review-proposals/SKILL.md` | Charge l'étape 5 de `agents/playbook-monitor.md`, lit `playbook-proposals.md`, décisions accepter/rejeter/éditer/différer, diff et archivage. | Conserver arbitrage explicite ; réécrire avec contrôle de version, propositions différées préservées et aucune règle de droit modifiée par vote. Retirer « playbook à jour » déduit d'un fichier absent. COM-012. |

## Agents et chaînes indirectes

| Fichier sous `commercial-legal/agents/` | Dépendances et défauts constatés | Décision et suite |
|---|---|---|
| `renewal-watcher.md` | Profil/destination → tracker mode 2 ; mode 3 si synchro >30 jours ; outils Read/Write/Ironclad/Slack. Dit ne pas modifier le registre alors que le mode 3 le peuple ; calendrier annoncé sans ordonnanceur fourni. | Réécrire en génération d'un rapport à partir du registre vérifié, politique d'import distincte, preuve de couverture. Conserver alerte urgente, retirer publication implicite et promesse de surveillance active. COM-007. |
| `deal-debrief.md` | Profil/dépôt → accords « signés » sur 7 jours → `deviation-log.yaml` ; raisons et exceptions `exclude_from_patterns`, dédoublonnage par `deal_id` ; outils MCP génériques. | Conserver capture du contexte, réécrire preuve de signature et version du playbook. Date de modification/nom « executed » ne certifient pas la signature. Réduire les permissions aux accès utiles ; sortie locale sans diffusion implicite. COM-010. |
| `playbook-monitor.md` | Profil + journal → filtre 12 mois/5 écarts et exceptions → propositions, notification, `playbook-monitor-log.yaml` → revue → archive. | Conserver détection proposée comme convention interne, réécrire séparation vente/achat/droit/date, historique et décisions. Retirer écrasement des propositions non traitées, conclusions juridiques tirées de fréquence et notification automatique. COM-011 (production), COM-012 (décision). |

Chaînes de contrôle suivies dans les corps :

- `review` → revue générale → DPA incorporé et éventuel renvoi privacy ;
  `saas-msa-review` → revue générale → handoff YAML → tracker → watcher.
- `renewal-tracker` emploie tantôt `send_by_effective`, tantôt
  `cancel_by_effective` pour l'urgence ; son calcul mentionne encore
  `initial_term_end` malgré l'instruction d'utiliser `current_term_end`.
  `--days` et `--horizon` sont incohérents ; le modèle contient seulement
  `cancel_by`. COM-006 fixe les champs, COM-007 leurs usages et bornes.
- `stakeholder-summary` → fichiers d'escalade → `escalation-flagger` :
  un fichier brouillon ne prouve ni transmission ni approbation. COM-008
  établit les états, COM-009 les conserve.
- `review-proposals` → étape 5 du monitor → profil durable : une proposition
  différée doit survivre à l'archivage et au prochain passage. COM-011/012.

## Autres fichiers embarqués — couverture complète

Outre les 12 skills et 3 agents, les 15 fichiers suivants complètent les
**30 fichiers** du paquet. Les références citées ci-dessous existent ; les
références métier envisagées dans les suites sont encore à créer.

| Fichier sous `commercial-legal/` | Décision et justification |
|---|---|
| `CLAUDE.md` | Réécrire progressivement les seuls blocs utilisés : exemples US, blocage setup/provisoire contradictoire, secret présumé, capacité des sorties et règles de sources. COM-013 porte le profil complet ; chaque COM corrige ses blocs sans l'attendre. |
| `references/company-profile-template.md` | Conserver comme scaffold ; utiliser sans exiger une équipe juridique, sans convertir exemples de pays/régulateurs en faits. Si modification nécessaire, traiter la synchronisation des copies dans une story transverse, pas une divergence locale silencieuse. COM-013. |
| `references/dashboard-template.md` | Conserver rendu autonome et protections HTML/tableur ; l'affichage ne valide pas les dates. COM-007/009 ; aucune refonte visuelle requise. |
| `references/shared/research-citation-method.md` | Conserver à l'identique, version `1.0.0`, charger depuis les entrées adaptées ; pas de corpus commercial à y ajouter. Toutes les suites. |
| `references/isolation.md` | Conserver frontière BASE-008 et contrat du helper ; pas de copie utilisateur dans le paquet. Toutes les suites. |
| `scripts/judge_store.py` | Conserver helper commun (Python ≥3.12), refus de liens/chemins hors racine et remplacement par digest. Pas de réécriture technique dans EXIST-001. Toute évolution relève d'un lot transverse avec copies synchronisées. |
| `skills/renewal-tracker/references/renewal-register.yaml` | Réécrire modèle et version de schéma, provenance, notification et statut de calcul ; migrer sans écraser le registre réel. COM-006. |
| `.claude-plugin/plugin.json` | Conserver identité/version `0.1.0` dans ce cadrage ; chaque tranche devra annoncer exactement son périmètre adapté et synchroniser marketplace. |
| `.mcp.json` | Conserver comme inventaire de configurations, pas preuve de connexion. Sept serveurs : Ironclad, DocuSign, iManage, TopCounsel, Definely, Slack, Google Drive. Clarifier usages facultatifs et permissions par lot. |
| `hooks/hooks.json` | Conserver stub `hooks: {}` ; aucun déclencheur ou scheduler actif à en déduire. |
| `README.md` | Réécrire par tranche : public TPE, état réel, 12 skills (table incomplète), sept connecteurs (liste incomplète), sources officielles sans abonnement obligatoire, limites des NDA et du suivi. Aucun changement ici. |
| `LICENSE` | Conserver licence Apache-2.0, aucune modification attendue. |
| `NOTICE` | Conserver attributions ; ajouter une entrée datée pour chaque future modification du paquet et mettre à jour le NOTICE racine selon les consignes. Aucun ajout pour les seuls fichiers backlog. |
| `.gitignore` | Conserver `.DS_Store` ; sans effet sur l'analyse juridique, pas d'uniformisation. |
| `logs/.gitkeep` | Conserver marqueur vide ; il n'autorise pas de journal durable dans le paquet remplaçable. |

## Dépendances hors paquet et accès externes

| Élément | Usage, frontière et suite |
|---|---|
| `.claude-plugin/marketplace.json`, `README.md`, `QUICKSTART.md` racine | Index et installation à synchroniser lors d'une livraison ; pas des fichiers nécessaires à l'exécution d'un plugin détaché. |
| `references/research-citation-method.md`, `references/isolation.md`, `scripts/judge_store.py` racine | Sources d'édition des copies embarquées, jamais des chemins de repli à l'exécution. Copies comparées dans les contrôles. |
| BASE-003, BASE-005, BASE-006, BASE-008, accès officiel BASE-010 ; protocole USAGE-001 | Architecture, preuve, isolation et orientation à appliquer par les futures tranches ; documents du backlog, sans chargement obligatoire depuis le client. |
| `managed-agent-cookbooks/renewal-watcher/agent.yaml` | Charge l'agent commercial et le plugin ; headless/handoff. Adaptation distante séparée COM-018, après COM-007/008/009, sans déploiement dans cette story. |
| `managed-agent-cookbooks/renewal-watcher/subagents/repo-reader.yaml` | Métadonnées et clauses → schéma JSON ; devise USD, noms ASCII et URL Ironclad malgré Drive ; droits MCP larges déclarés « read-only ». Réécrire schéma et permissions réelles en COM-018. |
| `managed-agent-cookbooks/renewal-watcher/subagents/deadline-calculator.yaml` | Autres bandes 30/60/90/180, jour 0 non classé explicitement, date la plus proche sans qualification du déclencheur. Harmoniser COM-018 avec COM-006/007. |
| `managed-agent-cookbooks/renewal-watcher/subagents/alert-writer.yaml` | Charge tracker/escalade/résumé ; rapport, protection injection et handoff Slack. Conserver protection, retirer secret présumé et harmoniser états/bandes en COM-018. |
| `managed-agent-cookbooks/renewal-watcher/README.md` | Schéma de permissions et promesse de handoff à comparer aux capacités effectives, sortie en panne et limites de couverture ; COM-018. |
| `managed-agent-cookbooks/renewal-watcher/steering-examples.json` | Scans généraux/ciblés et contrôle post-signature ; borner au suivi adapté et conserver date de référence explicite ; COM-018. |
| `scripts/orchestrate.py`, `scripts/deploy-managed-agent.sh`, `scripts/cookbook_paths.py`, `scripts/lint-tool-scope.py`, `scripts/test-cookbooks.sh`, `scripts/validate.py` | Infrastructure citée par le cookbook, pas moteur de calcul commercial. Réutiliser ses contrôles en COM-018 ; toute correction transverse révélée aura un périmètre propre. Pas d'exécution distante ici. |
| `privacy-legal:dpa-review`, `ip-legal:ip-clause-review`, gouvernance IA | Expertises complémentaires proposées, encore à adapter ; jamais supposées installées ou France/UE validées. Conserver dans commercial les constats nécessaires à son résultat et fournir les questions/pièces de relais. |
| CLM, DocuSign, dépôts, messagerie, Definely, TopCounsel ; outils DOCX/Excel et recherche cités | Facultatifs, à tester avant affirmation de capacité. CourtListener/Westlaw/SharePoint/Box cités dans la prose ne sont pas tous déclarés dans `.mcp.json`. Contrats fournis et rapport local restent un parcours utile ; aucun accès, envoi ou test de compte réalisé par l'inventaire. |

## Besoins sans skill actuel et retraits retenus

COM-015 propose une tâche de pièces/solde d'une facture B2B impayée,
COM-016 une comparaison de frais ou pénalités facturés aux clauses fournies,
COM-017 une préparation documentaire avant rupture d'une relation B2B.
Ces créations ne sont ni des commandes existantes ni une extension automatique
du recouvrement judiciaire. Leur sélection reste à faire.

Aucun skill complet n'est retiré ou renommé : chacun conserve un résultat
utile identifiable. Les retraits individuels ci-dessus concernent les
présomptions US, preuves fictives d'action, automatisations annoncées sans
support et déductions du playbook prises pour du droit. Tout changement futur
de nom de commande demandera sa compatibilité et ses liens dans le lot choisi.
