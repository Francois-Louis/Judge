# PILOTE-002 — bilan d'implémentation et de vérification

15 octobre 2026 (Europe/Paris). Story **a-verifier**. La demande d'implémentation
retient le pilote ; elle ne vaut pas recette utilisateur ni publication.

Le plugin `judge-fr-eu-employment-legal` passe de `0.1.0` à **`0.2.0`**.
Révision de départ et empreintes de l'artefact sont dans les
[preuves techniques](pilote-002-controles.json). Les changements restent locaux.

## Périmètre réalisé

- `hiring-review` : lecture d'une offre ou d'un contrat reçu, CDI privé en
  France métropolitaine ; contrôles CDD explicites ; hors champ orienté.
- Qualification de l'activité réelle, convention/champ, accords et dates,
  fonctions/classification, salaire, temps, essai et restrictions. Retrait du
  workflow américain et de ses feux verts automatiques.
- Accueil candidat sans playbook ni profil société obligatoire ; entretien
  factuel dans la conversation, sauvegarde volontaire seulement. Exceptions
  ciblées aux consignes du profil hérité, branches courtes de configuration.
- Tableau clause/source/conséquence/proposition, faits manquants prioritaires,
  question et destinataire. USAGE-001 `1.0.0` repris dans le skill, sans lien
  requis vers le backlog. Aucun envoi, acceptation, signature ou suivi.
- Références locales métier `1.0.0` et chargement de la méthode BASE-005
  `1.0.0`. README, notices, manifeste et marketplace concordants.

Les autres skills, l'agent congés et la configuration professionnelle hors
pilote restent hérités, non adaptés. Aucun composant métier supplémentaire
n'est appelé par la revue. Le hook livré est vide ; les connecteurs Slack et
Google Drive restent déclarés, aucun appel ni disponibilité déduit du manifeste.

## Dépendances du parcours

| Ressource | Nature et traitement |
|---|---|
| Frontière de stockage et helper Python | Embarqués, inchangés ; Python 3.12+ pour les accès persistants. Aucun profil réel lu pendant la maintenance. |
| Méthode BASE-005 | Embarquée et identique octet pour octet à la source versionnée ; empreintes dans le JSON de contrôle. |
| Repères métier | Embarqués ; articles effectivement lus et pistes non vérifiées distingués. Aucun import du dépôt au runtime. |
| Profil et dossier actif | Données utilisateur facultatives pour la simple lecture ; accès via helper, entretien neuf si absents, respect de l'isolation. |
| Contrat, extraits, annexes, faits et textes collectifs | Entrées explicites ; demander seulement les passages déterminants, masquer les données inutiles. |
| Publications officielles | Nécessaires aux conclusions juridiques, pas à l'explication factuelle ; accès réellement testé ou réserve ciblée. Aucun abonnement API imposé. |
| Autre régime / professionnel | Orientation et question précises, sans import de plugin, envoi ou commande proposée comme disponible. |

## Résultats par couche

| Contrôle | Résultat constaté et limite |
|---|---|
| JSON/YAML, nom canonique et liens locaux | Contrôle du paquet séparé : aucun `ECHEC`. `STRUCTURE INCOMPLET`, code 2, en raison des `A_RELIRE` de profils/chemins dynamiques et d'une orientation historique vers le hub. Ce n'est pas un paquet entièrement validé. |
| Comparaison de méthode | Réussie, copie complète identique à BASE-005 `1.0.0` ; empreintes conservées. |
| Schéma officiel plugin | `NON_EXECUTE` : CLI `claude` absente. Option `--schema` effectivement demandée au contrôleur. |
| Schéma officiel marketplace | `NON_EXECUTE`, même absence de CLI. Syntaxe JSON et cohérence nom/description/auteur vérifiées par la suite d'isolation. |
| Skill Creator `quick_validate.py` | Exécuté : refuse le champ `argument-hint` déjà présent dans le skill Claude hérité. Champ conservé ; le validateur Codex générique ne valide pas ce dialecte. Le contrôle de paquet parse le frontmatter ; aucun succès de schéma officiel n'en est déduit. |
| Régression stockage / noms / paquets détachés | Suite BASE-008 exécutée : 16 tests, 14 réussis et 2 ignorés (jsonschema absent ; privilège Windows de lien symbolique absent). La version attendue d'employment est mise à jour ; le test de mise à jour incrémente désormais la version de son paquet factice. |
| Installation / invocation réelle | `NON_EXECUTE`, CLI Claude absente ; copie et archive hors checkout ne constituent pas une installation. Aucune observation de comportement autonome revendiquée. |
| Sources juridiques | 28 articles reproduits par le CDTN lus, avec texte et dates affichées conservés. Deux accès Légifrance 403 suivis d'une lecture CDTN traçables ; décision sur non-concurrence inaccessible. Aucun texte conventionnel spécifique certifié. |
| Relecture rédactionnelle | Quatre cas de revue/orientation et un brouillon consignés ; calculs simples vérifiés. Ce travail par le rédacteur ne remplace ni le client isolé ni une relecture juridique indépendante. |
| Compréhension non juriste | `NON_EXECUTE` : aucun participant réel, aucune réponse inventée. |

Le journal complet du contrôle, l'inventaire et l'empreinte ZIP se trouvent
dans les preuves techniques. L'artefact reste dans un répertoire temporaire
séparé ; il n'est ni publié ni installé chez l'utilisateur.

## Relecture des points A_RELIRE

Les chemins du fork décrivent les données persistantes : ils restent sous le
contrat du helper, vérifié par les tests BASE-008 sur profils factices. Leur
usage effectif par le modèle demeure à éprouver. La mention historique du
profil personnel dans l'entretien est une interdiction de le lire ; ce n'est
pas une dépendance du parcours candidat. Le profil société, l'orientation
vers le hub et les dossiers congés/enquêtes/expansion appartiennent aux
branches héritées ; ils ne sont pas requis pour le pilote.

Les `A_RELIRE` ne sont pas supprimés ni transformés en réussite générale.
Le client de recette devra observer que le chemin candidat ne charge pas
ces branches et ne lit aucun autre dossier. Les tests de helper ne prouvent
pas à eux seuls que le modèle utilisera correctement le helper.

## Scénarios et sources réellement utilisées

[Pièces d'entrée H01–H14](pilote-002-pieces-fictives.md),
[sorties rédigées et relues](pilote-002-sorties-relecture.md),
[passages et accès de maintenance](pilote-002-sources-lues.json).
Le statut d'exécution dans un client isolé est **non exécuté pour tous**.

| Cas | Travail rédactionnel observé | Contrôle restant |
|---|---|---|
| H01 | Variante CDI simple relue : brut/annuel et heures expliqués, essai sourcé, prime et classification réservées. | Nominal complet non réalisé : textes collectifs applicables et annexes à obtenir/lire, client isolé, lecteur réel. |
| H02 | Pièce préparée ; instruction de recherche par clause réécrite. | Exécuter essai/renouvellement/restrictions et annexe absente ; jurisprudence utile à lire. |
| H03 | CDD incomplet relu sur L1242-1/-2/-7/-10/-12/-13 et L1245-1 ; aucune transposition CDI ni requalification annoncée comme acquise. | Client isolé, versions au début futur, compléments CDD et lecteur réel. |
| H04 | APE et poste traités comme indices ; CCN inconnue, question RH et pièces ciblées. L2261-2 effectivement lu. | Client isolé et cas avec champ collectif établi. |
| H05 | Pièce préparée et contrôle forfait explicite. | Exécuter avec accord/écrit individuel et autonomie réelle, rechercher garanties et décisions. |
| H06 | Variantes d'accords préparées ; instruction d'articulation par matière. L2253-1/-2/-3 et L2254-1 lus. | Analyse concrète d'accords authentifiés et de leurs dates. |
| H07 | Orientation France/Belgique rédigée ; loi/juridiction/exécution distinguées, aucune règle de fond étrangère appliquée. | Client isolé ; recherche transfrontalière hors périmètre de cette tranche. |
| H08 / H09 | Pièces public / outre-mer préparées ; qualification/orientation dans le skill. | Exécution réelle des deux frontières. |
| H10 | Pièce ancien modèle / début futur préparée, contrôle temporel explicite. | Exécution et recherches de versions/transitions pertinentes. |
| H11 | Accès Légifrance 403 et CDTN 200 réellement observés pendant la recherche de maintenance. | Comportement du skill après refus puis indisponibilité complète à éprouver en client ; pas de panne simulée revendiquée. |
| H12 | Chemin court et cas sans profil préparés ; helper testé séparément. | Exécution du setup et revue sans profil ni connecteur dans un environnement réellement isolé. |
| H13 | Brouillon court rédigé, sans acceptation ni envoi. | Client isolé et essai de compréhension. |
| H14 | Pièce hostile/illisible préparée ; règles d'intégrité et de couverture inscrites. | Exécution du scénario et observation des accès effectifs. |

Les dates affichées par le CDTN et les empreintes HTTP sont des traces de
lecture ; elles ne certifient pas une version historique, l'absence de réforme
future ni l'applicabilité à une entreprise réelle. Le relevé conserve les
statuts techniques d'origine (`non-verifie`, `a-etablir`) et ajoute séparément
la lecture de maintenance. Une décision seulement trouvée par moteur reste
non vérifiée si son texte n'a pas pu être lu.

## Conditions de clôture

Poursuivre la recette PILOTE-003 sur cet artefact : validation officielle,
environnement isolé avec profil vierge, commande exacte de revue, ressources
et accès observés, nominal avec textes collectifs lus et variantes H01–H14.
Faire ensuite lire la sortie à une personne sans formation juridique, sans
aide du rédacteur. Consigner sa reformulation de l'engagement, de la question,
de l'interlocuteur et de la réserve, puis les corrections et une nouvelle
lecture si nécessaire. Les critères correspondants restent non cochés.

Aucun problème d'accès ou outil manquant ne justifie de déclarer ces contrôles
réussis. Le lot reste local, sans publication.
