---
id: DOM-040
titre: "Cadrer un plugin chasse et pêche de loisir"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-040 — Cadrer un plugin chasse et pêche de loisir

## Objectif

Aider un chasseur, un pêcheur ou un propriétaire à comprendre ce que la
pratique exige, à lire un procès-verbal ou un avis reçu et à préparer une
démarche sur le droit de chasser ou de pêcher sur un terrain ou les dégâts de
gibier. Ajouté le 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

Nom de plugin proposé : `hunting-fishing-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un procès-verbal ou un avis de contravention lié à la chasse ou à la pêche et repérer infraction alléguée, agent, stade et pièces.
- Vérifier les documents d'une pratique : permis de chasser et validation, assurance obligatoire, carte de pêche et association agréée, règles locales.
- Préparer une demande sur le droit de chasser ou de pêcher sur un terrain : association de chasse, opposition du propriétaire, droit de pêche du riverain, étang privé.
- Documenter des dégâts de gibier et identifier la voie d'indemnisation à vérifier.

## Qualification et frontières

Pratique (chasse, pêche en eau douce, pêche maritime de loisir), qualité de
la personne (pratiquant, propriétaire, riverain, victime), lieu, date,
documents détenus, agent verbalisateur et acte reçu.

La pratique de loisir est ici. Détention et transport d'une arme →
CRIM-017 ; procédure pénale au-delà de la lecture de l'acte → DOM-002 ;
exploitation agricole, élevage et dégâts aux cultures d'un exploitant →
DOM-014 ; animal domestique → DOM-033 ; protection des espèces et pollution
→ DOM-030 ; nuisances de voisinage → DOM-020 ; garantie d'assurance →
DOM-005 ; dommage corporel d'un accident de chasse → DOM-035. La pêche
professionnelle n'est pas couverte par ce cadrage.

## Sources à prévoir et vérifier

Code de l'environnement (chasse, pêche en eau douce), Code rural et de la
pêche maritime (pêche maritime de loisir), arrêtés préfectoraux et règles
fédérales ; Office français de la biodiversité et fédérations comme sources
d'information.

Les guides orientent le cadrage ; les textes et versions applicables seront
vérifiés lors de chaque implémentation, y compris les règles locales.

## Première tranche proposée

Lire un procès-verbal ou un avis reçu après un contrôle de chasse ou de pêche
et repérer infraction alléguée, stade, pièces et interlocuteur.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son document sans connaître le texte applicable.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons avec CRIM-017, DOM-002, DOM-014 et DOM-030.
- [ ] Aucune période, quota, taille ou montant n'est affirmé sans texte ni règle locale lus.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un chasseur verbalisé alors que sa validation annuelle n'était pas à jour.
- Un propriétaire qui ne veut plus que l'association de chasse passe sur son terrain.
- Un pêcheur verbalisé pour la taille d'une prise, règle locale non fournie.
- Un jardin retourné par des sangliers.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas
résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, pêche professionnelle, conseils de pratique ou
d'équipement, aide à contourner une règle de chasse ou de pêche.
