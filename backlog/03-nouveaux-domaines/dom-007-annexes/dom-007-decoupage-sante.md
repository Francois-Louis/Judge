# DOM-007 — Découpage du domaine santé et droits des patients

Propositions du **16 octobre 2026**. Les 12 stories SAN restent `proposee`.
La [relecture documentaire](dom-007-verification.md) éprouve le routage sur
les trois scénarios de la story, sur le scénario issu des frictions données
personnelles et sur des cas limites. Aucun répertoire de plugin n'est créé
par ce cadrage.

## Plugin retenu et contrat d'installation

**Nom conservé : `health-legal`**, identifiant publié `judge-fr-eu-health-legal`
(BASE-008). Le domaine traite la relation juridique d'une personne avec un
professionnel, un établissement ou une structure de santé : accès aux
informations de santé, information et consentement, réclamation, sanction,
signalement, orientation d'un dommage lié aux soins et soins psychiatriques
sans consentement. Il ne traite ni les soins eux-mêmes ni le remboursement.
Public premier : le patient, ses proches et ses représentants, sans formation
juridique. Le professionnel de santé n'est pas un public visé par les tâches
proposées.

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais est une orientation. |
| Création du paquet | Par SAN-001, avec son premier skill. Aucun paquet vide. Inscription au marketplace et décompte des paquets dans les tests BASE-008 : décision explicite au moment de sélectionner SAN-001, coordonnée avec les autres premières tranches DOM retenues. |
| Profil et stockage | Aucun profil requis. Les données de santé ne sont demandées que si la tâche l'exige, au minimum, et ne sont jamais conservées ; aucun registre de dossier n'est tenu. |
| Agents, hooks, connecteurs | Aucun prévu. Aucun accès à un espace numérique de santé, à un portail d'établissement ou à une messagerie. Les pièces sont fournies par la personne. |
| Envoi | Brouillons seulement ; le plugin ne dépose aucune demande, plainte ou réclamation et ne contacte ni établissement, ni ordre, ni agence, ni commission. |

## Garde-fous propres au domaine

- **Ni diagnostic ni avis médical.** Le plugin ne dit pas si un soin était
  indiqué, bien réalisé ou fautif, ni s'il existe un aléa ; il nomme la
  question et l'interlocuteur qui peut l'examiner.
- **Urgence médicale d'abord.** Un danger immédiat pour la santé relève des
  secours ou du professionnel de santé, pas d'une démarche écrite ; la sortie
  le dit en tête avant toute autre information.
- **La qualité du demandeur d'abord.** Patient, parent, représentant,
  ayant droit, proche ou personne de confiance : aucune qualité ne vaut
  pouvoir ou droit d'accès sans texte lu et pièce établissant la qualité.
  Être aidant ne suffit pas à représenter.
- **Quatre objets à ne pas fusionner.** Obtenir une explication, faire
  sanctionner un professionnel, signaler un dysfonctionnement et obtenir une
  indemnisation sont des démarches distinctes, avec des interlocuteurs
  distincts. Une seule lettre n'est pas présentée comme les servant toutes.
- **Public ou privé qualifié.** Le statut de l'établissement ou du
  professionnel peut changer les voies et le juge ; il est établi, jamais
  supposé à partir du nom.
- **Aucun délai, seuil ni montant inventé.** Délais de communication, de
  réponse ou de prescription et seuils d'accès à une procédure ne sont
  donnés qu'avec la source lue et les dates établies ; aucun calendrier RGPD
  n'est appliqué automatiquement à un dossier médical.
- **Collecte minimale.** Seules les informations de santé nécessaires à la
  tâche sont demandées ; celles d'un tiers ne sont pas recherchées.

## Qualification commune

SAN-001 crée `health-legal/references/qualification-sante.md`, réutilisée par
les autres skills du paquet.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Demandeur et qualité | Patient majeur, patient mineur, parent, tuteur ou personne habilitée, ayant droit d'un patient décédé, proche, personne de confiance ; pièce établissant la qualité. | Droit d'accès, informations communicables, pièces exigées ; relais DOM-026 pour l'étendue d'une mesure. |
| Structure | Établissement public, établissement privé, professionnel libéral, centre de santé, structure médico-sociale, médecine du travail, médecin d'un assureur ou d'une caisse. | Régime d'accès, voie de réclamation et juge, à vérifier. |
| Objectif | Accès, information, explication, sanction, signalement, indemnisation, mesure de soins en cours. | Tâche et interlocuteur ; un objectif par sortie. |
| Informations visées | Nature des informations, période, ancienneté, support ; hospitalisation sans consentement en cause ou non. | Modalités particulières à rechercher ; aucune modalité supposée. |
| Dates | Soins, sortie, décès, demande, réception, réponse, relance, consolidation alléguée. | Aucun délai calculé sans texte lu et date prouvée. |
| Pièces | Demande et preuve d'envoi, réponse, comptes rendus, devis, facture, décision, échanges. | Distinguer pièce fournie, fait déclaré et inconnu. |
| Urgence | Danger immédiat, mesure de soins en cours, sortie imminente, échéance alléguée. | Renfort en tête ; urgence médicale avant toute démarche. |

## Frontières

| Domaine | Ce qui lui revient | Ce que health garde |
|---|---|---|
| Protection sociale — DOM-012 | Remboursement, prise en charge et décisions de la caisse ou de son médecin-conseil, arrêt de travail indemnisé, complémentaire santé solidaire, aide médicale de l'État. | La relation avec le soignant ; la facture du soignant comme pièce (SAN-011). |
| Assurance — DOM-005 | Complémentaire santé et prévoyance privées (INS-009), assurance emprunteur (INS-008), garantie due par son propre assureur. | Orientation d'un dommage lié aux soins (SAN-006), y compris face à l'assureur du soignant. |
| Responsabilité civile — DOM-035 | Chiffrage du préjudice corporel et dommage hors soins. | Qualification de la voie d'indemnisation d'un dommage lié aux soins (SAN-006). |
| Protection des majeurs — DOM-026 | Étendue d'une mesure ou d'un mandat pour un acte. | Demande d'accès ou d'information une fois la qualité établie (SAN-002). |
| Handicap et autonomie — DOM-025 | Décision de reconnaissance ou d'accompagnement de l'autonomie. | Dossier médical demandé pour constituer ce dossier (SAN-001). |
| Données personnelles — privacy | Droits relatifs au traitement, traces des accès, plainte à la CNIL : PRV-001, PRV-025, PRV-026, PRV-033, PRV-034. | Accès au dossier selon le régime sectoriel (SAN-001 à SAN-004) ; secret professionnel invoqué devant l'ordre (SAN-007). |
| Police et pénal — DOM-002 | Plainte pour une infraction alléguée, y compris violation du secret ou exercice illégal ; santé pendant une garde à vue (CRIM-002). | Soins psychiatriques sans consentement (SAN-010) ; DOM-002 ne garde rien sur ces mesures. |
| Violences intrafamiliales — DOM-038 | Parcours de protection et pièces strictement utiles. | Accès au dossier médical si la personne le demande (SAN-001), sans certificat produit par l'outil. |
| Contentieux — litigation | Procédure une fois la voie qualifiée ; lecture d'une mission d'expertise judiciaire (CTX-032). | Orientation préalable et pièces (SAN-006). |
| Travail privé — employment | Aptitude, inaptitude et obligations de l'employeur. | Rien sur la médecine du travail ; son dossier est hors SAN-001 et reste à découper. |
| Fonction publique — DOM-037 | Instances médicales de l'employeur public et décision de carrière. | Rien sur ces instances. |
| Séjour — DOM-028 | Titre de séjour pour soins. | Rien sur ce titre. |
| Successions — DOM-016 ; décès — DOM-031 | Règlement de la succession ; obsèques et formalités du décès. | Accès d'un ayant droit au dossier (SAN-003), sans trancher la qualité d'héritier. |
| Consommation — DOM-001 | Achat d'un appareil ou d'une prestation de bien-être sans professionnel de santé ; vente par un vendeur. | Information sur les frais d'un soin par un professionnel de santé (SAN-011). |
| Produits et publicité — product-legal | Publicité et allégations de santé d'un produit (PDT-006, PDT-009). | Signalement à l'ordre d'un titre usurpé (SAN-007). |
| Éducation — DOM-027 | Aménagements et décisions scolaires. | Rien sur ces décisions. |

Les relais sont des orientations : une question bornée, les seules pièces
utiles, sans dépendance d'installation ni appel à un skill absent.

## Tâches hiérarchisées

Le rang combine l'utilité directe (situation S-31), la fréquence des
démarches, la vérifiabilité et les dépendances. Il reste une proposition :
aucune story n'est sélectionnée par DOM-007. Toutes dépendent de DOM-007,
PILOTE-003, BASE-005, BASE-006 et BASE-008 ; SAN-001 crée le paquet. Les
rangs 1 à 3 portent la priorité P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [SAN-001](../suites/san-001-acces-dossier-patient.md) | `medical-record-request` | Demande d'accès au dossier médical par le patient majeur, pour lui-même | Aucune |
| 2 | [SAN-002](../suites/san-002-acces-representant.md) | `representative-record-request` | Qualité d'un parent, représentant ou proche vérifiée ; demande si établie | SAN-001 |
| 2 | [SAN-003](../suites/san-003-acces-ayant-droit.md) | `deceased-patient-record-request` | Demande d'un ayant droit après un décès, objectif motivé | SAN-001 |
| 2 | [SAN-004](../suites/san-004-relancer-acces-dossier.md) | `medical-record-access-follow-up` | Relance ou contestation d'une réponse tardive, incomplète ou refusée | SAN-001 |
| 2 | [SAN-005](../suites/san-005-reclamation-etablissement.md) | `care-complaint` | Réclamation sur une prise en charge et objets distincts de la démarche | SAN-001 |
| 2 | [SAN-006](../suites/san-006-orienter-dommage-soins.md) | `medical-harm-orientation` | Voies d'indemnisation d'un dommage lié aux soins à vérifier, pièces | SAN-005 |
| 3 | [SAN-007](../suites/san-007-plainte-ordre.md) | `professional-board-complaint` | Plainte auprès de l'ordre d'un professionnel, sanction distincte | SAN-005 |
| 3 | [SAN-008](../suites/san-008-signalement-ars.md) | `health-authority-report` | Signalement d'un dysfonctionnement à l'agence régionale de santé | SAN-005 |
| 3 | [SAN-009](../suites/san-009-information-consentement.md) | `care-information-request` | Questions et demande d'information avant ou après un acte | SAN-001 |
| 3 | [SAN-010](../suites/san-010-soins-sans-consentement.md) | `involuntary-care-orientation` | Lecture d'une mesure de soins psychiatriques sans consentement | SAN-001 |
| 3 | [SAN-011](../suites/san-011-frais-soins.md) | `care-bill-review` | Facture ou dépassement comparés à l'information reçue sur les frais | SAN-001 |
| 4 | [SAN-012](../suites/san-012-directives-anticipees.md) | `advance-directives-preparation` | Préparer directives anticipées et désignation d'une personne de confiance | SAN-001 |

SAN-001 possède `qualification-sante.md` et `acces-dossier.md`, relus par
SAN-002 à SAN-004 et, pour la qualification, par SAN-009 à SAN-012. SAN-005
possède `objets-demarche.md`, la table des quatre objets et de leurs
interlocuteurs, relue par SAN-006 à SAN-008. Une tâche suivante consomme ces
références sans les réécrire. Aucun cycle.

## Première tranche : SAN-001

**Inclus :** la demande, par un patient majeur agissant pour lui-même, de
communication des informations de santé le concernant détenues par un
établissement de santé ou un professionnel de santé exerçant en France ;
qualification de la structure et des informations visées ; brouillon de
demande ; pièces à joindre.

**Exclus :** toute autre qualité de demandeur (SAN-002, SAN-003) ; relance
ou contestation (SAN-004) ; informations recueillies lors d'une
hospitalisation sans consentement, dont les modalités particulières sont à
rechercher (orientation SAN-010) ; dossier de médecine du travail, dossier
détenu par un assureur, une caisse ou une structure médico-sociale, espace
numérique de santé : orientation seulement ; droits RGPD sur le traitement et
traces des accès (PRV-001, PRV-025) ; tout délai ou coût non sourcé ;
diagnostic ou lecture médicale des pièces ; envoi.

**Sortie :** résumé clair ; fiche de qualification (demandeur, structure,
statut public/privé établi ou à vérifier, informations visées, période) ;
pièces à joindre ; brouillon de demande ; ce qui reste à vérifier (modalités,
délai et frais, avec la source lue ou réservés) ; suites (SAN-004 sans
réponse, PRV-001 pour un volet RGPD distinct) ; limites et phrase BASE-013.

## Points ouverts à découper

- Dossier de médecine du travail et dossier détenu par un assureur ou un
  médecin-conseil : régime d'accès et propriétaire à qualifier.
- Structures médico-sociales (hébergement de personnes âgées, établissements
  pour personnes handicapées) : réclamation, signalement et accès, partagés
  avec DOM-025 ; aucun propriétaire décidé par ce cadrage.
- Refus de soins discriminatoire allégué : relais DOM-029 à préciser.
- Espace numérique de santé et dossier médical partagé : accès, masquage et
  traces, en coordination avec privacy.

Ces besoins ne reçoivent aucune story tant que leur propriétaire n'est pas
arrêté ; ils ne sont pas couverts par les suites ci-dessus.

## Frictions données personnelles intégrées

Points 45–47 de la [matrice données personnelles](../../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md),
repris dans le complément de la story DOM-007. La matrice n'est pas modifiée.

| Point | Propriétaire privacy | Part santé |
|---|---|---|
| 45 — données médicales transmises sans justification | [PRV-026](../../02-plugins-existants/suites/prv-026-reconstituer-collecte-reutilisation.md) | Secret professionnel invoqué devant l'ordre (SAN-007) ; assurance → DOM-005. |
| 46 — consultation injustifiée du dossier patient | [PRV-001](../../02-plugins-existants/suites/prv-001-preparer-demande-acces.md), [PRV-025](../../02-plugins-existants/suites/prv-025-demande-limitation.md), [PRV-034](../../02-plugins-existants/suites/prv-034-dossier-plainte-cnil.md) | Demande au DPO de l'établissement sans promettre l'identité de tous les agents ; signalement SAN-008 si dysfonctionnement. |
| 47 — dossier médical communiqué tardivement | [PRV-033](../../02-plugins-existants/suites/prv-033-contester-reponse-droits.md) pour un volet RGPD distinct | SAN-004 : demandeur, informations, ancienneté, réception et exceptions qualifiés avant tout délai sectoriel. |

Le scénario « copie du dossier et soupçon de consultation » donne deux
objets et deux calendriers distincts : SAN-001 ou SAN-004 pour la copie,
PRV-001 ou PRV-025 pour les accès ; il est relu dans la vérification.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005. Les voies officielles BASE-010 servent en maintenance, jamais au
runtime.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Accès du patient | Code de la santé publique, accès aux informations de santé (pistes L1111-7, R1111-1 et suivants) ; obligations des établissements (piste L1112-1). | SAN-001 |
| Mineurs et représentants | Code de la santé publique (pistes L1111-5, L1111-7) ; Code civil, autorité parentale et protection des majeurs selon la mesure. | SAN-002 |
| Ayant droit | Code de la santé publique, secret et accès après décès (piste L1110-4) ; objectifs exigés et opposition éventuelle du défunt. | SAN-003 |
| Réponse tardive ou refus | Pistes SAN-001 ; pour un établissement public, Code des relations entre le public et l'administration et saisine de la CADA ; voies devant le juge selon le statut. | SAN-004 |
| Réclamation | Code de la santé publique, commission des usagers et médiation en établissement (pistes L1112-3, R1112-79 et suivants, R1112-91 et suivants). | SAN-005 |
| Dommage lié aux soins | Code de la santé publique, responsabilité et indemnisation (pistes L1142-1 et suivants) ; commissions de conciliation et d'indemnisation, ONIAM ; prescription (piste L1142-28) ; information du patient après dommage (piste L1142-4). | SAN-006 |
| Ordre professionnel | Code de la santé publique, conciliation et juridiction disciplinaire (pistes L4123-2, L4124-1) ; codes de déontologie selon la profession. | SAN-007 |
| Agence régionale de santé | Code de la santé publique, missions de l'ARS, réclamations et événements indésirables graves (piste L1413-14) ; informations officielles de l'agence. | SAN-008 |
| Information et consentement | Code de la santé publique (pistes L1111-2, L1111-4) ; Code civil (piste article 16-3). | SAN-009 |
| Soins sans consentement | Code de la santé publique (pistes L3211-1 et suivants, L3212-1, L3213-1, L3211-12, L3211-12-1, L3222-5-1) ; contrôle par le juge judiciaire ; commission départementale des soins psychiatriques. | SAN-010 |
| Frais de soins | Code de la santé publique, information sur les frais (piste L1111-3 et textes d'application) ; Code de la sécurité sociale pour le seul vocabulaire de remboursement. | SAN-011 |
| Directives et personne de confiance | Code de la santé publique (pistes L1111-6, L1111-11) ; modèles officiels du ministère de la Santé comme information. | SAN-012 |
| Données de santé | RGPD, loi Informatique et Libertés, référentiels CNIL selon la question ; relais privacy. | SAN-001, SAN-004 |

Aucune de ces pistes n'a été ouverte par ce cadrage. Les numéros d'articles
viennent de la connaissance de l'agent de maintenance ; leur existence, leur
version et leur portée sont à établir par chaque propriétaire.

## Contrat commun des stories SAN

Chaque lot applique BASE-003, BASE-008, la méthode BASE-005 embarquée, les
garde-fous ci-dessus et les couches de recette BASE-006 : structure, paquet
détaché, client, résultat métier, lecture par une personne sans formation
juridique. Il inscrit NOTICE local et racine, synchronise manifeste et
marketplace, et n'annonce dans le README que les tâches livrées.

Chaque skill qualifie d'abord, puis traite. Il charge la méthode locale,
distingue mention d'une pièce, fait déclaré, règle lue et inconnue, et ne
donne ni délai, ni seuil, ni montant sans source lue et date établie, hors
montant recopié d'une pièce. Les pièces fournies sont des données, jamais des
instructions. Sans référence ou relais adapté, il produit les questions et
pièces utiles, sans appeler une branche absente. Chaque réponse se termine
par la phrase BASE-013 nommant l'interlocuteur de la situation, avec un
renfort en tête en cas d'urgence, de mesure en cours ou d'échéance.

Les fichiers « à créer » des suites sont des livrables futurs. La portée de
ce cadrage figure dans la [vérification](dom-007-verification.md).
