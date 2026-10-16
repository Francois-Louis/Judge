---
id: CRIM-014
titre: "Comprendre l'exécution d'une peine prononcée"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-006]
---

# CRIM-014 — Comprendre l'exécution d'une peine prononcée

## Objectif et résultat attendu

Une personne condamnée, ou un proche, comprend ce que la décision impose,
les convocations reçues (juge de l'application des peines, service
pénitentiaire d'insertion et de probation) et les questions à poser sur un
éventuel aménagement. Ajout du 16 octobre 2026
([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/sentence-execution/SKILL.md` — le skill (à créer)
- `criminal-legal/references/execution-peines.md` — acteurs, étapes, aménagements à vérifier, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Décision ; caractère définitif ou non ; convocations ; obligations prononcées ;
amendes ; situation familiale et professionnelle que la personne accepte de
communiquer.

## Sortie attendue

Fiche : peine, obligations, dates recopiées, acteurs ; aménagements à vérifier
avec un avocat ; pièces utiles ; limites. Aucune promesse d'aménagement ni
date de fin calculée.

## Travail attendu

Recours contre la décision → CRIM-006. Recouvrement d'une amende par saisie →
DOM-003. Ne jamais aider à se soustraire à une obligation ou à une convocation.

## Références métier et sources à rechercher

Code de procédure pénale, exécution des peines et application des peines
(pistes 707 et suivants, 712-1 et suivants) ; Code pénal pour les peines
prononcées.

## Critères d'acceptation

- [ ] E01 explique la décision et les convocations sans promesse.
- [ ] E02 oriente le recouvrement d'amende vers DOM-003.

## Vérification

- Cas normal : E01 — Convocation du service d'insertion et de probation après une condamnation avec sursis probatoire.
- Cas limite : E02 — Saisie sur compte pour une amende pénale ancienne.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Requête d'aménagement rédigée, détention, procédure, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-annexes/dom-002-decoupage-penal.md).
