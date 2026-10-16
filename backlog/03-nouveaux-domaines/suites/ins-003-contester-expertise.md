---
id: INS-003
titre: "Contester le chiffrage d'une expertise"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-003 — Contester le chiffrage d'une expertise

## Objectif et résultat attendu

Un assuré en désaccord avec le montant proposé après expertise compare le
rapport, ses devis et le contrat, comprend les options à vérifier
(contre-expertise, expertise contradictoire) et prépare une réponse.

## Périmètre et fichiers

- `insurance-legal/skills/expert-assessment-dispute/SKILL.md` — le skill (à créer)
- `insurance-legal/references/expertise.md` — postes, clauses, options, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Rapport d'expertise ; proposition d'indemnité ; devis et factures ; clauses
d'indemnisation (valeur à neuf, vétusté, franchise, plafond) ; clause
d'expertise ; garantie des honoraires d'expert.

## Sortie attendue

Tableau : poste, montant de l'expert, devis, clause applicable, écart ou
question. Options à vérifier ; brouillon de réponse motivée ; limites. Aucun
montant recalculé.

## Travail attendu

Distinguer désaccord sur la garantie (INS-001) et désaccord sur le chiffrage.
Ne pas présenter un devis comme la valeur due.

## Références métier et sources à rechercher

Clauses du contrat ; principe indemnitaire (piste L121-1 du Code des
assurances) ; information publique sur l'expertise contradictoire.

## Critères d'acceptation

- [ ] X01 produit le tableau des écarts sans recalcul.
- [ ] X02 renvoie le refus de garantie d'un poste vers INS-001.

## Vérification

- Cas normal : X01 — Incendie de cuisine, expert à un montant, devis presque double, vétusté appliquée.
- Cas limite : X02 — L'expert écarte un poste « non garanti ».

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Évaluation technique des dommages, choix d'un expert, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
