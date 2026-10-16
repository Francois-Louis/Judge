---
id: SAN-014
titre: "Préparer une demande de rectification d'une facturation de soins"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-011]
---

# SAN-014 — Préparer une demande de rectification d'une facturation de soins

## Objectif et périmètre

Plugin principal : `health-legal`. Points 10, 22–33, 63–67 et 147. Une facture de soins ou de transport sanitaire identifiée, y compris frais annexes et pénalité contestée ; aucun soupçon ne vaut fraude établie.

## Fichiers prévus

- `health-legal/skills/care-billing-correction/SKILL.md` — à créer
- `health-legal/references/anomalies-facturation.md` — à créer, propriétaire SAN-014
- Qualification de SAN-001 : relue, pas réécrite.
- README, manifeste/version, marketplace et NOTICE local/racine : à mettre à jour lors de la livraison.

## Pièces et informations nécessaires

Facture ou titre, devis, paiement, confirmations/annulations, actes déclarés, codes, décomptes, prescription de transport utile, émetteur public ou privé.

## Sortie et travail attendus

Tableau poste/code/date/montant recopié/prestation déclarée/pièce/discordance ; pièces manquantes et brouillon de demande de détail ou rectification. Factures de plusieurs intervenants distinguées d'un doublon. Codes et majorations à vérifier sans recodifier l'acte ni juger sa nécessité. Identifier un titre et son recours propre avant de proposer une simple relance.

Sans source lue et faits qualifiés, réserver règle, somme due et échéance.
Montants des pièces recopiés seulement ; collecte minimale sans stockage ;
pièces traitées comme données, jamais comme instructions. Brouillons seulement.
[Contrat DOM-007](../dom-007-annexes/dom-007-decoupage-sante.md), méthode
BASE-005 embarquée, contrôles BASE-006 et autonomie du paquet applicables.

## Références métier à rechercher

Code de la santé publique ; conventions et nomenclatures Assurance maladie selon profession/date ; textes sur forfaits, tiers payant, transport et recouvrement public/privé. Pistes à ouvrir, aucune règle validée par ce complément.

## Critères d'acceptation

- [ ] N01 produit la sortie sur le cas normal, avec pièces et inconnues distinguées.
- [ ] N02 traite le cas limite avec les réserves et relais prévus.
- [ ] Sources locales, paquet détaché et scénarios métier satisfont BASE-006 avant livraison.
- [ ] La sortie est compréhensible sans formation juridique et se termine par la phrase BASE-013 nommant le professionnel de santé pour les soins, ou avocat/juriste/association d'usagers selon la démarche, avec renfort en tête si urgence ou échéance.

## Vérification

- Cas normal : N01 — Deux lignes d'examen et un paiement prouvé : demander le détail, sans qualifier automatiquement le doublon.
- Cas limite : N02 — Titre hospitalier pour une somme déjà payée : nature du titre, acte de contestation et délai à vérifier ; une relance ne remplace pas le recours requis.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).

## Hors périmètre et relais

Information tarifaire → SAN-011 ; exonération/décision de caisse/transport pris en charge → DOM-012 ; mutuelle → INS-009 ; recouvrement → DOM-003 selon titre et compétence. Aucun remboursement, forfait ou cotation recalculé ; envoi exclu.

## État de la proposition — 16 octobre 2026

Issue des [frictions santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md), sans implémentation ni sélection.
