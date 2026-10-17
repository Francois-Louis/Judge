# Backlog — adaptation juridique France / Union européenne

> **Pour savoir ce qui est fait, en cours ou à faire, ouvrir [ETAT.md](ETAT.md).**
> Ce tableau est généré depuis le champ `statut:` des stories par
> `python backlog/etat.py` ; le relancer après chaque changement de statut.

Ce dossier organise l'adaptation du fork au droit français et européen. Ce
README explique comment le backlog est rangé et ce qui est acté. L'avancement
n'y est pas recopié : chaque story porte son statut et son bilan, et
[ETAT.md](ETAT.md) les rassemble.

## Comment s'y retrouver

```text
backlog/
  ETAT.md                    # tableau généré : fait / en cours / prêt / à faire
  etat.py                    # régénère ETAT.md (--check : vérifie qu'il est à jour)
  decisions-2026-10-16.md    # arbitrages rendus par l'utilisateur
  usages-quotidiens.md       # situations S-01 à S-42, entrée par problème
  story-template.md          # modèle d'une nouvelle story
  00-fondations/             # BASE : architecture, identité, méthode, recettes
  01-pilote-travail/         # PILOTE et ses suites TRAV
  02-plugins-existants/      # EXIST (un cadrage par plugin) et leurs suites
  03-nouveaux-domaines/      # DOM (un cadrage par domaine) et leurs suites
  04-livraison/              # LIV : lots livrés
  05-usages-quotidiens/      # USAGE : orientation et priorités
```

Dans chaque epic :

- `<id>-<titre>.md` au premier niveau est une story (frontmatter `id`, `statut`…) ;
- `suites/` contient les stories issues d'un cadrage ;
- `<id>-annexes/` contient tout ce qu'une story a produit : inventaire,
  découpage, vérification, matrice de frictions, scripts de contrôle et
  résultats JSON. Les fichiers y gardent le préfixe de leur story ;
- `sources/` conserve les textes fournis par l'utilisateur, à l'octet près ;
- `retrospective-*.md` fait le bilan de l'epic.

ETAT.md liste les annexes sous leur story et signale celles qui ne sont pas
rangées dans leur dossier.

## Ce qui est acté

- Adapter les workflows au droit français et à l'articulation européenne pertinente.
- Conserver le découpage du dépôt : un plugin par domaine, des skills par tâche.
- Adapter les plugins existants et créer des plugins séparés pour les domaines manquants.
- Avancer par petites stories vérifiables, sans réécriture générale en une seule fois.
- Garder les commits et push destinés au fork `Francois-Louis/Judge`, indépendants
  du dépôt d'origine ; le fork est conservé (BASE-002, option A).
- Aider largement les personnes dans leurs difficultés du quotidien : comprendre
  un document, vérifier une somme ou une obligation et préparer une démarche utile.
  Les sorties doivent aussi convenir aux personnes sans formation juridique.
- Pas de plugin généraliste `france-eu-legal` : les références métier restent
  dans leur domaine. Seule une méthode transverse limitée (recherche, citations,
  droit dans le temps) est partagée, par copie embarquée dans chaque paquet.

Les arbitrages ultérieurs sont consignés dans les
[décisions du 16 octobre 2026](decisions-2026-10-16.md).

## Documents de référence

| Sujet | Document |
|---|---|
| Architecture, propriétaires des tâches, contrat d'un plugin | [Dossier BASE-003](00-fondations/base-003-annexes/base-003-dossier-architecture.md) |
| Identité `judge-fr-eu` et séparation des configurations | [Cadrage BASE-004](00-fondations/base-004-annexes/base-004-strategie-identite-configurations.md), [validation BASE-008](../references/base008-validation.md) |
| Méthode de recherche et de citation (v1.0.0) | [Méthode BASE-005](../references/research-citation-method.md) |
| Contrôles d'un skill et d'un plugin | [Recette BASE-006](../references/package-validation.md) |
| Accès aux sources officielles sans souscription | [Voies BASE-010](../references/legal-source-access.md) |
| Avertissement et interlocuteur compétent | [BASE-013](00-fondations/base-013-avertissement-interlocuteur.md) |
| Jurisprudence pendant une réponse (accès testés, méthode proposée) | [BASE-015](00-fondations/base-015-jurisprudence-runtime.md) |
| Orientation à partir d'un problème concret | [Protocole USAGE-001](05-usages-quotidiens/usage-001-annexes/usage-001-protocole-orientation.md), [situations du quotidien](usages-quotidiens.md) |
| Audit initial du fork (15 octobre 2026) | [Relevé BASE-001](00-fondations/base-001-annexes/base-001-releve-audit.md) |
| Bilans d'epic | [Fondations](00-fondations/retrospective-fondations.md), [pilote travail](01-pilote-travail/retrospective-pilote-travail.md), [usages quotidiens](05-usages-quotidiens/retrospective-usages-quotidiens.md) |
| Premier lot livré | [LIV-001](04-livraison/liv-001-livrer-lot-borne.md), [notes de version](04-livraison/liv-001-annexes/liv-001-notes-version.md) |

Chaque cadrage EXIST ou DOM a dans ses annexes un `*-decoupage-*.md` qui
liste ses suites, et le plus souvent un `*-frictions-utilisateurs.md` qui
relie les difficultés rapportées à leurs propriétaires.

## Taille et suivi des stories

- Traiter une story à la fois, ou un petit lot explicitement choisi.
- Une story d'implémentation porte sur une tâche métier et un résultat observable.
  « Adapter tout le droit bancaire » est un périmètre de domaine, pas une story d'implémentation.
- Privilégier une sortie qui aide réellement la personne : explication du document,
  décompte lisible, pièces à demander, brouillon argumenté ou interlocuteur identifié.
  Le nombre de codes cités n'est pas un critère suffisant de couverture.
- Les stories EXIST et DOM sont des **cadrages** : leur livrable est un découpage
  plus fin. Elles n'autorisent pas une réécriture complète du domaine.
- Utiliser le [modèle de story](story-template.md) pour ajouter une tâche.
  Référencer les identifiants des dépendances dans le frontmatter.
- Ranger ce que produit une story dans `<id>-annexes/`, à côté d'elle.
- Statuts : `proposee` → `prete` → `en-cours` → `a-verifier` → `terminee`.
  Utiliser `bloquee` en précisant le fait manquant et la condition de reprise,
  `abandonnee` pour une story retirée sur décision, avec la raison et le lien.
  Après chaque changement, lancer `python backlog/etat.py`.
- Priorités : P0 fondations, P1 pilote, P2 extension après bilan,
  P3 domaines supplémentaires à prioriser. Ce ne sont pas des estimations de charge.

Une story est prête quand son périmètre, ses dépendances, son résultat et ses
scénarios sont suffisamment précis. Elle est terminée lorsque ses critères sont
satisfaits et que le bilan indique les vérifications réellement effectuées.
Un titre traduit, un manifeste valide ou une consigne générale « appliquer le
droit français » ne suffisent pas à valider un workflow métier.

Les cadrages peuvent être affinés à tout moment. Il n'est pas nécessaire de
terminer tous les cadrages ni tous les domaines pour livrer un petit lot. Les
noms de futurs plugins et les priorités des suites restent des propositions
tant que l'utilisateur n'a pas choisi d'extension.

## Structure cible d'un domaine

Exemple proposé pour la banque ; les noms restent à arrêter lors de l'implémentation :

```text
banking-legal/
  .claude-plugin/plugin.json
  CLAUDE.md
  README.md
  references/                       # Sources et méthodes propres au domaine
  skills/
    payment-dispute/SKILL.md        # Une tâche et son résultat
    credit-review/SKILL.md
    bank-complaint/SKILL.md
```

Ajouter un agent, un hook ou un connecteur seulement lorsqu'une tâche en a
besoin. Les exemples ci-dessus n'annoncent pas des fonctionnalités déjà présentes.

## Contrôles des stories terminées

Plusieurs cadrages ont un script `*-controles.py` dans leurs annexes, par
exemple `python -X utf8 backlog/03-nouveaux-domaines/dom-001-annexes/dom-001-controles.py`.
Ils vérifient le lot tel qu'il a été livré ; les échecs sur des suites ajoutées
après coup signalent l'évolution du backlog, pas une régression. Leurs
résultats JSON sont des relevés datés et ne sont pas réécrits.
