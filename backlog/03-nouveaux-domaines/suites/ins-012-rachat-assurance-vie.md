---
id: INS-012
titre: "Relancer un rachat d'assurance-vie retardé"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-012 — Relancer un rachat d'assurance-vie retardé

## Objectif et résultat attendu

Un souscripteur ayant demandé un rachat obtient une chronologie documentée, les pièces encore nécessaires et un brouillon de relance à l'assureur. Besoin issu du point 84 de la [matrice des frictions bancaires](../dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `insurance-legal/skills/life-insurance-surrender-follow-up/SKILL.md` — le skill (à créer)
- `insurance-legal/references/rachat-assurance-vie.md` — demande, complétude, paiement et sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

Les références de qualification INS-001 sont relues, pas réécrites. Ne pas confondre le souscripteur demandant un rachat avec le bénéficiaire après décès (INS-011).

## Pièces et informations nécessaires

Contrat, demande de rachat partiel ou total, réception prouvée, demandes de pièces et preuves de remise, relevé de paiement éventuel ; dates et qualité du demandeur.

## Sortie attendue

Frise demande/réception/pièces/paiement ; blocage expliqué ou restant à éclaircir ; brouillon de relance et demande d'intérêts éventuels à vérifier. Aucune fiscalité ni montant d'intérêts calculé.

## Travail attendu

Vérifier les conditions contractuelles, le point de départ et les exceptions du régime applicable. Ne pas affirmer que la seule date d'envoi déclenche nécessairement un délai. Capital après décès → INS-011 ; litige de rendement ou conseil de placement → orientation seule BNK-011 ; médiation → INS-005.

## Références métier et sources à rechercher

Code des assurances, valeur de rachat, délai de versement et intérêts de retard (piste L132-21), version applicable et exceptions ; contrat. Pistes à vérifier à l'implémentation, sans règle validée ici.

## Critères d'acceptation

- [ ] RACH01 distingue les dates établies des déclarations et prépare une relance sur une demande documentée.
- [ ] RACH02 réserve le point de départ si la réception ou la complétude sont inconnues.
- [ ] La sortie distingue le rachat, le capital décès et le conseil de placement ; le paquet fonctionne seul.

## Vérification

- Cas normal : RACH01 — Demande de rachat reçue par l'assureur, pièces remises, aucun versement ni explication.
- Cas limite : RACH02 — Première demande sans accusé de réception, nouvelle demande de pièce dont la nécessité est contestée.
- Sans source lue : pièces, chronologie et questions ; aucun délai ni intérêt affirmé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Conseil de rachat, arbitrage, fiscalité, simulation de rendement, calcul d'intérêts, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions utilisateur, sans implémentation ni sélection. Contrat commun : [découpage assurance](../dom-005-decoupage-assurance.md).
