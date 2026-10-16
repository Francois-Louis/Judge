# EXIST-010 — Inventaire de la formation juridique

Lecture locale du 16 octobre 2026 : **26 fichiers, 13 skills invocables** dans
`law-student`, aucun agent, alias déprécié ou cookbook propre. L’inventaire porte
sur les fichiers livrés, pas sur un environnement étudiant installé. Les chemins
des deux tableaux sont relatifs à `law-student/` ; dans le premier, à `skills/`.
Les décisions ci-dessous sont des adaptations proposées, aucune déjà livrée.

## Les treize skills

| Fichier | Comportement et dépendances réellement présents | Décision individuelle et justification | Suites |
|---|---|---|---|
| `bar-prep-questions/SKILL.md` | Gate NCBE/NextGen/UBE/État, MBE/MEE/MPT, majority/state rules ; questions de modèle et explications « confident » ; `--session` alimente plan ou journal. Mode mixed prévu aussi en absence de réponse, malgré la consigne de ne pas choisir silencieusement. | Réécrire pour une épreuve française qualifiée ; retirer les défauts américains du parcours français. Renommer l’intitulé visible en préparation CRFPA uniquement si cette cible est établie. Garder le chemin technique au départ, sans équivalence MBE/CRFPA. | ETU-001, 014, 018, 019 |
| `case-brief/SKILL.md` | Trame Facts/Issue/Holding/Reasoning/Rule/Notes, apprenant propose d’abord ; texte fourni cité, mais repli sur mémoire du nom de décision en tension avec interdiction de fiche complète. | Conserver l’étayage, réécrire en fiche d’arrêt à partir du texte lu ; retirer la restitution de mémoire et les rubriques inventées. Séparer commentaire et fiche ; intitulé français, chemin conservé initialement. | ETU-001, 004, 005 |
| `cold-call-prep/SKILL.md` | Prévision de 6–10 questions et des préférences du professeur, classement de vraisemblance, dissent suggéré et repli mémoire ; dialogue question/réponse. | Conserver l’oral guidé, réécrire et renommer visiblement en préparation de discussion ; retirer prédiction des questions, profilage du professeur et dissent obligatoire. Une date/identité réelle dans un arrêt n’est pas automatiquement un dossier client. | ETU-011 |
| `cold-start-interview/SKILL.md` | JD/1L/2L/3L/bar, matières/faiblesses, intake de 10–20 documents avec LIMITED DATA sous dix, noms de professeur tirés des supports ; lancement automatique de questions bar après entretien. Copie le modèle de profil dans la configuration active via helper. | Réécrire l’entretien pour le cursus réel ; conserver configuration minimale et droits d’accès. Retirer collecte obligatoire de notes, seuil de qualité arbitraire, prédiction et lancement MBE. Préférences ≠ consigne d’évaluation ni source de droit. | ETU-018, 020 |
| `customize/SKILL.md` | Modifie cours, styles d’examen, bar jurisdiction, préférences, sources et indicateurs de faiblesse. | Conserver l’utilitaire canonique, réécrire champs utiles ; aucune préférence ne permet de contourner intégrité, restrictions d’aide ou accès aux supports. Pas de renommage technique de confort. | ETU-020 |
| `exam-forecast/SKILL.md` | Annales du même professeur, syllabus, occurrences puis poids futurs ; confiance strong à six examens, pondération 3–5x, allocation de révision et « probably not coming back ». Les poids sont consommés par outline/cards/IRAC malgré réserves de non-prédiction. | Conserver le descriptif, retirer la promesse prédictive et ses recommandations dérivées. Intitulé « analyse descriptive d’annales » ; chemin exam-forecast provisoirement maintenu comme nom hérité explicite. Un grand échantillon ne valide pas une prévision du prochain sujet. | ETU-016 |
| `flashcards/SKILL.md` | Cartes markdown avec source, buckets et next review ; autoévaluation right/partial/wrong, intervalles Leitner ; génération depuis cours ou connaissances ; journal n_cards/right/partial/wrong/stuck_topics. | Conserver cartes et autoévaluation, réécrire provenance/version ; retirer règle de mémoire réputée certaine, pondération prédictive et promesse implicite d’actualité. Intervalles proposés ne sont pas rappels programmés ni preuve d’apprentissage. | ETU-013, 014, 016, 017, 021 |
| `irac-practice/SKILL.md` | Hypothèse fournie ou générée, retour sur structure/règle/application, grades Pass/borderline/not yet ; exemple abstrait limité, interdiction de réécrire la copie. | Conserver l’effort de l’apprenant, réécrire entraînement et retour de cas pratique ; retirer IRAC comme standard universel, majority rule, barème et promesse de réussite. Séparer modes dans les suites ; intitulé français sans nouvelle commande fictive. | ETU-001, 002, 003, 014, 016, 019 |
| `legal-writing/SKILL.md` | Retour sans réécriture ; memo/brief/paper/essay, Bluebook/ALWD, suivi de patterns à partir de trois observations ; exemple générique sans réponse substantielle. | Conserver la lecture de brouillon, réécrire critères par commentaire/dissertation/synthèse et consigne ; retirer normes US automatiques. Aucun plan français uniforme ou note officielle déduit. Les méthodes initiales ont des tâches distinctes du retour. | ETU-001, 005–010 |
| `outline-builder/SKILL.md` | Arbre vide, apprenant remplit depuis cours ; interdit de remplir de mémoire mais override autorise une majority rule non marquée si modèle confiant. | Conserver fiche de révision et sources ; réécrire, retirer cet override et les poids forecast. Nom visible fiche/support de révision ; pas plan de dissertation ni fiche d’arrêt. | ETU-012, 016, 017 |
| `session/SKILL.md` | Dispatcher `--mbe` par défaut pour bar, `--essay` vers bar-prep, `--flashcards` ; ajoute au journal alors que feuilles écrivent aussi ; plan.session_history ou fallback. | Conserver séance bornée, réécrire routage français et écriture unique/idempotente. Retirer défaut MBE et agrégation de mesures hétérogènes. Une séance interrompue ne devient pas terminée. | ETU-001, 014, 018, 021 |
| `socratic-drill/SKILL.md` | Question/réponse/indices et pas de solution même en cas de blocage ; renvoi au texte ; argument du futur bar exam, gate real matter et journal. | Conserver le dialogue, réécrire cadre/consigne et confort de l’apprenant ; retirer pression liée à un examen supposé et présomption de statut de non-juriste. Consigner sans doubler les bilans de session. | ETU-011, 014 |
| `study-plan/SKILL.md` | Modèle inline study-plan.yaml, phases 60/30/10 et cram 80/20, calendriers CA/NextGen/UBE, historique et pondérations ; questionnement de contraintes personnelles même connues. | Conserver plan modifiable, réécrire selon date/provenance, disponibilité et programme réels. Retirer calendriers US, poids prédictifs et collecte personnelle imposée ; séparer proposition de planning et rappels réellement créés. | ETU-014, 015, 016, 021 |

## Les treize autres fichiers du plugin

| Fichier | Contenu et dépendance | Décision et responsable futur |
|---|---|---|
| `.claude-plugin/plugin.json` | Identité technique judge-fr-eu-law-student, version 0.1.0, description d’accompagnement sans écrire pour l’apprenant. | Conserver identité ; version/description à adapter seulement à une tâche livrée (ETU-005/007/009/017 si nouveau skill), miroir marketplace si champ commun change. Pas de réécriture de manifeste dans le cadrage. |
| `.gitignore` | Exclusions de paquet propres au domaine. | Conserver, pas d’unification ; données d’étude hors paquet prévues par BASE-008/ETU-021. |
| `.mcp.json` | Quatre déclarations : Slack, Google Drive, CourtListener, Descrybe ; catégories legal-research/case-law/documents/chat. | Conserver sans revendiquer connexion authentifiée ou couverture FR/UE ; CourtListener est décrit comme corpus US. Aucun accès officiel CRFPA, moteur de droit français, planning ou système de répétition n’en découle. Toute évolution future est bornée à une capacité démontrée. |
| `CLAUDE.md` | Modèle de profil utilisateur, pas contexte automatiquement chargé ; garde-fous, study-notes header, parcours US, professor names, answer anyway, flag-but-don’t-use et verification-log. | Conserver filet partagé et identité d’aide pédagogique ; réécrire champs ETU-020, contexte ETU-001, données ETU-021 et vérification ETU-017. L’aide générique ne contourne pas les restrictions ; un point incertain n’est pas appliqué comme vrai. Journal de vérification borné par source/version/date, pas certification permanente. |
| `hooks/hooks.json` | Stub vide. | Conserver ; aucun hook métier, alerte, écriture ou calendrier réellement automatique. |
| `LICENSE` | Licence héritée. | Conserver inchangée, y compris lors des adaptations. |
| `NOTICE` | Attribution et historique du paquet. | Conserver ; entrée datée lors d’une future suite qui modifie le paquet, pas pour EXIST-010 limité au backlog. |
| `README.md` | Table de douze commandes omettant customize ; prévision et formats US ; « everything else in working directory » contradictoire avec isolation active rappelée plus loin. | Réécrire seulement pour les tâches effectivement livrées, ETU-021 pour stockage/table réelle ; annonces d’autres suites restent proposées. Méthode/retour/révisions/droit actuel distingués, récupération par connecteur ≠ vérification. |
| `references/company-profile-template.md` | Copie embarquée de modèle partagé, non spécifique à l’apprenant. | Conserver identique à la racine ; pas de profil d’entreprise obligatoire pour étudier (ETU-020). |
| `references/dashboard-template.md` | Copie embarquée d’un modèle de visualisation partagé. | Conserver identique ; aucune note/couleur ou statistique ne mesure une réussite future. |
| `references/isolation.md` | Contrat BASE-008 lu par les treize entrées ; racine active du fork, paquet en lecture seule et helper obligatoire. | Conserver byte pour byte ; contrat d’apprentissage ETU-021 respecte cette frontière, pas de copie d’origine ou répertoire courant en secours. |
| `references/shared/research-citation-method.md` | Copie versionnée BASE-005, 1.0.0 ; sa présence ne prouve pas son chargement effectif par une entrée héritée. | Conserver identique ; chaque entrée adaptée charge explicitement la méthode et ses références métier locales, sans chemin vers la racine du dépôt. |
| `scripts/judge_store.py` | Helper BASE-008 embarqué pour profil/état isolés. | Conserver identique ; ETU-014/021 l’utilisent sans créer un second moteur de stockage. |

## Dépendances de contenu et frontières

- Les plans, cartes, règles de correction, journaux et grilles sont principalement
  des modèles **inline** dans les skills. Aucun study-plan.yaml, session-history.yaml,
  jeu de cartes, learning tracker ou registre de notes n’est livré comme état utilisateur.
  Les futures références métier listées dans les suites sont à créer, pas disponibles.
- Graphe hérité : interview → profil puis questions bar ; session → feuilles puis
  écriture ; feuilles → plan ou journal ; forecast → plan, fiches, cartes, IRAC.
  ETU-014 possède le bilan unique, ETU-016 retire les poids des consommateurs,
  ETU-021 possède contexte/versions et frontières ; pas trois journaux concurrents.
- Les sources d’exercice, cours, annales, corrigés commerciaux et notes personnelles
  exigent un périmètre d’usage réel. Détenir un fichier ne prouve ni permission
  de le diffuser/réutiliser ni permission d’utiliser une IA pendant l’évaluation.
  Aucune collecte automatique de tous les cours ou résultats d’une cohorte.
- Consigne → méthode → tentative → retour ne constitue pas vérification du droit.
  ETU-017 vérifie un point daté à part ; note sur dossier fermé et cours historique
  conservent leur corpus. Une source fournie, récente ou « confident » ne suffit pas.
- Aucun agent/cookbook law-student ou moteur CRFPA n’existe dans ce dépôt.
  Intégrations déclarées facultatives : scénario utile sur pièces fournies et
  limites réelles si elles sont absentes. Pas de dépendance à PISTE ni abonnement
  déduit ; BASE-010 est une méthode de maintenance, pas un outil runtime installé.
- Litige avec l’établissement : DOM-027 ; dossier réel de clinique : EXIST-009 ;
  conseil de fond : domaine concerné. Une décision réelle est un support d’étude,
  pas automatiquement une demande de consultation. Aucun relais proposé ne rend
  un skill non adapté déjà utilisable pour cette tâche.

Le [découpage](exist-010-decoupage-formation.md) attribue les vingt-et-une tâches,
leurs fichiers et leurs dépendances ; les [contrôles](exist-010-controles.py)
comparent cet inventaire à tous les fichiers réellement présents et repèrent les
hypothèses héritées avec leurs lignes, sans valider les règles juridiques.
