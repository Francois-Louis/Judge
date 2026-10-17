# DOM-040 — Découpage chasse et pêche de loisir

Cadrage du 17 octobre 2026 (Europe/Paris). Les sept propositions CHP sont
des tâches futures, sans skill disponible ni sélection d'une extension.
La [vérification](dom-040-verification.md) donne les parcours documentaires
observés et la portée des contrôles.

## Propriétaire et contrat du futur paquet

Conserver `hunting-fishing-legal`, identifiant publié proposé
`judge-fr-eu-hunting-fishing-legal`. Public : pratiquant de loisir,
propriétaire, riverain ou personne subissant des dégâts. Le point d'entrée
est le document ou le récit, sans nom de code exigé. Qualifier séparément
chasse, pêche en eau douce et pêche maritime, y compris les lieux dont le
régime reste incertain (estuaire, étang, outre-mer).

CHP-001 est la première tranche proposée : lecture d'un acte après contrôle,
sans contestation formelle. Si elle est choisie, elle crée le paquet avec
un seul skill, ses références métier et les copies ordinaires BASE-005 et
BASE-008 ; aucun paquet vide n'est créé ici. Les autres suites dépendent
de CHP-001 pour ce socle technique, sans charger son workflow pour une
demande étrangère à un contrôle. PILOTE-003 est `terminee` après BASE-011 ;
ce préalable ne sélectionne aucune tranche automatiquement.

| Contrat | Exigence pour la première implémentation |
|---|---|
| Autonomie | Un seul paquet extrait hors checkout ; aucun autre plugin requis. Les relais sont des orientations avec transmission des faits et questions déjà établis. |
| Références | Chaque skill charge ses références locales et `references/shared/research-citation-method.md`, copie identique de la version BASE-005 retenue au lot. Sources, versions, modèles et raisonnements métier restent dans le paquet. Aucun renvoi au backlog comme dépendance d'exécution. |
| Identité et stockage | Manifeste, README, LICENSE, NOTICE, contrat d'isolation, helper et modèles BASE-008 embarqués. Aucun profil obligatoire, aucun registre de pratiquants ou de parcelles, aucun stockage durable pour ces tâches. |
| Intégrations | Aucun agent, hook ou connecteur prévu. Travail sur les pièces fournies ; recherche publique officielle selon les capacités du client. Accès impossible : tracer les tentatives, réserver la conclusion et poursuivre la lecture des pièces. |
| Effets | Brouillons seulement. Aucun paiement, recours, enregistrement de pêcheur, déclaration de capture, opposition foncière ou envoi effectué. |
| Recette | Schémas, contrôle BASE-006 de l'artefact détaché, isolation BASE-008, versions et sources relues selon BASE-014 ; recette en client sur cas normal et limite avec sorties conservées. |

## Entrées et suites

| Paroles de la personne | Proposition et résultat borné |
|---|---|
| « J'ai reçu ce papier après un contrôle, que me reproche-t-on ? » | [CHP-001](../suites/chp-001-lecture-acte-controle.md) : fiche d'acte, allégation, stade, dates recopiées, pièces et interlocuteur. |
| « J'ai mon permis, mais je ne sais pas si mes papiers suffisent ici » | [CHP-002](../suites/chp-002-documents-chasse.md) : tableau des documents de chasse et vérifications manquantes. |
| « Ma carte permet-elle de pêcher à cet endroit ? » | [CHP-003](../suites/chp-003-documents-peche-eau-douce.md) : rapprochement carte, secteur, association et sources locales. |
| « Je pêche en mer : quels papiers ou déclarations dois-je vérifier ? » | [CHP-004](../suites/chp-004-formalites-peche-maritime.md) : fiche des formalités pour une pratique, une zone et une date précises. |
| « Je ne veux plus que l'association chasse sur mon terrain » | [CHP-005](../suites/chp-005-droit-chasse-terrain.md) : dossier de droits et projet de demande d'explication avant opposition. |
| « La rivière borde mon terrain » ; « mon étang est privé » | [CHP-006](../suites/chp-006-droit-peche-terrain.md) : questions sur droit de pêche, accès et régime des eaux, séparément. |
| « Les sangliers ont retourné mon jardin » | [CHP-007](../suites/chp-007-degats-gibier.md) : dossier factuel des dégâts et voies à vérifier, sans indemnité promise. |

CHP-002/003/004 portent sur les documents et formalités d'une pratique
décrite, pas une certification générale de légalité. CHP-005/006 portent
sur le droit relatif au terrain. Un acte reçu déclenche CHP-001 en premier ;
les pièces de pratique utiles sont ensuite reprises sans second dossier.

## Qualification commune et traitement des inconnues

Relever qualité réelle de la personne, objectif, commune/département ou
façade maritime, emplacement utile, date et mode de pratique, espèce alléguée
sans identification inventée, documents détenus et autorisations invoquées.
Pour l'acte : copie lisible recto verso et annexes, nature portée, auteur et
qualité affichée, destinataire, date des faits, émission, réception et preuve,
démarches déjà faites, mentions de paiement, saisie, convocation ou retrait.
Ne pas exiger des coordonnées GPS, identifiants ou données de tiers sans
nécessité ; proposer de masquer les mentions inutiles des pièces.

Séparer pièce lue, déclaration et inconnu. Un récit suffit pour commencer
la fiche ; il ne permet pas d'inventer un acte ou une échéance. Un document
manquant n'est pas une infraction prouvée. Une carte, un titre de propriété
ou un accord allégué ne suffit pas à conclure sur toutes les conditions.
Ne présumer ni faute du pratiquant, ni abus de l'agent ou de l'association.

Aucune période, taille, quota, montant, durée de validation, délai de
recours ou de déclaration n'est affirmé sans texte/version applicable lus,
faits établis et règle locale pertinente. Une mention chiffrée d'un acte
est recopiée comme telle, sans validation ni recalcul. Avec une règle locale
absente, identifier texte, autorité, territoire et date à rechercher ;
réserver seulement la conclusion concernée, sans déclarer la pratique libre
ou interdite. Ne pas transformer une brochure fédérale en arrêté.

La sortie commence par l'urgence observée si acte pénal, convocation,
mesure ou échéance annoncée, puis explique document, inconnues, pièces et
prochaine étape. BASE-013 : phrase finale courte nommant le professionnel
compétent ; en pénal, avocat. L'agent verbalisateur ou la fédération apporte
des informations sur le dossier ou la pratique, sans être présenté comme
le conseil indépendant de la personne. Toute décision de justice utilisée
doit être ouverte et lue selon la section 10 de BASE-005.

## Frontières et transmission

| Objet distinct | Propriétaire | Ce que CHP transmet et conserve |
|---|---|---|
| Détention, transport, classement ou saisie d'une arme | CRIM-017 / DOM-002 | Description déclarée, acte et mesures recopiées ; ici, lecture du contrôle seulement, aucun conseil de manipulation. |
| Audition, contestation pénale, paiement/consignation et leurs effets, recours | DOM-002 | Acte, réception, faits allégués, démarches et inconnues ; CHP-001 ne rédige pas de contestation ni ne choisit de payer. |
| Retrait/suspension administratif du titre ou autre décision administrative | DOM-010, avec règles sectorielles locales | Fiche d'acte et pièces du titre ici ; recours distinct, aucun régime pénal appliqué par défaut. |
| Exploitation agricole, élevage, dégâts aux cultures d'un exploitant | DOM-014 | CHP-007 distingue jardin privé et cultures d'exploitation ; dossier factuel transmis sans double calcul ni indemnisation agricole ici. |
| Espèce protégée, pollution, atteinte au milieu | DOM-030 | Espèce et faits allégués, lieu et source à retrouver ; le contrôle reçu reste lisible ici. |
| Animal domestique | DOM-033 | Origine et espèce à établir ; ne pas attribuer les dégâts au gibier sans élément. |
| Bruit ou autre nuisance de voisinage | DOM-020 | Chronologie et objet distinct ; le droit de chasser n'épuise pas la question de voisinage. |
| Garantie, refus ou indemnité d'assurance | DOM-005 | Attestation lue pour CHP-002 ; analyse de couverture et déclaration de sinistre chez assurance. |
| Dommage corporel d'un accident de chasse, responsabilité civile et réparation contentieuse | DOM-035 | Pièces de l'accident ou des dégâts ; priorité à la sécurité, aucun chiffrage ni attribution de responsabilité ici. |
| Vote/exclusion associatif sans question de droit de chasse/pêche | DOM-032 | Acte et règles invoquées ; droits sectoriels sur le terrain conservés en CHP-005/006. |

La pêche professionnelle, même présentée avec une carte de loisir, est hors
périmètre : demander l'activité réelle et orienter vers un professionnel
compétent, sans appliquer les règles de loisir.

## Plan de sources et de références métier

Les références ci-dessous sont à créer dans le futur paquet. Les textes
primaires, versions historiques et mesures locales restent à ouvrir lors
de chaque implémentation. Leur présence dans ce plan ne les valide pas.

| Propriétaire | Référence locale proposée | Recherche primaire à effectuer |
|---|---|---|
| CHP-001 | `references/lecture-acte-controle.md` et `references/qualification-chasse-peche.md` | Code de l'environnement pour chasse/eau douce ; Code rural et de la pêche maritime pour mer ; acte exact, pouvoirs de l'auteur, procédure réellement annoncée, texte local visé. CPP seulement pour distinguer le stade et transmettre à DOM-002. |
| CHP-002 | `references/documents-chasse.md` | Code de l'environnement, titres et validation, assurance ; textes de sécurité et arrêtés du territoire, schéma départemental pertinent ; cas particuliers et outre-mer à qualifier. |
| CHP-003 | `references/documents-peche-eau-douce.md` | Code de l'environnement, conditions d'exercice et organisation agréée ; classement des eaux, arrêtés préfectoraux, titres et réciprocité invoqués. |
| CHP-004 | `references/formalites-peche-maritime.md` | Code rural et de la pêche maritime ; règlements UE de contrôle, actes nationaux et modifications ; mesures de façade/zone et sanitaires pertinentes. Enregistrement et déclaration de captures à vérifier séparément, selon âge, pratique, espèce et date. |
| CHP-005 | `references/droit-chasse-terrain.md` | Code de l'environnement, associations communales de chasse agréées (ACCA), opposition/retrait et droits invoqués ; régime local, statuts, bail et actes préfectoraux selon terrain. |
| CHP-006 | `references/droit-peche-terrain.md` | Code de l'environnement, régime des eaux et droits de pêche/passage ; propriété, conventions et actes de classement. Ne pas déduire « eaux closes » de « propriété privée ». |
| CHP-007 | `references/degats-gibier.md` | Code de l'environnement, voies d'indemnisation des dégâts ; Code civil si voie de responsabilité à explorer. Conditions, bénéficiaires, exclusions et interlocuteur à établir avant toute orientation ferme. |

Trois pages d'information officielles ont été ouvertes pour orienter ce
plan, sans adopter leurs nombres ni leurs calendriers :

| Repère | Lecture du 17 octobre 2026 par outil web | Usage et statut documentaire |
|---|---|---|
| S01 | OFB, [La validation du permis de chasser](https://ofb.gouv.fr/la-validation-du-permis-de-chasser), rubriques modalités et particularités territoriales | Distinguer titre, validation, assurance et territoire dans CHP-002. `partiel` : fiche d'information lue, textes et versions non contrôlés ; applicabilité `a-etablir`. |
| S02 | DILA, [Pêche de loisir à la ligne en eau douce](https://www.service-public.gouv.fr/particuliers/vosdroits/F2117), page indiquant une vérification au 25 septembre 2026, rubriques conditions, lieux et références | Prévoir des contrôles séparés carte/droit sur le lieu/régime des eaux et sources locales dans CHP-003/006. `partiel` : textes liés non ouverts ; applicabilité `a-etablir`. |
| S03 | Ministère chargé de la mer, [Pêche de loisir en mer](https://www.mer.gouv.fr/peche-de-loisir-en-mer), rubriques formalités, références réglementaires et interlocuteurs locaux | Ajouter à CHP-004 un contrôle des déclarations et enregistrements selon le champ exact, sans généralisation entre façades. `partiel` : fiche évolutive, actes liés et transitions non lus ; applicabilité `a-etablir`. |

Ces pages ne vérifient ni une infraction, ni une règle locale, ni les droits
d'un propriétaire. Les autres pistes de ce cadrage sont `non-verifie`.
Si une source est inaccessible à l'implémentation, appliquer les voies
BASE-010 puis consigner la limite dans le relevé BASE-005 du paquet.
