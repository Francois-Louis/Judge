---
id: DOM-038
titre: "Cadrer un plugin violences intrafamiliales et protection"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-038 — Cadrer un plugin violences intrafamiliales et protection

## Objectif

Préparer des tâches adaptées aux personnes victimes de violences et aux proches qui les aident, en tenant compte de l'urgence et de la sécurité.

Nom de plugin proposé : `domestic-violence-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Identifier une demande de protection et préparer une orientation selon la situation réelle.
- Organiser une chronologie et des pièces existantes sans exposer la personne à un risque supplémentaire.
- Distinguer démarches de protection, plainte, logement, enfants et démarches sociales, avec un dossier principal et des relais précis.

## Qualification et frontières

Danger ou mesure en cours, canal de contact sûr, personnes concernées, enfants, décisions existantes et pièces disponibles ; limiter les questions aux besoins immédiats.

Le besoin de protection coordonne ce domaine ; la qualification pénale relève de DOM-002, la séparation et la parentalité de DOM-013, le logement de DOM-006 et les soins de DOM-007.

## Sources à prévoir et vérifier

Codes civil, pénal et de procédure applicables, textes de protection spécifiques, Justice et ressources gouvernementales dédiées.

- [Arrêtons les violences](https://arretonslesviolences.gouv.fr/)
- [Justice](https://www.justice.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Définir un parcours de préparation d'une demande de protection et de ses pièces, en réservant l'urgence immédiate à une orientation adaptée.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage prévoit un canal sûr et l'orientation urgente ; il n'impose ni confrontation, ni médiation, ni collecte risquée de preuves comme étape par défaut.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une personne doit préparer un dossier sans que l'auteur allégué accède aux échanges.
- Une décision concernant les enfants coexiste avec une mesure de protection.
- Un proche cherche comment aider sans décider à la place de la personne.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

