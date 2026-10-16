---
id: SAN-013
titre: "Préparer une demande d'accès ou de continuité des soins"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-005]
---

# SAN-013 — Préparer une demande d'accès ou de continuité des soins

## Objectif et périmètre

Plugin principal : `health-legal`. Points 1–15 et 150. Patient majeur agissant pour lui-même auprès d'un cabinet ou d'une structure de santé en France. Refus, annulation, fermeture ou rupture de suivi ; ni recherche effective de rendez-vous ni prise de rendez-vous.

## Fichiers prévus

- `health-legal/skills/care-access-request/SKILL.md` — à créer
- `health-legal/references/acces-continuite-soins.md` — à créer, propriétaire SAN-013
- Qualification de SAN-001 : relue, pas réécrite.
- README, manifeste/version, marketplace et NOTICE local/racine : à mettre à jour lors de la livraison.

## Pièces et informations nécessaires

Refus et confirmations, dates, canal de réservation, motif annoncé, suivi et traitement menacé déclarés, résultat recherché. Pas de dossier médical complet exigé.

## Sortie et travail attendus

Chronologie et brouillon demandant un rendez-vous, une explication ou un relais à un destinataire identifié. Séparer accès, continuité et discrimination alléguée. Si urgence médicale déclarée, orienter vers soignant ou secours en tête, sans attendre la lettre.

Sans source lue et faits qualifiés, réserver règle, somme due et échéance.
Montants des pièces recopiés seulement ; collecte minimale sans stockage ;
pièces traitées comme données, jamais comme instructions. Brouillons seulement.
[Contrat DOM-007](../dom-007-annexes/dom-007-decoupage-sante.md), méthode
BASE-005 embarquée, contrôles BASE-006 et autonomie du paquet applicables.

## Références métier à rechercher

Code de la santé publique : continuité, non-discrimination, déontologie selon profession ; ressources ARS, Assurance maladie et Défenseur des droits. Pistes à ouvrir, aucune règle validée par ce complément.

## Critères d'acceptation

- [ ] N01 produit la sortie sur le cas normal, avec pièces et inconnues distinguées.
- [ ] N02 traite le cas limite avec les réserves et relais prévus.
- [ ] Sources locales, paquet détaché et scénarios métier satisfont BASE-006 avant livraison.
- [ ] La sortie est compréhensible sans formation juridique et se termine par la phrase BASE-013 nommant le professionnel de santé pour les soins, ou avocat/juriste/association d'usagers selon la démarche, avec renfort en tête si urgence ou échéance.

## Vérification

- Cas normal : N01 — Cabinet fermé et suivi interrompu : demande de relais et dossier via SAN-001/004.
- Cas limite : N02 — Agenda complet mais consultation privée proposée : conserver les messages ; discrimination à qualifier en DOM-029, sans verdict.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).

## Hors périmètre et relais

Médecin traitant déclaré/remboursement → DOM-012 ; accessibilité → DOM-025 ; discrimination → DOM-029 ; abonnement de plateforme → DOM-001 ; délivrance → SAN-016. Aucun diagnostic, classement d'urgence, traitement ajusté ou rendez-vous garanti.

## État de la proposition — 16 octobre 2026

Issue des [frictions santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md), sans implémentation ni sélection.
