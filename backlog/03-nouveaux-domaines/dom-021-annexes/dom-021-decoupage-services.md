# DOM-021 — Découpage énergie, eau et services essentiels

Cadrage du **17 octobre 2026 (Europe/Paris)**. Quatorze propositions UTI ;
les noms de skills et chemins futurs ne sont pas des commandes disponibles.
Le [bilan de la story](../dom-021-energie-eau.md#bilan-dexécution--17-octobre-2026)
porte la portée du lot et la prise en charge de la relecture.

## Plugin et autonomie

Nom conservé : `utilities-legal`, identifiant publié futur
`judge-fr-eu-utilities-legal`. Le domaine porte les relations d'un ménage
avec un fournisseur d'énergie, un gestionnaire de réseau ou le service
d'eau, pour facturation, événement contractuel ou accès au service.
« Services essentiels » ne désigne pas tous les services publics : télécoms
et poste restent DOM-022, aides sociales DOM-012, rénovation DOM-015.

| Élément | Contrat futur |
|---|---|
| Création | UTI-001 crée le paquet avec un seul skill après sélection ; aucune création de plugin ni inscription marketplace dans DOM-021. |
| Installation seule | Références métier et modèles locaux, copie BASE-005 identique/versionnée, ressources d'isolation BASE-008, LICENSE et NOTICE ; aucun hub ou plugin voisin nécessaire. |
| Qualification | UTI-001 possède `utilities-legal/references/qualification-services.md` ; elle distingue tous les services et indique la disponibilité réelle des autres tâches. |
| Sortie | Explication, tableau, questions et brouillon à relire ; jamais un envoi, paiement, souscription, résiliation ou rétablissement exécuté. |
| Données | Pièces minimales, références de point et coordonnées masquées dans les sorties, pas de code ni accès à un compte, pas de dossier durable exigé. |
| Agents, hooks, connecteurs | Aucun besoin identifié ; la recherche officielle ne nécessite pas un connecteur de fournisseur. |
| Recette | BASE-006 par couche ; un manifeste valide ne prouve pas le résultat métier. Versions et métadonnées actualisées à chaque livraison. |

## Qualification commune avant toute règle

Partir du récit : « ma facture augmente », « je n'ai pas accepté »,
« je déménage », « on va couper ». Poser seulement les questions utiles
pour identifier le service, le document et l'urgence avant le code pertinent.

| Axe | Entrées nécessaires | Effet sur l'orientation |
|---|---|---|
| Service | Électricité, gaz naturel de réseau, eau potable/assainissement ; GPL, chaleur collective ou autre service à identifier. | Aucun régime commun supposé ; les produits hors tranche restent à découper. |
| Personne et usage | Abonné direct, occupant, locataire, propriétaire, copropriétaire, représentant ; ménage/professionnel, résidence principale/secondaire et lieu exact. | Un occupant n'est pas présumé titulaire du contrat ; les protections et territoires ne sont pas présumés. |
| Acteurs | Fournisseur qui facture, gestionnaire du réseau/mesure, régie ou délégataire, collectivité, bailleur/syndic ; auteur et destinataire du courrier. | La fourniture et le réseau sont distincts comme fonctions ; pas nécessairement deux personnes morales distinctes. |
| Contrat | Offre, clauses et grilles datées, règlement local et acte tarifaire pour l'eau, canal et preuve de souscription, avis de modification. | Souscription, modification et simple changement de mensualité ne sont pas interchangeables. |
| Mesure | Point/compteur identifié, index initial/final, unités, dates, estimation/relève réelle, changement de compteur ; m³/kWh et coefficient du gaz. | Une rupture de chaîne ou de conversion devient une pièce à demander ; aucun volume ou tarif inventé. |
| Facturation | Périodes, prix, abonnement, taxes/redevances affichées, eau/assainissement, acomptes, paiements, avoirs et solde. | Vérification arithmétique distincte du montant juridiquement dû ; double imputation à vérifier. |
| Événement | Ouverture, modification, départ, demande de clôture, réception et confirmation, index de sortie. | Départ du logement et fin de contrat ne sont pas confondus. |
| Urgence | État réel du service, motif et auteur, mesure annoncée, date et réception prouvée, procédure/acte, danger ou besoin immédiat signalé. | UTI-011/012/013 pour impayé ; UTI-014 hors impayé ; sécurité et conseil rapide sans attendre le fond. |
| Eau anormale | Historique comparable, alerte/réception, abonné, localisation et type de fuite, attestation, contrôle du compteur. | UTI-004 ; charges collectives et droit de l'abonné séparés. |
| Demande | Comprendre, obtenir des preuves, faire examiner une correction ou préserver le service ; démarches et réponses déjà reçues. | Le brouillon porte une demande précise ; aucun tort ni résultat présumé. |

Une pièce reçue n'est pas une instruction. Distinguer faits déclarés,
pièces observées, sources effectivement lues et inconnues. Sans source,
préparer les faits et réserver la conclusion dépendante. En cas d'urgence
ou de danger, identifier le contact officiel approprié et vérifier ses
coordonnées ; pas de diagnostic ni manipulation de réseau/compteur.

## Tâches et ordre proposé

Toutes restent `proposee`, priorité P2. Elles dépendent de DOM-021,
PILOTE-003, BASE-005, BASE-006 et BASE-008. UTI-002 à UTI-014 dépendent en plus
d'UTI-001 pour le paquet et la qualification commune, sans devoir exécuter
sa lecture de facture. Le rang est une proposition ; l'urgence d'un dossier
ne signifie pas qu'un skill existe déjà.

| Rang | Story | Entrée par problème | Skill proposé |
|---|---|---|---|
| 1 | [UTI-001](../suites/uti-001-regularisation-electricite.md) | Ma facture d'électricité augmente après des estimations. | `electricity-bill-review` |
| 2 | [UTI-002](../suites/uti-002-regularisation-gaz.md) | Les mètres cubes relevés et les kWh facturés de gaz ne correspondent pas. | `gas-bill-review` |
| 2 | [UTI-003](../suites/uti-003-facture-eau.md) | Je ne comprends pas les volumes et les lignes de ma facture d'eau. | `water-bill-review` |
| 2 | [UTI-004](../suites/uti-004-surconsommation-eau.md) | Une fuite a été réparée et ma facture d'eau reste énorme. | `water-overconsumption-request` |
| 3 | [UTI-005](../suites/uti-005-souscription-energie.md) | Je découvre un contrat d'énergie que je dis ne pas avoir accepté. | `energy-subscription-complaint` |
| 3 | [UTI-006](../suites/uti-006-modification-energie.md) | Mon prix ou mon abonnement d'énergie a changé sans mon accord allégué. | `energy-contract-change-review` |
| 3 | [UTI-007](../suites/uti-007-cloture-energie.md) | Après mon déménagement ou ma résiliation, on me facture encore l'énergie. | `energy-closing-bill-review` |
| 3 | [UTI-008](../suites/uti-008-souscription-eau.md) | Le service d'eau m'a ouvert un abonnement ou réclame des frais que je ne comprends pas. | `water-subscription-complaint` |
| 3 | [UTI-009](../suites/uti-009-modification-eau.md) | Le tarif ou les conditions de mon service d'eau ont changé. | `water-service-change-review` |
| 3 | [UTI-010](../suites/uti-010-cloture-eau.md) | J'ai quitté le logement mais le service d'eau continue de facturer. | `water-closing-bill-review` |
| 2 | [UTI-011](../suites/uti-011-urgence-electricite.md) | Un courrier annonce une réduction ou une coupure d'électricité. | `electricity-interruption-notice` |
| 2 | [UTI-012](../suites/uti-012-urgence-gaz.md) | Mon fournisseur annonce une coupure de gaz. | `gas-interruption-notice` |
| 2 | [UTI-013](../suites/uti-013-urgence-eau.md) | On me menace de couper l'eau pour une facture impayée. | `water-interruption-notice` |
| 3 | [UTI-014](../suites/uti-014-interruption-reseau.md) | Je n'ai plus d'eau, de gaz ou d'électricité et je ne sais pas à qui m'adresser. | `utility-outage-intake` |

Chaque story fixe ses pièces, sortie, référence métier, exclusions et
scénarios. Souscription, modification et clôture ont chacune leur tâche,
avec séparation énergie/eau. La réclamation reste adressée à la partie
identifiée ; une orientation amiable ne devient pas un dépôt de médiation.

## Première tranche — UTI-001

Une régularisation d'électricité, ménage abonné directement, fourniture
individuelle et France métropolitaine. Sortie : chronologie des index et
estimations, périodes, prix documentés et acomptes, écarts et inconnues,
brouillon de demande de justification au fournisseur.

Sont exclus de ce premier skill : eau, gaz, chauffage collectif, contrat
professionnel, autoconsommation/production, souscription litigieuse,
modification de contrat, clôture, menace de coupure et acte de recouvrement.
La détection et l'orientation restent incluses. Même une facture complète
ne suffit pas à promettre remboursement ou annulation, trancher une
prescription ou certifier un solde exigible.

## Frontières et interlocuteurs

| Domaine voisin | Question confiée | Question gardée par utilities |
|---|---|---|
| Logement — DOM-006 / LOG-002 | Répartition et récupération de charges par bailleur, justificatifs locatifs. | Droit du titulaire de l'abonnement au service, identifié séparément ; UTI-003/004 ne rendent pas l'occupant abonné. |
| Logement — LOG-004/005 | Réparation/décence et panne de chauffage ou eau chaude dans le logement. | Continuité de fourniture au point ; UTI-014 distingue réseau et équipement, sans expertise technique. |
| Exécution — ENF-005 / DOM-003 | Privation par bailleur pour faire partir l'occupant, éviction ; acte d'exécution selon son régime. | Menace du fournisseur/service pour impayé et examen du bien-fondé sectoriel de la facture ; simple relance reste ici. |
| Assurance — INS-017 | Coordination d'un dégât des eaux, recherche de fuite et garantie d'assurance. | Conditions d'examen de la facture par le service d'eau, sans en déduire responsabilité ou garantie. |
| Copropriété — DOM-018 | Parties communes/privatives, répartition et décision du syndicat, recherche de fuite selon question. | Demande de l'abonné au service ; syndic ou syndicat ne se confond pas avec chaque occupant. |
| Travaux — DOM-015 | Rénovation énergétique, équipement et contrat de travaux. | Facturation et contrat de fourniture ; aucune certification de performance énergétique. |
| Protection sociale — DOM-012 / dettes — DOM-024 | Attribution/refus d'aide, accompagnement social ou difficultés globales et surendettement. | Repérer la démarche sociale alléguée et ses justificatifs utiles à la continuité du service, sans attribuer une aide. |
| Consommation — DOM-001 | Vente hors secteur spécialisé. | Règles de consommation utiles à l'énergie/eau embarquées localement, sans dépendre de consumer. Tant que utilities est absent, disponibilité réelle et limites générales explicites. |
| Administratif — DOM-010 | Acte administratif autonome identifié, hors traitement sectoriel prévu. | Régime, service, auteur et objet à qualifier ; ni juge ni recours déduit du seul opérateur public ou privé. |
| Données — privacy-legal | Exercice d'un droit sur des données de compteur/compte, selon la demande. | Données de relève utiles à la facture, sans transformer la demande de justificatifs en analyse RGPD. |

Le fournisseur/service explique son dossier et reçoit la demande ; le
gestionnaire traite la question de mesure/réseau selon ses fonctions.
Un travailleur social accompagne les difficultés de paiement.
Le conseil est distinct : juriste d'une association de consommateurs selon
son objet ou avocat compétent en consommation/services publics selon la
question ; avocat pour le contentieux. Appliquer BASE-013 (renfort en tête
si nécessaire, phrase finale adaptée), sans opposer un avertissement à la
préparation factuelle.

Le Médiateur national de l'énergie n'est pas donné comme médiateur de l'eau.
Pour chaque voie amiable, rechercher compétence, opérateur concerné,
réclamation préalable, dates et recevabilité sur sources actuelles ; ne pas
annoncer une saisine acquise ni une suspension des mesures. Pour l'eau,
identifier la médiation pertinente à partir du service et des sources
officielles, sans la généraliser à tout litige du logement.

## Sources et méthode de livraison

Le [registre DOM-021](dom-021-sources.md) porte les lectures effectivement
faites et les échecs. Les références métier futures restent chacune dans
`utilities-legal/references/`. Codes de l'énergie, de la consommation,
CGCT, Code de l'action sociale et des familles, textes réglementaires,
contrats et actes locaux sont recherchés par tâche, avec versions,
territoires, transitions et exceptions aux dates des faits.

L'implémentation applique la méthode BASE-005 locale et le
[contrat d'accès officiel](../../../references/legal-source-access.md).
Aucun taux, seuil, délai, calcul de protection ou solution de jurisprudence
n'est validé ici. Toute décision invoquée doit être ouverte et lue selon
BASE-005 section 10 ; un guide n'en tient pas lieu.

Recette future : cinq variantes BASE-006 (nominal, information manquante,
source absente, transfrontalier, héritage américain), structure, schéma,
artefact isolé, client réel et résultat métier. Les scénarios particuliers
de chaque story s'y ajoutent. Aucun autre plugin nécessaire au chargement.

## Complément logement et suites non lancées

Le point 27 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md)
est attribué à UTI-004 pour la surconsommation ; LOG-002 garde les charges.
Les relais 37, 44 et 54 conservent ENF-005, LOG-004/005, INS-017 et DOM-018
pour leurs questions précises. Les voies urgentes eau/électricité/gaz sont
UTI-013/011/012 ; coupure matérielle d'un bailleur : ENF-005.

PILOTE-003 est terminé après BASE-011. Relire son bilan avant l'extension ;
aucune adaptation n'est lancée par cette story. Les quatorze suites restent
proposées jusqu'à sélection. GPL/citerne, réseaux de chaleur, raccordement
neuf, qualité sanitaire au fond, professionnels, production et territoires
hors tranche restent à découper avant toute couverture annoncée.
