# DOM-016 — Découpage successions et donations

Cadrage du 17 octobre 2026 (Europe/Paris). Vingt-cinq suites SUC proposées,
sans création de plugin ni sélection d’une implémentation. La
[table des parcours](dom-016-parcours.md) relie chaque demande courante à sa
story, son résultat et ses deux scénarios ; la
[vérification](dom-016-verification.md) consigne les contrôles réellement faits.

## Propriétaire et première tranche

Plugin principal proposé : `inheritance-legal`, identifiant publié futur
`judge-fr-eu-inheritance-legal`. Public : héritier présumé, donateur,
donataire, survivant ou représentant dont les pouvoirs restent à établir.
Le récit ou le document est le point d’entrée ; aucun nom de code ni
qualification de l’acte n’est demandé à la personne.

SUC-001 est la première tranche proposée : expliquer un courrier de notaire,
les pièces demandées et les questions avant une décision. Elle créera un
paquet avec un seul skill, si elle est choisie. Les autres suites dépendent
de SUC-001 pour le socle technique, sans devoir exécuter sa tâche métier.
Le [bilan PILOTE-003](../../01-pilote-travail/pilote-003-bilan-pilote.md)
est `terminee` après BASE-011 ; ce préalable satisfait ne choisit pas une
extension. Toutes les suites restent `proposee`.

## Contrat du futur paquet

| Élément | Exigence à réaliser à la première implémentation |
|---|---|
| Identité | Répertoire `inheritance-legal`, manifeste, README, modèle de profil facultatif, LICENSE/NOTICE ; entrée marketplace seulement avec un lot réel. Versions et inventaires ajustés selon les conventions. |
| Autonomie | Une extraction seule hors checkout ; chaque skill trouve ses références et modèles dans le paquet. Aucun autre plugin, profil d’entreprise ni pièce personnelle préenregistrée requis. Le backlog est un document de maintenance, jamais une dépendance d’exécution. |
| Recherche | Copie ordinaire de la méthode BASE-005 retenue au lot dans `references/shared/research-citation-method.md` ; référence locale de qualification successorale commune et références métier propres aux tâches. Versions, transitions et jurisprudence relues pour les faits du dossier ; trace BASE-014. |
| Stockage | Contrat d’isolation et helper BASE-008, modèles et licences embarqués à l’identique. Aucun fichier personnel ni arbre familial durable par défaut ; persistance seulement pour un besoin explicite dans l’espace isolé autorisé. |
| Intégrations | Aucun agent, hook ou connecteur prévu. Pièces fournies et recherche publique officielle ; absence d’accès tracée, conclusions dépendantes réservées. Aucun accès bancaire ou notarial authentifié présumé. |
| Effets | Sorties préparatoires et brouillons. Aucun accès nominatif à un fichier, paiement, déclaration, option, signature, transfert de pièces ou envoi exécuté. |
| Validation | Schémas, version, contrôle d’artefact détaché BASE-006, isolation BASE-008, lectures BASE-014 ; recettes client normales et limites avec sorties conservées. Ce cadrage n’exécute pas ces validations de paquet absent. |

Les chemins de skills et références proposés dans les SUC désignent des
fichiers futurs, pas des commandes disponibles. Chaque suite reste autonome
quant à son résultat, ses entrées, ses limites et ses sources métier.

## Qualification et sortie communes

Demander le résultat recherché, le décès et sa date documentée ou déclarée,
les liens familiaux utiles, le statut du couple et régime matrimonial connu,
la résidence habituelle, les pays et territoires concernés, les biens/dettes
connus, les donations et testament, les capacités et pouvoirs invoqués,
les actes signés ou accomplis, notifications, réception prouvée et démarches
en cours. Pour une donation de vivant, adapter ces entrées : ne pas inventer
un décès. Proposer de masquer coordonnées, identifiants bancaires et données
de tiers sans utilité ; aucune copie intégrale d’identité dans la conversation.

Une personne se disant héritière ne prouve pas sa qualité ; une preuve de
qualité n’établit pas à elle seule l’option ni les pouvoirs sur un bien. Un
solde de compte ne prouve pas la propriété des fonds. Distinguer liquidation
du régime matrimonial, dévolution, option, inventaire formel, comptes
d’indivision, partage et déclaration fiscale. Les prestations d’assurance-vie
ne sont pas intégrées automatiquement à l’actif successoral.

Chaque sortie explique en langage courant : document ou situation,
faits/pièces, mentions seulement déclarées, inconnues, questions et prochaine
étape. Les montants et dates portés dans une pièce sont recopiés avec leur
provenance, sans en certifier le fondement. Ne pas produire de partage
définitif, de soulte ou d’actif net certain sur un dossier incomplet.

Un récit suffit pour commencer la fiche ; l’absence d’acte réserve le stade
et les effets concernés. Rechercher la source exacte et la version pertinente
avant tout délai, seuil, plafond, majorité, formalité, dette exigible ou effet
d’une décision. Distinguer décès, opération bancaire, service facturé,
signature, notification et connaissance d’un fait ; ne pas appliquer une
date unique à toutes les questions. L’option et la fiscalité ont des objets
et calendriers distincts. Une médiation ne suspend pas par présomption tous
les délais du dossier.

Ne présumer ni faute d’un héritier, ni abus de banque, de notaire ou de
généalogiste. Une disparition ou omission alléguée n’établit pas un recel.
La sortie ne choisit aucune option ni stratégie pour la personne et ne promet
pas un remboursement, une protection du patrimoine ou un accord favorable.

BASE-013 : phrase finale courte précisant que l’information et la préparation
ne remplacent pas le notaire ou l’avocat compétent. Renfort en tête si
sommation, procédure, délai possible, départ demandé, signature ou autre
enjeu irréversible. Le service bancaire, fiscal, le créancier ou le greffe
peuvent renseigner sur le dossier sans être présentés comme conseil
indépendant. En cas de litige ou procédure, nommer l’avocat. Toute décision
citée est ouverte et lue conformément à BASE-005 section 10 ; une piste non
lue conserve ce statut. Appliquer les voies BASE-010 si l’accès échoue.

## Ordre de traitement et frontière entre suites

| Situation | Résultat principal | Question distincte ensuite, si nécessaire |
|---|---|---|
| Courrier incompris | SUC-001 : fiche de lecture et pièces | Option/sommation SUC-003, passif SUC-002, frais SUC-009 ou DOM-041 selon émetteur. |
| Décision à préparer | SUC-002 : inventaire préparatoire | SUC-003 : options à expliquer ; SUC-004 : actes accomplis ; SUC-005/006 : dossier de formalités spécifique. Aucun choix produit. |
| Créance ou découverte tardive | SUC-007 : lecture de créance ; SUC-008 : dossier de connaissance après acceptation | Acte d’exécution identifié : DOM-003 prioritaire ; ni relance ni découverte ne prouvent une dette personnelle. |
| Avoirs bancaires | SUC-009 : frais ; SUC-010 : recherches ; SUC-011 : facture obsèques ; SUC-012 : fonctionnement ; SUC-013 : preuve de qualité | Propriété des fonds SUC-002, paiement contesté BNK-001 ; chaque résultat demeure séparé. |
| Préparation de partage | SUC-014/015/016/017 : effets, libéralités, évaluations, comptes | SUC-020 : rapprochement du projet ; SUC-018 : occupation ; SUC-019 : pouvoir de disposition. |
| Partage déjà signé | SUC-021 : grief, pièces et connaissance | Avocat pour fondement et calendrier ; aucune procédure ou prescription générique. |
| Survivant, généalogiste, donation, élément étranger | SUC-022/023/024/025 : un dossier préparatoire propre à chaque objet | Le transfrontalier réserve les conclusions françaises dépendantes ; SUC-025 ne tranche pas toute la succession. |

## Frontières et transmissions bornées

Le domaine voisin reçoit seulement la question distincte, la chronologie et
les pièces utiles avec leurs inconnues. Pas d’envoi ni de chargement automatique
de tous les domaines ; complément absent ou non adapté : orientation explicite.

| Objet distinct | Propriétaire | Données utiles ; ce qui reste en succession |
|---|---|---|
| Choix/prix des prestations, volonté funéraire, prise en charge | DOM-031, FUN-002/004/005 | Facture, commande, signataire et financements ; règlement bancaire SUC-011 et passif SUC-007 ici. Contribution familiale sans actif : question à qualifier avec le professionnel, sans dispense déduite de la renonciation. |
| Déclaration, droits de succession/donation, contrôles et échéances fiscales | DOM-011 | Décès, pays, actifs et actes documentés, dépôt/réception ; ici, option et partage, sans conseil fiscal ni dépôt supposé fait par le notaire. |
| Statut du couple, liquidation de son patrimoine, conflit parental | DOM-013 | Statut, régime, titres et pouvoirs ; ici, transmission et logement du survivant SUC-022. |
| Assistance/représentation d’un majeur | DOM-026 | Mesure exacte, acte envisagé et pouvoirs ; ici, résultat successoral sous réserve du pouvoir d’agir. Mineur : formalités successorales SUC-006 ; conflit parental DOM-013. |
| Bail et transfert du bail | DOM-006 | Type de bail, occupant et notifications ; SUC-022 ne déduit aucun transfert de la seule qualité d’héritier. |
| Assurance-vie, clause et bénéficiaire | INS-011 / DOM-005 | Contrat ou indice, qualité invoquée et recherches ; SUC-010 peut signaler Ciclade mais ne décide pas du bénéficiaire ni de l’actif civil/fiscal. |
| Paiement bancaire contesté ; compte d’un vivant ; médiation bancaire | BNK-001, BNK-017, BNK-004 / DOM-004 | Opération, dates et réclamation ; décompte successoral SUC-009, fonds du défunt SUC-010/012 ici. |
| Mission, frais et réclamation contre un notaire | DOM-041 | Lettre de mission, facture et échanges ; fond successoral et décompte bancaire restent ici. Plusieurs notaires : aucune facturation doublée présumée. |
| Titre et acte d’exécution, saisie ou mesure de départ | DOM-003 | Copie intégrale, notification et titre ; fond de la dette successorale SUC-007/008 conservé séparément. |
| Infraction alléguée, vol/recel/escroquerie | DOM-002 | Faits précis, provenance et pièces, sans qualification déjà acquise ; SUC-014/015/023 conserve inventaire ou lecture contractuelle. |
| Consentement contractuel général | DOM-001 | Contrat, signature, mode de conclusion et information ; contrat de révélation sectoriel SUC-023 ici. |
| Créances employeur, caisse, récupération ASPA | Emploi privé / DOM-037 ; DOM-012/036 | Contrat/décision, périodes et décompte ; SUC-002 recense seulement créance ou passif, sans seuil ASPA ni dette de prestation certifiés. |
| Transaction immobilière, défaut de travaux, charges de copropriété | DOM-017/015/018 | Projet, bien et pièces techniques/comptables ciblées ; pouvoirs indivis et comptes successoraux SUC-019/017 ici. |
| Facture EHPAD et restitution administrative des effets | DOM-025 | Contrat d’accueil, dépositaire, facture et reçu ; SUC-014 tient l’inventaire préparatoire et les preuves de remise. |

## Couverture des compléments reçus

Ce tableau actualise le périmètre de DOM-016 sans réécrire les matrices
historiques d’origine ni déclarer leurs capacités livrées.

| Origine / points | Attribution du découpage |
|---|---|
| [Banque](../dom-004-annexes/dom-004-frictions-utilisateurs.md), 86–88 | SUC-009 frais, tarif daté et gratuité alléguée ; SUC-010 recherches banque/FICOBA/Ciclade. Décision constitutionnelle alléguée de juin 2026 non identifiée ni validée ici. |
| [Décès](../dom-031-annexes/dom-031-frictions-utilisateurs.md), 33 | SUC-014 inventaire, dépositaire, preuve de remise ; facture d’établissement DOM-025. |
| Décès, 55–66 | 55–56 SUC-011 ; 57–60 SUC-012 et propriété SUC-002 ; 61–62 SUC-009 ; 63 SUC-013 ; 64/66 SUC-010 et inventaire SUC-002 ; 65 SUC-012, paiement contesté BNK-001. |
| Décès, 67–77 | 67 SUC-002 ; 68–70 SUC-003 ; 71–72 SUC-005 ; 73 SUC-004 ; 74 SUC-006 et FUN-005 ; 75 SUC-006 ; 76 SUC-007 ; 77 SUC-008. |
| Décès, 78–80 | DOM-011 pour dépôt, calendrier fiscal indépendant du partage, dispense déclarative distincte d’une exonération ; DOM-041 pour mission, suivi et responsabilité alléguée du notaire. SUC-001/020 donnent les pièces et questions, sans fusionner option et fiscalité. |
| Décès, 81–89 | 81 SUC-014 ; 82–83 SUC-015, fiscalité DOM-011 et pénal DOM-002 seulement sur question distincte ; 84 SUC-016 ; 85 SUC-020 ; 86 SUC-018/019 ; 87 SUC-021 ; 88 SUC-017 ; 89 DOM-041 pour mission et frais de plusieurs notaires. |
| Décès, 99 et 117 | 99 INS-011, frontière SUC-002/010 ; 117 SUC-002 pour les créances encore dues, droit sectoriel transmis à emploi/DOM-012/036. |
| Décès, 120–122 et 137 | 120–122 SUC-022, bail DOM-006 et couple DOM-013 ; 137 SUC-023 contrat de révélation. |
| Tâches initiales DOM-016 | Courrier SUC-001, patrimoine SUC-002, désaccord/partage SUC-017 à 021, projet de donation SUC-024. SUC-025 borne l’élément étranger relevé dès la qualification. |

## Plan des sources métier

Chaque suite nomme sa référence locale future, les textes à lire et la limite
de la recherche. Ces pistes ne déclarent aucune version française vérifiée.

| Groupe | Sources primaires à vérifier selon les faits et dates |
|---|---|
| SUC-001 à 008, 013/014 | Code civil : qualité et preuve, option et actes, dettes, renonciation et capacité ; CPC et formalités officielles applicables. Inventaire formel distinct d’un tableau préparatoire ; délais propres et réception documentée. |
| SUC-009 à 013 | Code monétaire et financier : frais, opérations après décès, inactivité/transferts ; textes d’application et tarifs datés. FICOBA : textes fiscaux et régime d’accès pour leur articulation, sans transfert de tout le volet fiscal. Décision constitutionnelle invoquée : identité exacte, motifs, dispositif, publication et effets à lire. |
| SUC-015 à 021 | Code civil : libéralités, indivision et partage ; CPC selon la procédure. Testaments, titres, conventions et décisions exacts. Réformes de sortie d’indivision annoncées : dispositions et transitions à vérifier avant une majorité ou un pouvoir. |
| SUC-022 | Code civil : logement du survivant, volonté et formalités ; distinguer statut personnel, vocation successorale et bail. |
| SUC-023/024 | Mandat de recherche successorale et contrat, règles de consommation selon le cas ; Code civil sur donation, forme, capacité, charges et effets civils. Fiscalité seulement orientée DOM-011. |
| SUC-025 | Règlement (UE) 650/2012, consolidations, rectificatifs, transitions et champ territorial ; autres conventions/règles de conflit si nécessaire. Compétence, loi applicable, circulation d’acte et fiscalité séparées. |

Les [lectures officielles](dom-016-sources.md) du cadrage orientent ce plan.
Elles ne résolvent aucun dossier et ne remplacent pas la relecture des sources
primaires lors de chaque implémentation et préparation de lot.
