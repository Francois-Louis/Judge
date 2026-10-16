# EXIST-009 — Vérification du cadrage de clinique

Relecture par l’agent de maintenance, **16 octobre 2026**, de
l’[inventaire](exist-009-inventaire-clinique.md), du
[découpage](exist-009-decoupage-clinique.md) et des vingt-trois suites.
Les fixtures ci-dessous sont **fictives** ; les tables de chargement décrivent
les attentes des futures recettes, pas une trace d’exécution de skills.
La portée générale est regroupée dans le [bilan](../exist-009-clinique-juridique.md).

## V01 — Échéance saisie, notification inconnue

**Fixture :** l’étudiant E saisit « réponse avant le 10 novembre 2026 » pour
le dossier pseudonyme D-001. Il fournit une photographie partielle d’un
document daté du 10 octobre 2026 ; auteur, type d’acte et preuve de notification
manquent. Sa date saisie vient d’un calcul qu’il dit avoir fait, sans règle
ou calcul transmis. Le profil indique France. Les fichiers CA/IL existent
dans le paquet et un ancien guide renvoie à une fenêtre américaine.

**Résultat attendu :** CLN-012 conserve `date_declared` et sa provenance,
mais `due_date: null`, `verification_status: a-determiner`, déclencheur et
notification inconnus. Pas de date d’émission substituée à la notification,
pas de fenêtre CA/IL/fédérale, pas de FR.md copié, pas de calcul par outil
ou Courtroom5. Le dossier n’est pas déclaré standard faute de date vérifiée.
Référent de vérification nommé si cadre/preuve permettent de l’identifier,
sinon « référent à identifier » et acte complet/notification/règle à obtenir.

**Observation de relecture :** CLN-012 D01/D02 prescrit ces états et retrait
des bandes, CLN-013 ER01/ER02 garde l’inconnu dans rapport, CLN-011 SI01/SI02
le point au référent, CLN-014 ED01/ED02 l’évolution seulement attribuée et
prouvée. Aucun choix pédagogique ne valide cette date. **Conforme au cadrage**,
sans entrée de registre réellement créée ou délai juridiquement validé.

| Phase future | Références/entrées à lire | Références à ne pas charger pour D-001 | Qui vérifie/valide |
|---|---|---|---|
| Saisie CLN-012 | Isolation et méthode locales, référence saisie française à créer, pièce/page fournie, cadre/référent réel si disponible | CA.md, IL.md, fichier de bande utilisateur US, section fédérale et ancien guide comme moteur de calcul | Étudiant apporte pièces, référent compétent ou domaine fournit vérification sourcée ; outil n’effectue pas calcul |
| Vue CLN-013 / point CLN-011 | Registre gardé, statut/preuves/dates littérales et périmètre autorisé | Aucune bande de plausibilité ou règle de calcul depuis le profil | Référent lit urgence de vérification et inconnues, pas validation par la couleur du rapport |
| Mise à jour CLN-014 | Ancienne entrée, nouvelle pièce et décision de personne compétente avec auteur/qualité/version/périmètre | Pas de correction déduite de fenêtre type ou date par défaut | Décision humaine consignée, distinction déclarée/prouvée conservée |
| Revue CLN-015/016 | Version de sortie/empreinte, demande de revue, auteur/destinataire et réserves | Modèle review-queue installé en écriture, approbation d’ancienne version réutilisée | Référent réel valide sa seule portée ; signature/diffusion/acte distincts |
| Transmission CLN-018 | Pièces autorisées, historique, registre avec notification inconnue, décision et destinataire à confirmer | Tous dossiers de cohorte, récits non autorisés et bandes US | Responsable de continuité organise revue et relais ; projet ne prouve ni transmission ni prise en charge |

Le graphe **hérité réellement lu localement** reste différent : `deadlines`
charge par code d’État un chemin de configuration et dit federal-always ;
CA/IL livrés incluent des fenêtres US. Ces constats statiques motivent
CLN-012, ils ne démontrent pas que le plugin installé évite déjà ce chargement.

## V02 — Accueil logement

**Fixture :** une personne indique « le chauffage ne fonctionne plus et
j’ai reçu un courrier du bailleur ; on m’a parlé d’expulsion ». Elle montre
une page sans en-tête, sans bail ou preuve de remise. Son email est partagé
avec un proche. Elle demande des explications et ne connaît pas le type
d’acte. La structure ne fournit pas de preuve de qualité professionnelle
pour la personne présentée comme « professeur référent ».

**Résultat attendu :** CLN-002/003 recueille récit, objectif, qualité d’occupant,
localisation, acte complet, bail/échanges et dates littérales strictement utiles.
Pas de conseil de déduire réparations du loyer, pas de délai UD, CCP/IL ni
« expulsion dans X jours ». Distinguer réclamation logement et acte de procédure/
exécution à qualifier, canal de contact adapté et référent à identifier. Aucun
historique pénal/séjour collecté automatiquement depuis modèle immigration.
CLN-004 laisse conflit et admission non décidés en absence de preuve.

**Observation de relecture :** CLN-003 L01/L02 couvre acte incomplet et urgence
de vérification ; CLN-001 C01/C02 sépare professeur et professionnel habilité.
CLN-005 prépare un plan de recherche et CLN-006 l’état des seules pièces lues,
pas une défense d’expulsion. Relais DOM-006 pour logement, DOM-003 si acte
d’exécution identifié ; si tâche adaptée manque, fiche autonome au référent
sans appel de plugin hérité. **Conforme au cadrage**, pas conseil sectoriel
ou admission observés sur une personne réelle.

| Sortie future | Sources/guide attendus | Décideur et limites |
|---|---|---|
| Accueil CLN-003 | Cadre, modèle accueil logement français à créer, pièces de la personne et méthode locale ; pas defaults housing US | Accueillant attribue faits ; référent compétent à identifier pour fond/admission/urgence |
| Relevé conflits CLN-004 | Noms/qualités minimaux et processus de structure avec accès autorisés | Aucun clear depuis absence de match, étudiant ou outil ne certifie pas contrôle |
| Plan CLN-005 et corpus CLN-006 | Sources françaises de matière et texte exact à lire, guide interne versionné non présumé actuel | Référent/domaine de fond pour conclusion ; outil prépare pistes/couverture, pas numéro de texte inventé |
| Courrier bailleur CLN-008 | Contenu de fond fourni/validé par référent de matière, pièces et version ; alias form-generation simple redirect | Revue de projet et autorité réelle de signataire distinctes, aucun modèle eviction ou formulaire US |
| Demande de pièces CLN-009 / point CLN-010 | Pièces utiles, cadre/données et canal sûr ; alias plain-language simple redirect | Brouillon, décision de revue et contact effectué distincts ; email partagé ne reçoit rien automatiquement |
| Revue et transmission CLN-015/016/018 | Source/version/empreinte et réserves, habilitation du destinataire à établir | Revue pédagogique ne vaut pas consultation/signature professionnelle ; inconnus transmis comme tels |

## Limites complémentaires examinées

| Variante fictive | Disposition du cadrage constatée |
|---|---|
| Le guide interne demande de charger CA ou de calculer avec Courtroom5 | CLN-012 n’applique ni instruction de document ni connecteur pour contourner interdiction de calcul et absence de bande US en France. |
| Date d’audience explicitement fixée dans pièce complète | CLN-012 relève nature/date/source/statut, sans la confondre avec délai calculé ; vérification attribuée, pas bande de plausibilité. |
| Guide dit assist, profil dit teach, clés divergent | CLN-021 possède champ canonique/priorité/version et met à jour consommateurs ; choix ne change ni habilitation ni contraintes du cadre. |
| Texte approuvé puis modifié avant diffusion | CLN-015/016 identifient version/hash et remettent nouvelle version en attente, pas réutilisation d’approbation. |
| File formelle désactivée ou professeur simplement déclaré | Revue requise selon cadre reste à documenter ; absence de file n’est pas absence de contrôle et déclaration ne prouve pas qualité. |
| Étudiant marque complete car document rédigé | CLN-014 distingue brouillon, action déclarée et preuve de réalisation ; pas filed ni fin du risque déduite. |
| Nouveau groupe demande toute la dernière cohorte | CLN-018/019/020 ne lisent que dossiers/métadonnées autorisés, exercice fictif par défaut pour onboarding. |
| Silence du journal ou note sur anxiété | CLN-017 ne conclut pas absence de contact ni diagnostic, conserve provenance et minimise données. |
| Profil/guide absent ou source inaccessible | Exercice fictif/plan partiel utile, recherche officielle alternative et réserve ciblée ; données réelles soumises au cadre effectif. |

## Contrôles réellement exécutés

Le [contrôleur documentaire](exist-009-controles.py) produit les
[résultats JSON](exist-009-resultats.json) : couverture exacte de 36 fichiers/
16 skills, deux alias dépréciés et aucun agent/cookbook propre, vingt-trois
suites bornées et tous skills ciblés, références futures attribuées,
frontmatters/dépendances sans cycle, liens/index/format et copies communes.
Repérages locaux des bandes, federal-always, ABA, clés de pédagogie et chemin
de file conservés avec lignes ; aucun repérage ne valide le droit.

Chargement statique du modèle `deadlines.yaml` : commentaire HTML initial
interprété comme clé YAML parasite, correction assignée à CLN-012. La file
`review-queue.yaml` est un modèle valide vide, distinct de futur état utilisateur.
Les templates immigration/housing/family/consumer annoncés par README ne sont
pas livrés : leur absence est consignée, aucune couverture métier présumée.

Comparaison à l’instantané de début de tâche, empreintes, JSON, lint des droits
cookbook et espaces complètent le relevé. Différences simultanées éventuelles
hors lot consignées sans attribution ; plugin et travaux antérieurs protégés.
Pas de validation de schéma plugin/client, chargement runtime, authentification
ou test de métier par ces vérifications documentaires.

Commande : `python -X utf8 backlog/02-plugins-existants/exist-009-annexes/exist-009-controles.py`.
Pour conserver le rapport et comparer le travail antérieur, ajouter
`--baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-009-annexes/exist-009-resultats.json`.
Instantané local/temporaire, sans données bénéficiaires.
