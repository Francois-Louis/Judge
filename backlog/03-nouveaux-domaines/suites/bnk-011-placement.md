---
id: BNK-011
titre: "Orienter une réclamation sur un placement ou un actif numérique"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-011 — Orienter une réclamation sur un placement ou un actif numérique

## Objectif et résultat attendu

Une personne en difficulté avec un placement, un intermédiaire ou un
prestataire d'actifs numériques identifie le produit, l'acteur, son statut à
vérifier auprès des autorités et l'interlocuteur. Aucun conseil
d'investissement.

## Périmètre et fichiers

- `banking-legal/skills/investment-orientation/SKILL.md` — le skill (à créer)
- `banking-legal/references/placements.md` — acteurs, listes officielles, médiateurs, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Nom de l'acteur et du produit ; documents reçus ; versements ; publicités ou
contacts d'origine ; tentatives de retrait.

## Sortie attendue

Fiche d'orientation ; vérifications à faire sur les listes officielles ;
interlocuteurs (prestataire, médiateur à identifier) ; signes de fraude à
relever ; limites.

## Travail attendu

Fraude : virements → BNK-002, plainte → DOM-002. Assurance-vie → DOM-005.
Aucune évaluation du produit ni du rendement.

## Références métier et sources à rechercher

Listes et alertes de l'AMF et de l'ACPR ; médiateur de l'AMF ; régime des
prestataires d'actifs numériques, à vérifier à la date des faits.

## Critères d'acceptation

- [ ] V01 produit l'orientation sans conseil d'investissement.
- [ ] V02 oriente la fraude vers BNK-002 et DOM-002.

## Vérification

- Cas normal : V01 — Perte sur un produit vendu par un conseiller, documents disponibles.
- Cas limite : V02 — Plateforme de cryptoactifs qui bloque les retraits après des « frais de déblocage ».

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Analyse du produit, réclamation au fond, action collective, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 80–83 et 89 de la [matrice](../dom-004-frictions-utilisateurs.md).

- [ ] V03 — Transfert PEA retardé ou coûteux : recueillir dates, établissements, lignes transférées, facture et réclamations ; produire orientation et liste de pièces, sans contrôler les plafonds ni établir la responsabilité.
- [ ] V04 — « Sans risque » ou frais mal compris : identifier nature juridique, garantie annoncée, documents et publicité ; demander détail des frais et orienter, sans évaluer risque, rendement ou qualité du conseil.

Scénarios V03/V04 **attendus, non exécutés**. Conserver la décision du 16 octobre 2026 : pas de traitement au fond des placements ni de nouveau domaine. Rachat d'assurance-vie → INS-012 ; capital après décès → INS-011. Le résultat annonce cette limite de couverture.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
