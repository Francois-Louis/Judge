---
id: INS-007
titre: "Mobiliser une garantie protection juridique"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-004]
---

# INS-007 — Mobiliser une garantie protection juridique

## Objectif et résultat attendu

Une personne qui a un litige vérifie si une garantie protection juridique
peut l'aider, ce qu'elle prend en charge selon le contrat et comment la
déclarer.

## Périmètre et fichiers

- `insurance-legal/skills/legal-expenses-cover/SKILL.md` — le skill (à créer)
- `insurance-legal/references/protection-juridique.md` — garanties, choix de l'avocat, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`lecture-garantie.md` (INS-004) est relu, pas réécrit.

## Pièces et informations nécessaires

Contrats détenus (habitation, carte bancaire, contrat dédié) ; nature et date
du litige ; démarches déjà faites ; avocat consulté ou non.

## Sortie attendue

Garanties possibles et conditions lues ; plafonds recopiés ; questions sur le
choix de l'avocat ; brouillon de déclaration ; limites.

## Travail attendu

Le litige lui-même reste à son domaine. Garantie attachée à une carte
bancaire : contrat d'assurance lu ici.

## Références métier et sources à rechercher

Code des assurances, protection juridique (pistes L127-1 et suivants).

## Critères d'acceptation

- [ ] J01 identifie la garantie et prépare la déclaration.
- [ ] J02 ne traite pas le litige de fond.

## Vérification

- Cas normal : J01 — Litige avec un artisan, contrat habitation avec option protection juridique.
- Cas limite : J02 — Demande d'analyser le litige avec l'employeur dans le même échange.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Analyse du litige, choix d'un avocat, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
