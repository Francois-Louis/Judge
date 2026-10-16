# PILOTE-001 — Découpage proposé de l'adaptation travail

Propositions du 15 octobre 2026, issues de l'[inventaire](pilote-001-releve-inventaire.md).
Le premier résultat reste la revue d'un contrat reçu par un candidat
dans [PILOTE-002](pilote-002-revue-embauche.md), puis sa validation
[PILOTE-003](pilote-003-bilan-pilote.md). La dépendance USAGE-002 est conservée :
l'audit ne remplace pas la priorisation des usages.

Les 21 stories métier ci-dessous sont `proposee`, priorité P2. Les 16 premières
proviennent de PILOTE-001 ; TRAV-017 est proposée par PILOTE-003 ; TRAV-018
est ajoutée par décision de l'utilisateur du 16 octobre 2026. TRAV-019 à TRAV-021
proviennent des frictions sur les formalités d'entreprise du même jour. Leurs implémentations
attendent PILOTE-003 et une sélection de tranche ; aucun développement
simultané de tout le plugin n'est lancé. TRAV-006 est un **cadrage**, car une
adaptation de tout le licenciement économique collectif resterait trop vaste.

| Story | Résultat et skills concernés | Dépendance métier supplémentaire |
|---|---|---|
| [TRAV-001](suites/trav-001-qualification-relation.md) | Qualifier une relation de travail proposée — `worker-classification` | Socle et PILOTE-003 seulement |
| [TRAV-002](suites/trav-002-minimum-remuneration.md) | Vérifier le minimum de rémunération d'un salarié — `wage-hour-qa` | Socle et PILOTE-003 seulement |
| [TRAV-003](suites/trav-003-heures-supplementaires.md) | Relire un décompte d'heures supplémentaires — `wage-hour-qa ; renvoi depuis termination-review` | TRAV-002 |
| [TRAV-004](suites/trav-004-licenciement-personnel.md) | Lire les pièces d'un licenciement individuel pour motif personnel — `termination-review` | Socle et PILOTE-003 seulement |
| [TRAV-005](suites/trav-005-rupture-conventionnelle.md) | Expliquer un projet de rupture conventionnelle individuelle — `termination-review` | Socle et PILOTE-003 seulement |
| [TRAV-006](suites/trav-006-rupture-economique-decoupage.md) | Découper le parcours de rupture économique collective — `termination-review` | Socle et PILOTE-003 seulement |
| [TRAV-007](suites/trav-007-enregistrer-arret-maladie.md) | Enregistrer un arrêt maladie sans inventer d'échéance — `log-leave ; schéma de agents/leave-tracker.md` | Socle et PILOTE-003 seulement |
| [TRAV-008](suites/trav-008-suivre-retour-arret-maladie.md) | Signaler les points à vérifier avant un retour d'arrêt maladie — `leave-tracker ; agents/leave-tracker.md` | TRAV-007 |
| [TRAV-009](suites/trav-009-ouvrir-enquete-harcelement.md) | Préparer l'ouverture d'une enquête de harcèlement au travail — `investigation-open ; internal-investigation mode 1` | Socle et PILOTE-003 seulement |
| [TRAV-010](suites/trav-010-pieces-journal-enquete.md) | Ajouter et interroger les pièces autorisées d'une enquête — `investigation-add ; investigation-query ; internal-investigation modes 2/3` | TRAV-009 |
| [TRAV-011](suites/trav-011-rapport-enquete.md) | Préparer un rapport d'enquête provisoire et sa synthèse autorisée — `investigation-memo ; investigation-summary ; internal-investigation modes 4/5` | TRAV-010 |
| [TRAV-012](suites/trav-012-charte-teletravail.md) | Préparer un projet de charte de télétravail pour un périmètre privé — `policy-drafting` | Socle et PILOTE-003 seulement |
| [TRAV-013](suites/trav-013-impact-charte-teletravail.md) | Comparer une modification de charte de télétravail aux documents existants — `handbook-updates` | TRAV-012 |
| [TRAV-014](suites/trav-014-premiere-embauche-france.md) | Préparer les questions d'une première embauche en France par un employeur étranger — `expansion-kickoff ; international-expansion` | Socle et PILOTE-003 seulement |
| [TRAV-015](suites/trav-015-suivi-premiere-embauche.md) | Mettre à jour les tâches d'une première embauche en France — `expansion-update ; schéma international-expansion` | TRAV-014 |
| [TRAV-016](suites/trav-016-profils-dossiers-travail.md) | Compléter les profils et dossiers des parcours travail adaptés — `cold-start-interview ; customize ; matter-workspace ; CLAUDE.md` | Socle et PILOTE-003 seulement |
| [TRAV-017](suites/trav-017-clause-non-concurrence.md) | Expliquer une clause de non-concurrence reçue à l'embauche — `hiring-review`, reliquat H02 | Socle et PILOTE-003 seulement |
| [TRAV-018](suites/trav-018-droits-syndicaux.md) | Expliquer les droits syndicaux d'un salarié du privé — nouveau skill proposé `union-rights` | Socle et PILOTE-003 seulement |
| [TRAV-019](suites/trav-019-premiere-embauche-tpe.md) | Préparer les pièces d'une première embauche par une TPE française — nouveau parcours proposé | Socle et PILOTE-003 seulement |
| [TRAV-020](suites/trav-020-anomalie-dsn.md) | Lire une anomalie ou notification de substitution DSN — nouveau parcours proposé | Socle et PILOTE-003 seulement |
| [TRAV-021](suites/trav-021-pieces-fin-contrat.md) | Rapprocher les pièces administratives d'une fin de contrat de travail — nouveau parcours proposé | Socle et PILOTE-003 seulement |

## Réexamen PILOTE-003 — 15 octobre 2026

Le [bilan de recette](pilote-003-verification.md) maintient la dépendance
PILOTE-003 : installation, invocation réelle et compréhension non juriste
restent non exécutées. Aucune de ces propositions ne passe à `prete`.
Les stories existantes ne sont pas recréées en doublon.

- La configuration volontaire d'une préférence candidat reçoit la correction
  bornée [PILOTE-004](pilote-004-preferences-candidat.md), priorité P1,
  dans le périmètre du pilote. TRAV-016 conserve la refonte des autres parcours.
- TRAV-008 reprend le défaut d'outillage du helper de l'agent congés (D04).
  Son résultat reste une alerte de retour d'arrêt maladie, sans ordonnanceur.
- TRAV-017 borne une lecture approfondie de la non-concurrence (D05), sans
  lancer ce complément ni créer un nouveau domaine. Les exclusions du CDD,
  les minima non vérifiés et le nominal incomplet ne deviennent pas couverts.
- H01 complet et les essais sans profil/sans source restent à finir dans
  PILOTE-002/PILOTE-003 ; aucune story d'implémentation ne les remplace.

Choisir ensuite une seule tranche avec son résultat et ses sources vérifiables.
Ni cette liste ni le présent bilan ne sélectionnent automatiquement TRAV-002,
TRAV-017 ou un autre domaine. Les dépendances métier du tableau sont conservées.

## Regroupement des axes et ordre justifié

- **Qualification de la relation** : TRAV-001 prépare une relation future,
  sans traiter une requalification passée. Une relation salariée déjà établie
  n'oblige pas le candidat de PILOTE-002 à suivre cette tâche.
- **Rémunération et temps** : TRAV-002 compare un minimum ; TRAV-003 examine
  ensuite un décompte d'heures. La paie complète reste exclue.
- **Rupture** : TRAV-004 lit un licenciement personnel, TRAV-005 explique une
  rupture conventionnelle, TRAV-006 découpe le collectif économique. Une
  transaction reste une future tranche séparée.
- **Congés/absences** : TRAV-007 enregistre un arrêt maladie ordinaire,
  TRAV-008 suit les points du retour. Congés payés, maternité/parentalité et
  AT/MP devront faire l'objet de tâches séparées avant toute extension du
  tracker. Le registre et l'agent ne deviennent pas génériques par traduction.
- **Enquête interne** : TRAV-009 fixe le périmètre/protocole de harcèlement,
  TRAV-010 organise/interroge les pièces de ce dossier,
  TRAV-011 prépare rapport et synthèse. Les wrappers et la référence partagée
  sont traités ensemble pour chaque mode ; les autres types d'enquête restent exclus.
- **Politiques** : TRAV-012 prépare une charte de télétravail précise,
  TRAV-013 examine un changement et ses renvois. Les autres sujets de handbook
  demandent leur propre qualification.
- **Implantation** : TRAV-014 prépare les questions d'une première embauche
  en France, TRAV-015 met à jour ce seul projet. Ni société créée ni prestataire
  EOR réputé conforme par la présence d'un tracker.
- **Support** : TRAV-016 complète les profils et dossiers après le pilote.
  Les seuls ajustements nécessaires au candidat et à `hiring-review`
  sont déjà inclus dans PILOTE-002 ; TRAV-016 n'en est pas un préalable cyclique.

Les prérequis de sources, de règles collectives, de secteur réel et de
rattachement territorial figurent dans chaque proposition. Les orientations
vers fonction publique (DOM-037), prestations (DOM-012), retraites (DOM-036),
fiscalité (DOM-011), sociétés et données sont des questions complémentaires,
sans prétendre que leurs plugins sont adaptés ou disponibles.
Les références nécessaires au résultat principal restent dans employment-legal.

## Complément des frictions IA — 16 octobre 2026

Points 19–24 de la [matrice IA](../02-plugins-existants/exist-005-frictions-utilisateurs.md) : encore à découper, côté candidat/salarié, documentation d'indices de discrimination dans tri de CV, entretiens vidéo, diffusion d'offres ou critères de substitution ; lecture d'une évaluation algorithmique et contestation des effets professionnels. Conserver offre, candidature, écran/notice, réponse, indicateurs, statut et dates ; PRV-030/031 gardent surveillance et demande de données, IA-003/004 la qualification IA, DOM-037 le régime public après qualification. Ni PILOTE-002 ni TRAV-009 à 011, bornées à une enquête de harcèlement, ne couvrent ces démarches. Prévoir interlocuteur discrimination/emploi selon compétence vérifiée, preuves comparables minimales et calendrier propre. Cas attendus : refus de CV ne prouvant pas à lui seul une discrimination ; clic humain sans pouvoir de révision documenté ; évaluation contestée pendant une demande RGPD.

Ces exigences restent à découper ou préciser ; [portée et contrôles de l'intégration](../02-plugins-existants/exist-005-frictions-verification.md).

## Taille et contrôle des lots

Chaque story annonce des pièces, une sortie et un cas limite. Les tâches
qui produisent plusieurs formes d'un même résultat gardent un seul dossier
et un seul périmètre : TRAV-010 ajoute les pièces puis les interroge ;
TRAV-011 dérive une synthèse du même rapport. Elles n'autorisent ni collecte
ni diffusion générales. Si leur recette révèle deux procédures indépendantes,
les fractionner avant de les passer à `prete`.

Les futures implémentations devront charger la méthode BASE-005 locale et
fournir les résultats réels BASE-006. Un statut proposé, une référence à une
source primaire ou un scénario attendu ne vaut ni exécution ni validation juridique.

## Complément — formalités d'employeur

Les points 71–78 de la [matrice formalités](../02-plugins-existants/exist-002-frictions-utilisateurs.md) ajoutent TRAV-019 à TRAV-021, proposées, sans élargir le pilote livré. TRAV-019 concerne une TPE française ; TRAV-014/015 gardent l'employeur étranger et son suivi. TRAV-020 lit une notification DSN, sans moteur de paie ; TRAV-021 rapproche les documents d'une fin de contrat, sans contrôler tout motif de rupture.

Les points 91–93, 95 et 98 demandent aussi un futur découpage des décisions, contrôles, CRA, contraintes, remises, échéanciers et médiation Urssaf d'un employeur société. Ces recours sociaux ne sont pas implémentés par TRAV-020 ni transférés au cadrage micro-entreprise. Une identification urgente de l'acte peut relever d'ENF-001 ; le fond social et la voie spéciale gardent un propriétaire à découper dans travail.

## Complément des frictions données personnelles — 16 octobre 2026

Points 32–40 de la [matrice données personnelles](../02-plugins-existants/exist-003-frictions-utilisateurs.md) : PRV-001/022/024/025/030 portent accès, correction, effacement, limitation et fiche de surveillance. Travail garde les effets sur candidature, évaluation, sanction ou rupture et leurs délais ; emploi public → DOM-037 selon statut. TRAV-012/013 concernent la charte de télétravail, sans couvrir toute contestation de surveillance. Découper la lecture d'une sanction hors licenciement, la contestation d'un dispositif et les recours adaptés ; ces besoins ne sont pas couverts par le pilote. Scénarios attendus : horaires erronés avec délai de contestation indépendant ; images rapidement écrasées avec demande ciblée de préservation. Portée et contrôles : voir la matrice.
