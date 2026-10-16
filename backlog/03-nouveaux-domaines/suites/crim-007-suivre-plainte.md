---
id: CRIM-007
titre: "Lire la suite donnée à une plainte"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-004]
---

# CRIM-007 — Lire la suite donnée à une plainte

## Objectif et résultat attendu

Une victime qui reçoit un avis de classement, une proposition d'alternative
ou aucune nouvelle comprend la décision et les options à vérifier.

## Périmètre et fichiers

- `criminal-legal/skills/complaint-follow-up/SKILL.md` — le skill (à créer)
- `criminal-legal/references/suites-plainte.md` — décisions possibles, options, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`plainte.md` (CRIM-004) est relu, pas réécrit.

## Pièces et informations nécessaires

Récépissé de plainte ; avis reçu et sa date ; motif indiqué ; démarches
faites depuis.

## Sortie attendue

Décision lue en langage clair ; options à vérifier (recours, constitution de
partie civile, citation) avec conditions ; questions à un avocat ; limites.
Aucun délai calculé.

## Travail attendu

Absence de nouvelles : préparer une demande d'information au parquet à
vérifier, sans interpréter le silence. Ne pas présenter une option comme
promettant une poursuite.

## Références métier et sources à rechercher

Code de procédure pénale, avis à la victime, recours contre le classement,
constitution de partie civile (pistes 40-2, 40-3, 85).

## Critères d'acceptation

- [ ] L01 explique le motif de classement et les options à vérifier.
- [ ] L02 n'interprète pas l'absence de réponse.

## Vérification

- Cas normal : L01 — Avis de classement « auteur inconnu » après un vol.
- Cas limite : L02 — Aucune nouvelle huit mois après la plainte.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Rédaction de la plainte avec constitution de partie civile, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
