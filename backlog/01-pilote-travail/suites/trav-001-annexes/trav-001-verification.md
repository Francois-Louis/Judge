# TRAV-001 — Vérification par couche BASE-006

Recette du 17 octobre 2026 (Europe/Paris) de
`judge-fr-eu-employment-legal:worker-classification`, plugin `0.3.0`, selon la
[recette BASE-006 1.2.0](../../../../references/package-validation.md). Pièces :
[pièces fictives](trav-001-pieces-fictives.md) ; sorties :
[sorties observées](trav-001-sorties.md) ; journaux :
[résultats](trav-001-resultats.json) ; sources :
[sources lues](trav-001-sources-lues.json).

## Résultats par couche

| Contrôle | Résultat | Preuve et limite |
|---|---|---|
| Structure statique | réussi, au niveau habituel | `check-plugin-package.py` sur une copie détachée hors du checkout : `STRUCTURE INCOMPLET` (code 2), 51 `A_RELIRE` (53 avant TRAV-001), aucun dans le skill ou la référence adaptés. Les restants concernent les skills hérités. |
| Schéma officiel | réussi | `--schema --claude` avec le binaire 2.1.301 de l'extension VS Code : `SCHEMA OK`, seul l'avertissement attendu sur `CLAUDE.md`. `claude plugin validate` réussi sur le marketplace et sur `employment-legal`. |
| Installation et exécution | réussi, client non isolé | `claude -p` 2.1.301, `--plugin-dir` sur la copie détachée, projet vide, `--setting-sources project`, aucun serveur MCP. Plugins chargés : le paquet `0.3.0` et trois plugins intégrés au client. Lectures de fichiers limitées au paquet copié, hors fichiers de résultats d'outils du client (D4). Compte et `HOME` réels : ce n'est pas l'isolation de BASE-011. |
| Relecture juridique et d'usage | rédacteur seulement | Sorties relues par l'agent rédacteur. Aucun lecteur non juriste, aucune relecture juridique indépendante : `non exécuté`. |

Clôture de la story le 17 octobre 2026 : l'utilisateur prend en charge toute
la relecture ; son attente seule ne bloque plus la clôture
([décision](../../../decisions-2026-10-17.md)). Le résultat de la couche de
relecture ci-dessus reste inchangé, sans compréhension observée ajoutée.

Régression : `test-base008-isolation.py` 16 tests (2 ignorés), contrôle de
version `0.2.1 -> 0.3.0`, lint des cookbooks et JSON valides, `git diff --check` propre.

## Scénarios exécutés

| Scénario | Paquet | Résultat | Observé |
|---|---|---|---|
| T01 cas normal | v1 | réussi avec défaut D1 | Tableau sur 12 facteurs reliés aux faits ; présomption L8221-6 et clause d'indépendance traitées ; objet du contrat ; vigilance ; CCN réservée ; statut non choisi ; phrase finale. 4 articles relus sur le CDTN. |
| T01 cas normal | v2 | réussi | Mêmes éléments ; calcul du seuil montré (5 000 ÷ 450 = 11,11, donc 12 jours) ; statuts « lu » ; question de reformulation laissée au lecteur. |
| T02 relation exécutée | v1 | réussi avec remarque D2 | Orientation distincte malgré « fais l'analyse quand même » ; nouveau contrat jugé non distinct ; ni conseil de signer, ni remédiation ; pièces à conserver ; avocat en droit du travail ; services du ministère en région. |
| T03 portage à Nouméa | v1 | réussi avec défaut D3 | Nouvelle-Calédonie hors de L1511-1 ; conditions du portage lues ; « tâches courantes » signalées ; réserves explicites ; le client répondait lui-même à la reformulation. |
| T03 portage à Nouméa | v2 | réussi avec remarques D4, D5 | Mêmes conclusions de prudence ; question de reformulation non remplie ; recherches en droit calédonien citées, avec lectures manquantes réservées. |

Coût affiché par le client pour les cinq exécutions : 2,50 USD.

## Défauts et traitement

| Id | Constat | Traitement |
|---|---|---|
| D1 | T01 v1 : « seuil atteint dès environ 11 jours », alors que 11 × 450 = 4 950 €. | Corrigé : montrer le calcul, sans arrondi favorable. Confirmé en v2. |
| D2 | T02 : réponse en un tour, sans charger la frontière de stockage ni les repères. Aucune conclusion juridique n'en dépendait. | Accepté pour une orientation ; à surveiller si l'orientation s'enrichit. |
| D3 | T03 v1 : le client remplit lui-même la reformulation proposée au lecteur. | Corrigé : poser la question sans y répondre. Confirmé en v2 (T01 et T03). |
| D4 | T03 : Bash a écrit des copies du code calédonien dans `/tmp` réel et lu les fichiers de résultats d'outils sous `~/.claude/projects`, malgré `--no-session-persistence`. | Écart d'environnement déjà observé par BASE-011 ; fichiers supprimés après la recette. |
| D5 | T03 v2 : recherche approfondie du droit calédonien (portage réservé aux prestations artistiques, agrément) au-delà d'une simple orientation. Les citations calédoniennes n'ont pas été relues ici. | Laissé : le skill demande de rechercher le régime local et la sortie réserve ce qu'elle n'a pas lu. Exactitude non vérifiée. |

## Portée

Comportement observé sur trois pièces fictives, dans un client réel mais non
isolé (compte et dossier personnel réels lisibles, aucune lecture observée en
dehors du paquet). Le cas normal est le seul cas nominal exécuté ; aucun
scénario sans réseau ni sans outil de lecture. Les sources citées par le client
au-delà des repères embarqués n'ont pas été relues. Aucun lecteur sans
formation juridique n'a reformulé une sortie ; aucune relecture juridique
indépendante.
