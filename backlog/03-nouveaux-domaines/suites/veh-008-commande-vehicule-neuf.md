---
id: VEH-008
titre: "Préparer une demande au vendeur d'un véhicule neuf livré en retard ou différent de la commande"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-004]
---

# VEH-008 — Préparer une demande au vendeur d'un véhicule neuf livré en retard ou différent de la commande

## Objectif et résultat attendu

Un acheteur particulier d'un véhicule neuf dont la livraison tarde, dont le
versement d'avance est en jeu ou dont le véhicule livré diffère de la
commande compare commande, échanges et livraison, et obtient un brouillon de
demande au vendeur.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/new-vehicle-order-dispute/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/commande-vehicule-neuf.md` — délai, versements, conformité à la commande, sources lues (à créer)
- `vehicle-legal/references/vente-vehicule.md` — relue, créée par VEH-004
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Bon de commande, date ou délai de livraison indiqué, options et équipements commandés.
- Versement : montant recopié, libellé (arrhes, acompte, autre) ; financement lié.
- Échanges sur le retard ; procès-verbal de livraison et réserves éventuelles.

## Sortie attendue

1. Résumé : commande, retard ou écart, demande envisagée.
2. Tableau : élément commandé, élément livré ou date annoncée, écart.
3. Qualification conditionnelle du versement, sans conclusion tirée du seul libellé.
4. Brouillon de demande au vendeur : livraison, mise en conformité ou information.
5. Suites : crédit lié → DOM-004 ; défaut apparu après livraison → VEH-004 pour la garantie, VEH-011 pour le constructeur.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `commande-vehicule-neuf.md` et l'appliquer : aucun délai légal ni
droit d'annulation affirmé sans source lue ; un versement n'est pas qualifié
d'arrhes ou d'acompte sur la seule base du libellé. Réserves à la livraison
signalées comme pièce utile, sans affirmer leur effet.

## Références métier et sources à rechercher

Code de la consommation, délai de livraison (pistes L216-1 et suivants) et
versements d'avance (pistes L214-1 et suivants) ; conformité à la commande ;
pistes VEH-004.

## Critères d'acceptation

- [ ] N01 compare commande et date annoncée et prépare une demande sans délai légal non sourcé.
- [ ] N02 compare équipements commandés et livrés et laisse conditionnelle la qualification du versement.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat.

## Vérification

- Cas normal : N01 — Livraison repoussée plusieurs fois au-delà de la date du bon de commande.
- Cas limite : N02 — Véhicule livré sans une option payée, réserve non portée au procès-verbal.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Offre de crédit, garantie après livraison, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
