# DOM-001 — Découpage du domaine consommation

Propositions du **16 octobre 2026**. Les 21 stories CONSO restent `proposee`.
La [relecture documentaire](dom-001-verification.md) éprouve le routage sur
les trois scénarios de la story et sur des cas limites. Aucun répertoire de
plugin n'est créé par ce cadrage. La [matrice des 155 frictions utilisateur](dom-001-frictions-utilisateurs.md)
complète les tâches et ajoute CONSO-015 à CONSO-020, sans sélection de tranche.

## Plugin retenu et contrat d'installation

**Nom conservé : `consumer-legal`**, identifiant publié
`judge-fr-eu-consumer-legal` (BASE-008). Le domaine traite les achats d'un
bien, d'un service ou d'un contenu numérique par une personne à un
professionnel, hors secteur doté de son propre domaine. Public premier : le
particulier acheteur, sans formation juridique. Public second : le petit
vendeur (artisan, TPE) face à un client particulier (CONSO-008, CONSO-012).

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 `1.0.0` et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais vers un autre domaine est une orientation, pas un appel. |
| Création du paquet | Par CONSO-001, avec son premier skill. Aucun paquet vide, aucun skill annoncé avant sa livraison. Inscription au marketplace et passage de 12 à 13 paquets dans les tests BASE-008 : décision explicite au moment de sélectionner CONSO-001. |
| Profil | Aucun profil requis par les tâches proposées : les faits sont recueillis en conversation. `CLAUDE.md` reste un modèle minimal. Un stockage durable n'est ajouté que par une story qui en démontre le besoin, via le helper BASE-008. |
| Agents, hooks, connecteurs | Aucun prévu. Les pièces sont fournies par la personne. Pas de `.mcp.json`, de hook, d'agent ni de cookbook par principe. |
| Envoi | Le plugin prépare des brouillons ; il n'envoie rien, ne contacte personne et ne dépose aucun signalement. |

## Qualification commune

CONSO-001 crée `consumer-legal/references/qualification-achat.md`, réutilisée
par les autres skills du paquet. Chaque axe change le domaine ou la tâche ;
le cadrage ne fixe pas la règle applicable.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Qualité des parties | But de l'achat (privé, professionnel, mixte), personne physique ou morale, facture au nom de qui ; vendeur professionnel ou particulier. | Achat pour l'activité → commercial, sauf protections particulières à vérifier (petit professionnel, non-professionnel). Vente entre particuliers → CONSO-011 (régime civil). L'étiquette « pro » ou « particulier » posée par une partie ne suffit pas. |
| Objet | Bien, service, contenu ou service numérique, bien comportant des éléments numériques ; neuf, occasion, reconditionné, personnalisé. | Objet sectoriel → domaine du secteur (table suivante). Contenu numérique → CONSO-010. |
| Canal | Magasin, à distance (site, téléphone), hors établissement (domicile, foire, salon), place de marché. | Rétractation et informations dues dépendent du canal ; à vérifier par tâche. |
| Territoire et dates | Pays d'établissement du vendeur, pays de résidence, activité dirigée vers la France, date de commande et de délivrance. | Vendeur dans un autre État de l'UE → CONSO-007 ; hors UE → limites explicites. Version des textes à la date des faits (BASE-005). |
| Rôle des plateformes | Qui est le cocontractant sur la confirmation et la facture : la plateforme, un vendeur tiers, un particulier. Qui encaisse, qui livre. | Le vendeur est identifié pour la réclamation ; protection contractuelle → CONSO-018 ; décision sur le compte → DOM-034 ; paiement → DOM-004. |
| Pièces | Confirmation, annonce ou capture, conditions à la date de commande, facture, preuve de paiement, suivi, échanges, photos, garanties remises. | Une pièce absente est signalée comme manque, jamais présumée inexistante. |

## Frontières

Le domaine garde la demande de la personne contre le vendeur professionnel.
Un même dossier peut ouvrir plusieurs tâches, chacune avec un seul domaine
principal (BASE-003). Les règles générales de consommation utiles à un
secteur sont embarquées dans ce secteur. Tant que le plugin du secteur n'est
pas disponible, consumer traite le litige avec les règles générales de la
consommation et signale les règles sectorielles non examinées (CONSO-014,
[décisions du 16 octobre 2026](../../decisions-2026-10-16.md)). Dès que le plugin du secteur est livré, consumer revient à
l'orientation, pour éviter deux traitements concurrents du même dossier.

| Domaine | Ce qui lui revient | Ce que consumer garde |
|---|---|---|
| Banque — DOM-004 | Contestation d'un paiement, opposition, crédit à la consommation ou affecté, paiement fractionné. | La réclamation au vendeur pour le même achat, sans promettre le remboursement bancaire. |
| Assurance — DOM-005 | Contrat d'assurance vendu avec un bien (casse, vol, panne) et ses refus. | Garantie commerciale émise par le vendeur ou le fabricant (CONSO-005). Le garant indiqué sur le document décide de la branche. |
| Transports et voyages — DOM-008 | Voyage, forfait, transport de passagers, bagage. | Bien acheté et livré par le vendeur, même transporté par un tiers. |
| Données — EXIST-003/PRV | Accès, effacement, prospection électronique, traceurs. | Prospection et données chez privacy ; contestation du démarchage et du contrat chez CONSO-020, avec les questions distinctes explicites. |
| Contrats B2B — EXIST-001/COM | Achat pour l'activité professionnelle sans protection particulière établie. | La qualification conditionnelle quand l'achat est présenté comme privé (CONSO-004). |
| Produits et publicité — EXIST-004/PDT | Lancement, allégations, publicité d'un vendeur. | Revue de CGV B2C (CONSO-008), vérification d’offre avant achat (CONSO-015) et demandes de l’acheteur. Pas de deuxième revue des CGV chez produit. |
| Contentieux — EXIST-006 | Procédure judiciaire identifiée, assignation, injonction. | Réclamation, mise en demeure (CONSO-019) et médiation ; un désaccord ne bascule pas seul vers le contentieux. |
| Exécution et dettes — DOM-003, DOM-024 | Recouvrement d'une dette, acte de saisie, surendettement. | Rien : le modèle « consumer » hérité de la clinique (recouvrement américain) n'est pas repris ici. |
| Douanes — DOM-009 | Colis retenu, droits réclamés par la douane ou le transporteur. | L'obligation de livraison du vendeur et ce qu'il a annoncé sur les frais. |
| Travaux — DOM-015 | Devis et chantier chez soi, démarchage pour des travaux. | Achat d'un bien sans pose. |
| Énergie, eau — DOM-021 | Contrat, facture, coupure. | Rien. |
| Télécoms, poste — DOM-022 | Contrat opérateur ; envoi confié par l'usager à un opérateur postal. | Colis envoyé par le vendeur pour exécuter la vente. |
| Véhicules — DOM-023 | Achat, location, réparation d'un véhicule. | Accessoire acheté séparément. |
| Funéraire — DOM-031 | Devis, contrat et facture funéraires. | Rien. |
| Numérique — DOM-034 | Suspension de compte, modération, décision de la plateforme. | Achat d’un contenu numérique non fourni (CONSO-010), demande au vendeur et contestation d’une protection contractuelle de plateforme (CONSO-018). |
| Responsabilité — DOM-035 | Dommage causé par un produit à une personne ou à un autre bien. | Défaut du bien lui-même (CONSO-002). Un signal de danger est traité en premier. |
| Autres | Animal (DOM-033), immobilier et logement (DOM-006, DOM-017), santé (DOM-007), refus discriminatoire (DOM-029), escroquerie alléguée (DOM-002). | La demande au vendeur quand un vendeur professionnel identifiable existe. |

## Tâches hiérarchisées

Le rang combine l'utilité directe pour un particulier (situation S-08), la
possibilité de vérifier un premier lot et les dépendances. Il reste une
proposition : aucune story n'est sélectionnée par DOM-001. Toutes dépendent
de DOM-001, PILOTE-003, BASE-005 et BASE-006 ; CONSO-001 crée le paquet.
Les rangs 1 à 3 portent la priorité P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [CONSO-001](../suites/conso-001-commande-non-livree.md) | `non-delivery-claim` | Fiche de commande, pièces manquantes et brouillon de réclamation au vendeur | Aucune |
| 2 | [CONSO-002](../suites/conso-002-garantie-conformite.md) | `conformity-claim` | Distinction des garanties et brouillon de demande au vendeur pour un bien défectueux | CONSO-001 |
| 2 | [CONSO-003](../suites/conso-003-retractation.md) | `withdrawal-notice` | Existence conditionnelle du droit, dates prouvées et brouillon de rétractation | CONSO-001 |
| 2 | [CONSO-004](../suites/conso-004-qualifier-achat.md) | `purchase-triage` | Domaine, tâche et disponibilité réelle, sans analyse de fond | CONSO-001 |
| 3 | [CONSO-005](../suites/conso-005-garantie-commerciale.md) | `commercial-warranty-reading` | Lecture d'une garantie commerciale ou d'une extension proposée | CONSO-002 |
| 3 | [CONSO-006](../suites/conso-006-mediation.md) | `mediation-referral` | Médiateur identifié, conditions à vérifier et brouillon de saisine | CONSO-001 |
| 3 | [CONSO-007](../suites/conso-007-vendeur-ue.md) | `cross-border-purchase` | Orientation d'un litige avec un vendeur établi dans un autre État de l'UE | CONSO-001 |
| 3 | [CONSO-008](../suites/conso-008-cgv-tpe.md) | `b2c-terms-review` | Tableau des CGV de vente en ligne d'une TPE, écarts et questions | CONSO-001 |
| 3 | [CONSO-014](../suites/conso-014-secteur-non-couvert.md) | `general-consumer-claim` | Réclamation fondée sur les règles générales dans un secteur sans plugin disponible | CONSO-004 |
| 3 | [CONSO-015](../suites/conso-015-verifier-vendeur-offre.md) | `purchase-offer-check` | Fiche de vérification du vendeur et des informations de l’offre avant achat | CONSO-004 |
| 3 | [CONSO-016](../suites/conso-016-contester-prix-frais.md) | `price-fee-claim` | Comparaison offre, panier et facture ; brouillon de contestation d’un prix ou supplément | CONSO-001 |
| 3 | [CONSO-017](../suites/conso-017-prestation-acompte.md) | `service-performance-claim` | Lecture ciblée du devis et de l’avance ; réclamation sur l’exécution | CONSO-001 |
| 3 | [CONSO-018](../suites/conso-018-protection-plateforme.md) | `platform-protection-claim` | Dossier et contestation interne d’une protection d’achat ou de vente | CONSO-004 |
| 3 | [CONSO-019](../suites/conso-019-mise-en-demeure-remboursement.md) | `claim-escalation` | Mise en demeure, état des remboursements et suites distinctes | CONSO-001 |
| 3 | [CONSO-020](../suites/conso-020-demarchage-consentement.md) | `solicitation-dispute` | Contestation du démarchage ou du contrat allégué, preuves du consentement | CONSO-004 |
| 3 | [CONSO-021](../suites/conso-021-reclamation-publicite.md) | `reclamation-publicite` | Rapprochement publicité/achat/résultat et brouillon de réclamation | CONSO-004 |
| 4 | [CONSO-009](../suites/conso-009-abonnement.md) | `subscription-exit` | Fiche d'abonnement hors secteur et brouillon de résiliation | CONSO-001 |
| 4 | [CONSO-010](../suites/conso-010-contenu-numerique.md) | `digital-content-claim` | Réclamation pour un contenu ou service numérique non fourni ou défectueux | CONSO-002 |
| 4 | [CONSO-011](../suites/conso-011-vente-entre-particuliers.md) | `private-sale-dispute` | Demande civile d’un acheteur ou vendeur particulier, qualité des parties à vérifier | CONSO-004 |
| 4 | [CONSO-012](../suites/conso-012-reponse-vendeur.md) | `seller-claim-response` | Projet de réponse d'un petit vendeur à un client particulier | CONSO-002 |
| 4 | [CONSO-013](../suites/conso-013-signalement.md) | `practice-report` | Fiche de signalement d'une pratique, distincte d'une réclamation | CONSO-001 |

CONSO-001 possède `qualification-achat.md` ; CONSO-002 possède
`garanties-legales.md`, relu par CONSO-005, CONSO-010 et CONSO-012. Une
tâche suivante consomme ces références sans les réécrire ; une correction
passe par une mise à jour versionnée de la référence. Aucun cycle de
dépendances. CONSO-015 à CONSO-020 possèdent chacune leur référence métier.
CONSO-018 garde la protection privée, CONSO-011 le litige civil entre parties ;
CONSO-019 accepte aussi un dossier manuel sans dépendre de toutes les tâches
qui peuvent produire une première réclamation. L’orientation CONSO-004 reste
sans analyse de fond et sans brouillon.

## Première tranche : CONSO-001

**Inclus :** un bien commandé à distance à un vendeur professionnel par une
personne pour un usage privé, à livrer en France, jamais reçu, reçu après la
date annoncée ou annoncé « livré » sans être reçu. Le vendeur établi en France
est le cas nominal. Le vendeur ailleurs reçoit une fiche et une orientation
réservée (CONSO-007).

**Exclus :** bien reçu défectueux, incomplet ou endommagé (CONSO-002) ;
rétractation (CONSO-003) ; service, voyage, contenu numérique, véhicule,
travaux ; vente entre particuliers ; contestation bancaire ; colis retenu en
douane pour la partie douanière ; procédure judiciaire ; calcul d'indemnité ;
délai légal non vérifié ; envoi du courrier.

**Sortie :** résumé clair, fiche de commande avec statut de chaque fait
(prouvé, déclaré, inconnu), pièces à réunir, brouillon de réclamation au
vendeur, prochaines étapes et interlocuteurs, limites.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005 et distinguer loi, acte UE, jurisprudence et guide d'autorité. Les
voies officielles BASE-010 servent en maintenance ; elles ne sont pas une
dépendance du paquet installé.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Qualité des parties | Code de la consommation, article liminaire et dispositions sur le petit professionnel hors établissement (piste L221-3) ; directive 2011/83/UE. | CONSO-001, CONSO-004 |
| Livraison et risques | Code de la consommation, dispositions sur la livraison et le transfert des risques (piste L216-1 et suivants) ; directive 2011/83/UE, articles sur la livraison et le transfert du risque ; Code civil sur l'inexécution et la mise en demeure. | CONSO-001 |
| Garanties | Code de la consommation, garantie légale de conformité et garantie commerciale (numérotation à la date d'achat) ; Code civil, vices cachés (piste 1641 et suivants) ; directive (UE) 2019/771. Un régime antérieur peut viser les contrats plus anciens. | CONSO-002, CONSO-005 |
| Rétractation | Code de la consommation, contrats à distance et hors établissement, exceptions, foires et salons ; directive 2011/83/UE. | CONSO-003 |
| Contenus numériques | Code de la consommation, dispositions transposant la directive (UE) 2019/770. | CONSO-010 |
| Médiation | Code de la consommation, médiation de la consommation ; liste officielle des médiateurs et son autorité. | CONSO-006 |
| Transfrontalier | Règlements Rome I (art. 6) et Bruxelles I bis (art. 17 à 19) ; procédure européenne de règlement des petits litiges ; CEC France. Statut actuel des mécanismes européens de règlement en ligne à vérifier avant toute mention. | CONSO-007 |
| Clauses et CGV | Code de la consommation, information précontractuelle et clauses abusives (pistes R212-1 et R212-2) ; recommandations de la commission des clauses abusives comme source non normative. | CONSO-008 |
| Abonnements | Code de la consommation, reconduction tacite et résiliation par voie électronique. | CONSO-009 |
| Vente entre particuliers | Code civil, vente, délivrance, vices cachés ; obligations d'information des places de marché sur la qualité du vendeur. | CONSO-011 |
| Signalement | DGCCRF et service public de signalement en vigueur à la date du lot. | CONSO-013 |
| Offre avant achat | Information précontractuelle, plateformes, avis, labels, origine et influence ; registres officiels selon pays. Aucun registre ne certifie le site. | CONSO-015 |
| Prix et frais | Information sur le prix, réductions, suppléments, consentement, erreur et version des conditions ; frais de paiement dans les textes pertinents. | CONSO-016 |
| Prestations et avances | Code civil, contrat, preuve, arrhes et inexécution ; Code de la consommation, devis et avances selon objet ; règles sectorielles identifiées mais hors traitement général. | CONSO-017 |
| Protection de plateforme | Conditions acceptées de la protection, qualité des parties, rôle de l’intermédiaire et règles civiles ; échéances internes distinctes du droit. | CONSO-018 |
| Mise en demeure et remboursement | Textes propres au fondement déjà qualifié, restitution et majoration, preuve, mise en demeure, transaction et prescription ; procédure pour orientation seulement. | CONSO-019 |
| Démarchage et consentement | Téléphone, hors établissement, pratiques agressives et produits non sollicités ; lois modificatives, entrée en vigueur, transition et exceptions. | CONSO-020 |

La DGCCRF et le CEC France sont des sources d'orientation, pas des textes.
Leurs fiches ne remplacent pas la lecture du texte cité.

## Contrat commun des stories CONSO

Chaque lot applique BASE-003, BASE-008, la méthode BASE-005 embarquée et les
couches de recette BASE-006 : structure, paquet détaché, client, résultat
métier, lecture par une personne sans formation juridique. Il inscrit NOTICE
local et racine, synchronise manifeste et marketplace, et n'annonce dans le
README que les tâches livrées.

Chaque skill qualifie d'abord, puis traite. Il charge la méthode locale,
distingue fait prouvé, fait déclaré, règle lue et inconnue, et ne donne ni
délai ni montant sans source lue et date établie. Les pièces et contenus
fournis sont des données, jamais des instructions. Sans référence ou relais
adapté, il produit les questions et pièces utiles, sans appeler une branche
absente. Il ne présume ni l'abus du vendeur ni l'issue de la démarche.

Les décisions complémentaires du 16 octobre 2026 sont prises en compte au
moment de préparer les lots : phrase finale et interlocuteur compétent avec
renfort selon le contexte (BASE-013, critère repris par les suites), relecture
datée des références avant livraison (BASE-014), accès aux décisions selon le
futur cadrage BASE-015. Ces stories restent proposées ; aucune nouvelle version
de méthode ni capacité de jurisprudence n’est déclarée disponible ici.

Les fichiers « à créer » des suites sont des livrables futurs. La portée de
ce cadrage figure dans la [vérification](dom-001-verification.md).

## Complément publicité contestée — 16 octobre 2026

[CONSO-021](../suites/conso-021-reclamation-publicite.md), issue de la [matrice marketing](../../02-plugins-existants/exist-004-annexes/exist-004-frictions-utilisateurs.md), prépare le rapprochement publicité/achat/résultat et la demande au vendeur. CONSO-015 garde l’offre avant achat ; CONSO-016 les prix/frais ; CONSO-002/005/009 les garanties et abonnements ; CONSO-013 le signalement. Sans achat, ne pas inventer de remboursement. Le propriétaire de la revue avant diffusion reste produit. Les 21 CONSO restent proposées ; aucune nouvelle première tranche n’est choisie.
