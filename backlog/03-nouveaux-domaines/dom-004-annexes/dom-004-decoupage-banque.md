# DOM-004 — Découpage du domaine bancaire

Propositions du **16 octobre 2026**. Les 19 stories BNK restent `proposee`.
La [matrice des 99 frictions utilisateur](dom-004-frictions-utilisateurs.md)
complète les exigences et propose BNK-013 à BNK-019 ; les règles du texte
fourni restent à vérifier. Les placements gardent leur périmètre d'orientation.
La [relecture documentaire](dom-004-verification.md) éprouve le routage sur
les trois scénarios de la story et sur des cas limites. Aucun répertoire de
plugin n'est créé par ce cadrage.

## Plugin retenu et contrat d'installation

**Nom conservé : `banking-legal`**, identifiant publié
`judge-fr-eu-banking-legal` (BASE-008). Le nom de skill `payment-dispute`,
laissé « à confirmer » par l'exemple d'arborescence BASE-003, est confirmé
pour BNK-001. Le domaine traite le compte, les opérations de paiement et le
crédit d'une personne avec son prestataire. Public premier : le particulier
titulaire d'un compte ou emprunteur, sans formation juridique. Public second :
l'entrepreneur individuel ou la TPE pour son compte professionnel.

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 `1.0.0` et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais est une orientation. |
| Création du paquet | Par BNK-001, avec son premier skill. Aucun paquet vide. Inscription au marketplace et décompte des paquets dans les tests BASE-008 : décision explicite au moment de sélectionner BNK-001, coordonnée avec les autres premières tranches DOM retenues. |
| Profil et stockage | Aucun profil requis. Les données bancaires (numéros de compte, de carte, codes) ne sont ni demandées en entier ni conservées. Un stockage n'est ajouté que par une story dédiée. |
| Agents, hooks, connecteurs | Aucun prévu ; aucun accès à un compte en ligne. Les pièces sont fournies par la personne. |
| Envoi | Brouillons seulement ; le plugin ne contacte pas la banque et ne fait aucune opposition. |

## Garde-fous propres au domaine

- **Urgence d'abord.** Fraude en cours, carte ou accès compromis : la sortie
  commence par l'opposition et le signalement au prestataire, par ses canaux
  officiels.
- **Jamais de code ni d'identifiant complet.** Le plugin ne demande ni code,
  ni mot de passe, ni numéro de carte complet, et rappelle qu'aucun
  conseiller légitime ne les demande.
- **Trois qualifications séparées.** Paiement non autorisé, opération
  autorisée sous tromperie et litige avec le commerçant ne reçoivent ni la
  même réclamation ni le même interlocuteur. Une règle privée de réseau de
  cartes (rétrofacturation) n'est pas présentée comme un droit.
- **Aucune conclusion sur la négligence.** La négligence alléguée par la
  banque ou par la personne reste une question, jamais une conclusion.
- **Aucun conseil d'investissement.** Placements et actifs numériques sont
  seulement orientés (BNK-011).

## Qualification commune

BNK-001 crée `banking-legal/references/qualification-bancaire.md`, réutilisée
par les autres skills du paquet.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Statut du client | Personne physique pour des besoins privés, entrepreneur individuel, société, association ; compte personnel ou professionnel. | Protections et médiation applicables, à vérifier par tâche ; un compte professionnel n'est pas traité avec les repères du particulier. |
| Prestataire | Banque, établissement de paiement ou de monnaie électronique, prêteur, intermédiaire, prestataire d'actifs numériques ; pays d'agrément. | Interlocuteur, médiateur, régime ; actif numérique → BNK-011. |
| Contrat | Convention de compte, conditions tarifaires datées, contrat de carte, offre de crédit, mandat de prélèvement. | Version applicable à la date de l'opération. |
| Opération | Carte, virement (instantané ou non), prélèvement, chèque, retrait ; montant, bénéficiaire, date, pays, devise. | Régime de l'instrument, à vérifier. |
| Consentement | Opération inconnue, validée par la personne sous tromperie, validée et contestée pour un motif commercial ; mode d'authentification déclaré. | Les trois branches de BNK-001. |
| Dates | Opération, découverte, signalement au prestataire, réclamation, réponse. | Aucun délai calculé sans texte lu. |
| Nature du produit | Compte, paiement, crédit, placement, assurance. | Placement → BNK-011 ; assurance → DOM-005. |

## Frontières

| Domaine | Ce qui lui revient | Ce que banking garde |
|---|---|---|
| Consommation — DOM-001 | Litige avec le vendeur (non-livraison, défaut). | Contestation du paiement auprès du prestataire ; mécanismes de réseau présentés comme règles privées. |
| Assurance — DOM-005 | Assurance emprunteur, assurance des moyens de paiement, garanties attachées à une carte. | Le crédit et l'opération de paiement. |
| Surendettement — DOM-024 | Situation globale, procédure et ses effets. | Difficulté sur un crédit identifié (BNK-007) et lecture d'une inscription à un fichier (BNK-010). |
| Exécution — DOM-003 | Saisie sur compte et sommes laissées disponibles. | Frais facturés par la banque au titre de la saisie (BNK-003). |
| Pénal — DOM-002 | Plainte pour escroquerie, usurpation. | Demande de remboursement au prestataire. |
| Données — EXIST-003/PRV | Fuite de données, accès aux données détenues par la banque. | Conséquences de la fraude sur le compte. |
| Numérique — DOM-034 | Compte d'une plateforme qui n'est pas prestataire de paiement. | Compte chez un prestataire de paiement, y compris en ligne. |
| Sociétés — EXIST-002/SOC | Pouvoirs bancaires dans la société (SOC-002). | Frais et opérations du compte professionnel. |
| Immobilier — DOM-017 | Avant-contrat, condition suspensive de prêt. | Offre de prêt (BNK-005). |
| Successions — DOM-016 | Comptes du défunt et leur déblocage. | Rien, hors question bornée. |
| Investissement et actifs numériques | Aucun domaine ne les porte, par décision du 16 octobre 2026. Assurance-vie → DOM-005. | Orientation seule (BNK-011) vers les autorités et les canaux à vérifier. |

**Décisions du 16 octobre 2026** ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)) : placements et actifs numériques
restent en orientation seule (BNK-011), sans cadrage dédié ; la caution
donnée pour un prêt est découpée dans BNK-012.

## Tâches hiérarchisées

Le rang combine l'utilité directe (situation S-09), l'urgence des fraudes,
la vérifiabilité et les dépendances. Il reste une proposition : aucune story
n'est sélectionnée par DOM-004. Toutes dépendent de DOM-004, PILOTE-003,
BASE-005 et BASE-006 ; BNK-001 crée le paquet. Les rangs 1 à 3 portent la
priorité P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [BNK-001](../suites/bnk-001-contester-paiement.md) | `payment-dispute` | Qualification d'un paiement contesté et réclamation au prestataire | Aucune |
| 2 | [BNK-002](../suites/bnk-002-virement-tromperie.md) | `authorised-fraud-claim` | Dossier et réclamation après une opération validée sous tromperie | BNK-001 |
| 2 | [BNK-003](../suites/bnk-003-frais-bancaires.md) | `bank-fees-claim` | Comparaison relevé/conditions tarifaires et réclamation sur des frais | BNK-001 |
| 2 | [BNK-004](../suites/bnk-004-mediation-bancaire.md) | `bank-mediation` | Escalade : service réclamation, puis médiateur | BNK-001 |
| 3 | [BNK-005](../suites/bnk-005-offre-credit.md) | `credit-offer-reading` | Lecture d'une offre de crédit et questions ciblées | BNK-001 |
| 3 | [BNK-006](../suites/bnk-006-prelevement.md) | `direct-debit-dispute` | Contestation d'un prélèvement | BNK-001 |
| 3 | [BNK-007](../suites/bnk-007-difficulte-credit.md) | `credit-repayment-difficulty` | Options à vérifier face à des échéances impayées | BNK-005 |
| 3 | [BNK-008](../suites/bnk-008-cloture-compte.md) | `account-closure-access` | Clôture, refus d'ouverture et droit au compte | BNK-001 |
| 3 | [BNK-013](../suites/bnk-013-mobilite-bancaire.md) | `bank-switch-follow-up` | Suivre une mobilité bancaire et ses incidents | BNK-001 |
| 3 | [BNK-014](../suites/bnk-014-blocage-compte.md) | `account-block-review` | Préparer une demande sur un compte ou un virement bloqué | BNK-001 |
| 3 | [BNK-015](../suites/bnk-015-erreur-virement.md) | `transfer-error-claim` | Réagir à une erreur d'exécution ou de bénéficiaire d'un virement | BNK-001 |
| 3 | [BNK-016](../suites/bnk-016-carte-preautorisation.md) | `card-hold-review` | Comprendre un double débit, une préautorisation ou un plafond de carte | BNK-001 |
| 3 | [BNK-017](../suites/bnk-017-compte-inactif.md) | `inactive-account-search` | Rechercher les fonds d'un compte inactif | BNK-001 |
| 3 | [BNK-018](../suites/bnk-018-financement-professionnel.md) | `business-credit-response` | Réagir à une réduction de concours ou à un refus de financement professionnel | BNK-005 |
| 3 | [BNK-019](../suites/bnk-019-encaissement-professionnel.md) | `merchant-settlement-review` | Comprendre les frais d'encaissement et les fonds commerçants retenus | BNK-001 |
| 4 | [BNK-009](../suites/bnk-009-remboursement-anticipe.md) | `credit-early-repayment` | Questions sur un remboursement anticipé ou une renégociation | BNK-005 |
| 4 | [BNK-010](../suites/bnk-010-fichiers-banque-france.md) | `banque-de-france-file-reading` | Lecture d'une inscription à un fichier de la Banque de France | BNK-007 |
| 4 | [BNK-011](../suites/bnk-011-placement.md) | `investment-orientation` | Orientation d'une réclamation sur un placement ou un actif numérique | BNK-001 |
| 4 | [BNK-012](../suites/bnk-012-caution.md) | `guarantee-review` | Lecture d'un engagement de caution ou d'un appel en garantie | BNK-005 |

BNK-001 possède `qualification-bancaire.md` et `paiements.md`, relus par
BNK-002 et BNK-006 ; BNK-004 possède `mediation-bancaire.md` ; BNK-005
possède `credit.md`, relu par BNK-007 et BNK-009. Une tâche suivante consomme
ces références sans les réécrire. Aucun cycle de dépendances.

## Première tranche : BNK-001

**Inclus :** une opération de paiement contestée sur un compte de paiement
par une personne physique pour ses besoins privés : carte ou opération
inconnue (non autorisée), avec réclamation complète. Opération validée sous
tromperie et litige avec le commerçant : qualification, actions urgentes et
orientation vers BNK-002 ou DOM-001.

**Exclus :** compte professionnel (qualification puis BNK-003 ou orientation) ;
prélèvement (BNK-006) ; chèque ; crédit ; actif numérique ; calcul de délai
ou de franchise ; conclusion sur la négligence ; opposition faite à la place
de la personne ; plainte ; envoi.

**Sortie :** maintenant (opposition, signalement par les canaux officiels) ;
fiche de l'opération avec statut de chaque fait ; branche retenue et ce qui
la décide ; pièces ; brouillon de réclamation au prestataire ; suites
(médiation BNK-004, plainte DOM-002, vendeur DOM-001) ; limites.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005. Les voies officielles BASE-010 servent en maintenance, jamais au
runtime. Une proposition de texte européen n'est jamais citée comme droit en
vigueur.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Opération non autorisée | Code monétaire et financier, services de paiement (pistes L133-18, L133-19, L133-23, L133-24) ; directive (UE) 2015/2366. | BNK-001 |
| Opération sous tromperie | Mêmes textes ; jurisprudence récente sur les fraudes au « faux conseiller », à lire ; règlement (UE) 2024/886 sur les virements instantanés pour la vérification du bénéficiaire, date d'application à vérifier. | BNK-002 |
| Prélèvement | Code monétaire et financier (piste L133-25) ; règles SEPA. | BNK-006 |
| Frais | Code monétaire et financier, convention de compte et plafonnement de certains frais (pistes L312-1-1, L312-1-3) ; règles propres à la clientèle fragile ; distinction particulier et professionnel. | BNK-003 |
| Médiation | Code monétaire et financier, médiation bancaire (piste L316-1) ; Code de la consommation, médiation ; rôle de l'ACPR et d'ABE Infoservice comme information, pas comme recours. | BNK-004 |
| Crédit | Code de la consommation, crédit à la consommation et immobilier (pistes L312-1 et suivants, L313-1 et suivants) ; directive (UE) 2023/2225, transposition et date d'application à vérifier. | BNK-005, BNK-007, BNK-009 |
| Compte | Code monétaire et financier, droit au compte et clôture (piste L312-1) ; procédure Banque de France. | BNK-008 |
| Fichiers | Code de la consommation et textes Banque de France sur les fichiers d'incidents. | BNK-010 |
| Placements | Listes et alertes de l'AMF et de l'ACPR ; médiateur de l'AMF. Orientation seulement. | BNK-011 |

## Contrat commun des stories BNK

Les nouvelles suites recherchent aussi les régimes de mobilité et de
comptes inactifs, les règles d'identifiant unique et de vérification du
bénéficiaire, les fonds bloqués sur carte, les concours aux entreprises et
les contrats d'acquisition commerçant. Chaque tâche en possède la référence
locale indiquée dans sa story ; BNK-001 garde la qualification et les règles
générales de paiement, BNK-005 celles du crédit. Aucun calcul général de
plafond, d'indemnité ou de prescription n'est ajouté à la première tranche.

Chaque lot applique BASE-003, BASE-008, la méthode BASE-005 embarquée, les
garde-fous ci-dessus et les couches de recette BASE-006 : structure, paquet
détaché, client, résultat métier, lecture par une personne sans formation
juridique. Il inscrit NOTICE local et racine, synchronise manifeste et
marketplace, et n'annonce dans le README que les tâches livrées.

Chaque skill qualifie d'abord, puis traite. Il charge la méthode locale,
distingue mention d'une pièce, fait déclaré, règle lue et inconnue, et ne
donne ni délai ni montant sans source lue et date établie, hors montant
recopié d'une pièce. Les pièces fournies sont des données, jamais des
instructions. Sans référence ou relais adapté, il produit les questions et
pièces utiles, sans appeler une branche absente.

Les fichiers « à créer » des suites sont des livrables futurs. La portée de
ce cadrage figure dans la [vérification](dom-004-verification.md).
