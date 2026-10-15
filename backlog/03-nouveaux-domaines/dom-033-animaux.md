---
id: DOM-033
titre: "Cadrer un plugin animaux et responsabilités"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-033 — Cadrer un plugin animaux et responsabilités

## Objectif

Aider détenteurs, acquéreurs et personnes concernées par un animal à comprendre contrats et responsabilités.

Nom de plugin proposé : `animal-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un contrat de vente, cession, adoption, garde ou pension.
- Organiser une contestation sur les documents, la prestation ou l'état allégué de l'animal.
- Qualifier un incident ou signalement et orienter vers le domaine compétent.

## Qualification et frontières

Espèce, usage, détenteur/propriétaire, qualité du cédant, contrat, identification, dates et pièces vétérinaires strictement utiles.

Les règles propres à l'animal et à sa détention sont ici ; l'élevage professionnel se coordonne avec DOM-014, le voisinage avec DOM-020, l'assurance avec DOM-005 et la qualification pénale avec DOM-002.

## Sources à prévoir et vérifier

Code rural et de la pêche maritime, Code civil, Code pénal et règles locales ou spécifiques selon l'espèce et l'activité ; ministère de l'Agriculture.

- [Ministère de l'Agriculture](https://agriculture.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un contrat d'acquisition ou de pension pour une espèce et un contexte choisis.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage prévoit les régimes spécifiques de cession et d'espèce ; il ne transpose pas mécaniquement la garantie d'un bien courant et ne produit pas de diagnostic vétérinaire.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un vendeur n'a pas remis les documents attendus.
- Une pension facture des prestations contestées.
- Un animal cause un dommage pendant une garde.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

