# PILOTE-001 — Découpage proposé de l'adaptation travail

Propositions du 15 octobre 2026, issues de l'[inventaire](pilote-001-releve-inventaire.md).
Le premier résultat reste la revue d'un contrat reçu par un candidat
dans [PILOTE-002](pilote-002-revue-embauche.md), puis sa validation
[PILOTE-003](pilote-003-bilan-pilote.md). La dépendance USAGE-002 est conservée :
l'audit ne remplace pas la priorisation des usages.

Les 16 stories ci-dessous sont `proposee`, priorité P2. Leurs implémentations
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
