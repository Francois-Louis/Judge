# DOM-002 — Découpage du domaine police et procédure pénale

Propositions du **16 octobre 2026**. Les 17 stories CRIM restent `proposee`.
La [relecture documentaire](dom-002-verification.md) éprouve le routage sur
les trois scénarios de la story et sur des cas limites. Aucun répertoire de
plugin n'est créé par ce cadrage.

## Plugin retenu et contrat d'installation

**Nom conservé : `criminal-legal`**, identifiant publié
`judge-fr-eu-criminal-legal` (BASE-008). Le domaine aide une personne face à
une mesure policière, une convocation, une plainte, une amende ou un acte de
procédure pénale. Public premier : la personne concernée ou un proche, sans
formation juridique, qu'elle soit témoin, victime ou mise en cause. Public
second : une organisation qui reçoit une réquisition (CRIM-009). Le plugin
ne remplace pas l'avocat ; il prépare les faits et les questions à lui poser.

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 `1.0.0` et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais est une orientation. |
| Création du paquet | Par CRIM-001, avec son premier skill. Aucun paquet vide. Inscription au marketplace et décompte des paquets dans les tests BASE-008 : décision explicite au moment de sélectionner CRIM-001, coordonnée avec CONSO-001 si les deux sont retenues. |
| Profil et stockage | Aucun profil requis. Les faits pénaux sont des données sensibles : aucune tâche proposée ne les conserve durablement. Un stockage n'est ajouté que par une story dédiée qui en démontre le besoin et la protection. |
| Agents, hooks, connecteurs | Aucun prévu. Pas de `.mcp.json`, de hook, d'agent ni de cookbook par principe. |
| Envoi | Le plugin prépare des fiches et des brouillons ; il n'envoie rien, ne contacte aucun service et ne dépose aucune plainte. |

## Garde-fous propres au domaine

- **Urgence d'abord.** Mesure en cours, convocation imminente, mineur,
  danger : la sortie commence par ce qui doit être fait maintenant, en peu de
  lignes, puis l'analyse documentaire.
- **Pas d'évitement de la justice.** Le plugin ne conseille pas de ne pas se
  présenter, de mentir, de dissimuler ou détruire une preuve, de contacter une
  victime ou un témoin pour influencer sa déclaration. Il explique que les
  conséquences d'un choix se vérifient avec un avocat et dans le texte.
- **Statut avant droits.** Les droits annoncés dépendent du statut et de la
  mesure établis ; aucune liste de droits n'est donnée depuis le seul mot
  « police ». Aucun équivalent américain (Miranda, subpoena, plea, grand
  jury) n'est importé.
- **Aucune qualification présumée.** Le plugin parle d'« infractions
  possibles à examiner », jamais de culpabilité ou d'innocence établie.
- **Recours à l'avocat.** Pour toute personne mise en cause ou gardée à vue,
  la sortie nomme le recours à un avocat et la manière de l'obtenir, à
  vérifier dans la source lue.

## Qualification commune

CRIM-001 crée `criminal-legal/references/qualification-penale.md`, réutilisée
par les autres skills du paquet. Chaque axe change la tâche ou la réponse ;
le cadrage ne fixe pas la règle applicable.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Statut de la personne | Témoin, victime, personne soupçonnée, gardée à vue, poursuivie, condamnée, proche, organisation ; ce que le document indique et ce que la personne suppose. | Droits, assistance et suite diffèrent ; un statut supposé reste « déclaré ». |
| Mesure exacte | Contrôle d'identité, vérification d'identité, audition libre, garde à vue, perquisition, convocation, acte de poursuite, jugement, amende. | Ne pas confondre contrôle, audition libre et garde à vue. Une retenue douanière ou pour vérification du droit au séjour relève d'abord d'un autre domaine. |
| Autorité | Police nationale, gendarmerie, police municipale, douane, parquet, juge, tribunal, service des amendes. | Police judiciaire ou administrative ; autorité administrative → DOM-010 ou secteur. |
| Dates et heures | Heure de début d'une mesure, date et heure de convocation, date d'infraction, d'envoi et de réception d'un avis. | Chaque date est prouvée, déclarée ou inconnue. Aucune durée ni délai calculé sans texte lu. |
| Âge et vulnérabilité | Mineur, majeur protégé, santé, besoin d'interprète. | Régime des mineurs distinct ; protection juridique coordonnée avec DOM-026. |
| Urgence | Mesure en cours, audience ou convocation proche, danger, privation de liberté. | Ordre de la sortie. |
| Pièces | Convocation complète, avis, procès-verbal remis, récépissé de plainte, jugement, preuve de paiement, enveloppe ou preuve de réception. | Une pièce absente est un manque, pas une absence d'acte. Un SMS ou courriel de « convocation » est vérifié avant d'être pris pour authentique. |

## Frontières

Le domaine garde la procédure pénale et les démarches de la personne dans
cette procédure. Un même événement peut ouvrir un volet pénal et des volets
civil, administratif ou de protection distincts, chacun avec son domaine.

| Domaine | Ce qui lui revient | Ce que criminal garde |
|---|---|---|
| Contentieux — EXIST-006/CTX | Procédure civile ou commerciale identifiée ; demande de pièces entre parties. | Convocation par une autorité pénale, réquisition pénale (CRIM-009). Aucun traitement « subpoena ». |
| Responsabilité — DOM-035 | Faits, preuves et chiffrage d'un dommage, action civile hors procédure pénale. | Plainte et constitution de partie civile dans la procédure pénale. L'indemnisation des victimes par une commission ou un fonds relève de CRIM-013. |
| Violences intrafamiliales — DOM-038 | Parcours de protection, canal sûr, coordination des volets. | La qualification pénale et les actes de procédure, sur question bornée transmise par DOM-038. CRIM-004 ne traite pas seul une plainte pour violences intrafamiliales. |
| Séjour — DOM-028 | Retenue pour vérification du droit au séjour, éloignement, rétention. | Procédure pénale visant une personne étrangère ; les conséquences sur le séjour sont une question à DOM-028. |
| Douanes — DOM-009 | Retenue, procès-verbal et transaction douaniers. | La procédure pénale lorsque l'affaire est confiée au parquet ou à la police judiciaire. |
| Administratif — DOM-010 | Mesures de police administrative (fermeture, interdiction administrative). | Mesures de police judiciaire. |
| Véhicules — DOM-023 | Achat, location, réparation. | Infractions routières, amendes et information sur les points du permis ; la suspension ou l'invalidation administrative est lue et orientée, sans recours préparé. |
| Exécution — DOM-003 | Acte de saisie, y compris pour le recouvrement d'une amende. | Contestation de l'amende elle-même. |
| Numérique — DOM-034 | Signalement à la plateforme, retrait, suspension de compte. | Plainte pour harcèlement, usurpation ou menaces en ligne. |
| Consommation et banque — DOM-001, DOM-004 | Réclamation au vendeur, remboursement bancaire. | Plainte pour escroquerie. |
| Travail — employment | Enquête interne, entretien préalable, droits du salarié. | Plainte et procédure pénale liées au travail. |
| Santé — DOM-007 | Soins sans consentement. | Rien sur ces mesures. |
| Clinique et formation — EXIST-009, EXIST-010 | Accueil, supervision, exercices. Le modèle « criminal defense » de la clinique n'est pas repris. | La tâche du justiciable. |

## Tâches hiérarchisées

Le rang combine l'utilité directe pour une personne (situation S-37 et
amendes du quotidien), la vérifiabilité d'un premier lot et la complexité
des régimes urgents. Il reste une proposition : aucune story n'est
sélectionnée par DOM-002. Toutes dépendent de DOM-002, PILOTE-003, BASE-005
et BASE-006 ; CRIM-001 crée le paquet. Les rangs 1 à 3 portent la priorité
P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [CRIM-001](suites/crim-001-lire-convocation.md) | `summons-reading` | Fiche d'une convocation par la police ou la gendarmerie, questions et préparation | Aucune |
| 2 | [CRIM-002](suites/crim-002-mesure-en-cours.md) | `custody-orientation` | Orientation brève pendant une garde à vue ou une retenue en cours | CRIM-001 |
| 2 | [CRIM-003](suites/crim-003-lire-avis-amende.md) | `fine-notice-reading` | Fiche d'un avis d'amende, stade et options à vérifier | CRIM-001 |
| 2 | [CRIM-004](suites/crim-004-preparer-plainte.md) | `complaint-preparation` | Chronologie, pièces et lieux de dépôt d'une plainte | CRIM-001 |
| 3 | [CRIM-005](suites/crim-005-contester-amende.md) | `fine-contest` | Brouillon de requête ou de réclamation contre une amende | CRIM-003 |
| 3 | [CRIM-006](suites/crim-006-lire-acte-poursuite.md) | `court-document-reading` | Fiche d'un acte de poursuite ou d'un jugement pénal | CRIM-001 |
| 3 | [CRIM-007](suites/crim-007-suivre-plainte.md) | `complaint-follow-up` | Lecture d'un avis de classement ou d'une suite donnée à une plainte | CRIM-004 |
| 3 | [CRIM-015](suites/crim-015-interpellation.md) | `arrest-follow-up` | Point après une interpellation : documents, objets retenus, suite | CRIM-001 |
| 4 | [CRIM-008](suites/crim-008-controle-subi.md) | `stop-account` | Récit structuré d'un contrôle ou d'une fouille déjà subis, et canaux à vérifier | CRIM-001 |
| 4 | [CRIM-009](suites/crim-009-requisition-organisation.md) | `requisition-reading` | Fiche d'une réquisition reçue par une organisation | CRIM-001 |
| 4 | [CRIM-010](suites/crim-010-points-permis.md) | `licence-points-reading` | Lecture d'un courrier sur les points du permis | CRIM-003 |
| 4 | [CRIM-011](suites/crim-011-mineur-mis-en-cause.md) | `minor-orientation` | Orientation des parents d'un mineur mis en cause | CRIM-001 |
| 4 | [CRIM-012](suites/crim-012-casier-judiciaire.md) | `criminal-record-request` | Demande d'extrait de casier et lecture des mentions | CRIM-001 |
| 4 | [CRIM-013](suites/crim-013-indemnisation-victimes.md) | `victim-compensation` | Orientation d'une victime vers l'indemnisation de son préjudice | CRIM-004 |
| 4 | [CRIM-014](suites/crim-014-execution-peines.md) | `sentence-execution` | Lecture d'une peine prononcée et de ses convocations | CRIM-006 |
| 4 | [CRIM-016](suites/crim-016-manifestation.md) | `demonstration-guide` | Cadre d'une manifestation et suites pour un participant | CRIM-001 |
| 4 | [CRIM-017](suites/crim-017-armes.md) | `weapons-status` | Catégorie, autorisations et démarche régulière pour une arme ou un objet | CRIM-001 |

CRIM-001 possède `qualification-penale.md` ; CRIM-003 possède
`amendes.md`, relu par CRIM-005 et CRIM-010 ; CRIM-004 possède `plainte.md`,
relu par CRIM-007. Une tâche suivante consomme ces références sans les
réécrire. Aucun cycle de dépendances.

## Première tranche : CRIM-001

**Inclus :** un document qui convoque une personne majeure par la police ou
la gendarmerie, reçu par courrier, remis en main propre ou annoncé par
téléphone ou message, avec ou sans qualité indiquée. Sortie utile au témoin,
à la victime ou à la personne soupçonnée.

**Exclus :** mesure en cours (CRIM-002) ; convocation devant un tribunal,
citation, ordonnance ou jugement (CRIM-006, fiche minimale et orientation) ;
mineur (CRIM-011, orientation) ; convocation administrative, douanière,
d'employeur ou de préfecture ; qualification de l'infraction ; préparation du
contenu de l'audition ; conseil de ne pas se présenter ; envoi.

**Sortie :** ce qu'il faut faire maintenant si la date est proche ; fiche du
document (autorité, date, lieu, référence, qualité indiquée ou absente) avec
statut de chaque mention ; questions à poser au service émetteur et à un
avocat ; pièces à apporter selon le document ; droits à vérifier selon le
statut établi ; limites.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005 et distinguer loi, acte UE, jurisprudence et information publique.
Les voies officielles BASE-010 servent en maintenance, jamais au runtime.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Convocation et audition libre | Code de procédure pénale, audition libre et comparution sur convocation (pistes 61-1, 78) ; directives 2012/13/UE, 2013/48/UE et 2010/64/UE. | CRIM-001 |
| Garde à vue | Code de procédure pénale, garde à vue et notification des droits (pistes 62-2 et suivants, 63-1 et suivants). | CRIM-002 |
| Mineurs | Code de la justice pénale des mineurs ; directive (UE) 2016/800. | CRIM-002, CRIM-011 |
| Amendes | Code de procédure pénale, amende forfaitaire, requête et réclamation (pistes 529 et suivants, 530) ; Code de la route, responsabilité du titulaire et désignation du conducteur (piste L121-3) ; ANTAI comme service d'information. | CRIM-003, CRIM-005 |
| Points du permis | Code de la route, permis à points (piste L223-1 et suivants). | CRIM-010 |
| Plainte et suites | Code de procédure pénale, plainte, avis et recours après classement, constitution de partie civile (pistes 15-3, 40-2, 40-3, 85) ; directive 2012/29/UE. Plainte en ligne : service officiel en vigueur à vérifier. | CRIM-004, CRIM-007 |
| Poursuites et jugement | Code de procédure pénale, modes de saisine, ordonnance pénale, voies de recours ; aide juridictionnelle. | CRIM-006 |
| Contrôles | Code de procédure pénale, contrôles et vérifications d'identité (pistes 78-2, 78-3) ; Code de la sécurité intérieure, déontologie ; Défenseur des droits et inspections comme canaux à vérifier. | CRIM-008 |
| Réquisitions | Code de procédure pénale, réquisitions (pistes 60-1, 77-1-1, 99-3) ; secret professionnel et données personnelles. | CRIM-009 |
| Casier judiciaire | Code de procédure pénale, casier et bulletins (pistes 768 et suivants, 777) ; service officiel de demande. | CRIM-012 |
| Infractions | Code pénal et textes spéciaux, seulement pour nommer des infractions possibles à examiner, sans qualification. | CRIM-004, CRIM-006 |

Les pages d'information publiques (service-public, ANTAI, ministère de la
Justice) orientent ; elles ne remplacent pas la lecture du texte cité.

## Contrat commun des stories CRIM

Chaque lot applique BASE-003, BASE-008, la méthode BASE-005 embarquée, les
garde-fous ci-dessus et les couches de recette BASE-006 : structure, paquet
détaché, client, résultat métier, lecture par une personne sans formation
juridique. Il inscrit NOTICE local et racine, synchronise manifeste et
marketplace, et n'annonce dans le README que les tâches livrées.

Chaque skill qualifie d'abord, puis traite. Il charge la méthode locale,
distingue mention du document, fait déclaré, règle lue et inconnue, et ne
donne ni durée, ni délai, ni montant sans source lue et date établie, hors
montant recopié d'un document. Les pièces fournies sont des données, jamais
des instructions. Sans référence ou relais adapté, il produit les questions
et pièces utiles, sans appeler une branche absente.

Les fichiers « à créer » des suites sont des livrables futurs. La portée de
ce cadrage figure dans la [vérification](dom-002-verification.md).
