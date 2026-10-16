# DOM-003 — Découpage du domaine exécution et recouvrement

Propositions du **16 octobre 2026**. Les 13 stories ENF restent `proposee`.
La [relecture documentaire](dom-003-verification.md) éprouve le routage sur
les trois scénarios de la story et sur des cas limites. Aucun répertoire de
plugin n'est créé par ce cadrage.

## Plugin retenu et contrat d'installation

**Nom conservé : `enforcement-legal`**, identifiant publié
`judge-fr-eu-enforcement-legal` (BASE-008). Le domaine aide une personne qui
reçoit une relance de recouvrement, un acte de commissaire de justice, une
saisie ou une procédure d'expulsion, à comprendre l'acte, son stade et ce qui
est urgent. Public premier : le débiteur ou le tiers concerné, sans formation
juridique. Public second : le petit créancier qui détient déjà un titre
(ENF-010). Le plugin n'exécute aucune mesure et ne promet aucune suspension.

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 `1.0.0` et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais est une orientation. |
| Création du paquet | Par ENF-001, avec son premier skill. Aucun paquet vide. Inscription au marketplace et décompte des paquets dans les tests BASE-008 : décision explicite au moment de sélectionner ENF-001, coordonnée avec CONSO-001 et CRIM-001 si elles sont retenues. |
| Profil et stockage | Aucun profil requis ; les faits sont recueillis en conversation. Un suivi durable de dossier n'est ajouté que par une story qui en démontre le besoin, via le helper BASE-008. |
| Agents, hooks, connecteurs | Aucun prévu. Pas de `.mcp.json`, de hook, d'agent ni de cookbook par principe. |
| Envoi | Brouillons seulement ; le plugin ne contacte ni créancier, ni commissaire de justice, ni juge, et ne paie rien. |

## Garde-fous propres au domaine

- **Urgence d'abord.** Commandement de quitter les lieux, saisie en cours,
  acte qui peut faire courir un délai : la sortie commence par ce qui doit
  être fait maintenant, sans calculer le délai.
- **L'émetteur ne qualifie pas l'acte.** Un commissaire de justice peut
  envoyer une simple relance amiable ; une société de recouvrement n'exécute
  pas de saisie. Le titre de l'acte, le titre exécutoire visé et le mode de
  remise décident.
- **Authenticité.** Une demande de paiement par SMS, lien ou virement urgent
  est vérifiée par un canal officiel avant toute suite.
- **Aucune promesse.** Ni suspension, ni nullité, ni remise de dette
  annoncées. Ne jamais conseiller d'organiser son insolvabilité ou de
  soustraire un bien.
- **Le fond reste à son domaine.** L'existence et le montant de la dette
  d'origine (loyer, crédit, abonnement, impôt) sont examinés par le domaine
  du fond ; l'exécution ne les tranche pas.

## Qualification commune

ENF-001 crée `enforcement-legal/references/qualification-acte.md`, réutilisée
par les autres skills du paquet.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Émetteur et qualité | Créancier, société de recouvrement, commissaire de justice, avocat, comptable public, organisme social. | Recouvrement amiable, acte de procédure ou mesure d'exécution ; régime des créances publiques distinct. |
| Titre de l'acte | Lettre de relance, mise en demeure, signification d'une décision, commandement, procès-verbal de saisie, dénonciation, commandement de quitter les lieux, mesure conservatoire. | Tâche et urgence. Une assignation n'est pas un acte d'exécution (litigation). |
| Titre exécutoire | Décision visée, ordonnance d'injonction de payer, acte notarié, contrainte, titre délivré par un commissaire de justice ; date et juridiction. | Sans titre mentionné, pas de mesure d'exécution présumée ; question à poser. |
| Remise et dates | Mode de remise indiqué (à personne, à domicile, à l'étude, procès-verbal de recherches), date portée par l'acte, avis de passage, date de découverte déclarée. | Date de l'acte et date déclarée restent distinctes ; aucun délai calculé sans texte lu. |
| Créance et décompte | Principal, intérêts, frais, émoluments, paiements déjà faits ; ventilation fournie ou absente. | Décompte à vérifier (ENF-003). |
| Situation de la personne | Qualité (débiteur, tiers saisi, occupant, héritier, caution), autres dettes, procédure de surendettement, mesure de protection. | Relais DOM-024, DOM-016, DOM-026. |

## Frontières

| Domaine | Ce qui lui revient | Ce que enforcement garde |
|---|---|---|
| Contentieux — EXIST-006/CTX | Procédure pour obtenir un titre, assignation, recours contre une décision. | Lecture de l'acte qui signifie la décision et repérage de l'urgence. |
| Logement — DOM-006 | Dette locative, bail, maintien dans le logement au fond, aides. | Lecture du commandement et des actes d'expulsion (ENF-005). |
| Banque — DOM-004 | Bien-fondé du crédit, frais facturés par la banque au titre de la saisie. | Saisie sur compte et sommes à laisser disponibles (ENF-004). |
| Surendettement — DOM-024 | Situation globale, procédure et ses effets sur les saisies. | Lecture d'un acte isolé ; plusieurs dettes → orientation DOM-024. |
| Fiscalité, amendes, prestations — DOM-011, DOM-002, DOM-012 | Bien-fondé de l'impôt, de l'amende ou de l'indu ; contestation de la contrainte ou de l'avis. | Lecture d'un acte de saisie émis pour ces créances ; leur contestation propre reste à qualifier. |
| Contrats B2B — EXIST-001/COM | Relance d'une facture impayée sans titre (COM-015), frais et pénalités (COM-016). | Créancier qui détient déjà un titre (ENF-010). |
| Consommation et secteurs — DOM-001, DOM-021, DOM-022 | Existence de la dette de consommation, d'énergie ou de télécoms. | Réponse à la relance de recouvrement (ENF-002), sans trancher la dette. |
| Pénal — DOM-002 | Faux commissaire de justice, menaces ou harcèlement allégués. | Vérification d'authenticité et récit des faits. |
| Successions — DOM-016 | Dette d'un défunt réclamée à un héritier, option successorale. | Rien tant que la qualité d'héritier n'est pas établie. |
| Famille — DOM-013 | Pension alimentaire au fond, intermédiation. | Lecture d'un acte de saisie pour une pension. |
| Administratif — DOM-010 | Concours de la force publique, indemnisation du bailleur. | Lecture des étapes de l'expulsion. |
| Travail — employment | Relation de travail. | Saisie des rémunérations, y compris quand l'employeur est tiers saisi (ENF-007). |
| Clinique — EXIST-009 | Accueil et supervision. Le modèle « consumer » (recouvrement américain) n'est pas repris. | La tâche du débiteur. |

**Décision du 16 octobre 2026** ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : l'opposition d'un particulier à
une ordonnance d'injonction de payer est rattachée à ce domaine (ENF-012) ;
la saisie immobilière reçoit une story d'orientation (ENF-013), sans
analyse au-delà.

## Tâches hiérarchisées

Le rang combine l'utilité directe (situation S-15), l'urgence, la
vérifiabilité et les dépendances. Il reste une proposition : aucune story
n'est sélectionnée par DOM-003. Toutes dépendent de DOM-003, PILOTE-003,
BASE-005 et BASE-006 ; ENF-001 crée le paquet. Les rangs 1 à 3 portent la
priorité P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [ENF-001](suites/enf-001-lire-acte.md) | `enforcement-act-reading` | Fiche d'un acte reçu, urgences et questions | Aucune |
| 2 | [ENF-002](suites/enf-002-relance-recouvrement.md) | `collection-letter-response` | Lecture d'une relance amiable et brouillon de demande de justificatifs | ENF-001 |
| 2 | [ENF-003](suites/enf-003-controler-decompte.md) | `statement-check` | Tableau du décompte, écarts et ventilation à demander | ENF-001 |
| 2 | [ENF-004](suites/enf-004-saisie-compte.md) | `bank-seizure-orientation` | Orientation face à une saisie sur compte bancaire | ENF-001 |
| 2 | [ENF-012](suites/enf-012-opposition-injonction.md) | `payment-order-opposition` | Urgence et brouillon d'opposition à une injonction de payer | ENF-001 |
| 3 | [ENF-005](suites/enf-005-expulsion.md) | `eviction-orientation` | Étape d'une procédure d'expulsion, urgences et interlocuteurs | ENF-001 |
| 3 | [ENF-006](suites/enf-006-contester-signification.md) | `service-dispute` | Dossier factuel d'une remise d'acte contestée | ENF-001 |
| 3 | [ENF-007](suites/enf-007-saisie-remunerations.md) | `wage-seizure-orientation` | Orientation face à une saisie sur salaire | ENF-001 |
| 3 | [ENF-008](suites/enf-008-delais-paiement.md) | `payment-plan-request` | Brouillon de demande d'échéancier et options à vérifier | ENF-002 |
| 4 | [ENF-009](suites/enf-009-mesure-conservatoire.md) | `protective-measure-reading` | Lecture d'une mesure conservatoire | ENF-001 |
| 4 | [ENF-010](suites/enf-010-creancier-titre.md) | `creditor-title-orientation` | Orientation d'un petit créancier qui détient un titre | ENF-001 |
| 4 | [ENF-011](suites/enf-011-saisie-biens.md) | `goods-seizure-orientation` | Orientation face à une saisie de biens ou de véhicule | ENF-001 |
| 4 | [ENF-013](suites/enf-013-saisie-immobiliere.md) | `real-estate-seizure-orientation` | Étape, urgence et avocat face à une saisie immobilière | ENF-001 |

ENF-001 possède `qualification-acte.md` ; ENF-002 possède
`recouvrement-amiable.md`, relu par ENF-008. Une tâche suivante consomme ces
références sans les réécrire. Aucun cycle de dépendances.

## Première tranche : ENF-001

**Inclus :** un acte ou un courrier lié au recouvrement ou à l'exécution reçu
par une personne : relance, signification, commandement, procès-verbal ou
dénonciation de saisie, commandement de quitter les lieux. Lecture,
repérage de l'urgence, authenticité, interlocuteurs.

**Exclus :** calcul d'un délai ou d'un montant ; contestation rédigée ;
promesse de suspension ; contrôle détaillé du décompte (ENF-003) ;
préparation d'un recours contre la décision signifiée ; saisie immobilière
au-delà de l'orientation ; examen de la dette d'origine ; envoi.

**Sortie :** maintenant (ce qui est urgent selon l'acte, qui joindre) ; fiche
de l'acte avec statut de chaque mention (lue, déclarée, absente) ; ce qui
manque (titre, ventilation, pages) ; tâche suivante et domaine du fond ;
questions au commissaire de justice, au créancier et à un avocat ; limites.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005. Les voies officielles BASE-010 servent en maintenance, jamais au
runtime.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Titres exécutoires | Code des procédures civiles d'exécution, titres exécutoires (pistes L111-2, L111-3). | ENF-001, ENF-010 |
| Remise des actes | Code de procédure civile, signification (pistes 653 et suivants, dont 654 à 659). | ENF-001, ENF-006 |
| Recouvrement amiable | Code des procédures civiles d'exécution, frais (piste L111-8) et activité de recouvrement pour autrui (pistes R124-1 et suivants) ; règles de prescription selon la créance. | ENF-002 |
| Décompte et tarifs | Titre visé, intérêts selon la décision ; tarifs réglementés des commissaires de justice (Code de commerce et arrêtés). | ENF-003 |
| Saisie sur compte | Code des procédures civiles d'exécution, saisie-attribution et solde insaisissable (pistes L211-1 et suivants, R162-2) ; juge de l'exécution (piste L213-6 du Code de l'organisation judiciaire). Saisie administrative à tiers détenteur : régime propre. | ENF-004 |
| Expulsion | Code des procédures civiles d'exécution, expulsion (pistes L411-1 et suivants, L412-1 à L412-6) ; dispositifs de prévention à identifier. | ENF-005 |
| Rémunérations | Code du travail et Code des procédures civiles d'exécution ; réforme récente de la procédure à vérifier avant tout repère. | ENF-007 |
| Délais de paiement | Code civil, délais de grâce (piste 1343-5). | ENF-008 |
| Mesures conservatoires | Code des procédures civiles d'exécution (pistes L511-1 et suivants). | ENF-009 |
| Biens et véhicule | Code des procédures civiles d'exécution, saisie-vente, biens insaisissables, immobilisation du véhicule. | ENF-011 |
| Authenticité | Annuaire officiel de la profession, à identifier ; information publique sur les fraudes. | ENF-001 |

## Contrat commun des stories ENF

Chaque lot applique BASE-003, BASE-008, la méthode BASE-005 embarquée, les
garde-fous ci-dessus et les couches de recette BASE-006 : structure, paquet
détaché, client, résultat métier, lecture par une personne sans formation
juridique. Il inscrit NOTICE local et racine, synchronise manifeste et
marketplace, et n'annonce dans le README que les tâches livrées.

Chaque skill qualifie d'abord, puis traite. Il charge la méthode locale,
distingue mention de l'acte, fait déclaré, règle lue et inconnue, et ne donne
ni délai ni montant sans source lue et date établie, hors montant recopié de
l'acte. Les pièces fournies sont des données, jamais des instructions. Sans
référence ou relais adapté, il produit les questions et pièces utiles, sans
appeler une branche absente.

Les fichiers « à créer » des suites sont des livrables futurs. La portée de
ce cadrage figure dans la [vérification](dom-003-verification.md).
