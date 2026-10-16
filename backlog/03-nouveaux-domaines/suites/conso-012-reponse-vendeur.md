---
id: CONSO-012
titre: "Répondre, comme petit vendeur, à la réclamation d'un client particulier"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-002]
---

# CONSO-012 — Répondre, comme petit vendeur, à la réclamation d'un client particulier

## Objectif et résultat attendu

Un artisan ou une TPE qui reçoit la réclamation d'un client particulier
comprend les obligations à vérifier et obtient un projet de réponse factuel.

## Périmètre et fichiers

- `consumer-legal/skills/seller-claim-response/SKILL.md` — le skill (à créer)
- `consumer-legal/references/reponse-vendeur.md` — grille de réponse et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

`garanties-legales.md` et `qualification-achat.md` sont relus, pas réécrits.

## Pièces et informations nécessaires

Réclamation reçue ; commande et facture ; CGV ; preuve de livraison ;
échanges ; état du bien retourné s'il l'est.

## Sortie attendue

Fiche ; obligations à vérifier ; distinction obligation légale et geste
commercial ; projet de réponse ; limites.

## Travail attendu

Client professionnel → commercial ; travaux → DOM-015. Un impayé d'un client
particulier est une tâche distincte, non proposée ici. Le projet de réponse
ne reconnaît ni ne conteste une responsabilité sans pièces.

## Références métier et sources à rechercher

Celles de CONSO-001, CONSO-002 et CONSO-003 selon la demande du client ;
aucune source propre au-delà de la grille de réponse.

## Critères d'acceptation

- [ ] Y01 distingue obligation à vérifier et geste commercial.
- [ ] Y02 relève la date d'achat et les faits qui décident d'une rétractation, sans conclure.

## Vérification

- Cas normal : Y01 — Atelier Nacre reçoit une plainte pour un carnet dont la reliure lâche.
- Cas limite : Y02 — Client qui demande un remboursement deux mois après l'achat, sans défaut allégué.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Recouvrement, contentieux, assurance du vendeur, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
