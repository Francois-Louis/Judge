---
id: BNK-006
titre: "Contester un prélèvement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-006 — Contester un prélèvement

## Objectif et résultat attendu

Une personne qui conteste un prélèvement sait s'il était autorisé par un
mandat, quelle demande adresser au prestataire et quelle question relève du
créancier.

## Périmètre et fichiers

- `banking-legal/skills/direct-debit-dispute/SKILL.md` — le skill (à créer)
- `banking-legal/references/prelevements.md` — mandat, demandes, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

`paiements.md` (BNK-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Relevé ; créancier et référence de mandat ; mandat signé ou non ; contrat
avec le créancier ; résiliation éventuelle ; dates.

## Sortie attendue

Prélèvement avec ou sans mandat ; demande au prestataire ; question au
créancier ; brouillon ; limites. Aucun délai calculé sans texte lu.

## Travail attendu

Contrat résilié mais prélèvement maintenu : volet créancier au domaine du
contrat (DOM-022, DOM-021, DOM-001). Opposition à de futurs prélèvements :
démarche à vérifier.

## Références métier et sources à rechercher

Code monétaire et financier (piste L133-25) ; règles SEPA.

## Critères d'acceptation

- [ ] D01 distingue prélèvement sans mandat et prélèvement autorisé contesté.
- [ ] D02 oriente le désaccord sur le contrat vers son domaine.

## Vérification

- Cas normal : D01 — Prélèvement d'un créancier inconnu.
- Cas limite : D02 — Abonnement résilié, prélèvements maintenus.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Litige avec le créancier, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
