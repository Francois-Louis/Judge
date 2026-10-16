---
id: ENF-010
titre: "Orienter un petit créancier qui détient un titre"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-010 — Orienter un petit créancier qui détient un titre

## Objectif et résultat attendu

Un particulier, un artisan ou une TPE qui a obtenu une décision de paiement
comprend ce qu'est un titre exécutoire, le rôle du commissaire de justice et
les pièces à lui remettre. Le skill ne lance aucune mesure.

## Périmètre et fichiers

- `enforcement-legal/skills/creditor-title-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/creancier-titre.md` — titres, étapes, pièces, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Décision ou acte invoqué ; formule exécutoire ; signification éventuelle ;
coordonnées connues du débiteur ; paiements reçus.

## Sortie attendue

Titre exécutoire ou non selon les mentions et la source lue ; étapes et
pièces pour le commissaire de justice ; frais à demander ; limites.

## Travail attendu

Sans titre → COM-015 (client professionnel) ou contentieux pour l'obtenir.
Ne pas choisir la mesure à la place du professionnel ni recommander de
rechercher soi-même des informations sur le débiteur par des moyens interdits.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, titres exécutoires (pistes L111-2,
L111-3) ; information officielle de la profession.

## Critères d'acceptation

- [ ] T01 identifie le titre et les pièces sans lancer de mesure.
- [ ] T02 oriente vers COM-015 ou le contentieux quand aucun titre n'existe.

## Vérification

- Cas normal : T01 — Artisan muni d'un jugement signifié contre un client.
- Cas limite : T02 — Facture impayée sans décision.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Choix et exécution de la mesure, recherche du débiteur, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
