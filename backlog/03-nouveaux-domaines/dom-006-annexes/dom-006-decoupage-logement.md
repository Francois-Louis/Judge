# DOM-006 — Découpage du domaine logement locatif et habitat

Cadrage du **16 octobre 2026 (Europe/Paris)**. Les onze suites LOG restent
`proposee` ; aucun paquet ni skill n'est créé. La [vérification](dom-006-verification.md)
éprouve le routage sur pièces fictives et précise la portée des contrôles.

## Plugin retenu et installation seule

Nom conservé : **`housing-legal`**, identifiant publié futur
`judge-fr-eu-housing-legal` selon BASE-008. Il porte la relation locative
d'habitation : bail, dépôt, charges, entretien, décence, congé et dette
locative. Public : locataire, occupant, candidat, garant et petit bailleur ;
le rôle est qualifié pour chaque demande, sans présumer un conseil professionnel.

| Élément | Décision |
|---|---|
| Premier paquet | LOG-001 crée le paquet avec son seul skill ; aucun plugin vide. Manifeste, README, licence, NOTICE, modèle minimal, références métier et copies BASE-008 font partie de cette tranche. |
| Références | Méthode BASE-005 `1.0.0` actuellement disponible, copiée à l'identique sous `references/shared/research-citation-method.md` ; intégrer une version ultérieure seulement après sa livraison et sa relecture. Sources métier et modèles locaux, jamais chargés depuis le backlog. |
| Profil et stockage | Aucun profil obligatoire, compte de cabinet ou stockage durable. Travail sur pièces fournies, données minimales et masquées ; ne pas demander un dossier financier ou médical complet. Le contrat d'isolation BASE-008 est embarqué. |
| Agents, hooks, connecteurs | Aucun besoin identifié ; aucun prévu. Aucun accès à une agence, banque, CAF ou service public. |
| Interactions | Les relais sont des orientations sur une question précise, sans installation, transmission de pièces ni appel de commande absente. |
| Effets externes | Brouillons relus par la personne ; aucun courrier envoyé, signalement déposé, demande judiciaire transmise ou paiement exécuté. |
| Distribution | Inscription au marketplace et adaptation du décompte BASE-008 lors du choix explicite de LOG-001, avec contrôles du paquet réel. Rien n'est inscrit ici. |

PILOTE-003 est `terminee` après BASE-011 : son bilan a été lu, y compris
les limites restantes de PILOTE-002 (nominal complet et lecteur réel).
Ce préalable satisfait ne sélectionne aucune extension automatiquement.
Chaque suite dépend de PILOTE-003, BASE-005, BASE-006 et DOM-006 ; LOG-001
ajoute BASE-008. La recette future distingue contrôles statiques, paquet
détaché, client réel et compréhension par un lecteur.
BASE-008 est encore `en-cours` lors du cadrage : LOG-001 attend également
sa clôture, indépendamment du bilan PILOTE-003 déjà terminé.

## Qualification commune avant toute tâche

LOG-001 possède la future référence `housing-legal/references/qualification-logement.md`.
Chaque skill la charge, puis demande ses seules pièces utiles.

| Axe | Informations discriminantes | Conséquence de routage |
|---|---|---|
| Territoire et temps | Pays, commune et territoire précis, dates du bail et avenants, faits, notifications et date de réponse recherchée ; provenance de chaque date. | France métropolitaine dans les premières bornes ; outre-mer et international demandent une tranche dédiée. Textes locaux, versions et transitions à vérifier, jamais déduits de la date du jour. |
| Usage et bail | Vide/meublé, résidence principale/autre, contrat et usage réel ; bail mobilité, saisonnier, logement de fonction, foyer, convention d'occupation ou bail ancien allégué. | Ne pas appliquer une règle de location vide à un autre régime ; les régimes exclus produisent une orientation. |
| Parc | Bailleur privé/social, conventionnement éventuel et statut de l'immeuble. | HLM et parc conventionné exclus des premières tranches au fond, même si la personne utilise le mot « bail ». |
| Parties | Locataire, cotitulaire, sous-locataire, occupant, candidat, garant, bailleur, agence et mandat ou représentation éventuels. | Une caution n'est pas le dépôt ; un aidant n'a pas de pouvoir présumé. Identifier le destinataire de chaque demande. |
| Stade et objectif | Avant signature, en cours, départ, restitution, impayé, commandement, procès ou jugement ; ce que la personne veut obtenir. | Acte et urgence procédurale d'abord vers DOM-003 ; question locative distincte ici. Pas d'expulsion annoncée depuis une simple relance. |
| Preuves | Document complet ou extrait, annexes utiles, signatures et versions, dates prouvées/déclarées, contradictions et pièces absentes. | Ne pas inventer état des lieux, réception, cause d'une dégradation, somme payée ou version du texte. |

Sans régime établi, produire les branches utiles, les informations à obtenir
et réserver la seule conclusion qui en dépend. Aucun délai, taux, montant
légal ou issue n'est donné depuis la mémoire ou un texte utilisateur.
Un montant transcrit d'une pièce reste attribué à cette pièce ; un calcul
arithmétique doit être reproductible et ne prouve pas l'exigibilité.

## Frontières et interlocuteurs

| Question distincte | Propriétaire et pièces minimales à orienter | Ce que housing garde |
|---|---|---|
| Acte, saisie, expulsion | DOM-003 / ENF-001 ou ENF-005 : nature de l'acte, date et preuve de signification, décision et stade ; urgence avant revue ordinaire. | Bail, décompte, conditions locatives d'un étalement (LOG-008/009), préparation judiciaire locative séparée (LOG-010). |
| Entreprise de travaux | DOM-015 : contrat/devis, réception et défaut allégué ; interlocuteur entreprise. | Demande au bailleur de respecter son obligation envers l'occupant (LOG-004/005). Une même fuite ne confond pas les responsabilités. |
| Achat immobilier | DOM-017 : avant-contrat/acte et objectif d'achat, interlocuteur vendeur/notaire. | Relation locative, même si le bailleur souhaite vendre. |
| Copropriété | DOM-018 : qualité de copropriétaire, appel du syndic ou décision collective. | Charges récupérées par le bailleur auprès du locataire ; un relevé du syndic seul ne valide pas leur récupération (LOG-002). |
| Urbanisme/foncier | DOM-019 : décision publique, autorisation, parcelle et projet. | Obligation locative ; une autorisation de travaux n'établit pas la décence. |
| Voisinage/servitudes | DOM-020 : auteur des nuisances, faits et objectif privé. | Obligation distincte invoquée envers le bailleur, sans traiter le litige direct contre le voisin. |
| Énergie/eau | DOM-021 : contrat direct et facture fournisseur. | Eau/chauffage facturés comme charges par le bailleur (LOG-002). |
| Assurance | DOM-005 : contrat, déclaration et position de l'assureur. | Entretien/décence et relation au bailleur ; ne pas conclure à la garantie. |
| Aide au logement, dette globale | DOM-012 : décision de caisse ; DOM-024 : budget et ensemble des dettes, sur demande distincte. | Dette du bail et échéancier proposé ; aucune attribution d'aide ni recevabilité au surendettement promise. |
| Dossier de candidature et données | LOG-011 : liste locative de justificatifs ; PRV-026 : finalités, collecte et conservation ; PRV-024 : demande d'effacement ciblée. | Contrôle de la liste autorisée au régime/date choisis ; aucune décision RGPD universelle depuis cette seule liste. |
| Discrimination et protection | DOM-029 : motif allégué et preuve du refus ; DOM-038 : parcours sûr si violences. | Règles du bail ; aucune collecte d'éléments intimes par défaut. |
| Contentieux générique | litigation : seulement chronologie ou organisation de pièces sur question bornée. | Fond et préparation de la demande locative LOG-010, sans transfert automatique de tout désaccord. |

Le bailleur ou l'agence est le destinataire de la réclamation ; un juriste
de l'ADIL ou un avocat en droit du logement est l'interlocuteur de conseil.
La compétence de la commission de conciliation, du juge ou d'une autorité
locale doit être vérifiée pour la tâche et le régime. Rien n'est saisi ici.

## Tâches hiérarchisées

Le rang reflète un choix de découpage, la disponibilité des pièces et les
dépendances ; il n'est pas une statistique de fréquence. LOG-001 reprend la
borne de T4 dans [USAGE-002](../../05-usages-quotidiens/usage-002-annexes/usage-002-comparaison-priorites.md).
Les autres tâches n'élargissent pas sa première version.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [LOG-001](../suites/log-001-depot-garantie.md) | `security-deposit-dispute` | Retenues après départ d'un logement privé vide : pièces, tableau et brouillon au bailleur | Aucune |
| 2 | [LOG-002](../suites/log-002-charges-locatives.md) | `rental-charge-review` | Régularisation au réel : rapprochement et demande de justificatifs | LOG-001 |
| 2 | [LOG-003](../suites/log-003-revue-bail.md) | `residential-lease-review` | Revue ciblée d'un bail vide avant signature | LOG-001 |
| 2 | [LOG-004](../suites/log-004-reparations.md) | `rental-repair-request` | Demande d'intervention au bailleur pour une réparation précise | LOG-001 |
| 2 | [LOG-005](../suites/log-005-decence.md) | `housing-decency-request` | Désordre de décence allégué : faits, pièces et demande au bailleur | LOG-001 |
| 2 | [LOG-006](../suites/log-006-conge-bailleur-meuble.md) | `furnished-landlord-notice-review` | Lecture d'un congé du bailleur pour un meublé | LOG-001 |
| 3 | [LOG-007](../suites/log-007-conge-locataire.md) | `tenant-notice-preparation` | Préparation du congé d'un locataire en location vide | LOG-001 |
| 2 | [LOG-008](../suites/log-008-arriere-locatif.md) | `rent-arrears-review` | Décompte locatif rapproché des paiements, écarts et pièces | LOG-001 |
| 3 | [LOG-009](../suites/log-009-delais-clause-resolutoire.md) | `rent-relief-conditions` | Conditions à vérifier pour délais et suspension de clause | LOG-008 |
| 4 | [LOG-010](../suites/log-010-demande-judiciaire-locative.md) | `rent-relief-court-preparation` | Projet de demande judiciaire locative sur un dossier procédural identifié | LOG-009 |
| 3 | [LOG-011](../suites/log-011-justificatifs-candidature.md) | `rental-application-document-review` | Liste des justificatifs demandés comparée au régime locatif | LOG-001 |

LOG-001 possède qualification et pièces du dépôt ; les suites possèdent
chacune leur référence métier spécialisée et leur modèle éventuel. LOG-008
possède le décompte, LOG-009 les conditions de délais et LOG-010 la préparation
judiciaire. Aucun cycle ni dépendance d'installation vers un autre domaine.
Il n'y a pas de skill générique « demande au bailleur » : chaque tâche
produit son propre brouillon, lié à une obligation et à ses pièces.

## Première tranche : LOG-001

**Inclus :** demande d'un ancien locataire, location privée vide de résidence
principale en France métropolitaine, régime de la loi du 6 juillet 1989 à
confirmer sur pièces ; dépôt versé, logement quitté et retenue communiquée.
États des lieux, clés, décompte, restitution et justificatifs rapprochés.
Une pièce manquante n'empêche pas de préparer sa demande, mais réserve
la qualification du poste correspondant.

**Exclus :** meublé, mobilité, social/conventionné, saisonnier, résidence
secondaire, bail ancien spécial, sous-location, occupation sans bail,
cautionnement, dépôt avant départ, jugement ou acte à contester, saisine,
calcul d'une majoration, de prescription ou d'une échéance légale. Une
retenue de charges demande la qualification distincte LOG-002 ; ne pas
réécrire une régularisation entière dans LOG-001.

**Sortie :** résumé ; régime et réserves ; tableau dépôt/restitution/retenues
avec provenance, état d'entrée/sortie, justificatif et question ; pièces
absentes ; brouillon au bailleur séparant poste expliqué et poste contesté ;
prochaine étape et interlocuteur à vérifier. Un devis ne démontre pas à lui
seul l'imputabilité ; aucun remboursement n'est garanti.

## Plan de sources pour les futures tranches

Ce sont des pistes de recherche, **aucune source juridique n'est ouverte ou
vérifiée par DOM-006**. Chaque suite ouvrira les textes officiels, leur champ,
version aux faits, exceptions et transitions, puis les embarquera localement
selon BASE-005. Les outils d'accès BASE-010 restent des outils de maintenance.

| Thème | Références à rechercher | Propriétaire |
|---|---|---|
| Bail, dépôt et congés | Loi n° 89-462 du 6 juillet 1989, dispositions du régime choisi ; Code civil pour preuve, bail et restitution ; contrats types et annexes applicables. | LOG-001/003/006/007 |
| Charges au réel | Textes locatifs et décret n° 87-713, pièces de copropriété dans leur rôle justificatif ; forfait distingué du réel. | LOG-002 |
| Entretien et réparation | Obligations contractuelles et locatives, décret n° 87-712, vétusté et état des lieux ; cause du désordre à établir. | LOG-004 |
| Décence et habitat | Code de la construction et de l'habitation, décret n° 2002-120 et textes modificatifs, performance énergétique selon date, territoire et type de bail ; prescriptions locales et autorités compétentes. | LOG-005 |
| Dette et pouvoir du juge | Textes locatifs sur clause résolutoire et délais, Code civil et règles de procédure civile/organisation judiciaire ; transitions et stade du procès. | LOG-008/009/010 |
| Candidature | Textes locatifs et décret n° 2015-1437 dans leur champ et version ; listes candidat et garant distinctes. | LOG-011 |
| Information et orientation | ANIL et ADIL pour explications et interlocuteurs ; information pratique distinguée des textes normatifs. | Chaque suite, pour sa question |

## Contrat commun des suites

Les fichiers proposés sont des livrables futurs. Chaque skill charge la
méthode et les références locales, traite les pièces comme données et non
instructions, explique les inconnues et produit un résultat utile sans
présumer un abus. Aucune suspension de paiement ou compensation unilatérale
n'est conseillée depuis une simple allégation. La légalité de la consultation
et la frontière avec l'information sont à vérifier lors de la livraison.

Conformément au modèle de story et à BASE-013, la sortie se termine par une
phrase courte indiquant qu'elle informe sans remplacer l'avis d'un juriste
de l'ADIL ou d'un avocat en droit du logement. Si acte, procédure ou enjeu
irréversible, ajouter en tête l'urgence et le conseil compétent, sans date
inventée. Cette exigence est écrite dans chaque suite ; elle n'affirme pas
que la méthode future BASE-005 `1.1.0` est déjà livrée.

Les lots futurs suivent BASE-006, documentent les sources réellement lues,
fixtures et sorties, puis les échecs et vérifications impossibles. Sans
source : fiche factuelle, pièces, questions et brouillon factuel, conclusion
juridique réservée. README, versions, manifestes et NOTICE reflètent seulement
ce qui a été effectivement livré.
