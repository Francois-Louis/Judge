---
id: CRIM-008
titre: "Structurer le récit d'un contrôle ou d'une fouille déjà subis"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-008 — Structurer le récit d'un contrôle ou d'une fouille déjà subis

## Objectif et résultat attendu

Une personne qui a subi un contrôle d'identité, une palpation ou une fouille
et le conteste structure son récit, ses preuves et les canaux de signalement
à vérifier. Le skill n'intervient pas pendant un contrôle en cours.

## Périmètre et fichiers

- `criminal-legal/skills/stop-account/SKILL.md` — le skill (à créer)
- `criminal-legal/references/controles.md` — types de contrôle, canaux, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Date, heure, lieu ; service ; ce qui a été demandé et fait ; durée déclarée ;
témoins ; documents remis ; préjudice déclaré.

## Sortie attendue

Récit chronologique ; distinction des mesures possibles ; canaux à vérifier
(inspection, Défenseur des droits, plainte) ; limites.

## Travail attendu

Ne pas qualifier le contrôle d'illégal. Discrimination alléguée : question
distincte à DOM-029. Pendant un contrôle en cours, rappeler seulement de
garder son calme et de noter les faits, sans consigne d'opposition.

## Références métier et sources à rechercher

Code de procédure pénale, contrôles et vérifications d'identité (pistes 78-2,
78-3) ; Code de la sécurité intérieure, déontologie ; compétences du
Défenseur des droits.

## Critères d'acceptation

- [ ] B01 produit récit et canaux à vérifier sans qualification.
- [ ] B02 isole la question de discrimination.

## Vérification

- Cas normal : B01 — Contrôle avec palpation à la sortie d'une gare.
- Cas limite : B02 — Contrôles répétés que la personne attribue à son origine.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Assistance pendant un contrôle, plainte rédigée, publication de vidéos.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
