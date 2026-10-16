# DOM-005 — Découpage du domaine assurance

Propositions du **16 octobre 2026**. Les 11 stories INS restent `proposee`.
La [relecture documentaire](dom-005-verification.md) éprouve le routage sur
les trois scénarios de la story et sur des cas limites. Aucun répertoire de
plugin n'est créé par ce cadrage.

## Plugin retenu et contrat d'installation

**Nom conservé : `insurance-legal`**, identifiant publié
`judge-fr-eu-insurance-legal` (BASE-008). Le domaine traite la relation d'une
personne avec son assureur, sa mutuelle ou son institution de prévoyance :
garantie, déclaration, refus, chiffrage, résiliation. Public premier : le
particulier assuré, bénéficiaire ou tiers victime, sans formation juridique.
Public second : l'artisan ou la TPE pour ses contrats professionnels.

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 `1.0.0` et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais est une orientation. |
| Création du paquet | Par INS-001, avec son premier skill. Aucun paquet vide. Inscription au marketplace et décompte des paquets dans les tests BASE-008 : décision explicite au moment de sélectionner INS-001, coordonnée avec les autres premières tranches DOM retenues. |
| Profil et stockage | Aucun profil requis. Les données de santé d'un questionnaire ou d'un dossier médical ne sont demandées que si la tâche l'exige, et jamais conservées. |
| Agents, hooks, connecteurs | Aucun prévu ; aucun accès à un espace client. Les pièces sont fournies par la personne. |
| Envoi | Brouillons seulement ; le plugin ne déclare aucun sinistre et ne contacte ni assureur, ni expert, ni médiateur. |

## Garde-fous propres au domaine

- **Quatre motifs à ne pas confondre.** Absence de garantie, exclusion,
  déchéance et nullité ont des conditions et des effets différents ; la
  sortie nomme la catégorie invoquée par l'assureur, puis ce qui reste à
  vérifier, sans conclure.
- **Le contrat applicable d'abord.** Conditions générales datées, conditions
  particulières et avenants en vigueur à la date du sinistre ; une pièce
  manquante est demandée, jamais supposée.
- **Garantie et responsabilité séparées.** La garantie due par l'assureur et
  la responsabilité de l'auteur du dommage sont deux questions et deux
  interlocuteurs.
- **Aucun chiffrage refait.** Indemnité, vétusté, franchise et plafond sont
  recopiés des pièces ; aucune somme n'est recalculée sans clause et source
  lues.
- **Aucune fausse déclaration.** Le plugin n'aide ni à embellir un sinistre
  ni à dissimuler un fait au questionnaire de souscription.

## Qualification commune

INS-001 crée `insurance-legal/references/qualification-assurance.md`,
réutilisée par les autres skills du paquet.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Parties | Souscripteur, assuré, bénéficiaire, tiers victime, intermédiaire (agent, courtier) ; particulier ou professionnel. | Droits et interlocuteur ; le tiers victime agit contre l'assureur du responsable selon un régime à vérifier. |
| Organisme et régime | Entreprise d'assurance, mutuelle, institution de prévoyance. | Code des assurances, Code de la mutualité ou Code de la sécurité sociale : règles différentes. |
| Contrat | Conditions générales (version), conditions particulières, avenants, attestation ; contrat individuel ou collectif. | Clause applicable à la date du sinistre. |
| Risque | Habitation, auto, appareil, voyage, animal, emprunteur, santé, prévoyance, construction, vie, protection juridique, professionnel. | Régimes isolés : emprunteur (INS-008), santé et prévoyance (INS-009), construction (INS-010), vie et décès (INS-011). |
| Dates | Souscription, sinistre, déclaration, réponse, refus, échéance. | Aucun délai de déclaration ni de prescription calculé sans texte lu. |
| Motif invoqué | Texte exact du courrier de refus et clause citée. | Absence de garantie, exclusion, déchéance, nullité ou autre, à vérifier. |

## Frontières

| Domaine | Ce qui lui revient | Ce que insurance garde |
|---|---|---|
| Travaux — DOM-015 | Responsabilité de l'entreprise, malfaçons, réception. | Garantie due par l'assureur, y compris dommages-ouvrage (INS-010). |
| Véhicules — DOM-023 | Achat, réparation, facture du garage. | Garantie auto et chiffrage du sinistre. |
| Santé — DOM-007 | Soins et responsabilité du soignant. | Complémentaire santé et prévoyance privées (INS-009). |
| Protection sociale — DOM-012 | Prestations de l'assurance maladie et des caisses. | Rien sur ces prestations. |
| Responsabilité — DOM-035 | Responsabilité de l'auteur, chiffrage du préjudice corporel. | Garantie de responsabilité civile de l'assuré et position de son assureur. |
| Banque — DOM-004 | Crédit et ses échéances. | Assurance emprunteur (INS-008). |
| Consommation — DOM-001 | Garantie commerciale du vendeur ou du fabricant. | Assurance vendue avec un bien (casse, vol, panne), dès que le garant est un assureur. |
| Voyages — DOM-008 | Obligations du transporteur et du vendeur de voyage. | Assurance voyage ou annulation. |
| Successions — DOM-016 | Règlement de la succession. | Versement d'une assurance-vie ou d'un capital décès au bénéficiaire (INS-011). |
| Funéraire — DOM-031 | Prestations funéraires. | Contrat obsèques comme contrat d'assurance. |
| Copropriété — DOM-018 | Décision et assurance de l'immeuble votées en assemblée. | Contrat de l'assuré copropriétaire ou occupant. |
| Travail — employment | Obligations de l'employeur sur la couverture collective. | Garantie due par l'organisme du contrat collectif. |
| Banque, placements — BNK-011 | Orientation des placements. | Assurance-vie comme contrat, sans conseil de placement. |
| Pénal — DOM-002 | Plainte pour vol ou fraude. | Récépissé de plainte comme pièce du sinistre. |

**Décision du 16 octobre 2026** ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : l'offre d'indemnisation faite par
un assureur à une victime d'accident de la circulation relève de la
responsabilité civile (DOM-035) ; insurance garde la garantie due à son
propre assuré.

## Tâches hiérarchisées

Le rang combine l'utilité directe (situation S-10), la fréquence des
démarches, la vérifiabilité et les dépendances. Il reste une proposition :
aucune story n'est sélectionnée par DOM-005. Toutes dépendent de DOM-005,
PILOTE-003, BASE-005 et BASE-006 ; INS-001 crée le paquet. Les rangs 1 à 3
portent la priorité P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [INS-001](suites/ins-001-refus-garantie.md) | `claim-denial-review` | Analyse d'un refus : motif, clause, pièces et demande d'explication | Aucune |
| 2 | [INS-002](suites/ins-002-declarer-sinistre.md) | `claim-declaration` | Déclaration de sinistre et pièces à réunir | INS-001 |
| 2 | [INS-003](suites/ins-003-contester-expertise.md) | `expert-assessment-dispute` | Comparaison rapport, devis et contrat ; options à vérifier | INS-001 |
| 2 | [INS-004](suites/ins-004-lire-garantie.md) | `coverage-review` | Lecture d'une garantie pour un événement donné | INS-001 |
| 2 | [INS-005](suites/ins-005-mediation-assurance.md) | `insurance-mediation` | Escalade : service réclamations, puis médiateur | INS-001 |
| 3 | [INS-006](suites/ins-006-resilier-contrat.md) | `policy-termination` | Résiliation par l'assuré ou lecture d'une résiliation par l'assureur | INS-001 |
| 3 | [INS-007](suites/ins-007-protection-juridique.md) | `legal-expenses-cover` | Mobiliser une garantie protection juridique | INS-004 |
| 3 | [INS-008](suites/ins-008-assurance-emprunteur.md) | `borrower-insurance` | Prise en charge ou changement d'assurance emprunteur | INS-001 |
| 3 | [INS-009](suites/ins-009-complementaire-sante.md) | `health-cover-claim` | Refus d'une complémentaire santé ou d'une prévoyance | INS-001 |
| 4 | [INS-010](suites/ins-010-dommages-ouvrage.md) | `construction-insurance-claim` | Déclaration et suivi d'une assurance dommages-ouvrage | INS-001 |
| 4 | [INS-011](suites/ins-011-assurance-vie-beneficiaire.md) | `life-insurance-beneficiary` | Démarches d'un bénéficiaire d'assurance-vie ou de capital décès | INS-001 |

INS-001 possède `qualification-assurance.md` et `motifs-refus.md`, relus par
INS-008 à INS-011 ; INS-004 possède `lecture-garantie.md`, relu par INS-007.
Une tâche suivante consomme ces références sans les réécrire. Aucun cycle.

## Première tranche : INS-001

**Inclus :** le refus, total ou partiel, opposé à un particulier sur un
contrat individuel relevant du Code des assurances (habitation, auto
dommages, appareil, voyage, animal, responsabilité civile), à partir du
courrier de refus et du contrat.

**Exclus :** régimes isolés (emprunteur, santé et prévoyance, construction,
vie et décès) au-delà de l'orientation ; contrat professionnel au-delà de la
qualification ; calcul de l'indemnité ; délai de prescription ;
responsabilité de l'auteur du dommage ; procédure ; envoi.

**Sortie :** résumé clair ; fiche du refus (motif cité, clause, catégorie
invoquée, version du contrat) ; ce qu'il faut vérifier pour cette catégorie ;
pièces manquantes, en premier lieu les conditions particulières ; brouillon
de demande d'explication ou de réexamen ; suites (médiation INS-005) ;
limites.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005. Les voies officielles BASE-010 servent en maintenance, jamais au
runtime.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Motifs de refus | Code des assurances, exclusions, déchéance, nullité et réduction (pistes L112-4, L113-1, L113-2, L113-8, L113-9). | INS-001 |
| Déclaration | Code des assurances, obligations de l'assuré après sinistre (piste L113-2) ; délais propres au risque. | INS-002 |
| Expertise et indemnité | Clauses du contrat ; principe indemnitaire (piste L121-1) ; pratiques d'expertise contradictoire comme information. | INS-003 |
| Prescription | Code des assurances (pistes L114-1, L114-2), à lire avant toute mention. | INS-001, INS-005 |
| Médiation | Médiation de l'assurance ; Code de la consommation, médiation ; ACPR et ABE Infoservice comme information. | INS-005 |
| Résiliation | Code des assurances, résiliation et information sur l'échéance (pistes L113-3, L113-12, L113-15-1, L113-15-2). | INS-006 |
| Protection juridique | Code des assurances (pistes L127-1 et suivants). | INS-007 |
| Emprunteur | Code des assurances et Code de la consommation, assurance emprunteur et changement de contrat ; convention AERAS comme information. | INS-008 |
| Santé, prévoyance | Code de la mutualité et Code de la sécurité sociale (institutions de prévoyance) ; contrats responsables. | INS-009 |
| Construction | Code des assurances, assurance dommages-ouvrage (piste L242-1). | INS-010 |
| Vie et décès | Code des assurances, assurance sur la vie (pistes L132-1 et suivants) ; dispositifs de recherche des bénéficiaires. | INS-011 |
| Distribution | Directive (UE) 2016/97 ; devoir de conseil, selon le grief. | INS-001, INS-004 |

## Contrat commun des stories INS

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
ce cadrage figure dans la [vérification](dom-005-verification.md).
