---
id: ENF-008
titre: "Demander un échéancier ou des délais de paiement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-002]
---

# ENF-008 — Demander un échéancier ou des délais de paiement

## Objectif et résultat attendu

Une personne qui reconnaît une dette mais ne peut la régler en une fois
prépare une demande d'échéancier au créancier ou à son mandataire, et
comprend les autres options à vérifier.

## Périmètre et fichiers

- `enforcement-legal/skills/payment-plan-request/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/delais-paiement.md` — options, justificatifs, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

`recouvrement-amiable.md` (ENF-002) est relu, pas réécrit.

## Pièces et informations nécessaires

Dette et justificatifs ; ressources et charges que la personne accepte de
communiquer ; propositions déjà faites ; titre éventuel.

## Sortie attendue

Brouillon de proposition d'échéancier ; justificatifs à joindre ; options à
vérifier (délais judiciaires, surendettement) ; limites. Le brouillon ne
reconnaît que ce que la personne confirme.

## Travail attendu

Plusieurs dettes ou impossibilité durable → DOM-024. Ne pas présenter un
accord comme obtenu ni une option judiciaire comme acquise.

## Références métier et sources à rechercher

Code civil, délais de grâce (piste 1343-5) ; information sur le
surendettement pour l'orientation.

## Critères d'acceptation

- [ ] P01 produit un brouillon fondé sur ce que la personne confirme.
- [ ] P02 oriente vers DOM-024 quand plusieurs dettes sont en jeu.

## Vérification

- Cas normal : P01 — Dette reconnue, proposition de versements mensuels.
- Cas limite : P02 — Cinq créanciers et une saisie en cours.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisine du juge, dossier de surendettement, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
