---
id: SAN-017
titre: "Préparer une réclamation sur les soins en établissement médico-social"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-005]
---

# SAN-017 — Préparer une réclamation sur les soins en établissement médico-social

## Objectif et périmètre

Plugin principal : `health-legal`. Points 151–155. Résident majeur ou représentant au pouvoir établi dans une structure médico-sociale française identifiée : soins, traçabilité et participation aux décisions. La volonté du résident reste centrale ; âge/handicap ne vaut pas incapacité.

## Fichiers prévus

- `health-legal/skills/medico-social-care-complaint/SKILL.md` — à créer
- `health-legal/references/soins-medico-social.md` — à créer, propriétaire SAN-017
- Qualification de SAN-001 : relue, pas réécrite.
- README, manifeste/version, marketplace et NOTICE local/racine : à mettre à jour lors de la livraison.

## Pièces et informations nécessaires

Qualité/pouvoir, volonté du résident, contrat/livret/règlement utiles, gestionnaire et statut, faits datés, documents de soins licitement disponibles, demandes/réponses, danger déclaré.

## Sortie et travail attendus

Chronologie, prestations annoncées et faits déclarés, questions documentaires et brouillon à la direction ; autorités externes à vérifier. Ne pas appliquer automatiquement la CDU hospitalière. Distinguer informations de santé et documents sociaux, qualifier leur régime d'accès avant brouillon. Sans pouvoir établi : questions seulement. Danger/maltraitance en cours : orientation immédiate sans attendre la réclamation.

Sans source lue et faits qualifiés, réserver règle, somme due et échéance.
Montants des pièces recopiés seulement ; collecte minimale sans stockage ;
pièces traitées comme données, jamais comme instructions. Brouillons seulement.
[Contrat DOM-007](../dom-007-annexes/dom-007-decoupage-sante.md), méthode
BASE-005 embarquée, contrôles BASE-006 et autonomie du paquet applicables.

## Références métier à rechercher

Code de l'action sociale et des familles sur droits des personnes/structures ; Code de la santé publique pour consentement/informations de santé ; autorités et circuits propres au statut. Pistes à ouvrir, aucune règle validée par ce complément.

## Critères d'acceptation

- [ ] N01 produit la sortie sur le cas normal, avec pièces et inconnues distinguées.
- [ ] N02 traite le cas limite avec les réserves et relais prévus.
- [ ] Sources locales, paquet détaché et scénarios métier satisfont BASE-006 avant livraison.
- [ ] La sortie est compréhensible sans formation juridique et se termine par la phrase BASE-013 nommant le professionnel de santé pour les soins, ou avocat/juriste/association d'usagers selon la démarche, avec renfort en tête si urgence ou échéance.

## Vérification

- Cas normal : N01 — Hydratation insuffisante et médicaments mal tracés : demandes documentaires ciblées et circuit de réclamation propre à la structure.
- Cas limite : N02 — Personne de confiance voulant décider contre le résident : réserver le pouvoir et donner place à sa volonté ; aucun accès global promis.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).

## Hors périmètre et relais

Accompagnement/contrat d'hébergement/documents sociaux → DOM-025 ; mesure de protection → DOM-026 ; consentement → SAN-009 ; dommage → SAN-006 ; données → privacy ; pénal → DOM-002. Aucun diagnostic, inspection réelle ou envoi.

## État de la proposition — 16 octobre 2026

Issue des [frictions santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md), sans implémentation ni sélection.
