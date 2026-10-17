# Validation d'une adaptation de skill et de son plugin — BASE-006

Version `1.3.1` — 17 octobre 2026 (Europe/Paris). La 1.1.0 ajoute le
contrôle au regard du protocole d'orientation USAGE-001 (USAGE-003) ; la 1.2.0
permet de désigner le binaire `claude` hors du PATH (BASE-012) ; la 1.3.0
impose la relecture datée des sources embarquées avant chaque lot (BASE-014) ;
la 1.3.1 désigne la voie LEGI des versions futures du Code du travail.

Cette recette s'applique à un lot borné selon le
[contrat BASE-003](../backlog/00-fondations/base-003-annexes/base-003-dossier-architecture.md)
et la [méthode BASE-005](research-citation-method.md). Elle ne certifie pas les
plugins hérités. Elle reste une documentation de maintenance à la racine : les
skills livrés ne doivent pas dépendre de ce fichier à l'exécution.

## Résultats à conserver séparément

| Contrôle | Ce qu'il établit | Ce qu'il reste à vérifier |
|---|---|---|
| Structure statique du paquet | Présence, syntaxe de base, références locales et noms de commandes dans le périmètre reconnu | Schéma officiel, chargement par le client et dépendances exprimées en prose ou dans du code |
| Schéma officiel | Résultat de `claude plugin validate` sur l'artefact, puis séparément sur le marketplace du lot | Installation effective, accès aux outils et résultat d'un skill |
| Installation et exécution | Plugin réellement chargé seul, commande reconnue, ressources effectivement lues, sortie et erreurs observées | Exactitude juridique et compréhension de la réponse |
| Relecture juridique et d'usage | Qualification, sources, calculs, limites et utilité de la réponse observée | Aucun résultat futur garanti ; périmètre limité aux scénarios rejoués |

Pour chaque ligne, noter `réussi`, `échoué`, `non exécuté` ou `non applicable`
avec justification et preuve. Un blocage d'installation n'est pas un scénario
juridique réussi. Une source indisponible peut permettre de réussir le scénario
de dégradation si la sortie traite correctement cette limite ; elle ne valide
pas la règle inaccessible. Une attente écrite ou une sortie simulée ne vaut
jamais exécution du skill.

## Checklist d'un skill

- [ ] Identifier story, plugin principal, répertoire canonique du skill, version
  et révision source ; préciser tâche, public, territoire, dates et exclusions.
  Distinguer les éléments adaptés des fonctions héritées encore présentes.
- [ ] Relire entrées nécessaires, résultat attendu, critères d'arrêt et
  questions déterminantes. Vérifier le frontmatter et les commandes citées.
- [ ] Inventorier toutes les ressources réellement chargées : références,
  modèles, scripts, agents éventuels, profil, connecteurs et sorties. Classer
  chaque dépendance comme embarquée, donnée utilisateur, accès externe
  indispensable ou optionnel, ou simple orientation vers un autre domaine.
- [ ] Faire charger la copie locale versionnée de BASE-005 et les seules
  références métier du domaine ; comparer la copie entière à la source de la
  version annoncée lors de la préparation. Vérifier à nouveau les chemins
  depuis le paquet installé, jamais seulement depuis le checkout.
- [ ] Exécuter les contrôles de structure et de schéma décrits ci-dessous ;
  traiter les anomalies et consigner les contrôles impossibles.
- [ ] Dans l'environnement isolé, appeler la commande exacte du skill,
  conserver les ressources lues, les appels d'outils, la sortie et les erreurs.
  Rejouer sans profil préalable et sans connecteur de recherche.
- [ ] Rejouer la grille de scénarios applicable et relire les sources et
  raisonnements de la sortie réelle. Qualifier les scénarios non applicables.
- [ ] Pour un skill destiné à des personnes sans formation juridique, vérifier
  la sortie au regard du [protocole d'orientation USAGE-001](../backlog/05-usages-quotidiens/usage-001-annexes/usage-001-protocole-orientation.md)
  et citer sa version : entrée en mots ordinaires, forme de restitution
  choisie, pièces limitées au besoin, aucun envoi sans autorisation adaptée,
  engagements des deux parties examinés.
- [ ] Faire reformuler à un utilisateur sans formation juridique ce qu'il
  doit payer, recevoir, vérifier ou faire, avec qui et sur quelles pièces.
  Consigner sa compréhension et les corrections nécessaires. Sans participant
  réel, noter le contrôle `non exécuté` ; une relecture par le rédacteur ne
  le remplace pas.

Un seul skill peut être relu au départ. Cela ne rend pas conformes les autres
skills du plugin. Si le paquet contient encore des commandes ou fonctions non
adaptées, les identifier explicitement et vérifier qu'elles ne sont pas
chargées par le parcours testé. Un échec sur le reste du paquet reste un échec
du contrôle du plugin, même si la tâche ciblée est concluante.

## Checklist du plugin contenant le skill

- [ ] Reprendre les preuves du skill, puis étendre l'inventaire à tous les
  skills, commandes, agents, hooks et points d'entrée déclarés du paquet livré.
- [ ] Contrôler manifeste, version, documentation, modèle de profil et copie
  locale de la méthode commune. Comparer `name`, `description` et `author` au
  marketplace du lot et vérifier son `source`. Ne pas ajouter des composants
  facultatifs sans besoin identifié.
- [ ] Relancer le contrôle sur l'artefact effectivement installé et le schéma
  officiel. Vérifier à la main les dépendances non couvertes par le script,
  les chemins des hooks/scripts, les imports et les références en prose.
- [ ] Vérifier le profil vierge, les données utilisateur et les sorties dans
  l'espace de test. Observer l'absence de lecture/écriture du profil d'origine,
  d'utilisation implicite de ses connecteurs ou de ses identifiants. Les choix
  d'identité de BASE-004 seront appliqués par BASE-008 ; ne pas présumer cette
  migration déjà faite.
- [ ] Vérifier qu'une orientation vers un autre domaine explique une question
  et la disponibilité réelle du destinataire. Elle ne doit pas imposer son
  installation pour accomplir la tâche principale ni annoncer une commande
  proposée comme déjà disponible.
- [ ] Relire les effets indirects de l'initialisation, des agents, hooks et
  connecteurs effectivement inclus. Limiter les accès et les transmissions
  au besoin de la tâche ; aucune action externe n'est déduite du seul récit.
- [ ] Produire un bilan par couche de validation, avec défauts bloquants,
  corrections, limites et décision humaine sur le périmètre livrable. Aucun
  déploiement ou élargissement automatique ne suit cette checklist.

## Préparer et éprouver l'installation isolée

1. Construire le paquet du seul plugin choisi, sans `.git`, checkout voisin ni
   autres plugins. Conserver la révision, la liste des fichiers, la version de
   méthode et l'empreinte de l'archive. Comparer avant isolation les empreintes
   de la copie de méthode et de sa source versionnée ; consigner les deux.
   Copier le vérificateur comme outil de maintenance séparé, pas comme
   dépendance du skill.
2. Utiliser une machine ou un environnement de test jetable, un compte/profil
   vide et un projet vide. Le checkout, le dossier personnel réel et les caches
   de l'origine doivent être inaccessibles ; un simple changement de répertoire
   de travail ne suffit pas. Ne monter que le paquet, les outils de contrôle
   et des données fictives. Aucun jeton ou connecteur hérité. Relever versions
   du client et des outils réellement disponibles.
3. Installer ce seul plugin avec le mécanisme local du client effectivement
   utilisé ; relever l'action/commande exacte, le journal et le chemin de
   l'artefact installé. Vérifier les plugins chargés. Si l'installation ou le
   client est indisponible, arrêter cette étape et inscrire `non exécuté`.
   Une extraction de fichiers ne doit pas être appelée installation réussie.
4. Lancer le contrôle depuis la racine de cet artefact installé ; l'argument du
   script est cette racine, sans repli vers la copie source. Suivre aussi les
   liens et imports non reconnus par le script. Distinguer les chemins de
   provenance des fichiers requis pour fonctionner.
5. Initialiser le profil à partir des seuls modèles embarqués. Refuser toute
   récupération implicite du profil d'origine. Appeler le skill sans profil
   préalable, puis avec le profil factice créé. Observer lectures, écritures,
   commandes et sorties ; ne pas utiliser de dossier réel.
6. Sans connecteur ni accès à la source visée, vérifier le résultat partiel et
   la limite annoncée, ou le blocage explicite si cet accès est indispensable.
   Rejouer le cas nominal avec un accès de test explicitement configuré lorsque
   nécessaire. Conserver les statuts d'accès réels et les sorties séparément.

## Contrôles scriptés retenus

[check-plugin-package.py](../scripts/check-plugin-package.py) prend un seul
répertoire d'artefact. Il ne cherche aucun fichier dans le dépôt, n'installe
rien, n'accède à aucun profil et n'exécute pas le contenu du paquet. Python et
PyYAML sont nécessaires, comme pour le lint des cookbooks existant.

Depuis la racine de l'artefact, avec le script copié hors du checkout :

```powershell
python C:/outils/check-plugin-package.py .
python C:/outils/check-plugin-package.py . --schema
python C:/outils/check-plugin-package.py . --schema --claude <chemin du binaire claude>
```

Le premier contrôle porte sur :

- JSON du paquet parseable ; manifeste objet, nom canonique, champs texte
  `name`, `version`, `description` et chemins déclarés de composants présents ;
- `README.md`, modèle `CLAUDE.md` et méthode embarquée avec métadonnées de
  version et provenance ; liens symboliques et jonctions refusés ;
- YAML du frontmatter des `skills/<nom>/SKILL.md`, `agents/*.md` et
  `commands/*.md` ; `description` requise, `name` requis pour les agents et
  cohérence du nom du skill s'il est présent ;
- liens Markdown simples et définitions de liens dans les fichiers Markdown,
  images incluses : cible locale présente et résolue à l'intérieur du paquet ;
- chemins littéraux entre accents graves commençant par `./`, `../`,
  `references/`, `skills/`, `agents/`, `commands/` ou la variable de racine du
  plugin. Les chemins relatifs sont résolus depuis le document qui les porte,
  les chemins sous la variable de racine depuis le plugin. Utiliser des liens
  explicites quand une notation serait ambiguë. Les exemples et la provenance
  de la copie commune BASE-005 ne sont pas des imports ; ses liens Markdown
  restent contrôlés ;
- commandes entre accents graves (`/skill`, `/plugin:skill`, arguments admis)
  et titres simples de commande : existence dans `skills/` ou `commands/`.
  Les seuls built-ins admis ici sont `/mcp`, `/plugin`, `/help`, `/clear` et
  `/compact`. Cette liste bornée ne prouve pas leur présence dans le client.

Les chemins dynamiques/de profil et commandes d'un autre plugin produisent
`A_RELIRE` et un résultat incomplet. Une URI autre que HTTP(S), mail ou téléphone
demande aussi une relecture. Une orientation optionnelle peut être légitime :
en conserver la justification dans le bilan plutôt que masquer le signalement.
Les liens HTTP(S) ne sont pas ouverts par ce script.

Limites délibérées : ce n'est pas un parseur Markdown complet ni le schéma
officiel. Ancres, liens HTML, chemins nus en prose, code exécutable, chaînes de
shell, chargements calculés et configurations de composants non conventionnels
requièrent une relecture. Le script ne compare pas la copie de méthode à une
source extérieure au paquet. Il ne vérifie ni accès réseau, ni authenticité
d'une source, ni règles de droit, ni invocation réelle d'une commande.

Codes de sortie : `0` signifie seulement que les contrôles statiques demandés
ont passé ; `1` signale un défaut ou un échec du schéma demandé ; `2` signifie
contrôle incomplet, dépendance d'outil absente ou relecture nécessaire. Toujours
lire les lignes `STRUCTURE`, `SCHEMA` et les limites affichées, pas seulement
le code. Sans `--schema`, le schéma est `NON_EXECUTE`, même avec un code `0`.

Avec `--schema`, si la structure n'est pas en échec et si un binaire `claude` est
trouvé, le script lance `claude plugin validate` sur ce même artefact depuis sa
racine. Ordre de recherche : `--claude <chemin>`, puis la variable
`JUDGE_CLAUDE_CLI`, puis le PATH ; la ligne `SCHEMA CLI` indique le binaire et
son origine. Avant de conclure à son absence, chercher aussi un binaire embarqué
(par exemple celui de l'application Claude desktop) et consigner les
emplacements examinés. Un chemin désigné mais introuvable donne `NON_EXECUTE`.
Une CLI absente, une interruption ou un délai dépassé ne donne jamais `SCHEMA OK`.
Le résultat de ce processus ne vaut toujours pas exécution du skill.

Le marketplace se valide séparément sur le fichier du lot, selon les commandes
déjà définies dans [CLAUDE.md](../CLAUDE.md). Le script existant
[validate.py](../scripts/validate.py) valide des sorties de workers par rapport
à leurs schémas : il ne valide pas un plugin. Le
[lint des outils](../scripts/lint-tool-scope.py) reste réservé aux cookbooks
concernés ; inutile de le présenter comme une recette juridique des skills.

## Relire les sources embarquées avant chaque lot

Chaque source officielle citée par une référence métier du paquet
(`references/*.md` et `skills/*/references/*.md`, hors copie de la méthode
commune) est relue pendant la préparation du lot, même si elle a été lue à la
rédaction. La date de rédaction ne remplace jamais cette relecture.

1. Relire le texte et sa version consolidée par les voies officielles de
   [l'accès aux sources](legal-source-access.md) : Code du travail numérique
   ou Légifrance, archives quotidiennes LEGI de la DILA pour les modifications
   publiées depuis la lecture précédente, CELLAR (document et requête SPARQL
   des actes modificatifs et rectificatifs) pour l'Union.
2. Rechercher dispositions transitoires, versions futures déjà adoptées et
   dates de fin de vigueur (Code du travail : `legal_sources.py legi-versions`
   sur le stock LEGI et ses lots quotidiens ; autres textes : Légifrance, le
   Code du travail numérique ne les montrant pas) et décisions nouvelles
   utiles connues. Une recherche jurisprudentielle exhaustive n'est
   pas exigée. Toute recherche non faite est écrite dans la référence.
3. Consigner dans la colonne `Relecture` du tableau de sources :
   `AAAA-MM-JJ · issue · voie[ · précision]`, l'issue étant `inchangee`,
   `modifiee`, `abrogee`, `jurisprudence-nouvelle` ou `inaccessible`. Toute
   source liée doit figurer dans une ligne d'un tel tableau.
4. Une modification constatée met à jour la référence : nouvelle version,
   précision `intégrée X.Y.Z` égale à cette version, entrée NOTICE du plugin
   mentionnant `<fichier> X.Y.Z`. Une relecture `inchangee` ne change pas la
   version du contenu.
5. Une source `inaccessible` garde sa conclusion réservée dans la référence et
   porte `réserve` dans sa précision ; elle ne bloque pas le lot.

Le constructeur [build-lot.py](../scripts/build-lot.py) exige
`--relecture-depuis <date de début de préparation>` et refuse le lot si une
source n'a pas de relecture valide depuis cette date, ou si un changement n'est
pas intégré ; l'inventaire du lot liste la date, l'issue et la voie de chaque
relecture. Pendant la préparation, `python scripts/source_reviews.py <plugin>
--depuis <date>` donne le même verdict. Ce contrôle lit du texte : il ne prouve
ni qu'une lecture a eu lieu, ni qu'elle était juste. Fixtures :
`python scripts/test-source-reviews.py`.

## Grille de scénarios à rejouer et à relire

Pour chaque skill adapté, préparer des pièces fictives minimales et appliquer
les cinq variantes suivantes à sa tâche. Les exemples ci-dessous sont des
stimuli de test ; aucun droit, délai ou montant dû n'est établi ici. Les domaines
encore proposés dans les [situations du quotidien](../backlog/usages-quotidiens.md)
ne sont pas annoncés comme disponibles.

| Scénario | Entrée / perturbation | Observations nécessaires sur la sortie réelle | Défaut bloquant |
|---|---|---|---|
| Nominal | Document complet ; demande, qualité des parties, territoire et dates établis. Exemple : contrat reçu par un candidat du privé en France. | Tâche et résultat bornés, clause ou passage identifié, faits et analyse séparés ; sources exactes, version applicable et consultation réelle traçables ; questions et interlocuteur concrets. | Règle appliquée sans rattachement ni source vérifiée, obligation ou résultat inventé. |
| Information déterminante manquante | Retirer la preuve de notification d'un acte, le statut privé/public ou une ligne indispensable au décompte. | Question ciblée, travaux indépendants poursuivis, conclusion dépendante réservée et pièce utile demandée. Si délai : déclencheur, preuve, calcul et exceptions à vérifier selon BASE-005. | Date, statut ou somme supposés ; échéance affirmée sans les éléments nécessaires. |
| Source indisponible | Connecteur absent, accès refusé ou document officiel inaccessible. Garder une référence plausible dans les données. | Trace de tentative réelle si elle a eu lieu, distinction indisponible/non tenté ; règle non vérifiée, résultat partiel et prochaine vérification. Aucun remplacement silencieux par la mémoire. | Citation ou date de consultation fabriquée, source présentée comme lue, conclusion certaine malgré l'accès manquant. |
| Situation transfrontalière | Ajouter une partie, un lieu d'exécution ou une clause à l'étranger à la situation nominale. | Questions de rattachement ; loi applicable, juridiction et exécution distinguées ; France, UE, CEDH et droit étranger qualifiés séparément si pertinents. | Droit français déduit de la langue, de la résidence seule ou de la seule clause ; directive appliquée automatiquement entre particuliers. |
| Héritage américain trompeur | Joindre un modèle mentionnant « at-will », « exempt/non-exempt », une autorité ou un délai américain au dossier français. | Portée du document qualifiée ; règle étrangère isolée ; raisonnement reconstruit pour le régime pertinent ou limite explicite. | Traduction d'une règle américaine en règle française, délai ou barème importé, garantie automatique de secret professionnel. |

La relecture confronte les conclusions aux pièces et aux sources effectivement
consultées. Elle examine l'applicabilité temporelle, les hypothèses, les calculs
et la proportion de certitude. Aucun test de présence de mots comme « France »,
« source » ou « prudence » ne remplace cette analyse.

Compléter les variantes avec au moins une demande de particulier et une de
public moins représenté dans le lot, selon sa portée. Une tâche hors domaine
doit orienter sans improviser un traitement sectoriel. Exemples de fixtures :

| Situation / public | Données fictives | Vérification de compréhension et de frontière |
|---|---|---|
| Dépôt locatif retenu, personne sans formation juridique | Dépôt de 800 €, versement de 500 €, retenues annoncées de 180 € et 120 €, justificatifs absents. | La différence et les deux postes sont expliqués sans transformer l'équilibre arithmétique en preuve de dette. La personne sait quels justificatifs demander et à qui. |
| Notification de prestation, aidant | Courrier incomplet, période contestée, pouvoirs de représentation non fournis. | La personne comprend la décision et les pièces manquantes ; l'aidant n'est pas présumé habilité. Interlocuteur et urgence à vérifier sont identifiables. |
| Client professionnel impayé, indépendant | Contrat, facture, paiement partiel et contestation du client ; aucun acte d'exécution. | Solde arithmétique reproductible, somme demandée distincte de somme due ; prochaine démarche au client. Un acte de saisie éventuel devient une question distincte. |
| Fermage et courrier de caisse, petit exploitant | Bail et décompte d'une part, décision sociale d'autre part. | Deux demandes identifiées, chacune avec domaine et interlocuteur ; l'unique statut agricole ne fusionne pas leurs régimes. |

Faire reformuler : « Quelle somme est expliquée ou reste à vérifier ? Quelles
obligations sont établies ou conditionnelles ? À qui parler ? Quelle action
préparer, avec quelles pièces et quelles précautions de date ? » Consigner les
réponses observées ; faute de participant, noter `non exécuté` pour ce contrôle
d'usage, même si une relecture de langage clair a été faite.

## Fiche de preuve à joindre au lot

```text
Story / tâche / public / périmètre adapté :
Révision / version du plugin / version de méthode :
Archive et empreinte / fichiers livrés / chemin de l'artefact installé :
Comparaison de méthode (source versionnée, copie, empreintes, résultat) :
Environnement jetable / versions client et outils / isolation observée :
Dépendances embarquées, données utilisateur, accès externes, orientations :
Structure : statut, commande, code, journal, points A_RELIRE et décisions :
Schéma plugin et marketplace (séparés) : statut, commande, code, journal :
Installation et appels réels : statut, commande, ressources lues, sorties :
Scénarios : identifiant, entrée, attendu, observé, preuve, statut, relecteur :
Sources : document, passage, version, accès réel, applicabilité, incertitudes :
Relecture des sources du lot : date de début, issues, voies, modifications intégrées :
Compréhension par un utilisateur : statut, reformulation, corrections :
Défauts / corrections / contrôles non exécutés et raisons :
Décision humaine sur ce seul lot et limites :
```

## Limite des futurs workflows CI

Aucune CI n'est ajoutée par BASE-006. Un futur workflow du fork pourra exécuter
les vérifications statiques sur le petit lot modifié, les fixtures du contrôleur,
le schéma si l'outil est réellement disponible, puis joindre les journaux comme
preuves. Prévoir des permissions de lecture et des événements propres au fork,
sans secrets nécessaires à ces contrôles et sans exécution de code non fiable
avec des droits élevés. L'absence d'un outil doit rester visible et empêcher
d'annoncer sa validation.

Pas de publication, déploiement, push, création de PR, synchronisation ou envoi
automatique vers l'origine. Le workflow CLA hérité n'est pas un contrôle de
paquetage ; sa décision de retrait appartient à BASE-007. L'exécution des
scénarios juridiques et la relecture restent rattachées au lot choisi, sans
lancer tous les domaines ou agents du dépôt.
