---
id: CHP-003
titre: "Lire une carte de pêche et les documents du secteur en eau douce"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, CHP-001]
---

# CHP-003 — Lire une carte de pêche et les documents du secteur en eau douce

## Objectif et périmètre

Un pêcheur comprend ce que ses documents établissent et ce qui manque pour
sa pratique à un endroit donné. Plugin proposé `hunting-fishing-legal`,
[contrat commun](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).

## Entrées et pièces

Carte, association agréée de pêche et de protection des milieux aquatiques
(AAPPMA) indiquée, justificatifs/options, réciprocité invoquée, règlement,
autorisation et arrêté fournis. Commune et cours d'eau/plan d'eau, date,
pratique et espèce recherchée, statut de loisir. Sans carte ou sans nom du
cours d'eau, commencer la liste des inconnues sans refuser toute aide.

## Sortie attendue

Tableau carte et options/secteur et dates portés/droit invoqué/règle à
vérifier ; liste des sources locales manquantes et demande d'explication à
l'association ou fédération compétente. Distinguer adhésion, documents de
pratique, réciprocité et autorisation sur le lieu. Aucune période, taille,
quota ni prix donné sans source exacte. Phrase finale BASE-013 nommant un
juriste ou avocat compétent, renfort pour acte ou mesure reçu.

## Travail et références métier

Créer `skills/freshwater-fishing-document-check/SKILL.md` et
`references/documents-peche-eau-douce.md` ; lire qualification et méthode
locales, mettre à jour README, version, inventaire attendu et NOTICE.
Rechercher Code de l'environnement (conditions d'exercice, organisation
agréée), classement des eaux, arrêtés préfectoraux, documents d'association
et conventions invoquées. S02 du découpage aide au repérage, sans remplacer
les textes. Le mot « privé » ne tranche pas le régime des eaux ; ne pas
certifier la légalité de la pêche à partir de la seule carte.

## Critères d'acceptation

- [ ] C07 explique les mentions de la carte et réserve le secteur/réciprocité non établis, sans conclure à une infraction.
- [ ] C08 réserve taille et période faute d'arrêté ; association et préfecture sont distinguées comme sources.
- [ ] Propriété, étang et accès aux berges → CHP-006 ; avis reçu → CHP-001 ; pollution/espèce protégée → DOM-030 ; pêche professionnelle exclue.
- [ ] Sources/version, phrase BASE-013, lecture des décisions selon BASE-005 et contrôles d'autonomie/recette client du contrat commun sont vérifiés.

## Vérification prévue

- C07 : carte avec option de réciprocité, lac non identifié dans les pièces
  → demander localisation et convention, produire les questions ciblées.
- C08 : capture projetée sur une rivière connue mais arrêté non fourni
  → retrouver la règle locale ou réserver taille/période, sans valeur nationale
  appliquée par défaut. Si un avis existe, passer d'abord à CHP-001.

## Hors périmètre et état

Vente de carte, conseils de capture, certification d'un site et recours.
Proposition non implémentée ;
[portée](../dom-040-annexes/dom-040-verification.md#portée).
