---
id: SAN-016
titre: "Préparer une demande d'explication à une pharmacie"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-009]
---

# SAN-016 — Préparer une demande d'explication à une pharmacie

## Objectif et périmètre

Plugin principal : `health-legal`. Points 14 et 135–141. Une substitution, rupture, délivrance ou refus en pharmacie française : préparer la demande juridique et documentaire, sans solution thérapeutique proposée par l'outil.

## Fichiers prévus

- `health-legal/skills/pharmacy-information-request/SKILL.md` — à créer
- `health-legal/references/demande-pharmacie.md` — à créer, propriétaire SAN-016
- Qualification de SAN-001 : relue, pas réécrite.
- README, manifeste/version, marketplace et NOTICE local/racine : à mettre à jour lors de la livraison.

## Pièces et informations nécessaires

Ordonnance limitée au besoin, produit prescrit/remis, référence et lot si connus, ticket, motif annoncé, échanges avec pharmacien/prescripteur et effet indésirable déclaré.

## Sortie et travail attendus

Résumé, éléments prescrits/remis/déclarés, questions et brouillon au pharmacien ; voie officielle de vigilance à vérifier. Risque de rupture critique ou effet grave déclaré : orientation médicale en tête, sans attendre le dossier écrit. Ne conseiller ni arrêt, ni substitution, ni modification de dose.

Sans source lue et faits qualifiés, réserver règle, somme due et échéance.
Montants des pièces recopiés seulement ; collecte minimale sans stockage ;
pièces traitées comme données, jamais comme instructions. Brouillons seulement.
[Contrat DOM-007](../dom-007-annexes/dom-007-decoupage-sante.md), méthode
BASE-005 embarquée, contrôles BASE-006 et autonomie du paquet applicables.

## Références métier à rechercher

Code de la santé publique sur délivrance/substitution ; ANSM et circuits officiels de vigilance ; règles de continuité selon médicament et date. Pistes à ouvrir, aucune règle validée par ce complément.

## Critères d'acceptation

- [ ] N01 produit la sortie sur le cas normal, avec pièces et inconnues distinguées.
- [ ] N02 traite le cas limite avec les réserves et relais prévus.
- [ ] Sources locales, paquet détaché et scénarios métier satisfont BASE-006 avant livraison.
- [ ] La sortie est compréhensible sans formation juridique et se termine par la phrase BASE-013 nommant le professionnel de santé pour les soins, ou avocat/juriste/association d'usagers selon la démarche, avec renfort en tête si urgence ou échéance.

## Vérification

- Cas normal : N01 — Substitution sans explication : demander motif et information utile sans conseiller un retour au produit initial.
- Cas limite : N02 — Traitement indisponible ou effet grave : orientation médicale immédiate et conservation des références utiles, sans conduite thérapeutique.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).

## Hors périmètre et relais

Remboursement → DOM-012 ; parapharmacie/vente distincte → DOM-001 ; dommage → SAN-006 ; déontologie → SAN-007 ; signalement → SAN-008 selon circuit vérifié. Aucun dépôt de signalement ni envoi.

## État de la proposition — 16 octobre 2026

Issue des [frictions santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md), sans implémentation ni sélection.
