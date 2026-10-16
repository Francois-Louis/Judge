---
id: CRIM-024
titre: "Repérer les points de régularité d'une procédure pénale à soumettre à l'avocat"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-024 — Repérer les points de régularité d'une procédure pénale à soumettre à l'avocat

## Objectif et résultat attendu

Une personne mise en cause, après une garde à vue, une perquisition, une
audition ou la réception d'un acte de poursuite, prépare pour son avocat la
liste factuelle des points de régularité à examiner, avec l'alerte sur le
moment où les nullités doivent être soulevées. Le skill ne conclut jamais à
une nullité. Ajout du 16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/procedure-points-review/SKILL.md` — le skill (à créer)
- `criminal-legal/references/regularite-procedure.md` — points à examiner, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Documents remis (procès-verbaux, notification des droits, convocation, acte
de poursuite) ; chronologie heure par heure déclarée ; avocat, interprète,
médecin demandés ou non ; perquisition ou saisie ; stade de la procédure.

## Sortie attendue

Chronologie factuelle ; tableau : point (horaire, notification, assistance,
autorisation, forme d'un acte), texte lu, constat (documenté, déclaré,
inconnu), question à l'avocat ; alerte en tête : selon le stade, les nullités
doivent être soulevées à un moment précis, souvent avant toute défense au
fond ; limites. Jamais « la procédure est nulle ».

## Travail attendu

Mesure encore en cours → CRIM-002. Amende contestée → CRIM-005. Violences
alléguées → CRIM-020 et CRIM-021. Ne pas suggérer de modifier un récit, de
mentir ou d'influencer un témoin.

## Références métier et sources à rechercher

Code de procédure pénale : garde à vue, audition, perquisition, notification
des droits, nullités et moment de leur présentation (pistes 63-1 et suivants,
171, 173, 385, 802) ; jurisprudence de la chambre criminelle sur le grief.

## Critères d'acceptation

- [ ] P01 produit chronologie et tableau sourcés, sans conclusion de nullité.
- [ ] P02 place l'alerte de moment en tête et nomme l'avocat.

## Vérification

- Cas normal : P01 — Garde à vue où l'avocat demandé serait arrivé après la première audition, selon le récit.
- Cas limite : P02 — Citation devant le tribunal correctionnel déjà reçue : alerte sur le moment de présentation, question à l'avocat.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Requête en nullité rédigée, défense au fond, évaluation des chances, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-annexes/dom-002-decoupage-penal.md).
