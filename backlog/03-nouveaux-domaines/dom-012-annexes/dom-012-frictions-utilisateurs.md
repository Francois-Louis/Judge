# Indemnisations, allocations et aides sociales — Réponses à prévoir

Demande du **16 octobre 2026** : « voici les frictions des utilisateurs auxquelles il faut pouvoir répondre ». Le [guide fourni](../sources/aides-sociales-frictions-2026-10-16.txt) est conservé à l'octet près. La matrice reprend ses **185 points**, ainsi que les tableaux de procédures, de prescriptions, de délais et les réflexes non numérotés.

**Exigences de backlog.** [DOM-012](../dom-012-protection-sociale.md) reste `proposee`. Les codes FT, RS, etc. ci-dessous désignent des tâches candidates locales à cette annexe, pas des stories ni des commandes. Elles restent à découper en stories d'implémentation, une prestation et une décision à la fois. La première tranche proposée reste la lecture d'un indu pour un organisme et une prestation choisis. L'éventuelle séparation d'un plugin emploi/minima sociaux reste à décider au cadrage ; aucun plugin ou skill n'est livré ici.

## Contrat des réponses futures

Partir du problème exprimé sans exiger de vocabulaire juridique. Qualifier demandeur et pouvoir du représentant, régime, territoire, organisme qui décide et organisme qui paie, prestation, périodes, décision complète, motif, notification et réception. Accepter les pièces manuelles ; demander seulement les données nécessaires, avec provenance, contradictions et inconnues. Une situation difficile, un contrôle ou une sélection algorithmique ne prouvent ni abus ni fraude.

La sortie explique ce qui est compris, les pièces manquantes, les sommes recopiées ou rapprochées et la prochaine démarche utile. Un calcul de droits exige une tâche distincte, des sources effectivement lues et les règles applicables aux dates du dossier. Une simulation n'est ni une demande ni une décision. Déclaration corrective, demande de décompte, contestation, remise, échéancier et opposition à contrainte ont des objets distincts ; leurs effets réciproques sont à rechercher avant toute recommandation.

Pour chaque échéance : nature, texte/version, champ et transitions, événement déclencheur et preuve, unité de décompte, exceptions, actes interruptifs ou suspensifs, acte requis et destinataire. Une date indiquée par le guide ou une notification reste à contrôler ; si les éléments manquent, terme `a-determiner`, pièces et conseil compétent. Ne pas attribuer par défaut un effet conservatoire au téléphone, à une médiation, à une seconde réclamation ou à une demande RGPD. Pour une urgence de ressources ou une contrainte, placer l'orientation vers un avocat compétent en tête ; BASE-013 impose aussi une phrase finale adaptée. France Services, le service payeur et le conseil juridique ont des rôles différents.

Les futures stories préciseront leurs fichiers et références embarquées, méthode locale BASE-005, autonomie BASE-003/008, recette BASE-006 et critères de compréhension. Les relais ci-dessous ne créent pas de dépendance d'installation ; si le relais n'est pas livré, produire une fiche manuelle pour le professionnel compétent. Aucun dépôt, signature, envoi, rappel récurrent ou synchronisation n'est exécuté par ce lot.

## Tâches candidates et frontières

Chaque ligne est un résultat à borner lors du cadrage, avec un cas normal et une limite. Les intitulés qui couvrent plusieurs actes devront être séparés en stories. Les sources sont des **pistes à ouvrir lors de l'implémentation**, pas un corpus lu dans ce lot.

| Code | Tâche et propriétaire principal | Entrées spécifiques et résultat attendu | Sources à rechercher | Cas normal / limite attendus |
|---|---|---|---|---|
| FT01 | Lire l'ouverture ou le refus ARE — [DOM-012](../dom-012-protection-sociale.md) | Fin de contrat, inscription, périodes, attestation et décision ; chronologie des conditions examinées et questions de réexamen | Code du travail, règlement/convention d'assurance chômage, Unédic et France Travail aux dates utiles | Contrats courts omis / démission-reconversion avant validation : pas d'ARE garantie |
| FT02 | Rapprocher les éléments d'un calcul ARE — DOM-012 | Bulletins, périodes retenues, notification et détail ; écarts de période, SJR, durée ou dégressivité à expliquer, sans moteur de calcul implicite | Textes d'assurance chômage, annexes et transitions | Période manquante / calcul défavorable mais conforme possible |
| FT03 | Lire le début de paiement — DOM-012 | Inscription, indemnités de rupture/congés, notification, historique et paiements ; séparer différés, attente, ouverture et terme de paiement | Régime ARE applicable et règles des différés | Premier paiement tardif / attente déjà appliquée : historique à vérifier |
| FT04 | Lire une reprise de reliquat ou un rechargement — DOM-012 | Ancienne ouverture, jours restants, emplois nouveaux, déclarations et décision ; questions sur reprise, option, rechargement et déchéance, actes à séparer | Règlement d'assurance chômage et droit d'option | Ancien droit repris / option potentiellement irréversible sans comparaison établie |
| FT05 | Préparer ou corriger une actualisation — DOM-012 | Demande d'actualisation, rubriques, activités, revenus, arrêt, formation, absence et accusés ; rapprochement et brouillon de correction par période | Consignes et textes France Travail propres au statut | Mission courte omise / personne dispensée : ne pas imposer une démarche universelle |
| FT06 | Préparer une demande d'adaptation du contrat d'engagement — DOM-012 | Contrat, référent, offres, contraintes exprimées et justificatifs utiles ; copie demandée et adaptation motivée | Code du travail, plein emploi, textes d'accompagnement et d'offre raisonnable | Garde incompatible / action d'insertion prise pour emploi : qualifier sa nature |
| FT07 | Répondre à un avertissement ou lire une sanction France Travail — DOM-012 | Convocation/envoi/réception, caractère obligatoire, démarches, observations et décision ; chronologie, motif et recours propre à l'acte | Textes de sanction/radiation dans leur version applicable | Justificatif ignoré / suspension, suppression et radiation distinguées |
| RS01 | Préparer une demande ou lire les ressources RSA — DOM-012 | Foyer réel, résidence, statut, ressources/patrimoine, demande et décision ; pièces et écarts à vérifier par nature de flux | CASF et textes RSA, CAF/MSA et département compétent | Séparation non enregistrée / transfert entre comptes distinct d'un revenu |
| RS02 | Lire l'accompagnement ou la sanction RSA — DOM-012 | Contrat, référent, convocations, contraintes et décision ; adaptation ou dossier de contestation à séparer | CASF, plein emploi, textes d'application et règles départementales | Plusieurs référents / santé empêchant une action : pas de durée uniforme imposée |
| PA01 | Préparer ou rectifier une déclaration de prime d'activité — DOM-012 | Foyer, justificatifs, préremplissage, mois et déclaration ; tableau source/mois/rubrique et demande ciblée | CSS prime d'activité, CAF/MSA, textes du préremplissage | Net social discordant / micro-activité : pas de transposition du net salarié |
| CR01 | Lire une demande ou décision ACRE — [DOM-039](../dom-039-micro-entreprise.md) | Statut, création/reprise, aide antérieure, demande, accusé, réponse et taux appliqué ; chronologie, conditions et questions à l'Urssaf | CSS, textes ACRE et transitions, Urssaf | Accusé absent / création autour d'une réforme : pas de taux ni délai repris du guide |
| CR02 | Préparer les questions d'un choix ARCE/maintien ARE — DOM-012 | Ouverture ARE, création, ACRE, revenus envisagés et décisions ; comparaison qualitative des conditions, besoins de trésorerie et inconnues | Régime ARCE/ARE, Unédic et France Travail | Activité incertaine / ACRE en attente : aucun choix fait à la place de la personne |
| CR03 | Lire un versement ARCE ou une reprise de droits — DOM-012 | Attribution, retenues, versements, activité, emploi repris, cessation et reliquat ; justificatifs et décision à demander | Régime ARCE et reprise/déchéance ARE applicable | Seconde fraction attendue / CDI ou activité poursuivie : condition à vérifier |
| CR04 | Rapprocher activité indépendante et maintien ARE — DOM-012 | Forme/régime, CA/bénéfice/rémunération, déclarations, paiements provisoires et décompte ; écarts et demande de régularisation | Règles de cumul selon statut et date d'ouverture | Micro-activité variable / SASU sans salaire ne prouve pas l'absence de déclaration |
| CR05 | Préparer une demande de poursuite de cumul à l'IPR — DOM-012 | Décision, plafond atteint, date et preuve, revenus et justificatifs ; conditions, calendrier et brouillon propre | Règlement applicable, Unédic/France Travail et procédure IPR | Plafond notifié / date incertaine ou conditions non remplies : réserve ciblée |
| CR06 | Lire une aide publique à la création — [DOM-010](../dom-010-administratif.md), attribution proposée à confirmer | Dispositif/financeur/territoire, appel, demande, décision, engagements, dépenses et versements ; conditions et dossier de justification, restitution à séparer | Règlement exact de l'aide, décision/convention, textes publics et cumuls pertinents | Accord de principe / dépense engagée avant autorisation : pas de subvention garantie |
| CR07 | Préparer les pièces ATI — DOM-012 | Statut, cessation/motif, ressources, décisions et attestation de non-viabilité éventuelle ; dossier et droits distincts de l'ARE | Code du travail, textes ATI et sources France Travail | Cessation documentée / fermeture volontaire seule : critères à rechercher |
| CR08 | Lire une régularisation de cotisations après cessation — DOM-039 | Cessation/radiation, dernières déclarations, périodes, appels et réception ; rapprochement et demande ciblée, distincts du droit ATI | CSS, régime social de l'activité et textes Urssaf | Régularisation après fermeture / dette sans détail : aucune extinction déduite de la radiation |
| LG01 | Lire une demande ou décision d'aide au logement — DOM-012 | Bail, entrée, demande, loyer, ressources, occupation, déménagement et notification ; chronologie d'ouverture/paiement et pièces à corriger | CCH, textes APL/ALF/ALS et sources CAF/MSA | Nouveau logement / période ou loyer retenu distinct du montant attendu |
| LG02 | Rapprocher versement logement et compte locatif — DOM-012 pour caisse, [DOM-006](../dom-006-logement.md) pour bailleur | Décomptes caisse/bailleur, quittances, impayés, décence et décisions ; écarts avec demandes séparées selon l'auteur | CCH aides, textes maintien/conservation et droit locatif pour le seul bailleur | Aide versée au bailleur / non-décence ne se traite pas comme simple absence de paiement |
| FD01 | Préparer un relais de fin de droits ASS/RSA — DOM-012 | Fin ARE, activité antérieure, foyer, ressources et décisions ; conditions distinctes, demandes et interactions à vérifier | Textes ASS et RSA, Unédic/France Travail, CAF/MSA | ASS refusée / ne pas conclure au refus RSA ni promettre un cumul intégral |
| FD02 | Lire rémunération et financement d'une formation — DOM-012 | Statut, formation, validation, dates, droits restants, accord de frais et rémunération ; deux circuits et chronologie | Textes ARE-F/RFF et autres dispositifs identifiés, financeur exact | Formation validée / frais engagés sans accord : aucun remboursement présumé |
| FD03 | Préparer une demande mobilité ou garde — DOM-012 pour aide France Travail | Événement, date, distance/frais, ressources, garde, accord et preuves ; dispositif actuel, pièces et calendrier propres | Décisions/règlements France Travail et sources officielles du dispositif | Reprise documentée / aide supprimée ou ancien formulaire : rechercher transition |
| JF01 | Lire un CEJ ou sa décision d'allocation — DOM-012 | Opérateur, contrat, actions, ressources, prestations, convocation et décision ; conditions/cumul ou sanction à séparer | Code du travail, textes CEJ, mission locale/France Travail | Entrée en CEJ / absence à une action : accompagnement et allocation distingués |
| JF02 | Préparer un dossier de prestations familiales ou ASF — DOM-012 | Foyer, événement, pension/titre, demande et décision ; prestation exacte, pièces et date d'effet à vérifier | CSS, CAF/MSA, ARIPA et textes propres à chaque prestation | Parent isolé / titre absent ou paiement partiel : ne pas confondre ASF, intermédiation et fixation de pension |
| SA01 | Lire un refus ou calcul IJ — DOM-012 | Arrêt, envois, activité/cotisations, attestation de salaire, subrogation, décomptes et motif ; pièces et recours administratif/médical à qualifier | CSS, assurance maladie, CRA/CMRA selon acte | Arrêt transmis / IJ payées à l'employeur : séparer caisse et maintien salarial |
| SA02 | Préparer une demande ou lire une décision C2S — DOM-012 | Régime, RSA éventuel, foyer, ressources, opposition/demande et décision ; questions d'ouverture/continuité | CSS et textes C2S, Assurance maladie | RSA et couverture absente / autre régime : pas d'attribution garantie sur le seul guide |
| SA03 | Lire reconnaissance ou renouvellement handicap — [DOM-025](../dom-025-handicap-autonomie.md) | Demande, décision MDPH/CDAPH, échéance, besoins et preuve ; pièces et voie propre ; paiement caisse chez DOM-012 | CASF/CSS et textes de la décision identifiée | Reconnaissance expirante / reconnaissance accordée mais paiement refusé : deux actes |
| SA04 | Préparer une demande de secours local ou FSL — DOM-012, attribution proposée à préciser avec DOM-010/006 | Lieu, urgence, foyer, dépenses, règlement, demande et décision ; subvention/prêt, pièces et interlocuteur | CASF, règlement départemental FSL, CCAS et aides locales | Dette énergie / prêt proposé : ne pas le présenter comme aide sans remboursement |
| IN01 | Lire un indu et rapprocher son décompte — DOM-012 | Notification intégrale, prestations/périodes, ressources, calculs et paiements ; tableau mensuel, motif et questions avant contestation | Textes propres à chaque prestation et organisme | Plusieurs prestations / erreur de caisse ne tranche pas à elle seule l'existence de dette |
| IN02 | Examiner une prescription d'indu — DOM-012 | Paiements, connaissance alléguée, qualification, notifications, titres et actes datés ; chronologie des prescriptions distinctes et inconnues | Textes prescription, récupération et recouvrement du régime, jurisprudence officielle | Anciennes mensualités / acte interruptif inconnu : pas de prescription déduite du seul âge |
| IN03 | Préparer une contestation d'indu — DOM-012 | Dette identifiée, désaccord précis, décision/réception, calcul et preuves ; brouillon adressé à l'autorité propre au régime et calendrier | Voies préalables et juridiction du régime, effets des demandes | Calcul contesté / décompte incomplet : ne pas laisser sa demande remplacer l'acte requis |
| IN04 | Préparer remise, échéancier ou adaptation de retenues — DOM-012, actes à séparer | Position sur dette, ressources/charges utiles, retenues, paiements et demande ; options expliquées puis brouillon de l'option choisie | Régime de remise, retenue/compensation et effets d'une reconnaissance ou demande | Dette admise et difficultés / dette contestée ou incertaine : pas de remise automatique ni renonciation présumée |
| IN05 | Lire une contrainte de récupération — DOM-012 | Acte intégral, émetteur, signification/notification, preuve, dette et démarches ; urgence, voie d'opposition et dossier pour avocat | Texte de contrainte propre au régime, juridiction et forme d'opposition | Contrainte France Travail / acte de saisie : relais [DOM-003](../dom-003-commissaires-justice-execution.md) à vérifier, pas de délai générique |
| CT01 | Préparer un contrôle et des observations — DOM-012 | Convocation, demande/pouvoirs invoqués, périodes, pièces, rapport et réponse ; inventaire proportionné et observations factuelles | Textes/charte du contrôle CAF/MSA/France Travail identifié | Colocation ou flux discuté / documents manquants : expliquer prochaine démarche sans conseiller une fausse pièce |
| CT02 | Lire une pénalité ou qualification de fraude — DOM-012 pour administratif | Griefs, observations, preuve de notification, décision et qualification ; défense factuelle et recours distincts de l'indu | Régime des pénalités, contradiction et jurisprudence ; volet pénal [DOM-002](../dom-002-police-penal.md) | Erreur rectifiée / poursuite pénale annoncée : avocat, pas de fraude déduite d'un score |
| RC01 | Qualifier puis préparer le recours propre à une décision — DOM-012 | Prestation, auteur, acte, réception, recours précédents et accusés ; voie préalable, silence, juge, acte et calendrier à sourcer | Textes du régime et procédures, pas de recours universel CAF/France Travail | Prime d'activité et prestation familiale / intitulé CAF identique, circuits à vérifier séparément |
| RC02 | Examiner médiation et urgence de ressources — DOM-012 pour régime social | Recours, médiateur/territoire, pièces d'urgence, retenues et échéances ; deux calendriers et orientation motivée | Textes de médiation et urgence, procédure civile/administrative selon décision | Médiation en cours / privation de ressources : aucune suspension générale présumée ; procédure à découper avec DOM-010 ou EXIST-006 selon juge |

Les références abrégées « DOM-012 » dans la table renvoient au [cadrage principal](../dom-012-protection-sociale.md). L'ACRE et les cotisations de l'activité restent DOM-039 ; ARE/ARCE/ATI et décisions de caisse restent DOM-012. La fiscalité personnelle de l'ARCE relève de [DOM-011](../dom-011-fiscalite.md). Prêt/garantie bancaire et médiation du crédit → [BNK-018](../suites/bnk-018-financement-professionnel.md), sans y assimiler une subvention ou un prêt d'honneur. La contractualisation privée avec un organisme de formation → [DOM-027](../dom-027-education-formation.md), distincte du financement/rémunération FD02.

Attestation employeur → [TRAV-021](../../01-pilote-travail/suites/trav-021-pieces-fin-contrat.md), données de paie/DSN → [TRAV-020](../../01-pilote-travail/suites/trav-020-anomalie-dsn.md), rupture volontaire → [TRAV-049](../../01-pilote-travail/suites/trav-049-depart-volontaire.md), effets contractuels du CSP → [TRAV-050](../../01-pilote-travail/suites/trav-050-rupture-economique-individuelle.md). Fixation/révision de pension et désaccord familial → [DOM-013](../dom-013-famille-patrimoine.md), exécution forcée → [DOM-003](../dom-003-commissaires-justice-execution.md). Garantie privée de prévoyance → [INS-009](../suites/ins-009-complementaire-sante.md), obligation employeur → [PILOTE-001](../../01-pilote-travail/pilote-001-inventaire-travail.md), tâches à préciser. Statuts public, intermittent ou pension militaire sont à qualifier vers DOM-037/042/044, sans appliquer le régime salarié ordinaire par défaut.

Données erronées et automatisation → [PRV-001](../../02-plugins-existants/suites/prv-001-preparer-demande-acces.md), [PRV-022](../../02-plugins-existants/suites/prv-022-demande-rectification.md), [PRV-031](../../02-plugins-existants/suites/prv-031-decision-automatisee.md) ; qualification éventuelle du système → [IA-003](../../02-plugins-existants/suites/ia-003-pratiques-interdites.md)/[IA-004](../../02-plugins-existants/suites/ia-004-qualification-haut-risque.md). Les faits justifiant ces relais doivent être recueillis ; le recours contre la décision de prestation reste indépendant.

## Matrice des 185 frictions

Chaque code renvoie à la tâche, à son propriétaire et à ses sources ci-dessus. « À découper » s'applique à toutes les tâches candidates ; les relais vers des stories existantes restent des propositions d'implémentation.

| Point | Friction du guide | Tâche ou relais | Résultat à prévoir |
|---|---|---|---|
| 1 | Inscription tardive | FT01 | Dates de fin et inscription, pièces reçues et droit demandé ; ne pas attendre une attestation pour identifier la démarche. |
| 2 | Attestation employeur erronée | FT01 | Rapprocher dates, salaires et motif avec les pièces ; correction employeur TRAV-021 distincte de la décision ARE. |
| 3 | Attestation non transmise | FT01 | Brouillon de relance employeur TRAV-021 et signalement du manque au service instructeur, avec preuves séparées. |
| 4 | Mauvais motif de rupture | FT01 | Conserver motif de l'attestation, acte de rupture et contradictions ; qualification contractuelle vers travail. |
| 5 | Démission supposée indemnisable | FT01 | Examiner conditions et exceptions du régime avant toute conclusion ; TRAV-049 garde le départ. |
| 6 | Démission-reconversion mal préparée | FT01 | Dater CEP, validation, démission et inscription ; pas de régularisation ou de droit ARE supposé acquis. |
| 7 | Période d'affiliation mal calculée | FT01, FT02 | Lister contrats et périodes particulières retenus/omis et demander le détail de l'affiliation. |
| 8 | Salaire journalier de référence défavorable | FT02 | Rapprocher périodes travaillées/non travaillées, assiette et plafonnements à vérifier, sans garantir un recalcul favorable. |
| 9 | Ancien reliquat de droits | FT04 | Comparer notification de reprise et nouveaux éléments ; examiner option et conséquences avant choix. |
| 10 | Rechargement non déclenché | FT04 | Rapprocher emplois déclarés, justificatifs et périodes retenues pour demander le réexamen. |
| 11 | Différé d'indemnisation | FT03 | Distinguer chaque différé à partir du solde, de la rupture et du décompte organisme. |
| 12 | Délai d'attente de 7 jours | FT03 | Obtenir l'historique du délai d'attente et sa règle d'application ; aucun nombre de jours adopté ici. |
| 13 | Confusion sur la durée des droits | FT02 | Séparer durée notifiée, jours consommés et calendrier des paiements. |
| 14 | Dégressivité de l'ARE | FT02 | Identifier date, âge et régime de dégressivité retenus ; questions sur déclenchement et exceptions. |
| 15 | Droit à l'ARE supposé automatique | FT01 | Énumérer conditions vérifiées et manquantes ; travail antérieur seul ne vaut pas ouverture. |
| 16 | Oublier l'actualisation | FT05 | Conserver calendrier applicable, preuve d'oubli et décision ; correction/réinscription à qualifier. |
| 17 | Croire que l'actualisation est inutile sans allocation | FT05 | Vérifier si la personne est soumise à actualisation et tracer les emplois même sans paiement. |
| 18 | Ne pas déclarer quelques heures d'intérim | FT05 | Dater mission et déclaration, joindre justificatifs, distinguer correction et indu éventuel. |
| 19 | Déclarer un salaire dans le mauvais mois | FT05 | Rapprocher mois de travail, salaire et rubrique ; ne pas transposer le mois d'une autre prestation. |
| 20 | Ne pas signaler un arrêt maladie | FT05, SA01 | Comparer dates d'arrêt, ARE et IJ ; démarches séparées France Travail/caisse. |
| 21 | Oublier une formation | FT05, FD02 | Relever entrée, validation et statut formation, puis distinguer actualisation et rémunération. |
| 22 | Absence ou séjour à l'étranger non déclaré | FT05 | Documenter absence et disponibilité ; rechercher règle et exceptions du statut avant sanction. |
| 23 | Convocation reçue seulement dans l'espace personnel | FT07 | Recueillir dépôt dans l'espace, alertes et réception alléguée ; aucune notification régulière présumée. |
| 24 | Absence justifiée trop tardivement | FT07 | Chronologie du motif, justificatif et réponse ; observations avant ou contre la décision selon stade. |
| 25 | Reprise d'emploi déclarée de manière incomplète | FT05 | Relire statut souhaité, emploi et déclaration ; questions sur poursuite d'inscription et paiement. |
| 26 | Activité non salariée non déclarée | FT05, CR04 | Création, activité et revenus distingués ; déclaration omise ne prouve pas seule une fraude. |
| 27 | Réponse inexacte à une question d'actualisation | FT05 | Comparer copie validée, réalité et accusé ; brouillon de rectification factuelle. |
| 28 | Contrat d'engagement trop restrictif | FT06 | Reprendre contraintes concrètes et demander adaptation documentée du contrat. |
| 29 | Offre raisonnable d'emploi mal définie | FT06 | Lire critères de l'offre et contrat ; ne pas qualifier raisonnable sur le seul intitulé. |
| 30 | Refus de deux offres raisonnables | FT06, FT07 | Conserver chaque offre, dates et motifs de refus ; régime de sanction à vérifier. |
| 31 | Absence à un atelier obligatoire | FT07 | Vérifier caractère obligatoire, information et motif d'absence, puis demande d'adaptation. |
| 32 | Recherches d'emploi non prouvées | FT07 | Inventorier candidatures, réponses, entretiens et provenance sans inventer de démarches. |
| 33 | Convocation impossible à honorer | FT06, FT07 | Préparer demande de report avec motif et preuve ; pas de dispense supposée accordée. |
| 34 | Sanction sans prise en compte des justificatifs | FT07 | Comparer observations transmises, réception et motifs réellement examinés. |
| 35 | Confusion entre suspension et suppression | FT07 | Expliquer nature, période, reprise et arriérés à vérifier pour chaque mesure. |
| 36 | Médiation prise pour un recours juridictionnel | RC01, RC02 | Tenir calendriers médiation et recours propres ; effet de chaque acte à rechercher. |
| 37 | Penser que le RSA est automatique | RS01 | Identifier demande, dépôt et conditions ; simulation distincte du droit ouvert. |
| 38 | Confondre absence de revenu et droit au RSA | RS01 | Qualifier âge, foyer, séjour, résidence et ressources sans réduire le droit au seul revenu. |
| 39 | Ressources du conjoint ignorées | RS01 | Recueillir situation réelle et revenus du foyer ; ne pas assimiler mariage et seul critère de couple. |
| 40 | Confondre colocation et concubinage | RS01, CT01 | Réunir faits de logement/vie commune sans déduire le concubinage du seul partage d'adresse. |
| 41 | Hébergement gratuit | RS01 | Documenter hébergement et forfait retenu ; demander sa base et son champ. |
| 42 | Épargne non renseignée | RS01 | Distinguer capital, produits d'épargne et règle de prise en compte ; pas de forfait universel. |
| 43 | Don familial confondu avec une ressource régulière | RS01 | Qualifier origine, objet et fréquence des transferts avec pièces ; pas de revenu déduit de tout virement. |
| 44 | Revenus exceptionnels mal imputés | RS01 | Dater versement, nature et période imputée ; demander le fondement de l'affectation. |
| 45 | Perte récente d'emploi | RS01 | Documenter perte d'emploi et revenus retenus ; neutralisation/abattement à rechercher selon situation. |
| 46 | Patrimoine immobilier oublié | RS01 | Identifier bien, usage et revenus ; traitement propre au régime à vérifier. |
| 47 | Revenus étrangers non déclarés | RS01 | Documenter ressources étrangères, nature et période ; ne pas transposer la règle fiscale. |
| 48 | Départ prolongé à l'étranger | RS01 | Établir calendrier des séjours, résidence et exceptions ; ne pas reprendre une durée uniforme du guide. |
| 49 | Séparation non signalée | RS01 | Conserver date et faits de séparation, déclaration et décision de majoration éventuelle. |
| 50 | Reprise d'activité indépendante | RS01, CR04 | Identifier régime indépendant et méthode retenue par chaque organisme ; pas de revenu commun automatique. |
| 51 | Recevoir des convocations de plusieurs organismes | RS02 | Identifier référent effectif, auteurs et objets des convocations ; demande de coordination. |
| 52 | Se voir attribuer des engagements inadaptés | RS02 | Distinguer besoins et justificatifs utiles ; préparer adaptation selon santé, garde et obstacles sociaux. |
| 53 | Confondre activité d'insertion et emploi salarié | RS02 | Lire action et cadre juridique ; rémunération et contrat salarié à qualifier séparément si faits utiles. |
| 54 | Ne pas obtenir de copie du contrat | RS02 | Demander copie/version du contrat et preuve de remise, sans reconstruire un accord supposé. |
| 55 | Manquer une action faute d'information claire | RS02 | Rassembler information reçue, date, lieu et justification demandée ; questionner l'obligation exacte. |
| 56 | Ne pas signaler l'impossibilité de respecter un engagement | RS02 | Préparer signalement d'empêchement et demande d'adaptation avec preuve. |
| 57 | Subir une suspension du RSA pour manquement | RS02 | Distinguer manquement, suspension et conditions éventuelles de reprise/régularisation. |
| 58 | Croire que toute sanction entraîne automatiquement une radiation définitive | RS02 | Identifier mesure exacte et durée sans assimiler suspension à radiation définitive. |
| 59 | Ignorer les garanties de procédure | RS02, CT02 | Comparer griefs, observations, décision et garanties procédurales propres. |
| 60 | Contester auprès du mauvais organisme | RS02, RC01 | Distinguer service payeur, décideur et destinataire du recours RSA. |
| 61 | Penser gagner trop pour y avoir droit | PA01 | Préparer données d'une simulation puis demande, sans annoncer d'éligibilité sur le seul salaire. |
| 62 | Croire que la prime est attribuée à tous les travailleurs | PA01 | Inventorier ressources et situation du foyer selon champ de la prestation. |
| 63 | Déclarer le net payé à la place du net social | PA01 | Comparer net social, net payé et rubrique ; correction de paie/DSN vers TRAV-020 si nécessaire. |
| 64 | Se fier aveuglément aux cases préremplies | PA01 | Vérifier chaque donnée préremplie contre sa pièce et tracer demande de correction. |
| 65 | Mauvais mois de rattachement du salaire | PA01 | Distinguer période de travail, versement et mois déclaré ; rechercher le rattachement applicable. |
| 66 | Confondre revenu et chiffre d'affaires | PA01 | Identifier CA, revenu et régime ; préparer rubriques indépendantes sans assimiler au net salarial. |
| 67 | Mauvaise catégorie de chiffre d'affaires | PA01 | Qualifier activité réelle et mixte, catégorie et instruction du formulaire ; pas d'abattement appliqué d'office. |
| 68 | Oublier les revenus du conjoint | PA01 | Rapprocher composition du foyer et ressources de chaque membre concerné. |
| 69 | Omettre les pensions alimentaires | PA01 | Qualifier pension et autre ressource avec justificatifs et règles propres. |
| 70 | Croire que le droit suit immédiatement les revenus | PA01 | Expliquer décalage entre période retenue et revenus actuels avec questions de réexamen. |
| 71 | Oublier la déclaration trimestrielle | PA01 | Conserver demande, échéance et accusé ; rappel seulement proposé, pas créé. |
| 72 | Croire qu'une demande refusée ne mérite jamais d'être renouvelée | PA01 | Identifier changement depuis refus, nouvelle demande possible et recours distinct sur l'ancien refus. |
| 73 | Croire l'ACRE automatique | CR01 | Vérifier si demande exigée pour statut/date ; preuve de dépôt, pas d'automaticité supposée. |
| 74 | Rater les 60 jours | CR01 | Dater ouverture, demande et réception ; délai et transitions à rechercher. |
| 75 | Confondre ACRE et ARCE | CR01, CR02 | Séparer exonération de cotisations et aide en capital, leurs autorités et conditions. |
| 76 | Utiliser un ancien taux d'exonération | CR01 | Vérifier texte/version et taux appliqué aux cotisations concernées ; pas de taux ancien repris. |
| 77 | Créer sans vérifier l'éligibilité | CR01 | Documenter statut, critères et aides antérieures avant conclusion d'éligibilité. |
| 78 | Créer en fin de trimestre civil | CR01 | Distinguer date choisie, début réel et période d'exonération ; aucune date optimale prescrite sans examen. |
| 79 | Ne pas conserver l'accusé de dépôt | CR01 | Inventorier preuve de dépôt et réception ; demander duplicata ou statut sans prétendre dépôt prouvé. |
| 80 | Ne pas suivre la réponse de l'Urssaf | CR01 | Rapprocher réponse Urssaf, période et taux effectivement appelé. |
| 81 | Créer l'entreprise avant d'avoir sécurisé ses droits ARE | CR02 | Chronologie fin de contrat, inscription, ouverture, création et demande à vérifier avant choix. |
| 82 | Demander l'ARCE sans avoir obtenu l'ACRE | CR02 | Recueillir demande/décision ACRE et conditions ARCE sans annoncer l'attribution. |
| 83 | Choisir l'ARCE sans comparer au maintien de l'ARE | CR02 | Comparer qualitativement flux, risque, conditions et besoins, avec montants réservés si non vérifiés. |
| 84 | Confondre ARCE et avance remboursable | CR02 | Expliquer nature et conditions du capital distinctes d'un prêt, sans promesse de non-restitution universelle. |
| 85 | Anticiper le second versement comme garanti | CR03 | Lister justificatifs de poursuite et conditions de seconde fraction aux dates pertinentes. |
| 86 | Ne pas provisionner la fiscalité | CR03 | Séparer versement et traitement fiscal personnel ; relais DOM-011, aucune simulation fiscale ici. |
| 87 | Croire que les 40 % de droits restants sont toujours immédiatement disponibles | CR03 | Identifier droits non versés, cessation/emploi et conditions de reprise, sans disponibilité immédiate promise. |
| 88 | Ignorer le délai de déchéance des droits ARE | FT04, CR03 | Dater ouverture, durée et événements de prolongation éventuels avant examen de déchéance. |
| 89 | Croire que le maintien de l'ARE dure systématiquement jusqu'à épuisement de tous les droits | CR04 | Identifier date et règles du cumul, droits consommés et plafond éventuel ; pas de maintien intégral garanti. |
| 90 | Ignorer la possibilité de saisir l'instance paritaire régionale (IPR) | CR05 | Vérifier conditions et pièces d'une demande IPR, distincte d'un recours contre une erreur de calcul. |
| 91 | Rater le délai de demande auprès de l'IPR | CR05 | Établir événement de plafond et date prouvée avant calcul du terme de demande. |
| 92 | Déclarer incorrectement les revenus indépendants | CR04 | Rapprocher revenus provisoires/définitifs, rubriques et justificatifs du statut exact. |
| 93 | Confondre chiffre d'affaires, bénéfice et rémunération du dirigeant | CR04 | Séparer CA, résultat et rémunération avec pièces ; activité/régime vers DOM-039, société vers EXIST-002 si utile. |
| 94 | Ignorer les paiements provisoires et régularisations | CR04 | Comparer avances, décomptes définitifs et régularisation ; ne pas confondre paiement provisoire et droit acquis. |
| 95 | Croire qu'une SASU sans salaire empêche toute difficulté | CR04 | Documenter activité et rémunération du dirigeant ; zéro salaire ne vaut pas zéro obligation. |
| 96 | Commencer un investissement avant l'accord de financement | CR06 | Comparer demande, autorisation et date d'engagement/paiement de chaque dépense. |
| 97 | Confondre accord de principe et attribution définitive | CR06 | Lire portée et réserves de l'accord ; décision formelle et versement distincts. |
| 98 | Oublier les critères de maintien de l'activité | CR06 | Lister engagements, durée, preuves et conséquence de cessation selon convention. |
| 99 | Ne pas remplir les obligations de publicité ou de justification | CR06 | Préparer liste des factures, paiements et obligations d'information/publicité propres à l'aide. |
| 100 | Confondre subvention, avance remboursable, prêt d'honneur et garantie bancaire | CR06 | Qualifier subvention, avance, prêt d'honneur et garantie ; prêt bancaire vers BNK-018 seulement si pertinent. |
| 101 | Ne pas vérifier les cumuls d'aides | CR06 | Inventorier aides déjà obtenues et assiettes ; rechercher incompatibilités/plafonds du dispositif exact. |
| 102 | Croire que les aides régionales sont identiques partout | CR06 | Identifier région, appel, financeur et version ; pas d'aide régionale nationale par analogie. |
| 103 | Rater une date de dépôt | CR06 | Distinguer date de dépôt, complétude, enveloppe et décision ; conserver accusés. |
| 104 | Ne pas vérifier les clauses de remboursement | CR06 | Lire engagements, dépenses rejetées et demande de restitution ; contestation à découper séparément. |
| 105 | Fermer son entreprise en pensant percevoir automatiquement l'ATI | CR07 | Qualifier motif de cessation et critères ATI avant conclure à un relais. |
| 106 | Ne pas faire attester la non-viabilité économique | CR07 | Identifier nécessité, auteur habilité et contenu de l'attestation ; comptabilité non reconstituée par le plugin. |
| 107 | Confondre ATI et anciens droits ARE | CR07, FT04 | Comparer conditions ATI et reliquat ARE, sans transfert automatique des règles. |
| 108 | Oublier les régularisations Urssaf après cessation | CR08 | Dernières déclarations et régularisations de cotisations vers DOM-039 ; radiation distincte d'extinction de dette. |
| 109 | Demande déposée trop tard | LG01 | Établir entrée, demande et preuve ; vérifier ouverture et rétroactivité du dispositif identifié. |
| 110 | Croire que le premier mois est toujours indemnisé | LG01 | Séparer mois d'entrée, ouverture et premier paiement ; exemple du guide non adopté comme règle. |
| 111 | Confondre loyer total et loyer retenu | LG01 | Comparer loyer réel, assiette, charges et zone retenus sans calcul d'aide improvisé. |
| 112 | Ne pas déclarer une modification de loyer | LG01 | Dater modification et justificatif ; demande de correction auprès de la caisse. |
| 113 | Erreur sur les ressources des 12 mois de référence | LG01 | Rapprocher période et nature des ressources retenues ; pas de fenêtre de référence commune aux aides. |
| 114 | Changement de situation professionnelle non pris en compte | LG01 | Dater changement professionnel et décision ; vérifier mécanisme de prise en compte. |
| 115 | Paiement direct au propriétaire mal compris | LG02 | Comparer destinataire, date de paiement caisse et imputation dans le compte locatif. |
| 116 | Bailleur ne déduisant pas l'APL reçue | LG02 | Écart documenté et brouillon au bailleur via DOM-006 ; décision caisse conservée séparément. |
| 117 | Attestation de loyer erronée | LG01, LG02 | Comparer attestation et bail, demander correction au bailleur puis réexamen caisse. |
| 118 | Changement de logement non déclaré | LG01 | Distinguer déclaration du départ et nouvelle demande pour le logement d'accueil. |
| 119 | Impayé de loyer | LG02 | Qualifier impayé, signalement, plan et décision sur aide ; pas de suppression immédiate présumée. |
| 120 | Logement non décent | LG02 | Distinguer constat/démarche de décence et conservation ou paiement de l'aide ; bail vers DOM-006. |
| 121 | Confusion sur la résidence principale | LG01 | Établir occupation réelle et condition de résidence propre à la prestation. |
| 122 | Fin de l'ARE sans vérification de l'ASS | FD01 | Préparer examen ASS avant fin ARE avec ressources et activité antérieure. |
| 123 | Ne pas examiner le RSA lorsque l'ASS est refusée | FD01, RS01 | Refus ASS distinct d'une demande RSA ; critères et interlocuteurs propres. |
| 124 | Croire que RSA et ASS sont totalement cumulables | FD01 | Rapprocher prestations et ressources pour cumul/différentiel à vérifier, sans cumul intégral promis. |
| 125 | Perdre son indemnisation pendant une formation | FD02 | Distinguer statut en formation, droits restants et relais de rémunération selon dates. |
| 126 | Commencer une formation sans validation de France Travail | FD02 | Séparer accord pédagogique, financement et allocation pendant la formation. |
| 127 | Payer soi-même une formation en pensant obtenir ensuite un remboursement | FD02 | Lire engagement, date et accord de financement ; remboursement non garanti, contrat vers DOM-027. |
| 128 | Oublier les aides à la mobilité | FD03 | Identifier événement, frais et dispositif mobilité actuel ; pièces selon aide exacte. |
| 129 | Rater le délai d'aide à la mobilité pour une reprise d'emploi | FD03 | Dater embauche, demande et justificatifs ; chaque échéance à sourcer séparément. |
| 130 | Ignorer les aides à la garde d'enfants | FD03, JF02 | Identifier organisme et aide de garde selon reprise/formation ou prestation familiale ; pas d'aide commune supposée. |
| 131 | Se fier à une ancienne aide au permis B | FD03 | Vérifier existence du dispositif, suppression alléguée et transitions ; aucune ancienne aide recommandée par défaut. |
| 132 | Licenciement économique et CSP mal compris | FT01, FT03 | Prestation du CSP ici ; réception, adhésion et effets sur préavis chez TRAV-050. |
| 133 | Accepter un CSP en pensant renoncer à toute contestation du licenciement | RC01 | Ne pas confondre contestation du licenciement TRAV-050 et contestation d'une décision de prestation. |
| 134 | Premier accès à l'ARE refusé sur la base d'une période de six mois sans examen de l'exception | FT01 | Examiner statut de primo-entrant, périodes, date de fin et transition de l'exception alléguée. |
| 135 | Contrat d'engagement jeune confondu avec une allocation automatique | JF01 | Lire contrat, opérateur et conditions de l'allocation sans automaticité. |
| 136 | Cumul CEJ/RSA/ARE mal anticipé | JF01 | Rapprocher CEJ et autres prestations ; rechercher chaque incompatibilité ou déduction. |
| 137 | Absence injustifiée à une action du CEJ | JF01 | Griefs, information et justificatifs avant lecture de sanction propre au CEJ. |
| 138 | Ne pas vérifier les aides pour parent isolé | JF02, RS01 | Identifier ASF, majoration RSA, garde et prestations séparément, avec demandes propres. |
| 139 | Confondre pension alimentaire impayée et absence de recours | JF02 | Distinguer service ARIPA, ASF et intermédiation de la fixation/révision DOM-013 et saisie DOM-003. |
| 140 | Oublier de signaler une naissance, une séparation ou un décès | JF02 | Lister organismes affectés et changements déclarés avec preuve ; pas de mise à jour générale supposée. |
| 141 | Croire que toutes les prestations familiales sont rétroactives | JF02 | Rechercher date d'effet et rétroactivité de chaque prestation, sans règle familiale unique. |
| 142 | Ne pas vérifier les indemnités journalières CPAM | SA01 | Distinguer affiliation/cotisation, période, attestation et calcul contesté ; administrative/médicale à qualifier. |
| 143 | Confondre arrêt maladie et indemnisation automatique | SA01 | Arrêt médical et conditions de paiement séparés ; pièces manquantes et motif à demander. |
| 144 | Ignorer la prévoyance collective ou individuelle | SA01 | IJ caisse ici ; garantie privée INS-009, maintien/obligation employeur vers travail, sans double indemnisation promise. |
| 145 | Ne pas vérifier la complémentaire santé solidaire (C2S) | SA02 | Vérifier régime C2S, situation RSA et opposition/décision ; ne pas assimiler à mutuelle privée. |
| 146 | Confondre décision médicale et décision administrative pour l'AAH | SA03, RC01 | Identifier auteur et objet : reconnaissance handicap chez DOM-025, paiement/ressources caisse chez DOM-012. |
| 147 | Ne pas renouveler suffisamment tôt une reconnaissance ou une allocation liée au handicap | SA03 | Dater fin de validité, dépôt et réception ; continuité/renouvellement propres à chaque droit. |
| 148 | Ignorer les aides du CCAS et du conseil départemental | SA04 | Repérer territoire, besoin urgent, CCAS/département et règlement actuel ; aucune aide garantie. |
| 149 | Confondre subvention et prêt FSL | SA04 | Lire règlement local et décision FSL : prêt, subvention, objet et remboursement distingués. |
| 150 | Croire qu'une erreur de l'administration annule automatiquement la dette. C'est faux | IN01 | Examiner fondement de dette et erreur alléguée ; aucune annulation automatique déduite de la faute de caisse. |
| 151 | Recevoir un indu sans décompte exploitable. Demander le détail mois par mois, avec les ressources retenues et les règles appliquées | IN01 | Demander décompte mois/prestation/ressource et pièces de calcul exploitables. |
| 152 | Se voir réclamer une période déjà prescrite. Vérifier la prestation concernée, la date de chaque paiement et les événements susceptibles d'avoir interrompu la prescription | IN02 | Chronologie des paiements et événements pertinents avant conclusion sur prescription. |
| 153 | Confondre prescription du droit de réclamer et prescription du recouvrement. Les règles peuvent être différentes après une notification ou l'établissement d'un titre de recouvrement | IN02 | Séparer récupération, titre et recouvrement ; règle de chaque phase à rechercher. |
| 154 | Accepter un calcul global sans vérifier les prestations distinctes. Une même erreur peut générer plusieurs indus, dont les bases et montants doivent être contrôlés séparément | IN01 | Éclater chaque prestation et période, même si la cause factuelle est commune. |
| 155 | Subir des retenues sur les allocations suivantes. La CAF peut récupérer certaines dettes directement sur les prestations versées | IN04 | Identifier retenue, dette imputée, notification et prestation affectée ; mécanisme à vérifier. |
| 156 | Croire que des ressources très faibles interdisent toute récupération. Il faut examiner les règles de retenue et demander leur adaptation lorsque c'est possible | IN04 | Ressources/charges et barème applicable avant demande d'adaptation, sans immunité automatique. |
| 157 | Ne pas solliciter un échéancier. Le remboursement en plusieurs fois peut éviter une aggravation de la situation financière | IN04 | Préparer demande d'échéancier choisi et conséquences à vérifier séparément de la contestation. |
| 158 | Demander une remise de dette alors qu'on en conteste le principe. C'est un piège majeur | IN03, IN04 | Demander position sur dette ; vérifier effets d'une remise sans présenter toute demande comme reconnaissance universelle. |
| 159 | Confondre remise gracieuse et droit à l'erreur. La bonne foi peut être importante pour les sanctions, mais elle n'annule pas automatiquement les sommes versées à tort | IN04, CT02 | Distinguer droit à l'erreur, bonne foi, sanction, dette et conditions de remise. |
| 160 | Laisser passer le délai de contestation en discutant au téléphone. Une conversation téléphonique ne remplace pas le recours formel requis | IN03, RC01 | Conserver échanges téléphoniques mais identifier acte formel et terme propres. |
| 161 | Recevoir une contrainte et ne pas former opposition. Pour certaines contraintes de France Travail, le délai d'opposition est de seulement 15 jours | IN05 | Contrainte intégrale et réception en tête, avocat et opposition propre au régime ; pas de délai transposé. |
| 162 | Ne pas distinguer erreur et fraude. La qualification de fraude peut entraîner des pénalités, des délais de récupération plus longs et des restrictions concernant les remises de dette | IN02, CT02 | Établir qualification, griefs et preuves avant effets allégués sur prescription, pénalité et remise. |
| 163 | Croire qu'un contrôle nécessite toujours un soupçon de fraude | CT01 | Identifier type et stade du contrôle sans présumer une suspicion ou une fraude établie. |
| 164 | Ne pas répondre à une demande de justificatifs | CT01 | Inventorier documents demandés, terme, motif et manques ; réponse ou difficulté tracée. |
| 165 | Refuser un contrôle en pensant exercer un droit absolu au silence | CT01 | Rechercher pouvoirs, garanties et conséquences propres ; aucun droit absolu de refus conseillé. |
| 166 | Ignorer le droit d'être accompagné lors d'un contrôle CAF sur place | CT01 | Vérifier accompagnement possible, charte et régime du contrôle sur place, sans généralisation à tous organismes. |
| 167 | Confondre colocataire et conjoint | CT01, RS01 | Répondre sur faits de vie commune avec ensemble d'indices, sans qualification à partir d'un seul bail. |
| 168 | Voir un virement bancaire qualifié automatiquement de revenu | CT01 | Classer flux avec preuve d'origine/objet ; remboursement ou transfert non assimilé d'office au revenu. |
| 169 | Avoir des comptes bancaires que l'administration ne connaît pas | CT01 | Qualifier périmètre, pertinence et régime de communication ; limiter données au nécessaire sans conseiller dissimulation. |
| 170 | Faire confiance aux échanges automatisés | CT01, PA01 | Documenter source de donnée et correction ; paie/DSN TRAV-020 ou donnée PRV-022 selon demande. |
| 171 | Ne pas conserver ses anciennes déclarations | CT01 | Inventorier versions de déclarations, dates et accusés pour chaque période recalculée. |
| 172 | Se voir reprocher une incohérence entre deux organismes | CT01 | Comparer définitions et périodes propres à chaque organisme ; pas d'incohérence déduite du seul montant différent. |
| 173 | Corriger une erreur sans garder de preuve | CT01 | Conserver version initiale, correction et preuve de réception ; correction distincte du recours contre décision. |
| 174 | Confondre sélection algorithmique pour contrôle et preuve de fraude | CT01, CT02 | Score de contrôle distinct de preuve de fraude ; données/automatisation vers PRV-001/022/031, IA si faits utiles. |
| 175 | Ne pas faire valoir ses observations avant une sanction | CT02 | Dater griefs, possibilité d'observations et réponse avant sanction ; garanties propres à vérifier. |
| 176 | Ne pas contester des conclusions factuellement inexactes | CT01, CT02 | Réponse point par point aux constatations avec pièces, contradictions conservées. |
| 177 | Envoyer de faux justificatifs pour débloquer un dossier | CT01, CT02 | Proposer demande de duplicata, explication ou délai ; aucune fausse pièce, volet pénal DOM-002 si nécessaire. |
| 178 | Envoyer une simple réclamation alors qu'un recours administratif préalable obligatoire est nécessaire | RC01 | Identifier recours préalable exigé, destinataire et forme ; simple messagerie non assimilée d'office. |
| 179 | Attendre la réponse du médiateur en croyant que tous les délais de justice sont suspendus | RC02 | Vérifier effet de médiation pour chaque échéance, conserver recours parallèles nécessaires. |
| 180 | Contester une notification sans préciser sa référence, sa date et les motifs du désaccord | RC01 | Brouillon identifiant référence, décision, réception, désaccords et pièces sans inventer de faits. |
| 181 | Saisir le mauvais tribunal | RC01 | Qualifier objet/régime avant juridiction ; logo de l'organisme insuffisant. |
| 182 | Ignorer qu'une absence de réponse peut constituer un rejet implicite | RC01 | Dater dépôt complet et réception, rechercher régime du silence et suite contentieuse. |
| 183 | Ne pas conserver la preuve du dépôt du recours | RC01 | Distinguer envoi, dépôt, réception et complétude ; conserver justificatif de chaque acte. |
| 184 | Supposer qu'un second recours identique relance automatiquement tous les délais | RC01 | Comparer actes et décisions ; aucun redémarrage automatique du calendrier après relance identique. |
| 185 | Ne pas demander la suspension d'une décision par la voie appropriée lorsqu'une urgence financière grave le justifie. Un recours ordinaire n'est pas automatiquement suspensif | RC02 | Documenter urgence vitale/financière et voie appropriée devant juge compétent, sans suspension ordinaire présumée. |

## Affirmations et nouveautés à vérifier

Ces mentions décrivent les assertions du guide et les recherches exigées ; elles ne sont pas adoptées comme règles. Lire texte exact, version, champ, transitions et exceptions, puis confronter les faits. Favicons, noms d'organismes et mentions « +1 » ne constituent pas des citations exploitables. Sources officielles à ouvrir pendant chaque implémentation selon BASE-005/010.

| Assertion du guide | Recherche exigée | Tâches |
|---|---|---|
| Attente ARE, différés, inscription maximale, durée et dégressivité | Régime de l'ouverture, événement pertinent, application antérieure de l'attente, indemnités et transitions ; droit et paiement distincts | FT01–FT04 |
| Réforme des sanctions en 2025 et reprise après remobilisation | Textes France Travail et RSA séparés, autorité, graduation, contradiction, reprise et arriérés | FT07, RS02 |
| Inscription RSA et référence hebdomadaire d'activité depuis 2025 | Champ, contrat/référent, adaptations, exemptions et nature des actions ; aucun travail gratuit uniforme déduit | RS02 |
| Préremplissage depuis mars 2025, mois M-2 à M-4 et exemple d'octobre | Prestation, déploiement du régime/organisme, période demandée, revenu de référence, versement et correction ; pas de transposition à ARE ou logement | PA01, RS01 |
| Réforme de prime d'activité annoncée au printemps 2026 | Texte, date pertinente, paramètres et transition ; calcul distinct à cadrer si retenu | PA01 |
| Abattements micro et saisie du CA brut en ligne | Régime, activité réelle/mixte, rubrique et canal, assiette et qui applique l'abattement ; pas d'abattement appliqué deux fois ni de transposition au réel | PA01, RS01, DOM-039 |
| Réforme ACRE de juillet 2026 et délai de demande | Texte publié, statut, création/reprise, taux/cotisations concernés, période et transitions | CR01 |
| ARCE : fraction de droits, retenues, versements, emploi repris et reliquat | Conditions de chaque fraction, ACRE, cessation, reprise et déchéance ; fiscalité personnelle séparée | CR02, CR03, DOM-011 |
| Cumul ARE/indépendant et demande IPR après plafond depuis 2025 | Droits concernés, plafond/assiette, revenus, notification et procédure/délai IPR | CR04, CR05 |
| ATI et attestation de non-viabilité | Motifs de cessation admis, activité et ressources, tiers habilité et articulation ARE | CR07 |
| Logement : période de ressources, premier mois et exemple de versement | Dispositif, entrée/demande, exceptions, effet/paiement, maintien/conservation lors d'impayé ou non-décence | LG01, LG02 |
| Aide au permis B supprimée en avril 2026 | Décision officielle, champ et demandes en cours ; autres aides séparées, sans ancien barème recommandé | FD03 |
| CSP : adhésion et maintien d'une contestation du licenciement | Réception, convention et documents ; délais distincts pour adhésion, rupture et prestation | TRAV-050, FT01, RC01 |
| Primo-entrants ARE : affiliation réduite depuis avril 2026 | Texte, entrée en vigueur, définition du public, dates de fin/engagement de rupture et exceptions | FT01 |
| C2S liée au RSA, CEJ et cumuls | Conditions et exceptions de chaque prestation, opposition et décisions ; pas d'automaticité transposée | SA02, JF01 |
| Remise présentée comme reconnaissance, bonne foi et erreur | Effet exact selon régime/acte, objet de la demande, contestation en cours et qualification ; ne pas déduire reconnaissance ou renonciation de toute demande | IN03, IN04, CT02 |
| Accompagnement, comptes bancaires et échanges lors du contrôle | Pouvoirs, pertinence et garanties du contrôle identifié ; pas de garantie CAF étendue par analogie à France Travail | CT01, CT02 |

## Les trois lignes de prescriptions du guide

Le tableau n'est pas exhaustif. RSA, logement, IJ, ATI ou autre prestation exigent leurs propres recherches. Séparer récupération, recouvrement après titre et délai de recours ; établir date et effet de chaque acte. Les durées du guide ne deviennent pas des règles validées.

| Ligne | Dette du tableau source | Résultat à rechercher |
|---|---|---|
| P01 | Prestations familiales CAF/MSA | IN02 : texte, départ par paiement, qualification fraude/fausse déclaration, interruption/suspension et titre éventuel |
| P02 | Prime d'activité CAF/MSA | IN02 : prescription propre et dérogation, sans importer le délai familial sur le seul logo CAF |
| P03 | Allocation chômage France Travail | IN02 : allocation exacte, qualification, récupération/recouvrement et actes antérieurs ; pas de généralisation aux autres aides France Travail |

## Les neuf lignes de voies de recours du guide

La table reprend les objets du tableau fourni ; voies et juges restent à vérifier avant brouillon. Demander décision, réception, recours précédents, territoire, éventuelle médiation préalable obligatoire et preuve de chaque dépôt. Confronter notification et texte applicable : sa lecture seule ne certifie ni compétence ni délai. Le lieu de dépôt ne suffit pas à identifier le décideur.

| Ligne | Décision à qualifier | Exigence de résultat futur |
|---|---|---|
| V01 | Prime d'activité | RC01 : voie préalable et juge propres, distincts des prestations familiales |
| V02 | RSA, attribution/montant/sanction | RS01/RS02 et RC01 : autorité départementale, délégations, recours et médiation locale éventuelle ; payeur distinct du décideur |
| V03 | APL, ALS, ALF | LG01 et RC01 : régime et décision exacte avant destinataire du préalable et juge |
| V04 | Prestations familiales CAF | JF02 et RC01 : prestation, commission éventuelle et contentieux propre |
| V05 | AAH, paiement par caisse | RC01 : ressources/calcul/paiement chez DOM-012, pas de recours contre reconnaissance non contestée |
| V06 | AAH, décision liée au handicap | SA03 chez DOM-025 : auteur MDPH/CDAPH, objet, préalable et juge selon droit demandé |
| V07 | Trop-perçu ARE | IN03/IN05 : notification de dette, décision sur recours et contrainte séparées ; forme/juridiction propres |
| V08 | Sanction France Travail | FT07 et RC01 : inscription, allocation et sanction exacte avant autorité et juge |
| V09 | IJ, refus administratif CPAM | SA01 et RC01 : vérifier caractère administratif ; décision médicale à requalifier avant choix CRA/CMRA et juge |

Allocation d'assurance chômage, aide publique et sanction d'inscription ne suivent pas nécessairement la même procédure. Contentieux spécialisé à découper chez DOM-012 avec [EXIST-006](../../02-plugins-existants/exist-006-contentieux.md) selon attribution ; urgence administrative avec DOM-010. Aucune opposition ou requête générale ne remplace ce travail.

## Les douze lignes du calendrier source

Le repère « France métropolitaine, octobre 2026 » ne prouve pas la version applicable aux faits. Rechercher chaque terme selon le contrat des réponses. La première ligne est un conseil d'organisation, pas un délai légal ajouté.

| Ligne | Démarche du calendrier | Propriétaire et vérification |
|---|---|---|
| D01 | S'inscrire après fin de contrat | FT01 : date de fin, dépôt, pièces et démarche utile |
| D02 | Faire valoir l'ouverture ARE dans le délai maximal | FT01 : événement, prolongations et admission au régime |
| D03 | Actualisation mensuelle | FT05 : calendrier officiel année/mois et obligation propre à la personne |
| D04 | Déclaration RSA/prime d'activité | RS01/PA01 : trimestre demandé, échéance et preuve |
| D05 | Adhésion au CSP | TRAV-050 : remise des documents, départ du délai et effets ; distinct de la contestation du licenciement |
| D06 | Aide mobilité après embauche | FD03 : demande puis justificatifs, échéances séparées |
| D07 | Demande ACRE | CR01 chez DOM-039 : statut, début d'activité, réforme et réception |
| D08 | Recours CAF/RSA/CPAM | RC01 : autant de calendriers que de décisions, préalables et régimes, sans délai commun |
| D09 | Contestation d'indu France Travail | IN03 : notification, objet et acte requis ; distinct de l'opposition à contrainte |
| D10 | Opposition à contrainte France Travail | IN05 : notification/signification réelle, forme, juge et urgence ; pas de délai transposé |
| D11 | Seconde fraction ARCE | CR03 : événement du premier versement, conditions et justificatifs ; paiement non garanti |
| D12 | Demande IPR après plafond de cumul | CR05 : plafond applicable, date établie, conditions et réception |

Les mentions hors calendrier — silence après recours, reprise/déchéance ARE, renouvellement handicap, date d'effet logement, prescription, rétroactivité familiale et contestation du licenciement — restent attachées à RC01, FT04/CR03, SA03, LG01, IN02, JF02 et TRAV-050. Elles ne doivent pas disparaître du calendrier individuel parce qu'elles manquent au tableau source.

## Les dix réflexes et le parcours après décision

| Ligne | Réflexe du guide | Exigence de sortie |
|---|---|---|
| R01 | Télécharger notifications et courriers | Inventaire disponible/manquant, sans accès au compte exigé |
| R02 | Garder accusés et justificatifs | Version, date, destinataire, dépôt et réception distingués |
| R03 | Vérifier périodes et revenus | Tableau par prestation, origine, mois et donnée contestée |
| R04 | Inscrire les dates limites | Calendrier avec fondement, événement, preuve et inconnues ; aucun rappel créé |
| R05 | Déclarer les changements | Organismes et démarches distincts, pas de propagation automatique présumée |
| R06 | Obtenir décision et motif écrits | Brouillon ciblé, sans attendre sa réponse pour identifier un recours urgent |
| R07 | Exercer le recours formel | Acte, destinataire et délai propres ; téléphone et explication distingués |
| R08 | Distinguer dette contestée et remise | Objectif/position de la personne, effets à vérifier avant choix |
| R09 | Examiner les aides complémentaires | FD01, SA02/04 et JF02 selon faits ; simulation séparée de dépôt et ouverture |
| R10 | Suivre recours, paiements et retenues | Tableau daté des actes et sommes avec preuve et prochaine action |

Les sept étapes après refus/suspension/indu deviennent un parcours de sortie : **A01** sauvegarder décision/annexes ; **A02** qualifier prestation, auteur et acte ; **A03** vérifier voie et calendrier ; **A04** demander détail et fondement ; **A05** préparer l'acte formel sans faire dépendre l'identification de l'urgence d'une réponse informelle ; **A06** garder dépôt/réception ; **A07** examiner parallèlement secours et mesure d'urgence. A05 exige de vérifier si et comment des pièces peuvent être complétées : ne pas promettre qu'un recours incomplet sera recevable ou conservera les droits. Ces étapes ne sont pas exécutées par ce lot.

Le choix interactif du guide devient une question dans IN01/03/04 : « je conteste », « j'admets mais ne peux payer » ou « je ne sais pas encore ». La troisième réponse conduit à obtenir pièces et calcul tout en identifiant l'acte formel urgent ; aucune reconnaissance ou remise préremplie.

## Services et limites de l'orientation

Les services cités sont des pistes à vérifier au moment de la réponse : Mes droits sociaux pour panorama/simulation ; Service Public pour information ; CAF/MSA, France Travail, caisse ou département pour instruction/décision selon régime ; Défenseur des droits pour les difficultés entrant dans ses missions ; France Services pour aide administrative ; Point-justice pour orientation juridique. Un signalement ou une aide au remplissage n'est pas présenté comme recours ou représentation. Aucune pièce transmise ni prise de rendez-vous automatique.

## Points restant à découper

- Choisir organisme/prestation du premier indu, puis séparer lecture, contestation, prescription, remise, retenues et contrainte. La matrice ne satisfait pas à elle seule les critères de DOM-012.
- Décliner les tâches par régime, acter propriétaires et éventuelle séparation emploi/minima ; conserver frontières ACRE, fiscalité, travail et handicap.
- Confirmer CR06 chez DOM-010 et SA04 chez DOM-012 avec frontières logement. Prêts d'honneur/avances hors banque demandent leur régime propre ; BNK-018 ne les couvre pas par son seul lien.
- Séparer recours préalable, médiation, urgence et contentieux spécialisé ; attribution à confirmer avec DOM-010/EXIST-006. Aucun délai, juge ou effet de médiation commun adopté.
- Prévoir règles aux dates des faits, paquet détaché, client et compréhension dans les futures stories. Le bilan PILOTE-003 terminé ne vaut pas sélection d'une tranche sociale.

[Contrôles et portée de cette intégration](dom-012-frictions-verification.md).
