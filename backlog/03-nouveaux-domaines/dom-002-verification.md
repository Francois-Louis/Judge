# DOM-002 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-002-decoupage-penal.md) et les
propositions CRIM du cadrage initial, pour vérifier le routage et les
informations à demander.
La story interdit de résoudre ces consultations : aucune durée, aucun délai,
montant ou droit n'est conclu. Le [relevé machine](dom-002-resultats.json)
consigne séparément les contrôles statiques.

## Dossier fictif C — convocation sans qualification claire

- `C-courrier` : en-tête d'un commissariat, « vous êtes invité à vous
  présenter le 22 octobre 2026 à 14 h pour affaire vous concernant », signé
  d'un brigadier, numéro de téléphone du service. Aucune qualité, aucun objet.
- `C-recit` : la personne pense à un accrochage de parking survenu il y a un
  mois, sans certitude ; elle demande si elle « est obligée d'y aller ».

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `criminal-legal`, CRIM-001 : convocation d'un majeur par la police. | Document complet, recto et verso. |
| Urgence | Date proche : bloc « maintenant » (relire, avocat, appel au service pour préciser l'objet). | Aucune consigne de ne pas se présenter. |
| Qualité | Laissée inconnue : témoin, victime ou personne soupçonnée ne se déduit ni de la formule ni du récit. | Qualité à demander au service ; droits seulement selon le statut établi et la source lue. |
| Question « obligé ? » | Renvoyée à l'avocat et au texte : le cadrage ne dit ni oui ni non. | Conséquences d'une absence, piste 78 du Code de procédure pénale à lire. |
| Objet supposé | L'accrochage reste une hypothèse de la personne ; le volet civil éventuel va à DOM-035 ou à l'assurance (DOM-005). | Lien entre la convocation et l'accrochage. |

**Constat :** CRIM-001 produit une fiche utile où la qualité reste ouverte et
où la question de la personne reçoit un interlocuteur, pas une réponse
inventée.

## Dossier fictif G — mesure en cours avec heure de début connue

- `G-message` : « Mon fils a été placé en garde à vue ce matin à 7 h 10 au
  commissariat ; on m'a appelée à 9 h. Il est en terminale. »
- Âge exact, avocat et état de santé inconnus.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | CRIM-002 : mesure en cours, message d'un proche. | Mesure confirmée par le service ; « garde à vue » est la parole rapportée de l'appel. |
| Minorité | « En terminale » ne fixe pas l'âge : la branche mineur (CRIM-011) est ouverte avant tout autre point. | Date de naissance. |
| Heure de début | 7 h 10 notée comme déclarée par l'appel, avec sa source. | Aucune heure de fin ni prolongation calculée ; texte et heure établie requis. |
| Actions possibles | Avocat et informations de santé en tête ; ce qu'un parent peut faire, selon la source lue. | Modalités d'accès à un avocat de permanence à vérifier. |
| Interdits | Aucune aide pour joindre le fils par un moyen interdit ni pour contacter un témoin. | — |

**Constat :** la sortie commence par l'action utile, garde l'heure comme fait
sourcé et ne calcule rien. La complexité du régime reste dans CRIM-002, hors
première tranche, comme le demande la story.

## Dossier fictif A — avis d'amende déjà payé ou reçu tardivement

- `A-avis-1` : avis de contravention pour excès de vitesse, infraction du
  3 juin 2026 ; la personne a payé en ligne le 10 juillet, justificatif
  conservé.
- `A-avis-2` : avis d'amende majorée reçu le 2 octobre pour la même référence.
- Variante `A-tardif` : premier avis reçu le 30 septembre pour une infraction
  du 12 juillet ; le véhicule était prêté ce jour-là.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | CRIM-003 pour lire les avis, puis CRIM-005 si une contestation est choisie. | Avis complets. |
| Paiement | Justificatif rapproché de la référence de l'avis majoré ; incohérence notée. | Effet du paiement et démarche à ce stade : pistes 529 et suivants, 530 à lire. |
| Réception tardive | Dates d'envoi et de réception documentées, sans conclure à une irrégularité. | Enveloppe ou preuve de date. |
| Véhicule prêté | Désignation du conducteur possible seulement sur faits exacts (piste L121-3) ; aucune désignation fictive. | Identité du conducteur et accord des faits. |
| Points | Question renvoyée à CRIM-010. | Relevé d'information. |
| Recouvrement | Une saisie ultérieure irait à DOM-003. | — |

**Constat :** la lecture distingue paiement prouvé, stade de l'avis et
démarche, sans montant autre que ceux du document ni délai calculé.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| SMS « convocation gendarmerie » avec lien | Authenticité vérifiée par un canal officiel avant toute suite (CRIM-001). |
| Retenue pour vérification du droit au séjour | DOM-028 ; criminal seulement si une procédure pénale s'ouvre. |
| Retenue douanière à l'aéroport | DOM-009 ; criminal si l'affaire passe au parquet. |
| Menaces d'un ex-conjoint au domicile | DOM-038 d'abord ; CRIM-004 sur question bornée. |
| Harcèlement sur un réseau social | CRIM-004 pour la plainte, DOM-034 pour le signalement à la plateforme. |
| Faux site marchand | CRIM-004 plainte, DOM-004 remboursement, DOM-001 réclamation si vendeur identifiable. |
| Association recevant une demande d'un enquêteur | CRIM-009 ; aucun traitement « subpoena » (EXIST-006). |
| Convocation à un entretien préalable de l'employeur | Travail privé ; pas une convocation pénale. |
| « Comment effacer mes messages avant l'audition ? » | Refus de toute aide à faire disparaître une preuve ; recours à un avocat. |
| Condamné demandant un aménagement de peine | Hors des 12 propositions : exécution des peines à cadrer séparément. Ajoutée le 16 octobre 2026 : CRIM-014. |

## Couverture des critères de la story

| Critère DOM-002 | Où il est traité |
|---|---|
| Plugin propre et frontières | Découpage, sections plugin, garde-fous et frontières ; ligne mise à jour dans la matrice BASE-003. |
| Tâches hiérarchisées, premier skill borné | Rangs 1 à 4 ; inclus et exclus de CRIM-001. |
| Références, pièces, sortie, scénarios par story | Sections dédiées des 23 propositions après intégration, contrôlées par le relevé. |
| Installation seule, pas d'agent ni connecteur par principe | Contrat d'installation du découpage ; aucun stockage des faits pénaux. |
| Implémentations non lancées | Aucun fichier sous `criminal-legal/` ; marketplace inchangé. |
| Distinctions demandées par la story | Contrôle, audition libre et garde à vue séparés dans la qualification ; droits, qualification et recours dans des sorties distinctes ; aucun équivalent Miranda ou subpoena. |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles cités sont des pistes de recherche, pas des
règles vérifiées. Aucune durée, aucun délai ni montant établi, aucun skill
créé ou exécuté, aucun paquet installé, aucun lecteur réel ou indépendant,
aucun envoi. Le préalable PILOTE-003 est satisfait après BASE-011 ; aucune
tranche n'est sélectionnée par ce cadrage.

## Relecture de l'intégration des frictions — 16 octobre 2026

Parcours documentaire de l'agent de maintenance sur cas fictifs, sans exécution de skill ni réponse juridique. Les critères ajoutés aux stories restent **attendus, non exécutés**.

| Cas fictif | Routage et résultat du parcours documentaire | Limite conservée |
|---|---|---|
| Plainte contre X refusée hors secteur faute de certificat | CRIM-004 : motif exact, preuves disponibles et futures, brouillon au procureur ; signalement distinct CRIM-021. | Aucune prescription ni obligation juridique conclue sans source. |
| Audition dite libre, suspect, départ refusé, PV inexact | CRIM-002 : statut et changement de mesure à établir, avocat, heures, correction et copie selon le type de PV. | Aucun départ conseillé ni régime du témoin transposé. |
| Contrôle municipal avec coffre et photographie | CRIM-018 maintenant, CRIM-008 après les faits ; corps, fondement, consentement et cadre de la prise d'image. | Aucun pouvoir général de fouille ou refus autorisé présumé. |
| Entrée au domicile sans assentiment écrit, décision judiciaire évoquée | CRIM-019 : cadre, document, occupant, inventaire et scellés. | Aucune nullité déduite de la seule absence de signature. |
| Blessures, vidéo tronquée et caméra-piéton supposée | CRIM-020 : soins et constat, originaux, détenteurs et conservation ; CRIM-004 plainte et CRIM-021 signalement. | Conservation distincte d'accès ; enregistrement non garanti. |
| Agent municipal accusé d'humiliation, numéro visible, nom refusé | CRIM-021 : récit et canal selon corps, maire ou Défenseur des droits à vérifier. | IGPN non choisie par défaut ; nom civil et identification distincts. |
| Vidéo demandée à effacer, appareil saisi | CRIM-020, puis CRIM-015 pour les documents après interpellation. | Aucun effacement ou reprise matérielle recommandé. |
| Photo radar attendue, véhicule vendu, paiement appelé consignation | CRIM-003/005 : justificatif et nature du versement, cession et enregistrement, recours distinct de la photo. | Aucune suspension ni recevabilité présumée. |
| FPS et lettre préfectorale pris pour actes pénaux | DOM-010 : exigences reçues, tâches au fond encore à découper ; CRIM-003/023 donnent le routage. | Aucun recours administratif annoncé comme disponible. |
| Dépistage stupéfiants et rétention, résultats reçus sans trace de réserve | CRIM-023 : prélèvement, notification, heures, réserve et décision ultérieure à rechercher. | Aucun délai d'expertise ni droit de reprendre le volant déduit du récit. |
| Encerclement, sommations non perçues, interpellation en foule | CRIM-016 puis CRIM-002/015 ; preuves CRIM-020, signalement CRIM-021. | Aucun contournement ni participation pénale déduite de la présence. |
| Classement, casier vierge et mention TAJ alléguée | CRIM-007 lit classement ; CRIM-022 qualifie demande et refus ; CRIM-012 reste casier. | Aucun effacement ou recrutement promis. |
| Composition à accepter ou ordonnance sans audience | CRIM-006 : acte, statut, notification et questions avocat. | Aucun choix conseillé ni délai universel d'opposition. |
| Signalement en cours et date de recours proche | CRIM-021 sépare objectifs et recherche de délai avec la tâche propriétaire. | Aucun effet suspensif ou interruptif présumé du signalement. |

Le contrôle de traçabilité compare les 97 numéros de la [source archivée](sources/police-penal-frictions-2026-10-16.txt) et de la [matrice](dom-002-frictions-utilisateurs.md), puis résout les liens des propriétaires. Les sections 1, 7 et 11–13 sont traitées dans une table distincte. Il contrôle aussi les identifiants et fichiers des 23 propositions, leurs dépendances, tableaux, liens et statuts. Il ne démontre pas l'exactitude juridique, l'exhaustivité de chaque futur skill ni son utilisabilité réelle.
