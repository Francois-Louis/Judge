---
id: ENF-004
titre: "S'orienter face à une saisie sur compte bancaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-004 — S'orienter face à une saisie sur compte bancaire

## Objectif et résultat attendu

Une personne dont le compte est saisi comprend la mesure, les sommes qui
peuvent rester disponibles selon la source lue, les démarches à vérifier et
les interlocuteurs.

## Périmètre et fichiers

- `enforcement-legal/skills/bank-seizure-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/saisie-compte.md` — mesures, sommes protégées, interlocuteurs, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Dénonciation ou avis de la banque ; émetteur ; titre visé ; comptes concernés ;
nature des sommes versées (salaire, prestations) ; date de la mesure.

## Sortie attendue

Nature de la mesure ; sommes à demander à la banque et justificatifs ;
contestation possible à vérifier et juge compétent à identifier, sans délai
calculé ; questions ; limites.

## Travail attendu

Distinguer saisie par commissaire de justice et saisie administrative à tiers
détenteur (régime propre, fond à DOM-011 ou DOM-002). Frais de la banque →
DOM-004. Plusieurs saisies ou dettes → DOM-024. Aucun conseil de vider ou
déplacer le compte.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, saisie-attribution et solde
insaisissable (pistes L211-1 et suivants, R162-2) ; juge de l'exécution
(piste L213-6 du Code de l'organisation judiciaire).

## Critères d'acceptation

- [ ] B01 explique la mesure et les sommes à demander, sans montant non sourcé.
- [ ] B02 distingue la saisie administrative et oriente le fond.

## Vérification

- Cas normal : B01 — Compte bloqué après une saisie-attribution ; prestations familiales versées sur ce compte.
- Cas limite : B02 — Saisie administrative à tiers détenteur pour une amende.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contestation rédigée, mainlevée, relations avec la banque au-delà de la
demande, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
