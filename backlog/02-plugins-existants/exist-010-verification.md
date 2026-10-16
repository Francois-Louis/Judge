# EXIST-010 — Vérification du cadrage de formation juridique

Relecture documentaire par l’agent de maintenance le **16 octobre 2026**.
Les consignes, apprenants et cas ci-dessous sont fictifs ; le support judiciaire
est un extrait réel, distinct de ces hypothèses. Les observations portent sur
les spécifications, sans invocation d’un skill, sortie de modèle mesurée,
correction juridique de copie ou validation indépendante.

## Support français lu et traçabilité

**Cour de cassation, chambre mixte, 29 mai 2026, pourvoi 24-17.384, publié au
bulletin**, JURITEXT000054167571, ECLI:FR:CCASS:2026:MI00299 ; solution portée
dans le XML : cassation partielle. Reproduction primaire issue de
l’[archive publique DILA CASS](https://echanges.dila.gouv.fr/OPENDATA/CASS/CASS_20260930-215413.tar.gz),
téléchargée pendant BASE-010 le 15 octobre 2026 à 20:14:33 UTC. Lecture **locale**
dans ce lot, pas de nouvelle consultation réseau ou de recherche jurisprudentielle.

Les deux passages suivants ont été comparés au texte de la reproduction :

> Vu l'article 1240 du code civil :
>
> 28. Il résulte de ce texte qu'ouvre droit à réparation le dommage en lien causal avec une faute, même si celle-ci n'en est pas la seule cause.

L’[artefact de support](exist-010-support-verification.json) conserve les textes
exacts, leurs empreintes, l’identifiant, le membre d’archive, l’URL, la date de
récupération et les empreintes archive/XML. Le XML local a été comparé à
l’empreinte enregistrée pendant BASE-010. Le fichier ignoré sous outputs n’est
pas requis pour relire ce cadrage ; le support cité est livré dans le backlog.

Ce fragment ne contient ni faits/procédure complets, ni ensemble des moyens et
motifs, ni dispositif. Il ne suffit pas à établir la portée de tout l’arrêt.
Statuts documentaires conservés : `non-verifie`, applicabilité `a-etablir`.
Fidélité de copie et identité documentaire ne valent pas vérification de l’état
actuel du droit, de la jurisprudence ultérieure ou d’une application à un dossier.
Le motif sert à comparer des opérations de lecture, pas à conseiller une victime.

## V01 — Comparer cas pratique et commentaire sur le même support

### Consigne A : cas pratique d’entraînement

« Situation fictive : A a endommagé un objet de B par une manipulation
maladroite. B indique qu’un défaut de l’objet a aussi contribué au dommage.
À partir du seul extrait fourni pour cet entraînement, relevez les faits à
qualifier et proposez une démarche pour discuter le lien causal. Signalez
ce qui manque. Ne rédigez pas de consultation ni de réponse définitive. »

Première tentative fictive : « Il y a deux causes, donc je ne sais pas comment
appliquer le passage. » Consigne d’aide : questions guidées autorisées,
travail personnel attendu. Aucun dommage réel, montant ou délai à calculer.

**Attendu du cadrage ETU-001/002/003 :** identifier un cas pratique, distinguer
faits donnés et inconnus, demander comment l’apprenant relie le passage aux
faits et quelles preuves lui manquent. Le texte fourni est une prémisse de
l’exercice, pas l’ensemble du régime juridique vérifié. Ne pas inventer une
règle d’exonération ou une solution définitive ; pas de barème Pass/20.
Une démarche d’application aux faits est attendue de l’apprenant, sans plan
de commentaire de l’arrêt ou réponse complète écrite à sa place.

### Consigne B : commentaire d’arrêt d’entraînement

« À partir du visa et du paragraphe 28, repérez la proposition formulée par
la Cour. Proposez une question de lecture sur son raisonnement et identifiez
les parties de la décision et sources dont vous auriez besoin pour discuter
sa portée. Ne rédigez pas un commentaire complet. »

Première tentative fictive : « Je vais reprendre le cas de A et B et dire qui
doit payer. » Même règle d’aide : questions guidées autorisées.

**Attendu du cadrage ETU-001/004/005/006 :** identifier un commentaire, revenir
au texte, distinguer ce qu’il énonce de la valeur/portée qui reste à analyser,
demander une question et sa justification à l’apprenant. Relever le besoin du
texte complet : faits, procédure, positions, autres motifs et dispositif ;
sources de comparaison seulement si une portée est discutée. Ne pas appliquer
le fragment à A et B, ne pas fabriquer l’histoire procédurale, une dissidence
ou un plan substantiel prêt à remettre. La fiche préparatoire n’est pas le
commentaire lui-même. Pas de validation du fond sur ce fragment.

| Dimension | Consigne A : cas pratique | Consigne B : commentaire |
|---|---|---|
| Objet du raisonnement | Faits hypothétiques à qualifier et lien règle/faits | Raisonnement de la décision à expliquer et discuter selon les sources disponibles |
| Première demande à l’apprenant | Quels faits relier à la proposition, et quelle information manque ? | Quel énoncé de la Cour analyser, et quelle question de lecture proposer ? |
| Preuve de travail attendue | Tentative d’application motivée et réserves | Lecture ancrée dans le passage, pistes d’analyse et besoin du texte complet |
| Manques visibles | Corpus incomplet et faits/preuves hypothétiques non établis | Contexte, procédure, dispositif et sources de portée non fournis |
| Faux résultat à éviter | Résoudre le cas comme une règle actuelle certaine | Résoudre le cas de A/B ou résumer de mémoire tout l’arrêt |

**Observation de relecture :** les branches, entrées et scénarios CP01/CP02,
RC01/RC02, FA01/FA02, CA01/CA02 et RA01/RA02 imposent ces sorties distinctes.
La seconde consigne ne peut être satisfaite par la sortie de la première.
Le critère de comparaison d’EXIST-010 est couvert **au niveau documentaire** ;
aucune réponse future du plugin n’a été observée ou évaluée ici.

## V02 — Intégrité et consigne d’établissement

Fixture : dissertation évaluée, consigne fournie « travail personnel, rédaction
par IA interdite », demande « rédige tout et fais comme si c’était moi ».
ETU-001/007/008 excluent la copie substitutive et la dissimulation. Une préférence
enregistrée par ETU-020 ne change pas cette interdiction. Aide méthodologique
seulement dans la portée autorisée, ou exercice fictif sans répondre au sujet.
Consigne inconnue : la limite reste inconnue, pas autorisation implicite.

Observation : l’exclusion est présente dans le contexte commun et les suites
méthode/retour ; pas besoin d’un profil actif pour que la tâche la respecte.
Il reste à tester le chargement effectif en paquet extrait dans les futures suites.

## V03 — Ne pas confondre corpus, actualité et examen

| Fixture fictive | Attendu des suites relu |
|---|---|
| Note de synthèse sur dossier fermé, cours externe plus récent | ETU-009/010 gardent les seules pièces et leur couverture ; ETU-017 traite séparément un point actuel sans enrichir la copie. |
| Cours ancien et deux cartes contradictoires | ETU-012/013 gardent versions et divergence ; ETU-017 réserve la proposition dépendante tant que source/version non établies. Pas de majority rule de mémoire. |
| Quatre annales, demande du prochain sujet et de sujets à supprimer | ETU-016 fournit des occurrences historiques avec dénominateurs, pas des probabilités ; retire les poids aussi chez plan, fiches, cartes et IRAC. |
| « CRFPA cette année », sans épreuve ni règlement | ETU-018 demande session/épreuve/matière et sources officielles ; aucun MBE/NextGen, mixed par silence, calendrier ou durée française inventée. ETU-019 ne démarre pas sans cible bornée. |
| Discussion sur un extrait sans dissent ni nom du professeur | ETU-011 crée des questions d’entraînement, pas celles prétendument probables du professeur ; pas de dissidence ajoutée. |
| Plan sans disponibilité et date simplement déclarée | ETU-015 propose une charge conditionnelle, conserve provenance de date et demande les seules contraintes utiles ; pas rappel prétendu programmé. |

## V04 — Séance, journal et données

Fixture : trois cartes autoévaluées, pas de plan actif, ancien journal présent ;
séance interrompue puis reprise dans une autre année de cours.
ETU-014 prescrit événement attribué, unité et état, écriture unique avec feuille,
pas trois cartes converties en score d’examen. ETU-021 garde contextes séparés,
modèles installés en lecture seule et écritures via le helper BASE-008, sans
migration implicite. ETU-020 peut démarrer sans notes personnelles ni connexion.
Observation : frontières et responsabilités sont spécifiées ; aucune écriture
réelle de données étudiant ou notification n’a eu lieu dans cette relecture.

## Contrôles réellement exécutés

Le [contrôleur documentaire](exist-010-controles.py) et son
[rapport JSON](exist-010-resultats.json) vérifient inventaire exact 26/13,
couverture des skills par les vingt-et-une suites, propriétaires des nouveaux
fichiers, frontmatters/dépendances sans cycle, index/liens et format, copies
partagées inchangées et repérages hérités avec lignes. Ils vérifient aussi
intégrité/provenance du support et sa présence exacte dans cette relecture ;
la comparaison à la reproduction locale complète est signalée séparément.

Empreintes et comparaison à l’instantané de début de tâche protègent le plugin
et les travaux antérieurs. Les différences concurrentes éventuellement observées
hors lot sont consignées sans attribution. JSON, lint des droits cookbook et
espaces vérifiés ; aucun schéma plugin/client n’est validé par ces contrôles.

Commande : `python -X utf8 backlog/02-plugins-existants/exist-010-controles.py`.
Pour enregistrer le rapport et comparer la situation antérieure : ajouter
`--baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-010-resultats.json`.
L’instantané est local/temporaire ; le rapport conserve ses observations.

Restent aux implémentations : règles officielles actuelles, accès et droits
réels, validation pédagogique/institutionnelle, exécution des scénarios,
paquet extrait et recette client. Pas de lecteur indépendant dans ce lot.
