---
id: CRIM-004
titre: "Préparer les faits d'une plainte"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-004 — Préparer les faits d'une plainte

## Objectif et résultat attendu

Une victime prépare une chronologie claire, la liste de ses pièces et les
informations utiles avant de déposer plainte, et sait où la déposer selon
les sources lues. Le skill ne qualifie pas l'infraction et ne dépose rien.

## Périmètre et fichiers

- `criminal-legal/skills/complaint-preparation/SKILL.md` — le skill (à créer)
- `criminal-legal/references/plainte.md` — lieux de dépôt, contenu utile, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`plainte.md` est relu par CRIM-007, qui ne le réécrit pas.

## Pièces et informations nécessaires

Faits datés ; lieu ; auteur connu, inconnu ou supposé ; témoins ; preuves
(captures, messages, certificats, factures) ; préjudice déclaré ; démarches
déjà faites.

## Sortie attendue

Chronologie factuelle ; tableau des pièces (existe, à obtenir, à conserver) ;
infractions possibles à examiner, sans qualification ; lieux et modes de
dépôt à vérifier ; ce qu'il faut garder et ne pas modifier ; limites.

## Travail attendu

Violences intrafamiliales ou danger : DOM-038 d'abord, sans plainte préparée
ici en dehors d'une question bornée. Escroquerie avec paiement : remboursement
→ DOM-004, réclamation au vendeur → DOM-001, en tâches distinctes.
Harcèlement en ligne : signalement à la plateforme → DOM-034. Aucune
prescription calculée. Ne pas accuser une personne nommée au-delà des faits.

## Références métier et sources à rechercher

Code de procédure pénale, plainte et information de la victime (pistes 15-3,
40) ; directive 2012/29/UE ; service officiel de plainte ou de pré-plainte en
ligne en vigueur à la date du lot.

## Critères d'acceptation

- [ ] P01 produit chronologie et pièces sans qualification ni prescription.
- [ ] P02 sépare plainte, remboursement bancaire et réclamation au vendeur.
- [ ] P03 renvoie vers DOM-038 sans conduire de collecte exposante.

## Vérification

- Cas normal : P01 — Vol de vélo dans un local fermé, facture et photo disponibles.
- Cas limite : P02 — Faux site marchand, carte débitée, aucun vendeur identifiable.
- Cas limite : P03 — Menaces d'un ex-conjoint qui vit encore au domicile.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Dépôt de la plainte, constitution de partie civile, chiffrage du préjudice
(DOM-035), indemnisation par une commission ou un fonds, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
