---
id: ENF-011
titre: "S'orienter face à une saisie de biens ou de véhicule"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-011 — S'orienter face à une saisie de biens ou de véhicule

## Objectif et résultat attendu

Une personne dont des biens meubles ou le véhicule sont saisis comprend la
mesure, l'inventaire, les biens dont l'insaisissabilité est à vérifier et les
suites possibles.

## Périmètre et fichiers

- `enforcement-legal/skills/goods-seizure-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/saisie-biens.md` — mesures, biens protégés, suites, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Procès-verbal et inventaire ; titre visé ; biens appartenant à un tiers et
preuves ; usage professionnel d'un bien ; véhicule et papiers.

## Sortie attendue

Fiche de la mesure ; biens à discuter et preuves ; suites à vérifier ;
questions ; limites.

## Travail attendu

Bien d'un tiers : preuves de propriété à réunir, revendication à vérifier.
Ne jamais conseiller de déplacer ou cacher un bien saisi. Achat ou réparation
du véhicule → DOM-023.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, saisie-vente, biens insaisissables,
immobilisation du véhicule.

## Critères d'acceptation

- [ ] G01 produit la fiche et les biens à discuter sans conclusion.
- [ ] G02 traite le bien d'un tiers comme question de preuve.

## Vérification

- Cas normal : G01 — Saisie-vente au domicile, inventaire incluant un outil de travail.
- Cas limite : G02 — Véhicule immobilisé appartenant à un parent.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisie immobilière, contestation rédigée, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
