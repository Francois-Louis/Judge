---
id: INS-004
titre: "Lire une garantie pour un événement donné"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-004 — Lire une garantie pour un événement donné

## Objectif et résultat attendu

Une personne qui se demande si son contrat couvre un événement identifie les
clauses pertinentes, les conditions, plafonds et franchises indiqués, et ce
qui manque pour répondre.

## Périmètre et fichiers

- `insurance-legal/skills/coverage-review/SKILL.md` — le skill (à créer)
- `insurance-legal/references/lecture-garantie.md` — méthode de lecture d'un contrat (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`lecture-garantie.md` est relu par INS-007, qui ne le réécrit pas.

## Pièces et informations nécessaires

Conditions générales et particulières en vigueur ; avenants ; description de
l'événement réel ou envisagé.

## Sortie attendue

Clauses pertinentes recopiées ; conditions ; plafonds et franchises lus ;
exclusions possibles à examiner ; pièces manquantes ; limites. Pas de verdict
« couvert » sans les conditions particulières.

## Travail attendu

Distinguer définition de la garantie, exclusion et condition. Une question
de devoir de conseil de l'intermédiaire est notée, sans analyse.

## Références métier et sources à rechercher

Code des assurances, information et mentions du contrat ; directive (UE)
2016/97 pour la distribution, selon la question.

## Critères d'acceptation

- [ ] L01 recopie les clauses et réserve la réponse aux pièces manquantes.
- [ ] L02 ne conclut pas « couvert » sur les seules conditions générales.

## Vérification

- Cas normal : L01 — « Mon assurance habitation couvre-t-elle un vélo volé dans le garage collectif ? »
- Cas limite : L02 — Conditions générales seules fournies.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Comparaison d'offres, conseil de souscription, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
