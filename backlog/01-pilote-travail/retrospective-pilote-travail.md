# Rétrospective de l'epic 01-pilote-travail

Établie le **15 octobre 2026 (Europe/Paris)** sur PILOTE-001 à PILOTE-004.
Elle s'appuie sur la relecture des stories, bilans et preuves, du skill
`hiring-review`, des références embarquées et des NOTICE, puis sur une nouvelle
exécution des contrôles. Les corrections qui ne demandaient aucune décision sont
tracées dans [PILOTE-005](pilote-005-corrections-retrospective.md).

## Bilan

Le pilote a produit ce qu'il visait sur le papier : une tranche verticale
relisible, un paquet détaché qui passe les schémas officiels et des défauts
reliés à des stories existantes. **Mise à jour du 16 octobre 2026 :** après
la recette [BASE-011](../00-fondations/base-011-recette-client-isole.md),
l'utilisateur a clos PILOTE-002 à PILOTE-004 ; sans lecteur indépendant ni
nominal H01 complet. Au moment de la rétrospective, **l'epic n'était pas clos.** Trois stories sur
quatre attendent la même recette, et rien dans le backlog n'en porte les moyens.

| Story | Statut | Point ouvert |
|---|---|---|
| PILOTE-001 | terminee | — |
| PILOTE-002 | a-verifier | Client isolé, nominal H01 complet (D02), lecteur réel |
| PILOTE-003 | a-verifier | Installation et scénarios sans profil / sans source |
| PILOTE-004 | a-verifier | Comportement du modèle dans un client, essai sans exécuteur Python, lecteur réel |

Contrôles rejoués : 63 fichiers (epic, README du backlog, plugin, NOTICE),
270 liens locaux, aucun absent ; tableaux de largeur cohérente. 85 stories à
identifiants distincts avant PILOTE-005. Régression BASE-008 : 14 réussis,
2 ignorés sur 16. Contrôleur BASE-006 : 11 réussis. Helper PILOTE-004 :
7 réussis. Lint des cookbooks propre, JSON valides. `claude plugin validate`
passe sur les 12 plugins, le marketplace et les deux artefacts exacts du pilote
([preuve](pilote-003-annexes/pilote-003-schema-cli.json)), avec le seul avertissement attendu sur
`CLAUDE.md`.

Après PILOTE-005 : 65 fichiers, 284 liens locaux, aucun absent ; 86 stories
distinctes ; plus aucun CRLF ; `git diff --check` propre ; mêmes résultats de
tests ; `claude plugin validate` toujours réussi sur le marketplace et
`employment-legal`.

## Ce qui a bien marché

- **Découpage tenu.** Un seul skill réécrit ; les 19 autres et l'agent congés
  restent hérités et signalés. Aucune extension n'a été lancée par défaut.
- **Références embarquées.** Repères métier, contrat candidat, méthode BASE-005
  et frontière de stockage sont dans le paquet ; le paquet détaché ne requiert
  aucun fichier du dépôt.
- **Preuves identifiables.** Inventaire et empreintes du paquet, ZIP, révision
  de départ ; preuves techniques, sorties relues et sources lues séparées.
- **BASE-010 utile dès le premier usage.** Les 403 de Légifrance ont été
  contournés par le CDTN et tracés ; les décisions illisibles restent réservées.
- **Défauts rattachés sans doublon.** D01–D07 vont vers PILOTE-002/003, la
  nouvelle PILOTE-004, TRAV-008 précisée et TRAV-017 proposée.
- **Parcours candidat.** Pas de playbook d'entreprise, persistance volontaire,
  préservation des réponses existantes vérifiée par 7 tests du helper.

## Écarts constatés

1. **Un seul goulot bloque quatre stories, sans propriétaire.** BASE-008,
   PILOTE-002, PILOTE-003 et PILOTE-004 attendent toutes un client jetable et
   authentifié, isolé du checkout et du vrai dossier personnel. PILOTE-002 et
   PILOTE-004 attendent aussi un lecteur réel. Aucune story ne prépare cet
   environnement ou ce recrutement. PILOTE-004 a été ouverte alors que PILOTE-003
   n'était pas close. Elle ajoute un troisième `a-verifier` sur le même blocage :
   le travail en cours augmente sans pouvoir être clos.
2. **Aucun commit, une troisième fois.** PILOTE-002 à PILOTE-004 n'existent que
   dans le worktree : 16 fichiers modifiés et 17 nouveaux avant cette
   rétrospective, sur une branche nommée
   `usages-quotidiens/usage-001-003`. Les preuves JSON référencent donc une
   révision « plus état non commité » que git ne permet pas de reconstituer.
   C'est l'écart 1 des deux rétrospectives précédentes. La règle n'est toujours
   pas appliquée au fil de l'eau.
3. **Empreintes calculées sur des fins de ligne CRLF.** `NOTICE`,
   `employment-legal/NOTICE`, `marketplace.json` et le `plugin.json` du plugin
   sont passés entièrement en CRLF dans le worktree, alors qu'ils sont en LF dans
   `HEAD`. Avec `core.autocrlf=input`, le commit les remettra en LF. Le
   `plugin.json` versionné ne correspondra donc plus à l'empreinte du paquet de
   PILOTE-003/004, ni le marketplace à la sienne.
4. **« CLI absente » admis sans recherche.** Le binaire `claude` embarqué par
   l'application desktop existait pendant tout l'epic. Une recherche hors du
   PATH aurait permis d'exécuter les schémas dès PILOTE-002. Trois bilans ont
   reporté le même `NON_EXECUTE`. La reprise du jour a dû modifier cinq fichiers
   et en a oublié un (`pilote-004-verification.md`).
5. **Critères cochés sur le compte rendu, pas sur le résultat.** Les quatre
   cases de PILOTE-003 portent sur le fait de rapporter, pas sur l'installation
   et les deux scénarios exigés par sa section Vérification. Toutes sont
   cochées alors que rien de cela n'a été exécuté. Le bilan le précise, mais le
   modèle de story ne l'empêche pas.
6. **Densité, y compris dans le prompt livré.** L'epic compte environ
   25 000 mots dans 31 fichiers Markdown, dont cinq documents de vérification
   de 1 000 à 2 000 mots. Le statut `a-verifier` et ses causes sont répétés dans
   la story, la vérification, le bilan, le découpage, le README du backlog et
   NOTICE (écart 4 en est la conséquence directe). Surtout, `hiring-review`
   fait environ 2 000 mots avec une centaine de tournures restrictives. C'est
   l'écart 6 de l'epic 05, désormais dans un contenu chargé en contexte à
   chaque invocation, où l'excès de réserves peut diluer les consignes utiles.
   Son effet n'est pas mesuré faute de client.
7. **Décomptes et NOTICE désynchronisés.** Le README du backlog annonce
   84 stories, dont 67 `proposee`, alors qu'il y en a 85, dont 68. L'écart
   d'une story existait déjà dans `HEAD` (82 annoncées pour 83). Le NOTICE
   du plugin recense PILOTE-004, mais pas le NOTICE
   racine, qui omet aussi `scripts/test-pilote004-preferences.py`.
8. Points mineurs : `pilote-003-bilan-pilote.md` se termine par une ligne
   vide. Les skills hérités `internal-investigation` et `worker-classification`
   n'ont pas de fin de ligne finale ; non modifiés, ils sont laissés en l'état.

## Suites

| Action | Traitement |
|---|---|
| Écart 3 : fins de ligne | Corrigé dans PILOTE-005 (LF) ; nouvel inventaire du paquet exigé à la prochaine recette |
| Écart 4 : mentions périmées de la CLI | Corrigé dans PILOTE-005 ; règle de recherche d'un outil ajoutée au [modèle de story](../story-template.md) |
| Écart 5 : critères d'une story de validation | Règle ajoutée au modèle de story ; cases de PILOTE-003 laissées telles quelles, le bilan faisant foi |
| Écart 7 et point mineur | Corrigés dans PILOTE-005 |
| Écart 6 : densité | Décidé le 16 octobre 2026 : `hiring-review` est gardé tel quel, densité acceptée comme coût de la prudence |
| Écart 1 : environnement de recette | Décidé : story transverse [BASE-011](../00-fondations/base-011-recette-client-isole.md), client jetable où l'utilisateur s'authentifie ; aucune nouvelle story `a-verifier` sur ce blocage d'ici là |
| Écart 1 : lecteur réel | Décidé : l'utilisateur lui-même, résultat marqué non indépendant, dans BASE-011 |
| Écart 2 : commits | Réalisé : quatre lots sur `usages-quotidiens/usage-001-003`, poussés le 16 octobre 2026 |
| Option `--claude` ou variable d'environnement pour le contrôleur BASE-006 | Réalisé dans [BASE-012](../00-fondations/base-012-designer-cli-claude.md) |
| NOTICE | Décidé : fichiers hors `backlog/` seulement, règle dans `CLAUDE.md` |
