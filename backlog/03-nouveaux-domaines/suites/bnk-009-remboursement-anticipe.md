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

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 59–61 de la [matrice](../dom-004-frictions-utilisateurs.md).

- [ ] E03 — Renégociation : tableau des montants annoncés pour capital, intérêts restants, frais d'avenant, garanties et assurance ; pièces manquantes et coût total restant à demander, sans comparaison d'offres ni simulation.
- [ ] E04 — Indemnité contestée : demander capital, montant remboursé, clause, décompte et fondement des limites ; aucune indemnité recalculée.
- [ ] E05 — Vente liée à un événement professionnel ou familial : recueillir événement, dates, lien avec la vente et justificatifs pour vérifier l'exonération selon le régime du prêt.

Scénarios E03–E05 **attendus, non exécutés** : proposition à taux moindre mais frais absents, indemnité globale non détaillée, vente après cessation d'activité. Sources : remboursement anticipé et exonérations propres au type et à la date du crédit. Cette tranche prépare les vérifications ; elle ne promet pas de valider le montant.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
