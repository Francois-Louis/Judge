---
id: INS-005
titre: "Escalader une réclamation d'assurance jusqu'au médiateur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-005 — Escalader une réclamation d'assurance jusqu'au médiateur

## Objectif et résultat attendu

Après un refus maintenu ou une absence de réponse, une personne identifie le
service réclamations puis le médiateur compétent, et prépare la saisine avec
les conditions à vérifier.

## Périmètre et fichiers

- `insurance-legal/skills/insurance-mediation/SKILL.md` — le skill (à créer)
- `insurance-legal/references/mediation-assurance.md` — étapes, médiateurs, rôle des autorités, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Réclamation et réponse ; dates ; médiateur indiqué au contrat ; organisme
(assureur, mutuelle, institution de prévoyance) ; procédure éventuelle.

## Sortie attendue

Étape suivante ; médiateur identifié selon l'organisme ou manque ; conditions
de recevabilité à vérifier ; question de prescription posée sans calcul ;
brouillon de saisine ; limites.

## Travail attendu

Accepter la sortie d'INS-001, INS-003 ou une réclamation fournie. Un
signalement à l'autorité de contrôle n'est pas présenté comme un recours.

## Références métier et sources à rechercher

Médiation de l'assurance et médiateurs des mutuelles et institutions de
prévoyance ; Code de la consommation, médiation ; prescription (pistes L114-1,
L114-2 du Code des assurances).

## Critères d'acceptation

- [ ] M01 prépare la saisine sans délai non sourcé.
- [ ] M02 identifie un médiateur différent pour une mutuelle.

## Vérification

- Cas normal : M01 — Refus maintenu après réclamation écrite.
- Cas limite : M02 — Refus d'une mutuelle santé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Procédure judiciaire, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
