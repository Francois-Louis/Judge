# EXIST-006 — Découpage du contentieux

Propositions du **16 octobre 2026**, issues de l'[inventaire exhaustif](exist-006-inventaire-contentieux.md).
Les 28 suites CTX restent `proposee`. [La vérification](exist-006-verification.md)
est une relecture du cadrage sur documents fictifs, pas une recette de skills.

## Contrat commun et première tranche proposée

Chaque suite dépend d'EXIST-006, PILOTE-003, BASE-005 et BASE-006. Le bilan
PILOTE-003 est terminé après BASE-011 ; ce préalable est satisfait, sans
sélection d'une extension. Le nominal H01 complet et le lecteur indépendant
du pilote demeurent des limites documentées.

**Première tranche proposée : CTX-001**, lecture et orientation d'un document
entrant pour particulier/TPE sans profil professionnel. Elle donne auteur,
destinataire, demande, dates visibles, pièces manquantes et interlocuteur à
identifier. Elle ne tranche pas le fond, ne calcule pas un délai et ne lance
aucune autre tâche. Les autres tranches restent des choix distincts.

Une dépendance métier désigne un contrat d'entrée ; une fiche équivalente
fournie manuellement est admise, avec contrôle de ses manques. Ni exécution
préalable ni installation du plugin voisin ne sont requises. Les tranches
de gestion ne conditionnent pas une lecture ponctuelle en conversation.
Chaque tranche embarque et charge ses références locales, méthode BASE-005
1.0.0 et contrat de stockage BASE-008 ; elle corrige ses propres annonces,
gates et profils nécessaires, sans attendre une réécriture transversale.

## Stories et résultats

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [CTX-001](suites/ctx-001-orientation-document.md) | Fiche de lecture et orientation d'un document entrant | Aucune |
| [CTX-002](suites/ctx-002-mise-en-demeure-recue.md) | Fiche des demandes et pièces d'une mise en demeure civile/commerciale reçue | CTX-001 |
| [CTX-003](suites/ctx-003-preparer-demande-paiement.md) | Fiche de préparation d'une demande de paiement contractuelle B2B | Aucune |
| [CTX-004](suites/ctx-004-projet-mise-en-demeure.md) | Projet de mise en demeure de paiement B2B et checklist de notification | CTX-003 |
| [CTX-005](suites/ctx-005-demande-communication-pieces.md) | Qualification d'une demande de communication de pièces civile | CTX-001 |
| [CTX-006](suites/ctx-006-projet-communication-pieces.md) | Projet de bordereau de communication sur corpus expressément choisi | CTX-005, CTX-009 |
| [CTX-007](suites/ctx-007-plan-conservation.md) | Projet de plan de conservation de pièces pour un litige identifié | Aucune |
| [CTX-008](suites/ctx-008-reexamen-conservation.md) | Fiche de réexamen d'une mesure de conservation | CTX-007 |
| [CTX-009](suites/ctx-009-restrictions-communication.md) | Tableau interne des restrictions de communication par pièce | Aucune |
| [CTX-010](suites/ctx-010-entretien-factuel.md) | Trame d'entretien factuel privé sans témoignage rédigé | Aucune |
| [CTX-011](suites/ctx-011-chronologie-documentee.md) | Chronologie sur corpus déclaré avec citations et contradictions | Aucune |
| [CTX-012](suites/ctx-012-matrice-preuve-contractuelle.md) | Matrice de preuve d'une obligation contractuelle B2B contestée | Aucune |
| [CTX-013](suites/ctx-013-section-factuelle-conclusions.md) | Projet de section factuelle de conclusions TJ en procédure écrite | CTX-011 |
| [CTX-014](suites/ctx-014-ouverture-dossier.md) | Fiche d'ouverture de dossier et registre cohérents | Aucune |
| [CTX-015](suites/ctx-015-evenement-dossier.md) | Événement daté et attribué sans réécriture de l'historique | CTX-014 |
| [CTX-016](suites/ctx-016-fiche-echeance.md) | Fiche d'une échéance de procédure TJ écrite ou impossibilité motivée | Aucune |
| [CTX-017](suites/ctx-017-point-dossier.md) | Point daté sur un dossier, couverture et questions ouvertes | CTX-014 |
| [CTX-018](suites/ctx-018-etat-portefeuille.md) | État des seuls dossiers autorisés, sans total financier trompeur | CTX-014 |
| [CTX-019](suites/ctx-019-demande-etat-conseil.md) | Brouillon local de demande d'état à un conseil pour un dossier | CTX-014 |
| [CTX-020](suites/ctx-020-cloture-suivi.md) | Clôture administrative de suivi avec obligations restantes | CTX-014 |
| [CTX-021](suites/ctx-021-preferences-contentieux.md) | Préférences volontaires et modification ciblée | Aucune |
| [CTX-022](suites/ctx-022-espace-dossier.md) | Espace isolé sans collision ni lecture croisée implicite | Aucune |
| [CTX-023](suites/ctx-023-rapport-evenements.md) | Rapport local de nouveaux événements depuis un export fourni | CTX-015, CTX-016 |
| [CTX-024](suites/ctx-024-cookbook-export-local.md) | Dry-run du rapport sur export dans un déploiement jetable | CTX-023 |
| [CTX-025](suites/ctx-025-assignation-recue.md) | Lecture d'une assignation ou d'une convocation reçue par un particulier | CTX-001 |
| [CTX-026](suites/ctx-026-saisir-juge-petit-litige.md) | Préparation de la saisine du juge pour un petit litige civil | CTX-001 |
| [CTX-027](suites/ctx-027-audience-sans-avocat.md) | Préparation d'une audience civile orale sans avocat | CTX-001 |
| [CTX-028](suites/ctx-028-jugement-civil-recu.md) | Lecture d'un jugement civil reçu et des recours à vérifier | CTX-001 |

## Devenir des trois tâches sans équivalent automatique

| Entrée héritée | Tâche française définie avant renommage | Décision sur le nom et retrait |
|---|---|---|
| subpoena-triage | CTX-005 : lire une demande de communication en procédure civile identifiée ; auteur, partie/tiers, pièce, injonction éventuelle et réception sont nécessaires | Conserver le chemin technique tant que le routage n'est pas migré ; intitulé visible futur « Demande de communication de pièces ». Ne pas rendre subpoena synonyme de sommation/convocation ; branches CID/grand jury hors parcours français. |
| deposition-prep | CTX-010 : préparer des questions pour un entretien privé volontaire et noter l'origine des souvenirs ; aucune audition judiciaire ou pénale | Intitulé futur « Préparation d'un entretien factuel », chemin technique conservé provisoirement. Deposition, attestation, audition, comparution et interrogatoire ne sont pas interchangeables ; toute nouvelle tâche d'acte formel demande son propre cadrage. |
| privilege-log-review | CTX-009 : tableau interne des motifs possibles limitant une communication, avec source et décision à instruire | Intitulé futur « Restrictions de communication des pièces ». Retirer export automatique d'un privilege log et classifications US comme preuves de secret ; bordereau externe distinct CTX-006. |

Un renommage technique futur devra migrer descriptions, README, appels internes,
agent/cookbook, profils et recettes ; aucune commande française n'est créée
ici. Les parcours étrangers éventuels doivent être explicitement choisis et
qualifiés, jamais servir de défaut à un acte français.

## Quatre chaînes indépendantes et leurs contrats

Mise en demeure : CTX-002 lit l'entrant ; CTX-003 prépare la demande ; CTX-004
porte projet/signataire/destinataire et checklist de notification. Le montant
allégué, le montant justifié et le solde calculé restent distincts. Réclamation
sectorielle, proposition transactionnelle et acte d'exécution sont d'autres tâches.

Preuves : CTX-007 possède mesure/support/période/responsable/fondement/preuve
d'exécution ; CTX-008 ajoute réexamen et décision attribuée. CTX-009 possède
la restriction par pièce, auteur/qualité/destinataires/finalité, fondement
et incertitude. CTX-005 possède l'acte de demande ; CTX-006 consomme la revue
et porte le projet de bordereau, versions, numérotation et pièces exclues.
Aucune transmission, collecte de compte, suppression ou levée de restriction
n'est déduite de ces tableaux.

Écritures : CTX-011 possède les faits sourcés et contradictions, CTX-012
les conditions de l'obligation et preuve contraire, CTX-013 sa seule section
factuelle. La tâche exige juridiction, procédure écrite, stade, qualité des
parties et représentation qualifiés ; pas de modèle universel d'assignation,
requête, conclusions, attestation ou plaidoirie.

Suivi : CTX-014 possède identités et schéma dossier/log, CTX-015 l'événement
attribué, CTX-016 la fiche de délai, CTX-017/018 leurs synthèses, CTX-020 la
clôture administrative. CTX-022 possède espace/identifiant/actif, sans second
schéma concurrent ; CTX-021 préférences. CTX-023/024 ne produisent que rapports
sur entrées délimitées, pas un système de notification judiciaire français.

## Transpositions à retirer et recherches à effectuer

Ces lignes sont des exigences de recherche future, **pas des règles de droit
vérifiées dans ce cadrage**. Les sources précises et versions devront être lues
selon BASE-005/BASE-010 ; aucun abonnement ni fournisseur privé obligatoire.

| Point hérité et emplacement | Faits requis et recherche future | Résultat si faits/source absents |
|---|---|---|
| Work product et privilege : profil Outputs/Shared guardrails, modèles inline des 19 skills, agent et tracker-writer | Auteur et qualité à la date, mission, destinataires réels, objet, pièces jointes, pays/procédure ; règles professionnelles en vigueur, textes nationaux pertinents et droit UE seulement dans son champ | Restriction « à instruire », aucune protection par en-tête ni waiver automatique depuis une diffusion. Vérifier spécifiquement régime actuel des juristes d'entreprise, sans reprendre les généralisations héritées. |
| Discovery/disclosure : subpoena, chronology, claim-chart, privilege-log, legal-hold, log et watcher | Nature exacte de l'acte, autorité/parties/tiers, pièces, stade, mesures déjà ordonnées et restrictions d'usage ; Code de procédure civile, Code civil et texte spécial | Demande alléguée/ordonnée/à qualifier distincte ; ni collecte massive, sanctions US, log obligatoire ni calcul FRCP. Recherche spécifique si mesure d'instruction avant procès ; ne pas l'assimiler à discovery. |
| Without prejudice / FRE 408 / waiver : demand-intake, demand-draft, demand-received, profil Demand-letter practice et demand-letters/_README | Assertion de droits ou négociation, auteurs/mandats, contenu, droit applicable et destinataire ; Code civil, procédure, règles professionnelles et textes exacts de négociation/confidentialité | Mention citée comme fait, pas garantie de confidentialité, d'inadmissibilité ou d'absence d'aveu. Pas de traduction « sous toutes réserves » réputée équivalente. |
| Acte, compétence et représentation | Territoire, parties/qualités, objet/montant, juridiction/formation, stade, avocat/mandat, régime écrit/oral ; CPC, Code de l'organisation judiciaire, textes de compétence et dispositions spéciales | Qualification conditionnelle et pièces à demander ; aucun acte universel ni signature/représentation présumée. Un avocat confirmé ne prouve pas toutes les habilitations. |
| Notification et délai | Acte intégral, déclencheur juridique, preuve d'envoi/remise/signification, destinataire et mode, dates/fuseau/lieu, décision/calendrier, exceptions ; procédure et textes spéciaux applicables aux dates pertinentes | `a-determiner`, faits manquants et urgence de vérification ; ne pas substituer date d'émission, téléchargement ou inscription à la date du déclencheur. Distinguer délai réclamé, fixé au dossier, légal et jalon interne. |
| Conservation et données | Pièces/supports, finalité, accès, personnes, politique/obligation existante, autres dossiers ; textes de preuve et procédure, RGPD/droit national et règles sectorielles | Plan proportionné proposé avec manques, pas de suspension générale éternelle ni suppression à la clôture. Données personnelles ne deviennent pas librement transmissibles pour le seul motif du litige. |

Les textes et décisions sont à rechercher aux dates des faits et de l'acte,
avec versions/transitions, passage exact, lien, date réelle de consultation
et applicabilité motivée. Code civil et CPC ne couvrent pas à eux seuls
pénal, administratif, travail, exécution ou transfrontalier. Échec d'une voie
d'accès : tenter les voies officielles alternatives pertinentes et réserver
seulement la conclusion dépendante, sans demander de permission répétée.

## Frontières et relais autonomes

| Situation | Propriétaire et limite du contentieux |
|---|---|
| Convocation police/gendarmerie, enquête, poursuite pénale | DOM-002 police/pénal ; CTX-001 relève auteur, qualité déclarée, date et document, prépare questions au conseil/émetteur. Aucun refus de comparaître, entraînement deposition ou réponse subpoena conseillé. |
| Décision/convocation administrative, agent public ou domaine public spécialisé | DOM-010 administratif, DOM-037 emploi public ou secteur selon acte. Vérifier compétence et Code de justice administrative/textes spéciaux lors du lot concerné ; aucun délai civil plaqué sur recours administratif. |
| Saisie, commandement, expulsion ou exécution d'un titre | DOM-003 exécution, avec CPCE et régime précis à rechercher ; présence d'un commissaire de justice ne suffit pas à qualifier l'acte d'exécution. Bien-fondé de dette garde son secteur ; notification d'un acte civil peut rester contentieuse selon qualification. |
| Travail, consommation, bail, famille, santé, PI, responsabilité | Le domaine de fond conserve sa réclamation et ses conditions de droit ; litigation porte la tâche procédurale distincte si son régime est qualifié. Brevet français/UE/JUB/étranger demande cadrage PI et juridiction, pas tableau §102 traduit. |
| Arbitrage, mesure étrangère ou demande transfrontalière | Aucun tribunal/arbitrage traité par défaut. Rechercher compétence, droit applicable, instruments UE/internationaux de notification ou preuve pertinents et représentation ; bornage futur distinct si hors civil français retenu. |

Chaque relais reçoit une fiche manuelle autonome : demande exacte, auteur et
destinataire/qualités, procédure supposée et inconnues, pièces/pages lues,
dates visibles et preuves manquantes, question réservée. L'absence de plugin
adapté produit cette fiche et les prochaines questions ; aucun skill hérité
voisin n'est lancé et aucun délai supposé n'est fourni.
