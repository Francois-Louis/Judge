---
id: INS-011
titre: "Accompagner un bénéficiaire d'assurance-vie ou de capital décès"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-011 — Accompagner un bénéficiaire d'assurance-vie ou de capital décès

## Objectif et résultat attendu

Une personne qui pense être bénéficiaire d'un contrat après un décès sait
comment le vérifier, quelles pièces fournir et comment relancer l'assureur.

## Périmètre et fichiers

- `insurance-legal/skills/life-insurance-beneficiary/SKILL.md` — le skill (à créer)
- `insurance-legal/references/assurance-vie.md` — recherche, pièces, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Acte de décès ; contrat ou indice d'existence ; clause bénéficiaire connue ;
courriers de l'assureur ; lien avec le défunt.

## Sortie attendue

Démarches de recherche à vérifier ; pièces ; brouillon de demande ou de
relance ; limites. Aucune fiscalité ni délai affirmés sans texte lu.

## Travail attendu

Succession → DOM-016 ; fiscalité → DOM-011 ; rendement ou gestion du
placement → hors domaine. Clause bénéficiaire contestée entre proches :
question à un avocat ou au notaire, sans arbitrage.

## Références métier et sources à rechercher

Code des assurances, assurance sur la vie (pistes L132-1 et suivants) ;
dispositifs officiels de recherche des bénéficiaires.

## Critères d'acceptation

- [ ] V01 décrit la recherche et prépare la demande.
- [ ] V02 ne tranche pas un désaccord sur la clause bénéficiaire.

## Vérification

- Cas normal : V01 — Enfant pensant être bénéficiaire du contrat de son père.
- Cas limite : V02 — Deux proches revendiquant le même capital.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Succession, fiscalité, conseil de placement, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
