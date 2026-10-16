---
id: BNK-004
titre: "Escalader une réclamation bancaire jusqu'au médiateur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-004 — Escalader une réclamation bancaire jusqu'au médiateur

## Objectif et résultat attendu

Après une réponse insatisfaisante ou une absence de réponse, une personne
identifie l'étape suivante (service réclamation, médiateur) et prépare la
saisine, avec les conditions à vérifier.

## Périmètre et fichiers

- `banking-legal/skills/bank-mediation/SKILL.md` — le skill (à créer)
- `banking-legal/references/mediation-bancaire.md` — étapes, médiateurs, rôle des autorités, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Réclamation et réponse ; dates ; médiateur indiqué par la convention ;
qualité du client ; procédure judiciaire éventuelle.

## Sortie attendue

Étape suivante ; médiateur identifié ou manque ; conditions de recevabilité à
vérifier, y compris pour un client professionnel ; brouillon de saisine ;
signalement possible à l'autorité de contrôle présenté comme distinct d'un
recours ; limites.

## Travail attendu

Accepter la sortie de BNK-001, BNK-002 ou BNK-003, ou une réclamation fournie.
Placement → médiateur à vérifier en BNK-011. Assurance → DOM-005.

## Références métier et sources à rechercher

Code monétaire et financier, médiation bancaire (piste L316-1) ; Code de la
consommation, médiation ; rôle de l'ACPR et d'ABE Infoservice.

## Critères d'acceptation

- [ ] M01 prépare la saisine sans délai non sourcé.
- [ ] M02 laisse ouverte la recevabilité pour un client professionnel.

## Vérification

- Cas normal : M01 — Refus écrit de rembourser une opération contestée.
- Cas limite : M02 — Artisan sans réponse à une réclamation sur ses frais.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Procédure judiciaire, envoi de la saisine.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
