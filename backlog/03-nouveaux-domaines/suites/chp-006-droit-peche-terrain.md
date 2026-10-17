---
id: CHP-006
titre: "Préparer les questions sur le droit de pêche d'un riverain ou propriétaire"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, CHP-001]
---

# CHP-006 — Préparer les questions sur le droit de pêche d'un riverain ou propriétaire

## Objectif et périmètre

Un riverain ou propriétaire comprend les questions à établir sur la pêche
et l'accès à son terrain. Plugin proposé `hunting-fishing-legal`,
[contrat commun](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).
Le résultat est une fiche de droits et une demande d'information, sans
permission générale de pêcher ou d'empêcher le passage.

## Entrées et pièces

Qualité du demandeur, cours d'eau ou étang, commune, plan utile et titre,
connexion aux eaux décrite sans expertise inventée, classement ou acte
administratif disponible, conventions, bail de pêche, courriers de
l'association et objectif : pêcher, autoriser, refuser, comprendre un passage.

## Sortie attendue

Trois rubriques séparées : propriété et droits détenus ; régime des eaux et
droit de pêche ; accès/passage invoqué. Pour chacune : fait, pièce, inconnue,
source à lire et question. Brouillon ciblé à l'association/détenteur allégué
ou au service compétent. Carte et conditions de pratique → CHP-003 avec
les faits déjà établis. Phrase BASE-013 nommant un avocat en droit de la
pêche/foncier ; renfort si acte ou enjeu irréversible.

## Travail et références métier

Créer `skills/freshwater-land-rights-review/SKILL.md` et
`references/droit-peche-terrain.md` ; lire qualification/méthode locales,
actualiser README, version, inventaire attendu et NOTICE. Ouvrir Code de
l'environnement, dispositions sur régime des eaux, droits de pêche et
passage, actes de classement, titre et conventions applicables. S02 du
découpage sert au repérage. « Étang privé » ne détermine pas la qualification
d'eaux closes ; une photo seule ne suffit pas à résoudre cette question.
Sources indisponibles : maintenir les branches, demander l'acte pertinent.

## Critères d'acceptation

- [ ] C13 distingue droit de pêche et passage sans les déduire de la seule carte ou propriété.
- [ ] C14 conserve la qualification des eaux comme inconnue et n'écarte aucune règle à cause du seul mot « privé ».
- [ ] Classement/recours administratif → DOM-010 ; pollution/espèces → DOM-030 ; propriété/voisinage distinct → DOM-020 ; avis de contrôle → CHP-001.
- [ ] Sources/version, phrase BASE-013, lecture des décisions selon BASE-005 et recette client/autonomie du contrat commun vérifiées.

## Vérification prévue

- C13 : riverain recevant un courrier d'AAPPMA sur un passage, convention
  non jointe → demander titre invoqué et emprise, réserver le droit, préparer
  une demande d'explication sans entrave conseillée.
- C14 : propriétaire d'un étang relié à un ruisseau affirmant « privé donc
  sans carte » → relever les faits, demander classement/conventions et
  vérifier le régime, sans valider cette déduction.

## Hors périmètre et état

Expertise hydraulique, travaux, clôture, accès forcé, pêche professionnelle
et recours. Proposition non implémentée ;
[portée](../dom-040-annexes/dom-040-verification.md#portée).
