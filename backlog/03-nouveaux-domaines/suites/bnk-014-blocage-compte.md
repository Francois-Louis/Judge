---
id: BNK-014
titre: "Préparer une demande sur un compte ou un virement bloqué"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-014 — Préparer une demande sur un compte ou un virement bloqué

## Objectif et résultat attendu

Une personne privée d'accès à ses fonds identifie la nature du blocage connue ou encore incertaine et prépare une demande exploitable au bon interlocuteur.

Besoin issu des frictions 23, 52–53 de la [matrice utilisateur](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/account-block-review/SKILL.md` — le skill (à créer)
- `banking-legal/references/blocage-compte.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Convention, notification ou message d'erreur, opération empêchée et dates, demandes de justificatifs et preuves de remise, échanges, pertes documentées ; données sensibles masquées.

## Sortie attendue

Chronologie du blocage ; tableau demande de pièce/remise/réponse ; demande ciblée de traitement et d'accès aux services ; préjudices déclarés et prouvés séparés. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Distinguer conformité et connaissance du client, panne technique, saisie, clôture et plafond de carte. Ne pas inventer un motif non communiqué ni exiger une révélation interdite ; aucune aide au contournement des contrôles. Saisie → ENF-004 ; clôture → BNK-008 ; carte → BNK-016.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, obligations de vigilance et information sur les services de paiement ; contrat et disponibilité des services. Vérifier les limites de communication et le régime du prestataire. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] La demande reprend les justificatifs effectivement remis sans qualifier automatiquement le blocage d'abusif.
- [ ] La sortie garde la cause ouverte et documente l'opération empêchée et la perte sans responsabilité présumée.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : BLOC01 — Virement suspendu après une demande de justificatif, document déjà remis.
- Cas limite : BLOC02 — Application indisponible et échéance manquée ; aucune notification de conformité fournie.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Déblocage exécuté, contournement des contrôles, contestation de saisie, expertise informatique, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
