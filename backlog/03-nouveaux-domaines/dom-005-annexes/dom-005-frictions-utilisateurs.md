# Assurance — Frictions utilisateur et réponses à prévoir

Demande du **16 octobre 2026** : « voici les frictions des utilisateurs auxquelles il faut pouvoir répondre ». Le [texte fourni](../sources/assurances-frictions-2026-10-16.txt) est conservé intégralement comme expression du besoin. Ses 90 points sont repris avec propriétaire et résultat attendu ; les sections sur les délais, recours et réflexes sont traitées séparément.

**État : exigences de backlog.** Les 21 stories INS restent `proposee`. Un rattachement ne signifie pas qu'un skill existe ou répond déjà. DOM-035 reste un cadrage à découper ; BNK-011 assure l'orientation seule. Aucune première tranche ni création de plugin n'est lancée.

## Lecture du texte fourni

La mention « État des règles et pratiques au 16 octobre 2026 » appartient au document utilisateur. Aucun montant, délai, taux, statistique ou événement juridique n'est validé par cette intégration. Les favicons, noms de sites et mentions « +1 » ne sont pas des citations de passages effectivement lus.

À rechercher lors des implémentations : bilan 2025 et publication alléguée en septembre 2026 de la Médiation, communiqué ACPR d'avril 2026, accord CCSF allégué du 26 mai 2026 et son effet, réforme du démarchage téléphonique et transitions. Vérifier aussi les régimes de déclaration tardive, communication du rapport auto/habitation, catastrophe naturelle et sécheresse, franchises, relogement, véhicule irréparable, santé emprunteur, renonciation et prescription. Un accord ou une recommandation n'a pas par défaut le statut d'une obligation légale.

La hiérarchie pratique et les statistiques du texte ne fixent ni taux d'abus ni priorité statistiquement établie. Les rangs restent des propositions de planification.

## Changements de découpage

- INS-001 à INS-006, INS-008, INS-009 et INS-011 : compléter les preuves, sorties et scénarios sans supprimer leurs limites.
- INS-013 : dossier et règlement bloqués, provisions et transaction.
- INS-014 : cotisation, coefficient auto, impayé et régularisation.
- INS-015 : déclaration ou correction du risque.
- INS-016 : contestation de souscription, promesse et consentement.
- INS-017 : coordination d'un dégât des eaux ; INS-018 : dossier catastrophe naturelle.
- INS-019 : une garantie professionnelle pour un risque précis.
- INS-020 : actualisation d'une clause bénéficiaire par un souscripteur vivant.
- INS-021 : échéances d'un dossier, prescription, interruption et suspension.
- DOM-035 : conserver l'offre corporelle de la victime et les préjudices dans ce domaine ; traitement au fond à découper.
- Points 66–67 : conserver l'orientation seule BNK-011 selon les [décisions du 16 octobre 2026](../../decisions-2026-10-16.md). L'analyse au fond du placement, des frais et du conseil reste non couverte ; aucune story nouvelle ne l'annonce.

## Matrice des 90 points

Le premier propriétaire porte la question principale ; les suivants traitent un volet distinct. Chaque ligne est une exigence future, pas une consultation résolue.

| N° | Friction | Propriétaire et relais | Résultat attendu |
|---|---|---|---|
| 1 | Garantie plus étroite que son intitulé | [INS-004](../suites/ins-004-lire-garantie.md) | Comparer définition, événement couvert et circonstances établies. |
| 2 | Exclusion peu visible ou imprécise | [INS-001](../suites/ins-001-refus-garantie.md) | Demander clause, présentation et conditions de validité à vérifier. |
| 3 | Contradiction entre documents contractuels | [INS-004](../suites/ins-004-lire-garantie.md) | Rapprocher versions, conditions particulières, générales et avenants sans hiérarchie présumée. |
| 4 | Option présentée comme incluse | [INS-016](../suites/ins-016-contester-souscription.md), [INS-004](../suites/ins-004-lire-garantie.md) | Comparer promesse, option réellement souscrite et preuve du consentement. |
| 5 | Franchise découverte après sinistre | [INS-004](../suites/ins-004-lire-garantie.md), [INS-003](../suites/ins-003-contester-expertise.md) | Identifier assiette, minimum et maximum ; demander le calcul sans le refaire. |
| 6 | Cumul de franchises | [INS-003](../suites/ins-003-contester-expertise.md) | Rapprocher chaque franchise de la garantie et du fondement du cumul. |
| 7 | Plafond par objet, événement ou année | [INS-004](../suites/ins-004-lire-garantie.md) | Présenter plafonds et périodes avec la catégorie du bien. |
| 8 | Sous-plafonds masqués | [INS-004](../suites/ins-004-lire-garantie.md) | Séparer plafond global et limites de chaque poste. |
| 9 | Vétusté contestée | [INS-003](../suites/ins-003-contester-expertise.md) | Demander taux, état retenu et détail du décompte. |
| 10 | Valeur à neuf versée en deux temps | [INS-003](../suites/ins-003-contester-expertise.md), [INS-013](../suites/ins-013-suivre-indemnisation.md) | Séparer valeur initiale, complément, conditions et justificatifs de remplacement. |
| 11 | Sous-assurance et capitaux | [INS-015](../suites/ins-015-declaration-risque.md), [INS-003](../suites/ins-003-contester-expertise.md) | Comparer capitaux déclarés et base invoquée ; distinguer les réductions sans recalcul. |
| 12 | Carence initiale | [INS-004](../suites/ins-004-lire-garantie.md) | Identifier début, terme et garantie concernée ; régime santé → INS-009. |
| 13 | Franchise temporelle | [INS-009](../suites/ins-009-complementaire-sante.md), [INS-008](../suites/ins-008-assurance-emprunteur.md) | Distinguer période sans versement, carence et conditions d'incapacité. |
| 14 | Prise d'effet différente de la signature | [INS-004](../suites/ins-004-lire-garantie.md) | Comparer signature, effet du contrat et effet des options. |
| 15 | Promesse commerciale orale | [INS-016](../suites/ins-016-contester-souscription.md) | Rassembler traces et demander confirmation écrite de la promesse et du conseil. |
| 16 | Déclaration tardive | [INS-002](../suites/ins-002-declarer-sinistre.md), [INS-021](../suites/ins-021-echeances-recours.md) | Relever connaissance, déclaration et réception ; vérifier régime et unité du délai. |
| 17 | Refus automatique pour retard | [INS-001](../suites/ins-001-refus-garantie.md), [INS-021](../suites/ins-021-echeances-recours.md) | Séparer clause de déchéance, préjudice allégué, circonstances et preuve ; pas de refus validé automatiquement. |
| 18 | Déclaration seulement téléphonique | [INS-002](../suites/ins-002-declarer-sinistre.md) | Préparer confirmation écrite fidèle et conserver les références du premier signalement. |
| 19 | Pièces redemandées et dossier incomplet | [INS-013](../suites/ins-013-suivre-indemnisation.md) | Produire inventaire daté et demande de liste consolidée. |
| 20 | Formulation imprécise du récit | [INS-002](../suites/ins-002-declarer-sinistre.md) | Distinguer fait observé, hypothèse et correction explicite sans réécrire l'histoire. |
| 21 | Cause du sinistre affirmée trop tôt | [INS-002](../suites/ins-002-declarer-sinistre.md) | Garder constatations et hypothèses séparées. |
| 22 | Réparation avant expertise | [INS-002](../suites/ins-002-declarer-sinistre.md) | Documenter preuves et mesures urgentes, sans retarder une mise en sécurité. |
| 23 | Refus pour défaut d'entretien | [INS-001](../suites/ins-001-refus-garantie.md) | Rapprocher motif, clause, factures d'entretien et origine constatée. |
| 24 | Dommages tenus pour antérieurs | [INS-003](../suites/ins-003-contester-expertise.md), [INS-001](../suites/ins-001-refus-garantie.md) | Comparer photos, états des lieux, rapport et motif ; garantie et constat technique séparés. |
| 25 | Expertise minorant les dommages | [INS-003](../suites/ins-003-contester-expertise.md) | Comparer postes et devis ; demander justification technique sans réévaluer le dommage. |
| 26 | Rapport d'expertise non communiqué | [INS-003](../suites/ins-003-contester-expertise.md) | Demander le rapport et vérifier le régime auto ou habitation, sans obligation universelle affirmée. |
| 27 | Expertise présentée comme incontestable | [INS-003](../suites/ins-003-contester-expertise.md), [INS-007](../suites/ins-007-protection-juridique.md) | Expliquer options contradictoires et frais à vérifier, dont honoraires éventuellement garantis. |
| 28 | Transaction ou renonciation générale | [INS-013](../suites/ins-013-suivre-indemnisation.md) | Repérer portée, réserves et préjudices non traités ; corps → DOM-035. |
| 29 | Paiement partiel présenté comme définitif | [INS-013](../suites/ins-013-suivre-indemnisation.md) | Séparer provision, règlement initial, complément et solde. |
| 30 | Règlement repoussé | [INS-013](../suites/ins-013-suivre-indemnisation.md), [INS-005](../suites/ins-005-mediation-assurance.md), [INS-021](../suites/ins-021-echeances-recours.md) | Demander obstacle et date annoncée ; suivre réclamation et échéances parallèles. |
| 31 | Cambriolage sans effraction visible | [INS-004](../suites/ins-004-lire-garantie.md), [INS-001](../suites/ins-001-refus-garantie.md) | Lire les formes de vol garanties et les preuves policières ou techniques. |
| 32 | Sécurité des ouvertures | [INS-004](../suites/ins-004-lire-garantie.md), [INS-001](../suites/ins-001-refus-garantie.md) | Identifier obligation, équipement exigé et sanction invoquée. |
| 33 | Logement longtemps inoccupé | [INS-004](../suites/ins-004-lire-garantie.md) | Lire définition et mode de décompte de l'inhabitation sans durée universelle. |
| 34 | Vol en cave ou garage | [INS-004](../suites/ins-004-lire-garantie.md) | Identifier local assuré, biens admis et sous-plafond. |
| 35 | Objets précieux mal déclarés | [INS-004](../suites/ins-004-lire-garantie.md), [INS-015](../suites/ins-015-declaration-risque.md) | Rapprocher définition, preuve de valeur et déclaration initiale. |
| 36 | Dommages d'eau et réparation de la fuite | [INS-017](../suites/ins-017-coordonner-degat-eaux.md), [INS-004](../suites/ins-004-lire-garantie.md) | Séparer cause, recherche de fuite, réparation et dommages consécutifs. |
| 37 | Infiltration ou défaut d'entretien | [INS-001](../suites/ins-001-refus-garantie.md), [INS-017](../suites/ins-017-coordonner-degat-eaux.md) | Documenter événement, état antérieur et origine technique sans diagnostic. |
| 38 | Renvoi entre assureurs, voisin, bailleur et syndic | [INS-017](../suites/ins-017-coordonner-degat-eaux.md) | Identifier rôles et gestionnaire à confirmer ; champ et statut d'IRSI à vérifier. |
| 39 | Déclaration catastrophe naturelle | [INS-018](../suites/ins-018-catastrophe-naturelle.md), [INS-021](../suites/ins-021-echeances-recours.md) | Vérifier arrêté, publication, territoire, période et preuve de déclaration. |
| 40 | Franchise catastrophe naturelle | [INS-018](../suites/ins-018-catastrophe-naturelle.md) | Vérifier catégorie, territoire et version du régime avant tout montant. |
| 41 | Relogement omis | [INS-018](../suites/ins-018-catastrophe-naturelle.md), [INS-017](../suites/ins-017-coordonner-degat-eaux.md), [INS-004](../suites/ins-004-lire-garantie.md) | Qualifier régime, frais et clause ou texte pertinent ; ne pas promettre une couverture uniforme. |
| 42 | Biens professionnels au domicile | [INS-019](../suites/ins-019-garantie-professionnelle.md), [INS-004](../suites/ins-004-lire-garantie.md) | Distinguer usage privé, activité, propriété du bien et police pertinente. |
| 43 | Assurance au tiers mal comprise | [INS-004](../suites/ins-004-lire-garantie.md) | Séparer tiers victimes, véhicule assuré et blessures du conducteur. |
| 44 | Garantie conducteur absente | [INS-004](../suites/ins-004-lire-garantie.md), [DOM-035](../dom-035-responsabilite-dommages.md) | Lire garantie propre ; préjudice corporel et droits de victime dans DOM-035. |
| 45 | Prêt du véhicule | [INS-004](../suites/ins-004-lire-garantie.md) | Lire conducteurs admis, conditions, restrictions et franchise annoncée. |
| 46 | Usage professionnel non déclaré | [INS-015](../suites/ins-015-declaration-risque.md), [INS-019](../suites/ins-019-garantie-professionnelle.md) | Comparer usage réel et questions initiales avant de préparer une déclaration. |
| 47 | Constat imprécis et responsabilité retenue | [INS-002](../suites/ins-002-declarer-sinistre.md), [DOM-035](../dom-035-responsabilite-dommages.md) | Préparer complément factuel et preuves sans modifier un constat signé ni attribuer la responsabilité. |
| 48 | Malus contesté | [INS-014](../suites/ins-014-contester-cotisation.md), [DOM-035](../dom-035-responsabilite-dommages.md) | Séparer coefficient et tarif ; demander faits et fondement, responsabilité civile distincte. |
| 49 | Valeur avant sinistre trop faible | [INS-003](../suites/ins-003-contester-expertise.md) | Rassembler comparables, état, kilométrage et équipements sans fixer soi-même la valeur. |
| 50 | Offre de cession d'un véhicule irréparable | [INS-003](../suites/ins-003-contester-expertise.md), [INS-021](../suites/ins-021-echeances-recours.md) | Lire offre, rapport, choix et conséquences à vérifier ; distinguer restrictions administratives et garantie. |
| 51 | Résiliation auto après sinistre | [INS-006](../suites/ins-006-resilier-contrat.md) | Distinguer motif spécial et échéance ; lire notification et régime sans droit général supposé. |
| 52 | Préjudices corporels sous-évalués | [DOM-035](../dom-035-responsabilite-dommages.md) | Prévoir inventaire des préjudices, consolidation, offre et renonciation ; tâche au fond restant à découper. |
| 53 | Pourcentage de complémentaire trompeur | [INS-009](../suites/ins-009-complementaire-sante.md) | Distinguer facture, base, part obligatoire et complémentaire sans recalcul. |
| 54 | Forfaits et plafonds santé | [INS-009](../suites/ins-009-complementaire-sante.md) | Lire acte, période, forfait et plafond annuel. |
| 55 | Carence et exclusions de prévoyance | [INS-009](../suites/ins-009-complementaire-sante.md) | Comparer événement, effet et causes exclues selon le régime de l'organisme. |
| 56 | Invalidité sociale et contractuelle confondues | [INS-009](../suites/ins-009-complementaire-sante.md) | Séparer décision de caisse et définition du contrat. |
| 57 | Arrêt des prestations avant reprise | [INS-009](../suites/ins-009-complementaire-sante.md) | Demander motif et expertise médicale, avec collecte minimale et contre-avis à vérifier. |
| 58 | Seuil d'une garantie accidents de la vie | [INS-004](../suites/ins-004-lire-garantie.md), [INS-001](../suites/ins-001-refus-garantie.md), [DOM-035](../dom-035-responsabilite-dommages.md) | Lire seuil et définition contractuels ; évaluation corporelle séparée, aucun seuil universel. |
| 59 | Définition restrictive de l'accident | [INS-004](../suites/ins-004-lire-garantie.md), [INS-001](../suites/ins-001-refus-garantie.md) | Distinguer définition de garantie, exclusion et faits observés. |
| 60 | Quotité d'assurance emprunteur | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Séparer coemprunteurs, quotités et part annoncée sans recalculer la prestation. |
| 61 | Garantie perte d'emploi restrictive | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Lire statut, cause de fin d'activité et exclusions réellement souscrites. |
| 62 | Carences successives lors d'une substitution | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Frise ancien/nouveau contrat, effet, carence et franchise ; accord CCSF allégué à rechercher avant application. |
| 63 | Substitution refusée | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Comparer exigences, garanties proposées et motivation du prêteur. |
| 64 | Questionnaire santé potentiellement interdit | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Vérifier crédit, montant cumulé par assuré, âge et terme sans collecter la santé au préalable. |
| 65 | Erreur dans le questionnaire santé | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Demander questions et réponses exactes ; intention et sanction non déduites automatiquement. |
| 66 | Assurance-vie présentée comme garantie | [BNK-011](../suites/bnk-011-placement.md) | Orientation seule : produit, documents et promesse ; pas d'évaluation du placement ni du conseil. |
| 67 | Cumul des frais d'assurance-vie | [BNK-011](../suites/bnk-011-placement.md) | Orientation seule : demander décomposition et documents ; contrôle au fond non couvert par la décision actuelle. |
| 68 | Clause bénéficiaire ancienne ou imprécise | [INS-020](../suites/ins-020-actualiser-clause-beneficiaire.md) | Préparer actualisation par le souscripteur vivant, sous réserve des pouvoirs et acceptations. |
| 69 | Contrat inconnu après décès | [INS-011](../suites/ins-011-assurance-vie-beneficiaire.md) | Qualifier recherche AGIRA/Ciclade, qualité, pièces et destinataire ; ne pas confondre succession. |
| 70 | Voyage et carte bancaire | [INS-004](../suites/ins-004-lire-garantie.md) | Distinguer assurance et assistance, paiement exigé ou non, bénéficiaires, territoire et activation. |
| 71 | Annulation pour motif non garanti | [INS-004](../suites/ins-004-lire-garantie.md), [INS-001](../suites/ins-001-refus-garantie.md) | Lire motif et conditions ; obligations du vendeur ou transporteur → DOM-008. |
| 72 | Assurance accessoire téléphone ou électronique | [INS-004](../suites/ins-004-lire-garantie.md), [INS-016](../suites/ins-016-contester-souscription.md) | Lire exclusions et qualifier renonciation selon vente, date et régime ; garantie vendeur → DOM-001. |
| 73 | Reconduction automatique | [INS-006](../suites/ins-006-resilier-contrat.md) | Lire échéance, information reçue, statut de l'assuré et voie pertinente. |
| 74 | Résiliation infra-annuelle refusée | [INS-006](../suites/ins-006-resilier-contrat.md) | Vérifier famille du contrat, ancienneté et continuité de l'assurance obligatoire. |
| 75 | Parcours de résiliation compliqué | [INS-006](../suites/ins-006-resilier-contrat.md) | Documenter disponibilité de la voie électronique et preuve de la demande ; champ à vérifier. |
| 76 | Prélèvement après résiliation | [INS-014](../suites/ins-014-contester-cotisation.md), [INS-006](../suites/ins-006-resilier-contrat.md) | Rapprocher période facturée, date effective et régularisation attendue. |
| 77 | Impayé et suspension de garantie | [INS-014](../suites/ins-014-contester-cotisation.md), [INS-006](../suites/ins-006-resilier-contrat.md), [INS-021](../suites/ins-021-echeances-recours.md) | Séparer exigibilité, mise en demeure, suspension, résiliation et paiement ; aucun maintien supposé. |
| 78 | Hausse de cotisation incomprise | [INS-014](../suites/ins-014-contester-cotisation.md) | Comparer avis, clauses et motifs ; pas de droit automatique à résilier. |
| 79 | Fausse déclaration invoquée tardivement | [INS-015](../suites/ins-015-declaration-risque.md), [INS-001](../suites/ins-001-refus-garantie.md) | Retrouver questions et réponses initiales, faits connus et intention alléguée. |
| 80 | Aggravation du risque non déclarée | [INS-015](../suites/ins-015-declaration-risque.md), [INS-021](../suites/ins-021-echeances-recours.md) | Qualifier changement et connaissance avant de vérifier obligation et délai. |
| 81 | Démarchage et consentement contestés | [INS-016](../suites/ins-016-contester-souscription.md) | Rechercher preuve et régime temporel ; réforme alléguée non tenue pour acquise. |
| 82 | RC Pro et pertes propres confondues | [INS-019](../suites/ins-019-garantie-professionnelle.md) | Distinguer dommages à autrui, biens propres et pertes d'exploitation. |
| 83 | Pertes financières d'un client web | [INS-019](../suites/ins-019-garantie-professionnelle.md) | Distinguer préjudices matériels, immatériels consécutifs et non consécutifs. |
| 84 | Activité web déclarée trop étroitement | [INS-019](../suites/ins-019-garantie-professionnelle.md), [INS-015](../suites/ins-015-declaration-risque.md) | Comparer activité déclarée et maintenance, hébergement, sécurité ou paiement réellement exercés. |
| 85 | RC exploitation et après livraison | [INS-019](../suites/ins-019-garantie-professionnelle.md) | Identifier phase d'activité, produit et garantie sans substitution automatique. |
| 86 | Biens confiés par des clients | [INS-019](../suites/ins-019-garantie-professionnelle.md) | Distinguer propriété, garde, lieu et garantie dédiée. |
| 87 | Stock sous-déclaré | [INS-019](../suites/ins-019-garantie-professionnelle.md), [INS-015](../suites/ins-015-declaration-risque.md) | Comparer catégories, variations et capitaux sans recalculer l'indemnité. |
| 88 | Atelier ou local partagé | [INS-019](../suites/ins-019-garantie-professionnelle.md) | Cartographier occupants, biens et polices sans couverture mutuelle supposée. |
| 89 | Transport ou expédition non couverts | [INS-019](../suites/ins-019-garantie-professionnelle.md) | Identifier trajet, territoire, phase de garde et contrat transport ; transporteur → DOM-008. |
| 90 | Protections du particulier appliquées au professionnel | [INS-019](../suites/ins-019-garantie-professionnelle.md), [INS-006](../suites/ins-006-resilier-contrat.md), [INS-005](../suites/ins-005-mediation-assurance.md) | Qualifier usage et recevabilité avant résiliation ou médiation de consommation. |

## Exigences des sections délais, recours et réflexes

| Besoin | Résultat attendu | Propriétaire |
|---|---|---|
| Préparer le dossier | Contrat intégral et versions, avenants, photos, factures, rapport, refus, échanges et inventaire daté. Distinguer pièce lue, fait déclaré, hypothèse et inconnue. | Tâche métier concernée |
| Comprendre la couverture | Définition, condition, exclusion, déchéance, nullité et réduction distinguées ; option, franchise, plafond, sous-plafond, carence et effet séparés. Clause défavorable ne signifie pas automatiquement abus. | INS-001, INS-004 ; régimes propres INS-008/INS-009/INS-019 |
| Préserver les preuves | Confirmation écrite d'un appel, constatations séparées des causes supposées ; photos et objets conservés si possible ; mesures urgentes de sécurité et conservatoires distinguées des réparations définitives. | INS-002 |
| Obtenir une décision exploitable | Demander motif écrit, clause/version, faits et pièces retenus, décompte et poste contesté ; ne pas inventer une obligation générale de motivation. | INS-001, INS-003, INS-013 |
| Réclamer utilement | Brouillon daté, demande précise, pièces et preuve d'envoi à conserver par la personne ; destinataire identifié, sans envoi par l'outil. | Tâche métier ; INS-005 pour escalade |
| Accéder à la médiation | Réclamation initiale, réponse définitive ou silence, recevabilité et date limite à vérifier ; aucun deuxième niveau interne imposé par principe ; organisme et statut consommateur/professionnel qualifiés. | INS-005 |
| Signaler un manquement | ACPR/autorité compétente selon organisme ; signalement distinct de la médiation et de l'indemnisation individuelle. | INS-005 |
| Suivre les délais du tableau | Déclaration ordinaire et vol, catastrophe naturelle, aggravation, impayé, réponse aux réclamations, médiation, prescription, sécheresse, corps, résiliation, emprunteur et renonciation vie : chaque catégorie conserve son régime, sa source et son déclencheur. | INS-021 ; tâche métier pour le fond, DOM-035 pour le corps |
| Protéger l'action | Ne pas considérer qu'un échange, une réclamation ou une saisine protège automatiquement la prescription ; prouver les événements interruptifs ou suspensifs, réserver le calcul et orienter vers un professionnel si nécessaire. | INS-021, INS-005 |
| Examiner une offre | Séparer provision, solde, complément et transaction ; effets d'une renonciation à vérifier avant signature. | INS-013 ; DOM-035 pour l'offre corporelle |
| Préparer un recours judiciaire | Dossier de faits, pièces et urgence, question d'expertise judiciaire à soumettre au professionnel compétent ; pas de procédure exécutée. | INS-003, INS-005, INS-021 ; DOM-035 selon dommage |
| Garder des réflexes adaptés | Liste contextualisée de pièces, questions, confirmations et échéances ; aucune veille, alerte ou connexion automatique. | Toutes les tâches concernées |

## Vérification de l'intégration

Les contrôles DOM-005 vérifient 90 identifiants uniques et continus, le lien au texte conservé, les propriétaires, le rattachement des 21 suites, les dépendances sans cycle, les chemins futurs, les liens et l'index. Les points 66–67 gardent une couverture d'orientation seulement ; le point 52 reste à découper dans DOM-035.

Relecture documentaire des frontières :

- Points 17/80 : déchéance pour retard de sinistre et déclaration d'aggravation du risque restent distinctes.
- Points 26/50 : rapport et offre de cession auto → INS-003 ; aucune obligation identique supposée pour l'habitation.
- Points 28/52 : règlement contractuel propre → INS-013 ; offre de préjudice corporel de la victime → DOM-035.
- Points 38/39 : coordination entre assureurs → INS-017 ; reconnaissance administrative Cat Nat → INS-018.
- Points 48/78 : coefficient auto et augmentation de tarif restent séparés dans INS-014.
- Points 56/60 : invalidité de caisse, invalidité contractuelle et quotité ne se déduisent pas l'une de l'autre.
- Points 66–69 : orientation placement BNK-011, clause du souscripteur vivant INS-020 et recherche après décès INS-011 séparées.
- Points 76/77 : restitution après résiliation et suspension pour impayé ont des déclencheurs distincts.
- Points 82–90 : lecture d'un risque professionnel ciblé, sans transposition automatique des protections du particulier.

**Portée :** intégration documentaire et relecture par l'agent de maintenance. Scénarios métier attendus, non exécutés ; aucune recherche juridique externe, création ou exécution de skill, installation, recette client, connexion, envoi ou publication.
