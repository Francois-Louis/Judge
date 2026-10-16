# Backlog — adaptation juridique France / Union européenne

Ce dossier organise le travail à venir. Le backlog contient 387 stories :
BASE-001 à BASE-007, BASE-009 à BASE-012, PILOTE-001 à PILOTE-005,
USAGE-001 à USAGE-003, EXIST-001 à EXIST-011, DOM-001 à DOM-005 et LIV-001 sont `terminee`,
BASE-008 est `en-cours`, COM-001 est `a-verifier` ; les 349 autres sont `proposee`.
Les [décisions du 16 octobre 2026](decisions-2026-10-16.md) consignent les
arbitrages rendus après les cadrages DOM-001 à DOM-005 et la livraison LIV-001.
La [rétrospective des fondations](00-fondations/retrospective-fondations.md)
fait le bilan de l'epic 00 et de ses points ouverts.
La [rétrospective du pilote travail](01-pilote-travail/retrospective-pilote-travail.md)
fait celui de l'epic 01 ; ses corrections sans décision sont dans
[PILOTE-005](01-pilote-travail/pilote-005-corrections-retrospective.md).
Le [relevé BASE-001](00-fondations/base-001-releve-audit.md) consigne l'audit du
15 octobre 2026. Le retrait local du contrôle CLA et les consignes de contribution
au fork sont réalisés dans [BASE-007](00-fondations/base-007-cla-contributions-fork.md).
Les autres corrections proposées restent à réaliser séparément.

## Ce qui est acté

- Adapter les workflows au droit français et à l'articulation européenne pertinente.
- Conserver le découpage du dépôt : un plugin par domaine, des skills par tâche.
- Adapter les plugins existants et créer des plugins séparés pour les domaines manquants.
- Avancer par petites stories vérifiables, sans réécriture générale en une seule fois.
- Garder les commits et push destinés au fork indépendants du dépôt d'origine.
- Aider largement les personnes dans leurs difficultés du quotidien : comprendre
  un document, vérifier une somme ou une obligation et préparer une démarche utile.
  Les sorties doivent aussi convenir aux personnes sans formation juridique.

La [matrice des situations du quotidien](usages-quotidiens.md) donne une entrée
par problème rencontré : facture, bail, devis, héritage, décision d'une caisse,
contrat, activité agricole, scolarité, compte en ligne, etc. Elle couvre aussi
les aidants, indépendants, artisans, petites associations et petits exploitants.

[USAGE-001](05-usages-quotidiens/usage-001-orientation-accessible.md) a défini le
[protocole documentaire d'orientation](05-usages-quotidiens/usage-001-protocole-orientation.md)
et enrichi les 42 situations avec leur domaine principal et leurs frontières.
Sa [vérification sur récits fictifs](05-usages-quotidiens/usage-001-verification.md)
ne vaut ni essai utilisateur réel, ni exécution de skill. Ce cadrage précise
les sorties attendues, sans créer de commande ou adapter un domaine métier.

[USAGE-002](05-usages-quotidiens/usage-002-priorites-utilite.md) a comparé
[cinq tâches bornées](05-usages-quotidiens/usage-002-comparaison-priorites.md)
et proposé l'ordre contrat reçu par un candidat, justificatifs d'une facture
ciblée, pièces du notaire, retenue sur dépôt, devis. La
[relecture avec trois profils fictifs](05-usages-quotidiens/usage-002-verification.md)
explicite bénéfices et obstacles, sans essai utilisateur réel. Le premier lot
est PILOTE-002, retenu par la demande d'implémentation du 15 octobre 2026,
avec ses exclusions. Le classement reste une hypothèse ; aucun second pilote
n'est lancé.
Le critère déterminant de ce rang est la capacité à vérifier un premier lot,
non une utilité supérieure : la relecture montre un bénéfice direct limité de
cette tâche pour un retraité ou un petit exploitant.
La [rétrospective de l'epic 05](05-usages-quotidiens/retrospective-usages-quotidiens.md)
a conduit aux corrections de [USAGE-003](05-usages-quotidiens/usage-003-corrections-retrospective.md) :
protocole versionné et repris par PILOTE-002 et la recette BASE-006,
situations numérotées `S-01` à `S-42`.

Il n'y a pas de plugin généraliste `france-eu-legal` prévu. Les références métier
restent dans leur domaine. Seule une méthode transverse limitée (recherche,
citations, droit dans le temps) peut être partagée, à condition que le paquet
installé d'un plugin reste autonome.

Le [dossier d'architecture BASE-003](00-fondations/base-003-dossier-architecture.md)
fixe les propriétaires des tâches, les frontières, le contrat d'un plugin et
la réutilisation de la méthode commune par copies versionnées embarquées.
Ses matrices distinguent l'existant à adapter des créations proposées ; elles
ne décrivent pas des fonctionnalités France/UE déjà disponibles.

Le [cadrage BASE-004](00-fondations/base-004-strategie-identite-configurations.md)
retient `judge-fr-eu` pour le marketplace et les configurations, avec des
identifiants de plugins préfixés pour séparer aussi les commandes. Il comprend
l'inventaire des références et une simulation sur profils factices.
[BASE-008](00-fondations/base-008-isoler-identite-configurations.md) a migré
les manifestes, commandes et chemins opérationnels vers ce namespace. Les
contrôles hors ligne et l'installation côte à côte en client jetable passent ;
la recette de session authentifiée et le test réel des liens symboliques
restent à exécuter. Voir le [relevé de validation](../references/base008-validation.md).

La [méthode BASE-005](../references/research-citation-method.md), version `1.0.0`,
fixe la qualification France/UE, la traçabilité des sources, le traitement des
incertitudes et les informations minimales d'un délai. Son
[compte rendu de vérification](00-fondations/base-005-verification-methode.md)
distingue les scénarios fictifs des accès officiels réellement effectués.
BASE-008 en a embarqué une copie identique dans les 12 plugins internes,
sous `references/shared/`. `hiring-review` charge désormais sa copie locale
dans PILOTE-002 ; le chargement des autres skills reste à adapter.

La [recette BASE-006](../references/package-validation.md) définit les contrôles
du skill puis du plugin, l'installation isolée, les scénarios juridiques et
la compréhension par un utilisateur sans formation juridique. Son contrôleur
statique est vérifié sur des artefacts factices ; cela ne vaut ni installation
réelle, ni schéma officiel validé, ni exécution des futurs skills adaptés.

## État de départ observé le 15 octobre 2026

- 12 plugins internes au premier niveau, contenant 150 skills.
- Un plugin éditeur sous `external_plugins/cocounsel-legal/`, à distinguer des adaptations.
- Cinq cookbooks d'agents gérés, à examiner séparément des skills manuels.
- `origin` pointe en lecture et écriture vers `git@github.com:Francois-Louis/Judge.git`.
  Aucun remote `upstream` n'est configuré dans l'état local observé.
- Le workflow `.github/workflows/cla.yaml` contrôlait la signature du CLA lors
  de l'audit BASE-001. Il a depuis été retiré des fichiers locaux dans BASE-007 ;
  les éventuelles exigences des protections GitHub restent à examiner séparément.
- La clinique contient notamment des références de délais Californie et Illinois.
  Leur adaptation est suivie par EXIST-009, pas par un remplacement de nom de pays.

Ces observations servent au découpage. Elles ne remplacent pas l'audit complet,
ni une vérification de l'état distant ou du droit applicable. Le lien public d'un
fork avec son origine est une question distincte de la destination des push :
l'utilisateur a choisi de conserver le fork (BASE-002, option A).

## Ordre de travail proposé

[PILOTE-001](01-pilote-travail/pilote-001-inventaire-travail.md) a produit
l'[inventaire des 20 skills](01-pilote-travail/pilote-001-releve-inventaire.md),
le [plan hiring-review](01-pilote-travail/pilote-001-plan-hiring-review.md) et
16 [stories de suite](01-pilote-travail/pilote-001-decoupage-travail.md), encore
proposées et dépendantes du bilan PILOTE-003. Aucun skill n'est adapté par cet audit.
PILOTE-002 a depuis réécrit `hiring-review`, version de plugin `0.2.0`.
Le [bilan PILOTE-003](01-pilote-travail/pilote-003-verification.md) rapporte
les contrôles sur le paquet détaché. La recette en client isolé
[BASE-011](00-fondations/base-011-recette-client-isole.md) du 16 octobre 2026
a exécuté installation et scénarios. PILOTE-002 à PILOTE-004 sont closes ;
l'utilisateur a validé comme lecteur des réponses de fixture, sans lecteur
indépendant, et le nominal H01 complet de PILOTE-002 reste à exécuter
(voir [PILOTE-004](01-pilote-travail/pilote-004-preferences-candidat.md)). La tranche
[TRAV-017](01-pilote-travail/suites/trav-017-clause-non-concurrence.md) reste
proposée ; aucune extension métier n'est engagée.
La lecture des sources bloquées dans l'outil web dispose désormais de
[voies officielles testées sans souscription API](../references/legal-source-access.md)
(BASE-010) : CDTN, CELLAR et extractions XML ciblées DILA ; l'indexation complète
des stocks reste à réaliser. L'accès PISTE refusé à l'utilisateur n'est pas un prérequis.

1. BASE-001 : audit local du fork. BASE-003 : architecture par domaines.
2. BASE-002 : lien GitHub, fork conservé (option A, 16 octobre 2026).
3. BASE-004 à BASE-006 : identité/configurations, méthode de sources et contrôles.
4. USAGE-001 et USAGE-002 ont défini l'orientation accessible et comparé cinq
   petites tâches. Le pilote travail a été retenu lors de l'implémentation de PILOTE-002.
5. PILOTE-001 a inventorié ce plugin ; PILOTE-002 a réécrit un seul skill,
   la revue d'un contrat reçu par un candidat, avec une recette encore ouverte.
6. PILOTE-003 a produit le bilan ; la recette client BASE-011 a clos le pilote.
   Le nominal H01 complet reste à faire avant de statuer sur une extension.
7. Choisir ensuite un autre skill ou un premier nouveau domaine, puis préparer
   une livraison correspondant seulement au périmètre terminé.

Le choix du travail comme pilote est acté pour PILOTE-002. Les priorités des
suites et les noms des futurs plugins restent des propositions de planification,
sans choix d'extension par l'utilisateur. Les domaines P3 sont des extensions possibles à prioriser,
pas une obligation de les développer.

Les nouveaux cadrages séparent notamment agriculture, construction, successions,
achat immobilier, copropriété, urbanisme, voisinage, services essentiels,
retraites et protection des personnes. Leurs frontières sont écrites dans les
stories ; chaque nouveau nom de plugin reste une proposition à cadrer.

Les cadrages EXIST et DOM peuvent être affinés avant la fin du pilote. Leurs
implémentations attendent son bilan. Il n'est pas nécessaire de terminer tous
les cadrages ni tous les domaines pour livrer un petit lot.

## Taille et suivi des stories

- Traiter une story à la fois, ou un petit lot explicitement choisi.
- Une story d'implémentation porte sur une tâche métier et un résultat observable.
  « Adapter tout le droit bancaire » est un périmètre de domaine, pas une story d'implémentation.
- Privilégier une sortie qui aide réellement la personne : explication du document,
  décompte lisible, pièces à demander, brouillon argumenté ou interlocuteur identifié.
  Le nombre de codes cités n'est pas un critère suffisant de couverture.
- Les stories EXIST et DOM ci-dessous sont des **cadrages** : leur livrable est
  un découpage plus fin. Elles n'autorisent pas une réécriture complète du domaine.
- Utiliser le [modèle de story](story-template.md) pour ajouter les tâches issues
  des cadrages. Référencer les identifiants des dépendances dans le frontmatter.
- Statuts : `proposee` → `prete` → `en-cours` → `a-verifier` → `terminee`.
  Utiliser `bloquee` en précisant le fait manquant et la condition de reprise.
- Priorités proposées : P0 fondations, P1 pilote, P2 extension après bilan,
  P3 domaines supplémentaires à prioriser. Elles ne sont pas des estimations de charge.

Une story est prête quand son périmètre, ses dépendances, son résultat et ses
scénarios sont suffisamment précis. Elle est terminée lorsque ses critères sont
satisfaits et que le bilan indique les vérifications réellement effectuées.
Un titre traduit, un manifeste valide ou une consigne générale « appliquer le
droit français » ne suffisent pas à valider un workflow métier.

## Structure cible d'un domaine

Exemple proposé pour la banque ; les noms restent à arrêter dans DOM-004 :

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

## Fondations — P0

| Story | Résultat attendu | Nature | Priorité |
|---|---|---|---|
| [BASE-001](00-fondations/base-001-audit-independance-fork.md) | Auditer les push et les automatisations du fork | audit | P0 |
| [BASE-002](00-fondations/base-002-choix-lien-fork.md) | Choisir le niveau d'indépendance du dépôt | decision | P0 |
| [BASE-003](00-fondations/base-003-architecture-domaines.md) | Fixer l'architecture des plugins par domaine | cadrage | P0 |
| [BASE-004](00-fondations/base-004-identite-configurations-mises-a-jour.md) | Définir l'identité du fork et la séparation des configurations | cadrage | P0 |
| [BASE-005](00-fondations/base-005-methode-sources-juridiques.md) | Définir la méthode de recherche et de vérification France/UE | cadrage | P0 |
| [BASE-006](00-fondations/base-006-controles-paquetage.md) | Définir les contrôles d'une adaptation de skill | cadrage | P0 |
| [BASE-007](00-fondations/base-007-cla-contributions-fork.md) | Retirer le contrôle CLA hérité et préciser les contributions au fork | implementation | P0 |
| [BASE-008](00-fondations/base-008-isoler-identite-configurations.md) | Appliquer l'identité Judge FR/UE et isoler les configurations | implementation | P0 |
| [BASE-009](00-fondations/base-009-corrections-retrospective.md) | Appliquer les corrections issues de la rétrospective des fondations | implementation | P0 |
| [BASE-010](00-fondations/base-010-acces-sources-officielles.md) | Lire les sources officielles par des voies testées sans souscription API | implementation | P0 |
| [BASE-011](00-fondations/base-011-recette-client-isole.md) | Exécuter la recette des paquets dans un client Claude isolé | validation | P0 |
| [BASE-012](00-fondations/base-012-designer-cli-claude.md) | Désigner le binaire claude utilisé par le contrôleur de paquet | implementation | P1 |

## Orientation et utilité quotidienne — P0 / P1

| Story | Résultat attendu | Nature | Priorité |
|---|---|---|---|
| [USAGE-001](05-usages-quotidiens/usage-001-orientation-accessible.md) | Définir une orientation accessible à partir d'un problème concret | cadrage | P0 |
| [USAGE-002](05-usages-quotidiens/usage-002-priorites-utilite.md) | Prioriser les premières tâches selon leur utilité quotidienne | cadrage | P1 |
| [USAGE-003](05-usages-quotidiens/usage-003-corrections-retrospective.md) | Appliquer les corrections issues de la rétrospective des usages quotidiens | implementation | P1 |

## Pilote proposé — P1

| Story | Résultat attendu | Nature | Priorité |
|---|---|---|---|
| [PILOTE-001](01-pilote-travail/pilote-001-inventaire-travail.md) | Inventorier le plugin travail et découper son adaptation | audit | P1 |
| [PILOTE-002](01-pilote-travail/pilote-002-revue-embauche.md) | Adapter un premier skill : revue d'embauche en France | implementation | P1 |
| [PILOTE-003](01-pilote-travail/pilote-003-bilan-pilote.md) | Vérifier le pilote avant d'étendre l'adaptation | validation | P1 |
| [PILOTE-004](01-pilote-travail/pilote-004-preferences-candidat.md) | Modifier une préférence candidat sans initialisation professionnelle | implementation | P1 |
| [PILOTE-005](01-pilote-travail/pilote-005-corrections-retrospective.md) | Appliquer les corrections issues de la rétrospective du pilote travail | implementation | P1 |

## Adaptations à découper — P2

Les suites du plugin travail sont détaillées dans le
[découpage TRAV-001 à TRAV-018](01-pilote-travail/pilote-001-decoupage-travail.md).
Chaque story a son fichier, ses dépendances et ses scénarios. Elles attendent
la clôture de PILOTE-003 et une sélection explicite ; PILOTE-002 reste la seule
tranche métier d'embauche réécrite. PILOTE-004 corrige son setup candidat,
avec une recette client et utilisateur encore ouverte.

Les suites commerciales sont proposées dans le
[découpage COM-001 à COM-018](02-plugins-existants/exist-001-decoupage-commercial.md),
avec [inventaire des 12 skills et dépendances](02-plugins-existants/exist-001-inventaire-commercial.md)
et [vérification documentaire](02-plugins-existants/exist-001-verification.md).
Le bilan PILOTE-003 est terminé après la recette BASE-011 du 16 octobre 2026 ;
ce cadrage ne sélectionnait aucune tranche. Depuis, [COM-001](02-plugins-existants/suites/com-001-orientation-contrat.md)
est réécrite : orientation sans profil, version commerciale 0.2.0,
statut `a-verifier` (recette client/lecteur non exécutée). Les 17 autres COM
restent `proposee`, sans déploiement du cookbook.

Les suites sociétés et opérations sont proposées dans le
[découpage SOC-001 à SOC-022](02-plugins-existants/exist-002-decoupage-societes.md),
avec [inventaire des 13 skills et dépendances](02-plugins-existants/exist-002-inventaire-societes.md)
et [relecture SAS, SARL et acquisition avec filiale étrangère](02-plugins-existants/exist-002-verification.md).
Les décisions sociales, PV, formalités, diligences et suivi d'opération ont
des résultats distincts. Les 22 SOC restent `proposee` ; aucune adaptation
du plugin ni sélection d'extension ou déploiement du cookbook par EXIST-002.

Les suites protection des données sont proposées dans le
[découpage PRV-001 à PRV-021](02-plugins-existants/exist-003-decoupage-donnees.md),
avec [inventaire des 23 fichiers et 9 skills](02-plugins-existants/exist-003-inventaire-donnees.md)
et [relecture accès, sous-traitance et santé](02-plugins-existants/exist-003-verification.md).
Exercice des droits, traitement, AIPD, sous-traitance, transferts et suivi sont
séparés ; le particulier dispose d'une proposition propre de demande d'accès.
Les 21 PRV restent `proposee` ; EXIST-003 ne modifie pas le plugin et ne
sélectionne aucune extension. Le préalable PILOTE-003 est satisfait après BASE-011.

Les suites produits et publicité sont proposées dans le
[découpage PDT-001 à PDT-017](02-plugins-existants/exist-004-decoupage-produits.md),
avec [inventaire des 23 fichiers, 7 skills, agent et cookbook](02-plugins-existants/exist-004-inventaire-produits.md)
et [relecture lancement B2C France et campagne environnementale](02-plugins-existants/exist-004-verification.md).
La première tranche proposée est une fiche de qualification ; lancement,
évolution, publicité et question ponctuelle restent séparés. Les 17 PDT
restent `proposee`, sans adaptation du plugin ni sélection d'extension,
publication ou déploiement du radar. Le préalable PILOTE-003 est satisfait
après BASE-011 ; ses limites documentées restent consignées.

Les suites gouvernance IA sont proposées dans le
[découpage IA-001 à IA-020](02-plugins-existants/exist-005-decoupage-ia.md),
avec [inventaire des 23 fichiers et 10 skills](02-plugins-existants/exist-005-inventaire-ia.md)
et [relecture outil RH, assistant interne et service public](02-plugins-existants/exist-005-verification.md).
Inventaire factuel, qualification, obligations par rôle, évaluation interne,
FRIA, contrats et politique sont séparés. Les 20 IA restent `proposee` ;
EXIST-005 ne modifie pas le plugin, ne sélectionne aucune extension et ne
valide ni catégorie définitive ni calendrier. Le préalable PILOTE-003 est
satisfait après BASE-011 ; ses limites documentées restent consignées.

Les suites contentieuses sont proposées dans le
[découpage CTX-001 à CTX-024](02-plugins-existants/exist-006-decoupage-contentieux.md),
avec [inventaire des 38 fichiers, 19 skills et cookbook associé](02-plugins-existants/exist-006-inventaire-contentieux.md)
et [relecture mise en demeure, demande de pièces et convocation](02-plugins-existants/exist-006-verification.md).
Mise en demeure, conservation/communication des preuves, écritures et suivi
sont séparés ; aucune équivalence automatique subpoena/deposition/privilege
log. Les 24 CTX restent `proposee`, sans adaptation, renommage, sélection
d'extension ou déploiement. Le préalable PILOTE-003 est satisfait après
BASE-011 ; les limites du pilote restent consignées.

Les suites de veille sont proposées dans le
[découpage VEI-001 à VEI-020](02-plugins-existants/exist-007-decoupage-veille.md),
avec [inventaire des 26 fichiers, 9 skills et cookbook associé](02-plugins-existants/exist-007-inventaire-veille.md),
[relecture JORF/directive/consultation](02-plugins-existants/exist-007-verification.md)
et [sources déclarées et sondages techniques](02-plugins-existants/exist-007-sources.json).
Collecte, qualification, modification, temporalité/transposition, écarts,
politique et consultation ont des résultats distincts. Les vingt VEI restent
`proposee` ; tâches manuelles avant agent et cookbook séparé, sans adaptation,
connexion ou déploiement par EXIST-007. Préalable PILOTE-003 satisfait après
BASE-011 ; limites du pilote conservées.

Les suites de propriété intellectuelle sont proposées dans le
[découpage PI-001 à PI-025](02-plugins-existants/exist-008-decoupage-pi.md),
avec [inventaire des 27 fichiers et 12 skills](02-plugins-existants/exist-008-inventaire-pi.md)
et [relecture marque France, invention de salarié et retrait de photo](02-plugins-existants/exist-008-verification.md).
Titres/territoires, droit d'auteur, créations/inventions de salariés,
cession/licence, OSS, retrait et portefeuille sont séparés. Les vingt-cinq PI
restent `proposee` ; aucun défaut USPTO/DMCA/fair use transposé par simple
traduction, aucune liberté d'exploitation complète depuis recherche partielle.
Préalable PILOTE-003 satisfait après BASE-011, limites du pilote consignées ;
aucune adaptation du plugin, sélection d'extension ou action externe ici.

Les suites de clinique sont proposées dans le
[découpage CLN-001 à CLN-023](02-plugins-existants/exist-009-decoupage-clinique.md),
avec [inventaire des 36 fichiers et 16 skills](02-plugins-existants/exist-009-inventaire-clinique.md)
et [relecture notification inconnue et accueil logement](02-plugins-existants/exist-009-verification.md).
Cadre réel, accueil, recherche, rédaction supervisée, échéances et transmission
sont séparés. Aucune bande CA/IL/fédérale chargée dans les futurs parcours
français ; saisie incertaine sans calcul, qui valide et quoi explicités.
Les vingt-trois CLN restent `proposee`, sans adaptation du plugin ni usage de
données bénéficiaires. Préalable PILOTE-003 satisfait après BASE-011 ; limites
du pilote consignées et aucune extension sélectionnée.

Les suites de formation juridique sont proposées dans le
[découpage ETU-001 à ETU-021](02-plugins-existants/exist-010-decoupage-formation.md),
avec [inventaire des 26 fichiers et 13 skills](02-plugins-existants/exist-010-inventaire-formation.md)
et [comparaison cas pratique/commentaire sur extrait français](02-plugins-existants/exist-010-verification.md).
Méthode, retour sur brouillon, révisions et actualisation du droit sont séparés ;
CRFPA à qualifier, sans équivalence MBE ni prédiction de sujet. Les vingt-et-une
ETU restent `proposee`, sans adaptation du plugin ni nouvelle commande disponible.
Préalable PILOTE-003 satisfait après BASE-011, limites du pilote consignées ;
aucune extension sélectionnée par ce cadrage.

Les suites de gestion des skills sont proposées dans le
[découpage HUB-001 à HUB-020](02-plugins-existants/exist-011-decoupage-hub.md),
avec [inventaire des 30 fichiers, 10 skills et un agent](02-plugins-existants/exist-011-inventaire-hub.md)
et [vérification préservation locale et portée Californie](02-plugins-existants/exist-011-verification.md).
La fixture filesystem du helper refuse l’update d’un skill personnalisé sans
altérer fichiers ou journal ; la découverte US reste une relecture d’attendus.
Défauts de confiance, verdicts QA et fraîcheur sont bornés dans vingt suites
`proposee`, sans réécriture du plugin ou application automatique. Préalable
PILOTE-003 satisfait après BASE-011, limites du pilote consignées ; aucune
extension choisie, installation réelle ou notification externe.

| Story | Résultat attendu | Nature | Priorité |
|---|---|---|---|
| [EXIST-001](02-plugins-existants/exist-001-contrats-commerciaux.md) | Découper l'adaptation des contrats commerciaux | cadrage | P2 |
| [EXIST-002](02-plugins-existants/exist-002-societes-operations.md) | Découper l'adaptation du droit des sociétés et des opérations | cadrage | P2 |
| [EXIST-003](02-plugins-existants/exist-003-donnees-personnelles.md) | Découper l'adaptation de la protection des données | cadrage | P2 |
| [EXIST-004](02-plugins-existants/exist-004-produits-publicite.md) | Découper l'adaptation des produits et de la publicité | cadrage | P2 |
| [EXIST-005](02-plugins-existants/exist-005-gouvernance-ia.md) | Découper l'adaptation de la gouvernance IA | cadrage | P2 |
| [EXIST-006](02-plugins-existants/exist-006-contentieux.md) | Cadrage terminé : inventaire et 24 suites contentieuses proposées | cadrage | P2 |
| [EXIST-007](02-plugins-existants/exist-007-veille-reglementaire.md) | Cadrage terminé : inventaire et 20 suites de veille proposées | cadrage | P2 |
| [EXIST-008](02-plugins-existants/exist-008-propriete-intellectuelle.md) | Cadrage terminé : inventaire et 25 suites PI proposées | cadrage | P2 |
| [EXIST-009](02-plugins-existants/exist-009-clinique-juridique.md) | Cadrage terminé : inventaire et 23 suites de clinique proposées | cadrage | P2 |
| [EXIST-010](02-plugins-existants/exist-010-formation-juridique.md) | Cadrage terminé : inventaire et 21 suites de formation proposées | cadrage | P2 |
| [EXIST-011](02-plugins-existants/exist-011-gestion-des-skills.md) | Cadrage terminé : inventaire et 20 suites du hub proposées | cadrage | P2 |

## Nouveaux domaines à cadrer — P2 / P3

Le domaine consommation est cadré dans le
[découpage CONSO-001 à CONSO-013](03-nouveaux-domaines/dom-001-decoupage-consommation.md),
avec [relecture commande non livrée, produit défectueux et achat professionnel](03-nouveaux-domaines/dom-001-verification.md).
Le plugin proposé reste `consumer-legal`, installable seul, sans profil,
agent ni connecteur. Première tranche proposée : CONSO-001, réclamation pour
une commande non livrée, qui crée le paquet avec ce seul skill. Les 14 CONSO
restent `proposee` ; aucun répertoire de plugin n'est créé et aucune tranche
n'est sélectionnée par DOM-001.

Le domaine police et procédure pénale est cadré dans le
[découpage CRIM-001 à CRIM-012](03-nouveaux-domaines/dom-002-decoupage-penal.md),
avec [relecture convocation, garde à vue en cours et avis d'amende](03-nouveaux-domaines/dom-002-verification.md).
Le plugin proposé reste `criminal-legal`, installable seul, sans profil ni
stockage des faits pénaux. Ses garde-fous excluent tout conseil d'évitement
de la justice et tout équivalent Miranda ou subpoena. Première tranche
proposée : CRIM-001, lecture d'une convocation, qui crée le paquet avec ce
seul skill. Les 17 CRIM restent `proposee` ; aucune tranche n'est
sélectionnée par DOM-002.

Le domaine exécution et recouvrement est cadré dans le
[découpage ENF-001 à ENF-011](03-nouveaux-domaines/dom-003-decoupage-execution.md),
avec [relecture relance de recouvrement, signification contestée et saisie sans ventilation](03-nouveaux-domaines/dom-003-verification.md).
Le plugin proposé reste `enforcement-legal`, installable seul, sans profil ;
il ne promet aucune suspension et laisse la dette d'origine à son domaine.
Première tranche proposée : ENF-001, lecture d'un acte et repérage de
l'urgence, qui crée le paquet avec ce seul skill. Les 13 ENF restent
`proposee`, dont l'opposition à une injonction de payer (ENF-012) et la
saisie immobilière (ENF-013) ajoutées le 16 octobre 2026.

Le domaine bancaire est cadré dans le
[découpage BNK-001 à BNK-011](03-nouveaux-domaines/dom-004-decoupage-banque.md),
avec [relecture carte contestée, virement sous tromperie et frais professionnels](03-nouveaux-domaines/dom-004-verification.md).
Le plugin proposé reste `banking-legal`, installable seul, sans profil ni
accès à un compte ; le skill `payment-dispute` est confirmé. Première tranche
proposée : BNK-001, qualification d'un paiement contesté et réclamation, qui
crée le paquet avec ce seul skill. Les 12 BNK restent `proposee`, dont la
caution (BNK-012) ; placements et actifs numériques en orientation seule.

Le domaine assurance est cadré dans le
[découpage INS-001 à INS-011](03-nouveaux-domaines/dom-005-decoupage-assurance.md),
avec [relecture exclusion citée, conditions particulières manquantes et expertise contestée](03-nouveaux-domaines/dom-005-verification.md).
Le plugin proposé reste `insurance-legal`, installable seul, sans profil ni
accès à un espace client. Première tranche proposée : INS-001, analyse d'un
refus de garantie, qui crée le paquet avec ce seul skill. Les 11 INS restent
`proposee`. L'indemnisation des victimes d'accidents de la circulation est
rattachée à DOM-035.

| Story | Résultat attendu | Nature | Priorité |
|---|---|---|---|
| [DOM-001](03-nouveaux-domaines/dom-001-consommation.md) | Cadrer un plugin de droit de la consommation | cadrage | P2 |
| [DOM-002](03-nouveaux-domaines/dom-002-police-penal.md) | Cadrer un plugin police et procédure pénale | cadrage | P2 |
| [DOM-003](03-nouveaux-domaines/dom-003-commissaires-justice-execution.md) | Cadrer un plugin d'exécution et de recouvrement | cadrage | P2 |
| [DOM-004](03-nouveaux-domaines/dom-004-banque.md) | Cadrer un plugin bancaire | cadrage | P2 |
| [DOM-005](03-nouveaux-domaines/dom-005-assurance.md) | Cadrer un plugin d'assurance | cadrage | P2 |
| [DOM-006](03-nouveaux-domaines/dom-006-logement.md) | Cadrer un plugin logement locatif et habitat | cadrage | P2 |
| [DOM-007](03-nouveaux-domaines/dom-007-sante.md) | Cadrer un plugin santé et droits des patients | cadrage | P2 |
| [DOM-008](03-nouveaux-domaines/dom-008-transports.md) | Cadrer un plugin transports et voyages | cadrage | P2 |
| [DOM-009](03-nouveaux-domaines/dom-009-douanes.md) | Cadrer un plugin douanes et import-export | cadrage | P2 |
| [DOM-010](03-nouveaux-domaines/dom-010-administratif.md) | Cadrer un plugin de droit administratif | cadrage | P3 |
| [DOM-011](03-nouveaux-domaines/dom-011-fiscalite.md) | Cadrer un plugin de fiscalité | cadrage | P3 |
| [DOM-012](03-nouveaux-domaines/dom-012-protection-sociale.md) | Cadrer un plugin de sécurité sociale et prestations | cadrage | P2 |
| [DOM-013](03-nouveaux-domaines/dom-013-famille-patrimoine.md) | Cadrer un plugin famille et patrimoine du couple | cadrage | P2 |
| [DOM-014](03-nouveaux-domaines/dom-014-agriculture-rural.md) | Cadrer un plugin agricole et rural | cadrage | P2 |
| [DOM-015](03-nouveaux-domaines/dom-015-construction-travaux.md) | Cadrer un plugin construction et travaux | cadrage | P2 |
| [DOM-016](03-nouveaux-domaines/dom-016-successions-donations.md) | Cadrer un plugin successions et donations | cadrage | P2 |
| [DOM-017](03-nouveaux-domaines/dom-017-transactions-immobilieres.md) | Cadrer un plugin d'achat et de vente immobilière | cadrage | P2 |
| [DOM-018](03-nouveaux-domaines/dom-018-copropriete.md) | Cadrer un plugin copropriété et syndic | cadrage | P2 |
| [DOM-019](03-nouveaux-domaines/dom-019-urbanisme-foncier.md) | Cadrer un plugin urbanisme et foncier | cadrage | P3 |
| [DOM-020](03-nouveaux-domaines/dom-020-voisinage-servitudes.md) | Cadrer un plugin voisinage et servitudes | cadrage | P2 |
| [DOM-021](03-nouveaux-domaines/dom-021-energie-eau.md) | Cadrer un plugin énergie, eau et services essentiels | cadrage | P2 |
| [DOM-022](03-nouveaux-domaines/dom-022-telecoms-poste.md) | Cadrer un plugin télécoms et services postaux | cadrage | P2 |
| [DOM-023](03-nouveaux-domaines/dom-023-vehicules-garages.md) | Cadrer un plugin véhicules, garages et réparations | cadrage | P2 |
| [DOM-024](03-nouveaux-domaines/dom-024-dettes-surendettement.md) | Cadrer un plugin dettes et surendettement des particuliers | cadrage | P2 |
| [DOM-025](03-nouveaux-domaines/dom-025-handicap-autonomie.md) | Cadrer un plugin handicap et autonomie | cadrage | P2 |
| [DOM-026](03-nouveaux-domaines/dom-026-protection-majeurs.md) | Cadrer un plugin de protection juridique des majeurs | cadrage | P2 |
| [DOM-027](03-nouveaux-domaines/dom-027-education-formation.md) | Cadrer un plugin éducation et formation | cadrage | P2 |
| [DOM-028](03-nouveaux-domaines/dom-028-sejour-nationalite-asile.md) | Cadrer un plugin séjour, nationalité et asile | cadrage | P2 |
| [DOM-029](03-nouveaux-domaines/dom-029-discriminations.md) | Cadrer un plugin discriminations et égalité d'accès | cadrage | P2 |
| [DOM-030](03-nouveaux-domaines/dom-030-environnement-pollutions.md) | Cadrer un plugin environnement et pollutions | cadrage | P3 |
| [DOM-031](03-nouveaux-domaines/dom-031-deces-obseques.md) | Cadrer un plugin décès et prestations funéraires | cadrage | P2 |
| [DOM-032](03-nouveaux-domaines/dom-032-associations-adherents.md) | Cadrer un plugin associations et droits des adhérents | cadrage | P3 |
| [DOM-033](03-nouveaux-domaines/dom-033-animaux.md) | Cadrer un plugin animaux et responsabilités | cadrage | P3 |
| [DOM-034](03-nouveaux-domaines/dom-034-numerique-plateformes.md) | Cadrer un plugin numérique et plateformes du quotidien | cadrage | P2 |
| [DOM-035](03-nouveaux-domaines/dom-035-responsabilite-dommages.md) | Cadrer un plugin responsabilité civile et dommages | cadrage | P2 |
| [DOM-036](03-nouveaux-domaines/dom-036-retraites.md) | Cadrer un plugin retraites et droits de carrière | cadrage | P2 |
| [DOM-037](03-nouveaux-domaines/dom-037-fonction-publique.md) | Cadrer un plugin fonction publique et agents publics | cadrage | P2 |
| [DOM-038](03-nouveaux-domaines/dom-038-violences-intrafamiliales.md) | Cadrer un plugin violences intrafamiliales et protection | cadrage | P2 |
| [DOM-039](03-nouveaux-domaines/dom-039-micro-entreprise.md) | Cadrer un plugin micro-entreprise et travail indépendant | cadrage | P2 |

## Livraison d'un lot vérifié

[LIV-001](04-livraison/liv-001-livrer-lot-borne.md) a préparé le lot 001 :
`judge-fr-eu-employment-legal` 0.2.1 seul, construit hors du checkout par
`scripts/build-lot.py` et installé dans une configuration jetable
([vérification](04-livraison/liv-001-verification.md),
[notes de version](04-livraison/liv-001-notes-version.md)). Close le
16 octobre 2026 par décision de l'utilisateur, sur la base de la recette
BASE-011 ; l'invocation sur l'artefact 0.2.1 n'a pas été exécutée.
Publication uniquement vers le dépôt `Francois-Louis/Judge`.

| Story | Résultat attendu | Nature | Priorité |
|---|---|---|---|
| [LIV-001](04-livraison/liv-001-livrer-lot-borne.md) | Préparer une livraison limitée au périmètre adapté | livraison | P2 |

## Limites de ce lot

Les stories de cadrage ne modifient pas les plugins. Les stories
d'implémentation BASE-007, BASE-008 et BASE-009 ont modifié localement le
workflow CLA, les manifestes, les chemins de stockage, des formulations du hub
et des scripts ; elles n'adaptent aucune tâche juridique France/UE. Les scripts
de preuve utilisent exclusivement des profils factices temporaires. Aucun push,
PR ou changement GitHub n'est effectué ; une publication distante reste une
opération distincte, préparée par LIV-001.
