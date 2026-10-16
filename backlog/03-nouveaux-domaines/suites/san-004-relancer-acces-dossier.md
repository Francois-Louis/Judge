---
id: SAN-004
titre: "Relancer ou contester une communication tardive, incomplète ou refusée du dossier médical"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-004 — Relancer ou contester une communication tardive, incomplète ou refusée du dossier médical

## Objectif et résultat attendu

Une personne qui a demandé un dossier médical et n'a rien reçu, ou une
réponse incomplète ou un refus, obtient une chronologie, ce qui reste à
établir avant de parler de retard, un brouillon de relance et les voies
possibles à vérifier selon le statut de la structure.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/medical-record-access-follow-up/SKILL.md` — le skill (à créer)
- `health-legal/references/suite-acces-dossier.md` — chronologie, voies selon le statut, sources lues (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/references/acces-dossier.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Demande initiale, date et preuve d'envoi et de réception.
- Qualité du demandeur ; informations visées et leur ancienneté.
- Réponses reçues : accusé, demande de pièces, envoi partiel, refus et motif.
- Statut public ou privé de la structure.

## Sortie attendue

1. Résumé : où en est la demande, ce qui manque pour parler de retard.
2. Chronologie : événement, date prouvée ou déclarée, pièce.
3. Ce qui reste à vérifier : délai applicable selon l'ancienneté, réception et exceptions, avec la source lue ou réservé.
4. Brouillon de relance ou de demande de motifs.
5. Voies à vérifier selon le statut : médiation interne, commission d'accès aux documents administratifs pour un établissement public, juge.
6. Volet RGPD distinct → PRV-033 ; soupçon de consultation → PRV-001 ou PRV-025.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `suite-acces-dossier.md` et l'appliquer : aucun délai sans source lue,
date de réception prouvée et qualification de l'ancienneté ; aucun
calendrier RGPD appliqué automatiquement ; demande de pièces reçue comme
événement à dater ; refus motivé distingué d'une absence de réponse.

## Références métier et sources à rechercher

Pistes SAN-001 ; pour un établissement public, Code des relations entre le
public et l'administration et saisine de la CADA ; voies juridictionnelles
selon le statut.

## Critères d'acceptation

- [ ] R01 établit la chronologie et réserve le délai si la réception n'est pas prouvée.
- [ ] R02 sépare deux objets et deux calendriers : copie du dossier et accès soupçonné.
- [ ] R03 distingue refus motivé, envoi partiel et absence de réponse.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'établissement, la commission compétente ou un avocat selon le statut.

## Vérification

- Cas normal : R01 — Demande envoyée par courrier simple il y a plusieurs semaines, aucune réponse.
- Cas limite : R02 — Copie toujours attendue et soupçon de consultation par un tiers (points 46–47 de la [matrice données personnelles](../../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md)).
- Cas limite : R03 — Hôpital public n'envoyant que la lettre de sortie.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Rédaction d'une saisine ou d'une requête, délai validé sans source,
indemnisation, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
