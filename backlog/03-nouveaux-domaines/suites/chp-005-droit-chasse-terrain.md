---
id: CHP-005
titre: "Préparer les questions d'un propriétaire sur la chasse sur son terrain"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, CHP-001]
---

# CHP-005 — Préparer les questions d'un propriétaire sur la chasse sur son terrain

## Objectif et périmètre

Un propriétaire qui souhaite que la chasse cesse sur son terrain obtient un
dossier des droits invoqués et une demande d'explication préalable. Plugin
proposé `hunting-fishing-legal`,
[contrat commun](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).
Ne pas rédiger d'opposition définitive sans régime établi.

## Entrées et pièces

Qualité du demandeur, commune, parcelle et titre utile masqué ; éventuelle
indivision, location, cession du droit de chasse ou convention ; nom et
nature de l'association (ACCA ou autre, à établir), statuts, actes locaux,
correspondance et dates. Motif et résultat souhaité exprimés par la personne,
sans lui suggérer de motif ni présumer ses pouvoirs sur tout le terrain.

## Sortie attendue

Fiche du terrain et des qualités, chronologie et tableau droit invoqué/pièce/
point à vérifier ; questions sur association, régime local, opposition ou
retrait, portée et destinataire à établir. Brouillon de demande de pièces
ou d'explication au détenteur allégué du droit ou au service identifié.
Aucun effet immédiat promis. Phrase BASE-013 nommant un avocat compétent
en droit de la chasse/foncier ; renfort si décision ou signature imminente.

## Travail et références métier

Créer `skills/hunting-land-rights-review/SKILL.md` et
`references/droit-chasse-terrain.md` ; charger qualification/méthode locales,
mettre à jour README, version, inventaire attendu et NOTICE. Lire Code de
l'environnement pour droit de chasse, ACCA, opposition/retrait ; actes locaux,
statuts, conventions et régime territorial pertinent. Distinguer droit de
chasse, passage et propriété. Sources absentes : établir les branches et
demander les actes, sans déduire un droit d'interdire de la seule propriété.

## Critères d'acceptation

- [ ] C02 produit un dossier et un brouillon préparatoire sans promettre l'arrêt de la chasse ni fixer un délai non sourcé.
- [ ] C12 réserve les pouvoirs du demandeur et le régime associatif/territorial ; aucun motif d'opposition inventé.
- [ ] Décision administrative/recours → DOM-010 ; vote/exclusion seul → DOM-032 ; voisinage → DOM-020 ; acte pénal → CHP-001/DOM-002.
- [ ] Sources/version, phrase BASE-013, décisions lues selon BASE-005 et recette client/autonomie du contrat commun vérifiées.

## Vérification prévue

- C02 : « Je ne veux plus que l'association chasse chez moi », seul titre
  de propriété fourni → demander actes et conventions, qualifier ACCA ou
  autre association, préparer les questions sans opposition réputée acquise.
- C12 : indivisaire recevant une demande de signature de retrait et terrain
  sous un régime local non documenté → pouvoirs et régime réservés, avocat
  nommé en tête, pas de signature conseillée.

## Hors périmètre et état

Opposition déposée, recours, conseil de clôture ou confrontation sur place,
résolution de propriété/indivision (DOM-020/DOM-016 selon objet). Proposition
non implémentée ; [portée](../dom-040-annexes/dom-040-verification.md#portée).
