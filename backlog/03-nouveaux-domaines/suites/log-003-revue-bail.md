---
id: LOG-003
titre: "Relire un bail vide de résidence principale avant signature"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-003 — Relire un bail vide de résidence principale avant signature

## Objectif et résultat attendu

Un futur locataire comprend les engagements d'un projet de bail privé vide
en France métropolitaine et obtient des questions au bailleur avant signature.
La revue porte sur les clauses et annexes, sans audit de tout le logement.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/residential-lease-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/revue-bail-vide.md` — clauses, annexes, sources et réserves locales (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale fournie par LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Projet complet et annexes disponibles, date de signature envisagée, commune,
usage réel et qualité des parties ; clause de loyer/charges, dépôt et frais,
annonce si elle éclaire une contradiction. Aucun justificatif financier personnel requis.

## Sortie attendue

Résumé des engagements ; tableau clause/effet/source lue/question ou
proposition ; annexes absentes ; points territoriaux ou temporels réservés ;
questions au bailleur et prochaine étape avant signature.

## Travail attendu

Qualifier résidence principale, privé/vide et date avant toute analyse.
Repérer encadrement, diagnostics et clauses particulières à rechercher
localement ; sans texte local exact, réserver ces points, sans valider un
loyer. Cautionnement distinct à orienter ; justificatifs de candidature →
LOG-011 ; bail meublé ou commercial hors tranche. Une clause ne devient
pas valable du seul fait de sa signature.

## Références métier et sources à rechercher

Loi n° 89-462 du 6 juillet 1989, contrats types et annexes du régime vide,
Code civil, règles de frais et diagnostics ; textes locaux exacts si un
encadrement est allégué ; ANIL/ADIL. Versions, champ et transitions à ouvrir
lors du lot, sans validation générale de conformité.

## Critères d'acceptation

- [ ] B01 explique les clauses et demande les annexes utiles absentes.
- [ ] B02 réserve l'encadrement si la source locale manque ; B03 oriente le régime exclu.
- [ ] Sources locales chargées et paquet seul vérifiés selon BASE-006 ; absence de source explicitée dans la revue.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si signature imminente, délai ou procédure (BASE-013).

## Vérification

- Cas normal : B01 — Projet de bail vide et annexe manquante ; tableau accessible et questions avant signature.
- Cas limite : B02 — Annonce évoquant un encadrement sans arrêté fourni ni source accessible ; aucun loyer déclaré conforme.
- Cas limite : B03 — Bail meublé présenté comme vide ; relever la contradiction et réserver le régime.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Social/conventionné, meublé, commercial, saisonnier, cautionnement au fond,
calcul du loyer légal, négociation automatique, signature et envoi.
