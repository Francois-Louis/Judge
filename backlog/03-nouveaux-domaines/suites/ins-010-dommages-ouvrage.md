---
id: INS-010
titre: "Déclarer et suivre un sinistre dommages-ouvrage"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-010 — Déclarer et suivre un sinistre dommages-ouvrage

## Objectif et résultat attendu

Un propriétaire qui constate des désordres après des travaux comprend le rôle
de l'assurance dommages-ouvrage, prépare sa déclaration et lit les réponses
de l'assureur, avec les étapes à vérifier.

## Périmètre et fichiers

- `insurance-legal/skills/construction-insurance-claim/SKILL.md` — le skill (à créer)
- `insurance-legal/references/dommages-ouvrage.md` — étapes, pièces, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Attestation dommages-ouvrage ; procès-verbal de réception ; désordres et
dates ; photos ; courriers de l'assureur.

## Sortie attendue

Étape de la procédure ; brouillon de déclaration ou de réponse ; pièces ;
limites. Aucun délai calculé sans texte lu.

## Travail attendu

Responsabilité des constructeurs et réception → DOM-015. Absence d'assurance
dommages-ouvrage : question, sans conclusion.

## Références métier et sources à rechercher

Code des assurances, assurance dommages-ouvrage (piste L242-1).

## Critères d'acceptation

- [ ] O01 prépare la déclaration et identifie l'étape.
- [ ] O02 sépare garantie et responsabilité des constructeurs.

## Vérification

- Cas normal : O01 — Fissures dans une maison réceptionnée il y a trois ans.
- Cas limite : O02 — Demande de mettre en cause l'entreprise dans la même démarche.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Expertise technique, action contre les constructeurs, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-annexes/dom-005-decoupage-assurance.md).
