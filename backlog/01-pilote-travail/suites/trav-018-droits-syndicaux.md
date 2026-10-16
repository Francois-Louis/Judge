---
id: TRAV-018
titre: "Expliquer les droits syndicaux d'un salarié du privé"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-003, BASE-005, BASE-006]
---

# TRAV-018 — Expliquer les droits syndicaux d'un salarié du privé

## Objectif

Un salarié du secteur privé en France comprend ses droits liés à l'adhésion
ou à l'activité syndicale (adhérer, être désigné ou élu, être protégé contre
une mesure liée à son engagement) et prépare les questions utiles. Ajout du
16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre

Plugin principal `employment-legal`, nouveau skill proposé `union-rights`
(`skills/union-rights/SKILL.md`) et ses repères métier embarqués. Entrées :
situation du salarié, entreprise et effectif connus, mandat envisagé ou
détenu, courrier ou décision reçus, faits datés. Sortie : explication des
droits à vérifier selon la situation, pièces à conserver, questions et
interlocuteurs (syndicat, représentant, inspection du travail, avocat).

## Travail attendu

- Distinguer adhésion, désignation syndicale et mandat électif ; ne pas
  présumer une protection sans mandat ou candidature établis.
- Mesure défavorable alléguée en lien avec l'engagement : récit factuel et
  pièces ; discrimination alléguée → question à DOM-029, sans conclusion.
- Emploi public → DOM-037. Fonctionnement interne d'une organisation
  syndicale : hors tranche.
- Lire le Code du travail (dispositions sur le droit syndical et les salariés
  protégés) et les textes collectifs applicables, avec versions ; charger la
  méthode locale BASE-005 et embarquer les repères nécessaires.

## Critères d'acceptation

- [ ] Le salarié distingue adhésion, désignation et mandat et sait ce qui reste à vérifier.
- [ ] Aucune protection n'est affirmée sans mandat ou candidature établis et source lue.
- [ ] La sortie nomme les pièces à conserver et un interlocuteur utile, sans verdict sur l'employeur.
- [ ] Paquet installé autonome et scénarios BASE-006 conservés ; un lecteur non juriste reformule droit, question et réserve.

## Vérification

Cas normal : salarié qui veut adhérer et se demande si son employeur doit
être informé. Limites : candidat aux élections professionnelles convoqué à un
entretien préalable ; agent d'une collectivité orienté vers DOM-037. Aucune
règle étrangère ni conclusion sur une discrimination.

## Hors périmètre

Contentieux, négociation collective, élections organisées par l'employeur,
fonctionnement des syndicats, envoi.

## Bilan d'exécution

Proposition du 16 octobre 2026 ; aucune adaptation réalisée. Les sources
restent à lire lors de la tranche explicitement choisie.
