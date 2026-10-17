---
id: CHP-004
titre: "Identifier les formalités d'une pêche maritime de loisir située"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, CHP-001]
---

# CHP-004 — Identifier les formalités d'une pêche maritime de loisir située

## Objectif et périmètre

Le pêcheur obtient les questions et justificatifs nécessaires pour vérifier
ses formalités, sans transposer la carte de pêche en eau douce à la mer.
Plugin proposé `hunting-fishing-legal`,
[contrat commun](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).
Une pratique située par dossier : bord, pied, embarquée ou sous-marine.

## Entrées et pièces

Lieu/façade, zone ou parc connu, date, âge utile au régime sans date de
naissance complète, mode de pratique, espèce visée ou alléguée, destination
des captures et caractère de loisir. Autorisation, récépissé d'enregistrement,
déclaration ou courrier existant, règlement/arrêté fourni. En estuaire ou
outre-mer, établir le champ avant de choisir les sources.

## Sortie attendue

Fiche de pratique, tableau formalité potentielle/champ à vérifier/source
exacte/document détenu/pièce ou question manquante. Distinguer enregistrement,
autorisation et déclaration des captures, sans obligation universelle
supposée. Brouillon de demande d'explication au service maritime local
identifié. Si règles locales, sanitaires ou d'espèces manquent, les repérer
sans autoriser la sortie. Phrase BASE-013 nommant un juriste ou avocat
compétent ; renfort si acte reçu, transmis d'abord à CHP-001.

## Travail et références métier

Créer `skills/recreational-sea-fishing-formalities/SKILL.md` et
`references/formalites-peche-maritime.md` ; réutiliser méthode/qualification
locales et actualiser README, version, inventaire attendu et NOTICE.
Lire Code rural et de la pêche maritime, règlements UE et actes d'application,
textes nationaux modifiés, règles de façade/zone et mesures sanitaires
pertinentes. La page ministérielle S03 du découpage signale des formalités
évolutives : contrôler dates d'application, transitions, âge, espèces et
territoires dans les textes, sans reprendre le calendrier de la fiche comme
règle vérifiée. Marquage ou limitation non lié à la formalité demandée :
question distincte à traiter ultérieurement, sans certification globale.

## Critères d'acceptation

- [ ] C10 identifie zone, pratique et formalité à vérifier sans imposer ni écarter une déclaration par analogie avec une autre façade.
- [ ] C11 conserve l'incertitude du régime eau douce/mer et de la zone sanitaire ; aucune taille, quota, période ou montant non sourcé.
- [ ] Aucun compte créé ni déclaration déposée ; pêche professionnelle exclue, atteinte au milieu → DOM-030 ; sécurité/navigation hors périmètre.
- [ ] Sources/version/transitions tracées ; phrase BASE-013, lecture des décisions selon BASE-005 et recette client/autonomie du contrat commun vérifiées.

## Vérification prévue

- C10 : pêcheur embarqué ayant un récépissé, demande s'il doit déclarer une
  espèce sur une autre façade → distinguer documents et captures, vérifier
  espèce/zone/date sans réutiliser automatiquement l'ancien récépissé.
- C11 : pêche à pied dans une embouchure, seule capture d'écran ancienne
  disponible → régime et source locale à établir, questions au service
  compétent, aucune autorisation ni conclusion sanitaire.

## Hors périmètre et état

Dépôt de formalité, pêche professionnelle, pratiques de pêche, équipement,
navigation et sécurité nautique. Proposition non implémentée ;
[portée](../dom-040-annexes/dom-040-verification.md#portée).
