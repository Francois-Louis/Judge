---
id: VEH-002
titre: "Lire des frais de gardiennage et s'orienter face à un véhicule retenu par le garage"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-002 — Lire des frais de gardiennage et s'orienter face à un véhicule retenu par le garage

## Objectif et résultat attendu

Une personne dont le garage garde le véhicule, ou qui reçoit une facture de
frais de gardiennage, comprend ce qui est réclamé, depuis quand et sur quelle
pièce, ce qui reste à établir sur le droit de garder le véhicule, et obtient
un brouillon de demande de restitution ou d'explication.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/garage-storage-retention/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/retention-gardiennage.md` — rétention, dépôt, information sur les frais, sources lues (à créer)
- `vehicle-legal/references/qualification-vehicule.md` — relue, créée par VEH-001
- `vehicle-legal/references/accords-travaux.md` — relue, créée par VEH-001
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Facture ou décompte de gardiennage ; affichage ou information reçue sur ces frais.
- Date de fin des travaux, date d'information de la personne, date de la demande de restitution.
- Facture des travaux et état du paiement ; contestation déjà formulée.
- Échanges avec le garage ; motif donné au refus de restituer.

## Sortie attendue

1. Résumé : véhicule retenu ou non, somme réclamée, motif invoqué.
2. Chronologie : dépôt, fin des travaux, information, demande de restitution, refus.
3. Tableau du gardiennage : période facturée, montant recopié, information préalable retrouvée.
4. Questions à établir sur le droit de garder le véhicule, avec la source lue ou réservées.
5. Brouillon de demande de restitution ou d'explication.
6. Suites : facture des travaux → VEH-001 ; saisie par un commissaire de justice → DOM-003 ; fourrière → DOM-010.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `retention-gardiennage.md` et l'appliquer : aucune affirmation
générale sur le droit de rétention ; la question est posée à partir des
pièces lues. Les jours de gardiennage ne sont pas recalculés à partir d'un
tarif supposé. Un véhicule indispensable au travail ou des frais qui
s'accumulent placent un renfort en tête. Paiement sous réserve évoqué comme
option à vérifier, sans conseil de payer ou de ne pas payer.

## Références métier et sources à rechercher

Code civil, droit de rétention (piste 2286) et dépôt (pistes 1915 et
suivants) ; information préalable sur les frais de gardiennage, texte à
identifier ; pistes VEH-001 pour la facture.

## Critères d'acceptation

- [ ] R01 reconstitue la chronologie et prépare une demande de restitution sans affirmer le droit du garage ni son absence.
- [ ] R02 distingue rétention par le garage, saisie et fourrière.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat, avec renfort en tête si le véhicule est retenu.

## Vérification

- Cas normal : R01 — Gardiennage facturé depuis la fin des travaux sans information préalable retrouvée.
- Cas limite : R02 — Véhicule enlevé sur la voie publique, la personne croyant à une rétention du garage.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Contestation des travaux eux-mêmes, saisie, fourrière, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
