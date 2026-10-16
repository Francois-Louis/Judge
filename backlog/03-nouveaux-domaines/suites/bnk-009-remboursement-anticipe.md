---
id: BNK-009
titre: "Préparer un remboursement anticipé ou une renégociation de crédit"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-005]
---

# BNK-009 — Préparer un remboursement anticipé ou une renégociation de crédit

## Objectif et résultat attendu

Un emprunteur qui veut rembourser par anticipation ou renégocier comprend les
clauses du contrat, les frais possibles à vérifier et les questions à poser.

## Périmètre et fichiers

- `banking-legal/skills/credit-early-repayment/SKILL.md` — le skill (à créer)
- `banking-legal/references/remboursement-anticipe.md` — clauses, indemnités à vérifier, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

`credit.md` (BNK-005) est relu, pas réécrit.

## Pièces et informations nécessaires

Contrat ; tableau d'amortissement ; capital restant dû ; projet (vente,
rachat, renégociation).

## Sortie attendue

Clauses recopiées ; indemnités possibles à vérifier ; questions au prêteur ;
brouillon de demande de décompte ; limites. Aucun calcul d'indemnité.

## Travail attendu

Vente immobilière liée → DOM-017. Assurance emprunteur → DOM-005.

## Références métier et sources à rechercher

Code de la consommation, remboursement anticipé selon le type de crédit.

## Critères d'acceptation

- [ ] E01 recopie les clauses et prépare la demande de décompte.
- [ ] E02 sépare la vente du bien et le crédit.

## Vérification

- Cas normal : E01 — Remboursement anticipé partiel d'un crédit auto.
- Cas limite : E02 — Vente de la maison financée par un prêt immobilier.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Comparaison d'offres de rachat, calcul, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
