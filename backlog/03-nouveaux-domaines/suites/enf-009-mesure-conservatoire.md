---
id: ENF-009
titre: "Lire une mesure conservatoire"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-009 — Lire une mesure conservatoire

## Objectif et résultat attendu

Une personne visée par une saisie conservatoire ou une sûreté judiciaire
comprend en quoi la mesure diffère d'une saisie d'exécution, ce qu'elle
bloque et les questions à poser.

## Périmètre et fichiers

- `enforcement-legal/skills/protective-measure-reading/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/mesures-conservatoires.md` — mesures, conditions à vérifier, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte ; autorisation du juge ou titre invoqué ; biens visés ; procédure au fond
engagée ou non.

## Sortie attendue

Fiche de la mesure ; différence avec une saisie d'exécution ; conditions et
suites à vérifier ; questions à un avocat ; limites.

## Travail attendu

Procédure au fond → contentieux. Bien immobilier : orientation avocat.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, mesures conservatoires (pistes L511-1
et suivants).

## Critères d'acceptation

- [ ] M01 distingue mesure conservatoire et saisie d'exécution.
- [ ] M02 oriente la sûreté sur un immeuble vers un avocat sans analyse.

## Vérification

- Cas normal : M01 — Saisie conservatoire sur compte d'un artisan, autorisation jointe.
- Cas limite : M02 — Hypothèque judiciaire provisoire sur une maison.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Mainlevée, procédure au fond, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
