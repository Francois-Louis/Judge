# BASE-004 — Identité, configurations et mises à jour du fork

> Cadrage historique antérieur à l'implémentation. BASE-008 a depuis migré les
> manifestes et chemins ; voir son [bilan](../base-008-isoler-identite-configurations.md)
> et les [preuves actuelles](../../../references/base008-validation.md). Les
> formulations « encore » et « futur » ci-dessous décrivent l'état audité.

Cadrage établi le **15 octobre 2026 (Europe/Paris)**. Les valeurs ci-dessous
sont les décisions cibles pour [BASE-008](../base-008-isoler-identite-configurations.md).
Le marketplace et les plugins livrés portent encore leurs noms d'origine.
Ce document ne constitue ni une installation ni une adaptation juridique.

## Identité retenue

| Élément | Origine observée | Cible du fork |
|---|---|---|
| Nom du marketplace | `claude-for-legal` | `judge-fr-eu` |
| Affichage dans les documents | Claude for Legal | Judge FR/UE — adaptations France / Union européenne |
| Maintenance du marketplace (`owner.name`) | Anthropic | `Judge FR/UE maintainers`, rôle de maintenance du fork |
| Identifiant d'un plugin interne | `<domaine>` | `judge-fr-eu-<domaine>`, identique dans les deux manifestes |
| Répertoire source d'un domaine | `<domaine>/` | Même répertoire ; `source` conserve son chemin relatif |
| Répertoire de configuration | `config/claude-for-legal/` | `config/judge-fr-eu/` |
| Noms des skills | Par exemple `hiring-review` | Conservés ; seul leur préfixe de plugin change |
| Version d'un paquet interne | `1.0.2` | Cycle du fork indépendant, première version technique `0.1.0` |

Changer uniquement le marketplace ne suffit pas : Claude Code utilise le nom
du manifeste pour l'espace des commandes et arbitre les conflits de noms
entre plugins. Nous choisissons donc aussi des identifiants de plugins distincts.
Voir la [référence des manifestes](https://code.claude.com/docs/en/plugins-reference#name)
et les [conflits de chargement](https://code.claude.com/docs/en/plugins/loading#name-conflicts),
consultés le 15 octobre 2026. Le préfixe est un choix du fork.

Correspondance exhaustive des 12 plugins internes ; la colonne de gauche sert
aussi de clé de dossier sous `config/judge-fr-eu/` :

| Répertoire / ancien identifiant | Nouvel identifiant de manifeste et d'entrée |
|---|---|
| `ai-governance-legal` | `judge-fr-eu-ai-governance-legal` |
| `commercial-legal` | `judge-fr-eu-commercial-legal` |
| `corporate-legal` | `judge-fr-eu-corporate-legal` |
| `employment-legal` | `judge-fr-eu-employment-legal` |
| `ip-legal` | `judge-fr-eu-ip-legal` |
| `law-student` | `judge-fr-eu-law-student` |
| `legal-builder-hub` | `judge-fr-eu-legal-builder-hub` |
| `legal-clinic` | `judge-fr-eu-legal-clinic` |
| `litigation-legal` | `judge-fr-eu-litigation-legal` |
| `privacy-legal` | `judge-fr-eu-privacy-legal` |
| `product-legal` | `judge-fr-eu-product-legal` |
| `regulatory-legal` | `judge-fr-eu-regulatory-legal` |

Les nouveaux domaines de BASE-003 garderont ce préfixe pour leur identifiant
publié ; leurs noms de répertoires restent à arrêter dans leurs cadrages.
Il n'est créé aucun plugin généraliste `france-eu-legal`.

Le plugin éditeur `cocounsel-legal` ne sera pas renommé ni modifié. Pour éviter
deux distributions actives de même nom, retirer seulement son entrée du futur
marketplace du fork ; son répertoire, sa documentation et ses attributions
restent conservés. Son installation éventuelle se fait depuis sa distribution
d'origine. Une adaptation éditeur nécessiterait un accord et une story distincts.

## Installation côte à côte

Les commandes suivantes sont des **exemples cibles après BASE-008**, pas des
commandes à exécuter sur ce checkout encore nommé `claude-for-legal` :

```text
claude plugin marketplace add <chemin-absolu-vers-la-version-migree-de-Judge>
claude plugin install judge-fr-eu-employment-legal@judge-fr-eu --scope user
```

Dans une session : `/judge-fr-eu-employment-legal:cold-start-interview`, puis
`/judge-fr-eu-employment-legal:hiring-review`. L'installation et les commandes
de l'original restent distinctes, notamment
`employment-legal@claude-for-legal` et `/employment-legal:hiring-review`.
La [syntaxe officielle d'installation](https://code.claude.com/docs/en/plugin-marketplaces#add-the-marketplace-and-install-the-plugin)
distingue le nom du plugin et celui du marketplace.

La documentation officielle consultée réserve `claude-for-legal` aux sources
Anthropic : l'ajout local de ce fork sous le nom hérité peut être refusé.
Le nouveau nom corrige aussi cette ambiguïté ; voir les
[noms réservés](https://code.claude.com/docs/en/plugins/marketplace-reference#reserved-names).
Ne pas remplacer l'enregistrement de l'original pour installer le fork.

BASE-008 devra vérifier les deux entrées installées et leurs commandes dans
une même session. Le choix de portée (`user`, `project`, `local`) devra rester
explicite dans les instructions ; une portée différente ne sépare pas les
chemins de profils actuellement codés en dur. Dans les autres clients, ne
promettre la coexistence qu'après un test de leurs règles de chargement.

## Stockage : inventaire et contrat cible

`~` désigne le dossier personnel de la plateforme, sans chemin propre au poste.
Les chemins de configuration sont une convention des prompts de ce dépôt,
pas un mécanisme automatique de migration fourni par Claude Code.

| Données / point de départ | Cible et règle |
|---|---|
| Profil métier `~/.claude/plugins/config/claude-for-legal/<domaine>/CLAUDE.md` | `~/.claude/plugins/config/judge-fr-eu/<domaine>/CLAUDE.md` ; lecture/écriture seulement dans ce namespace |
| Profil partagé `.../claude-for-legal/company-profile.md` | `.../judge-fr-eu/company-profile.md` ; partagé uniquement entre les domaines du fork |
| Modèle `<domaine>/CLAUDE.md` dans le paquet | Structure depuis `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` ; jamais un profil utilisateur à importer depuis un autre paquet |
| Cache hérité `~/.claude/plugins/cache/claude-for-legal/<plugin>/<version>/` | Cache cible `~/.claude/plugins/cache/judge-fr-eu/judge-fr-eu-<domaine>/<version>/` ; paquet remplaçable, aucune donnée durable à y écrire |
| Dossiers `matters/<slug>/`, `_archived/`, `history.md`, `notes.md`, sorties et journaux | Sous `config/judge-fr-eu/<domaine>/` ; mêmes slugs possibles dans l'original, sans lecture croisée |
| Registres de congés, enquêtes, expansions, renouvellements, politiques, propositions et vérifications | Même séparation pour **tous** les fichiers annexes, pas seulement les `CLAUDE.md` |
| Hub : `allowlist.yaml`, `install-log.yaml`, liste des skills et préférences | Sous `config/judge-fr-eu/legal-builder-hub/` ; aucun journal, allowlist ou consentement repris de l'original |
| Hub : installation actuelle dans `~/.claude/skills/[skill-name]/` | Futur dossier `~/.claude/skills/judge-fr-eu-<skill-name>/`, avec identité de skill cohérente ; refuser toute destination existante, même vide |
| Hub : sauvegarde actuelle `~/.claude/skills/.backups/[skill]-[old-sha]/` | `config/judge-fr-eu/legal-builder-hub/backups/<skill>/<sha>/` ; restauration limitée au chemin du fork enregistré dans son journal |
| Cookbooks : `./out/`, dont `handoff-audit.jsonl` ; éventuels `logs/` / `outputs/` du lanceur | Répertoire de travail et destinations distincts pour chaque déploiement ; ne jamais réutiliser ceux d'un agent original |
| Déploiement : `REPO_SLUG`, `SKILL_TITLE_PREFIX` | Identité explicite du fork, par exemple `judge-fr-eu` et `judge-fr-eu-`, sans confondre tags, titres et données |

Le cache décrit est le chemin standard documenté par la
[référence de chargement](https://code.claude.com/docs/en/plugins/loading#in-place-and-copied-plugins).
Son emplacement peut varier avec la configuration du client. Les registres
`known_marketplaces.json`, `installed_plugins.json` et les réglages
`enabledPlugins` restent gérés par le client ; ne pas les réécrire à la main.
Tout stockage propre au client hors de ces chemins doit être vérifié lors
du test d'installation de BASE-008.

L'isolation des données exige des chemins résolus sous la bonne racine,
sans `..`, chemin absolu fourni comme slug, lien symbolique ou jonction vers
un autre espace. Un contexte inter-dossiers activé ne permet pas de changer
de namespace. Le hub du fork ne doit ni installer dans les paquets internes
ni modifier les skills communautaires de l'original. Un nom préfixé ne suffit
pas : contrôler aussi le chemin canonique enregistré et l'identité du paquet.
Ces règles n'isolent pas les documents que l'utilisateur fournit expressément
aux deux installations, ni les services externes utilisant les mêmes comptes.

### Relevé reproductible des fichiers

L'[inventaire TSV](base-004-inventaire-references.tsv) énumère **218 fichiers**,
avec catégories et numéros de lignes. Parmi eux, **187 fichiers / 1 150 lignes**
contiennent le nom `claude-for-legal`. Les 24 fichiers parlant du cache
comprennent les 12 modèles de profils et les 12 entretiens de configuration.
Le relevé comprend aussi les commandes de domaines, l'installation, les
destinations communautaires et les sorties/déploiements des cookbooks.

Reproduction, sans modifier le dépôt :

```text
python scripts/check-base004-isolation.py --inventory
```

Le script lit les fichiers suivis et non suivis, non ignorés par Git. Il exclut
le backlog et son propre code de preuve pour éviter de compter le cadrage
comme une migration à faire. Il ne lit aucun profil installé. La colonne
`lignes_nom_origine` compte des lignes, pas des occurrences. Les numéros sont
ceux de ce checkout ; régénérer le relevé avant BASE-008. Les correspondances
sont des points de revue, pas une liste de remplacements automatiques.

## Migration des profils : création neuve par défaut

1. Rechercher seulement le profil du domaine dans `config/judge-fr-eu/`.
   S'il existe, conserver ses données et proposer la reprise de l'entretien.
   S'il manque, démarrer un entretien neuf France/UE. Ne chercher ni dans
   `config/claude-for-legal/` ni dans son cache.
2. Supprimer dans le futur paquet les consignes héritées de copie automatique
   depuis `cache/claude-for-legal/<plugin>/*/CLAUDE.md`. Elles figurent notamment
   aux étapes initiales des `cold-start-interview` et dans les modèles.
3. Une éventuelle reprise de l'original exige une demande explicite et un
   aperçu des fichiers/champs sélectionnés. Lire seulement ces sources, puis
   préparer le résultat dans une destination neuve. Aucune fusion implicite
   si un profil du fork existe : conserver les deux et préparer une comparaison.
4. Reprendre au plus des faits d'organisation confirmés par la personne.
   Requalifier territoires, rôle et dates ; ne pas importer automatiquement
   droit américain, seuils, délais, escalades, modèles ou raisonnement juridique.
   Dossiers clients, registres et sorties ne sont jamais copiés avec le profil.
5. Refuser les destinations existantes, les alias et liens entre racines.
   Conserver l'original ; journaliser provenance, sélection, validation et
   destination dans le fork. Une reprise interrompue ne remplace rien.

BASE-008 implémentera le démarrage neuf et la suppression des reprises
automatiques. Un outil d'import assisté n'est pas requis : s'il est souhaité,
il devra avoir sa propre story et les scénarios des points 3 à 5. Aucune
installation ni mise à jour ne vaut consentement à reprendre un profil.

## Attribution, maintenance et affichage

L'[Apache License 2.0](../../../LICENSE), notamment ses articles 4 et 6, reste
conservée. L'auteur d'origine (`Anthropic`) dans les manifestes internes et
les mentions de copyright existantes restent attribués à l'origine ; le rôle
de mainteneur du fork est distinct. Les entrées marketplace et manifestes
internes gardent les mêmes champs `name`, `description`, `author`.

Les documents de livraison indiqueront l'origine Claude for Legal / Anthropic,
le dépôt du fork, les fichiers et versions adaptés, et l'absence d'affiliation
revendiquée. Les fichiers modifiés porteront une mention visible de modification
par le fork. Fournir la licence avec chaque distribution, préserver les notices
pertinentes et tout `NOTICE` reçu avec une version amont ; aucun `NOTICE` n'a
été trouvé dans ce checkout. Le nom et l'affichage du fork ne transfèrent pas
les marques de l'original. Le changement d'identité ne certifie aucune tâche
juridique France/UE ; les statuts métier restent ceux du backlog.

## Politique de mise à jour

Trois opérations restent distinctes :

- **Intégrer l'amont au dépôt du fork** : relever le SHA de départ et le SHA
  candidat, travailler sur une branche, examiner le diff par domaine, intégrer
  les changements retenus et résoudre les conflits explicitement. Aucun reset,
  remplacement du dossier ou mise à jour aveugle vers la branche amont. Garder
  le diff des adaptations, les tests et la provenance dans le bilan du lot.
- **Mettre à jour un paquet du fork installé** : diffuser une version distincte,
  revue et bornée. Conserver les profils, dossiers et sorties hors du cache.
  Les éditions faites directement dans le cache ne sont pas une personnalisation
  durable : reporter ces changements dans une branche locale ou un paquet privé
  à identifiant distinct avant toute mise à jour. Prévoir retour au paquet
  précédent ; une évolution de format des données exige sa propre migration
  avec sauvegarde, sans restauration aveugle sur de nouvelles données.
- **Mettre à jour un skill communautaire via le hub** : conserver le diff,
  l'examen de confiance et l'approbation explicite déjà prévus par
  `legal-builder-hub/skills/auto-updater/SKILL.md`. Épingler le SHA exact ;
  refuser en cas de régression au contrôle. Vérifier le chemin et le journal
  du fork, sauvegarder sans collision, puis mettre à jour seulement cette
  installation. `--apply` ne contourne pas la revue ; pas de mode automatique.

Les agents planifiés signalent les nouveautés, sans les appliquer. Pour le
marketplace du fork, configurer les mises à jour automatiques du client comme
désactivées lors de la future recette ; vérifier ce réglage dans le client
plutôt que d'inventer un champ de manifeste. Une mise à jour de référence
juridique exige aussi sa vérification métier : une nouvelle version technique
ne prouve pas que le droit embarqué est à jour.

## Fichiers à modifier et ordre de réalisation

La liste exacte des références est dans le TSV ; les chemins paramétrés
ci-dessous couvrent les 12 domaines du tableau d'identité.

| Ordre | Fichiers / lot | Modification future et condition de passage |
|---|---|---|
| 1 | Inventaire TSV ; `.claude-plugin/marketplace.json` ; `<domaine>/.claude-plugin/plugin.json` | Geler la correspondance, préfixer les noms dans les deux manifestes, owner/affichage/version du fork ; exclure l'entrée éditeur sans toucher à son contenu |
| 2 | Les 12 `<domaine>/CLAUDE.md` et `skills/cold-start-interview/SKILL.md` | Basculer profils partagés/métier, supprimer toute copie/fallback du cache original, conserver le modèle embarqué et les profils existants |
| 3 | `<domaine>/skills/**`, `<domaine>/agents/**`, références locales signalées dans le TSV | Basculer toutes les lectures/écritures annexes et préfixes de commandes ; contrôler les renvois entre plugins, sans renommer les 150 dossiers de skills |
| 4 | `legal-builder-hub/skills/{skill-installer,auto-updater,skill-manager,disable,uninstall}/SKILL.md`, son modèle, agent et références concernés | Séparer installations, sauvegardes, allowlist/journal, identités et listes de plugins internes ; contrôler aussi les chemins sans ancien nom |
| 5 | `references/dashboard-template.md`, `README.md`, `QUICKSTART.md`, `CLAUDE.md`, les 12 README et autres fichiers signalés | Expliquer état réel, nouvelles commandes, stockage, provenance et mises à jour ; préserver les mentions historiques justifiées |
| 6 | `managed-agent-cookbooks/**`, `scripts/deploy-managed-agent.sh`, `scripts/orchestrate.py` | Revoir renvois, titres/tags et répertoires d'exécution ; vérifier hors ligne, sans lancer ni modifier d'agents distants |
| 7 | Tests de BASE-008, notices de modification, licence de chaque paquet | Validation des manifestes puis installation isolée avec les deux distributions, dossiers et versions ; publication seulement dans la livraison prévue |

Les étapes 1 à 6 sont préparées ensemble sur la branche d'implémentation :
ne pas publier un manifeste basculé avec des skills lisant encore l'ancien
namespace. BASE-005/006 traitent la méthode partagée et l'autonomie du paquet,
BASE-007 le CLA, LIV-001 la livraison. BASE-004 ne fait aucun remplacement
dans ces fichiers opérationnels.

## Simulation effectuée et limites

Commande locale, Python **3.12 ou ultérieur**, bibliothèque standard seulement :

```text
python scripts/check-base004-isolation.py
```

Le [script de preuve](../../../scripts/check-base004-isolation.py) construit deux
profils factices, deux profils d'organisation et deux dossiers de même slug
dans un répertoire temporaire. Un ancien profil factice est aussi placé dans
le cache original. Son modèle minimal trace les lectures/écritures ; le
vérificateur compare les empreintes des fichiers avant/après.

| Scénario exécuté | Résultat observé le 15 octobre 2026 |
|---|---|
| Profil du fork absent, original et ancien cache remplis | Profil absent signalé ; aucune reprise automatique |
| Deux profils et deux dossiers `demo` présents | Chaque instance lit exclusivement ses propres marqueurs, y compris le profil partagé |
| Création sur une destination déjà occupée | Refus, contenu du fork inchangé |
| Chemin absolu de cache original ou traversée `../claude-for-legal/` | Refus avant lecture |
| Nouvelle version de paquet factice et sortie du fork | Deux profils et cache original inchangés ; sortie créée dans le fork |
| Trace des opérations du fork | 10 accès, tous sous `config/judge-fr-eu/` |

Tous les scénarios passent et les fixtures sont supprimées automatiquement.
Le modèle vérifie le contrat de chemins proposé, **pas l'exécution des prompts
existants** : ceux-ci continuent de partager les chemins d'origine. Il n'y a
eu ni lecture de profils réels, ni installation, ni test dans Claude Code
(CLI indisponible sur ce poste), ni migration réelle. La recette de BASE-008
devra prouver ce comportement sur les paquets effectivement migrés, tester
liens/jonctions et refus d'import, puis vérifier l'installation côte à côte.
