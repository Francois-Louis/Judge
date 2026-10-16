---
id: VEH-003
titre: "Préparer une réclamation après une réparation défaillante ou une détérioration au garage"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-003 — Préparer une réclamation après une réparation défaillante ou une détérioration au garage

## Objectif et résultat attendu

Une personne dont la panne persiste ou réapparaît après une réparation, ou
qui constate une détérioration pendant la garde ou l'intervention,
reconstitue les faits, sait quelle question
technique reste ouverte, et obtient un brouillon de réclamation au garage.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/repair-failure-claim/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/reparation-defaillante.md` — inexécution, preuve, questions techniques, sources lues (à créer)
- `vehicle-legal/references/qualification-vehicule.md` — relue, créée par VEH-001
- `vehicle-legal/references/accords-travaux.md` — relue, créée par VEH-001
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Motif du dépôt, devis ou ordre de réparation, facture de l'intervention.
- Symptômes après la réparation, dates et kilométrage ; nouvelle intervention ailleurs.
- Diagnostic ou avis d'un autre professionnel ; pièces remplacées conservées ou non.
- Échanges avec le garage depuis la réparation.

## Sortie attendue

1. Résumé : ce qui était demandé, ce qui a été fait, ce qui est constaté.
2. Chronologie datée avec kilométrage.
3. Question technique ouverte, nommée sans être tranchée.
4. Pièces à réunir et état du véhicule à conserver.
5. Brouillon de réclamation demandant une reprise, une explication ou un examen contradictoire.
6. Suites : expertise amiable → VEH-010 ; facture → VEH-001 ; procédure → litigation.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `reparation-defaillante.md` et l'appliquer : aucune conclusion sur la
cause de la panne ni sur la qualité du travail ; la nature de l'obligation
du réparateur n'est affirmée qu'avec une source lue, jurisprudence comprise
selon BASE-015. Une réparation faite entre-temps par un autre garage est
signalée comme pouvant compliquer la preuve, sans conclure.

## Références métier et sources à rechercher

Code civil, inexécution (pistes 1217 et suivants) et contrat d'entreprise ;
nature de l'obligation du réparateur selon la jurisprudence à rechercher ;
pistes VEH-001.

## Critères d'acceptation

- [ ] P01 produit chronologie et réclamation sans attribuer la panne au garage.
- [ ] P02 signale l'intervention d'un autre garage et l'intérêt de l'expertise amiable.
- [ ] La sortie se termine par la phrase BASE-013 nommant un expert automobile pour la question technique et une association de consommateurs ou un avocat pour la démarche.

## Vérification

- Cas normal : P01 — Même voyant allumé quelques jours après le remplacement d'une pièce.
- Cas limite : P02 — Panne réparée entre-temps par un autre garage, ancienne pièce jetée.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Diagnostic technique, attribution de la cause, chiffrage d'un préjudice,
procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 10, 12–19, 25–27, 30–32, 163–169, 173, 179 et 195 de la [matrice](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Exigences supplémentaires du futur skill, sans implémentation.

- [ ] F01 — Essais de diagnostic successifs et panne répétée : tableau symptômes, mesures, codes, pièces, sous-traitant et coût annoncé ; demander justification technique sans faute déduite de la seule hypothèse erronée.
- [ ] F02 — Détérioration pendant garde/intervention, kilomètres inexpliqués, pneus, vitrage/ADAS ou carrosserie : comparer photos, références, compteur et rapports avant/après ; demander constat et explication au cocontractant sans attribuer causalité, responsabilité ou nécessité du calibrage depuis le récit.
- [ ] F03 — Clauses de limitation et proposition de geste contre quittance générale : citer clause et portée à vérifier ; transaction → CTX-039 ; préjudice documenté mais non chiffré → VEH-014, état → VEH-010. Sécurité en tête si freinage/direction ou capteur critique allégués.

Les cas F ci-dessus constituent les scénarios complémentaires **attendus, non exécutés**. Recueillir les pièces nommées, produire la comparaison et le brouillon prévus par la story ; sans source accessible, réserver droit, tarif, calendrier et effet de la clause. Rechercher les textes sectoriels et jurisprudence pertinents avec version, champ et dates ; le texte utilisateur n'est pas une source juridique. [Portée et vérification](../dom-023-annexes/dom-023-frictions-verification.md).
