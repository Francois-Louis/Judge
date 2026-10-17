# BASE-014 — Vérification

Contrôles du 17 octobre 2026 (Europe/Paris). Journal des lectures :
[relecture des sources](base-014-relecture.json).

## Contrôle de relecture et constructeur de lot

`python scripts/test-source-reviews.py` : 10 tests réussis.

| Scénario de la story | Test | Résultat observé |
|---|---|---|
| Toutes les sources relues, aucune modification : lot construit, dates dans l'inventaire | `test_lot_built_with_review_dates_in_inventory` (constructeur réel, `employment-legal`, arbre de travail) et `test_normal_all_unchanged` | Lot construit hors du dépôt ; `lot-inventory.json` contient `source_reviews.since` et, pour chaque ligne, référence, date, issue et voie. |
| Article modifié depuis la rédaction : refus tant que la référence n'est pas mise à jour | `test_modified_article_requires_reference_update_and_notice` | Refus sans `intégrée X.Y.Z`, refus si la version citée n'est pas celle de la référence, refus sans entrée NOTICE `<fichier> X.Y.Z`, acceptation une fois les trois présents. |
| Légifrance inaccessible, voie alternative réussie : relecture consignée avec la voie utilisée | `test_alternative_official_route_is_recorded` | La voie « CDTN après Légifrance HTTP 403 » est reprise dans le relevé. |
| Source non relue pour ce lot | `test_review_before_lot_preparation_is_refused`, `test_lot_refused_when_sources_not_reread_for_this_lot` | Refus du contrôle et du constructeur réel ; aucun répertoire de lot créé. |
| Source liée hors tableau, cellule incomplète, issue inconnue, date future ou invalide | quatre autres tests | Refus avec le chemin et la cellule en cause. |
| Source inaccessible | `test_inaccessible_source_needs_recorded_reserve` | Refus sans `réserve` ; lot accepté lorsque la réserve est consignée. |

État réel du dépôt au 17 octobre 2026, `--depuis 2026-10-17` :
`employment-legal` sans erreur (43 lignes de relecture couvrant 63 liens) ;
`commercial-legal` refusé, quatre sources de `orientation-commerciale.md` sans
relecture. La copie de la méthode `references/shared/` est hors contrôle par
construction.

## Relecture d'`employment-legal`

| Sources | Voie | Issue |
|---|---|---|
| 52 articles distincts du Code du travail (28 cités par `hiring-review-fr.md`, 25 par `worker-classification-fr.md`, L1221-1 commun) | `legal_sources.py travail` : Code du travail numérique, HTTP 200, date « Mis à jour le » comparée à la date consignée ; archives LEGI de la DILA du 15 octobre (deux) et du 16 octobre parcourues en flux | 52 dates identiques. Dans les archives, seuls L2253-1 et L2253-2 réapparaissent, avec la même version en vigueur depuis le 1er avril 2018 et aucune version future. |
| Règlement Rome I, directive 2024/2831 | EUR-Lex HTTP 202 sans contenu ; document lu par le CELLAR ; requête SPARQL du CELLAR sur les actes modificatifs, rectificatifs, consolidations et abrogations | Aucun acte modificatif ; rectificatifs français connus (2009) ou absents ; article 8 de Rome I et articles 5 et 29 de la directive relus. |
| Cinq décisions de `worker-classification-fr.md` | Légifrance par l'outil de lecture web | Identité et passages utilisés confirmés. |
| Deux pistes de `hiring-review-fr.md` | Légifrance ; publication de la Cour | Arrêt de 2002 désormais lisible, laissé comme piste ; arrêt de 2017 `inaccessible`, réserve maintenue. |

Aucune modification constatée : aucune version de contenu ni règle n'a changé.
Les colonnes `Relecture` ont été ajoutées aux deux références, qui portent
désormais la date, l'issue et la voie de chaque source.

## Régressions

`test-base008-isolation.py` (version attendue `0.3.2`), `check-version-bump.py`,
`test-check-plugin-package.py`, `test-pilote004-preferences.py`,
`test-legal-sources.py`, `lint-tool-scope.py`, JSON valides, `backlog/etat.py
--check` et `git diff --check` réussis. Paquet `employment-legal` copié hors
du dépôt : `STRUCTURE INCOMPLET` avec 51 `A_RELIRE` comme avant, aucun dans les
références modifiées ; `SCHEMA OK` (binaire 2.1.301) ; marketplace validé.

## Portée

Le contrôle lit du texte : il ne prouve ni qu'une lecture a eu lieu, ni
qu'elle était juste. Les versions futures adoptées avant la première lecture
n'ont été recherchées sur Légifrance que pour L1221-19 ; les pages du Code du
travail numérique contiennent plusieurs identifiants Légifrance et ne
permettent pas de retrouver de façon fiable celui de chaque article. Aucune
recherche jurisprudentielle exhaustive n'a été faite. Les décisions ont été
lues par résumé de l'outil web. La relecture vaut pour un lot préparé à partir
du 17 octobre 2026 ; un lot préparé plus tard demande une nouvelle relecture.
Aucun lot n'a été livré par cette story.
