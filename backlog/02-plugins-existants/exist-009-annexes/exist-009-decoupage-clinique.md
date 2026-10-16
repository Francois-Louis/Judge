# EXIST-009 — Découpage de la clinique juridique

Propositions du **16 octobre 2026**, issues de l’[inventaire exhaustif](exist-009-inventaire-clinique.md).
Les 23 CLN restent `proposee`. La [relecture du cadrage](exist-009-verification.md)
suit une échéance à notification inconnue et un accueil logement fictifs :
références à lire, références interdites au parcours français et personnes qui
doivent vérifier/valider sont distinguées. Aucun skill n’est exécuté ici.

## Contrat commun et première tranche proposée

Toutes les suites dépendent d’EXIST-009, PILOTE-003, BASE-005 et BASE-006.
PILOTE-003 est terminé après BASE-011 : préalable satisfait, sans sélection
d’extension. Les limites H01 complet et lecteur indépendant restent consignées.

**Première tranche proposée : CLN-001**, fiche du cadre réel d’une structure à
partir de ses documents et déclarations. Clinique universitaire, association,
accueil d’information, consultation juridique et représentation ne sont pas
présumés identiques. Sortie : activités/périmètre, acteurs/qualités, limites,
règles de supervision et traitement des données à établir, sans certification.
Exercices fictifs et préfiguration documentaire restent possibles sans ouvrir
dossier réel ; l’usage sur données bénéficiaires exige cadre et accès établis.

Une dépendance métier désigne le contrat d’entrée ; une fiche équivalente
manuelle est admise avec provenance et manques, sans historique d’exécution.
Chaque tranche embarque méthode BASE-005 1.0.0 et ses références locales et
corrige ses propres blocs de setup/routage/annonces ; données durables gardées
par BASE-008, profil absent créé seulement après entretien neuf. Aucune
installation du domaine voisin requise.

## Stories et résultats

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [CLN-001](../suites/cln-001-cadre-structure.md) | Documenter le cadre réel d’une clinique | Aucune |
| [CLN-002](../suites/cln-002-accueil-minimal.md) | Préparer une fiche d’accueil minimal | CLN-001 |
| [CLN-003](../suites/cln-003-accueil-logement.md) | Préparer un accueil logement sans analyse de fond | CLN-002 |
| [CLN-004](../suites/cln-004-releve-conflits.md) | Préparer un relevé pour contrôle de conflits | CLN-001 |
| [CLN-005](../suites/cln-005-plan-recherche.md) | Préparer un plan de recherche français borné | CLN-002 |
| [CLN-006](../suites/cln-006-etat-recherches.md) | Dresser l’état d’un corpus de recherche fourni | CLN-005 |
| [CLN-007](../suites/cln-007-support-analyse.md) | Préparer un support d’analyse pour l’étudiant | CLN-005 |
| [CLN-008](../suites/cln-008-forme-projet-logement.md) | Mettre en forme un projet logement déjà instruit | CLN-003 |
| [CLN-009](../suites/cln-009-demande-pieces.md) | Préparer une demande routine de pièces à la personne | CLN-002 |
| [CLN-010](../suites/cln-010-point-personne.md) | Préparer un point à la personne accueillie | CLN-002 |
| [CLN-011](../suites/cln-011-point-referent.md) | Préparer un point interne au référent | CLN-002 |
| [CLN-012](../suites/cln-012-saisie-echeance.md) | Consigner une échéance déclarée et ses incertitudes | Aucune |
| [CLN-013](../suites/cln-013-etat-echeances.md) | Présenter les échéances et dates à vérifier | CLN-012 |
| [CLN-014](../suites/cln-014-suivi-echeance.md) | Consigner une décision sur une échéance suivie | CLN-012 |
| [CLN-015](../suites/cln-015-soumission-revue.md) | Soumettre une version de sortie à revue | CLN-001 |
| [CLN-016](../suites/cln-016-decision-revue.md) | Consigner une décision de revue attribuée | CLN-015 |
| [CLN-017](../suites/cln-017-journal-contacts.md) | Consigner un contact de dossier | CLN-002 |
| [CLN-018](../suites/cln-018-transmission-dossier.md) | Préparer la transmission d’un dossier | CLN-002 |
| [CLN-019](../suites/cln-019-continuite-cohorte.md) | Présenter la continuité d’un périmètre de dossiers | CLN-018 |
| [CLN-020](../suites/cln-020-accueil-etudiant.md) | Préparer un parcours étudiant sur cas fictif | CLN-001 |
| [CLN-021](../suites/cln-021-guide-accueil.md) | Préparer un guide de supervision pour l’accueil logement | CLN-001 |
| [CLN-022](../suites/cln-022-preferences-clinique.md) | Modifier une préférence de clinique | Aucune |
| [CLN-023](../suites/cln-023-espace-dossier.md) | Isoler un espace minimal de dossier clinique | Aucune |

Les deux alias `form-generation` et `plain-language-letters` restent des
redirections non invocables alignées par CLN-008/009/010 ; pas deux nouvelles
tâches françaises. Aucun agent, scheduler ou cookbook n’est ajouté par principe.

## Cadre, rôles et validation

Les questions suivantes sont des exigences des futures implémentations, **pas
une qualification de la structure de l’utilisateur ou des règles françaises
vérifiées dans EXIST-009**.

| Élément | Faits/pièces à obtenir | Distinction à conserver |
|---|---|---|
| Structure/activité | Statut, objet, établissement porteur, convention/charte, activité réellement proposée, public, territoires, services et actes couverts | Accueil/information, analyse et conseil, rédaction pour tiers, signature, représentation et transmission distincts. Aucun rôle déduit du seul nom clinique. |
| Personnes | Responsable organisationnel, enseignant, étudiant, personnel accueil, référent métier, avocat/autre professionnel si pertinent, signataire et relais | Titre de professeur, étudiant juriste ou rôle déclaré ne prouve pas qualité professionnelle, mandat ou habilitation. Qualité et périmètre à documenter, preuve manquante visible. |
| Supervision | Processus réel, décisionnaire, critères de revue, version du guide et sorties concernées | Validation pédagogique, vérification des faits/sources, contrôle juridique, autorisation interne et décision d’agir sont distincts ; mode assist/guide/teach et file facultative ne changent pas cadre juridique. |
| Données/outils | Organisme/responsables et prestataires, finalités, catégories nécessaires, personnes/destinataires autorisés, accès, conservation, transferts et règles de structure | Consentement IA seul ne certifie pas base/traitement ; outils autorisés, information des personnes, sécurité et droits à rechercher selon contexte. Aucun envoi à des services présumés connectés. |
| Conflits/admission | Parties/qualités strictement utiles, processus autorisé, résultats/provenances, décideur et périmètre | Indicateur ou absence de résultat distincts de clearance ; admission distincte de mandat et d’accès. Pas de lecture interclient depuis simple homonymie. |
| Urgence | Document complet, auteur/acte, dates littérales, notification prouvée ou manquante, fait de danger allégué, canal utile et référent | Inconnu ne devient pas standard ou absence d’urgence. Fiche de vérification et référent manquant explicites ; aucune attente de fin de semestre comme prise en charge. Alerte préparée distincte d’alerte effectivement transmise/reçue. |

Sources à rechercher par CLN-001 : documents réels de structure et établissement,
encadrement français des activités/qualités concernées, règles professionnelles
lorsqu’applicables, RGPD/droit national et conditions/documentation des outils.
Les textes précis, versions, champ et exceptions sont à lire avant conclusion ;
ABA Formal Opinion 512 et Model Rules ne sont pas des règles françaises.
L’étiquette AI-assisted, l’origine d’une communication ou une approbation
ne garantissent pas secret professionnel ou confidentialité.

## Retirer le graphe américain des échéances françaises

**Chemin hérité constaté :** `deadlines` lit profil/jurisdiction → sélectionne
`config/.../plausibility-bands/<state>.md` → annonce références CA/IL livrées
→ charge bande État **et federal-always** → compare date saisie au déclencheur
et fenêtre → écrit registre/avertissement. Une absence de bande renvoie à
copie du modèle IL. L’entretien ne doit pas être présenté comme mécanisme de
copie déjà démontré ; chemin déclaré et lecture réelle sont distincts.

CA contient des fenêtres California et Federal, IL des placeholders avec
durées US déjà renseignées et Federal. Leur simple renommage France ou copie
des fenêtres reste interdit dans la cible. Une date « dans la bande » ne
prouve ni droit applicable, ni fait générateur, ni notification.

CLN-012 possède le contrat de remplacement :

- registre d’une information et de son incertitude, **sans calcul** ;
- aucune référence CA/IL/fédérale chargée ou copiée pour dossier français ;
- références étrangères éventuellement conservées hors graphe français,
  explicitement identifiées, sans prétendre validation du droit US ;
- aucun `FR.md` de plausibilité fabriqué et pas d’erreur à corriger en créant
  une bande quand on veut seulement consigner une date déclarée ;
- aucune substitution d’une date de courrier, téléchargement ou entretien
  à la preuve de notification manquante.

CLN-013 et CLN-014 propagent ce contrat, ainsi que consommateurs intake,
draft/status, communications, revue et handoff. Courtroom5 ou guide configuré
ne contourne pas l’interdiction de calculer. L’étudiant/référent compétent ou
domaine procédural peut fournir une fiche équivalente sourcée ; outil clinique
enregistre son auteur et périmètre sans vérifier par une fenêtre américaine.

## Contrats de données et de contenu

| Contrat possédé | Champs et limites |
|---|---|
| Cadre CLN-001 et guide CLN-021 | Activités/rôles/qualités/périmètres/règles/décideurs, guide/version et champ pédagogique canonique `pedagogy_default` avec overrides explicités. Harmoniser producteurs et consommateurs qui utilisent aujourd’hui trois noms divergents ; préférence n’est pas règle. |
| Accueil CLN-002/003 et conflits CLN-004 | Identifiant minimal pseudonyme, récit attribué, pièces/pages, acteurs utiles, orientation supposée, dates/inconnues, urgence motivée, contrôle de conflit et admission encore non décidés ou attribués. Aucun patronyme requis dans chemin. |
| Recherche CLN-005/006 et support CLN-007 | Question bornée, faits/dates/territoire, source primaire/secondaire/piste, version/passages lus/non lus, couvert/non couvert, éléments de l’étudiant séparés de suggestions générées. Source accessible ne prouve pas applicabilité, guide interne ne remplace pas texte. |
| Dates CLN-012/013/014 | `case_id`, nature de date, `date_declared`, `due_date` nullable, `verification_status`, `trigger_event`, `notification_evidence`, source/passage/version, `reviewer`/`reviewed_at` et historique. Échéance alléguée calculée avec notification inconnue : `due_date: null`, `a-determiner`, date entrée conservée comme déclaration et responsable de vérification nommé ou absent. |
| Projet CLN-008/009/010/011 et revue CLN-015/016 | Identifiant/version/empreinte de document, auteur et destinataire/canal, source du contenu, questions/réserves, version soumise, décideur/qualité/portée/preuve et date d’approbation. Toute modification produit nouvelle version à revoir ; approuvé ne signifie signé/envoyé/déposé. File mutable en racine BASE-008, référence empaquetée en lecture seule. |
| Contacts CLN-017 et transmission CLN-018/019 | Événements prévus/déclarés/prouvés, correctif attribué, résumé minimal, source et actions restantes ; projet préparé/revu/transmis/reçu/prise en charge distincts. Cohorte voit seules métadonnées autorisées, pas tous récits/dossiers. |
| Espace CLN-023 | Identifiant lié à intake/dates/comms/revue/handoff, racine gardée, refus collisions/liens et liste minimale. Aucun admission/mandat/droit d’accès depuis simple création d’un espace ; archive ne détruit pas données ni recours. |

Les dates d’audience ou de remise explicitement fixées dans une pièce ont leur
nature et preuve, sans être assimilées au calcul d’un délai. La clinique ne
refait aucun calcul ; date de référence et fuseau de rapport explicites.
Avertissements 14/7/3/1 restent préférences de vue ; `completed` et `closed`
ne constatent pas dépôt ou extinction de droits. Unknown/a-determiner doit
apparaître dans vues, revues et transmissions, pas disparaître du tri des dates.

## Accueil français et domaines de fond

| Situation d’accueil | Propriétaire et fiche à transmettre |
|---|---|
| Logement, bail, charges, réparations, dépôt | DOM-006 ; clinique porte récit/pièces/qualités/acte et questions, pas régime UD, repair-and-deduct ou conseil de cesser paiement. |
| Acte de saisie/expulsion/exécution distinct | DOM-003 ; acte complet, auteur, parties, notification/dates et question ; commissaire de justice seul ne suffit pas à qualifier l’acte. |
| Séjour/asile ou demande d’autorité | DOM-028 ou secteur selon acte ; pas ICE/NTA/asylum one-year ; ne collecter faits sensibles supplémentaires que si utiles au cadre d’accueil. |
| Famille/sécurité/protection | DOM-013/038 selon demande ; canal de contact adapté, faits strictement nécessaires, qualification des acteurs/actes et urgence à instruire sans diffusion large. |
| Consommation, dette, banque ou surendettement | DOM-001/004/024 ou secteur selon objet ; consumer du modèle US est recouvrement, pas tout le droit consommation français. |
| Travail, dommages, santé, données, autres secteurs | Domaine propre selon faits ; clinique prépare fiche autonome de question exacte, pièces/dates et manques, pas raisonnement de fond dupliqué. |
| Acte judiciaire/réponse à contrôle ou décision | Procédure et qualité d’intervenant à identifier, contentieux/administratif/pénal/secteur selon acte ; pas court-ready ou représentation déduits du rôle étudiant/professeur. |

Les relais DOM/EXIST/CLN encore proposés ne sont pas des capacités déjà
adaptées. S’il manque un relais, remettre fiche manuelle/question/pièces à
obtenir sans appeler skill hérité ou charger tous plugins. Un guide contenant
un appel interplugin n’est pas autorisation d’exécuter une tâche non adaptée.

## Sources et recette futures

Sources françaises par matière : textes applicables/version aux faits, pièces
et décisions exactes, autorités/juridictions selon acte ; EUR-Lex seulement si
rattachement. Règles de structure/encadrement professionnel ne sont pas des
substituts à ces sources ; source inaccessible réserve la conclusion dépendante
après voie officielle alternative pertinente BASE-010, sans règles/citations
inventées ni abonnement obligatoire. Le modèle pédagogique ne prime pas la
preuve des faits ou les limites de compétence.

La recette de CLN-012/003/015/016/018 comprend trace des fichiers lus/non lus,
profil/guide absents, source inaccessible, notification inconnue, bande US
présente dans paquet mais non lue, référent absent et document modifié après
approbation. Paquet détaché, client, résultat métier et lecteur non juriste
restent couches distinctes BASE-006 ; la relecture présente n’en tient pas lieu.

Aucun contenu éditeur, donnée bénéficiaire, installation, contact, compte,
signature, paiement, dépôt, publication ou transmission réelle n’est modifié
ou réalisé dans ce cadrage.

