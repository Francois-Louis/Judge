---
id: SAN-003
titre: "Préparer la demande d'un ayant droit au dossier d'un patient décédé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-003 — Préparer la demande d'un ayant droit au dossier d'un patient décédé

## Objectif et résultat attendu

Un proche d'un patient décédé comprend si sa qualité et son objectif lui
permettent de demander des informations, lesquelles, avec quelles pièces,
et obtient un brouillon de demande motivée.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/deceased-patient-record-request/SKILL.md` — le skill (à créer)
- `health-legal/references/acces-ayant-droit.md` — qualités, objectifs, opposition, sources lues (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/references/acces-dossier.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Lien avec le défunt et pièce l'établissant ; date du décès ; acte de décès.
- Objectif poursuivi, exprimé par la personne.
- Opposition du défunt connue ou non.
- Structure, séjour ou période et informations visées.

## Sortie attendue

1. Résumé : qualité invoquée, objectif, informations susceptibles d'être visées, avec la source lue.
2. Fiche : lien, pièce, objectif, opposition connue ou inconnue.
3. Brouillon de demande motivée.
4. Ce qui reste à vérifier : étendue des informations communicables, délai et forme.
5. Suites : dommage suspecté → SAN-006 ; succession → DOM-016 ; obsèques → DOM-031.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `acces-ayant-droit.md` et l'appliquer : ne pas trancher la qualité
d'héritier ; distinguer objectif exprimé et informations demandées ; signaler
qu'un refus partiel peut tenir à l'objectif ou à l'opposition, à vérifier ;
ne pas demander d'informations sur des tiers.

## Références métier et sources à rechercher

Code de la santé publique, secret et accès après décès (piste L1110-4) et
accès aux informations (piste L1111-7) ; pièces de qualité exigées à
rechercher.

## Critères d'acceptation

- [ ] D01 produit une demande motivée pour un enfant du défunt, objectif exprimé.
- [ ] D02 signale qu'une demande du dossier entier peut excéder l'objectif, sans conclure.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'établissement, une association d'usagers ou un avocat.

## Vérification

- Cas normal : D01 — Fils voulant connaître les causes du décès de sa mère à l'hôpital.
- Cas limite : D02 — Concubine demandant « tout le dossier » sans objectif précisé.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Règlement de la succession, qualité d'héritier tranchée, indemnisation,
relance, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).

## Complément des frictions santé — 16 octobre 2026

Points 100 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Recueillir qualité, objectif motivé, opposition connue, justificatifs et refus reçu ; ne pas promettre l'intégralité du dossier ni assimiler proche et ayant droit.
- [ ] FS02 — Le scénario ci-dessous produit les distinctions et réserves demandées.

Scénario attendu : Proche sans qualité établie demandant tout le dossier : pièces utiles et accès réservé.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).
