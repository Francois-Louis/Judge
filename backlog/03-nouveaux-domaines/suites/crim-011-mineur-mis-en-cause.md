---
id: CRIM-011
titre: "Orienter les parents d'un mineur mis en cause"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-011 — Orienter les parents d'un mineur mis en cause

## Objectif et résultat attendu

Les parents ou représentants d'un mineur convoqué, retenu ou poursuivi
comprennent le régime propre aux mineurs, leur place dans la procédure et les
questions à poser à un avocat.

## Périmètre et fichiers

- `criminal-legal/skills/minor-orientation/SKILL.md` — le skill (à créer)
- `criminal-legal/references/mineurs.md` — régime, rôle des représentants, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Âge et date de naissance ; acte ou mesure ; autorité ; lien de la personne qui
écrit avec le mineur ; avocat désigné ; mesure éducative existante.

## Sortie attendue

Fiche ; spécificités du régime à vérifier ; place des représentants ;
questions ; limites. Mesure en cours : bloc d'urgence de CRIM-002 adapté.

## Travail attendu

Ne pas appliquer les repères des majeurs. Conflit entre parents ou
assistance éducative : question à DOM-013, sans la traiter ici. École : DOM-027.

## Références métier et sources à rechercher

Code de la justice pénale des mineurs ; directive (UE) 2016/800.

## Critères d'acceptation

- [ ] N01 n'applique aucun repère des majeurs et nomme l'avocat.
- [ ] N02 sépare la sanction scolaire et la procédure pénale.

## Vérification

- Cas normal : N01 — Convocation d'un adolescent de quinze ans pour des dégradations.
- Cas limite : N02 — Exclusion du collège et convocation au commissariat pour les mêmes faits.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Assistance éducative, procédure scolaire, défense au fond.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-annexes/dom-002-decoupage-penal.md).
