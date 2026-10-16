---
id: BNK-005
titre: "Lire une offre de crédit"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-005 — Lire une offre de crédit

## Objectif et résultat attendu

Une personne qui reçoit une offre de crédit à la consommation ou immobilier
comprend ce qu'elle s'engage à payer, les conditions importantes et les
questions à poser avant de signer.

## Périmètre et fichiers

- `banking-legal/skills/credit-offer-reading/SKILL.md` — le skill (à créer)
- `banking-legal/references/credit.md` — types de crédit, mentions, droits à vérifier, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

`credit.md` est relu par BNK-007 et BNK-009, qui ne le réécrivent pas.

## Pièces et informations nécessaires

Offre complète ; fiche d'information précontractuelle ; tableau
d'amortissement ; assurance proposée ; achat financé (crédit lié) ; date de
réception.

## Sortie attendue

Fiche : prêteur, type, montant, durée, coût et taux recopiés, échéances,
conditions, crédit lié ou non ; questions avant signature ; droits à vérifier
(rétractation, assurance) ; limites. Aucun taux ni coût recalculé.

## Travail attendu

Assurance emprunteur → DOM-005. Achat financé → DOM-001 pour la vente.
Avant-contrat immobilier → DOM-017. Vérifier la version des textes à la date
de l'offre : le droit européen du crédit à la consommation évolue.

## Références métier et sources à rechercher

Code de la consommation, crédit à la consommation et immobilier (pistes L312-1
et suivants, L313-1 et suivants) ; directive (UE) 2023/2225, transposition et
date d'application à vérifier.

## Critères d'acceptation

- [ ] O01 produit la fiche avec montants recopiés et questions.
- [ ] O02 sépare crédit, vente et assurance.

## Vérification

- Cas normal : O01 — Offre de prêt personnel pour une voiture d'occasion.
- Cas limite : O02 — Crédit proposé en magasin pour une cuisine, assurance incluse.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Conseil d'achat, comparaison d'offres, simulation, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
