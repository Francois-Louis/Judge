---
id: CONSO-010
titre: "Réclamer pour un contenu ou service numérique non fourni ou défectueux"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-002]
---

# CONSO-010 — Réclamer pour un contenu ou service numérique non fourni ou défectueux

## Objectif et résultat attendu

Une personne qui a payé un contenu ou un service numérique (jeu, logiciel,
application, film) qu'elle ne peut pas utiliser obtient la fiche de son
achat, les pièces utiles et un brouillon de réclamation au fournisseur.

## Périmètre et fichiers

- `consumer-legal/skills/digital-content-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/contenus-numeriques.md` — régime et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

`garanties-legales.md` (CONSO-002) est relu, pas réécrit.

## Pièces et informations nécessaires

Preuve d'achat ; fournisseur et plateforme ; ce qui ne fonctionne pas et
depuis quand ; mises à jour ; échanges ; compte concerné.

## Sortie attendue

Fiche, pièces, brouillon de réclamation, limites.

## Travail attendu

Compte suspendu ou décision de modération → DOM-034, en tâche distincte.
Données → privacy. Bien avec éléments numériques → CONSO-002. Accès internet
ou mobile → DOM-022.

## Références métier et sources à rechercher

Code de la consommation, dispositions transposant la directive (UE)
2019/770, version à la date d'achat.

## Critères d'acceptation

- [ ] D01 produit fiche et brouillon sur pièces.
- [ ] D02 sépare la suspension de compte (DOM-034) et la réclamation d'achat.

## Vérification

- Cas normal : D01 — Jeu payé qui ne se lance plus après une mise à jour.
- Cas limite : D02 — Compte suspendu avec des achats inaccessibles.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contestation de modération, données personnelles, télécoms, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
