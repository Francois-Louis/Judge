<!-- Added by Judge FR/UE for BASE-008, 2026-10-15. -->

# BASE-008 — preuves de migration technique

Relevé du **15 octobre 2026, Europe/Paris**. Source amont et HEAD de départ :
`4a6c651889c97cc9140580363c73e0eb17379c2b`. Le worktree contenait déjà les
travaux BASE-001 à BASE-007 ; ils sont conservés. Aucune release ni adaptation
juridique des 150 tâches n'est annoncée.

## Modifications livrées

- Marketplace `judge-fr-eu`, 12 identifiants `judge-fr-eu-<domaine>`, version
  technique `0.1.0`. Sources de domaines et noms des skills conservés.
  Les champs name/description/author des deux manifestes concordent ; auteurs
  Anthropic conservés, maintenance du fork distincte. L'entrée CoCounsel est
  exclue ; ses fichiers, la licence racine et CLA.md sont préservés.
- Configuration partagée, profils métier, dossiers actifs/archivés, registres,
  sorties et journaux sous `config/judge-fr-eu/`. Suppression des reprises
  depuis le cache. Profil absent : entretien neuf ; profil présent : réponses
  et progression conservées. Aucun outil d'import ajouté.
- Contrat de stockage embarqué chargé par les 150 skills et les agents,
  assistant Python autonome copié dans chaque paquet. Contrôle des ancêtres,
  traversées, chemins Windows, liens, jonctions, liens physiques et collisions.
  Remplacement conditionné par l'empreinte du fichier relu ; archivage sans
  écrasement. Modèles de profil/dashboard et méthode BASE-005 embarqués.
- Hub : identité/dossier communautaire préfixés, journal JSON compatible YAML
  propre au fork, chemins et empreintes enregistrés, sauvegardes sous sa config,
  cycle install/update/rollback/disable/enable/uninstall par assistant local.
  Les contrôles de confiance et accords du workflow restent requis. Les fichiers
  modifiés localement et les journaux étrangers sont refusés avant mutation.
- Cookbooks : identifiants, titres et tags du fork, répertoire propre à chaque
  identifiant de déploiement et cookbook. Le journal de l'orchestrateur local
  et ses chemins de rapports utilisent le même contrat. La protection distante
  doit être fournie par le workflow de déploiement : le payload n'est pas un
  mécanisme de confinement du système d'exploitation.

Les notices de chaque paquet et le [NOTICE racine](../NOTICE) énumèrent les
fichiers du lot. Les modifications sont identifiées dans les contenus modifiés ;
les textes historiques et la copie de la méthode commune restent intacts.
L'[inventaire avant migration](../backlog/00-fondations/base-008-annexes/base-008-inventaire-avant.tsv)
a été régénéré avant modification : **221 fichiers**. Le cadrage BASE-004 et
son inventaire restent des constats historiques.
L'[inventaire après migration](../backlog/00-fondations/base-008-annexes/base-008-inventaire-apres.tsv)
et le [relevé résiduel commenté](../backlog/00-fondations/base-008-annexes/base-008-residus.tsv)
permettent de revoir les références restantes sans confondre fixtures et accès actifs.

## Contrôles exécutables

```text
python scripts/test-base008-isolation.py
python scripts/test-check-plugin-package.py
python scripts/lint-tool-scope.py
bash scripts/test-cookbooks.sh
python scripts/check-base004-isolation.py --inventory
git diff --check
```

Python **3.12.9**, PyYAML, jsonschema, Git Bash et jq **1.8.2** utilisés.
Les dépendances manquantes ont été installées dans un répertoire temporaire,
sans installation globale. Les tests copient les **vrais paquets migrés** hors
du dépôt et n'utilisent que des profils factices. Les assistants de ces copies
effectuent les accès et les tests comparent les empreintes avant/après ; le
modèle de BASE-004 ne sert pas de preuve de cette implémentation.

| Vérification | Résultat et portée |
|---|---|
| Suite BASE-008 | 16 tests : 15 passent, 1 ignoré (création de lien symbolique refusée par Windows, WinError 1314) |
| Accès aux 12 profils par CLI embarquée | Profil absent malgré original/cache remplis ; création exclusive, lecture, historique et archive du fork ; original inchangé |
| Profil partagé, update/rollback de paquet | Deux profils partagés séparés ; version de paquet modifiée puis paquet précédent : profils, sorties et personnalisation durable inchangés |
| Hub communautaire | Même slug dans les deux distributions ; cycle complet du fork, empreintes originales inchangées ; destination vide, sauvegarde occupée, journal étranger, chemin falsifié et édition locale refusés |
| Chemins | Traversées, absolus, lecteurs Windows/UNC/flux alternatifs, destinations existantes, liens physiques et jonctions réelles refusés ; liens symboliques réels à rejouer sur un hôte compatible |
| Paquets détachés, contrôleur BASE-006 | Zéro erreur structurelle ; chemins dynamiques et appels interplugins restent des points de relecture, sans prétendre les avoir exécutés dans un modèle |
| Commandes | Tous les appels qualifiés documentés résolvent un dossier de skill existant ; noms des 150 skills conservés |
| Fixtures du contrôleur BASE-006 | 11 tests passent, y compris référence retirée et commande inventée |
| Cinq cookbooks | Résolution hors ligne : 5/4/4/4/4 corps d'agents ; noms, tags et sorties du fork ; portée des outils conforme |
| Sorties locales des cinq cookbooks | Deux déploiements distincts par cookbook, journaux du fork ; sorties originales inchangées ; réutilisation et traversée refusées |

Le contrôleur BASE-006 conserve ses statuts de relecture pour les chemins
dynamiques/profils et commandes interplugins. Leur présence n'est pas assimilée
à une preuve d'accès effectif par un skill. La suite BASE-008 contrôle les accès
des assistants embarqués ; le respect de ces instructions par le modèle reste
à vérifier dans la recette interactive.

### Environnement pour rejouer ces contrôles

Ajouté par BASE-009. Requis : Python **3.12+** avec PyYAML et jsonschema,
Bash (Git Bash sous Windows) et jq. Les scripts shell utilisent le premier
interpréteur `python3` ou `python` qui s'exécute, ou celui désigné par `PYTHON`.
Sans installation globale, par exemple :

```text
python -m pip install --target <dossier-temporaire>/pydeps pyyaml jsonschema
PYTHONPATH=<dossier-temporaire>/pydeps
PATH=<dossier-contenant-jq>:$PATH
```

Sans jsonschema, le test d'orchestrateur est ignoré ; sans droit de créer un
lien symbolique (mode développeur Windows ou shell administrateur), le test
correspondant est ignoré. Ces absences ne valent pas réussite.

Rejeu du 15 octobre 2026 après BASE-009, avec jq **1.8.1** et jsonschema
temporaires : 16 tests BASE-008, 15 réussis et 1 ignoré (lien symbolique) ;
dry-run des cinq cookbooks réussi ; 11 fixtures du contrôleur réussies.

## Client officiel jetable

La CLI a ensuite été installée **localement dans le répertoire temporaire** :
`@anthropic-ai/claude-code`, version réellement exécutée **2.1.301**.
`CLAUDE_CONFIG_DIR` pointe vers une configuration temporaire, distincte de la
configuration personnelle. `DISABLE_AUTOUPDATER=1` et
`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` sont définis pour chaque appel ;
aucune mise à jour automatique n'est active pendant cette recette.

- `claude plugin validate` passe sur le marketplace et sur les 12 paquets
  détachés. Avertissement attendu : CLAUDE.md est un modèle et n'est pas chargé
  automatiquement comme contexte de projet. Les skills chargent explicitement
  le contrat embarqué ; le modèle reste à son emplacement prévu.
- Ajout du marketplace local du fork, puis installation de
  `judge-fr-eu-employment-legal@judge-fr-eu --scope user` : réussis.
- Une tentative d'ajout de l'original depuis une copie locale est refusée :
  son nom est réservé aux sources officielles Anthropic. Cette observation
  confirme le besoin de distinguer le nom du fork ; l'original n'a pas été renommé.
- Ajout de `anthropics/claude-for-legal` depuis la source officielle, puis
  installation de `employment-legal@claude-for-legal --scope user` : réussis.
  Le SHA public de cette source correspond au HEAD indiqué plus haut.
- `claude plugin list --json` montre simultanément les deux identifiants,
  activés en portée user : original **1.0.2**, fork **0.1.0**, chemins distincts.
- `claude auth status --json` indique `loggedIn: false`, `authMethod: none`.
  Aucune authentification personnelle n'a été utilisée. Le chargement dans une
  session de modèle et les appels aux commandes qualifiées ne sont donc pas
  présentés comme exécutés.

La [preuve structurée](../backlog/00-fondations/base-008-annexes/base-008-resultats-client.json)
conserve les résultats du client, avec chemins temporaires anonymisés.

## Recette interactive restante

Dans une configuration jetable authentifiée, installer les deux sources comme
ci-dessus, vérifier la désactivation des mises à jour automatiques du fork,
noter `claude --version`, puis recharger les plugins. Avec des profils factices
et un home de test séparé au niveau du système, invoquer les deux commandes
`/employment-legal:hiring-review` et
`/judge-fr-eu-employment-legal:hiring-review` dans la même session. Observer les
accès aux fichiers, pas seulement les déclarations du modèle.

Rejouer les cas de profil absent/cache rempli, deux profils partagés et deux
dossiers de même slug, absence d'écrasement, sorties annexes, update/rollback,
et cycle communautaire. `CLAUDE_CONFIG_DIR` ne déplace pas les chemins
`~/.claude/plugins/config/judge-fr-eu/` : seul un home de test isole les profils. Comparer les empreintes et traces réelles de chaque
namespace. Rejouer les liens symboliques sur un hôte autorisant leur création.
Les tests automatiques fournissent les fixtures et opérations attendues.

Les sources officielles ont été consultées le 15 octobre 2026 :
[nom et composants de manifeste](https://code.claude.com/docs/en/plugins-reference#name),
[installation depuis un marketplace](https://code.claude.com/docs/en/plugin-marketplaces),
[nom d'entrée, conflits, cache et mises à jour](https://code.claude.com/docs/en/plugins/loading),
[champs et noms réservés du marketplace](https://code.claude.com/docs/en/plugins/marketplace-reference),
[distribution officielle de la CLI](https://github.com/anthropics/claude-code/blob/main/README.md).
Les contrôles réellement exécutés sont ceux relevés ci-dessus ; la lecture de
ces références n'est pas une preuve de comportement juridique.

Aucun profil personnel, déploiement distant, publication, push, PR ou réglage
GitHub modifié. Le déploiement Managed Agents, les autres clients et les tâches
France/UE restent hors de la validation réalisée.
