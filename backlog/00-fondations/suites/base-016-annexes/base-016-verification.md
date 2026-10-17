# BASE-016 — Vérification

Contrôles du 17 octobre 2026 (Europe/Paris).

## Voies de la section 10.4 rejouées le jour de l'intégration

Outil de lecture web de la session (WebFetch), environ une heure après les
tentatives de [BASE-015](../../base-015-annexes/base-015-acces-session.json) :

| Voie | Adresse rejouée | Issue |
|---|---|---|
| Légifrance, recherche judiciaire | `search/juri`, requête `22-20.926` | 1 résultat, JURITEXT000049053200. |
| Légifrance, décision judiciaire | `juri/id/JURITEXT000049053200` | Identité, paragraphe 5 et dispositif restitués. |
| Légifrance, recherche administrative | `search/cetat`, requête `489206` | 1 résultat, CETATEXT000048734416. |
| Légifrance, décision administrative | `ceta/id/CETATEXT000048734416` | Visas, points 1 à 10, dispositif. |
| Conseil d'État | `arianeweb/CE/decision/2024-05-23/494320` | Visas, points 1 à 11, dispositif. |
| Conseil constitutionnel | `decision/2010/201014_22QPC.htm` | Visas, considérants 1 à 30, dispositif. |
| Cour EDH | conversion HUDOC `001-57619` | Texte présent, lecture par tranches. |
| Cour de cassation | `decision/6079b1ab9ba5988459c53061` | Page vide. |
| CJUE | `infocuria…/document.jsf?docid=169195` | Page vide (« RPEX »). |

Aucune adresse de la table n'a changé ; la proposition est intégrée sans
correction de voie. La recherche du Conseil constitutionnel n'a pas été
rejouée : la table garde l'observation de BASE-015 au passé.

## Relecture : fiche selon la section 10

Lecteur : l'agent de maintenance (non indépendant), sur la page Légifrance.

| Champ | Valeur |
|---|---|
| Juridiction et formation | Cour de cassation, chambre sociale |
| Date | 24 janvier 2024 |
| Numéro | 22-20.926 |
| ECLI | ECLI:FR:CCASS:2024:SO00084 (affiché) |
| Publication | Publié au bulletin ; cassation partielle |
| Accès | `https://www.legifrance.gouv.fr/juri/id/JURITEXT000049053200`, outil de lecture web, 17 octobre 2026, français |
| Passages lus | Paragraphe 5 (règle : la violation de la clause de non-concurrence prive le salarié de la contrepartie financière, même après la fin de la violation) ; début du dispositif « CASSE ET ANNULE, mais seulement en ce qu'il… » |
| Statut | `verifie` pour ce passage, par extraits littéraux courts restitués par l'outil |
| Portée et applicabilité | Solution publiée sur l'effet d'une violation ; ne porte pas sur les conditions de validité de la clause ; évolutions postérieures non recherchées ; applicabilité à un dossier `a-etablir` |

Tous les champs de 10.2 sont renseignables à partir de la seule page de la
décision.

## Contrôles du dépôt

| Contrôle | Résultat |
|---|---|
| Empreintes de la source et des onze copies | 12 fichiers identiques (MD5 `361ae020d74597b6a044e37785c4a58a`). |
| `python scripts/test-base008-isolation.py` | 16 tests, OK (2 ignorés, liens symboliques Windows). |
| `python scripts/check-version-bump.py` | Onze paquets relevés : 0.1.2, commercial-legal 0.2.2, employment-legal 0.3.3 → 0.3.4 (base `b0d3ba2`, contrôles rejoués après ce commit). |
| `claude plugin validate` (binaire 2.1.299 de l'application) | Marketplace valide ; onze plugins valides avec les avertissements attendus (modèle `CLAUDE.md`). |
| `check-plugin-package.py --schema` sur copies hors dépôt | `SCHEMA OK` ; `STRUCTURE INCOMPLET` inchangé : employment-legal 51, commercial-legal 42, privacy-legal 31 `A_RELIRE`, mêmes constats qu'au commit précédent. |
| `scripts/source_reviews.py --depuis 2026-10-17` | employment-legal sans erreur (43 relectures) ; commercial-legal refusé comme avant BASE-016 (relecture de son lot non faite). |
| `test-check-plugin-package.py`, `test-source-reviews.py`, `test-legal-sources.py`, `lint-tool-scope.py` | OK (13, 10 et 30 tests ; portée des orchestrateurs propre). Les tests qui lancent un sous-processus demandent `PYTHONUTF8=1` sous Windows. |
| JSON, `backlog/etat.py --check`, `git diff --check` | OK. |

## Portée

Aucune exécution d'un skill installé : le comportement pendant une réponse
reste à recetter dans un client isolé (BASE-017). Les voies valent pour la
date et l'outil testés. La relecture est faite par l'agent qui a rédigé la
section, pas par un lecteur indépendant. Aucune règle de droit n'est ajoutée ;
les références métier gardent leurs décisions jusqu'à TRAV-062.
