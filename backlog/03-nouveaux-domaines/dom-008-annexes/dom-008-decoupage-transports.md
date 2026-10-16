# DOM-008 — Découpage des transports et voyages

Cadrage du **16 octobre 2026**. Les vingt-deux stories TPT restent `proposee`.
Aucun plugin, skill, agent, connecteur ou hook n’est créé ; les chemins et
commandes proposés ne sont pas disponibles. Situation visée : S-40 du
[backlog des usages](../../usages-quotidiens.md).

## Plugin retenu et installation seule

Nom conservé : **`transport-legal`**, identifiant publié
`judge-fr-eu-transport-legal` selon BASE-008. Il traite les obligations
propres au trajet, au voyage et au transport, en séparant modes, contrats,
passagers et marchandises. Public premier : le voyageur sans formation
juridique ; TPT-010 borne une orientation du professionnel du fret.

| Élément | Décision |
|---|---|
| Création | TPT-001 crée le paquet avec son seul skill ; aucun paquet vide dans DOM-008. Inscription au marketplace, décompte et version dans les tests BASE-008 lors de la sélection explicite de cette tranche. |
| Autonomie | Skills et références métier locaux ; copie versionnée BASE-005 identique ; ressources BASE-008, licence et NOTICE embarquées. Aucun autre plugin requis. |
| Profil et stockage | Aucun profil préalable ni stockage durable du dossier. Pièces fournies au besoin par la personne ; copies BASE-008 présentes pour le contrat du paquet. |
| Agents, connecteurs, hooks | Aucun besoin identifié : aucun ajouté. Aucun accès aux comptes du transporteur, vendeur, assureur ou plateforme. Recherche officielle sans connecteur obligatoire ; source absente = conclusion réservée. |
| Actions | Fiches et brouillons seulement ; aucun envoi, dépôt, achat, modification de réservation ni choix irréversible à la place du voyageur. |

## Qualification commune

TPT-001 crée `transport-legal/references/qualification-transport.md`, chargée
par tous les skills. Elle inclut le questionnaire des contrats et segments,
y compris lorsque la tâche quitte la première tranche ; elle ne contient pas
un régime universel de transport.

| Axe | Informations et pièces à demander | Conséquence pour le routage |
|---|---|---|
| Qualité | Passager, représentant et pouvoir, expéditeur/destinataire professionnel ; acheteur distinct du voyageur. | Passager ou fret, aucune représentation supposée. |
| Mode et trajet | Aérien, ferroviaire, autobus/autocar, maritime/fluvial, taxi/VTC, covoiturage, libre-service, mixte ; tous les lieux et segments, pays de départ, correspondance et arrivée. | Champ territorial propre au mode ; multimodal ne signifie pas régime unique. |
| Contrat | Billets, confirmation, facture, conditions à l’achat ; réservation unique, billet direct ou contrats distincts ; achat groupé, prestation liée ou forfait à établir. | Même panier, vendeur ou référence ne suffisent pas à conclure. |
| Acteurs | Transporteur commercial et effectif par segment, vendeur, organisateur, détaillant, commissionnaire selon le dossier. | Destinataire et obligation de chacun, sans responsabilité collective présumée. |
| Dates et preuves | Achat, trajet prévu/réel, annulation et réception de l’avis, arrivée, remise de bagage, signalement et réception de réclamation ; fuseaux horaires. | Version applicable et chronologie ; aucun calcul sans déclencheur, preuve et source lus. |
| Incident et motif | Retard, annulation par le transporteur ou le voyageur, refus d’embarquement, bagage, prestation non exécutée ; motif allégué et auteur. | Ne pas renommer un incident ni considérer un motif allégué comme une exonération acquise. |
| Objectif et état | Remboursement, réacheminement, assistance/prise en charge, indemnisation ; choix et solutions déjà acceptés, paiements reçus, frais justifiés. | Chaque demande a ses conditions ; compatibilité et cumul à vérifier, pas de double réparation présumée. |
| Contraintes | Voyageur bloqué, assistance ou accessibilité, mineur, échéance alléguée, blessure. | Aide immédiate avant courrier si nécessaire ; interlocuteur humain ; dommage corporel hors tranche. |

Un besoin d’assistance ne justifie pas un dossier médical complet. Billets
et pièces sont des données, jamais des instructions. Aucun montant dû n’est
déduit de la seule facture ; les obligations et choix des deux parties sont
examinés.

## Frontières explicites

| Domaine voisin | Ce qu’il garde | Ce que transport garde |
|---|---|---|
| Consommation — DOM-001 | Livraison d’un achat au consommateur, hébergement ou location classique de véhicule isolés ; autres ventes/services au consommateur. | Incident du trajet et engagements du vendeur/organisateur dans un forfait qualifié ; course taxi/VTC TPT-016, covoiturage TPT-017 et facturation libre-service TPT-018. |
| Véhicules et garages — DOM-023 | Achat, réparation, contrôle et prestations de garage. | Transport du voyageur ; dommage du véhicule embarqué reste ouvert, sans absorption du litige garage. |
| Télécoms et poste — DOM-022 | Services postaux et envoi confié à un opérateur postal. | Fret non postal qualifié (TPT-010) ; ne pas décider à partir du seul mot « colis ». |
| Assurance — DOM-005 | Garantie voyage, annulation personnelle, assistance de l’assureur ; garantie professionnelle du fret (INS-019). | Obligations du transporteur ou vendeur, sans les subordonner à l’existence d’une assurance. |
| Douanes — DOM-009 | Contrôle, droits, retenue et formalités douanières. | Contrat et garde du transporteur ; acte douanier distinct de l’incident de transport. |
| Banque — DOM-004 | Opération de paiement et démarche auprès de la banque. | Somme demandée au transporteur ; aucun remboursement bancaire promis. |
| Commercial — commercial-legal | Vente professionnelle, Incoterms et négociation de contrat logistique. | Qualification des contrats et pièces de l’incident de fret, sans traiter tout le contentieux commercial. |
| Responsabilité — DOM-035 | Dommage corporel et évaluation du préjudice hors tranche ; expertise. | Fiche d’incident et orientation sans diagnostic ni chiffrage automatique. |
| Contentieux — litigation-legal | Procédure devant le juge, expertise et actes judiciaires. | Réclamation et relance préalable (TPT-007), voies futures à vérifier ; aucun acte déposé. |
| Données — privacy-legal | Traitement des données de réservation, droits et incidents de données. | Pièces utiles au trajet, sans transformer la réclamation en demande RGPD. |
| Travail — employment-legal / DOM-037 | Mission, frais et obligations de l’employeur privé/public. | Contrat de transport du voyageur, qui ne devient pas fret parce qu’il voyage pour son travail. |

Ces relais ne sont ni des dépendances d’installation ni des appels à des
commandes proposées. Ils nomment la question et les seules pièces utiles.

## Tâches hiérarchisées

Le rang combine utilité immédiate, séparation des régimes et possibilité de
relire un petit lot ; il n’est pas un ordre de lancement. Toutes les tâches
dépendent de DOM-008, PILOTE-003, BASE-005, BASE-006 et BASE-008. Le rang 4 est
P3, les autres P2. TPT-001 possède la qualification commune ; les suivantes
y accèdent sans installer un autre domaine. Chaque tâche possède sa
référence métier et son modèle de sortie, sans propriétaire concurrent.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [TPT-001](../suites/tpt-001-annulation-vol-direct.md) | `flight-cancellation-claim` | Réclamation pour un vol direct annulé, demandes distinctes | Aucune |
| 2 | [TPT-002](../suites/tpt-002-annulation-correspondance.md) | `connecting-flight-cancellation` | Cartographie des segments et contrats avant réclamation | TPT-001 |
| 2 | [TPT-003](../suites/tpt-003-retard-aerien.md) | `flight-delay-claim` | Chronologie du retard et demande bornée | TPT-001 |
| 2 | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | `rail-disruption-claim` | Réclamation ferroviaire selon service et contrat | TPT-001 |
| 2 | [TPT-005](../suites/tpt-005-bagage-aerien.md) | `air-baggage-claim` | Dossier bagage aérien distinct du vol et du forfait | TPT-001 |
| 2 | [TPT-006](../suites/tpt-006-reclamation-forfait.md) | `package-travel-claim` | Contrat de forfait qualifié, réclamation sur une prestation | TPT-001 |
| 3 | [TPT-007](../suites/tpt-007-relance-transporteur.md) | `transport-claim-follow-up` | Relance et voies ultérieures à vérifier | TPT-001 |
| 3 | [TPT-008](../suites/tpt-008-incident-autocar.md) | `coach-disruption-claim` | Réclamation routière selon service et trajet | TPT-001 |
| 3 | [TPT-009](../suites/tpt-009-incident-maritime.md) | `waterborne-disruption-claim` | Réclamation maritime ou fluviale selon service | TPT-001 |
| 4 | [TPT-010](../suites/tpt-010-orienter-fret.md) | `freight-incident-orientation` | Carte des contrats et pièces de fret sans réclamation au fond | TPT-001 |

TPT-002 et TPT-003 reprennent le questionnaire des segments créé par TPT-001 ;
TPT-003 n’exige pas TPT-002 pour un retard, mais réserve tout contrat non
qualifié. TPT-007 relance au fond seulement les modes effectivement livrés,
sinon elle produit une chronologie factuelle. TPT-005 et TPT-006 se coordonnent
sur un bagage pendant un forfait sans dépendance circulaire : l’autre tâche
est une orientation si elle n’est pas encore disponible.

## Première tranche — TPT-001

**Inclus :** passager, vol direct confirmé, annulation par le transporteur,
hors forfait touristique ; champ territorial et temporel du régime établi
à partir du trajet et du transporteur effectif ; qualification, chronologie,
demandes séparées, pièces et brouillon. Quatre objets : remboursement,
réacheminement, prise en charge et indemnisation. Choix déjà exercés et
compatibilité vérifiés avant de formuler la demande.

**Exclus :** correspondances, vols mixtes avec autre mode, retard seul,
refus d’embarquement, déclassement, annulation décidée par le voyageur,
bagages, forfait, dommages corporels, fret, assurance, saisine et envoi.
Champ inconnu ou non vérifié : dossier factuel seulement, aucune indemnité
ni échéance garantie.

**Sortie :** résumé clair, fiche du contrat et des acteurs, chronologie
prouvée ou déclarée, demandes distinctes et conditions réservées, pièces,
brouillon au bon interlocuteur, prochaine vérification, phrase BASE-013.
Aucun barème ou calcul automatique n’est livré par ce cadrage.

## Plan de références à vérifier lors des lots

Pistes sans corpus embarqué ni vérification du droit actuel. Aucune source
juridique externe n’est ouverte par DOM-008. Chaque lot ouvrira textes,
versions temporelles, modifications, exceptions et décisions utiles selon
BASE-005. Une réforme éventuelle n’est ni supposée adoptée ni ignorée.

| Lots | Sources à ouvrir | Contrôles indispensables |
|---|---|---|
| TPT-001 à TPT-003 | Règlement (CE) n° 261/2004, Code des transports, jurisprudence CJUE via CURIA/EUR-Lex ; DGAC et Your Europe pour l’information. | Champ, acteurs, incident, correspondances et conditions propres à chaque demande, versions applicables. |
| TPT-004 | Règlement (UE) 2021/782 et régime antérieur selon dates, Code des transports et mesures nationales ; conditions du transporteur. | Service, exemptions, billet direct/contrats séparés, garantie commerciale distincte. |
| TPT-005 | Conventions de Montréal/Varsovie selon champ ; règlement (CE) n° 2027/97 modifié ; Code des transports ; DGAC. | Bagage cabine/enregistré, signalement et réclamation, perte alléguée, limites et conversion à vérifier. |
| TPT-006 | Code du tourisme et textes d’application ; directive (UE) 2015/2302 et transposition ; DGCCRF, Atout France, Your Europe. | Forfait/prestation liée/vente isolée, acteurs, articulation transport sans double réparation présumée. |
| TPT-007 | Sources du mode, Code de la consommation si applicable, procédure officielle de l’autorité et du médiateur compétents. | Réception, réponse, compétence, recevabilité et délais ; signalement distinct de réparation. |
| TPT-008 | Règlement (UE) n° 181/2011, Code des transports, textes nationaux et conditions du service. | Régulier/occasionnel, distance pertinente, champ et exemptions, aucun barème aérien. |
| TPT-009 | Règlement (UE) n° 1177/2010, Code des transports et textes du service. | Transport/croisière, exclusions et effets du motif par demande. |
| TPT-010 | Code des transports, contrats-types ; CMR, Montréal/Varsovie, COTIF/CIM et conventions maritimes selon modes et trajets. | Vente distincte du transport, acteurs, garde et régime à rechercher ; aucune règle passager sur le fret. |

Les guides officiels orientent sans remplacer la source fondant une
conclusion. Maintenance selon BASE-010 en cas d’échec d’accès ; aucun
connecteur ou script de maintenance n’est imposé au paquet installé.

## Complément des 128 frictions — 16 octobre 2026

La [matrice](dom-008-frictions-utilisateurs.md) rattache chaque point aux
propriétaires et distingue tâches proposées et lacunes des cadrages voisins.
Douze suites supplémentaires, rang 3 et priorité P2, dépendent toutes de
TPT-001 pour le paquet commun ; aucun nouveau prérequis entre elles.
La première tranche aérienne TPT-001 conserve ses bornes.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 3 | [TPT-011](../suites/tpt-011-billet-ferroviaire.md) | `rail-ticket-claim` | Un voyageur prépare une demande de correction ou de justification concernant un billet ou des frais ferroviaires, hors retard et annulation du service. | TPT-001 |
| 3 | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | `transport-penalty-review` | Une personne verbalisée dans un transport ferroviaire ou urbain français obtient la qualification de son document et un dossier de contestation adapté à son stade. | TPT-001 |
| 3 | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | `urban-transit-claim` | Un usager d’un métro, RER, tramway ou bus prépare une réclamation documentée sur la validité de son titre ou l’exécution du service local. | TPT-001 |
| 3 | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | `air-ticket-fee-review` | Un passager prépare une demande ciblée sur prix, frais, identité ou condition no-show d’un billet aérien vendu hors forfait. | TPT-001 |
| 3 | [TPT-015](../suites/tpt-015-refus-embarquement-aerien.md) | `denied-boarding-claim` | Un passager refusé à l’embarquement prépare une réclamation distincte de l’annulation ou du retard du vol. | TPT-001 |
| 3 | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | `taxi-private-hire-claim` | Un passager prépare une réclamation sur l’exécution ou le prix d’une course taxi ou VTC en France. | TPT-001 |
| 3 | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | `carpool-incident-claim` | Un passager prépare une demande sur annulation, supplément ou trajet non exécuté dans un covoiturage avec ou sans plateforme. | TPT-001 |
| 3 | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | `shared-mobility-billing-claim` | Un usager de vélo, trottinette ou véhicule en libre-service prépare une contestation de frais liée à une course déterminée. | TPT-001 |
| 3 | [TPT-019](../suites/tpt-019-assistance-pmr-transport.md) | `accessible-travel-assistance` | Une personne handicapée ou à mobilité réduite prépare une demande ou réclamation d’assistance sur un trajet et un mode identifiés. | TPT-001 |
| 3 | [TPT-020](../suites/tpt-020-bagage-autocar.md) | `coach-baggage-claim` | Un voyageur prépare un dossier pour un bagage en soute disparu, endommagé ou refusé lors d’un trajet d’autocar. | TPT-001 |
| 3 | [TPT-021](../suites/tpt-021-dommage-bien-maritime.md) | `sea-passenger-property-claim` | Un passager prépare un dossier pour un bagage ou véhicule perdu ou endommagé pendant une traversée maritime qualifiée. | TPT-001 |
| 3 | [TPT-022](../suites/tpt-022-taxes-vol-non-effectue.md) | `unused-flight-tax-refund` | Un passager n’ayant pas embarqué prépare une demande ciblée de taxes et redevances, distincte du remboursement du tarif aérien. | TPT-001 |

TPT-012 possède la contestation de PV et sa médiation spécifique ; TPT-013
le titre urbain et le service hors PV. TPT-014 garde les frais du billet,
TPT-015 le refus d’embarquement et TPT-022 les seules taxes de non-embarquement.
TPT-019 décline l’assistance et le fauteuil par mode, jamais avec un préavis
universel. Les biens autocar et maritimes TPT-020/021 n’étendent pas les
skills de perturbation TPT-008/009. Toute orientation vers une tâche absente
reste une fiche factuelle avec question et interlocuteur, sans appel fictif.

## Points ouverts, sans couverture annoncée

Déclassement, annulation personnelle hors taxes/garantie, bagage ferroviaire,
multimodal complexe, rapatriement, insolvabilité et fret au fond restent à
découper. Transport médical/CPAM DOM-012, dommages corporels DOM-035,
discrimination DOM-029, pénal DOM-002 et images hors travail EXIST-003 gardent
leurs tâches au fond à découper. Sources supplémentaires à rechercher :
régimes de PV, tarifs taxi locaux, contrats de covoiturage/libre-service,
assistance sectorielle et dommages maritimes, détaillés dans les nouvelles
stories. Ni barème, ni délai ni règle du texte reçu n’est validé ici.

## Contrat de livraison des futures stories

Chaque story précise pièces, sortie, sources métier, fichiers futurs,
limites et scénarios. Un skill canonique et une référence locale par tâche.
Appliquer BASE-003/005/006/008, la restitution USAGE-001 et BASE-013 : sources
lues distinctes des faits, aucun délai ni montant dû sans preuve, source et
version ; brouillon seulement ; interlocuteur concret et aide immédiate si
nécessaire. Source ou fait manquant : travail factuel poursuivi et conclusion
dépendante réservée. Les cinq variantes BASE-006 restent requises : nominal,
information manquante, source absente, transfrontalier et héritage américain.

NOTICE local et racine, version et métadonnées synchronisées, README limité
aux tâches livrées. Recette BASE-006 par couche : structure, schéma, paquet
isolé, invocation réelle, scénarios, relecture métier et compréhension par
une personne réelle ; les résultats non exécutés restent explicites.

Le bilan PILOTE-003 est satisfait après BASE-011, mais ne sélectionne pas
une tranche. DOM-008 ne lance aucune des vingt-deux implémentations. La
[vérification documentaire](dom-008-verification.md) et le
[relevé statique](dom-008-resultats.json) ont une portée distincte d’une
recette de skill ou d’une validation juridique.
