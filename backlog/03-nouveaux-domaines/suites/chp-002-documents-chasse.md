---
id: CHP-002
titre: "Rapprocher les documents de chasse d'une pratique située"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, CHP-001]
---

# CHP-002 — Rapprocher les documents de chasse d'une pratique située

## Objectif et périmètre

Le chasseur distingue ses documents et les vérifications nécessaires pour
une date et un territoire précis. Plugin proposé `hunting-fishing-legal`,
socle technique créé par CHP-001, sans obligation de passer par un contrôle.
[Contrat commun](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).

## Entrées et pièces

Permis ou titre présenté, validation, attestation d'assurance, courriers et
autorisation invoquée ; date, territoire et mode de pratique envisagés,
statut particulier déclaré (mineur, titre étranger, accompagnement), règles
locales disponibles. Ne pas demander de données médicales ou de détails
d'arme inutiles à la lecture des titres.

## Sortie attendue

Tableau document/mention lue/période et territoire portés/condition à
vérifier/source lue ou manquante ; pièces absentes et brouillon de demande
de justificatif ou d'explication à la fédération ou au service compétent.
Séparer existence du permis, validation, assurance et droit sur le terrain.
La sortie ne certifie pas que la personne peut chasser. Phrase finale
BASE-013 nommant un juriste ou avocat compétent ; renfort en cas de mesure
ou d'acte reçu, traité en premier par CHP-001.

## Travail et références métier

Créer `skills/hunting-document-check/SKILL.md` et
`references/documents-chasse.md` ; réutiliser la qualification et la méthode
locales, mettre à jour README, version, inventaire attendu et NOTICE du lot.
Lire Code de l'environnement, textes sur les titres/validation et assurance,
arrêtés et prescriptions territoriales pertinents, dans leurs versions
applicables. La fiche OFB S01 du découpage est une piste d'information.
Contrôler territoire et exceptions avant toute conclusion ; aucun prix ou
calendrier standard mémorisé. Absence d'arrêté : vérification réservée.

## Critères d'acceptation

- [ ] C05 distingue les documents et identifie la période/zone à vérifier sans autorisation générale de chasser.
- [ ] C06 conserve le territoire comme inconnu déterminant ; aucune règle métropolitaine transposée automatiquement.
- [ ] Droit sur le terrain → CHP-005 ; arme → CRIM-017 ; garantie contestée → DOM-005 ; acte → CHP-001.
- [ ] Sources et versions tracées, phrase BASE-013 et décisions de justice lues selon BASE-005 ; paquet autonome et recette client nominale/limite vérifiés selon le contrat commun.

## Vérification prévue

- C05 : « J'ai le permis et un reçu de paiement, est-ce suffisant pour ma
  sortie ? » → demander validation et attestation, date et lieu, distinguer
  reçu et document de validation, sans infraction présumée.
- C06 : titre présenté pour une pratique en Guyane, validation d'un autre
  territoire → vérifier le régime territorial, réserver ce qui dépend des
  sources absentes et identifier le service local.

## Hors périmètre et état

Garantie d'assurance, manipulation/transport d'armes, achat d'équipement,
inscription à l'examen ou validation effectuée pour la personne. Proposition
non implémentée ; [portée](../dom-040-annexes/dom-040-verification.md#portée).
