# EXIST-008 — Découpage de la propriété intellectuelle

Propositions du **16 octobre 2026**, issues de l’[inventaire exhaustif](exist-008-inventaire-pi.md).
Les 31 PI restent `proposee`. La [relecture du cadrage](exist-008-verification.md)
porte sur nom de marque en France, invention de salarié et retrait de contenu
fictifs. Aucun droit, titre, recherche externe ou délai réel n’est validé ici.

## Contrat commun et première tranche proposée

Chaque suite dépend d’EXIST-008, PILOTE-003, BASE-005 et BASE-006. Le bilan
PILOTE-003 est terminé après BASE-011 : préalable satisfait, sans sélection
d’extension. Les limites H01 complet et lecteur indépendant restent consignées.

**Première tranche proposée : PI-001**, qualification d’une demande depuis
récit/document, sans profil professionnel. Sortie : objet/droit allégué, qualité
des acteurs, pays/actes/dates, pièces manquantes et prochaine question utile.
Aucune disponibilité de marque, brevetabilité, titularité ou procédure de
retrait ne découle de cette orientation ; les tâches suivantes restent des
choix explicites et non des appels automatiques.

Les dépendances métier désignent des contrats d’entrée ; une fiche équivalente
manuelle peut être utilisée avec contrôle de provenance/manques, sans exécution
préalable ou installation d’un autre plugin. Préférences et dossiers ne bloquent
pas la lecture ponctuelle conversationnelle. Chaque tranche corrige ses propres
gates/annonces et charge méthode BASE-005 1.0.0, références métier locales et
stockage BASE-008 ; profil durable absent soumis à entretien neuf.

## Stories et résultats bornés

| Story | Résultat | Dépendances métier |
|---|---|---|
| [PI-001](../suites/pi-001-qualifier-demande.md) | Qualifier une demande de propriété intellectuelle | Aucune |
| [PI-002](../suites/pi-002-recherche-nom-france.md) | Préparer une recherche préliminaire de marque pour la France | PI-001 |
| [PI-003](../suites/pi-003-fiche-invention.md) | Constituer une fiche factuelle d’invention | Aucune |
| [PI-004](../suites/pi-004-invention-salarie.md) | Qualifier une invention de salarié en France | PI-003 |
| [PI-005](../suites/pi-005-dossier-brevetabilite.md) | Préparer l’examen de brevetabilité d’une invention | PI-003 |
| [PI-006](../suites/pi-006-rapprochement-brevet.md) | Rapprocher une caractéristique et une revendication pour la France | PI-001 |
| [PI-007](../suites/pi-007-chaine-droits-photo.md) | Documenter la chaîne de droits d’une photographie | Aucune |
| [PI-008](../suites/pi-008-logiciel-salarie.md) | Qualifier les droits sur un logiciel créé par un salarié | Aucune |
| [PI-009](../suites/pi-009-cession-photo.md) | Examiner une cession de droits sur une photographie | Aucune |
| [PI-010](../suites/pi-010-licence-photo.md) | Examiner une licence d’utilisation de photographie | Aucune |
| [PI-011](../suites/pi-011-licence-dependance.md) | Examiner la licence d’une dépendance logicielle | Aucune |
| [PI-012](../suites/pi-012-livraison-logiciel.md) | Préparer les obligations d’une livraison logicielle bornée | PI-011 |
| [PI-013](../suites/pi-013-courrier-pi-recu.md) | Lire une lettre d’assertion de droits PI reçue | PI-001 |
| [PI-014](../suites/pi-014-usage-marque.md) | Examiner un usage contesté d’une marque pour la France | PI-001 |
| [PI-015](../suites/pi-015-projet-lettre-marque.md) | Préparer une lettre sur un usage de marque en France | PI-014 |
| [PI-016](../suites/pi-016-qualifier-retrait.md) | Qualifier une demande ou décision de retrait de contenu | PI-001 |
| [PI-017](../suites/pi-017-signalement-photo.md) | Préparer un signalement de reprise de photographie | PI-007, PI-016 |
| [PI-018](../suites/pi-018-notification-retrait-recue.md) | Lire une notification de retrait de contenu | PI-016 |
| [PI-019](../suites/pi-019-incident-secret-affaires.md) | Documenter un incident allégué de secret des affaires | Aucune |
| [PI-020](../suites/pi-020-fiche-actif.md) | Enregistrer les faits d’un actif PI | Aucune |
| [PI-021](../suites/pi-021-echeance-marque-france.md) | Documenter une échéance de renouvellement de marque française | PI-020 |
| [PI-022](../suites/pi-022-etat-portefeuille.md) | Présenter un portefeuille PI délimité | PI-020 |
| [PI-023](../suites/pi-023-preferences-pi.md) | Gérer des préférences PI volontaires | Aucune |
| [PI-024](../suites/pi-024-dossier-pi.md) | Isoler un dossier PI | Aucune |
| [PI-025](../suites/pi-025-agent-rapport-pi.md) | Adapter l’agent à un rapport PI local | PI-020, PI-021, PI-022 |
| [PI-026](../suites/pi-026-contrat-edition-production.md) | Lire un contrat d'édition ou de production proposé à un auteur | PI-001 |
| [PI-027](../suites/pi-027-gestion-collective.md) | Comprendre l'adhésion et les relevés d'une société de gestion collective | PI-001 |
| [PI-028](../suites/pi-028-reprise-oeuvre.md) | Documenter la reprise d'un texte, d'une musique ou d'une œuvre plastique | PI-001 |
| [PI-029](../suites/pi-029-droit-moral.md) | Faire valoir le droit moral d'un auteur | PI-001 |
| [PI-030](../suites/pi-030-dessins-modeles.md) | Qualifier la protection d'un dessin ou modèle et documenter une copie alléguée | PI-001 |
| [PI-031](../suites/pi-031-droits-campagne-synthetique.md) | Documenter les droits d’un visuel publicitaire synthétique | Aucune |

PI-025 attend adaptation et recette manuelles PI-020/021/022 ; aucun cookbook
propre au plugin n’est livré ou créé dans ce découpage. Les tranches restent
bornées à une photo, une dépendance/version, une livraison, un titre ou une
activité déterminés ; elles ne promettent pas adaptation du domaine entier.

## Contrats de contenu

| Chaîne | Propriétaire du résultat et limite |
|---|---|
| Demande → signe → recherche | PI-001 qualifie objet/acteur/territoire ; PI-002 possède protocole de recherche, requêtes, registres, date, résultats et exclusions. Signe distinctif, antériorité, domaine libre, dépôt possible et usage licite restent questions distinctes. |
| Invention → emploi → examen → exploitation | PI-003 possède contributions/divulgations/chronologie ; PI-004 fiche salarié/mission/moyens/qualités ; PI-005 dossier d’examen et références connues ; PI-006 tableau d’une revendication et caractéristique. Être brevetable ne prouve pas titulaire ou liberté d’exploiter ; titre délivré ne prouve pas toute validité/portée actuelle. |
| Œuvre → chaîne → contrat | PI-007 possède chaîne de droits photo et preuves ; PI-008 logiciel de salarié distinct ; PI-009 portée d’une cession indépendante et PI-010 licence d’utilisation. Rémunération/paiement, support, transfert de droits, droits moraux et autorité du signataire ne sont pas un seul champ ownership. |
| Logiciel → licences → livraison | PI-011 possède paquet/version/texte/exception/options et montage ; PI-012 checklist d’une livraison et preuves d’exécution. SPDX/README ne remplacent pas l’octroi réel ; licence inconnue, architecture inconnue et transitifs non lus restent visibles. |
| Usage → lettre → plateforme | PI-013 lit courrier, PI-014 examine usage marque, PI-015 rédige un projet borné. PI-016 qualifie droit/canal/régime ; PI-017 projet photo ; PI-018 décision reçue. Chacun conserve brouillon/envoyé/reçu/exécuté distincts ; pas lettre + retrait simultanés imposés. |
| Secret | PI-019 possède périmètre information/mesures/actes/preuves et critères à instruire, sans extraction intrusive ni accusation déduite du départ d’un salarié. |
| Actifs → dates → rapport | PI-020 possède données et schéma du registre, PI-021 fiche d’une échéance nationale marque française, PI-022 rapport. Responsable externe déclaré n’est pas vérification, date passée n’est pas perte de droit certaine. PI-025 reprend seulement ces contrats livrés. |
| Préférences et espaces | PI-023 possède préférences volontaires ; PI-024 espace/actif autorisé et identifiant lié à registre, sans second actif implicite ou droit de lecture croisée. Classe, appétence ou dossier ne valent ni titre ni règle. |

Chaque futur résultat conserve identifiant/objet/version, acteur/qualité,
territoire/actes et date de référence, pièces/passages/sources réellement lus,
statut déclaré/vérifié/réservé, couverture/exclusions et prochaine pièce utile.
Le modèle `portfolio.yaml` et les grilles inline sont hérités ; ils ne sont ni
un registre utilisateur livré ni un corpus de droit français vérifié.

## Choisir les recherches selon titre, territoire et tâche

**Pistes de recherche future**, non consultations effectuées dans EXIST-008.
Les autorités et juridictions utiles ne sont pas toutes obligatoires à chaque
tâche ; vérifier champ et compétence au moment du lot.

| Objet et tâche | Faits/pièces déterminants | Sources à rechercher, seulement si pertinentes |
|---|---|---|
| Nom de marque destiné à France | Signe/variantes, produits/services réellement visés et libellés, public, pays/actes, usage et droits connus | CPI et INPI ; EUIPO pour titres UE et OMPI/registres des désignations internationales lorsqu’effets pertinents en France. Antériorités non limitées au seul numéro de classe ou domaine. Requêtes exactes/approchées et exclusions documentées. |
| Marque UE ou procédure sur un titre | Type/numéro/statut et territoire, usage/dépôt/opposition/nullité/recours allégués, parties/stade | Règlement marque UE sur EUR-Lex, EUIPO et jurisprudence primaire ; compétence INPI, EUIPO, juridictions nationales ou UE à qualifier selon procédure exacte, pas office unique pour toutes questions. |
| Invention et brevet français/voie européenne | Inventeurs/contributions, divulgation et contenu prouvés, demande/titre/version des revendications, pays/actes/voie | CPI et INPI pour voie française ; CBE et OEB pour voie européenne. Espacenet/famille/résumé ne remplace pas titre/revendication et preuve d’effet territorial. Refus d’un accès ne justifie pas une date ou référence inventée. |
| Titre européen, effet unitaire ou contentieux brevet | États et effets, validation/statut/annuités, amendements, option/opt-out allégué et procédure/stade | Registres et textes pertinents OEB/INPI/nationaux, textes UE et accord/règles JUB lorsque question le justifie ; juridiction nationale ou JUB à rechercher selon titre/territoire/procédure. L’OEB ne devient pas le juge général de toute atteinte. |
| Œuvre/photo, salarié logiciel, cession ou licence | Auteur/contributions, original/versions, qualité/statut, mission/instructions, contrats/accords, droits/usages/durée/pays | CPI et textes propres à chaque objet/qualité, règles UE et jurisprudence du point précis, contrats/cessions/licences réellement accordés. Pas de registre INPI/EUIPO/OEB imposé pour toute photographie. |
| Invention de salarié | Emploi réel/régime privé public, mission/fonctions/moyens, employeurs/pays/dates, déclarations et accords collectifs | CPI et textes d’application spécifiques, pièces de travail et accords réellement applicables ; travail garde statut/rémunération/rupture, PI garde classification/invention/droits à instruire. Pas work-for-hire ni régime logiciel importés. |
| Licence OSS/version et livraison | Fichiers LICENSE/NOTICE/en-têtes, choix de double licence/exception, modification, liaison, destinataires/réseau, version du binaire | Textes officiels de licence/version et octroi réel sur fichiers, CPI/droit applicable pour point de qualification. Aucune recherche INPI/EUIPO/OEB obligatoire par principe. Compatibilité et obligations ne se décident pas depuis label et couleur. |
| Retrait/photo et décision reçue | Auteur/chaîne, URL exactes, reproduction/usage/licence ou exception alléguée, service/rôle, pays, motif et acte de notification | CPI, textes UE/France du mécanisme retenu dont DSA et textes nationaux selon champ, modalités officielles actuelles du service ; voies et conditions propres à cet acte. La localisation seule ne détermine pas régime ; portail non testé reste non testé. |
| Échéance du portefeuille | Type national/UE/international, dépôt/renouvellement et source, événement/décision/preuve, état et date de référence | Texte/version et registre/modalités de l’office pertinent. Première tranche PI-021 limitée à marque nationale française ; autres dates et titres demandent tranche propre, pas table mondiale. |

Temporalité : version applicable aux faits/contrats/dépôts/notifications,
modifications/rectificatifs/transitions et date réelle de lecture. Une échéance
calculée exige nature, source/passage, déclencheur prouvé, méthode reproductible,
exceptions et contrôle attribué ; sinon `a-determiner`. Déclaré/lu/vérifié,
calculé/fixé/interne, demandé/déposé/payé/accepté restent distincts. Aucun barème,
délai de grâce ou calendrier universel n’est figé ici.

## Traitement des hypothèses étrangères

| Hypothèse et emplacement hérités | Décision pour futur parcours France/UE | Si rattachement étranger établi |
|---|---|---|
| USPTO/TESS/TTAB, classes/first use, §8/§9/§15 et maintenance 3.5/7.5/11.5 ; clearance, portfolio, agent et setup | Retirer defaults et calculs de la branche française ; identifier titre, office, effets, date/statut, preuves et corpus non consultés | Documenter pays/titre/acte/procédure concernés et choisir sources officielles étrangères exactes dans tranche bornée distincte, sans les appliquer au portefeuille entier. |
| §101/Alice/Mayo, §102/grâce un an, §103, US willfulness/§271/§284 ; invention-intake, fto-triage et infringement-triage | Retirer verdicts et délais importés ; distinction factuelle, classification salarié, examen brevetabilité et comparaison d’un titre séparés | Recherche propre à ce droit/dates/titre avec spécialiste si hors tranche ; jamais perte certaine de droits ou lancement autorisé depuis résumé. |
| DMCA §512(c)/(g), perjury, consentement fédéral, 10–14 jours ; takedown, cease-desist et profil | Ne pas traduire en notification/recours UE ; qualifier acteur/régime/canal avant tout projet, pas contre-notice automatique | Avis réel complet, rôle/service, rattachements et conséquences à analyser avec sources US actuelles ; aucune compétence déduite du simple siège de plateforme et pas rédaction US livrée par ces suites. |
| Fair use, Lenz, common-law copyright et enregistrement US ; takedown/infringement/clearance | Ne pas appliquer les quatre facteurs ou prérequis d’enregistrement à toute œuvre française. Autorisation/exception pertinente à rechercher sur faits et droit qualifiés | Rechercher régime exact de l’usage dans pays concerné ; pas principe « internet = fair use » ni défense ou atteinte automatique. |
| Work-for-hire, hereby assigns, waiver moral et patent agent-client privilege ; ip-clause-review, profil/setup | Retirer solutions universelles ; objet, qualité, droits/conditions, mission et contrat déterminent la recherche. Confidentialité non garantie par en-tête | Analyse distincte du droit/contrat/qualité réellement concernés ; pas extension du statut USPTO au CPI ou à toute mission. |
| Lanham/DTSA/UTSA, DJ/Rule 11/statutory damages, design patent D/PP/RE et claim chart US | Retirer comme moteurs de qualification française, sanctions ou preuve ; dessins/modèles/obtention/validité détaillée restent à recadrer | Tranche étrangère ou spécialisée explicite, titres et procédures exacts, sans prétendre équivalence de nom. |

Ces décisions viennent de la lecture des fichiers locaux. Aucun standard
étranger cité dans ce tableau n’a été vérifié juridiquement ici.

## Frontières et autonomie

PI garde droit/titre, chaîne et projet propres à l’objet. Commercial garde
contrat B2B général, travail statut/contrat/rémunération et rupture, privacy
collecte/partage de données, IA rôle/usage d’outil et produit lancement/allégations.
Apport d’IA ne prouve ni originalité ni absence de droit ; seule question
déterminante est transmise au domaine avec pièces et réserves.

Suspension de compte sans droit PI → DOM-034 ; procédure identifiée ou acte
d’exécution → contentieux/administratif/exécution selon acte. Le tableau
brevets de `litigation-legal:claim-chart` reste hérité ; CTX-012 ne propose
qu’une matrice contractuelle B2B. PI-006 fonctionne sans ce plugin et ne
prétend pas livrer une contrefaçon brevet/JUB ; fiche manuelle au spécialiste.

Dessins/modèles (hors PI-030, ajoutée le 16 octobre 2026), obtentions végétales, certificats complémentaires, contentieux
de validité/opposition/dépôt, domaines et régimes publics/étrangers non bornés
demandent cadrages propres avant implémentation. Leur retrait des branches
US par défaut n’annonce pas un traitement France/UE de remplacement.

Chaque paquet fournit seul références, méthode et limites ; un relais non
adapté donne une fiche autonome sans exécuter le skill hérité. BASE-010 offre
voies officielles alternatives de maintenance sans abonnement requis, mais
ni outil du checkout ni corpus complet ne sont des dépendances runtime.

Aucun dépôt, signature, paiement, publication, retrait effectif, message,
compte connecté, planification de veille ou déploiement n’est réalisé ici.

## Complément publicités synthétiques — 16 octobre 2026

[PI-031](../suites/pi-031-droits-campagne-synthetique.md), issue de la [matrice marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), documente les droits d’un visuel ou d’une séquence synthétiques/retouchés. Licence du générateur, droits sur les sources, protection éventuelle de la sortie et image/voix ne sont pas fusionnés. PI-007/009/010 gardent la photographie ; DOM-035/043 gardent le litige de personnalité/expression à qualifier. IA-005 et PDT-009 gardent les mentions. Les 31 PI restent proposées ; les preuves historiques ne sont pas recalculées.
