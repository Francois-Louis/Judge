---
id: CRIM-012
titre: "Demander un extrait de casier judiciaire et lire ses mentions"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-012 — Demander un extrait de casier judiciaire et lire ses mentions

## Objectif et résultat attendu

Une personne à qui un employeur ou un organisme demande un extrait de casier
sait quel bulletin elle peut obtenir et comment, et comprend les mentions
d'un extrait reçu.

## Périmètre et fichiers

- `criminal-legal/skills/criminal-record-request/SKILL.md` — le skill (à créer)
- `criminal-legal/references/casier.md` — bulletins, demande, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Qui demande l'extrait et pourquoi ; bulletin mentionné ; extrait reçu s'il
existe ; lieu de naissance (en France ou à l'étranger).

## Sortie attendue

Bulletin concerné et démarche à vérifier ; lecture des mentions d'un extrait ;
questions sur une éventuelle demande d'effacement, à poser à un avocat ;
limites.

## Travail attendu

Ne pas annoncer qu'une mention sera effacée ni qu'un employeur peut ou non
exiger un bulletin sans texte lu. Emploi public : question à DOM-037.

## Références métier et sources à rechercher

Code de procédure pénale, casier judiciaire et bulletins (pistes 768 et
suivants, 777) ; service officiel de demande en ligne.

## Critères d'acceptation

- [ ] R01 identifie le bulletin et la démarche à vérifier.
- [ ] R02 lit une mention sans promettre son effacement.

## Vérification

- Cas normal : R01 — Employeur privé demandant « un extrait de casier ».
- Cas limite : R02 — Extrait portant une condamnation ancienne que la personne croyait effacée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Requête en effacement ou en réhabilitation, relations avec l'employeur.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
