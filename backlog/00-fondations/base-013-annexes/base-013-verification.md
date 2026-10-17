# BASE-013 — Vérification

Recette du 17 octobre 2026 (Europe/Paris). Pièces :
[pièces fictives](base-013-pieces-fictives.md) ; sorties :
[sorties observées](base-013-sorties.md) ; journaux :
[résultats](base-013-resultats.json) ; lectures de cadrage :
[sources lues](base-013-sources-lues.json).

## Contrôles statiques

| Contrôle | Résultat |
|---|---|
| Copies de la méthode `1.1.0` | Source et onze copies `references/shared/` identiques octet pour octet (empreinte MD5 commune) ; contrôle aussi exécuté par `test-base008-isolation.py`. |
| Isolation BASE-008 | `python scripts/test-base008-isolation.py` : 16 tests réussis, 2 ignorés ; versions attendues `0.1.1`, `0.2.1` et `0.3.1`. |
| Versions | `python scripts/check-version-bump.py` : onze paquets relevés par rapport à `origin/main`. |
| Schéma officiel | `claude plugin validate` (binaire 2.1.301 de l'extension VS Code) : marketplace réussi ; onze paquets réussis avec les avertissements attendus sur `CLAUDE.md`. |
| Paquets détachés | `check-plugin-package.py --schema --claude` sur des copies hors du checkout : `employment-legal` `STRUCTURE INCOMPLET` avec 51 `A_RELIRE` (comme après TRAV-001), `commercial-legal` 42 ; aucun dans les skills, références ou méthode modifiés ; `SCHEMA OK` pour les deux. |
| Autres régressions | `test-check-plugin-package.py` (13 tests), `test-pilote004-preferences.py`, `lint-tool-scope.py`, JSON valides, `git diff --check` propre. |

## Scénarios exécutés

Client `claude -p` 2.1.301, modèle `claude-opus-5-5`, copie détachée du
paquet, Bash interdit ; isolation et commande dans les résultats.

| Scénario | Paquet | Renfort en tête | Phrase finale et interlocuteur | Résultat |
|---|---|---|---|---|
| A01 offre sans urgence | v1 | absent, à juste titre | Présente, « avocat ou juriste en droit du travail », mais suivie de deux phrases (RH, syndicat) puis d'une liste de sources : quatre lignes, pas en dernière position. | défaut D1 |
| A01 offre sans urgence | v2 | absent, à juste titre | Dernière ligne, après les sources, deux phrases ; RH présentés comme non-conseils dans la prochaine étape. | réussi |
| A02 signature avant demain, non-concurrence, démission | v1 | « À faire en premier » : signature, démission difficile à annuler, avocat ou juriste, syndicat ; aucun délai calculé. | Dernière ligne conforme. | réussi |
| A02 | v2 | « Ce qui presse » : mêmes éléments, échéance qualifiée de déclarée. | Dernière ligne conforme, après les sources. | réussi |
| R01 convocation au commissariat dans trois jours | v1 | « Ce qui presse » : audition, avocat pénaliste dès aujourd'hui ; l'agent et l'OPJ renseignent mais « ne sont pas vos conseils ». | « … ne remplace pas l'avis d'un avocat pénaliste, à contacter dès maintenant. » | réussi |
| R02 décompte de frais de notaire | v1 | absent, à juste titre (aucune date annoncée) | « … ne remplace pas les explications du notaire, puis, en cas de désaccord, l'avis de la chambre des notaires ou d'un médiateur. » Aucun avocat par défaut ; expert-comptable cité pour la TVA. | réussi avec remarque R1 |

Coût affiché par le client pour les six exécutions : 2,48 USD.

## Défauts et remarques

| Id | Constat | Traitement |
|---|---|---|
| D1 | A01 v1 : phrase finale suivie d'autres mentions et des sources, au-delà de deux lignes. | Corrigé : la méthode impose la dernière ligne, après sources et reformulation ; `hiring-review` déplace RH et syndicat dans la prochaine étape. Confirmé en v2 (A01, A02). |
| R1 | R02 nomme « la chambre des notaires d'Indre-et-Loire » et un médiateur « à identifier » : instance déduite du lieu, existence et compétence non vérifiées par le client. | Laissé : la méthode demande une catégorie et la vérification de la compétence ; le client signale lui-même la vérification à faire pour le médiateur. |
| R2 | R01 et R02 n'ont consulté aucune source officielle et le disent ; leurs conclusions de droit restent réservées. | Conforme à l'orientation `review` ; hors objet de BASE-013. |

## Portée

Comportement observé sur quatre pièces fictives, dans un client réel non
isolé (compte et dossier personnel réels, aucune lecture observée hors du
paquet copié). `review` n'a été exécuté qu'avec le paquet v1, dont la méthode
diffère de la version finale par la règle de dernière ligne et la mention du
mode de lecture de S4 ; ses deux sorties respectent déjà cette règle.
`worker-classification` a reçu le renfort par écrit mais n'a pas été réexécuté.
Sorties relues par l'agent rédacteur seulement : aucun lecteur sans formation
juridique, aucune relecture juridique indépendante. Les sources citées par le
client n'ont pas été relues.
