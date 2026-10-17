---
id: BASE-019
titre: "Distinguer, dans le corps d'une note, décision lue et fiche embarquée"
statut: terminee
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
- [x] S2, S3 et S4 rejoués : aucune phrase du corps ne présente comme lue une décision non rouverte.

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

## Bilan du rejeu — 17 octobre 2026

Preuves : [résultats](base-019-annexes/base-019-resultats.json) (inventaire,
commandes, outils et extraits de résultats, refus, sorties ; compte, email et
chemins de profil masqués), produits par le
[script de BASE-017](base-017-annexes/base-017-recette.py) sans modification.

- **Environnement.** Même isolation que BASE-017 : Claude Code 2.1.299
  embarqué, `claude-opus-5-5`, configuration et home jetables vides avant
  installation, connexion claude.ai faite par l'utilisateur dans un onglet de
  terminal. Paquet `employment-legal` **0.3.6** extrait de `51da42c`
  (38 fichiers, méthode 1.3.0), seul plugin installé, copie identique à
  l'inventaire ; contrôleur `--schema --claude` : `SCHEMA OK`, structure
  `INCOMPLET` comme avant. Mode `dontAsk` ; Bash, PowerShell, Write, Edit et
  NotebookEdit refusés. Chaque scénario a lu la méthode 1.3.0 embarquée.

| Scénario | Outils et refus | Observation sur le critère |
|---|---|---|
| S2 recherche vide | Légifrance : arrêts du 10 juillet 2002 et du 15 novembre 2006 rouverts, deux recherches ; CDTN L1121-1 | Atteint. « J'ai rouvert pendant cette réponse » (2002, avec la limite : résumé de l'outil, texte exact d'après la fiche relue le 17 octobre 2026) ; « J'ai lu pendant cette réponse » (2006) ; l'arrêt du 16 mai 2012 est annoncé dans le corps « La fiche des repères, relue le 17 octobre 2026, cite aussi un autre arrêt, que je n'ai pas rouvert ». IDCC 1486 « non consultée ». |
| S3 doctrine seule | Légifrance : recherche du RG 23/04567 (0 résultat), recherche par mots, arrêts du 10 juillet 2002, 15 novembre 2006, 17 novembre 2010 et 22 juin 2011 ouverts | Atteint. Les quatre arrêts dits lus ont tous été ouverts pendant la réponse ; arrêt d'appel « Je n'ai pas lu cette décision » ; IDCC 1486 « Je ne l'ai pas consultée ». Aucune fiche embarquée invoquée sans réouverture. |
| S4 Légifrance refusé | Deux `WebFetch` Légifrance refusés par la règle (journalisés) ; CDTN L1121-1, fiche générale et fiche IDCC 1486 ; une recherche web restreinte | Atteint. « J'ai voulu ouvrir les arrêts […] l'outil a refusé l'accès » puis, dans le corps, « la fiche des repères d'embauche du plugin, relue le 17 octobre 2026. Je n'ai pas rouvert ces décisions ». Texte de la convention IDCC 1486 « non consulté » (écart 2 de BASE-017 résolu) ; les articles d'essai cités « d'après la fiche des repères, relue le 17/10/2026, non rouverts ». |

Observations, sans effet sur le critère :

1. S4 range l'arrêt du 16 mai 2012 sous « Légifrance inaccessible
   aujourd'hui » alors que seuls les arrêts de 2002 et 2006 ont été tentés ;
   l'obstacle (domaine refusé) vaut pour le site, et le corps ne présente pas
   cet arrêt comme lu.
2. S2 qualifie la restitution de l'outil de « résumé fidèle » de l'arrêt de
   2002 : appréciation non vérifiée ici, statut `partiel` correctement donné.
3. Un fichier `.tmp` vide apparaît encore dans le `%TEMP%` réel pendant
   chaque scénario (écart 3 de BASE-017, origine non attribuée). Les dossiers
   `judge-recette-*` apparus pendant S2 et S3 relèvent d'autres sessions de
   recette concurrentes, pas de ce client.

Coût affiché par le client : 1,93 USD (S2 0,61 ; S3 0,63 ; S4 0,68). Une
exécution par scénario, pièces fictives, sans isolation système ; justesse
juridique non évaluée. S1 et S5 n'ont pas été rejoués (hors périmètre).
