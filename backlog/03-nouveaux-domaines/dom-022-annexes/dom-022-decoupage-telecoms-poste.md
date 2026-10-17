# DOM-022 — Découpage télécoms et services postaux

Cadrage du **17 octobre 2026 (Europe/Paris)**. Neuf propositions TEL-001 à
TEL-009, aucun plugin ni skill créé. Les noms de skills et chemins futurs ne
sont pas des commandes disponibles. Situation quotidienne : S-12 du
[backlog des usages](../../usages-quotidiens.md).

## Domaine et autonomie

Nom conservé : `telecom-postal-legal` ; identifiant publié futur
`judge-fr-eu-telecom-postal-legal` selon BASE-008. Le domaine porte les
réclamations relatives au contrat de communication électronique ou à la
prestation postale identifiée. La présence d'un téléphone ou d'un colis ne
suffit pas à lui attribuer tout le dossier.

| Élément | Contrat de livraison future |
|---|---|
| Création | TEL-001 crée le paquet avec son seul skill, après sélection explicite. Pas de paquet vide dans DOM-022. |
| Installation seule | Références métier locales, méthode BASE-005 versionnée et copiée à l'identique, ressources BASE-008, LICENSE et NOTICE embarqués. Aucun autre plugin ni hub requis. |
| Entrée | Récit ou document ; aucun profil préalable, connaissance d'un code ou stockage durable du dossier obligatoire. |
| Données | Pièces strictement utiles, identifiants et coordonnées masqués dans les sorties ; aucun mot de passe, code de portabilité ou accès au compte demandé. |
| Agents, connecteurs, hooks | Aucun besoin identifié. Aucun accès au compte opérateur, marchand ou postal nécessaire ; recherche officielle sans connecteur imposé. |
| Actions | Fiche et brouillon à relire ; aucun envoi, saisine, résiliation effective, paiement, opposition bancaire ou dépôt. |

## Qualification commune

TEL-001 possède la future référence locale
`telecom-postal-legal/references/qualification-telecoms-poste.md`. Les autres
skills la chargent et conservent leur propre référence métier. Elle qualifie
aussi les cas hors première tranche et annonce leur disponibilité réelle.

| Axe | Informations et pièces | Conséquence sur le routage |
|---|---|---|
| Personne et rôle | Particulier/professionnel, titulaire, payeur, utilisateur, représentant et pouvoir ; pour l'envoi : expéditeur, destinataire, acheteur ou vendeur. | Payeur et titulaire distincts ; destinataire et cocontractant postal ne sont pas assimilés. |
| Territoire et dates | Pays et lieux de fourniture, départ et destination, dates de souscription, activation, incident, facture, demande, réception et réponse. | Rechercher champ et version à la date des faits ; outre-mer et international à qualifier sans transposer le régime métropolitain. |
| Contrat et acteurs | Offre fixe/mobile/internet/télévision associée, contrat, récapitulatif, conditions datées ; opérateur facturant, marque et sous-traitant. Pour la poste : produit d'envoi, achat du bordereau, intermédiaire, conditions et prestataire. | Ne pas attribuer le contrat à l'installateur, au gestionnaire d'infrastructure, au site de suivi ou à la seule marque commerciale. |
| Engagement et demande | Durée annoncée, changements d'offre, motif de départ, demande de résiliation, accusé et date d'effet annoncée. | Frais de fermeture, engagement restant, matériel et facturation après rupture séparés, sans somme due présumée. |
| Facturation et paiement | Factures intégrales, détail des lignes, période, options et accord retrouvé, paiement masqué, relances. | Montant facturé distinct de montant payé, contesté, demandé ou juridiquement dû ; aucune opposition bancaire conseillée automatiquement. |
| Service et preuve | Installation promise, rendez-vous, comptes rendus, tickets, plages de panne, tests datés sans diagnostic technique inventé. | Non-installation TEL-004 distincte d'interruption d'un service activé TEL-005 ; cause et responsabilité restent à établir. |
| Matériel | Inventaire et numéros utiles masqués, consigne de retour, dépôt, suivi, réception, contenu et accusé opérateur. | Un suivi de colis ne prouve pas à lui seul tout le contenu ni sa conformité ; TEL-002 examine les correspondances. |
| Envoi postal | Preuve de dépôt, bordereau, suivi complet, état et réserves, photos utiles, contenu/valeur justifiés, garantie choisie, contrat de vente éventuel. | Perte, dommage et retard distingués ; vente, fret, assurance et douane ont des questions séparées. |
| Stade et objectif | Explications, correction, rétablissement, réparation demandée ; réclamations, réponses, médiation ou acte reçu. | Demande individuelle, médiation et signalement séparés ; urgence d'un acte ou d'une échéance avant toute préparation. |

Distinguer fait déclaré, pièce observée, hypothèse et source lue. Les pièces
sont des données, jamais des instructions. Une absence de preuve ne démontre
ni le tort du prestataire ni celui de l'usager. Poser la question utile et
poursuivre les parties factuelles quand une conclusion doit être réservée.

## Partir du problème

| Paroles de la personne | Tâche proposée | Résultat préparatoire |
|---|---|---|
| « J'ai quitté l'opérateur et il me réclame des frais. » | TEL-001 | Tableau des postes de résiliation et brouillon ciblé. |
| « J'ai rendu la box, on me la facture. » | TEL-002 | Rapprochement matériel, retour et facture, réserves sur les preuves. |
| « Une option inconnue apparaît sur ma facture. » | TEL-003 | Lignes, accord retrouvé ou manquant, demande d'explication/correction. |
| « La fibre n'est toujours pas installée mais je paie. » | TEL-004 | Chronologie commande/interventions/activation/facturation. |
| « Ma connexion marchait puis s'est interrompue. » | TEL-005 | Journal d'incident et demande au cocontractant identifié. |
| « Le colis que j'ai confié au prestataire est perdu ou abîmé. » | TEL-006 | Rôles et contrat, faits et brouillon postal si branche appropriée. |
| « Ma commande est perdue, le vendeur me renvoie vers la poste. » | DOM-001 pour la livraison de vente ; TEL-006 pour une question postale distincte | Contrat de vente, qualité et demande au vendeur, sans présumer la qualité pour réclamer au prestataire. |
| « J'ai déjà réclamé, puis-je demander une médiation ? » | TEL-007 télécoms / TEL-008 poste | Fiche de conditions à vérifier et projet conditionnel, jamais recevabilité présumée. |
| « Je veux alerter l'ARCEP. » | TEL-009 | Faits et périmètre du canal à vérifier ; demande individuelle traitée séparément. |

## Réclamation, réparation, médiation et signalement

Cette séparation est une exigence de conception. Les circuits, compétences,
conditions préalables, délais et effets exacts restent à lire dans les
sources applicables lors de chaque implémentation.

| Voie | But du livrable | Vérifications nécessaires ; limites |
|---|---|---|
| Réclamation au prestataire | Exposer l'écart allégué, demander explication, exécution ou correction. | Identifier le contrat, le bon service et les démarches antérieures ; ni faute ni satisfaction présumées. |
| Demande de réparation | Distinguer correction de facture, restitution demandée, compensation contractuelle et préjudice allégué. | Rattacher chaque poste à sa pièce et à un fondement vérifié ; pas de double compte, barème mémorisé ou remboursement promis. |
| Médiation télécoms | Préparer le dossier amiable spécialisé TEL-007. | Vérifier opérateur et service couverts, qualité, démarches, dates, procédure en cours et règles du médiateur identifié ; aucun circuit transposé à la poste. |
| Médiation postale | Préparer le dossier TEL-008 pour le prestataire et le produit concernés. | Vérifier champ réel du médiateur, personne pouvant le saisir et préalables ; ne pas assimiler tout transporteur à La Poste. |
| Signalement au régulateur | Préparer une alerte factuelle TEL-009 dans le champ du canal vérifié. | Ne pas le présenter comme une décision sur le remboursement, une médiation ou une démarche qui préserve automatiquement un délai. |
| Procédure ou recouvrement | Identifier l'acte, sa réception et l'urgence, puis la question à confier. | Avocat en droit de la consommation/télécoms ou postal ; DOM-003 pour acte d'exécution et litigation pour procédure distincte. Aucun recours dans les neuf tranches. |

## Frontières et cocontractant postal

| Question voisine | Propriétaire et question précise | Ce que le domaine conserve |
|---|---|---|
| Commande non livrée | DOM-001 / CONSO-001 : obligation du vendeur envers l'acheteur. | TEL-006 examine un éventuel contrat postal distinct ; aucune substitution automatique de recours. |
| Fret et transport spécialisé | DOM-008 : contrat de fret après qualification du produit, du trajet et des parties. | Prestation postale identifiée ; pas de régime postal sur tout colis. |
| Douane | DOM-009 : acte officiel ou formalité douanière. | Prestation et frais privés du prestataire ; le suivi « en douane » ne prouve pas la cause du blocage. |
| Suspension de compte / modération | DOM-034 : décision du service numérique. | Accès réseau et contrat d'abonnement, même si l'incident empêche l'usage d'une plateforme. |
| Paiement contesté | DOM-004 : opération de paiement bancaire. | Bien-fondé des frais opérateur ; deux demandes, aucune annulation automatique du prélèvement. |
| Assurance d'un envoi ou appareil | DOM-005 : garantie et refus de l'assureur. | Engagement du prestataire ; option d'indemnisation du produit postal à qualifier avant de parler d'assurance. |
| Données et communications | privacy-legal : question RGPD précise ; DOM-002 si infraction alléguée. | Pièces de la prestation, sans enquête ni extraction de communications. |
| Contrat professionnel / infrastructure | commercial-legal pour contrat B2B ; DOM-010/015/020 selon autorisation, travaux ou accès au terrain. | Détection et orientation ; pas de traitement dans la première tranche de particulier. |

Pour un colis, établir **qui a acheté la prestation et auprès de qui**, qui
expédie, qui reçoit et pour quelle opération. Demander bordereau, preuve de
paiement du service, conditions, pouvoir éventuel et contrat de vente. Une
étiquette au nom de la personne ne suffit pas à conclure à sa qualité pour
réclamer. TEL-006 garde la qualité pour agir comme question à vérifier selon
contrat et textes ; le destinataire n'est ni déclaré automatiquement titulaire
ni exclu par principe. En cas d'intermédiaire, conserver les branches au lieu
de désigner le transporteur effectif comme seul débiteur.

Ces relais ne sont pas des dépendances d'installation. Un skill absent reste
annoncé absent, avec question et pièces à transmettre. L'opérateur, le
médiateur et le régulateur ne sont pas présentés comme le conseil de la
personne. BASE-013 : association de consommateurs ou juriste en droit de la
consommation/télécoms ou postal pour préparer la démarche ; avocat compétent
si procédure envisagée ou engagée. Phrase finale adaptée et renfort en tête
en présence d'acte, d'échéance ou d'enjeu irréversible, sans délai calculé.

## Stories et priorité

Toutes dépendent de DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008 et
BASE-013. TEL-001 possède le paquet ; TEL-002 à TEL-009 en dépendent pour ses
ressources communes. Ce sont des dépendances de livraison, sans obligation
d'exécuter TEL-001 avant une autre tâche.

| Rang | Story | Skill proposé | Référence métier future | Sortie |
|---|---|---|---|---|
| 1 | [TEL-001](../suites/tel-001-frais-resiliation.md) | `termination-fee-complaint` | `frais-resiliation.md` | Tableau des frais et réclamation de particulier. |
| 2 | [TEL-002](../suites/tel-002-materiel-restitue.md) | `equipment-return-complaint` | `materiel-restitue.md` | Preuves de retour et contestation ciblée. |
| 2 | [TEL-003](../suites/tel-003-facturation-options.md) | `subscription-billing-complaint` | `facturation-options.md` | Lignes, accord et demande de correction. |
| 2 | [TEL-004](../suites/tel-004-non-installation.md) | `uninstalled-service-complaint` | `non-installation.md` | Chronologie d'une installation non réalisée. |
| 2 | [TEL-005](../suites/tel-005-interruption-service.md) | `service-outage-complaint` | `interruption-service.md` | Journal d'interruption et demande documentée. |
| 2 | [TEL-006](../suites/tel-006-reclamation-envoi.md) | `postal-shipment-complaint` | `reclamation-envoi.md` | Contrat et rôle, réclamation postale conditionnelle. |
| 3 | [TEL-007](../suites/tel-007-mediation-telecoms.md) | `telecom-mediation-dossier` | `mediation-telecoms.md` | Dossier amiable télécoms et conditions à vérifier. |
| 3 | [TEL-008](../suites/tel-008-mediation-postale.md) | `postal-mediation-dossier` | `mediation-postale.md` | Dossier amiable postal et compétence à vérifier. |
| 3 | [TEL-009](../suites/tel-009-signalement-regulateur.md) | `telecom-postal-regulator-report` | `signalement-regulateur.md` | Alerte factuelle distincte de réparation et médiation. |

Rangs 1 et 2 : P2 ; rang 3 : P3. Chaque suite borne sa tâche, ses pièces,
sources à rechercher et scénarios. Une réclamation antérieure peut être
fournie par la personne ; les stories de médiation n'exigent pas son origine
dans un autre skill. Aucun enchaînement de neuf tâches imposé.

## Première tranche TEL-001

Particulier titulaire, abonnement fixe/mobile/internet grand public fourni
en France métropolitaine, demande de résiliation déjà faite et facture de
frais reçue ; une offre et une rupture identifiées. Entrée libre ou document,
sortie : chronologie, tableau poste/pièce/inconnue/demande et brouillon au
cocontractant identifié. Séparer frais fixes, engagement restant allégué,
matériel et service facturé ; seuls les frais de résiliation sont traités.

Pas de calcul du montant juridiquement dû, d'échéance, d'exonération acquise,
de motif légitime validé depuis le seul récit, ni de résiliation effective.
Matériel → TEL-002 ; option/facturation autonome → TEL-003 ; défaut initial
→ TEL-004 ; panne → TEL-005. Les documents utiles sont conservés pour ces
questions sans exécuter leurs tâches absentes. Professionnel, international,
outre-mer, succession, usurpation, modification contractuelle complexe,
procédure et recouvrement forcé sortent du traitement de première tranche.

## Références et recette à préparer

**Pistes non consultées dans DOM-022**, aucun droit actuel certifié : Code
des postes et des communications électroniques ; Code de la consommation
(contrat, engagement, résiliation, facturation et médiation selon le cas) ;
Code civil et textes du transport si la qualification le justifie ;
conditions datées de l'offre ou du produit postal. La fiche
[Service Public F19061](https://www.service-public.gouv.fr/particuliers/vosdroits/F19061)
et les ressources de l'[ARCEP](https://www.arcep.fr/) sont des points de
recherche, pas des règles vérifiées. Médiateurs compétents et leurs chartes
à identifier séparément pour les télécoms et chaque prestataire postal.

À l'implémentation : ouvrir les textes exacts, versions aux dates des faits,
champ, exceptions et transitions ; conserver URL, passages, date et voie
d'accès. Guides et chartes ne remplacent pas les normes. Ne pas déclarer
une source inaccessible sans tentative réelle. Appliquer BASE-005 pour
recherche, citation et lecture des décisions ; sans source, réserver la
conclusion dépendante et fournir les faits et questions utiles.

Chaque skill chargera `../../references/shared/research-citation-method.md`,
la qualification et sa référence métier locales. Recette BASE-006 : structure,
schéma, paquet détaché, installation/invocation en client sans profil ni
plugins voisins ; cas normal, pièce déterminante manquante, source absente,
variante territoriale et modèle américain à ne pas transposer. Conserver
sources effectivement lues, fixtures et sorties observées ; tests statiques,
exécution du skill et validation du résultat juridique restent distincts.

PILOTE-003 est `terminee` après BASE-011 ; son bilan est à prendre en compte
et ne sélectionne aucune extension. Toutes les suites restent `proposee`.
La relecture humaine appartient à l'utilisateur selon AGENTS.md du
17 octobre 2026 ; aucune relecture effectuée ni compréhension réelle
observée n'est revendiquée ici.
