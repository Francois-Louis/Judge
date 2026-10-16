---
id: CRIM-013
titre: "Orienter une victime vers l'indemnisation de son préjudice"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-004]
---

# CRIM-013 — Orienter une victime vers l'indemnisation de son préjudice

## Objectif et résultat attendu

Une victime d'infraction comprend les voies d'indemnisation à vérifier
(constitution de partie civile, commission ou fonds d'indemnisation, aide au
recouvrement d'une condamnation) et réunit les pièces de la démarche qui la
concerne. Ajout du 16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/victim-compensation/SKILL.md` — le skill (à créer)
- `criminal-legal/references/indemnisation-victimes.md` — voies, conditions à vérifier, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`plainte.md` (CRIM-004) est relu, pas réécrit.

## Pièces et informations nécessaires

Récépissé de plainte ; décision pénale éventuelle ; nature des faits et du
préjudice ; justificatifs ; assurances ; auteur connu ou non, solvable ou non.

## Sortie attendue

Voies possibles à vérifier selon la situation ; pièces ; questions à un
avocat ou à une association d'aide aux victimes ; limites. Aucun montant ni
délai affirmé sans texte lu.

## Travail attendu

Chiffrage du préjudice → DOM-035. Accident de la circulation → DOM-035, selon
la [décision du 16 octobre 2026](../../decisions-2026-10-16.md). Garantie
d'assurance → DOM-005. Violences intrafamiliales : DOM-038 d'abord.

## Références métier et sources à rechercher

Code de procédure pénale, commission d'indemnisation des victimes et aide au
recouvrement (pistes 706-3 et suivants, 706-15-1) ; fonds de garantie
compétent, à identifier.

## Critères d'acceptation

- [ ] V01 distingue les voies et liste les pièces sans montant non sourcé.
- [ ] V02 oriente l'accident de la circulation vers DOM-035.

## Vérification

- Cas normal : V01 — Victime d'une agression, auteur condamné mais insolvable.
- Cas limite : V02 — Piéton blessé par un conducteur assuré.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisine de la commission, chiffrage, procédure, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-decoupage-penal.md).
