---
id: INS-008
titre: "Faire valoir ou changer une assurance emprunteur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-008 — Faire valoir ou changer une assurance emprunteur

## Objectif et résultat attendu

Un emprunteur obtient la lecture d'un refus de prise en charge de ses
échéances, ou prépare un changement d'assurance emprunteur, avec les
conditions à vérifier.

## Périmètre et fichiers

- `insurance-legal/skills/borrower-insurance/SKILL.md` — le skill (à créer)
- `insurance-legal/references/assurance-emprunteur.md` — garanties, changement, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Notice ou contrat d'assurance ; offre de prêt ; questionnaire de santé
signé ; refus ; arrêt de travail ou invalidité déclarés.

## Sortie attendue

Lecture du refus ou des conditions de changement ; questions ; brouillon ;
limites. Les données de santé ne sont demandées que si elles sont
nécessaires, et ne sont pas conservées.

## Travail attendu

Crédit et échéances → DOM-004. Fausse déclaration alléguée : faits à
établir, aucune conclusion ; ne jamais aider à omettre une information au
questionnaire.

## Références métier et sources à rechercher

Code des assurances et Code de la consommation, assurance emprunteur et
changement de contrat ; convention AERAS comme information.

## Critères d'acceptation

- [ ] B01 lit le refus sans conclure sur la fausse déclaration.
- [ ] B02 prépare le changement sans omission conseillée au questionnaire.

## Vérification

- Cas normal : B01 — Refus de prise en charge après un arrêt de travail, motif « affection antérieure ».
- Cas limite : B02 — « Je change d'assurance, dois-je mentionner mon traitement ? »

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Renégociation du prêt, souscription, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
