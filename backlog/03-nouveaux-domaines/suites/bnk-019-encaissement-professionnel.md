---
id: BNK-019
titre: "Comprendre les frais d'encaissement et les fonds commerçants retenus"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-019 — Comprendre les frais d'encaissement et les fonds commerçants retenus

## Objectif et résultat attendu

Un commerçant rapproche son contrat d'encaissement des commissions et retenues constatées et prépare une demande de justification ou de libération des fonds.

Besoin issu des frictions 94–95 de la [matrice utilisateur](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/merchant-settlement-review/SKILL.md` — le skill (à créer)
- `banking-legal/references/encaissement-professionnel.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Contrat d'acquisition ou de prestataire de paiement, location du terminal, grilles datées, relevés transactions/versements, réserves, rétrofacturations et demandes de pièces.

## Sortie attendue

Tableau transaction/commission/réserve/versement ; clauses invoquées ou manquantes ; demande détaillée de justification, de décompte ou de libération ; coût de résiliation à vérifier. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Séparer commission de transaction, abonnement, location, remboursement, rétrofacturation et réserve. Identifier le prestataire réellement détenteur des fonds. Blocage réglementaire → qualification BNK-014 ; frais du compte bancaire → BNK-003. Qualifier une garantie financière sans la présenter comme une pénalité illégale par principe.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, services de paiement et régime du prestataire ; contrat commerçant, règles privées d'acquisition et de réseau distinctes des plafonds des particuliers. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] Le rapprochement ventile commissions et versements et laisse les écarts inexpliqués comme questions documentées.
- [ ] La sortie identifie la clause de réserve ou son absence et demande les conditions de libération sans promettre le versement.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : ENC01 — Les versements du terminal ne correspondent pas au montant des ventes.
- Cas limite : ENC02 — Un prestataire retient une réserve après des rétrofacturations et demande des justificatifs.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Accès aux transactions, transfert de fonds, contestation de la vente au fond, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
