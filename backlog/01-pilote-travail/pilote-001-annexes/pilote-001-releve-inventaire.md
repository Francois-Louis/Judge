# PILOTE-001 — Inventaire de contenu du plugin travail

Audit local du **15 octobre 2026 (Europe/Paris)**, révision de départ
`bf1dc682cda0fc247a51a090cecfa7c4c6fe7fb7`.
Plugin source `employment-legal`, identifiant publié
`judge-fr-eu-employment-legal`, version `0.1.0`.

**Aucun des 20 skills n'est adapté au droit français par cette livraison.**
L'audit prépare PILOTE-002 et les suites ; il ne réécrit ni skills, ni profil,
ni agent. L'isolation technique BASE-008 ne constitue pas une adaptation juridique.

## Méthode et couverture

Lecture du corps intégral des 20 `SKILL.md`, du modèle `CLAUDE.md`, du README,
de l'agent, des quatre références livrées et des métadonnées/configurations.
Examen du contrat d'accès au helper de stockage et de ses points d'entrée,
sans nouvel audit de son implémentation de sécurité. Le
[relevé de contrôle](pilote-001-resultats.json) conserve chemins et empreintes.
Les documents utilisateur, profils réels, HRIS et autres connecteurs ne sont
pas consultés. Les parcours ci-dessous sont suivis **dans les instructions**,
sans invocation d'un modèle ni exécution d'une commande métier.

## Dépendances communes

Les chemins de paquet ci-dessous partent de
[`employment-legal/`](../../../employment-legal/). Les chemins de données sont
des entrées utilisateur futures, pas des fichiers manquants à ajouter au dépôt.

| Repère | Fichier ou donnée | Nature et constat |
|---|---|---|
| S | [`references/isolation.md`](../../../employment-legal/references/isolation.md) → [`scripts/judge_store.py`](../../../employment-legal/scripts/judge_store.py) | Embarqués, chargement imposé au début des 20 skills et de l'agent ; Python ≥ 3.12, accès gardé aux données durables. Les exemples `Read/Write` hérités doivent être relus à la lumière de ce contrat. |
| P | Modèle [`CLAUDE.md`](../../../employment-legal/CLAUDE.md) ; profil réel `config/judge-fr-eu/employment-legal/CLAUDE.md` et profil commun `config/judge-fr-eu/company-profile.md`, sous `~/.claude/plugins/` | Modèle embarqué, réponses utilisateur hors paquet. Secteurs, territoires, rôles, escalade, modèles, en-têtes et sources influencent tous les parcours via le profil commun au plugin. Ce modèle n'est pas automatiquement chargé comme contexte de projet. |
| M | `matters/<slug>/matter.md`, `history.md`, `notes.md`, `outputs/`, dossier actif dans P | Données utilisateur ; contexte de dossier explicite dans les skills de fond, leurs références d'enquête/implantation et `matter-workspace`. Les wrappers ne répètent pas tous ce chargement. |
| R | [`references/shared/research-citation-method.md`](../../../employment-legal/references/shared/research-citation-method.md), version `1.0.0` | Embarquée et identique à la source BASE-005 ; **aucun skill ni agent ne la charge encore**. Chaque adaptation devra ajouter le chargement local et résoudre ses contradictions avec les consignes héritées. |
| C | [`references/company-profile-template.md`](../../../employment-legal/references/company-profile-template.md) | Embarqué ; utilisé par `cold-start-interview`, entreprise/cabinet présumé. Prévoir aussi candidat/salarié/aidant sans entreprise à configurer. |
| D | [`references/dashboard-template.md`](../../../employment-legal/references/dashboard-template.md) | Embarqué ; proposé par P pour les sorties tabulaires, mention directe dans l'agent congés. Échappement HTML et provenance à conserver ; pas de règle métier française. |
| X | [`.mcp.json`](../../../employment-legal/.mcp.json) | Slack et Google Drive déclarés. HRIS/documents/chat/email sont des catégories recommandées, **pas** des connecteurs HRIS ni une recherche juridique fonctionnels. Westlaw/CourtListener cités dans les prompts ne sont pas déclarés ici. Fichiers fournis et recherche officielle sont des voies distinctes. |

`verification-log.md` est une autre donnée utilisateur référencée dans P.
Sa fenêtre générique de fraîcheur ne suffit pas à valider une version pour
un nouveau dossier. R impose le contrôle des dates et de l'applicabilité.

## Inventaire exhaustif des 20 skills

Chaque lien désigne le corps lu. S et P sont les dépendances communes
ci-dessus ; les colonnes précisent les compléments directs ou indirects.
Les prérequis sont un **programme de recherche**, sans règle française déjà validée.

| Skill | Dépendances de contenu et données | Logique réutilisable | Droit ou hypothèses à remplacer | Prérequis France/UE et suite proposée |
|---|---|---|---|---|
| [`cold-start-interview`](../../../employment-legal/skills/cold-start-interview/SKILL.md) | S, P, C ; handbook, offres, mémos de rupture, HRIS ; renvois vers hub et commandes métier | Reprise d'entretien, réponses confirmées, profil partagé, statut réel des connexions | States par défaut, at-will, severance/release, Californie/New York, proposition d'essayer une rupture ; quick start avec défauts en tension avec la borne finale BASE-008 | Distinguer candidat/salarié/employeur, public/privé, CCN/accords, territoires et dates ; setup minimal dans PILOTE-002, refonte restante TRAV-016 |
| [`customize`](../../../employment-legal/skills/customize/SKILL.md) | S, P ; modèle de profil, intégrations et préférences d'enquête | Modification ciblée et effet annoncé sur les autres parcours | At-will standard, supplements par État, exemple Washington présenté comme règle, choix de marquage privileged | Faits déclarés séparés des règles vérifiées, qualification collective/territoriale, profil candidat et compatibilité des anciennes sections ; TRAV-016 |
| [`expansion-kickoff`](../../../employment-legal/skills/expansion-kickoff/SKILL.md) | S, P → `international-expansion` complet ; `expansion-<slug>.yaml` | Intake et détection d'un tracker existant | Hypothèses EOR/entity et briefing héritées par chargement indirect | Employeur étranger recrutant en France, structure effectivement autorisée, accords/secteur et territoire ; TRAV-014 |
| [`expansion-update`](../../../employment-legal/skills/expansion-update/SKILL.md) | S, P ; tracker créé par `international-expansion` ; référence de schéma citée en fin de fichier, sans instruction explicite de la charger dans les étapes | Statuts, propriétaire, questions et prochaines tâches | Hérite de la qualification EOR/entity et des échéances du tracker, même sans doctrine propre | Distinguer jalon projet et délai légal sourcé ; ne pas clore sur simple date ; TRAV-015 |
| [`handbook-updates`](../../../employment-legal/skills/handbook-updates/SKILL.md) | S, P, M ; handbook, texte proposé, supplements ; reçoit `policy-drafting` | Diff, recherche de renvois et effets sur les avantages | State supplements, handbook promise, consideration et approbation « ready to publish » | Nature de l'acte, contrat/accord/usage/engagement, CSE et formalités à rechercher ; première tranche charte télétravail TRAV-013 |
| [`hiring-review`](../../../employment-legal/skills/hiring-review/SKILL.md) | S, P, M ; offre, fiche de poste, politique et modèle employeur ; renvoi final `wage-hour-qa` | Revue structurée, localisation réelle du travail, clauses citées, faits manquants | Exempt/non-exempt, at-will, domicile = droit applicable, ban-the-box, I-9, house policy d'abord, feu vert employeur | Contrat reçu par candidat, emploi/classification, CCN/accords, salaire/temps/essai, conflits de lois ; **PILOTE-002**, [plan détaillé](pilote-001-plan-hiring-review.md) |
| [`internal-investigation`](../../../employment-legal/skills/internal-investigation/SKILL.md) | S, P, M ; cinq modes, modèles de sources, logs et mémos internes ; pas d'agent d'enquête | Traçabilité des pièces, contradictions, couverture, chronologie, séparation faits/analyse | Upjohn, Weingarten, Garrity, NLRA, EEOC/DFEH, work product automatique, preponderance comme standard général | Mandat, harcèlement/alerte, contradictoire adapté, données/secret, acteurs compétents, délais disciplinaires à rechercher ; TRAV-009 à TRAV-011 |
| [`international-expansion`](../../../employment-legal/skills/international-expansion/SKILL.md) | S, P, M ; matrice EOR/entity, briefing fiscal/RH/conseil, schéma tracker | Questions par responsable, dépendances et hypothèses visibles | Maison mère US présumée, EOR plus simple/PI mieux protégée par entité, envoi du briefing demandé dans le texte | Faisabilité de chaque structure, prêt de main-d'œuvre/portage, emploi direct, établissement stable et sécurité sociale ; TRAV-014/015 ; aucun envoi déduit du lancement |
| [`investigation-add`](../../../employment-legal/skills/investigation-add/SKILL.md) | S, P → `internal-investigation` mode 2 ; log, checklist et documents-reviewed | Lots, critères de sélection, couverture et ratio | Enregistrement Upjohn et champ privilege hérités ; collecte large par défaut | Licéité/minimisation des pièces, accès, provenance et conservation, pas de collecte automatique RH ; TRAV-010 |
| [`investigation-memo`](../../../employment-legal/skills/investigation-memo/SKILL.md) | S → `internal-investigation` mode 4 → P, M ; log, checklist et memo.md | Mise à jour motivée, lacunes et modifications visibles | **Le wrapper lui-même** impose ATTORNEY WORK PRODUCT à toute sortie ; standard preponderance et crédibilité dans la référence | Rapport factuel provisoire, cadre du secret et appréciation sourcée sans décision disciplinaire ; TRAV-011 |
| [`investigation-open`](../../../employment-legal/skills/investigation-open/SKILL.md) | S, P → `internal-investigation` mode 1 ; répertoire et trois YAML | Intake, périmètre, contrôle du slug existant | Dossier dit privilégié dès l'ouverture ; Weingarten/Garrity et Upjohn indirects | Statut réel des personnes et employeur, accords/protocole, mandat, protection et information ; TRAV-009 |
| [`investigation-query`](../../../employment-legal/skills/investigation-query/SKILL.md) | S → `internal-investigation` mode 3 → P, M ; journal complet, checklist, gaps | Réponse avec IDs de pièces, absence de preuve explicitée | Requête spéciale Upjohn et présomption de privilege dans le journal | Accès au seul dossier autorisé, faits/allégations distingués ; aucune conclusion sur pièces non lues ; TRAV-010 |
| [`investigation-summary`](../../../employment-legal/skills/investigation-summary/SKILL.md) | S → `internal-investigation` mode 5 → P, M ; memo préexistant et destinataire | Synthèse adaptée à la décision et au public | Privilege circle, rétention systématique des citations pour RH, variantes counsel/leadership américaines | Habilitation et minimisation, justification du marquage, traçabilité conservée pour relecture ; TRAV-011 |
| [`leave-tracker`](../../../employment-legal/skills/leave-tracker/SKILL.md) | S → **agent** `agents/leave-tracker.md` → P, D, registre/HRIS | Vue d'actions avec responsable, besoin de données et examen périodique | FMLA/CFRA/PFL, USERRA, ADA ; congés ordinaires exclus ; schéma et alertes US indirects | Congé/arrêt à qualifier, contrat/CCN/accords, obligations employeur/salarié/médecin séparées ; TRAV-008, première tranche arrêt maladie |
| [`log-leave`](../../../employment-legal/skills/log-leave/SKILL.md) | S, P ; **schéma du registre fourni par l'agent**, `leave-register.yaml` | Informations groupées, ajout sans effacer les notes | **5 business days**, **15 days**, alerte à **75 %** ; FMLA/USERRA/ADA ; promesse « alert automatically » | Déclencheur et preuve, échéance indéterminée si régime absent, santé limitée au nécessaire ; TRAV-007 |
| [`matter-workspace`](../../../employment-legal/skills/matter-workspace/SKILL.md) | S, P ; modèles `matter.md`, `history.md`, `notes.md` inclus dans le skill | Dossier actif, pas de lecture croisée implicite, archive | Modèles copiés des contrats commerciaux (MSA/NDA, LoL, Delaware), in-house présumé sans besoin d'isoler les salariés | Qualité des parties et droits d'accès, distinction isolement client/salarié/enquête, archivage ≠ politique de conservation ; TRAV-016 |
| [`policy-drafting`](../../../employment-legal/skills/policy-drafting/SKILL.md) | S, P, M ; handbook ; renvois `hiring-review` et `handbook-updates` | But, public, règle et processus lisibles, cohérence | FMLA/state paid leave, state supplements, handbook non-contract disclaimer ; dress code supposé sans variation | Qualification de l'acte, accords/CCN, libertés/proportionnalité et CSE à rechercher ; télétravail uniquement TRAV-012 |
| [`termination-review`](../../../employment-legal/skills/termination-review/SKILL.md) | S, P, M ; contrats, mémos et preuves ; **`wage-hour-qa` étape 2a** pour rappels | Chronologie, motifs déclarés, preuves contradictoires, alertes avant décision | FMLA, exempt/state/title trigger, FLSA/PAGA, WARN, COBRA, OWBPA, severance contre release, « most terminations are fine » | Qualifier mode de rupture, salarié protégé, motif/procédure, CCN/ancienneté ; séparer licenciement personnel TRAV-004, rupture conventionnelle TRAV-005, collectif économique TRAV-006 |
| [`wage-hour-qa`](../../../employment-legal/skills/wage-hour-qa/SKILL.md) | S, P, M ; recherche ; renvoi `worker-classification` | Question contextualisée, sources à lire, calcul explicite et hypothèses | **FLSA §207(e)**, multiplicateurs **0,5/1,5**, doublement **§216(b)**, prescription **2/3 ans**, exempt/PTO/state defaults | Minima/classification d'une part TRAV-002, relevé et heures d'autre part TRAV-003 ; CCN/accords, période et statut du temps à rechercher |
| [`worker-classification`](../../../employment-legal/skills/worker-classification/SKILL.md) | S, P, M ; projet, fonctions, moyens ; renvoi `hiring-review` | Réalité du travail plutôt que titre, facteurs documentés et limites du prospectif | ABC/economic realities, IRS §530, W-2/1099, PAGA, joint employer ; vendor/SOW présenté comme le plus propre | Subordination et qualifications réelles, prestation/intérim/portage et règles sociales distinctes, régime/territoire ; TRAV-001 ; situations déjà exécutées réservées |

Il y a **18 skills invocables** et **2 références non invocables**
(`internal-investigation`, `international-expansion`). `handbook-updates` n'a
pas de `user-invocable: false` ; son affichage sans commande dans le README
ne le rend pas non invocable. `customize` est absent de la table du README.
Il n'y a pas de répertoire `commands/` dans ce plugin : les commandes sont
les skills invocables, sous le namespace publié.

## Chaînes de chargement suivies

| Entrée | Chaîne réelle dans le contenu | Fichiers/données et risque indirect |
|---|---|---|
| `leave-tracker` | `skills/leave-tracker/SKILL.md`, instruction 1 → `agents/leave-tracker.md`, étapes 1 à 6 | P puis HRIS ou `leave-register.yaml` ; calculs FMLA, USERRA, ADA ; enregistrement recalculé ; D optionnel. Les outils déclarés de l'agent sont Read/Write et requêtes MCP ; le besoin d'exécuter le helper Python imposé par S devra être vérifié en client, pas présumé compatible. |
| `log-leave` | Instructions 3/4 → P et chiffres codés ; instruction 5 → format de l'agent | Le simple remplacement de l'agent laisserait les délais 5/15 et l'automatisation promise dans le wrapper. Pas d'ordonnanceur livré : `hooks/hooks.json` est vide, l'agent dit lui-même qu'il ne s'exécute pas seul. |
| `investigation-open` | Instructions 1/2 → P → référence `internal-investigation`, mode 1 | `investigation-<slug>/log.yaml`, `sources-checklist.yaml`, `documents-reviewed.yaml` ; collecte représentations syndicales/public employer → Weingarten/Garrity ; checklists Upjohn. |
| `investigation-add` | Instructions 1/2 → P → même référence, mode 2 | Lit/complète ces YAML, pièces et IDs ; `privilege: attorney-work-product` inscrit dans chaque entrée ; confirmation de couverture, sans ingestion réelle ici. |
| `investigation-query` | Instruction 1 → même référence, mode 3 → P/M | Log complet puis checklist/gaps selon la question ; branche Upjohn dédiée. |
| `investigation-memo` | Instruction 1 → même référence, mode 4 ; instruction 4 du wrapper | Lit log/checklist et `memo.md` existant ; standard de preuve et en-têtes américains restent dans **les deux** fichiers. |
| `investigation-summary` | Instruction 1 → même référence, mode 5 → `memo.md` | Synthèse selon audience, retrait de sources pour RH, gate EEOC/DFEH dans la référence. Aucun agent d'enquête distinct à adapter. |
| `termination-review` | Flag exempt et demande de chiffrage → `wage-hour-qa`, étape 2a | Une revue de rupture traduite pourrait encore produire un rappel FLSA ; réserver le renvoi non adapté dans la future tranche française. |
| `expansion-kickoff` / `expansion-update` | Référence commune `international-expansion` et schéma `expansion-<slug>.yaml` | Les tâches sans doctrine propre héritent de la qualification initiale et des dates. L'en-tête brut du modèle YAML de la référence n'est pas un commentaire YAML ; à corriger dans TRAV-014, pas dans l'audit. |

La référence d'enquête indique à la fois un contexte M et des chemins
`investigation-<slug>/` à la racine du domaine ; sa recherche de tous les
dossiers s'oppose potentiellement à l'isolement du dossier actif.
Le suivi des congés lit aussi un registre global, sans sélection explicite de M.
Ce sont des points à éprouver dans TRAV-009/010, TRAV-008 et TRAV-016 ;
aucune fuite réelle n'a été testée ou constatée pendant cet audit.

## Profil, références et accès à reprendre

Dans P, conserver la distinction template/profil réel et l'isolation S.
Revoir `Who we are`, `Who's using this`, `Jurisdictional footprint`,
`Hiring review`, `Termination review`, `Handbook`, `Wage & hour`,
`Jurisdiction-specific escalation rules`, `Systems` et `Escalation` :
les cases américaines ne couvrent ni CCN/IDCC et accords d'entreprise,
ni candidat autonome, ni statut public/privé, ni régime territorial précis.

`Outputs`, `Destination check` et les modèles d'enquête affirment des effets
de privilege/work product trop généraux. R interdit la garantie automatique
de secret. Les consignes de recherche se contredisent aussi : certains skills
ordonnent de s'arrêter après peu de résultats et de redemander l'accord pour
le web, P permet un supplément étiqueté, R permet d'autres publications
officielles avec réserve limitée à la conclusion incertaine. PILOTE-002 doit
résoudre ces conflits pour son seul parcours, sans certifier les autres.

Les quatre références livrées sont les fichiers S (isolation), R, C et D :
**aucun corpus français d'emploi ou de convention collective n'est fourni**.
Les exemples juridiques sont surtout dans les skills, P et l'agent ; les
rechercher seulement dans un dossier `references/` manquerait l'essentiel.
Le manifeste conserve « controlling state test » et « state supplements ».
README et description sont hérités, avec une mention technique d'adaptation
en attente ; ils ne prouvent pas une couverture France/UE.

## Qualification française commune à prévoir

| Dimension | Informations et contrôle à inscrire dans chaque future tranche concernée |
|---|---|
| Parties et régime | Candidat/salarié/employeur/conseil/aidant ; employeur et statut réel de la relation, sans déduire emploi public de la seule nature publique de l'organisme. Emploi public → DOM-037, encore proposé. Régimes particuliers (apprentissage, particulier employeur, agricole, mandataire social, etc.) à borner ou orienter, jamais assimiler sans contrôle. |
| Règles collectives | Activité réelle, convention mentionnée et IDCC éventuel, champ professionnel/territorial/personnel, extension/adhésion/application volontaire à vérifier ; accords de branche, d'entreprise/établissement, dates et articulation par sujet. Ni APE seul, ni titre de poste ne suffisent au futur contrôle. |
| Territoires | Lieux effectifs et habituels de travail, établissement employeur, déplacements, télétravail, détachement, outre-mer précis. Séparer loi applicable, juge compétent et protection sociale ; la clause choisie ou le domicile ne résout pas tout. |
| Temps | Dates des faits et d'exécution, périodes de paie, versions des accords/textes, transitions ; conserver provenance de chaque date. |
| Sortie utile | Clause ou pièce précise, explication accessible, effet concret, hypothèse réservée, question/pièce/interlocuteur suivant. Pas de décision favorable garantie ni de playbook employeur obligatoire pour un candidat. |

## Programme de recherche et accès effectivement éprouvés

BASE-005 reste le socle ; chaque future tranche ajoutera ses références
**dans le plugin** et recontrôlera les textes utiles au dossier.

| Piste de recherche pour l'implémentation | Questions à établir ; état dans cet audit |
|---|---|
| Code du travail et textes d'application | Formation du contrat, CDD/temps partiel/essai, minima et temps, rupture, santé et représentation ; **non vérifiés**, hormis lecture limitée de L2261-2 ci-dessous. Aucun barème français n'est livré. |
| Corpus conventionnel Légifrance/KALI, accords fournis et publications officielles | Applicabilité, classifications, minima, essai, préavis/congés et articulation par thème ; **non vérifiés**, aucune CCN choisie d'avance. |
| Jurisprudence officielle française | Qualification/subordination, clauses restrictives et essai, preuve/confidentialité, enquête et rupture ; **non vérifiée**, aucune décision mémorisée transformée en source contrôlée. |
| Rome I, Bruxelles I bis, détachement et coordination sociale UE | Rattachements selon la question, sans confondre contrat/juridiction/cotisations ; seul le passage Rome I décrit ci-dessous a été lu, reste à vérifier pour un dossier. |
| RGPD, textes nationaux et CNIL | Collecte, accès, information, conservation, alertes/données de santé ; **non vérifiés** pour les futurs parcours. Documents explicatifs distingués des textes. |
| Sources emploi public, protection sociale, fiscalité et sociétés | Orientation limitée respectivement DOM-037, DOM-012/036, DOM-011 et corporate-legal ; aucun de ces domaines n'est une dépendance obligatoire du plugin. |

Les premiers accès web directs ont échoué (Légifrance : erreur d'accès ;
EUR-Lex : écran JavaScript). À la demande de l'utilisateur, **BASE-010 a fourni
et testé des routes officielles alternatives**, voir
[procédure](../../../references/legal-source-access.md) et
[résultats horodatés](../../00-fondations/base-010-annexes/base-010-resultats-acces.json).

- **F1** — [Code du travail numérique, L2261-2](https://code.travail.gouv.fr/code-du-travail/l2261-2),
  ouvert par HTTP le 15 octobre 2026 ; texte intégral de l'article, lien source
  `LEGIARTI000006901780`, date affichée `01/05/2008` lus. Statut `partiel` :
  reproduction officielle accessible, version temporelle et champ conventionnel
  d'un dossier non établis ; applicabilité `a-etablir`. Ce passage justifie de
  rechercher l'activité exercée pour le rattachement, pas de choisir une CCN.
- **F2** — [Règlement (CE) n° 593/2008, texte français via CELLAR](https://publications.europa.eu/resource/cellar/3db0a06f-cae9-433d-a229-dde3e68d6dc7.0010.03/DOC_1),
  CELEX `32008R0593`, ouvert le 15 octobre 2026 ; article 8 et contexte voisin
  lus. Statut `partiel` : acte d'origine, non consolidation à la date d'un
  dossier ; modifications, transitions et jurisprudence non contrôlées ;
  applicabilité `a-etablir`. Ce passage motive le remplacement de l'équivalence
  « domicile = droit applicable », sans résoudre un cas transfrontalier.

Le script garde le statut documentaire initial `non-verifie` à la récupération ;
les deux mentions `partiel` ci-dessus résultent de la lecture du contenu
pendant cette session d'audit, sans validation d'un futur dossier.

## Suites et limites de livraison

Le [découpage](pilote-001-decoupage-travail.md) rattache chaque workflow à une
story proposée et à ses dépendances, avec des tranches distinctes pour salaire
et temps, modes de rupture, saisie et suivi d'absence, étapes d'enquête,
politique et impact documentaire, lancement et suivi d'implantation.

Les scénarios de [hiring-review](pilote-001-plan-hiring-review.md) sont des
**attentes de recette**, pas des sorties exécutées. PILOTE-002 reste proposée,
avec USAGE-002 parmi ses dépendances. L'utilisateur a demandé l'audit ; cela
ne clôt ni USAGE-002 ni le choix de toute la feuille de route. Les autres
implémentations attendent PILOTE-003. Fonction publique, autres régimes de
congé, paie complète et licenciement collectif complet restent hors des
premières tranches ; aucun workflow n'est déclaré adapté par anticipation.
