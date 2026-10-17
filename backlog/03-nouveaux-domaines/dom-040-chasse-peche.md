---
id: DOM-040
titre: "Cadrer un plugin chasse et pêche de loisir"
statut: terminee
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

## Tâches métier découpées

- Lire un procès-verbal ou un avis de contravention lié à la chasse ou à la pêche et repérer infraction alléguée, agent, stade et pièces.
- Vérifier les documents d'une pratique : permis de chasser et validation, assurance obligatoire, carte de pêche et association agréée, règles locales.
- Préparer une demande sur le droit de chasser ou de pêcher sur un terrain : association de chasse, opposition du propriétaire, droit de pêche du riverain, étang privé.
- Documenter des dégâts de gibier et identifier la voie d'indemnisation à vérifier.

Le [découpage détaillé](dom-040-annexes/dom-040-decoupage-chasse-peche.md)
transforme ces axes en sept propositions CHP-001 à CHP-007, avec entrées,
pièces, sortie, limites et scénarios. Documents de chasse, pêche en eau
douce et formalités maritimes sont séparés, comme les droits de chasse et
de pêche sur un terrain.

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

- [x] Les tâches sont découpées en sept stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [x] Un utilisateur peut partir de son document sans connaître le texte applicable. *Parcours documentaires fictifs C01/C03/C09, relus par l'agent ; compréhension réelle non testée.*
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons avec CRIM-017, DOM-002, DOM-014 et DOM-030. *Contrat du futur paquet, sans installation.*
- [x] Aucune période, quota, taille ou montant n'est affirmé sans texte ni règle locale lus. *Cadrage sans règle chiffrée établie ; inconnues réservées.*
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici. *PILOTE-003 terminée après BASE-011 ; aucune suite sélectionnée.*

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

## Bilan d'exécution — 17 octobre 2026

Le [découpage](dom-040-annexes/dom-040-decoupage-chasse-peche.md) fixe le
propriétaire `hunting-fishing-legal`, le contrat autonome et les transmissions
aux domaines voisins. CHP-001 est la première tranche proposée, limitée à
une fiche d'acte après contrôle ; CHP-002 à CHP-007 préparent les autres
résultats, sans lancer de plugin. Les sept suites restent `proposee`.

La [vérification](dom-040-annexes/dom-040-verification.md) rapporte quinze
parcours documentaires, dont les quatre scénarios initiaux, et distingue
les contrôles de structure des recettes futures. Trois pages officielles
d'information ont été lues pour orienter les sources ; aucune règle locale
ou version de texte primaire n'est déclarée vérifiée. Le
[relevé technique](dom-040-annexes/dom-040-resultats.json) conserve les
résultats des contrôles du lot. L'index est régénéré avec la famille CHP.

**Portée :** voir la [portée de la vérification](dom-040-annexes/dom-040-verification.md#portée).
La relecture des livrables est prise en charge par l'utilisateur ; elle
n'est pas déclarée effectuée et ne maintient pas le cadrage ouvert.
