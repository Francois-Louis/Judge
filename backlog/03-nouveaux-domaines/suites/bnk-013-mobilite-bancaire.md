---
id: BNK-013
titre: "Suivre une mobilité bancaire et ses incidents"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-013 — Suivre une mobilité bancaire et ses incidents

## Objectif et résultat attendu

Un titulaire qui change de banque obtient le suivi des opérations transférées, des anomalies et des demandes de correction, sans confondre mobilité et clôture.

Besoin issu des frictions 21, 47–49 de la [matrice utilisateur](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/bank-switch-follow-up/SKILL.md` — le skill (à créer)
- `banking-legal/references/mobilite.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Mandat de mobilité, dates de réception et d'exécution, relevés des deux comptes, liste des opérations récurrentes et chèques encore en circulation, courriers des créanciers et frais subis.

## Sortie attendue

Tableau par créancier ou émetteur : ancien compte, nouveau compte, transfert annoncé, débit constaté, anomalie et preuve ; brouillon de correction ou d'indemnisation documentée. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Distinguer service de mobilité, transfert d'un produit et clôture. Vérifier l'éligibilité et les étapes datées ; conserver les opérations en attente sans recommander une clôture prématurée. Double prélèvement → BNK-006 ; frais → BNK-003 ; clôture → BNK-008.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, mobilité bancaire ; textes d'application et informations officielles Banque de France. Vérifier le point de départ et les jours retenus pour chaque étape. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] Le tableau relève le double débit et les preuves du manquement sans garantir une indemnisation.
- [ ] La sortie identifie les chèques en circulation et sépare la décision de clôture du suivi de mobilité.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : MOB01 — Un abonnement est débité sur les deux comptes après un mandat de mobilité.
- Cas limite : MOB02 — La personne veut fermer l'ancien compte alors que des chèques ne sont pas débités.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Changement de banque exécuté, transfert de PEA, clôture faite pour la personne, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
