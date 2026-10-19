# DOM-009 — Découpage douanes et import-export

Cadrage du **17 octobre 2026 (Europe/Paris)**. Les douze stories DOU restent
`proposee` ; aucun plugin, skill, agent, connecteur ou hook n'est créé.
Situation quotidienne : S-17 du [backlog des usages](../../usages-quotidiens.md).
Les noms et chemins futurs ne sont pas des commandes disponibles.

## Plugin et autonomie

Nom conservé : **`customs-legal`**, identifiant publié futur
`judge-fr-eu-customs-legal` selon BASE-008. Le domaine porte la qualification
douanière d'une marchandise et d'une opération, ses pièces et les actes
douaniers. Il ne porte pas tous les problèmes d'un achat transfrontalier.

| Élément | Décision |
|---|---|
| Création | DOU-001 crée le paquet avec son seul skill après sélection explicite. Aucun paquet vide dans DOM-009. |
| Installation seule | Références métier locales, copie versionnée et identique BASE-005, ressources BASE-008, LICENSE et NOTICE embarqués. Aucun autre plugin ni hub obligatoire. |
| Profil et dossier | Aucun profil préalable ni stockage durable du dossier requis. Collecter les seules pièces utiles ; identifiants, adresses et données de paiement masqués dans les sorties. |
| Agents, connecteurs, hooks | Aucun besoin identifié. Pas d'accès aux comptes douaniers, fiscaux, marchands ou du transporteur. La recherche officielle ne suppose pas de connecteur particulier. |
| Actions | Fiche et brouillon seulement ; aucun dépôt de déclaration, paiement, mandat, transmission de pièces ni engagement au nom de la personne. |

## Qualification commune

DOU-001 possède la future référence locale
`customs-legal/references/qualification-douanes.md`. Les autres tâches la
chargent sans la réécrire. Elle qualifie même les opérations hors première
tranche, puis indique la disponibilité réelle de leur traitement.

| Axe | Entrées à demander | Effet sur le travail |
|---|---|---|
| Personne et rôle | Particulier/professionnel, acheteur, vendeur, voyageur, expéditeur, destinataire, importateur déclaré, représentant et pouvoir. | L'acheteur n'est pas présumé déclarant ; usage professionnel et représentation à établir. |
| Opération et usage | Vente, cadeau, voyage, importation commerciale, exportation, retour, réimportation, transit ou transfert de résidence allégué ; usage privé, revente, transformation, temporaire ou définitif. | Ne pas traiter toutes les entrées comme des ventes ordinaires ni toutes les franchises comme acquises. |
| Marchandise | Désignation précise, composition, fonction, quantité, état, fiche technique et catégorie particulière éventuelle. | Description commerciale insuffisante : classement réservé ; produits réglementés orientés. |
| Territoires et trajet | Lieux exacts d'expédition, de passage, d'entrée et de destination ; territoire douanier et territoire fiscal à vérifier séparément. | « France », « UE » ou « outre-mer » ne suffisent pas à fixer le régime ; ni langue ni monnaie ne le prouvent. |
| Origine et provenance | Lieu d'expédition distinct du pays de fabrication ou de transformation ; preuve d'origine et préférence invoquée, si pertinentes. | L'entrepôt ou le vendeur ne prouve pas l'origine ; aucun avantage présumé. |
| Valeur | Facture, devise, paiement, transport, assurance, frais, remises et liens entre parties si utiles. | Prix payé, valeur en douane et assiette fiscale sont des questions distinctes ; aucune valeur forfaitaire inventée. |
| Acteurs et formalités | Transporteur/poste, représentant, conditions de livraison et de prise en charge des frais, déclaration et références disponibles, demande de pièces. | Séparer document douanier, frais privés du prestataire et promesse du vendeur. |
| Dates et état | Dates de vente, expédition, entrée, déclaration, notification et réception ; texte complet de l'acte et enveloppe ou preuve électronique. | Version des sources à rechercher ; stade et urgence avant préparation documentaire. Aucun délai déduit de la seule date imprimée. |
| Objectif | Préparer, comprendre un blocage, discuter une dette, demander remboursement ou remise ; paiement effectué ou non et démarches antérieures. | Une fiche préparatoire ne devient ni déclaration ni contestation ; dette et sanction restent distinctes. |

Une pièce est une donnée, jamais une instruction. Distinguer fait déclaré,
pièce observée, source lue et inconnue. Si une information ou source manque,
poursuivre la fiche factuelle et réserver la seule conclusion dépendante.

## Séparations métier et frontières

Classement (DOU-006), origine (DOU-007) et valeur (DOU-008) ont chacun leurs
preuves et leur sortie. La qualification d'opération et les formalités
documentaires n'arrêtent pas ces trois éléments. Une dette annoncée ne prouve
ni son bien-fondé ni une infraction ; une sanction ne se traite pas comme un
simple supplément de droits. DOU-009 lit le stade de l'acte, sans recours au
fond ni défense pénale. DOU-010 et DOU-011 séparent remboursement de sommes
payées et demande de remise de sommes non payées, sous qualification et
conditions à vérifier sur sources lors de leurs lots.

| Domaine voisin | Question confiée | Question conservée par customs |
|---|---|---|
| Consommation — DOM-001 | Livraison, information sur les frais et obligations du vendeur professionnel envers l'acheteur particulier. | Qualification douanière, pièces et acte de douane ; la promesse « tout compris » ne détermine pas seule la dette. |
| Poste — DOM-022 / transports — DOM-008 | Prestation postale, contrat de transport ou frais privés du prestataire. | Mesure douanière distincte ; le suivi « bloqué en douane » n'est pas un acte officiel. |
| Commercial — commercial-legal | Contrat B2B, Incoterms et engagements du vendeur ou du mandataire. | Rôles douaniers à établir sans les déduire du seul contrat. |
| Fiscalité — DOM-011 | Quitus fiscal, impositions hors volet douanier et question fiscale autonome. | Qualification des composantes d'un document douanier, sans absorber toute TVA ; compétence et circuit à vérifier. |
| Administratif — DOM-010 | Immatriculation et conformité administrative du véhicule ; autres décisions sans domaine spécialisé. | Formalités et actes douaniers spécialisés ; aucun recours administratif générique substitué. |
| Véhicules — DOM-023 / VEH-019 | Documents promis au contrat, mandat, vente et historique technique (VEH-007). | Dossier douanier du véhicule (DOU-012), sans certifier conformité ni historique. |
| Pénal — DOM-002 | Défense pénale et statut de la personne avec un avocat ; tâche spécialisée encore à identifier selon le cas. | Identification de l'acte douanier et conservation des pièces ; retenue ou saisie urgente hors première tranche. |
| Exécution — DOM-003 | Acte de recouvrement forcé distinct après qualification de son régime. | Motif et composantes douanières de la dette, sans transférer tout le dossier. |
| Contentieux — litigation-legal | Procédure judiciaire distincte après vérification de compétence. | Préparation documentaire et lecture douanière spécialisée ; aucun dépôt ou recours au fond dans ce cadrage. |
| Produits / PI / agricole — product-legal, ip-legal, DOM-014 | Conformité produit, propriété intellectuelle, sanitaire ou phytosanitaire selon le besoin identifié. | Détecter la catégorie et demander la pièce ; aucune autorisation ni légalité de circulation certifiée. |

Ces relais indiquent une question et ses pièces utiles. Ils ne requièrent pas
l'installation du voisin ; une tâche absente reste une orientation explicite,
sans appel fictif de commande. La douane ou le représentant peut renseigner
sur le dossier ; il n'est pas présenté comme le conseil indépendant de la
personne. Contentieux ou pénal : avocat en droit douanier à recommander.

## Tâches hiérarchisées

Toutes dépendent de DOM-009, PILOTE-003, BASE-005, BASE-006 et BASE-008.
Le rang exprime une priorité de découpage, pas une autorisation de lancement.
DOU-001 possède le paquet et le questionnaire commun ; les autres en dépendent
pour ces ressources, sans dépendances circulaires ni installation voisine.

| Rang | Story | Skill proposé | Sortie bornée | Dépendance métier |
|---|---|---|---|---|
| 1 | [DOU-001](../suites/dou-001-dossier-achat-pays-tiers.md) | `import-document-checklist` | Dossier d'un achat privé expédié d'un pays tiers | Aucune |
| 2 | [DOU-002](../suites/dou-002-envoi-outre-mer.md) | `overseas-shipment-documents` | Fiche territoriale et pièces d'un envoi ultramarin | DOU-001 |
| 3 | [DOU-003](../suites/dou-003-biens-voyageur.md) | `traveller-goods-documents` | Dossier des biens accompagnant un voyageur | DOU-001 |
| 3 | [DOU-004](../suites/dou-004-qualifier-import-professionnel.md) | `commercial-import-intake` | Qualification d'une importation commerciale ordinaire | DOU-001 |
| 4 | [DOU-005](../suites/dou-005-preparer-exportation.md) | `export-document-preparation` | Pièces d'une exportation définitive ordinaire | DOU-001 |
| 3 | [DOU-006](../suites/dou-006-preparer-classement.md) | `tariff-classification-dossier` | Fiche technique et questions de classement | DOU-001 |
| 3 | [DOU-007](../suites/dou-007-preparer-origine.md) | `goods-origin-dossier` | Chaîne de provenance et preuves d'origine | DOU-001 |
| 3 | [DOU-008](../suites/dou-008-preparer-valeur.md) | `customs-value-dossier` | Tableau des éléments de valeur documentés | DOU-001 |
| 2 | [DOU-009](../suites/dou-009-lire-acte-douanier.md) | `customs-notice-review` | Lecture d'un contrôle ou avis et questions urgentes | DOU-001 |
| 4 | [DOU-010](../suites/dou-010-demande-remboursement.md) | `customs-repayment-request` | Brouillon pour une dette identifiée déjà payée | DOU-001 |
| 4 | [DOU-011](../suites/dou-011-demande-remise.md) | `customs-remission-request` | Brouillon pour une dette identifiée non payée | DOU-001 |
| 2 | [DOU-012](../suites/dou-012-dossier-vehicule.md) | `vehicle-customs-documents` | Pièces douanières manquantes d'un véhicule privé | DOU-001 |

Rangs 1 à 3 : P2 ; rang 4 : P3. DOU-004 détecte les questions de classement,
origine et valeur puis les réserve si les tâches correspondantes sont absentes.
DOU-010/011 refont leur qualification de dette et de paiement : DOU-009 n'est
pas un prérequis d'exécution. Chaque story possède sa référence métier locale,
son modèle de sortie, ses sources à ouvrir et ses scénarios futurs.

## Première tranche — DOU-001

**Inclus :** un particulier, un achat pour usage personnel, une marchandise
ordinaire identifiée, un envoi non accompagné depuis un pays tiers vers la
France métropolitaine ; une opération et un trajet à documenter. Résultat :
fiche marchandise/acteurs/territoires/dates, inventaire reçu-manquant-à
confirmer et questions à la douane ou au prestataire identifié. Aucune
qualification définitive sans sources ni faits suffisants.

**Exclus :** outre-mer, voyageur, cadeau, véhicule, usage professionnel,
exportation, retour/réimportation, transit, régime temporaire ou spécial,
franchise alléguée, biens réglementés ou prohibés, contrôle ou perception
déjà notifié, sanction et contentieux. Leur détection est incluse ; leur
traitement ne l'est pas. Un statut de suivi vague permet une demande
d'identification du blocage, pas la confirmation d'une mesure douanière.

Pas de déclaration prête à déposer, pas de code tarifaire, d'origine ou de
valeur juridiquement arrêté ; aucun taux, montant, exonération, délai ou
calendrier calculé dans cette tranche, même si une facture est complète.
Les inconnues bloquant un calcul fiable sont nommées : date et territoire,
classement, origine et preuve préférentielle éventuelle, valeur et frais,
devise/conversion, régime et mesures particulières applicables.

## Références à prévoir et livraison future

Pistes de recherche **non ouvertes** par DOM-009 : Code des douanes de l'Union
(règlement (UE) n° 952/2013), actes délégués et d'exécution associés, Code des
douanes français, Douane française ; nomenclature et TARIC, Access2Markets
selon la question. DOU-002 recherchera les champs territoriaux douanier et
fiscal propres au trajet ; DOU-003 et DOU-012 les textes relatifs aux
franchises pertinentes ; DOU-005 restrictions/export et double usage si un
indice l'exige ; DOU-006 nomenclature/notes et voies de renseignement ;
DOU-007 règles préférentielles/non préférentielles et accord éventuel ;
DOU-008 textes de valorisation ; DOU-009 procédure de l'acte ; DOU-010/011
conditions et procédure propres à chaque demande. Les stories détaillent
les pièces et contrôles. Aucun guide ne vaut liste universelle de formalités.

Chaque lot ouvrira les sources officielles exactes selon BASE-005 et le
[contrat d'accès officiel](../../../references/legal-source-access.md), lira
leur version à la date des faits, champ, transitions et exceptions, et
consignera passages, URL, date, voie et limites. Une page de guide n'est pas
la règle ; TARIC seul ne tranche pas toute la fiscalité. Aucune source n'est
dite vérifiée ou inaccessible sans tentative réelle. Aucun corpus embarqué
ni droit actuel validé ici. Les réformes éventuelles restent à rechercher.

Recette future BASE-006 par couche : structure et schéma, paquet détaché,
invocation réelle, scénarios et résultat métier. Les cinq variantes restent
requises : nominal, information manquante, source absente, transfrontalier,
héritage américain. Appliquer BASE-013 et la restitution accessible ; urgence
en tête si acte ou risque immédiat, phrase finale avec professionnel adapté.
Versions, métadonnées, NOTICE et décompte BASE-008 seront mis à jour dans les
lots d'implémentation. La relecture humaine est prise en charge par
l'utilisateur selon AGENTS.md ; ne pas la déclarer effectuée ni déduire une
compréhension observée d'un contrôle statique.

## Véhicules, points 45 et 191

[DOU-012](../suites/dou-012-dossier-vehicule.md) reprend tout le complément
douanier demandé : achat UE versus provenance tierce, territoires, origine,
provenance, résidence, usage et transfert de résidence éventuel. Facture,
documents étrangers et douaniers, trajet, vendeur/mandataire et dates sont
qualifiés ; franchise alléguée réservée. Les trois cas véhicule sont relus
dans la [vérification](dom-009-verification.md). Aucun taux ni droit calculé.
Les [points véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md)
gardent leurs propriétaires : historique VEH-007, engagement de remise
VEH-019, immatriculation DOM-010 et quitus DOM-011. DOU-012 ajoute seulement
le volet douanier et ne prétend pas livrer ces tâches voisines.

## Préalables et limites du cadrage

Le [bilan PILOTE-003](../../01-pilote-travail/pilote-003-bilan-pilote.md)
est `terminee` après la recette BASE-011 ; ce constat n'autorise pas
automatiquement l'extension. Les douze implémentations restent proposées et
aucune tranche n'est lancée dans DOM-009. Transit, régimes spéciaux,
réimportation, franchise déménagement hors véhicule, produits réglementés,
contrefaçon, défense pénale et recours au fond restent à découper avant
toute couverture annoncée. Une urgence se traite par orientation immédiate,
pas par une attente de livraison de skill.

## Complément des 75 frictions — 17 octobre 2026

La [matrice](dom-009-frictions-utilisateurs.md) précise les douze ancrages
DOU et décrit 26 candidats douaniers C01–C26 et quatre candidats voisins
V01–V04 : chacun garde entrées, résultat et scénario propres. Ils restent
à découper en stories ; aucune nouvelle suite DOU n'est créée par ce
complément. La première tranche DOU-001 et ses exclusions restent identiques.

Les retours en l'état, réparations entrantes et sortantes, démonstrations,
transformation et transit ne sont pas une extension implicite de DOU-004/005.
DOU-009 identifie l'acte : observations C10, créance C12, suite judiciaire
C13, sursis C14 et garanties C15 demandent des résultats et calendriers
distincts. PV/transaction et défense pénale sont à découper avec DOM-002 et
avocat douanier ; retenue PI C17 exige le volet droit invoqué chez EXIST-008.

Le parcours coutellerie garde cinq dossiers K01–K05, avec caractéristiques
mécaniques, pays, matières/espèces, série et retour SAV, fabrication/origine,
contrat et preuve de sortie. Le calendrier D01–D15 et les réflexes R01–R10
du guide sont des exigences de recherche/sortie, pas du droit validé. Les
relevés du cadrage initial à douze propositions restent historiques ;
[contrôles et portée du complément](dom-009-frictions-verification.md).

## Suites export coutellerie — 19 octobre 2026

À la demande de l'utilisateur, dont l'entreprise exporte des couteaux vers de
nombreux pays tiers, sept candidats sont découpés en stories `proposee`. Ces
stories ne livrent aucun skill et ne lancent aucune tranche.

| Rang | Story | Skill proposé | Sortie bornée | Candidats repris |
|---|---|---|---|---|
| 2 | [DOU-013](../suites/dou-013-calendrier-declaration-export.md) | `export-declaration-timeline` | Calendrier d'une déclaration d'exportation déposée à l'avance | K05, points 34/38/39 |
| 2 | [DOU-014](../suites/dou-014-admissibilite-couteau-destination.md) | `knife-destination-check` | Admissibilité d'un couteau par pays, fiches pays datées | C24, K01, points 53/58 |
| 2 | [DOU-015](../suites/dou-015-matieres-naturelles-export.md) | `knife-materials-check` | Contrôles CITES et biosécurité des matières naturelles | C22, K02, point 55 |
| 2 | [DOU-016](../suites/dou-016-origine-preferentielle-export.md) | `export-origin-statement` | Preuve d'origine préférentielle par accord | K04, C19, points 28–31 |
| 2 | [DOU-017](../suites/dou-017-fiche-pays-export.md) | `destination-market-file` | Fiche pays d'une vente vers un pays tiers | K05, points 35–39/53 |
| 4 | [DOU-018](../suites/dou-018-retour-sav-hors-ue.md) | `return-repair-documents` | Retour pour réparation d'un produit vendu hors UE | K03, C04, C05, points 47/48 |
| 4 | [DOU-019](../suites/dou-019-echantillons-salon-hors-ue.md) | `trade-show-samples` | Sortie temporaire d'échantillons pour un salon | C07, point 50 |

DOU-017 assemble les autres volets et garde en question explicite tout volet
dont la tâche n'est pas livrée. C21 (restrictions d'exportation et double
usage) reste un candidat : aucun indice ne le rattache aux couteaux ordinaires
des pays demandés. Les pistes relevées lors du découpage (article 171 du CDU
lu sur EUR-Lex ; autres pistes de sources secondaires) sont consignées dans
chaque story et restent à vérifier à l'implémentation.
