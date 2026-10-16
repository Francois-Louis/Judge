# BASE-002 — Dossier de décision sur le lien de fork

Établi le **15 octobre 2026 (Europe/Paris)** pour
[`Francois-Louis/Judge`](https://github.com/Francois-Louis/Judge).
La documentation officielle GitHub citée a été consultée à cette date.

**Choix de l'utilisateur : à décider.** La demande d'implémenter BASE-002
autorise ce dossier, sans sélectionner une option ni autoriser une opération
distante. Aucune story d'opération distante n'est créée à ce stade.

## Ce qu'un commit ou un push change

Un commit reste local. Dans le checkout audité, `origin` vise
`git@github.com:Francois-Louis/Judge.git` en lecture et en écriture, et `main`
suit `origin/main`. Un push ordinaire depuis cette branche met à jour Judge ;
il ne crée pas, à lui seul, de PR vers l'origine. GitHub décrit la création
d'une PR comme une action distincte, après le push, avec sélection du dépôt
cible et validation du formulaire.
[Source : création d'une PR depuis un fork](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork).

Si une PR existe déjà, pousser sur sa branche source peut l'actualiser.
L'existence de telles PR n'a pas été inventoriée ici. Le workflow CLA local
réagit à des PR/commentaires existants, sans événement `push` ni création de
PR identifiée. Voir les mécanismes et les limites de
[l'audit BASE-001](base-001-releve-audit.md).

L'absence de remote `upstream` ne supprime pas le lien enregistré chez GitHub.
Un fork public reste public ; sa visibilité ne peut pas être changée isolément.
Les commits du réseau peuvent être accessibles depuis l'origine, y compris
après suppression du fork. Le détachement ou la copie ne garantit donc ni
l'invisibilité du travail déjà publié, ni l'effacement des clones ou archives.
[Source : visibilité et données partagées des forks](https://docs.github.com/en/pull-requests/reference/forks).

## État réellement vérifié

Les lectures n'ont modifié aucun réglage. Les valeurs distantes sont un
instantané, à renouveler avant toute opération.

| Vérification | Observation du 15 octobre 2026 | Portée |
|---|---|---|
| Git local : `.git/config`, `git remote -v`, URL de push résolue | Remote unique `origin`, URL ci-dessus, suivi `main → origin/main`, aucun `pushurl` séparé | Confirme la destination locale, pas le statut de fork chez GitHub |
| API publique : dépôt | ID `1421088516`, `fork: true`, parent et source `anthropics/claude-for-legal`, visibilité `public`, branche par défaut `main`, non archivé | Confirme le lien distant |
| Connecteur GitHub authentifié : métadonnées du dépôt | `permissions.admin: true`, lecture et écriture autorisées | Accès administrateur annoncé pour cette connexion |
| API publique : taille et forks enfants | `size: 1711` (Ko), `forks_count: 0` ; liste des forks : HTTP 200, corps `[]`, sans pagination suivante | Conditions documentées de détachement apparemment satisfaites |
| API publique : quelques métadonnées | Issues désactivées ; wiki activé ; compteurs des issues/PR ouvertes, stars et abonnés à zéro | Ces compteurs ne constituent pas un inventaire des PR fermées, du wiki ou des PR vers l'origine |
| Interface Settings / Danger Zone | Non inspectée ; présence du bouton non confirmée | Disponibilité effective de « Leave fork network » à confirmer, sans cliquer pour exécuter |

Lectures publiques reproductibles :
[métadonnées de Judge](https://api.github.com/repos/Francois-Louis/Judge) et
[forks de Judge](https://api.github.com/repos/Francois-Louis/Judge/forks?per_page=100).
Le connecteur authentifié `get_repo` a complété ces observations pour les
permissions. La signification des lectures est décrite dans les API officielles
[Get a repository](https://docs.github.com/en/rest/repos/repos#get-a-repository)
et [List forks](https://docs.github.com/en/rest/repos/forks#list-forks).

## Options et conséquences

| Option | Historique Git | Issues, PR et autres métadonnées | Lien et visibilité |
|---|---|---|---|
| A — Conserver le fork | Conservé | Conservées, sans migration | Lien public avec l'origine maintenu |
| B — Quitter le réseau via GitHub | Commits et leurs métadonnées préservés | Pertes annoncées par GitHub ; détail ci-dessous | Dépôt autonome ; sortie permanente |
| C — Créer un dépôt indépendant sous un autre nom | Conservé pour les branches et tags copiés | Non transférées par une copie Git | Nouveau dépôt, visibilité à choisir ; ancien fork toujours présent |

### A — Conserver le fork

Cette option est déjà disponible : elle n'exige aucune action distante et
préserve l'espace de collaboration actuel. GitHub continue d'afficher
l'origine sous le nom du fork. Elle suffit si le besoin est de travailler
dans Judge sans ouvrir de PR vers l'origine ; elle ne répond pas à un besoin
de disparition du lien public.
[Source : fonctionnement des forks](https://docs.github.com/en/pull-requests/reference/forks).

Le maintien du fork n'applique aucune mise à jour de code par lui-même.
Les risques de remplacement par les outils installés et la politique CLA
restent traités par BASE-004, EXIST-011 et BASE-007, comme prévu dans BASE-001.

### B — Quitter le réseau via « Leave fork network »

GitHub réserve cette option aux forks publics de moins de 1 Go et sans fork
enfant. Judge paraît éligible d'après les lectures ci-dessus ; le bouton dans
Settings reste à vérifier. La sortie est définitive : le dépôt ne peut pas
être rattaché de nouveau à ce réseau. Certaines opérations deviennent
brièvement indisponibles pendant le traitement.

GitHub annonce la conservation des commits et de leurs métadonnées, mais la
perte des issues, PR, wikis, stars, abonnés, commentaires, forks enfants et
autres métadonnées associées. Ne pas présumer la conservation des réglages,
intégrations ou données Actions non détaillés : leur devenir et les sauvegardes
nécessaires devront être établis avant exécution.
[Source : détachement d'un fork](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/detaching-a-fork).

Cette option ne vaut pas passage en privé. Un changement ultérieur de
visibilité serait une opération distincte, avec ses propres effets : les
forks publics existants restent publics, des fonctions dépendent du plan et
les stars/abonnés peuvent être perdus.
[Source : changement de visibilité](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).

### C — Créer un dépôt indépendant

Créer un dépôt vide sous un autre nom puis y copier les branches et tags
permet de conserver l'historique correspondant, auteurs, dates et identifiants
de commits. GitHub documente la duplication par clone nu et envoi miroir ;
les objets Git LFS, s'il y en a, demandent un transfert spécifique.
[Source : duplication d'un dépôt](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository).

Une copie Git ne migre pas les objets de collaboration GitHub : issues,
PR, commentaires, stars, abonnés, pièces de releases, historique Actions,
secrets, webhooks, droits ou protections. Le wiki est à traiter séparément.
Les fichiers versionnés, dont les workflows, font en revanche partie du code
copié ; copier un workflow ne copie pas ses secrets ni ses exécutions.
Ces éléments devront être inventoriés et leur migration préparée séparément.
[Source : sauvegardes et limites d'une copie Git](https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository).

Le nouveau dépôt peut être public ou privé selon les droits et politiques
du compte ; le privé ne retire aucune copie antérieure du domaine public.
Conserver l'ancien fork évite sa suppression, mais laisse son lien public
avec l'origine en place. Un changement de nom ou d'URL exige aussi de préparer
les références au dépôt et la destination des futurs push.
[Source : création d'un dépôt](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

La variante qui **supprime Judge puis le recrée au même emplacement** est
destructive : réutiliser son nom ne restaure pas son identité ou ses données
GitHub. La procédure de détachement manuel avertit de la perte irréversible
des PR et configurations. Ce n'est pas un repli automatique si le bouton
de détachement manque.
[Source : procédure manuelle](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/detaching-a-fork#manually-leaving-the-fork-network).
La suppression ne supprime pas l'origine ni les forks publics et détruit
définitivement les permissions d'équipe. Certaines restaurations sont possibles
sous 90 jours, mais cette possibilité ne constitue pas un retour arrière garanti.
[Source : suppression d'un dépôt](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository).

## Décision et suite

| Élément à consigner | État |
|---|---|
| Choix A, B ou C | **A — conserver le fork**, choisi par l'utilisateur le 16 octobre 2026 |
| Visibilité souhaitée | Inchangée (public) ; aucune demande de changement |
| Nom du dépôt cible et devenir de Judge pour C | Sans objet |
| Pertes acceptées et données à conserver | Sans objet : aucune opération distante |
| Accord d'exécution distante | Aucun dans BASE-002 |

Repères pour choisir : A conserve le fonctionnement actuel ; B retire le lien
de réseau au prix des pertes annoncées ; C permet de préparer une copie
indépendante en gardant l'ancien dépôt disponible. Aucun de ces repères
ne constitue un choix au nom de l'utilisateur.

Le choix A ne demande aucune opération distante ni story d'exécution. Les
règles BASE-007 (pas de PR vers l'origine) restent la protection applicable.
Si le choix est revu plus tard vers B ou C, préparer une story dédiée qui précise :

- le dépôt exact, son ID, l'option, la visibilité et les pertes acceptées ;
- un inventaire des données Git et GitHub, les sauvegardes et leurs limites ;
- la vérification des droits, de l'éligibilité et de la fonction disponible ;
- les étapes, les critères de réussite, les liens et remotes à adapter,
  ainsi que le retour arrière réellement possible ;
- l'autorisation d'exécuter l'opération et les actions destructives exactes,
  sans déduire cet accord de la seule sélection d'une option.

Aucun détachement, suppression, création distante, changement de visibilité,
push, PR ou publication n'a été effectué pour ce dossier. Les licences et
attributions existantes ne sont pas modifiées.
