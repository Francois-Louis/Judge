---
id: VEH-012
titre: "Préparer la réponse d'un vendeur particulier à la réclamation de l'acheteur du véhicule"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-005]
---

# VEH-012 — Préparer la réponse d'un vendeur particulier à la réclamation de l'acheteur du véhicule

## Objectif et résultat attendu

Un particulier qui a vendu son véhicule et reçoit une réclamation de
l'acheteur comprend ce qui lui est demandé, rassemble les pièces de la
vente, sait ce qui reste à établir, et obtient un brouillon de réponse
mesurée.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs. Story soumise au même arbitrage que VEH-005.

- `vehicle-legal/skills/private-seller-response/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/vente-entre-particuliers-vehicule.md` — relue, créée par VEH-005
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Réclamation reçue et sa date ; annonce publiée ; échanges avant la vente.
- Certificat de cession et preuve de son enregistrement ; contrôle technique remis.
- Factures d'entretien et de réparation connues du vendeur ; clause d'exclusion éventuelle.

## Sortie attendue

1. Résumé : ce que l'acheteur demande et sur quel fondement apparent.
2. Pièces de la vente classées : remises, déclarées, manquantes.
3. Points à établir, sans conclure à l'absence de responsabilité.
4. Brouillon de réponse demandant précisions et pièces, ou proposant un examen contradictoire.
5. Suites : expertise → VEH-010 ; amendes reçues après la cession → DOM-002 (CRIM-005) ; assignation reçue → litigation (CTX-025).
6. Limites et phrase BASE-013.

## Travail attendu

Appliquer `vente-entre-particuliers-vehicule.md` du point de vue du
vendeur : l'acheteur n'est pas présumé de mauvaise foi, le vendeur n'est pas
présumé à l'abri ; aucune clause d'exclusion présentée comme décisive sans
source lue.

## Références métier et sources à rechercher

Pistes VEH-005 ; clause d'exclusion de garantie et bonne foi du vendeur, à
rechercher.

## Critères d'acceptation

- [ ] S01 classe les pièces et prépare une réponse mesurée sans écarter la réclamation par principe.
- [ ] S02 oriente une assignation reçue vers litigation avec renfort en tête.
- [ ] La sortie se termine par la phrase BASE-013 nommant un avocat ou une association de consommateurs, avec renfort en tête en cas de procédure.

## Vérification

- Cas normal : S01 — Acheteur invoquant un défaut caché plusieurs semaines après la vente.
- Cas limite : S02 — Vendeur recevant une assignation sans réclamation préalable.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Défense en justice, amendes, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
