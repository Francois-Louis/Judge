---
id: DOM-036
titre: "Cadrer un plugin retraites et droits de carrière"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-036 — Cadrer un plugin retraites et droits de carrière

## Objectif

Aider les personnes à comprendre leur relevé, une décision de pension et les informations à faire corriger.

Nom de plugin proposé : `pension-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Repérer les périodes ou données à vérifier dans un relevé de carrière.
- Lire une notification de pension, de réversion ou de régularisation.
- Préparer une demande de correction ou un recours auprès d'un régime identifié.

## Qualification et frontières

Régimes, périodes, statuts, relevés, décisions, pièces de carrière, dates et éventuel élément international.

La carrière et la retraite sont ici ; les autres prestations restent en DOM-012, le litige employeur dans le plugin travail et la fiscalité en DOM-011. La complémentaire, l'agricole et le public demandent des références propres. La retraite militaire reste ici ; les faits de service et la pension militaire d'invalidité relèvent de [DOM-044](dom-044-militaires-anciens-combattants.md).

## Sources à prévoir et vérifier

Code de la sécurité sociale et textes des régimes concernés, sources officielles Info Retraite, caisses et régimes complémentaires.

- [Info Retraite](https://www.info-retraite.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Préparer une demande de correction d'une période de carrière, dans un régime choisi et sur pièces fictives.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage distingue estimation, relevé et décision liquidant un droit ; aucun âge, taux ou montant n'est extrapolé sans régime et données vérifiés.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une période travaillée est absente du relevé.
- Une personne a cotisé sous plusieurs statuts.
- Un montant de pension diffère de ce que l'usager avait compris.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

