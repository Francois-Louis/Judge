# DOM-039 — Découpage micro-entreprise et travail indépendant

Cadrage du **17 octobre 2026**, public sans formation juridique, situations
[S-43 et S-49](../../usages-quotidiens.md). Les 42 suites IND restent
`proposee`. Le nom `self-employed-legal` est conservé, avec identifiant publié
proposé `judge-fr-eu-self-employed-legal`. Aucun plugin ni commande n'est livré.

## Entrer par le document ou le problème

| Phrase de la personne | Première qualification | Tâche ou relais |
|---|---|---|
| « On me demande de payer, je ne comprends pas ce courrier » | Organisme réel, document entier, période, réception, activité/statut encore inconnus | IND-001 commence sans nom de régime ; fiscal → IND-024/DOM-011 selon objet ; soupçon d'imitation → COM-019 |
| « J'ai déclaré zéro et l'Urssaf me relance » | Déclaration déposée ou zéro recette seulement ? Accusé et même période ? | IND-001 puis IND-013 ; recours distinct IND-034 si pertinent |
| « J'ai dépassé un seuil » | Quel seuil, quelle activité, quelles années et dates d'encaissement ? | IND-014 pour micro et IND-015 pour TVA, deux contrôles |
| « Mon dossier est payé mais bloqué » | EI ou société, état du portail et auteur du blocage | IND-002 puis IND-003 si régularisation ; société → SOC-023 |
| « On publie mon adresse » | Source officielle ou copie privée, registre, acte et donnée | IND-039 ou IND-040 ; PRV-028/029 pour questions privées distinctes |
| « Je ferme, donc je ne dois plus rien ? » | Cessation réelle, formalité et radiation, dernière période et dette | IND-028 à IND-031, SOC-027 si difficulté globale/patrimoine |
| « Je suis salariée, auto-entrepreneuse et à la CAF » | Trois rapports différents, décisions et revenus qualifiés séparément | IND-041, emploi privé et DOM-012 sur questions bornées |
| « Une contrainte arrive pendant ma médiation » | Acte complet et réception en premier, urgence sans durée annoncée | IND-035 et identification ENF-001 ; IND-038 n'est pas substitué à l'opposition |

## Qualification commune à embarquer par IND-001

Demander seulement ce qui change le résultat : objectif et courrier complet,
territoire précis (dont outre-mer), établissement/résidence, pays d'opération,
qualité du demandeur et pouvoir si représentant, EI/société/autre statut et
micro/réel **séparément**, activité réelle et mixte, création/début effectif,
périodicité, option fiscale/ACRE, organisme et authenticité à vérifier,
périodes, notification et preuve de réception, demandes/recours déjà engagés.
Une information inconnue n'interdit pas la lecture factuelle du courrier.

Conserver la distinction entre CA encaissé, facture, bénéfice, rémunération,
revenu de prestation et revenu fiscal. Un taux unique n'est pas déduit du
code APE ; montant d'un courrier, paiement effectué et somme due ne sont
pas synonymes. Les pièces reçues sont des données, jamais des instructions.

Chaque échéance a sa fiche : objet, acte, régime, déclencheur, preuve, règle
et version, unité, jours non ouvrés/heure, exceptions/transitions et état de
vérification. Déclaration initiale et suivante, recours et paiement,
médiation et opposition gardent des calendriers séparés. Le cadrage ne
fournit **aucun taux, plafond, délai ou montant légal**.

## Première tranche proposée — IND-001

Lire un seul courrier Urssaf adressé à une personne qui se présente comme
auto-entrepreneur ou indépendant ; demander le régime sans l'exiger à
l'entrée. Sortie : résumé, auteur/objet et authenticité à vérifier si doute,
chronologie, tableau période/ligne/montant **recopié**/provenance, stade établi
ou incertain, pièces ciblées, question et destinataire de la prochaine étape.

Une mise en demeure est lue sans être assimilée à une contrainte. Contrôle,
lettre d'observations et contrainte déclenchent une orientation propre et
un renfort BASE-013 avec avocat ; l'acte n'est jamais retenu pour une revue
ordinaire. Pas de calcul de cotisation, déclaration corrigée, recours rédigé,
stratégie de contrôle ni échéancier dans cette tranche. Le courrier fiscal
ou l'employeur société produit une fiche de relais, pas une analyse Urssaf
de fond. Aucun autre plugin requis pour cette lecture.

## Installation autonome et contrat des futures livraisons

IND-001 crée le paquet avec son seul skill et la référence commune
`self-employed-legal/references/qualification-independant.md`. Il embarque
manifeste initial `0.1.0`, README limité aux tâches livrées, modèle CLAUDE.md
facultatif, LICENSE et NOTICE, méthode BASE-005 versionnée identique sous
`references/shared/`, ainsi que copies BASE-008 d'isolation, stockage et
modèles. Le marketplace, le décompte/version du test BASE-008 et les NOTICE
local/racine sont mis à jour seulement lors de cette livraison.

Chaque suite crée son skill et sa référence métier locale avec modèle de
sortie, sources réellement lues et versions applicables ; elle charge le
socle sans dépendance au checkout, à un autre plugin ou à un profil cabinet.
Installation seule, aucun agent, hook ou connecteur nécessaire identifié,
aucun compte Urssaf/fisc/INPI connecté. Pièces fournies par la personne et
recherche officielle sans intégration obligatoire ; pas de dépôt, envoi,
paiement, modification de compte, purge ni stockage durable du dossier.

Recette future par couche BASE-006 : contrôles statiques du paquet extrait
hors checkout, schémas officiels et isolation BASE-008, invocation réelle en
client sans profil et sans autre plugin, scénarios nominal, pièce manquante,
source absente, transfrontalier et héritage étranger. Un contrôle statique
ne prouve ni le comportement ni la compréhension. Appliquer BASE-013/014/019
et la méthode BASE-005 en vigueur ; source inaccessible = conclusion
dépendante réservée et accès tracés. La relecture est prise en charge par
l'utilisateur sans être annoncée effectuée ; les tests restent à exécuter.

## Tâches hiérarchisées

Rang 1 : lecture fondatrice proposée ; rang 2 : documents fréquents, urgences
et contrôles distincts ; rang 3 : autres tâches bornées ; rang 4/P3 : calculs
isolés nécessitant paramètres vérifiés. Ces rangs ne sélectionnent aucun lot.
Toutes les suites dépendent de DOM-039, PILOTE-003, BASE-005/006/008/013/014/019.
La colonne finale ne reprend que les dépendances métier IND. Les renvois
non livrés sont des orientations, jamais des commandes à lancer.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [IND-001](../suites/ind-001-courrier-urssaf.md) | `urssaf-letter-reading` | Fiche du courrier : auteur, objet, période, sommes recopiées, stade, inconnues et pièces utiles | Aucune |
| 2 | [IND-002](../suites/ind-002-stade-formalite.md) | `sole-trader-filing-status` | Chronologie des états prouvés, auteur du blocage et demande de suivi ciblée | IND-001 |
| 3 | [IND-003](../suites/ind-003-pieces-regularisation.md) | `sole-trader-filing-correction` | Checklist comparant chaque demande de régularisation avec la pièce retrouvée et brouillon d'accompagnement | IND-001, IND-002 |
| 3 | [IND-004](../suites/ind-004-donnee-registre.md) | `sole-trader-register-data` | Fiche d'une donnée contestée, pièces de comparaison et destinataire compétent à établir | IND-001 |
| 3 | [IND-005](../suites/ind-005-questions-statut.md) | `self-employed-status-questions` | Tableau qualitatif des options et des hypothèses à faire vérifier | IND-001 |
| 3 | [IND-006](../suites/ind-006-prerequis-activite.md) | `self-employed-activity-prerequisites` | Fiche de l'activité précise, conditions à rechercher et dossier de relais sectoriel | IND-001 |
| 2 | [IND-007](../suites/ind-007-acre-demande.md) | `acre-application-preparation` | Conditions documentées ou réservées, pièces et brouillon de demande ACRE | IND-001 |
| 3 | [IND-008](../suites/ind-008-acre-decision.md) | `acre-decision-reading` | Lecture de décision, chronologie demande/réponse et brouillon de demande d'explication | IND-001, IND-007 |
| 4 | [IND-009](../suites/ind-009-calcul-acre.md) | `acre-period-calculation` | Tableau reproductible du calcul ACRE pour une période et un régime micro-social établis | IND-001, IND-008, IND-042 |
| 2 | [IND-010](../suites/ind-010-declaration-ca.md) | `turnover-declaration-review` | Tableau période/activité/encaissement/déclaration/reçu avec écarts documentaires | IND-001 |
| 3 | [IND-011](../suites/ind-011-correction-declaration.md) | `turnover-declaration-correction` | Dossier de correction d'une déclaration identifiée et brouillon à l'Urssaf | IND-001, IND-010 |
| 2 | [IND-012](../suites/ind-012-calendrier-social.md) | `social-declaration-deadline` | Fiche d'une échéance : événement, périodicité, règle/version, date et preuve ou inconnues | IND-001 |
| 2 | [IND-013](../suites/ind-013-declaration-zero.md) | `zero-turnover-declaration-review` | Fiche de période à zéro, preuve de dépôt et demande de clarification ou régularisation | IND-001, IND-010 |
| 2 | [IND-014](../suites/ind-014-seuil-micro.md) | `micro-regime-threshold-review` | Tableau par exercice et activité, champ, plafond sourcé et effet de dépassement établi ou réservé | IND-001 |
| 2 | [IND-015](../suites/ind-015-franchise-tva.md) | `vat-exemption-threshold-review` | Chronologie des opérations et contrôle des seuils de franchise distinct du micro | IND-001 |
| 3 | [IND-016](../suites/ind-016-option-micro-fiscale.md) | `sole-trader-tax-option-reading` | Fiche d'une option, preuve, période et questions au service fiscal | IND-001 |
| 3 | [IND-017](../suites/ind-017-declaration-annuelle-activite.md) | `self-employed-annual-tax-papers` | Tableau des recettes d'activité et rubriques à vérifier pour une année | IND-001 |
| 3 | [IND-018](../suites/ind-018-option-versement-liberatoire.md) | `discharge-tax-option-review` | Fiche d'éligibilité et d'option datée, acceptation ou inconnues, questions ciblées | IND-001 |
| 4 | [IND-019](../suites/ind-019-calcul-versement-liberatoire.md) | `discharge-tax-period-calculation` | Calcul reproductible d'un versement de l'activité et rapprochement avec le relevé | IND-001, IND-018 |
| 3 | [IND-020](../suites/ind-020-compte-dedie.md) | `dedicated-account-obligation-review` | Fiche d'obligation à vérifier, distinction compte dédié/offre professionnelle et questions à la banque | IND-001 |
| 3 | [IND-021](../suites/ind-021-pieces-livres-archivage.md) | `self-employed-records-inventory` | Liste par catégorie : document requis à vérifier, pièce existante, lacune et conservation sourcée | IND-001 |
| 3 | [IND-022](../suites/ind-022-inactivite.md) | `sole-trader-inactivity-review` | Chronologie d'inactivité et liste des obligations à examiner sans cessation supposée | IND-001 |
| 3 | [IND-023](../suites/ind-023-cfe-initiale.md) | `initial-cfe-declaration-papers` | Dossier de déclaration initiale CFE et canal/échéance à vérifier | IND-001 |
| 2 | [IND-024](../suites/ind-024-avis-cfe.md) | `self-employed-cfe-notice-reading` | Fiche de l'avis, montants recopiés, période/base et demande d'explication | IND-001 |
| 3 | [IND-025](../suites/ind-025-conditions-exoneration-cfe.md) | `cfe-relief-conditions-review` | Dossier d'une exonération/réduction identifiée avec conditions, pièces et demande d'information | IND-001 |
| 3 | [IND-026](../suites/ind-026-tva-operation-france.md) | `domestic-vat-operation-papers` | Fiche d'une opération française, régime, période et pièces déclaratives à vérifier | IND-001, IND-015 |
| 3 | [IND-027](../suites/ind-027-tva-internationale.md) | `cross-border-vat-orientation` | Carte d'une opération, pays/parties, questions TVA et dossier de relais douanier si nécessaire | IND-001 |
| 3 | [IND-028](../suites/ind-028-cessation-ei.md) | `sole-trader-cessation-papers` | Dossier de formalité de cessation, état du dépôt et obligations restant à examiner | IND-001 |
| 3 | [IND-029](../suites/ind-029-dernieres-declarations-sociales.md) | `final-social-declaration-papers` | Fiche de dernière période sociale, recettes à rapprocher et dépôt à vérifier | IND-001, IND-028 |
| 3 | [IND-030](../suites/ind-030-dernieres-pieces-fiscales.md) | `final-business-tax-papers` | Dossier de fin d'activité pour un impôt et une période identifiés | IND-001, IND-028 |
| 3 | [IND-031](../suites/ind-031-regularisation-apres-cessation.md) | `post-closure-contribution-reading` | Rapprochement cessation/déclarations/appels et demande d'explication ciblée | IND-001, IND-028 |
| 2 | [IND-032](../suites/ind-032-avis-controle.md) | `self-employed-urssaf-audit-notice` | Fiche du contrôle, périmètre, modalités annoncées et pièces utiles pour préparer le contact | IND-001 |
| 2 | [IND-033](../suites/ind-033-lettre-observations.md) | `urssaf-audit-observations-response` | Tableau chef d'observation/faits/pièces/inconnues et brouillon de réponse ciblé | IND-001, IND-032 |
| 2 | [IND-034](../suites/ind-034-recours-cra.md) | `self-employed-cra-appeal` | Dossier et brouillon de recours propre à une décision éligible, calendrier sourcé ou réservé | IND-001 |
| 2 | [IND-035](../suites/ind-035-opposition-contrainte.md) | `urssaf-constraint-opposition` | Fiche de contrainte et dossier pour opposition selon régime spécial vérifié | IND-001 |
| 3 | [IND-036](../suites/ind-036-remise-majorations.md) | `urssaf-surcharge-remission` | Dossier gracieux et brouillon portant sur des majorations identifiées | IND-001 |
| 3 | [IND-037](../suites/ind-037-echeancier-urssaf.md) | `urssaf-payment-plan-request` | Proposition documentée d'échéancier demandé et brouillon, distincte d'un accord | IND-001 |
| 3 | [IND-038](../suites/ind-038-mediation-urssaf.md) | `self-employed-urssaf-mediation` | Dossier d'admissibilité et brouillon de médiation avec calendriers distincts | IND-001 |
| 3 | [IND-039](../suites/ind-039-non-diffusion-sirene.md) | `sole-trader-sirene-dissemination` | Fiche du statut de diffusion, données concernées et brouillon au canal officiel vérifié | IND-001 |
| 3 | [IND-040](../suites/ind-040-occultation-rne.md) | `sole-trader-rne-redaction` | Dossier identifiant registre/acte/donnée, fondement à vérifier et demande bornée | IND-001 |
| 3 | [IND-041](../suites/ind-041-questions-cumul.md) | `self-employed-cumulation-questions` | Tableau de questions et pièces par décisionnaire, sans calcul commun de revenu | IND-001 |
| 4 | [IND-042](../suites/ind-042-calcul-cotisations.md) | `micro-social-period-calculation` | Tableau reproductible des cotisations d'une période, distinct des taxes et prestations | IND-001 |

IND-009 dépend du calcul ordinaire IND-042 et de la lecture ACRE IND-008 :
pas de dépendance inverse. IND-034 et IND-035 ne dépendent pas d'une médiation,
ni réciproquement : chaque voie se qualifie avec son propre acte. IND-032 et
IND-033 couvrent la phase de contrôle, pas un recours contre la décision
ultérieure. IND-016/018 lisent les options ; IND-017 prépare la déclaration
annuelle ; IND-019 seul calcule le versement de l'activité pour une période.
IND-014 et IND-015 vérifient leurs propres seuils et proratas ; IND-042
calcule les cotisations ordinaires, IND-009 l'ACRE du micro-social, sans
calcul général de statuts ni double calcul de l'exonération.

## Frontières et fiches de relais

| Propriétaire du complément | Question transmise et seules pièces nécessaires | Résultat conservé ici |
|---|---|---|
| DOM-011 — fiscalité | Impôt du foyer hors activité, société/IS, contrôle fiscal, réclamation formelle, recouvrement fiscal, sursis et recours ; acte, impôt, périodes, notification, avis/options et question précise. Facturation électronique/e-reporting et mentions fiscales de facture : flux, qualités, territoires et dates. | Fiscalité courante de l'activité indépendante : options, préparation annuelle, CFE, TVA, pièces de cessation. Pas de double calcul ni de recours formel inclus dans une demande d'information. |
| DOM-012 — protection sociale | CAF, ARE, ARCE, ATI, aides France Travail et décisions de caisse : prestation/décision, dates, pièces de création/revenus strictement utiles ; CR07 pour ATI. | ACRE CR01, cotisations et CR08 après cessation ; aucun abattement ni revenu universel partagé avec la caisse. |
| Travail privé / DOM-037 | Clause ou relation de travail, exclusivité, éventuel salariat déguisé ; contrat et faits du lien d'emploi, statut public à qualifier. Employeur société : ses recours sociaux restent à découper dans le travail, TRAV-020 ne les remplace pas. | Obligations propres à l'activité indépendante et questions de cumul IND-041, sans décision sur le contrat d'emploi. |
| DOM-036 / DOM-042 | Pension ou régime artiste/intermittent : décision, statut, périodes utiles. | Régime micro non présumé à partir de la profession ni du seul mot Urssaf. |
| commercial / consommation ou secteur | Client professionnel : contrat et facture chez commercial ; client particulier : qualité et objet vers consommation/secteur. COM-019/020 pour paiement suspect, abonnement ou mandat de formalités ; PI-002 pour marque. | Lecture des obligations publiques de l'activité, pas de recouvrement client ni de contrat traité du seul fait du statut indépendant. |
| SOC-023/024/026/027 | Société : forme et formalité ; difficultés globales/patrimoine EI : dettes, dates, garanties et inconnues de solvabilité vers SOC-027 à cadrer. | Formalités EI, inactivité et cessation sur pièces, aucune radiation assimilée à extinction de dette. |
| DOM-003 / ENF-001 | Identification d'une contrainte ou acte de saisie : acte entier, notification, titre/décompte. Aucun délai générique d'exécution sur une opposition sociale. | IND-035 garde le régime spécial de l'opposition à contrainte Urssaf ; la saisie est une question distincte. |
| DOM-041 | Relation avec expert-comptable : mission, facture, échanges et question sur prestation. | Inventaire de pièces, calcul borné sourcé si tâche livrée, aucune tenue comptable ni expertise. |
| EXIST-003 / PRV-028/029 | Copie d'annuaire ou moteur : URL, donnée, source/date et demandeur ; questions séparées au responsable et au moteur. | Sirene IND-039 et RNE/occultation d'acte IND-040 ; non-diffusion et effacement privé ne se confondent pas. |
| DOM-009 / secteur / EXIST-007 | Opération douanière : pays, bien, trajet et acte ; activité réglementée : métier et acte envisagé ; changement réglementaire identifié : texte concerné. | Fiche TVA d'une opération, qualification des prérequis et des pièces sans autorisation d'exercer déduite du registre. |
| DOM-004 | Convention bancaire et litige d'usage : clauses et faits utiles. | IND-020 vérifie l'obligation légale de compte ; ne décide pas des conditions commerciales de la banque. |

Pas de transfert automatique de pièces, installation ni délégation. Si le
complément n'est pas disponible, expliquer la question, les pièces et le
professionnel ou service concret à consulter, en signalant la limite.
L'administration instruit le dossier ; l'avocat/expert-comptable conseille.

## Références métier prévues et limites

Les sources détaillées de chaque suite sont des **pistes non ouvertes** :
CSS et textes micro-social/ACRE/contrôle/recours ; CGI/annexes/LPF pour les
obligations fiscales courantes ; Code de commerce et textes de formalités,
Sirene/RNE ; textes UE pertinents pour TVA ; procédures officielles Urssaf,
Insee, INPI et fisc. Guides et doctrine ont leur statut propre ; BOFiP
n'est invoqué comme opposable qu'après vérification de son régime.

Chaque implémentation recherchera texte exact, champ, version, exceptions,
entrée en vigueur et transitions. Les allégations des matrices sur réforme
ACRE, franchise TVA, calendriers ou références de facture ne sont ni validées
ni intégrées comme règles par défaut. BASE-010 offre les voies alternatives
officielles en maintenance, sans dépendance runtime à ses scripts.

Points restant hors de ce découpage : recours juridictionnel après CRA,
contentieux/rejet de formalité EI, calcul complet au réel ou option IS,
comparaison financière de statuts, calcul total d'IR du foyer, liquidation
de TVA/CFE, tenue des livres, représentation, fraude/pénal allégué, prévention
et procédures collectives/patrimoine traités par SOC-027 à cadrer. Une
orientation ne vaut pas livraison de ces fonctions. Les points reçus et leur
couverture sont tracés dans la [matrice](dom-039-couverture-demandes.md).
