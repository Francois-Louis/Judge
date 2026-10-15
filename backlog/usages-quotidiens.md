# Situations du quotidien — matrice de couverture

L'objectif est d'aider une personne à comprendre ce qu'on lui demande, repérer
une erreur ou un abus possible, rassembler ses pièces et préparer une démarche
utile. La couverture se mesure aussi par les situations traitées, au-delà du
nombre de codes cités ou de plugins créés.

Cette matrice décrit des usages à construire. Les liens mènent à des stories
de cadrage, d'audit ou d'implémentation, et ne prouvent pas la disponibilité
d'une fonctionnalité. La qualification exacte
dépend du document, du statut des parties et des faits ; une même situation
peut comporter plusieurs demandes avec un domaine principal pour chacune.

Le [dossier d'architecture BASE-003](00-fondations/base-003-dossier-architecture.md)
associe ces domaines à leur plugin principal, précise les interactions et
vérifie le routage pour les particuliers, aidants, indépendants et petits
exploitants. Les nouveaux plugins restent proposés jusqu'à leur cadrage.

Le [protocole USAGE-001](05-usages-quotidiens/usage-001-protocole-orientation.md)
définit les questions minimales, la restitution, l'accessibilité et les limites
de collecte et d'envoi. Les colonnes « Domaine principal » et « Frontière »
forment l'index documentaire ; la correspondance vers les plugins et leur état
reste dans BASE-003. Chaque domaine principal est retenu pour la tâche exprimée,
sous réserve des faits discriminants de la dernière colonne. Une question
complémentaire ouvre une tâche distincte seulement si elle est utile.

## Sorties à privilégier

- Une explication courte du document, de la somme ou de l'obligation.
- Les faits établis et les vérifications qui peuvent changer la réponse.
- Les pièces utiles et les dates dont il faut obtenir la preuve.
- Une prochaine étape concrète, ses conditions et le bon interlocuteur.
- Si demandé, un décompte lisible ou un brouillon de courrier appuyé sur les pièces.

Les règles et recours doivent être vérifiés avant d'être appliqués. Une
contestation n'établit pas à elle seule un abus ; une démarche préparée ne
garantit pas le résultat. Les urgences de sécurité ou de procédure sont traitées
avant une revue documentaire ordinaire.

## Logement, propriété et travaux

| Situation exprimée | Domaine principal | Cadrage ou pilote | Premier résultat utile | Frontière et question complémentaire |
|---|---|---|---|---|
| Le bailleur retient mon dépôt ou me réclame des charges. | Logement locatif | [DOM-006](03-nouveaux-domaines/dom-006-logement.md) | Comprendre le décompte et préparer une demande de justificatifs. | Bailleur/agence ; acte d'expulsion → DOM-003, charges du copropriétaire → DOM-018. |
| Le devis change ou le chantier reste inachevé. | Construction et travaux | [DOM-015](03-nouveaux-domaines/dom-015-construction-travaux.md) | Comparer contrat, accords et paiements ; organiser la réclamation. | Artisan/entrepreneur ; permis → DOM-019, vote de travaux → DOM-018, refus d'assurance → DOM-005. |
| Je ne comprends pas ce que je signe pour acheter un logement. | Achat et vente immobilière | [DOM-017](03-nouveaux-domaines/dom-017-transactions-immobilieres.md) | Identifier acte, engagements et pièces manquantes. | Notaire/vendeur ; prêt → DOM-004, travaux → DOM-015, bail → DOM-006. |
| Le syndic réclame des charges ou fait voter des travaux. | Copropriété | [DOM-018](03-nouveaux-domaines/dom-018-copropriete.md) | Lire décompte, règlement et décision ; distinguer les contestations. | Syndic/syndicat ; charges réclamées au locataire → DOM-006, malfaçons → DOM-015. |
| La mairie refuse mon projet ou des travaux voisins m'affectent. | Urbanisme et foncier | [DOM-019](03-nouveaux-domaines/dom-019-urbanisme-foncier.md) | Qualifier décision et documents locaux à consulter. | Service instructeur/mairie ; servitude privée → DOM-020, pollution → DOM-030. |
| Un voisin conteste une limite, une haie ou un passage. | Voisinage et servitudes | [DOM-020](03-nouveaux-domaines/dom-020-voisinage-servitudes.md) | Préparer titres, chronologie et preuves utiles. | Voisin/conseil ; autorisation publique → DOM-019, pollution → DOM-030. |
| Une activité semble polluer mon terrain ou mon voisinage. | Environnement | [DOM-030](03-nouveaux-domaines/dom-030-environnement-pollutions.md) | Structurer observations et signalement sans présumer la causalité. | Autorité compétente selon activité/lieu ; voisinage privé → DOM-020, exploitation agricole → DOM-014. |

## Argent, achats et services essentiels

| Situation exprimée | Domaine principal | Cadrage ou pilote | Premier résultat utile | Frontière et question complémentaire |
|---|---|---|---|---|
| Ma commande n'arrive pas ou le produit est défectueux. | Consommation | [DOM-001](03-nouveaux-domaines/dom-001-consommation.md) | Qualifier la demande au vendeur et préparer les pièces. | Vendeur ; paiement → DOM-004, livraison due par l'opérateur postal → DOM-022. Les secteurs spécialisés gardent leurs litiges. |
| Je conteste un débit ou une réponse de ma banque. | Banque | [DOM-004](03-nouveaux-domaines/dom-004-banque.md) | Identifier l'opération et l'objet exact de la réclamation. | Prestataire de paiement/prêteur ; garantie d'assurance → DOM-005, difficulté globale → DOM-024. |
| L'assureur refuse de couvrir le sinistre. | Assurance | [DOM-005](03-nouveaux-domaines/dom-005-assurance.md) | Comparer refus, contrat et pièces manquantes. | Assureur ; crédit → DOM-004, responsabilité du dommage → secteur ou DOM-035. |
| Une facture d'énergie ou d'eau me paraît incohérente. | Énergie et eau | [DOM-021](03-nouveaux-domaines/dom-021-energie-eau.md) | Reconstituer période, index, prix et demandes d'explication. | Fournisseur/gestionnaire ; charges du bailleur → DOM-006, travaux énergétiques → DOM-015. |
| L'opérateur facture des frais ou du matériel déjà rendu. | Télécoms et poste | [DOM-022](03-nouveaux-domaines/dom-022-telecoms-poste.md) | Comparer contrat, factures et preuves de restitution. | Opérateur ; non-livraison due par le vendeur → DOM-001, modération de plateforme → DOM-034. |
| Le garage ou le loueur me réclame une somme contestée. | Véhicules et garages | [DOM-023](03-nouveaux-domaines/dom-023-vehicules-garages.md) | Comparer travaux autorisés, état du véhicule et décompte. | Garage/vendeur/loueur ; assurance → DOM-005, infraction → DOM-002, dommage corporel → qualification sectorielle avec DOM-035. |
| Je n'arrive plus à payer plusieurs dettes. | Dettes et surendettement | [DOM-024](03-nouveaux-domaines/dom-024-dettes-surendettement.md) | Organiser situation et courriers ; distinguer les démarches. | Organisme du dossier/créanciers ; saisie → DOM-003, bien-fondé du crédit → DOM-004. Difficultés professionnelles à qualifier séparément. |
| Je reçois un acte de saisie ou une demande de recouvrement. | Recouvrement et exécution | [DOM-003](03-nouveaux-domaines/dom-003-commissaires-justice-execution.md) | Identifier acte, émetteur, notification et informations urgentes. | Acte de saisie/exécution à lire en priorité ; une simple relance reste au domaine de la dette. Le fond locatif ou bancaire reste distinct ; la qualité de l'émetteur ne suffit pas. |
| L'administration fiscale réclame une somme que je ne comprends pas. | Fiscalité | [DOM-011](03-nouveaux-domaines/dom-011-fiscalite.md) | Identifier l'impôt, la période et le stade de la procédure. | Service fiscal ; transmission successorale → DOM-016, acte d'exécution distinct → DOM-003 après qualification du régime. |
| Mon colis importé est bloqué ou des droits sont réclamés. | Douanes | [DOM-009](03-nouveaux-domaines/dom-009-douanes.md) | Identifier marchandise, territoire, documents et acte reçu. | Douane/transporteur selon l'acte ; obligation du vendeur → DOM-001, impôt hors douane → DOM-011. |

## Travail, activité et parcours de vie

| Situation exprimée | Domaine principal | Cadrage ou pilote | Premier résultat utile | Frontière et question complémentaire |
|---|---|---|---|---|
| Je veux comprendre le contrat de travail qu'on me propose. | Travail privé — contrat proposé au candidat | [PILOTE-002](01-pilote-travail/pilote-002-revue-embauche.md) | Expliquer engagements et questions à poser avant signature. | Recruteur pour engagements avant signature ; statut public à qualifier : DOM-037. Skill hiring-review existant, adaptation France/UE encore proposée. |
| Je conteste mon salaire ou une décision de mon employeur privé. | Travail privé — relation d'emploi | [PILOTE-001](01-pilote-travail/pilote-001-inventaire-travail.md) | Découper le futur workflow selon la demande et les pièces. | Employeur pour salaire/décision ; caisse : DOM-012, pension : DOM-036, emploi public selon statut : DOM-037. Audit réalisé, tâches encore à adapter. |
| Une décision affecte mon emploi dans le public. | Fonction publique | [DOM-037](03-nouveaux-domaines/dom-037-fonction-publique.md) | Identifier statut, décision et régime pertinent. | Employeur/service RH pour décision de carrière ; employeur public seul insuffisant. Emploi privé : travail, pension : DOM-036, caisse : DOM-012. |
| Une période manque à ma carrière ou ma pension semble erronée. | Retraites | [DOM-036](03-nouveaux-domaines/dom-036-retraites.md) | Préparer les éléments à vérifier auprès du régime concerné. | Régime de retraite concerné ; litige employeur → travail privé ou DOM-037, autres prestations → DOM-012. |
| Une caisse me réclame un indu ou refuse une prestation. | Protection sociale | [DOM-012](03-nouveaux-domaines/dom-012-protection-sociale.md) | Lire motif, période, décision et justificatifs nécessaires. | Caisse/organisme émetteur, dont MSA selon statut ; retraite → DOM-036, reconnaissance du handicap → DOM-025. |
| Une école ou un organisme de formation m'oppose une décision. | Éducation et formation | [DOM-027](03-nouveaux-domaines/dom-027-education-formation.md) | Distinguer statut de l'établissement et contrat ou décision. | Établissement ; apprentissage salarié → travail privé, handicap → DOM-025, aides → DOM-012. |
| Mon client professionnel ne paie pas ou conteste mon contrat. | Contrats professionnels B2B | [EXIST-001](02-plugins-existants/exist-001-contrats-commerciaux.md) | Préparer la revue du contrat et la demande de l'indépendant. | Client professionnel pour contrat courant ; client particulier/travaux : DOM-015 ou secteur B2C. Le statut professionnel du demandeur seul ne suffit pas ; acte d'exécution distinct : DOM-003. |
| Mon bail agricole ou un décompte de fermage pose problème. | Agriculture et rural | [DOM-014](03-nouveaux-domaines/dom-014-agriculture-rural.md) | Qualifier l'occupation, les pièces et les sommes à vérifier. | Bailleur/preneur ; caisse MSA → DOM-012, salarié agricole → travail privé, succession → DOM-016. |
| L'association ou le club m'exclut ou conserve une somme. | Associations | [DOM-032](03-nouveaux-domaines/dom-032-associations-adherents.md) | Distinguer statuts, décision, cotisation et service vendu. | Organe associatif ; service vendu → DOM-001 ou secteur, salarié → travail privé, accident → DOM-035 ou secteur. |

## Famille, santé et protection

| Situation exprimée | Domaine principal | Cadrage ou pilote | Premier résultat utile | Frontière et question complémentaire |
|---|---|---|---|---|
| Une décision organise la séparation ou les frais des enfants. | Famille et couple | [DOM-013](03-nouveaux-domaines/dom-013-famille-patrimoine.md) | Extraire obligations, pièces et points restant à éclaircir. | Conseil/notaire ou juridiction identifiée ; succession → DOM-016, besoin de protection contre des violences → DOM-038. |
| Je suis confronté à des violences au sein de la famille. | Violences intrafamiliales | [DOM-038](03-nouveaux-domaines/dom-038-violences-intrafamiliales.md) | Prévoir une orientation sûre et des démarches de protection adaptées. | Interlocuteur de protection adapté à la situation ; qualification pénale → DOM-002, séparation → DOM-013, logement → DOM-006, soins → DOM-007. |
| Je ne comprends pas un courrier du notaire après un décès. | Successions et donations | [DOM-016](03-nouveaux-domaines/dom-016-successions-donations.md) | Identifier les décisions concernées et préparer les questions. | Notaire/cohéritiers ; obsèques → DOM-031, fiscalité → DOM-011, pouvoirs d'un majeur protégé → DOM-026. |
| Un devis ou une facture d'obsèques me semble injustifié. | Décès et obsèques | [DOM-031](03-nouveaux-domaines/dom-031-deces-obseques.md) | Comparer prestations, documents et qualité des intervenants. | Opérateur funéraire/signataire ; succession → DOM-016, contrat d'assurance → DOM-005. |
| Je veux accéder à mon dossier médical ou contester une prise en charge. | Santé | [DOM-007](03-nouveaux-domaines/dom-007-sante.md) | Identifier demande, qualité, établissement et interlocuteur. | Professionnel/établissement ; prestation de caisse → DOM-012, garantie privée → DOM-005. |
| Une décision liée au handicap ou à l'autonomie est contestée. | Handicap et autonomie | [DOM-025](03-nouveaux-domaines/dom-025-handicap-autonomie.md) | Comprendre la décision et préparer le dossier utile. | Organisme décisionnaire, MDPH selon le cas ; calcul par une caisse → DOM-012, école → DOM-027. |
| Un proche veut agir pour une personne sous protection juridique. | Protection des majeurs | [DOM-026](03-nouveaux-domaines/dom-026-protection-majeurs.md) | Lire la mesure et les pouvoirs au regard de l'acte envisagé. | Pouvoirs au regard de la mesure et de l'acte ; être aidant ne suffit pas à représenter. Soins : DOM-007, succession : DOM-016. |
| Une personne ou un objet a subi un dommage. | Responsabilité civile | [DOM-035](03-nouveaux-domaines/dom-035-responsabilite-dommages.md) | Documenter faits, préjudice et éventuel régime sectoriel. | Auteur allégué/conseil ; dommage médical, construction, circulation ou infraction d'abord orientés au secteur ; garantie → DOM-005. |
| Un contrat de pension, de garde ou de vente d'animal pose problème. | Animaux | [DOM-033](03-nouveaux-domaines/dom-033-animaux.md) | Qualifier parties, espèce, contrat et pièces manquantes. | Cédant/gardien ; élevage professionnel → DOM-014, voisinage → DOM-020, pénal → DOM-002. |

## Démarches, déplacements et droits

| Situation exprimée | Domaine principal | Cadrage ou pilote | Premier résultat utile | Frontière et question complémentaire |
|---|---|---|---|---|
| Un courrier administratif ou un silence me laisse sans réponse. | Administratif | [DOM-010](03-nouveaux-domaines/dom-010-administratif.md) | Identifier demande, décision et régime à examiner. | Administration émettrice ; chercher d'abord un domaine spécialisé : fiscalité, école, caisse, urbanisme, séjour ou emploi public. |
| Je reçois un document de police ou une convocation. | Police et pénal | [DOM-002](03-nouveaux-domaines/dom-002-police-penal.md) | Identifier mesure, statut, date et urgence éventuelle. | Autorité émettrice/conseil pénal ; réparation civile distincte → DOM-035 ou secteur. |
| Je conteste un refus ou une demande concernant mon séjour. | Séjour, nationalité, asile | [DOM-028](03-nouveaux-domaines/dom-028-sejour-nationalite-asile.md) | Identifier procédure, acte et preuve de notification. | Autorité émettrice/conseil ; emploi → travail privé ou DOM-037, famille → DOM-013. Urgences en tâches distinctes. |
| Un service, un logement ou une formation me sont refusés. | Discriminations | [DOM-029](03-nouveaux-domaines/dom-029-discriminations.md) | Distinguer qualification alléguée et faits permettant de l'examiner. | Si un traitement discriminatoire est allégué : auteur du refus/organisme compétent à identifier ; sinon, refus au domaine du bail, du service ou de la formation. La contestation sectorielle reste distincte. |
| Mon vol, mon train ou mon voyage ne s'est pas passé comme prévu. | Transports et voyages | [DOM-008](03-nouveaux-domaines/dom-008-transports.md) | Identifier contrat, incident, transporteur et demandes distinctes. | Transporteur/vendeur du voyage selon contrat ; assurance voyage → DOM-005. |
| Un compte en ligne est suspendu ou mon identité est usurpée. | Numérique et plateformes | [DOM-034](03-nouveaux-domaines/dom-034-numerique-plateformes.md) | Lire notification, rôle de la plateforme et mécanismes disponibles. | Plateforme ; données → données personnelles, droit d'auteur → propriété intellectuelle, achat → DOM-001, paiement → DOM-004, infraction alléguée → DOM-002. |
| Je veux accéder à mes données ou faire corriger une information. | Données personnelles | [EXIST-003](02-plugins-existants/exist-003-donnees-personnelles.md) | Qualifier le droit invoqué et le responsable concerné. | Responsable du traitement/délégué pour accès ou correction ; accès au compte/modération : DOM-034. Pas de profil de cabinet nécessaire. |

## Utilisation dans les stories

La matrice sert à [définir l'orientation accessible](05-usages-quotidiens/usage-001-orientation-accessible.md)
et à [prioriser un petit lot](05-usages-quotidiens/usage-002-priorites-utilite.md).
Elle doit évoluer avec les demandes rencontrées : ajouter une situation,
identifier le domaine principal, puis écrire une story bornée. Elle ne commande
ni l'implémentation simultanée des domaines ni la création automatique d'un
nouveau plugin pour chaque problème.

La [comparaison USAGE-002](05-usages-quotidiens/usage-002-comparaison-priorites.md)
précise cinq petites tâches et leurs résultats évaluables. Elle propose de
conserver la revue du contrat reçu par un candidat comme premier lot, sans
arrêter le choix du pilote ni déclencher son développement. Les autres
situations restent au backlog ; le classement ne mesure ni leur fréquence ni
leur importance pour chaque personne.
