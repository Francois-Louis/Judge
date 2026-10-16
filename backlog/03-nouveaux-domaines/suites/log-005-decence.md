---
id: LOG-005
titre: "Documenter un problème de décence et préparer une demande au bailleur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-005 — Documenter un problème de décence et préparer une demande au bailleur

## Objectif et résultat attendu

Le locataire d'un logement privé vide de résidence principale en France
métropolitaine documente un désordre précis et prépare sa demande.
Aucun diagnostic de non-décence ou d'insalubrité n'est prononcé.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/housing-decency-request/SKILL.md` — tâche (à créer)
- `housing-legal/references/decence-habitat.md` — critères, versions et autorités (à créer)
- `housing-legal/skills/housing-decency-request/references/demande-constat.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale de LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Bail, localisation précise, dates des faits, photos ciblées, diagnostics
disponibles avec version/date, description de l'humidité, chauffage ou autre
désordre, échanges et constat officiel éventuel. Décrire l'impact sans
collecter par défaut certificats médicaux ou données de santé du foyer.

## Sortie attendue

Fiche désordre/preuve/inconnue/critère à vérifier ; urgence éventuelle ;
demande de constat et d'intervention au bailleur ; organisme local ou
conseil à identifier ; limites et prochaine étape compréhensible.

## Travail attendu

Distinguer décence locative, insalubrité/péril et autorisation d'urbanisme.
Ne pas transformer un DPE ou une photo en décision d'inhabitabilité. Vérifier
les conditions énergétiques à la date et au lieu pertinents. Danger allégué :
mise en sécurité et interlocuteur compétent avant la revue ordinaire.
Travaux → DOM-015 pour le contrat ; autorisation publique → DOM-019 ;
prestation de caisse → DOM-012. Aucun droit à suspendre le loyer présumé.

## Références métier et sources à rechercher

Textes locatifs, Code de la construction et de l'habitation, décret
n° 2002-120 et modifications, critères énergétiques et dispositions
transitoires, prescriptions locales, pouvoirs des autorités ; ANIL/ADIL.
Vérifier texte officiel, territoire, régime et date avant toute application.

## Critères d'acceptation

- [ ] H01 documente humidité et inconnues sans conclure à l'insalubrité.
- [ ] H02 réserve un critère énergétique sans version ou territoire établi.
- [ ] Sans source, demander constat et pièces, réserver la règle ; paquet seul et références locales vérifiés selon BASE-006.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si enjeu irréversible, acte ou délai (BASE-013).

## Vérification

- Cas normal : H01 — Humidité récurrente et courrier sans réponse, photos disponibles ; demande ciblée sans diagnostic technique.
- Cas limite : H02 — Ancien DPE présenté comme preuve d'une interdiction actuelle ; vérifier version, date et territoire sans conclure.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Autres régimes locatifs, diagnostic médical ou technique, audit énergétique,
signalement déposé, décision administrative, indemnisation, saisine et envoi.
