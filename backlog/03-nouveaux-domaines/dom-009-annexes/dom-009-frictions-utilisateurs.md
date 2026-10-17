# DOM-009 — Frictions douanes et commerce international

Intégration du **17 octobre 2026 (Europe/Paris)** du [guide fourni](../sources/douanes-frictions-2026-10-16.txt), qui porte la date du 16 octobre. Les 75 points, quinze lignes du calendrier, dix réflexes et cinq dossiers coutellerie sont conservés comme **besoins de réponse**. La mention « réglementation vérifiée » appartient au texte reçu ; elle n'est pas une validation par ce dépôt.

DOM-009 est un cadrage terminé ; les douze DOU restent `proposee`. Cette annexe précise leurs exigences et identifie des tâches candidates supplémentaires, **à découper en stories**, sans implémentation ni sélection de tranche. Aucun code local C/V ci-dessous n'est un skill ou une story disponible. Les résultats historiques du cadrage ne sont pas réécrits. [Portée et contrôles du complément](dom-009-frictions-verification.md).

## Contrat des futures réponses

Partir du problème exprimé, puis qualifier particulier/professionnel, rôle réel et représentation, marchandise/composition/usage, trajet et territoires douanier/fiscal, origine/provenance, opération/régime, dates et acte reçu. Demander facture, preuve de paiement, frais ventilés, déclaration/MRN lorsqu'il existe, mandat, conditions de vente/transport, échanges, notification et preuve de réception utiles. Ne pas exiger un document inexistant ni un dossier intégral pour commencer. Masquer les données superflues ; ne demander ni accès au compte ni secret IOSS.

Produire une fiche accessible : objectif de la personne ; faits déclarés/pièces observées/inconnues ; chronologie ; tableau **droits / TVA / frais privés / stockage / sanction** avec bénéficiaire et justificatif de chaque poste ; actions possibles à rechercher, interlocuteur et pièces manquantes. Lorsque la tâche le permet, ajouter un brouillon ciblé et un calendrier indiquant texte/version/champ, acte requis, événement de départ, preuve et incertitude. Une somme recopiée n'est pas un montant juridiquement dû ; une simulation nécessite une tâche et des paramètres sourcés propres. DOU-001 ne calcule toujours aucun droit, taxe ou délai.

Acte notifié, destruction, retenue, sanction ou recouvrement : identifier immédiatement les échéances propres et le conseil adapté, notamment un avocat en droit douanier. Une demande de détail au transporteur, une correction, une médiation, un remboursement commercial et une contestation formelle restent des démarches distinctes ; ne présumer aucun effet conservatoire ou suspensif entre elles. Une inconnue réserve sa conclusion sans bloquer la préparation factuelle. Aucun dépôt, transmission, signature, paiement, mandat ou rappel automatique.

Rechercher les sources officielles exactes selon BASE-005 et le [contrat d'accès officiel](../../../references/legal-source-access.md), aux dates des faits, avec champ, exceptions et transitions. Les noms d'organismes, favicons et « +1 » ne sont pas des références vérifiées. Le droit étranger suppose un rattachement établi et une recherche locale ; la politique du transporteur s'examine séparément. La relecture humaine est prise en charge par l'utilisateur selon AGENTS.md ; aucune compréhension réelle n'est déclarée observée.

## Ancrage dans les douze propositions existantes

| Story | Exigences de la liste et limites maintenues |
|---|---|
| [DOU-001](../suites/dou-001-dossier-achat-pays-tiers.md) | Achat privé ordinaire, facture détaillée, pièces de dédouanement et vrai motif du suivi ; C01 pour lecture des postes. TVA/IOSS, frais et seuils sont identifiés sans calcul ni déclaration. Un acte officiel sort de la tranche. |
| [DOU-002](../suites/dou-002-envoi-outre-mer.md) | Qualification territoriale commune ; ne pas transposer une règle de métropole à l'outre-mer. Le guide ne fournit pas de régime ultramarin à adopter. |
| [DOU-003](../suites/dou-003-biens-voyageur.md) | Biens accompagnés distincts des colis. Des échantillons professionnels transportés en valise relèvent de C07 à découper, sans élargir cette tranche privée. |
| [DOU-004](../suites/dou-004-qualifier-import-professionnel.md) | Rôle, représentation, EORI, identité TVA et habilitations à distinguer ; détection des régimes et restrictions, sans compléter les déclarations fiscales ou douanières. |
| [DOU-005](../suites/dou-005-preparer-exportation.md) | Preuve de sortie à réclamer, destination, conditions de transport et responsabilités à documenter. Retours, réparations, temporaire et restrictions restent des tâches séparées. |
| [DOU-006](../suites/dou-006-preparer-classement.md) | Description technique, déclaration réellement utilisée, nomenclature et mesures à rechercher ; dossier de classement distinct d'une demande de RTC C18. |
| [DOU-007](../suites/dou-007-preparer-origine.md) | Fabrication, transformations, matières et justificatifs ; origine non préférentielle, marquage et préférence par accord distincts. RCO C19 distinct du dossier. |
| [DOU-008](../suites/dou-008-preparer-valeur.md) | Facture, paiement, devise, fret/assurance inclus ou ajoutés, remises et Incoterm ; rechercher doublons sans arrêter valeur, assiette de TVA ou montant dû. |
| [DOU-009](../suites/dou-009-lire-acte-douanier.md) | Identifier contrôle, projet, décision, dette, PV, retenue/saisie et réception. La lecture ne prépare pas à elle seule observations, recours, sursis ou transaction. |
| [DOU-010](../suites/dou-010-demande-remboursement.md) | Paiement rattaché aux postes, motif précis et preuves de retour/défaut ; droits, TVA et honoraires suivent des démarches propres. Ni remboursement automatique ni délai unique. |
| [DOU-011](../suites/dou-011-demande-remise.md) | Dette identifiée non payée et fondement propre ; remise, contestation du bien-fondé, échéancier et sursis séparés. |
| [DOU-012](../suites/dou-012-dossier-vehicule.md) | Conserve son périmètre véhicule ; aucune règle générale sur les colis, couteaux ou petits envois ne lui est étendue. |

## Tâches supplémentaires à découper

Chaque ligne décrit un résultat distinct, avec un propriétaire proposé et un scénario futur. Les codes sont locaux à cette annexe. Aucun transfert automatique de dossier ni installation du voisin n'est requis. Les tâches douanières futures devront partager la qualification et les références locales de DOU-001 ; références métier et recette BASE-006 restent à prévoir dans chaque future story.

| Code / propriétaire proposé | Entrées déterminantes | Résultat borné et scénario attendu |
|---|---|---|
| C01 — douanes, lire la ventilation | Factures vendeur/prestataire, déclaration, sommes déjà payées, dates et régime invoqué | Tableau des postes et justificatifs à obtenir, destinataires séparés, sans calcul de taxation ; TVA au panier puis réclamée à livraison. |
| C02 — douanes, préparer une rectification | Déclaration acceptée, statut/mainlevée, erreur, auteur et preuves exactes | Brouillon de rectification après vérification de qualité, conditions, voie et délai ; transport ajouté deux fois, prestataire disant toute correction impossible. |
| C03 — douanes, préparer une invalidation | Déclaration, acceptation, motifs, retour/réexportation et état des biens | Brouillon propre après recherche des conditions, sans assimiler invalidation, correction et remboursement ; retour consommateur alors que le vendeur n'a pas remboursé. |
| C04 — douanes, marchandises en retour en l'état | Export initial, identité/série, état, trajet, dates et propriété | Dossier de régime en retour et inconnues, droits et TVA séparés ; pièce revenue intacte sans preuve de sortie. |
| C05 — douanes, retour en atelier UE pour réparation | Export initial, série, propriété, diagnostic, garantie, réparation et réexpédition | Dossier d'entrée pour SAV et régime à rechercher ; couteau revenant pour réparation pris pour achat neuf. Ne pas confondre retour en l'état, réparation et échange standard. |
| C06 — douanes, réparation hors UE | Bien initial, sortie prévue/réelle, devis, garantie, réparation ou remplacement, dates | Dossier de perfectionnement passif à rechercher avant départ ; équipement revenant avec taxation sur sa valeur entière. Pas d'autorisation rétroactive promise. |
| C07 — douanes, démonstration temporaire | Échantillons, inventaire/séries, pays, itinéraire, ventes prévues, carnet et échéances | Dossier temporaire/ATA ou e-ATA à qualifier, admission et réexportation distinctes de validité du carnet ; démonstrateur vendu pendant un salon. |
| C08 — douanes, transformation puis réexportation | Composants, opérations, quantités/rendements, autorisations, écritures et destination | Dossier de perfectionnement actif à rechercher ; stock importé pour transformation déclaré en définitif. Aucun régime accordé d'office. |
| C09 — douanes, incident de transit | MRN transit, titulaire, garantie, départ/arrivée, présentation et preuve d'apurement | Chronologie et demande documentée de vérification/régularisation ; livraison prouvée mais apurement absent. Livraison et apurement ne sont pas assimilés. |
| C10 — douanes, observations avant décision | Projet/griefs, pièces communiquées, réception, observations et pièces contraires | Brouillon contradictoire avec fondement, champ, exceptions et terme recherchés ; projet défavorable sans annexes. DOU-009 reste une lecture. |
| C11 — douanes, représentation contestée | Mandat, représentation annoncée/réelle, déclaration, données transmises, acteurs | Fiche des rôles et griefs, brouillon de demande de pièces ; destinataire nommé déclarant sans mandat compris. Responsabilité contractuelle V03 distincte de dette ou sanction. |
| C12 — douanes, contestation d'une créance | Acte intégral, dette/postes, notification, griefs, paiements, recours antérieurs | Brouillon motivé à l'autorité dont compétence est vérifiée ; AMR présenté comme incontestable. Régime français/UE et transitions à rechercher, sans reprise automatique du délai du guide. |
| C13 — douanes, suite juridictionnelle avec EXIST-006 | Réclamation, dépôt/réception, réponse/silence, notification et actes ultérieurs | Fiche de saisine puis story procédurale propre à définir, juge/représentation et terme vérifiés ; réclamation sans réponse. Pas de requête universelle. |
| C14 — douanes, demande de sursis | Créance, recours, recouvrement, demande antérieure, garanties et situation économique utile | Brouillon de sursis après vérification de conditions et effets ; contestation déposée mais poursuites continuées. Ne pas présenter tout recours comme suspensif. |
| C15 — douanes, contestation de garanties | Décision du comptable, réception, garantie proposée/refusée et procédure en cours | Dossier urgent et voie propre à rechercher avec avocat ; garantie refusée pendant un sursis. Le référé et son terme ne se déduisent pas d'un modèle générique. |
| C16 — douanes, mesure sur les biens, avec DOM-002 si pénal | Mesure complète, fondement, inventaire, service, réception, statut de la personne | Fiche de mesure et voie spécialisée à découper après qualification ; saisie appelée simple blocage. PV et transaction : lecture DOU-009 puis avocat ; aucune défense pénale ni signature dans cette tâche. |
| C17 — douanes, retenue PI, avec EXIST-008 sur le droit invoqué | Notification, droits/titulaire invoqués, biens, factures/licences, réception, réponse et destruction annoncée | Dossier urgent et brouillon de position à découper selon procédure vérifiée ; authenticité discutée et silence du destinataire. Aucun accord à destruction déduit ou envoyé par l'outil. |
| C18 — douanes, préparer une demande de RTC | Fiche technique DOU-006, opérations futures, produit et décisions existantes | Dossier/brouillon de demande distinct de conseil oral, portée et validité à rechercher ; expéditions répétées d'un couteau décrit comme outil métallique. Aucun classement opposable promis. |
| C19 — douanes, préparer une demande de RCO | Produit, matières, transformations, accord éventuel, preuves DOU-007 | Dossier de renseignement contraignant d'origine, portée et procédure à vérifier ; marquage français pris pour preuve préférentielle. |
| C20 — douanes, qualifier l'obligation EMEBI | Courrier de sélection, flux biens/services, période, activité et réponses antérieures | Fiche statistique propre et calendrier officiel à rechercher ; ancienne « DEB » utilisée pour trois objets. État récapitulatif TVA et DES restent V04. |
| C21 — douanes, restrictions d'exportation | Produit/technique, pays et transit, client, utilisateur/usage final, licences et date | Dossier de contrôle export à borner par mesure, sans autorisation certifiée ; échantillon gratuit susceptible de double usage ou destination sous sanctions. Sanctions financières et contrat bancaire séparés. |
| C22 — douanes, matières et espèces, avec DOM-014 selon objet | Identification scientifique/matière, espèce, transformation, origine/licéité, pays et documents | Dossier CITES et restrictions locales à rechercher selon spécimen ; manche décrit comme ivoire de mammouth sans preuve d'identification. Aucune exemption déduite du nom commercial. |
| C23 — douanes, emballage phytosanitaire, avec DOM-014 | Palette/caisse, matériau, traitement/marquage, pays, trajet et date | Dossier d'exigences de conditionnement à rechercher ; produit accepté mais palette bloquée. NIMP 15 à vérifier dans son champ sans certificat fabriqué. |
| C24 — douanes, couteaux à destination, avec DOM-002 selon question | Mécanisme d'ouverture, lame, dimensions utiles, vente/livraison, âge, pays/territoire et transporteur | Fiche d'admissibilité à rechercher pays par pays et clauses du prestataire ; couteau artisanal vers Canada ou Royaume-Uni. Pas d'interdiction générale de tous couteaux ni d'application de règles françaises seules. |
| C25 — douanes, demande de décision et silence | Objet précis, texte de demande, complétude, dépôt/réception, prolongations, réponses | Fiche de régime décisionnel et voie/calendrier à vérifier ; silence pris pour autorisation. Information orale, renseignement contraignant et décision formelle restent distincts. |
| C26 — douanes, vérifier la taxation d'une opération | Date, trajet/territoires, déclaration, régime, classement et origine étayés, préférence, valeur/fret/assurance, devise/conversion et prélèvements sourcés | Tableau de calcul conditionnel avec paramètres, formules, sources et écarts à la taxation facturée ; fret doublé ou seuil petits colis invoqué. Aucun calcul si un paramètre déterminant manque ; TVA autonome avec V04. Cette tâche n'est pas incluse dans DOU-001/006/007/008. |
| V01 — DOM-022 poste / DOM-008 fret selon contrat | Contrat/rôles, suivi, pièces demandées/transmises, tarifs, frais et dommage | Réclamation privée stockage/retour/inaction à découper ; pièces fournies mais jours de magasinage encore facturés. TEL-006 et TPT-010 ne couvrent pas seuls tous ces frais. |
| V02 — DOM-005 assurance transport | Police, valeur assurée, poids, limites/exclusions, sinistre et déclaration | Lecture de garantie puis brouillon ciblé selon tâche à borner ; objet léger de forte valeur. Plafond de responsabilité du transporteur distinct de garantie d'assurance. |
| V03 — EXIST-001 contrat international | Vente/mandat/transport, qualités, droit applicable, clause et version Incoterm, lieu, frais et preuve de sortie | Revue d'une clause puis réclamation contractuelle à découper séparément ; DDP annoncé mais dette réclamée à l'importateur. Aucun choix automatique FCA/EXW ni confusion avec qualité de redevable. |
| V04 — DOM-011 fiscalité / IND-027 chez DOM-039 pour indépendant | Régime TVA, identification, flux, territoire, dates, données douanières, CA3/OSS/IOSS et justificatifs | Tâches fiscales à borner : TVA import, correction/déduction, vente à distance, état récapitulatif et DES distincts ; micro en franchise croyant ne rien déclarer à l'importation. Aucune CA3 ni seuil universels. |

Les questions de frais/change/paiement bloqué restent dans les propositions [BNK-003](../suites/bnk-003-frais-bancaires.md), [BNK-014](../suites/bnk-014-blocage-compte.md), [BNK-019](../suites/bnk-019-encaissement-professionnel.md) selon contrat ; un virement professionnel n'est pas automatiquement un encaissement de plateforme. Fraude au paiement : qualifier l'opération avant orientation bancaire/pénale. Livraison, retour et remboursement du vendeur : [DOM-001](../dom-001-consommation.md). Conformité CE et sécurité produit : [EXIST-004](../../02-plugins-existants/exist-004-produits-publicite.md), avec volet douanier spécialisé distinct.

## Matrice des 75 points

Les titres reproduisent les situations du guide ; les exigences ne certifient pas que chaque pratique est illicite. « C » ou « V » signifie **tâche candidate à découper** ; une DOU désigne une proposition existante, jamais une fonction livrée.

| Point | Situation fournie | Ancrage / candidats | Exigence de réponse future |
|---|---|---|---|
| 1 | Les « frais de douane » qui ne sont pas des droits de douane | C01, V01 | Ventiler taxes publiques et honoraires, demander déclaration et contrat ; ne pas présumer que toute somme est due ou abusive. |
| 2 | La TVA réclamée deux fois | C01, C02, V04 | Rapprocher TVA au panier et à l'importation, facture et circuit IOSS ; choisir correction et éventuel remboursement sans double restitution. |
| 3 | Le seuil de 150 € présenté comme une exonération générale | C01, C26 | Rechercher régime, date, catégorie tarifaire et unité d'imposition ; ne confirmer aucun seuil, forfait ou suspension du guide. |
| 4 | La TVA calculée sur un montant supérieur au prix du produit | DOU-008, C01, V04, C26 | Distinguer valeur douanière et assiette TVA, frais et droits ; demander calcul détaillé et repérer doublons sans taxer. |
| 5 | Les frais de dédouanement facturés après la livraison | V01, V03, C01 | Vérifier information, contrat, prestation et avances réellement effectuées ; livraison passée ne suffit pas à établir la créance privée. |
| 6 | Le « paiement obligatoire avant livraison » utilisé abusivement | C01, V01 | Identifier émetteur authentique, somme et déblocage possible ; ne conseiller ni paiement aveugle ni refus global sans conséquences examinées. |
| 7 | Les droits facturés sur une mauvaise valeur | DOU-008, C02, C26 | Confronter valeur déclarée, transaction et ajustements requis aux justificatifs ; prix payé seul insuffisant pour arrêter valeur. |
| 8 | Les frais de transport comptés deux fois | DOU-008, C02, V03, C26 | Rapprocher facture, fret et clause de livraison ; isoler transport inclus et ajouté sans arrêter l'assiette. |
| 9 | Le cadeau déclaré qui n'en est pas un | DOU-001, DOU-004 | Qualifier vente ou vrai cadeau privé ; aucune fausse mention Gift ni franchise depuis une étiquette. |
| 10 | La facture artificiellement minorée | DOU-008, C02, C11 | Conserver prix réel et données transmises, préparer correction à vérifier ; aucune facture minorée proposée. |
| 11 | Le fractionnement artificiel des commandes | DOU-001, DOU-004, C01 | Reconstituer commandes, paiements et expéditions réelles ; aucun montage de fractionnement pour contourner une règle. |
| 12 | La mauvaise application d'un taux réduit ou nul | DOU-006, C18, V04, C26 | Qualifier précisément produit, nomenclature et régime fiscal ; code ou RTC ne détermine pas seul tout taux. |
| 13 | Le colis prétendument « bloqué par la douane » | DOU-001, V01, DOU-009 | Identifier blocage logistique, pièce manquante ou contrôle officiel ; suivi ne prouve pas une décision douanière. |
| 14 | Les documents demandés au compte-gouttes | DOU-001, DOU-004, V01 | Inventorier pièces utiles, demandes et dates de transmission ; demander liste consolidée sans promettre un dossier universel complet. |
| 15 | Les frais de stockage provoqués par l'inaction du transporteur | V01 | Documenter tarifs, jours, demandes et pièces fournies, cause du retard ; brouillon de contestation ciblée à découper. |
| 16 | L'immobilisation sans information exploitable | DOU-001, DOU-009, V01 | Demander déclaration/MRN s'il existe, bureau, statut réel et action attendue ; ne pas laisser un suivi vague masquer une urgence. |
| 17 | Le choix imposé entre payer, retourner ou abandonner | C02, C03, V01 | Vérifier alternatives selon statut/régime, coûts et pouvoir du représentant ; pas de correction, réexportation ou changement garanti. |
| 18 | Le retour automatique aux frais de l'expéditeur | V01, V03, DOM-001 | Examiner refus, clauses de retour, responsabilités et factures ; refus de livraison ne garantit ni gratuité ni remboursement commercial. |
| 19 | La destruction ou l'abandon de marchandise | C16, C17, V01 | Identifier acte, auteur, fondement et terme, distinguer abandon privé et destruction officielle ; conseil urgent avant perte irréversible. |
| 20 | Le dépôt temporaire considéré comme illimité | DOU-004, V01 | Vérifier placement en IST, date et suite du régime ; durée réglementaire distincte du tarif et des jours gratuits. |
| 21 | L'assurance transport qui couvre beaucoup moins que prévu | V02, V01 | Lire police, poids/valeur, exclusions et délais propres ; garantie souscrite distincte de responsabilité du transporteur. |
| 22 | Le transporteur qui refuse d'indemniser en invoquant la douane | V01, V02 | Confronter chronologie du dommage, contrôle allégué, contrat et preuves ; aucune exonération automatique du prestataire. |
| 23 | Le vendeur qui renvoie systématiquement le consommateur vers le transporteur | DOM-001, V01 | Qualifier vente B2C, droit applicable et choix du transporteur ; obligation du vendeur distincte de réclamation postale. |
| 24 | Les fausses demandes de paiement des douanes | BNK-001, BNK-002, DOM-002 | Vérifier identité par canal connu sans suivre lien reçu ; si paiement, qualifier autorisation/tromperie et preuves avant voie bancaire/pénale. |
| 25 | Le mauvais code douanier | DOU-006, C18, C26 | Fiche technique, code réellement déclaré, nomenclature et mesures à rechercher ; aucun code fiable déduit du nom commercial. |
| 26 | La classification laissée entièrement au transporteur | DOU-006, C11 | Fournir caractéristiques et contrôler déclaration, mandat et données ; transporteur ne devient pas seul responsable par automatisme. |
| 27 | Confondre provenance et origine douanière | DOU-007 | Tracer fabrication/transformation et expédition séparées ; entrepôt européen ne prouve pas origine UE. |
| 28 | Croire que le « Made in France » suffit pour obtenir un droit réduit | DOU-007, C19 | Séparer marquage, origine non préférentielle et origine par accord ; aucune préférence depuis Made in France seul. |
| 29 | La preuve d'origine préférentielle oubliée | DOU-007 | Identifier accord, produit, preuve et auteur admissibles avant promesse de taux réduit. |
| 30 | Les mentions d'origine improvisées sur les factures | DOU-007, C19 | Rechercher formule, qualité/identifiant d'exportateur et seuil propres à l'accord ; ne pas improviser French origin. |
| 31 | L'exportateur qui ne peut pas prouver l'origine de ses matières | DOU-007 | Relier matières, fournisseurs et transformations aux preuves ; déclaration fournisseur discutée si incohérente. |
| 32 | Le mauvais régime douanier sélectionné | DOU-004, DOU-005, C04–C09 | Qualifier intention, propriété, état et trajet avant régime ; définitif, retour, transit et temporaire ont des conditions distinctes. |
| 33 | La déclaration faite au mauvais nom | DOU-004, C11 | Lire déclaration/mandat, représentation et qualité de chaque acteur ; dette et responsabilité contractuelle séparées. |
| 34 | La rectification présentée comme impossible | C02, C03 | Identifier acceptation/mainlevée, erreur et qualité ; rechercher rectification ou invalidation sans délai commun. |
| 35 | Les Incoterms absents du contrat | V03, DOU-004, DOU-005 | Identifier clause, version, lieu et répartition des formalités ; livraison comprise ne suffit pas. |
| 36 | La confusion entre DAP et DDP | V03, C11 | Lire DAP/DDP convenu et capacité de réalisation ; domicile livré ne prouve pas toutes taxes payées. |
| 37 | Le DDP qui se transforme en refacturation surprise | V03, C12, C01 | Réclamation contractuelle au vendeur distincte de dette publique ; qualifier redevable réel et poste refacturé. |
| 38 | L'EXW utilisé alors qu'il complique l'exportation | V03, DOU-005, V04 | Examiner maîtrise de sortie et justificatifs fiscaux selon contrat ; aucun remplacement automatique EXW par FCA. |
| 39 | L'exportation hors UE sans preuve de sortie | DOU-005, V04 | Rapprocher export, sortie effective et preuves admises ; facture hors TVA ne prouve pas la sortie. |
| 40 | Le numéro EORI absent ou incorrect | DOU-004 | Identifier opérateur, EORI, TVA et habilitations, vérifier migration applicable ; aucun identifiant ou calendrier confirmé de mémoire. |
| 41 | L'autoliquidation de TVA mal comprise | V04, C01 | Rapprocher données douanières et déclaration fiscale, période et corrections ; absence de décaissement ne prouve pas absence d'obligation. |
| 42 | Le piège spécifique des microentrepreneurs en franchise de TVA | V04, IND-027, DOU-004 | Qualifier franchise, importation et identification avant rubriques/CA3 et déduction ; aucune solution universelle micro. |
| 43 | Le seuil des ventes à distance dans l'UE oublié | V04, IND-027 | Qualifier ventes biens/services, pays/qualité et CA pertinent ; seuil, localisation, OSS et franchises à rechercher séparément. |
| 44 | La DEB considérée comme une formalité unique | C20, V04 | Séparer sélection EMEBI, état récapitulatif TVA et DES ; calendrier propre à chaque obligation. |
| 45 | Une commission de change ou des frais de paiement international cachés | BNK-003, BNK-019, V03 | Comparer devise, taux, frais correspondants et répartition contractuelle ; aucun frais bancaire qualifié droit douanier. |
| 46 | Une marchandise livrée, mais une somme encore retenue par la banque | BNK-014, BNK-019, C21 | Identifier blocage compte/virement/encaissement et pièces économiques ; ne pas présumer illégalité ni conseiller contournement des contrôles. |
| 47 | Le produit retourné qui est taxé une deuxième fois | C05, C04, C02 | Reconstituer export initial, série, motif et réparation/échange ; rechercher régime adapté sans facturer une vente fictive. |
| 48 | Le régime des marchandises en retour oublié | C04, V04 | Prouver identité, export, état et dates ; exonération droits et TVA examinées séparément. |
| 49 | La réparation à l'étranger qui devient une nouvelle importation | C06, DOU-008 | Documenter bien, réparation ou remplacement et frais, autorisation/régime avant départ ; aucune exonération automatique sur seule facture SAV. |
| 50 | Les échantillons commerciaux traités comme des ventes | C07, C21 | Démonstration, biens vendus et pays distingués ; carnet accepté, validité et apurement à rechercher. |
| 51 | Les marchandises destinées à être transformées taxées comme des produits définitifs | C08 | Documenter composants, opérations et réexportation, autorisations et écritures ; pas de suspension de droits accordée automatiquement. |
| 52 | Le retour commercial confondu avec un droit automatique au remboursement | C03, DOU-010, DOU-011, V01, V04 | Séparer remboursement vendeur, invalidation, droits, TVA et honoraires ; ne pas attendre issue commerciale pour identifier échéance formelle. |
| 53 | Le produit légal en France mais interdit à destination | C21, C24, EXIST-004 | Vérifier export, import destination, licences et utilisateur/usage ; légalité française ne prouve pas admission étrangère. |
| 54 | La conformité CE présentée comme un passeport mondial | EXIST-004 | Identifier texte produit, marché, rôle et exigences locales ; ni CE universel ni conformité mondiale certifiée. |
| 55 | Les matériaux d'origine animale ou végétale protégés | C22 | Identifier espèce/matière et licéité, annexes et permis selon trajet ; pas de CITES déclenchée par tout bois ou cuir. |
| 56 | Les produits soumis à embargo ou à double usage | C21, BNK-014 | Qualifier technique, client, usage final et sanctions applicables ; gratuité et temporaire ne valent pas dispense. |
| 57 | Les emballages en bois qui bloquent l'expédition | C23 | Identifier emballage séparément du produit et exigences pays/date ; traitement ou marquage à vérifier sans attestation inventée. |
| 58 | Les restrictions propres aux couteaux et objets tranchants | C24, DOM-002 | Caractéristiques mécaniques, pays/territoire, vente/livraison et politique transporteur séparés ; recherche UK/Canada sans généralisation. |
| 59 | Le contrôle après dédouanement | DOU-004, DOU-009, C10 | Conserver pièces et versions de classement/origine/valeur ; dédouanement ne prouve pas absence de contrôle ultérieur. |
| 60 | Le droit d'être entendu méconnu | DOU-009, C10 | Dater projet/réception, rechercher droit d'être entendu et exceptions ; observations distinctes du recours contre décision finale. |
| 61 | Le procès-verbal signé sans réserves | DOU-009, DOM-002 | Lire PV et déclarations attribuées, erreurs et copies, avocat selon statut ; ni signature ni refus universel recommandé. |
| 62 | La transaction douanière acceptée trop rapidement | DOU-009, DOM-002, V03 | Identifier faits reconnus, dette, pénalités et portée avant examen par avocat ; aucune transaction rédigée ou acceptée dans cette intégration. |
| 63 | Une suspicion de contrefaçon traitée comme une preuve définitive | C17, EXIST-008 | Séparer suspicion, titre invoqué, authenticité et procédure ; notification/destruction et réponse urgentes avant toute conclusion PI. |
| 64 | Une saisie dont le fondement n'est pas compris | DOU-009, C16, DOM-002 | Qualifier contrôle, immobilisation, retenue, saisie et confiscation avec acte/fondement propres ; pas de recours commun présumé. |
| 65 | La responsabilité du représentant en douane mal définie | C11, V03 | Contrôler mandat, type de représentation et données de chacun ; auteur matériel ne porte pas seul toute dette ou faute. |
| 66 | Les erreurs de transit non apurées | C09 | Rapprocher transit, présentation, livraison, garantie et apurement ; preuve de livraison seule insuffisante pour clôturer le régime. |
| 67 | Croire qu'un avis de mise en recouvrement est incontestable | C12, DOU-009 | Lire AMR, bases et notification, qualifier voie française/UE et transitions ; recours motivé à préparer dans sa tâche propre. |
| 68 | Le délai de recours judiciaire oublié | C13, EXIST-006 | Dater dépôt/réception, réponse ou silence, vérifier juge et représentation ; pas de délai judiciaire transposé aux autres décisions. |
| 69 | Le recours qui ne suspend pas automatiquement le paiement | C14, C12 | Séparer contestation, exigibilité et recouvrement ; demande de sursis propre et effets à vérifier. |
| 70 | Les garanties contestées trop tard | C15, C14 | Décision du comptable et réception en tête, avocat et régime propre ; garanties et remise pour difficultés ne sont pas assimilées. |
| 71 | Le trop-perçu jamais réclamé | DOU-010, DOU-011 | Distinguer payé/non payé, motif et conditions, notification et qualité ; aucun remboursement automatique ni délai unique CDU. |
| 72 | Le remboursement pour marchandise défectueuse demandé trop tard | DOU-010, DOU-011, C03 | Prouver défaut/non-conformité, état/utilisation, retour et dates ; fondement particulier distinct du simple changement d'avis. |
| 73 | La réponse orale prise pour une décision sécurisante | C18, C19, C25 | Distinguer aide orale, écrit d'information et décision formelle opposable ; portée d'un RTC/RCO à rechercher. |
| 74 | Le silence administratif considéré comme un accord | C25, C13 | Qualifier demande, recevabilité, complétude, prolongations et silence ; aucune autorisation tacite générale. |
| 75 | Le mauvais interlocuteur saisi pour la réclamation | C01, V01, V04, C12 | Attribuer chaque poste/acte au bon destinataire, calendrier et objectif ; médiation ou demande informelle ne remplace pas le recours requis. |

## Assertions du guide à vérifier avant toute réponse au fond

Les éléments suivants sont des **allégations reçues**, pas des règles adoptées. Rechercher le texte exact, sa version, son champ, transitions et exceptions ; conserver la voie d'accès et les passages lus. Les liens de ressources dans la source sont des pistes non consultées dans ce lot ; leurs coordonnées et disponibilité ne sont pas certifiées.

| Affirmation reçue | Travail de recherche requis / tâches |
|---|---|
| Point 3 : droit UE de 3 € par catégorie jusqu'à 150 € depuis juillet 2026 ; taxe française de 2 € de mars à juin puis suspension | C01 : actes UE/français, dates d'application, assiette/unité, opérations et exclusions, articulation des prélèvements. Aucun exemple 6/15 € repris comme calcul validé. |
| Points 2/4/41/42 : IOSS, assiette, autoliquidation depuis 2022, CA3 et absence de déduction du micro en franchise | V04/C01/DOU-008 : statut TVA et opérations exactes, champ, rubriques et correction ; déterminer le bon destinataire sans promettre remboursement double. |
| Points 29/30 : preuves d'origine, formule et seuil de 6 000 € | DOU-007/C19 : accord, produit, règles de transformation, preuve et statut d'exportateur ; aucun seuil commun à tous accords. |
| Point 40 : migration EORI vers SIREN en 2026 et gratuité | DOU-004 : calendrier officiel et transition propres à l'opérateur/application ; EORI, numéro TVA et habilitations distincts. |
| Points 43/44 : seuil ventes B2C UE de 10 000 €, OSS et EMEBI/état TVA/DES | V04/C20 : champ, qualité, franchise éventuelle, biens/services, sélection statistique et calendrier propre ; pas d'obligation unique « DEB ». |
| Points 35–38 : répartition DAP/DDP, intérêt de FCA plutôt qu'EXW | V03 : règles ICC de la version contractuelle et droit applicable, lieu/clauses, rôles douaniers et preuve fiscale ; tableau simplifié du guide insuffisant. |
| Points 48–51 : retour en l'état, perfectionnement, ATA/e-ATA | C04–C08 : conditions d'autorisation, identification, garantie, apurement, pays et preuve de sortie ; droits et TVA distincts. |
| Points 53–58 et section coutellerie : CE, sécurité générale depuis décembre 2024, CITES/mammouth, sanctions, NIMP 15, couteaux UK/Canada | EXIST-004/C21–C24 : texte par produit/matière/pays/opération et date ; réglementation française/UE, destination et politique transporteur séparées. |
| Point 24 : absence de demande directe de droits par SMS/courriel émis par la douane | Vérifier consignes officielles d'identification de l'émetteur ; ne pas déduire authenticité ou fraude du seul canal ni cliquer sur un lien suspect. |
| Points 60/63/67–74 : contradiction, retenue PI, recodification en mai 2026, L331-1/2, L332-2/3 et CDU | C10/C12–C17/C25 et DOU-010/011 : versions et dispositions transitoires, dette/acte précis, préalable, juge et effets propres ; tableau ci-dessous reste une liste de recherches. |

## Les quinze lignes du calendrier source

Chaque nombre est une assertion du guide, **non vérifiée ici**. Le futur calendrier établit événement de départ, preuve, unité, champ, prolongations, interruptions/suspensions et acte à accomplir. La date imprimée n'est pas assimilée à réception. Rechercher aussi les termes absents du tableau : recours contre saisie, apurement des régimes, signalement sinistre, réclamation transport et banque, retour commercial et médiation selon objet.

| Ligne | Objet et repère annoncé par le guide | Propriétaire / distinctions à rechercher |
|---|---|---|
| D01 | Observations : 30 jours en principe | C10 : projet, communication, exceptions et terme propre. |
| D02 | Retenue PI : 10 jours ouvrables / 3 denrées périssables | C17/EXIST-008 : procédure, destinataire, réception, prolongation et destruction. |
| D03 | Invalidation : généralement 90 jours | C03 : acceptation et motif, conditions et exceptions ; retour commercial distinct. |
| D04 | Rectification après mainlevée : jusqu'à 3 ans | C02 : acceptation, qualité, statut, motif et admissibilité. |
| D05 | Défectueux/non conforme : 1 an | DOU-010/011 : motif propre, notification, utilisation/retour et conditions. |
| D06 | Trop-perçu/autres motifs : 3 ans | DOU-010/011 : fondement, notification, preuve de paiement et exceptions. |
| D07 | Créance relevant de L331-1 : 3 ans | C12 : régime, notification et articulation avec droit UE/transitions. |
| D08 | Réponse à contestation : 6 mois | C12/C13 : dépôt/réception, demande complète et effet du silence. |
| D09 | Saisine relevant de L332-2 : 2 mois | C13 : réponse ou silence, juge et représentation à vérifier. |
| D10 | Référé garanties : 15 jours | C15 : décision exacte, notification, conditions et juge propres. |
| D11 | Décision sur demande article 22 CDU : 120 jours prolongeables | C25 : recevabilité, complétude, départ, prolongations et recours ; aucun accord tacite général. |
| D12 | Stockage temporaire IST : maximum 90 jours | DOU-004/V01 : placement réel, événement de départ et suite ; aucune gratuité commerciale déduite. |
| D13 | Marchandises en retour : généralement 3 ans | C04 : export initial, état, identité, exceptions et TVA séparée. |
| D14 | Carnet ATA : généralement 12 mois | C07 : validité du carnet, admission et réexportation/apurement distincts. |
| D15 | EMEBI : 10e jour ouvrable après le mois | C20 : obligation/sélection et calendrier officiel mois/année ; pas de transposition à DES/état TVA. |

## Les dix réflexes du guide comme exigences de sortie

| Ligne | Réflexe reçu | Sortie attendue |
|---|---|---|
| R01 | Identifier nature du problème | Table des objets dette/TVA/frais/blocage/contrôle/sanction/litige, avec propriétaire par question. |
| R02 | Obtenir références exactes | Inventaire déclaration/MRN, facture, dossier et service disponibles/manquants. |
| R03 | Demander motivation écrite | Brouillon ciblé : règle, postes, pièces et stade ; sans attendre la réponse pour qualifier une urgence. |
| R04 | Conserver échanges et preuves | Chronologie des demandes, pièces transmises, accusés et suivi, avec provenance et données minimisées. |
| R05 | Identifier immédiatement les délais | Calendrier sourcé par acte, avec inconnues ; aucune échéance reprise mécaniquement du guide. |
| R06 | Éviter reconnaissances précipitées | PV/transaction et faits contestés identifiés, aide d'un avocat avant engagement ; aucune signature/refus universel conseillé. |
| R07 | Contester précisément | Tableau grief / pièce / règle recherchée / demande ; brouillon seulement dans la tâche pertinente. |
| R08 | Séparer paiement et recours | État dette/paiements/recours/sursis/garanties avec voies et effets propres. |
| R09 | Documenter frais consécutifs | Tableau dates, postes, montant, contrat et causalité à prouver, sans indemnisation promise. |
| R10 | Saisir le bon interlocuteur | Destinataire par poste, rôle de douane/fisc/vendeur/prestataire/banque/médiateur/juge distinct ; aucun envoi automatique. |

## Les cinq dossiers coutellerie

Ils ne prouvent ni que l'utilisateur exerce cette activité ni que toutes les matières sont réglementées. Recueillir les faits avant d'ouvrir le parcours ; le guide décrit des besoins particuliers à conserver.

| Ligne | Dossier | Exigence et scénario futur |
|---|---|---|
| K01 | Couteaux, destination et transporteur | C24/C21 : caractéristiques mécaniques et pays, vente/livraison/âge et clauses ; couteau de poche artisanal vers UK ou Canada, sans assimilation automatique à une arme prohibée. |
| K02 | Matières des manches | C22/C23 : espèce/matière identifiée, acquisition et documents ; mammouth annoncé sans preuve, bois du manche distinct de palette et règle locale distincte de CITES. |
| K03 | Retours SAV | C04/C05/C06 et C02/C03 selon cas : série, première sortie, propriété, retour et réparation/échange ; couteau réparé en atelier puis réexpédié, sans déclaration de vente fictive. |
| K04 | Origine française | DOU-007/C19 : preuves de fabrication et transformations, composants et accord ; marquage français documenté mais preuve préférentielle absente. |
| K05 | Ventes hors UE | DOU-005/V03/V04/V01 : CGV, Incoterm, représentant, preuve de sortie, taxes et retour/refus ; vente DDP refusée et transport retour facturé, sans confondre contrat, dette publique et exonération fiscale. |

## Découpage et couverture restant à réaliser

La matrice couvre la traçabilité des besoins ; elle ne signifie pas que les 75 réponses sont disponibles. C01–C26 et V01–V04 exigent encore des stories bornées, sources et recettes, avec confirmation des propriétaires proposés. C26 permet de prévoir une vraie vérification chiffrée distincte des dossiers préparatoires, avec faits et paramètres sourcés. Prioriser les échéances/destructions pour le futur découpage C10/C12–C17, et les parcours coutellerie C04–C07/C22/C24, sans les sélectionner automatiquement ni élargir DOU-001.

PV, transaction et défense pénale nécessitent leur propre découpage DOM-002 avec spécialiste douanier ; DOU-009/C16 ne les implémentent pas. Recouvrement forcé : DOM-003 après qualification de l'acte. Médiation économique/financière : régime, recevabilité et effets sur chaque calendrier à préciser dans une tâche séparée ; aucune médiation considérée comme un recours ou une suspension générale. Préparer également le volet conformité EXIST-004, droits PI EXIST-008 et les tâches privées V01–V04 sans les attribuer fictivement aux suites de simple orientation.
