# EXIST-002 — Inventaire sociétés et opérations

Relevé du **16 octobre 2026** sur le checkout. L'[état machine](exist-002-resultats.json)
énumère et empreinte les **30 fichiers du plugin**, dont **13 skills et un
agent**, et les sept fichiers du cookbook associé. L'inventaire porte sur du
contenu hérité à adapter. Le [découpage SOC](exist-002-decoupage-societes.md)
attribue chaque tâche ; la [relecture documentaire](exist-002-verification.md)
compare les situations SAS, SARL et acquisition avec filiale étrangère.

## Contrat et dépendances communes

Les 13 skills et l'agent chargent `references/isolation.md` avant l'accès
durable. Le helper embarqué `scripts/judge_store.py` porte les opérations
sous `~/.claude/plugins/config/judge-fr-eu/corporate-legal/`. Le profil
effectif est son `CLAUDE.md` ; celui du paquet est un modèle, pas le contexte
utilisateur. Le seul profil partagé est `../company-profile.md` dans la
racine de configuration du fork.

Les modèles d'actes, statuts et pactes fournis, organigrammes, délégations,
seuils de revue, listes de demandes et préférences de format sont des pièces
ou conventions de travail. Ils ne constituent pas une règle de droit. Les
seuils de matérialité ne déterminent ni compétence d'un organe, ni obligation
de formalité. Les pièces de chaque société doivent être identifiées et datées.

La méthode BASE-005 `1.0.0` est embarquée dans
`references/shared/research-citation-method.md`, mais les entrées héritées
ne la chargent pas explicitement. Chaque tranche adaptée devra la charger,
résoudre les contradictions avec ses anciens garde-fous et rester utilisable
dans un paquet détaché. Le chargement d'un profil ne remplace pas la
qualification de l'acte et de la société.

## Les 13 skills — décision par tâche

Noms techniques conservés pour les commandes existantes. Les intitulés
français ci-dessous décrivent les résultats proposés ; aucun renommage
technique ni retrait de fichier n'est réalisé.

| Fichier sous `corporate-legal/skills/` | Corps, appels et données suivis | Décision motivée et porteur |
|---|---|---|
| `written-consent/SKILL.md` | Profil Board & Secretary, précédent/répertoire, action routine/exceptionnelle, signataires, conflits, contrôle de droit étatique placé après la rédaction, présomption d'unanimité et délégation générale. Ne suit pas les signatures reçues. | Conserver recherche de forme et liste de pièces ; réécrire d'abord compétence/modalité SAS ou SARL (SOC-001), puis un projet borné d'autorisation bancaire (SOC-002). Retirer consentement unanime du board comme voie par défaut, ratification générale et validité de signature électronique présumée. Un ancien acte n'établit pas la procédure actuelle. |
| `board-minutes/SKILL.md` | Calendrier ±30/14 jours, agenda/slides, présence réelle, quorum, votes, annexes, modèle antérieur ; renvoi à written-consent. | Conserver traçabilité et lacunes visibles ; réécrire PV d'une décision sociale française après SOC-001 (SOC-003). Retirer présences/votes déduits d'une invitation ou présentation et « motion seconded / waiver » importés. Présentation française « projet de procès-verbal » ; pas de finalisation automatique. |
| `entity-compliance/SKILL.md` | Cinq modes et sous-modes init/rebuild, report, update/from-report/sweep, audit, export ; schéma YAML inline, custom_jurisdictions, registered agent, good standing. Le texte évoque une table de référence non livrée, puis interdit son emploi en init. | Conserver inventaire et provenance ; séparer initialisation de formalités identifiées (SOC-004), preuves/mise à jour (SOC-005), rapport/export (SOC-006), audit de pièces (SOC-007). Retirer calendrier Delaware et franchise tax comme défaut France, application d'une définition à toutes les entités d'un pays, « current » déduit d'un dépôt, dissolution préconisée à cinq ans. Immatriculation, dépôt, réception et validation ont des états distincts. |
| `tabular-review/SKILL.md` | Profil, deal-context, .review-schema.yaml ; échantillon puis extraction par document, sept types, quatre états, quote/location, relecture des citations, CSV/sources, Excel/Sheets et liens vers trois références locales. Alimente issues/schedule/handoff. | Conserver grille typée, citations exactes et traçabilité par cellule ; réécrire schéma France/étranger, versions/chaînes d'avenants, unités/devises, inconnues et couverture (SOC-008). Retirer silence = permission et toute certification juridique par cellule « answered » ; garder preuves brutes distinctes du texte neutralisé pour tableur. |
| `diligence-issue-extraction/SKILL.md` | Profil + deal-context → inventaire VDR → filtre → constats par catégorie → mémo, puis summary/schedule/checklist. Handoff IA avant lecture dans une entrée, alors que ai-tool-handoff propose grille native d'abord. Modèles §280G/HSR/CFIUS et successor liability US. | Conserver constat/pièce/conséquence/question ; réécrire revue documentaire bornée sociétés/contrats d'une acquisition de titres (SOC-009). Retirer références US comme fondement français, seuil financier qui masque pièce essentielle et obligation de recherche payante ; questions PI/travail/fiscalité restent des relais explicites. |
| `material-contract-schedule/SKILL.md` | Définition et format du PA → findings/grille → inclusion par branche de définition → annexe et overlay interne d'accords → checklist. | Conserver annexe contractuelle et critères exacts (SOC-010) ; réécrire source/version, périmètre lu, exclusions et cas inconnus. Retirer équivalence entre définition négociée et liste légale française, exhaustivité proclamée sans corpus complet, et secret hérité automatiquement. |
| `closing-checklist/SKILL.md` | deal/closing-checklist.yaml inline ; init depuis PA, ingestion de trois amonts, mise à jour et rapport/chemin critique ; dédoublonnage counterparty+action ; champ blocking et exemples US. | Conserver conditions/livrables et renvois ; scinder construction sourcée (SOC-011) et rapprochement/rapport (SOC-012). Retirer checklist complète = opération autorisée ou réalisée, criticité déduite d'une durée estimée, et CP déclarée satisfaite sans preuve/version. Le tiers et l'action seuls ne suffisent pas à fusionner deux contrats. |
| `deal-team-summary/SKILL.md` | Profil/cadence, deal-context, constats accumulés, trois publics, évolutions de gravité, couverture, décisions → checklist. | Conserver synthèse par destinataire, réécrire réserves/couverture/statut exact et langage accessible pour dirigeant de TPE (SOC-013). Retirer protection automatique par privilège et résolution d'un point par simple résumé ; pas d'envoi implicite. |
| `integration-management/SKILL.md` | deal-context + closing-checklist → integration-tracker.yaml inline ; init, import contrats, report, update, export. J1 cible +7 jours ; PA dates dont garanties/séquestre/earn-out ; accords required/desired ; classement auto-assign/CoC. | Conserver suivi avec provenance ; séparer plan initial (SOC-014), mécanismes contractuels et accords (SOC-015), mises à jour/rapport (SOC-016). Retirer phases 1/30/90/180 prises pour délais, silence ou achat de titres = cession automatique, CoC systématiquement déclenché, et renvoi à written-consent pour lettre à un cocontractant. |
| `ai-tool-handoff/SKILL.md` | Profil/trust level, inventaire, lot >50, instructions de chargement Luminance/Kira, QA sur seuls documents signalés, sortie → constats/checklist ; ne pilote pas les outils annoncés. | Conserver préparation et contrôle d'un export fourni, réécrire couverture avec négatifs et échantillon explicite (SOC-017). Retirer « use as-is » comme preuve juridique et absence de ligne = absence de clause. Pas d'export réel ou licence requis ; harmoniser ordre grille/handoff avec SOC-009. |
| `cold-start-interview/SKILL.md` | Quick/full, pause/reprise, redo/module/check-integrations/new-deal ; écrit profil partagé/domaine et contexte deal ; modèles M&A, Board, Public, Entities ; seeds et defaults. | Conserver préférences volontaires et accès testé, réécrire pour associé/dirigeant sans GC et société sans board (SOC-019). Isoler new-deal en SOC-020. Retirer defaults US, blocage d'une lecture ponctuelle faute de seeds, faux périmètre installé depuis cwd ; le bloc BASE-008 final prévaut déjà sur les vieux defaults. |
| `customize/SKILL.md` | Carte des modules et changements ciblés du profil/partagé ; exemples seuil monétaire → annexe, niveau confiance IA et Public Company. | Conserver édition ciblée, réécrire séparation préférences/droit et revue de version (SOC-019). Retirer seuil interne qui remplace définition du contrat, tolérance au risque qui dispense d'une source, activation Public Company promettant fonctionnalité absente. |
| `matter-workspace/SKILL.md` | new/list/switch/close/none, actif dans profil ; matter.md/history.md/notes.md/outputs ; exemple commercial copié, croisement on/off et archivage. | Conserver séparation/archivage via helper (SOC-021), réécrire modèles sociétés/opérations et liaison avec deals. Retirer désactivation automatique pour in-house multi-entités et accès croisé implicite. Conflits/conservation non prétendus exécutés. |

## Agent et chaînes indirectes

| Fichier sous `corporate-legal/` | Décision et justification |
|---|---|
| `agents/dataroom-watcher.md` | Conserver comparaison d'inventaires et rapport local ; réécrire pointeur de reprise, changements de version, périmètre accessible, distinction ajout/lecture et cadence réellement activée (SOC-018). Retirer post Slack automatique et autorisations génériques comme preuve d'accès lecture seule. Contradiction : dit Slack non livré alors que .mcp.json le déclare ; README dit hebdomadaire, corps quotidien ; aucun scheduler dans hooks. Ne modifie pas la checklist malgré la mention de mise à jour par watcher dans closing-checklist. |

Chaînes à corriger dans leurs lots :

- gouvernance : statuts/pactes/délégations → SOC-001 → SOC-002 ou SOC-003.
  Accord d'un associé, vote d'un organe et autorisation d'un tiers sont distincts ;
  ni « consent » ni société française ne désignent une procédure unique.
- grille → constats → annexe/synthèse → checklist → suivi post-acquisition.
  Préserver id, entité, contrat, version, citation, gravité motivée, condition,
  garant, préavis et réserve ; garder brouillon/proposé/inscrit/exécuté distincts.
  Les schémas inline actuels divergent et ne constituent pas encore un contrat
  de données versionné.
- matière active sous matters versus fichiers deals/[code] : chemin ambigu
  susceptible de mélanger deux dossiers. SOC-020/021 définissent le lien ;
  chaque tranche corrige son routage sans attendre un profil complet.
- grille native versus export IA : la taille et la préférence d'outil
  n'établissent pas une couverture. SOC-008/009/017 ne suppriment pas les
  lignes non signalées, documents illisibles ou pièces exclues par seuil.

## Les 16 autres fichiers du paquet

Avec les 13 skills et l'agent, ces 16 chemins couvrent les 30 fichiers, y
compris les fichiers cachés.

| Fichier sous `corporate-legal/` | Décision et justification |
|---|---|
| `CLAUDE.md` | Réécrire progressivement blocs setup/sources/secret/routage/modules (SOC-019/020/021 et tranche concernée). Le module Public Company n'a aucun skill livré : retirer promesses SEC, §16/Form 4, 10-K/10-Q comme France/UE ou simple futur activable ; laisser statut explicite hors périmètre, sans créer un domaine coté. |
| `references/company-profile-template.md` | Conserver scaffold partagé ; exemples de régulateurs ne sont pas faits. SOC-019 ; toute modification du commun exige synchronisation transverse des copies. |
| `references/dashboard-template.md` | Conserver rendu autonome et protection HTML ; SOC-006/012/013/016 ; aucune refonte, aucune date certifiée par un graphique. |
| `references/isolation.md` | Conserver frontière et copies identiques, toutes tranches. Pas d'import d'un profil d'origine ou cache. |
| `references/shared/research-citation-method.md` | Conserver identique à la racine, version 1.0.0 ; chargement local par toutes les entrées adaptées, pas de corpus sociétés dans le commun. |
| `scripts/judge_store.py` | Conserver helper commun, contrôles de chemins et digest de remplacement ; pas de changement technique dans EXIST-002. Évolution éventuelle dans lot transverse avec copies synchronisées. |
| `skills/tabular-review/references/ma-diligence-columns.md` | Réécrire individuellement les 21 colonnes et les ajouts sectoriels (SOC-008) : document/entité/versions, cession distincte du contrôle, assurances sans workers_comp automatique, devise, indemnisation réelle. Retirer BAA/FDA/FAR/DFARS/FINRA/SEC par défaut et promesse « six colonnes = 80 % ». Droits étrangers dans bloc identifié. |
| `skills/tabular-review/references/excel-output.md` | Conserver feuilles Review/Flags/_schema/_summary, sources masquées et Verified vide ; clarifier état, preuve exacte versus neutralisation de formule et échec d'outil (SOC-008). Une coche ne vérifie pas le droit à elle seule. |
| `skills/tabular-review/references/gsheets-output.md` | Conserver mêmes données et repli CSV ; réécrire capacités réellement disponibles, partage restreint, sources conservées à l'export et absence de privilège automatique (SOC-008). Aucun compte cloud requis pour résultat local. |
| `.claude-plugin/plugin.json` | Conserver identité judge-fr-eu-corporate-legal/version 0.1.0 ici. Chaque livraison future décrit seulement les tâches adaptées et synchronise marketplace. |
| `.mcp.json` | Sept serveurs déclarés : Slack, Google Drive, Box, iManage, TopCounsel, Definely, Solve Intelligence. Conserver comme configuration, vérifier capacités par lot ; ni preuve d'authentification ni calendrier. Intralinks/Datasite, recherche juridique et Sheets cités ailleurs ne sont pas tous déclarés. |
| `hooks/hooks.json` | Conserver stub hooks vide ; pas de surveillance active ou planning à en déduire. |
| `README.md` | Réécrire par tranche état/public, liste des 13 skills (customize absent), connecteurs, cadence et recherche officielle facultative sans abonnement ; corriger promesses Public Company. SOC-019 porte la présentation générale. |
| `LICENSE` | Conserver Apache-2.0 et attributions, aucune modification prévue. |
| `NOTICE` | Conserver ; une entrée datée dans NOTICE du plugin et racine pour chaque lot qui touche au paquet. Cadrage sous backlog uniquement : pas d'entrée requise. |
| `.gitignore` | Conserver .DS_Store, aucune uniformisation liée à l'adaptation. |

## Dépendances hors paquet

| Élément | Contenu suivi et décision |
|---|---|
| `managed-agent-cookbooks/diligence-grid/agent.yaml` | Charge corporate-legal et tabular-review, modes watch/grid, quatre workers, sorties et handoff Slack ; conserver séparation des pouvoirs, adapter schéma/provenance/qualification et quatre états en SOC-022. « three-state » en annonce contredit les quatre valeurs. |
| `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml` | Lecture MCP, preview, id/parties/URL ; noms ASCII excluent accents et URL autorisées excluent Drive pourtant activé. Réécrire métadonnées France/étranger et permissions réelles en SOC-022. |
| `managed-agent-cookbooks/diligence-grid/subagents/extractor.yaml` | Quote/location facultatifs dans output_schema malgré promesse de preuve ; limites de taille, valeurs structurées, pas d'empreinte source. SOC-022 doit préserver les états et rejeter une preuve tronquée sans la reconstruire. |
| `managed-agent-cookbooks/diligence-grid/subagents/normalizer.yaml` | Ne peut relire source, contrairement à la vérification caractère par caractère de tabular-review ; simple suspicion de paraphrase insuffisante. SOC-022 définit un retour au lecteur et un état non vérifié jusqu'au rapprochement. |
| `managed-agent-cookbooks/diligence-grid/subagents/grid-writer.yaml` | Seul Write, CSV + sources + summary, protection formule ; annonce flags que la sortie ne spécifie pas clairement. SOC-022 conserve preuve brute séparée de son rendu, schéma/états et flags exportés ; pas de fichier xlsx promis. |
| `managed-agent-cookbooks/diligence-grid/README.md` | SOC-022 corrige tableau des droits (« read-only » alors que toolsets MCP génériques sont activés), Definely annoncé au normalizer sans outil, autonomie et portée de la preuve ; ni publication ni secret automatique. |
| `managed-agent-cookbooks/diligence-grid/steering-examples.json` | SOC-022 réécrit trois exemples : grille, inventaire depuis cutoff, reprise ciblée avec schéma/version et conservation des lignes non touchées. |
| `scripts/orchestrate.py`, `scripts/deploy-managed-agent.sh`, `scripts/cookbook_paths.py`, `scripts/lint-tool-scope.py`, `scripts/test-cookbooks.sh`, `scripts/validate.py`, `managed-agent-cookbooks/README.md` | Infrastructure d'assemblage/validation citée ; réutiliser contrôles dans SOC-022 sans modifier l'orchestrateur pour adapter le droit. Déploiement séparé de l'adaptation du cookbook. |
| `.claude-plugin/marketplace.json`, `README.md`, `QUICKSTART.md` racine | Installation/index à synchroniser à la livraison ; jamais dépendances runtime d'un paquet détaché. |
| Références et helper racine | Sources d'édition des copies embarquées comparées dans le relevé, pas chemins de repli à l'exécution. BASE-003/005/006/008/010 et protocole USAGE-001 guident les lots. |
| VDR/dépôts, calendrier, messagerie, Office/openpyxl, Sheets/ADC, Luminance/Kira, recherche juridique | Accès facultatifs à constater réellement ; fichiers fournis et sortie locale restent possibles. Outil déclaré, configuré et appel réussi ont des états distincts. |
| commercial, travail, PI, privacy, réglementation, fiscalité DOM-011, contentieux | Compléments par question précise selon BASE-003 ; aucun autre plugin requis pour comprendre la sortie. Les modèles US ne justifient ni transfert de responsabilité ni commande future présentée comme installée. |

## Conservation, renommage et retraits

Aucun skill entier supprimé : chaque tâche fournit un résultat utile bornable.
Aucun identifiant technique renommé. Renommer les **présentations** « unanimous
board consent », « good standing » et « auto-assign » ne suffira pas : les
procédures, états de preuve et hypothèses à retirer sont attribués ci-dessus.
Le contenu Public Company sans skill reçoit un retrait des promesses dans
SOC-019, sans remplacement automatique par un calendrier AMF. Les cas SA,
société cotée, opération sur capital, fusion, dissolution ou procédure
collective demandent une tranche propre avant toute rédaction métier.

