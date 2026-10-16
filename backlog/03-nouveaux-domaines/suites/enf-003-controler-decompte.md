---
id: ENF-003
titre: "Contrôler le décompte d'un acte d'exécution"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-003 — Contrôler le décompte d'un acte d'exécution

## Objectif et résultat attendu

Une personne compare le décompte d'un acte au titre exécutoire et à ses
paiements, repère les postes non justifiés et obtient une demande de
ventilation.

## Périmètre et fichiers

- `enforcement-legal/skills/statement-check/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/decompte.md` — postes, justificatifs, tarifs à vérifier, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte et décompte ; titre exécutoire et ses condamnations ; paiements avec
preuves ; actes antérieurs.

## Sortie attendue

Tableau : poste, montant recopié, fondement indiqué, justificatif, écart ou
question. Postes non ventilés signalés ; brouillon de demande de ventilation ;
limites. Aucun intérêt ni tarif recalculé sans source lue.

## Travail attendu

Distinguer principal, intérêts, frais et émoluments. Un total global sans
détail est une absence de ventilation, pas une erreur établie. Frais bancaires
liés à la saisie → DOM-004.

## Références métier et sources à rechercher

Titre exécutoire visé ; tarifs réglementés des commissaires de justice
(Code de commerce et arrêtés) ; règles sur la charge des frais d'exécution.

## Critères d'acceptation

- [ ] D01 produit le tableau et la demande de ventilation sans recalcul.
- [ ] D02 rapproche un paiement prouvé non déduit, sans conclure à une faute.

## Vérification

- Cas normal : D01 — Total « principal, intérêts et frais » sans détail.
- Cas limite : D02 — Acompte versé au créancier absent du décompte.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Calcul d'intérêts, contestation devant le juge, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
