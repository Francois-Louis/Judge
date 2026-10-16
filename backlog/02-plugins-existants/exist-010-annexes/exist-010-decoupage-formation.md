# EXIST-010 — Découpage de la formation juridique

Vingt-et-une suites **proposées**, à sélectionner une par une ; aucun nouveau
skill, nom de commande ou comportement ci-dessous n’est implémenté.
Le plugin principal est `law-student` ; une tâche garde une sortie bornée.
L’[inventaire](exist-010-inventaire-formation.md) couvre les treize skills et
les treize autres fichiers effectivement présents.

## Tâches et ordre des préalables

Toutes les suites dépendent de EXIST-010, PILOTE-003, BASE-005 et BASE-006.
La colonne finale donne les autres préalables ETU. ETU-021 dépend de ETU-001 ;
les numéros ne constituent pas un ordre d’exécution.

| Suite | Tâche | Résultat distinct | Autres préalables |
|---|---|---|---|
| [ETU-001](../suites/etu-001-qualifier-exercice.md) | Qualifier la consigne et le cadre d’un exercice | Une fiche de contexte distingue exercice, entraînement ou travail évalué, corpus, date de référence et aide autorisée avant de choisir une tâche. | Contexte du lot seulement |
| [ETU-002](../suites/etu-002-entrainement-cas-pratique.md) | Guider un entraînement de cas pratique | Un entraînement conduit l’apprenant à qualifier faits et questions, choisir une règle sourcée puis l’appliquer, selon la consigne réelle. | ETU-001 |
| [ETU-003](../suites/etu-003-retour-cas-pratique.md) | Relire le raisonnement d’un cas pratique | Un retour sur un brouillon localise les étapes réussies ou manquantes sans écrire la copie corrigée. | ETU-001, ETU-002 |
| [ETU-004](../suites/etu-004-fiche-arret.md) | Accompagner une fiche d’arrêt | Une trame de fiche distingue faits pertinents, procédure, prétentions/moyens, question et solution selon les seuls passages disponibles. | ETU-001 |
| [ETU-005](../suites/etu-005-methode-commentaire-arret.md) | Guider la méthode d’un commentaire d’arrêt | Un skill distinct aide à construire une lecture du sens, de la valeur et de la portée de la décision selon la consigne. | ETU-001, ETU-004 |
| [ETU-006](../suites/etu-006-retour-commentaire-arret.md) | Relire un brouillon de commentaire d’arrêt | Le retour repère paraphrase, détachement des motifs ou portée non étayée et demande une reprise ciblée. | ETU-001, ETU-005 |
| [ETU-007](../suites/etu-007-methode-dissertation.md) | Accompagner la méthode d’une dissertation | L’apprenant délimite un sujet, construit une question et justifie son organisation avec ses sources. | ETU-001 |
| [ETU-008](../suites/etu-008-retour-dissertation.md) | Relire un brouillon de dissertation | Un retour distingue délimitation du sujet, démonstration et cohérence du plan selon les attentes fournies. | ETU-001, ETU-007 |
| [ETU-009](../suites/etu-009-methode-note-synthese.md) | Accompagner une note de synthèse sur dossier | Une méthode de lecture et de classement aide l’apprenant à synthétiser un dossier délimité selon la consigne. | ETU-001 |
| [ETU-010](../suites/etu-010-retour-note-synthese.md) | Relire un brouillon de note de synthèse | Le retour vérifie couverture du dossier, fidélité et organisation sans ajouter une opinion ou réécrire la note. | ETU-001, ETU-009 |
| [ETU-011](../suites/etu-011-lecture-orale-guidee.md) | Préparer une discussion orale sur une décision | Des questions progressives entraînent à expliquer les passages d’une décision sans prévoir celles d’un professeur. | ETU-001, ETU-004 |
| [ETU-012](../suites/etu-012-fiches-revision.md) | Construire des fiches de révision à partir du cours | Un support de révision conserve les sources et contributions de l’apprenant, sans remplir un cours de mémoire. | ETU-001 |
| [ETU-013](../suites/etu-013-cartes-revision.md) | Créer et revoir des cartes sourcées | Des cartes rattachées au cours/version sont revues par autoévaluation, sans certifier l’état du droit ni la mémorisation. | ETU-001, ETU-012 |
| [ETU-014](../suites/etu-014-session-journal.md) | Router une séance et consigner un seul bilan | Une séance choisit une tâche adaptée à la consigne et enregistre un événement unique attribué, sans défaut MBE. | ETU-001, ETU-021 |
| [ETU-015](../suites/etu-015-plan-revision.md) | Construire un plan de révision réaliste | Un planning proposé utilise échéance et disponibilité déclarées sans inventer calendrier officiel ni sujets probables. | ETU-001, ETU-021 |
| [ETU-016](../suites/etu-016-analyse-annales.md) | Décrire les annales sans prédire le sujet | Un relevé descriptif montre corpus, occurrences, changements de programme et limites ; aucune probabilité de futur sujet. | ETU-001 |
| [ETU-017](../suites/etu-017-actualiser-point-droit.md) | Vérifier un point de droit pour une révision | Une vérification ponctuelle et sourcée établit l’état documentaire d’un point daté, distinct de la méthode et du contenu historique du cours. | ETU-001 |
| [ETU-018](../suites/etu-018-qualifier-crfpa.md) | Qualifier une préparation au CRFPA | Une fiche précise année, épreuve, matière/option, consigne et statut des règles consultées avant tout entraînement. | ETU-001 |
| [ETU-019](../suites/etu-019-entrainement-crfpa-cas-pratique.md) | Entraîner un cas pratique dans un contexte CRFPA défini | Un exercice fictif et un retour guidé respectent l’épreuve qualifiée, sans questions américaines traduites ou note prédictive. | ETU-002, ETU-003, ETU-018 |
| [ETU-020](../suites/etu-020-preferences-apprenant.md) | Configurer les préférences d’un apprenant | Un profil minimal et modifiable renseigne cursus, objectifs et préférences déclarées sans autoriser des aides interdites ou prévoir l’examen. | ETU-001, ETU-021 |
| [ETU-021](../suites/etu-021-donnees-apprentissage.md) | Isoler et documenter les données d’apprentissage | Un contrat local sépare cours/année/exercice, modèles installés et données de l’apprenant, sans fusion ou migration implicite. | ETU-001 |

Première tranche suggérée : **ETU-001**, qualification de la consigne, sans
sélection implicite de sa réalisation. Ensuite choisir un exercice et son
retour utile ; ETU-021 précède toute nouvelle persistance de séance/plan/profil.
Ne pas livrer les vingt-et-une suites comme une réécriture générale.
PILOTE-003 est terminé après BASE-011 ; restent les limites H01 complet et
lecteur indépendant du bilan. Ce préalable satisfait ne vaut ni extension
choisie, ni validation des exercices, sources ou intégrations de ce domaine.

## Des exercices différents selon la consigne

| Demande réelle | Travail de l’apprenant et aide attendue | Ce que la tâche ne peut pas déduire |
|---|---|---|
| Cas pratique | Qualifier des faits hypothétiques, poser les questions, justifier règle et application puis conclusion ; questions guidées ETU-002, retour ETU-003. | Pas un commentaire sur la valeur d’un arrêt ; IRAC n’est ni obligatoire ni un barème français. |
| Fiche d’arrêt | Dégager depuis le texte les éléments demandés : faits, procédure, positions, question, solution ; trame ETU-004. | La fiche ne suffit pas à faire un commentaire, et un extrait ne révèle pas toute la procédure. |
| Commentaire d’arrêt | Lire la décision et argumenter sur son raisonnement, sens, valeur ou portée selon la consigne ; méthode ETU-005 et retour ETU-006. | Pas application de l’arrêt à un nouveau cas ; portée non établie sans corpus pertinent. |
| Dissertation | Délimiter le sujet, construire une question et une démonstration justifiée ; méthode ETU-007 et retour ETU-008. | Pas IRAC, consultation ou plan à deux parties imposé faute de consigne. |
| Note de synthèse | Organiser fidèlement un dossier défini, selon les règles de l’épreuve ; méthode ETU-009 et retour ETU-010. | Dossier fermé ne reçoit pas une règle extérieure issue d’une actualisation. |
| Préparation CRFPA | D’abord préciser session, épreuve, matière, modalités et sources officielles ETU-018 ; puis tâche correspondante, premier cas pratique ETU-019. | Ni examen unique générique ni traduction MBE/UBE/NextGen ; aucun calendrier français fixé ici. |

Ces éléments sont des distinctions de travail, pas des règles nationales
uniformes de correction. Le texte exact de l’établissement ou de l’épreuve
détermine ce qu’il est demandé et quelles aides sont permises.

## Noms, retraits et compatibilité

Les chemins techniques existants `irac-practice`, `bar-prep-questions`,
`case-brief`, `cold-call-prep`, `outline-builder` et `exam-forecast` sont
initialement conservés pour ne pas inventer des alias. Leurs titres et
descriptions futurs doivent annoncer la tâche française effectivement livrée :
cas pratique, préparation CRFPA qualifiée, fiche d’arrêt, discussion orale,
fiches de révision et analyse descriptive d’annales. Le chemin hérité
`exam-forecast` ne doit plus porter une promesse prédictive, même assortie
d’un avertissement.

Aucune commande américaine n’est conservée comme mode français par inertie.
MBE/MEE/MPT, NextGen, majority/state rule, calendriers CA et « mixed si silence »
sont retirés du parcours français proposé. Les formats américains ne sont pas
réétiquetés France. Une éventuelle prise en charge américaine ultérieure serait
un périmètre séparé explicitement demandé, pas une branche livrée par ce cadrage.

Si un futur lot choisit un renommage technique, il doit d’abord constater un
usage réel qui justifie la compatibilité, créer le chemin canonique et mettre
à jour références, README et manifeste. Un alias éventuel ne fait que rediriger
vers la tâche canonique ; pas de second moteur ni d’ancienne correction US.
Aucun alias n’est requis à ce stade. Les quatre nouveaux chemins proposés
(commentaire-arret, dissertation, note-synthese, actualiser-point-droit) ont
chacun un propriétaire et ne sont pas cités comme commandes disponibles.

## Méthode, sources, révision et données

- ETU-001 qualifie la consigne et l’intégrité ; le mode pédagogique ne permet pas
  la rédaction substitutive, une aide interdite ou la dissimulation d’usage.
  Inconnue de consigne : aide générale limitée, pas politique inventée.
- ETU-002 à 011 et 019 guident ou relisent un travail de l’apprenant. Méthode,
  exemple abstrait et retour localisé restent distincts d’un corrigé intégral
  ou d’un plan substantiel prêt à remettre.
- ETU-012/013 construisent des supports datés ; ETU-014 consigne une séance ;
  ETU-015 propose le temps de travail ; ETU-016 décrit les annales. Aucun poids
  de sujet futur, apprentissage garanti, note ou succès déduit.
- ETU-017 vérifie un point de droit daté à partir de sources réellement lues,
  à part de l’exercice. Retrieval, lecture et applicabilité sont des états
  distincts. Ne pas transformer cours historique ou dossier fermé en droit
  actuel par une correction silencieuse.
- ETU-018 vérifie les modalités officielles de la session ciblée, au moment de
  l’implémentation et de l’usage ; aucune date/durée/coefficient français n’est
  validé dans le présent lot.
- ETU-020 possède préférences et entretien ; ETU-021 possède le contrat des
  données cours/année/exercice ; ETU-014 possède événements et producteur unique.
  Plan/cartes/trackers ne constituent pas des preuves équivalentes de compétence.

Chaque entrée adaptée doit lire isolation, méthode et références métier
**embarquées**. Les cinq copies partagées restent identiques ; ne pas déplacer
la dépendance vers un autre paquet. Supports absents : question ciblée et
travail de méthode utile, sans règle inventée ni obligation de connecter Drive,
Slack ou un moteur américain. Vérifier les permissions d’usage des supports et
la portée d’accès aux données. Pas de données personnelles d’étude dans le paquet.

## Coordination des fichiers communs

Les références à créer sont attribuées à leur unique suite propriétaire.
Les autres suites les consomment après ce préalable. Les retours ETU-006/008/010
partagent legal-writing : les implémenter séparément, conserver leurs modes
déjà adaptés et rejouer les scénarios concernés à chaque nouvelle branche.
Même règle pour irac-practice (002/003/019), bar-prep (018/019) et les journaux
014/021. Pas de duplication de skill de correction par exercice pour éviter
ce partage.

Une future nouvelle entrée doit documenter son nom canonique, frontmatter,
déclencheur, entrées, exclusions, références locales et sortie, puis adapter
version, NOTICE et documentation aux seuls comportements livrés ; synchroniser
les champs du marketplace si ceux du manifeste changent. Vérification BASE-006
sur paquet extrait, recette pédagogique, droit/sources et installation client
sont des résultats séparés. Un lecteur indépendant et une vérification
institutionnelle réelle restent à obtenir.

La [relecture comparative](exist-010-verification.md) utilise deux consignes
fictives et un [extrait français traçable](exist-010-support-verification.json).
Le [contrôleur](exist-010-controles.py) vérifie structure, couverture et liens ;
il n’exécute pas ces futures tâches.

