---
id: BNK-017
titre: "Rechercher les fonds d'un compte inactif"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-017 — Rechercher les fonds d'un compte inactif

## Objectif et résultat attendu

Une personne recherche ses propres fonds devenus inaccessibles et distingue une demande à la banque d'une recherche auprès du dépositaire officiel.

Besoin issu des frictions 45–46 de la [matrice utilisateur](../dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/inactive-account-search/SKILL.md` — le skill (à créer)
- `banking-legal/references/compte-inactif.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Derniers relevés et contacts, preuve de titularité à fournir seulement par canal officiel, notifications d'inactivité ou de transfert, produit et dates connus.

## Sortie attendue

Frise dernières opérations/notifications/transfert connu ; interlocuteur à identifier ; liste de pièces à transmettre par canal officiel et brouillon de recherche. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Ne pas déduire l'inactivité du seul manque d'utilisation ; vérifier produit, titulaire vivant ou décédé, dates et régime de transfert. Frais → BNK-003 ; fonds d'un défunt → DOM-016 ; assurance-vie → DOM-005. Ne pas demander de pièce d'identité complète dans la conversation.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, comptes inactifs et déshérence ; Caisse des dépôts et Ciclade, canaux officiels à vérifier. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] La sortie distingue recherche auprès de la banque et recherche Ciclade sans délai de déchéance non sourcé.
- [ ] La sortie relève le décès et la qualité à établir puis oriente vers DOM-016, sans accès aux fonds promis.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : INA01 — Ancien compte personnel dont la banque indique avoir transféré les fonds.
- Cas limite : INA02 — Recherche au nom d'un parent décédé sans preuve de transfert ni qualité successorale établie.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Recherche exécutée avec identité complète, règlement de succession, conseil de placement, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-decoupage-banque.md).
