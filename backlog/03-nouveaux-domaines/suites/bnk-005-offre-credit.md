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

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 56, 58, 62–63 et 78 de la [matrice](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

- [ ] O03 — Crédit renouvelable présenté par sa seule mensualité : distinguer capital, amortissement, intérêts, TAEG, total annoncé et assurance, à partir des documents sans recalcul.
- [ ] O04 — Assurance externe et frais de dossier : rapprocher clause, consentement et frais ; séparer lecture de l'offre et substitution INS-008.
- [ ] O05 — Crédit proposé pour payer les frais d'incident : relever les dettes et orienter la situation globale vers DOM-024 sans recommander de nouveau financement.

Pièces : contrat renouvelable, relevé de situation et détail des frais et assurances. Scénarios O03–O05 **attendus, non exécutés**. Les bornes de lecture et d'absence de simulation restent celles de cette story.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-annexes/dom-004-decoupage-banque.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 85, 116–120, 125, 128–130 ; tableau §11 de la [matrice véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md).

- [ ] AUTO01 — Qualifier LOA, crédit affecté et LLD sans option avant lecture des droits ; en LLD → VEH-018. Recopier premier versement, dépôt, loyers, option, entretien et frais/assurances annoncés ; demander coût total et postes absents sans simulation ni comparaison d'offres.
- [ ] AUTO02 — Dater acceptation, demande de livraison anticipée et livraison ; distinguer échéances de financement et vente, source/version et événement de départ. Aucun délai extrait du guide ni disparition automatique d'un contrat depuis l'autre.
- [ ] AUTO03 — Sortie anticipée LOA : identifier clause, décompte et question ; la demande au fond et la notification de rétractation restent à découper en DOM-004. BNK-005 garde sa borne de lecture et de questions ; VEH-009 traite les frais de restitution matérielle.

Pièces : contrat complet et annexes, publicité, coûts annoncés, consentements et dates prouvées. Cas attendus : mensualité seule avec option omise ; premier loyer présenté comme dépôt ; livraison anticipée et deux calendriers. Scénarios **attendus, non exécutés** ; textes applicables et transitions du crédit à vérifier, aucun coût recalculé.

[Portée et vérification documentaire](../dom-023-annexes/dom-023-frictions-verification.md) ; aucune implémentation ni droit validé par ce complément.
