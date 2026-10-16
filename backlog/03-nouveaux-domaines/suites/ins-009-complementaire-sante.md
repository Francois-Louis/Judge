---
id: INS-009
titre: "Contester un refus de complémentaire santé ou de prévoyance"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-009 — Contester un refus de complémentaire santé ou de prévoyance

## Objectif et résultat attendu

Un adhérent dont la complémentaire santé ou la prévoyance refuse un
remboursement ou une prestation comprend le motif selon le régime de
l'organisme et prépare une demande.

## Périmètre et fichiers

- `insurance-legal/skills/health-cover-claim/SKILL.md` — le skill (à créer)
- `insurance-legal/references/sante-prevoyance.md` — régimes, garanties, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Tableau des garanties ; notice ; organisme (mutuelle, institution de
prévoyance, assureur) ; contrat individuel ou collectif ; décompte de
remboursement ; refus.

## Sortie attendue

Régime identifié ; garantie lue ; motif ; brouillon ; limites. Aucun
remboursement recalculé.

## Travail attendu

Part de l'assurance maladie → DOM-012. Obligations de l'employeur sur un
contrat collectif → employment. Soins → DOM-007.

## Références métier et sources à rechercher

Code de la mutualité ; Code de la sécurité sociale pour les institutions de
prévoyance ; règles des contrats responsables.

## Critères d'acceptation

- [ ] S01 identifie le régime de l'organisme avant de lire le refus.
- [ ] S02 sépare la part de l'assurance maladie.

## Vérification

- Cas normal : S01 — Mutuelle refusant des lunettes « hors période de renouvellement ».
- Cas limite : S02 — Décompte où la part de l'assurance maladie semble erronée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Prestations de sécurité sociale, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
