---
id: BASE-019
titre: "Distinguer, dans le corps d'une note, décision lue et fiche embarquée"
statut: en-cours
priorite: P1
nature: implementation
dependances: [BASE-016, BASE-017]
---

# BASE-019 — Distinguer, dans le corps d'une note, décision lue et fiche embarquée

## Objectif

Une note ne dit « j'ai lu » que pour une décision ouverte pendant la réponse.
Une décision connue seulement par la fiche d'une référence embarquée est
présentée comme telle, avec sa date de relecture, dans le texte et pas
seulement dans la liste des sources. Écart observé dans la recette
[BASE-017](base-017-recette-jurisprudence-runtime.md), le 17 octobre 2026.

## Constat

- S3 : « J'ai lu les décisions suivantes de la Cour de cassation » introduit
  quatre arrêts. Trois n'ont pas été rouverts pendant la réponse ; le tableau
  des sources le dit (« sans réouverture pendant cette réponse »).
- S2 : la note commence par « J'ai lu votre contrat et les décisions de
  justice utiles » ; l'arrêt du 16 mai 2012, cité dans le corps, n'a pas été
  rouvert, ce que seule la liste des sources précise.
- S4, S5 : arrêts correctement annoncés comme non rouverts, mais la date de
  relecture de la fiche n'apparaît qu'en fin de note. S4 dit aussi la
  convention IDCC 1486 « inaccessible (Légifrance a refusé l'accès) » sans
  qu'une lecture en ait été tentée.

## Périmètre

Méthode partagée (`references/research-citation-method.md`, section 10) et
copies embarquées ; `employment-legal/skills/hiring-review/SKILL.md` si une
consigne de restitution est nécessaire. Versions et NOTICE selon les règles du dépôt.

## Travail attendu

- Ajouter à la section 10 une règle de formulation : le verbe « lire » et
  ses équivalents ne qualifient qu'une décision ouverte pendant la réponse ;
  une fiche embarquée est annoncée « d'après la fiche de [référence], relue
  le [date] ».
- Donner une formulation type pour un paragraphe qui mélange les deux.
- Une source n'est dite inaccessible que pour une tentative réelle ; sinon
  « non consultée ».
- Rejouer S2, S3 et S4 de BASE-017 dans un client isolé.

## Critères d'acceptation

- [x] La méthode distingue explicitement lecture pendant la réponse et fiche embarquée dans le corps de la note.
- [ ] S2, S3 et S4 rejoués : aucune phrase du corps ne présente comme lue une décision non rouverte.

## Hors périmètre

Exactitude juridique des solutions, autres plugins que `employment-legal` pour la recette.

## Réalisation — 17 octobre 2026

Méthode BASE-005 **1.3.0** : nouvelle section 10.6 « Dire, dans le corps de
la note, ce qui a été lu » (verbe « lire » réservé à une décision ouverte
pendant la réponse ; fiche embarquée annoncée « d'après la fiche de
[référence], relue le [date] » là où la décision est invoquée ; formulation
type pour un paragraphe mixte ; « inaccessible » seulement après une tentative
réelle, sinon « non consultée »). Renvoi depuis l'introduction de la section
10 et formulation de la section 5 alignée. Copie identique dans les **dix-sept**
paquets (la consigne initiale en comptait onze, avant l'ajout de six paquets),
version patch de chacun, renvois `1.3.0`. `hiring-review` et
`worker-classification` rappellent la règle là où ils demandent de distinguer
lu, fourni, non consulté et inaccessible. Aucune règle de droit ajoutée.

Contrôles : `check-version-bump.py` réussi ; `test-base008-isolation.py`
16 tests OK, 2 ignorés (jsonschema absent, liens symboliques refusés par
Windows) ; `test-source-reviews.py` 10 OK ; `source_reviews.py
employment-legal --depuis 2026-10-17` sans erreur (45 relectures) ;
`claude plugin validate` réussi sur le marketplace et sur `employment-legal`
(avertissement attendu sur `CLAUDE.md`).
