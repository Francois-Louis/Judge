# DOM-033 — Découpage animaux et responsabilités

Cadrage du **17 octobre 2026 (Europe/Paris)** pour la situation S-35 des
[usages quotidiens](../../usages-quotidiens.md). Les sept suites ANM restent
`proposee` : les noms et chemins ci-dessous désignent des livrables futurs.

## Domaine et contrat de paquetage

Nom retenu pour la cible : `animal-legal`, identifiant publié
`judge-fr-eu-animal-legal`. Le domaine porte les engagements liés à l'acquisition,
à la détention et à la garde d'un animal identifié. Une tâche a un seul
propriétaire ; le statut professionnel d'un éleveur ne transfère pas toute
vente à l'acquéreur vers le droit de l'exploitation agricole.

| Élément | Décision pour la future première tranche |
|---|---|
| Création | ANM-001 crée un paquet avec un seul skill utile ; aucun répertoire ni manifeste créé dans DOM-033. |
| Références | Questionnaire commun `references/qualification-animal.md` et référence propre à chaque tâche, dans le paquet. Aucun corpus du domaine dans le plugin généraliste, le hub ou l'index d'orientation. |
| Méthode | Copie identique de la méthode BASE-005 alors courante dans `references/shared/research-citation-method.md`, chargée par les skills ; version et empreinte consignées. |
| Isolation | Copies BASE-008 du contrat de stockage, du script et des modèles, LICENSE et NOTICE ; identifiant propre. Aucun profil préalable ni conservation durable des pièces par défaut. |
| Dépendances | Aucun autre plugin, abonnement PISTE, compte I-CAD ou connecteur indispensable. Une orientation n'est pas une dépendance d'installation. |
| Extensions | Aucun agent, hook ou connecteur identifié comme nécessaire. Les sources officielles peuvent être recherchées avec les outils disponibles ; sans lecture, seule la conclusion dépendante est réservée. |
| Validation | BASE-006 sur l'artefact détaché, schéma officiel, installation et exécution réelles rapportés séparément ; relecture datée des références selon BASE-014 avant lot. |
| Actions | Explication, dossier et brouillon à relire ; aucune signature, déclaration, modification de détenteur, prise de contact, remise d'animal ou paiement. |

## Entrer par le problème et qualifier progressivement

Reprendre le récit ou le document déjà fourni. Poser une ou deux questions
déterminantes à la fois, selon USAGE-001 `1.0.0`, sans demander le nom d'un code.
« Il manque les papiers », « la pension me demande un supplément » et
« le chien a blessé quelqu'un chez son gardien » sont des entrées suffisantes.

| Axe | Informations utiles | Effet sur la tâche |
|---|---|---|
| Besoin immédiat | Blessure, danger actuel, souffrance alléguée, animal disparu, intervention ou courrier avec échéance. | Aide humaine compétente avant revue documentaire ; aucun soin conseillé ni délai calculé de mémoire. |
| Animal | Espèce, âge déclaré et justificatif si pertinent, identification disponible, catégorie ou protection alléguée, usage compagnie/élevage/travail/loisir. | Pas de régime générique « animal » ; espèce ou statut incertain = question avant conclusion. |
| Acteurs | Propriétaire déclaré, détenteur enregistré, gardien effectif, acquéreur, cédant professionnel/particulier/association, intermédiaire ; personne agissant pour autrui. | Enregistrement, propriété et garde sont trois questions distinctes ; aucun pouvoir de représentation présumé. |
| Opération | Vente, cession gratuite, adoption associative, pension rémunérée, garde privée ; prix, don, frais, options, conditions. | Le titre « adoption » et le paiement d'une somme ne suffisent pas à qualifier la convention. |
| Lieux et dates | Pays et commune, contrat, réservation, remise, entrée/sortie de pension, apparition d'un signe, découverte, échanges et réception des courriers. | Versions et règles locales à rechercher ; langue française et domicile du demandeur ne déterminent pas seuls la loi applicable. |
| Pièces | Contrat et conditions à la date concernée, annonce, facture, échanges, justificatif d'identification, documents de remise, certificat ou constat vétérinaire pertinent. | Liste ciblée selon le cas ; absence de pièce fournie distincte d'absence de remise ou d'obligation établie. |
| État et dommage | Observation datée, auteur du constat, animal concerné, dommage matériel/corporel, garde au moment de l'événement. | Fait rapporté, pièce professionnelle et causalité distingués ; aucun diagnostic, vice ou responsable déduit. |
| Demande | Comprendre, obtenir une pièce, vérifier une facture, préparer une réponse, documenter un incident. | Choisir fiche, tableau ou brouillon utile ; examiner aussi ce que la personne s'est engagée à faire. |

Masquer les coordonnées non utiles et les données de tiers. Ne demander ni
dossier médical humain complet ni historique vétérinaire sans lien avec la
question. Aucun accès direct à un registre ou transfert automatique de pièces.

## Tâches hiérarchisées

Les rangs sont une proposition d'ordre de travail, sans lancement automatique.
Toutes les suites sont P3 et dépendent de DOM-033, PILOTE-003, BASE-005,
BASE-006, BASE-008 et BASE-013. ANM-001 crée le questionnaire commun et le paquet ;
les suivantes en dépendent pour leur socle technique, sans dépendance entre
elles. Le préalable PILOTE-003 est satisfait par la recette BASE-011 du
16 octobre 2026 ; les limites du pilote restent celles de son bilan.

| Rang | Story | Skill proposé | Sortie bornée | Dépendance métier |
|---|---|---|---|---|
| 1 | [ANM-001](../suites/anm-001-acquisition-chien-documents.md) | `dog-acquisition-document-review` | Lecture documentaire d'une vente de chien en France, questions au cédant | Aucune |
| 2 | [ANM-002](../suites/anm-002-adoption-chat-association.md) | `cat-adoption-agreement-review` | Lecture d'une convention d'adoption de chat avec une association | ANM-001 |
| 2 | [ANM-003](../suites/anm-003-facture-pension-chien.md) | `dog-boarding-invoice-review` | Rapprochement contrat, séjour et facture d'une pension professionnelle | ANM-001 |
| 3 | [ANM-004](../suites/anm-004-dommage-garde-privee.md) | `private-dog-care-incident` | Chronologie d'un dommage matériel pendant une garde privée de chien | ANM-001 |
| 3 | [ANM-005](../suites/anm-005-etat-chien-apres-vente.md) | `dog-sale-health-dispute-file` | Dossier factuel sur l'état allégué d'un chien après vente, sans diagnostic | ANM-001 |
| 3 | [ANM-006](../suites/anm-006-incident-signalement-chien.md) | `dog-incident-orientation` | Orientation d'un incident ou signalement concernant un chien détenu en France | ANM-001 |
| 4 | [ANM-007](../suites/anm-007-cession-autre-espece.md) | `other-species-transfer-orientation` | Qualification documentaire d'une cession d'autre espèce avant examen spécialisé | ANM-001 |

## Première tranche proposée : ANM-001

**Inclus :** particulier acquérant pour compagnie un chien auprès d'un
professionnel ou d'un particulier, contrat et remise situés en France ;
lecture d'un contrat/projet et des seules pièces de cession utiles, conditions
financières et obligations réciproques, liste conditionnelle de documents à
vérifier selon acteurs, dates et espèce, questions et brouillon au cédant.

**Exclus :** adoption associative, élevage pour l'activité, pension, état
pathologique contesté, action en garantie ou résolution, chien soumis à un
statut particulier non qualifié, transport/importation et formalités étrangères.
Pour ces situations, conserver la fiche factuelle et orienter vers la suite ou
le professionnel utile, en disant si la tâche reste proposée.

ANM-001 ne livre aucune promesse de remboursement. ANM-005 est propriétaire
de la contestation liée à l'état après vente : qualification des voies
éventuelles et de leurs conditions à vérifier dans sa propre tranche, sans
copier la garantie de conformité d'un objet ordinaire. L'achat entre
particuliers ne devient pas consommation par défaut.

## Frontières et interlocuteurs

| Domaine voisin | Question qu'il garde | Question conservée ici |
|---|---|---|
| Agriculture — DOM-014 | Exploitation d'élevage, activité professionnelle et obligations de l'exploitant. | Contrat de cession à un particulier et pièces propres à l'animal ; qualification du cédant utile au contrat. |
| Voisinage — DOM-020 | Nuisances répétées, occupation et relations de voisinage. | Identification du contrat/garde et obligations propres à la détention ; incident isolé documenté. |
| Assurance — DOM-005 | Garantie, déclaration de sinistre, refus ou montant demandé à l'assureur. | Faits de garde et engagements ; responsabilité et garantie ne se confondent pas. |
| Police et pénal — DOM-002 | Plainte, convocation, infraction alléguée et procédure pénale. | Chronologie et question liée à la détention ; pas d'infraction conclue depuis le récit ou une photo. |
| Responsabilité — DOM-035 | Dommage corporel et évaluation du préjudice, expertise générale. | ANM-004 borne la garde et un dommage matériel ; ANM-006 oriente la victime blessée. |
| Consommation — DOM-001 | Autres biens et services ordinaires, dont accessoire vendu séparément ; médiation générale si question distincte. | Vente de l'animal et pension ; pas de renvoi global au régime des biens courants. |
| Santé — DOM-007 | Soins et droits de la personne humaine. | Aucun avis médical vétérinaire ; questions de santé de l'animal à un vétérinaire. |
| Administration — DOM-010 | Recours formel contre une décision administrative distincte. | Identifier émetteur et objet d'une mesure relative à l'animal ; autorité compétente à vérifier selon lieu. |
| Environnement / chasse-pêche — DOM-030 / DOM-040 | Protection d'espèces et de milieux, capture/chasse/pêche et leur réglementation. | ANM-007 qualifie l'espèce et la cession avant orientation ; aucune autorisation de détention présumée. |
| Douanes / transport — DOM-009 / DOM-008 | Formalités d'importation et contrat de transport. | Contrat de cession et pièces reçues, sans certifier les mouvements internationaux. |
| Contentieux — litigation-legal | Actes de procédure et expertise judiciaire distincts. | Réclamation factuelle préalable et dossier ; aucun recours déposé. |
| Données — privacy-legal | Rectification de données ou accès à un fichier comme demande autonome. | Lire un justificatif d'identification sans déduire qu'il prouve la propriété. |
| Funéraire — DOM-031 | Prestations et démarches liées au décès d'une personne. | Le sort du corps d'un animal reste une extension à cadrer, non couverte par ces sept suites. |

Une orientation nomme la question, les pièces strictement utiles, le
destinataire et la disponibilité réelle. Pour le contrat : cédant,
association ou pension ; pour conseil juridique : avocat ou juriste compétent ;
pour santé animale : vétérinaire ; pour danger ou signalement : autorité
locale compétente à vérifier. L'autorité qui décide n'est pas un conseil.
La phrase BASE-013 et le renfort en tête s'appliquent selon la situation.

## Plan de sources, sans droit validé par le cadrage

| Ensemble à rechercher | Questions à vérifier lors de chaque implémentation |
|---|---|
| Code rural et de la pêche maritime | Cession, identification, documents et information, activité de garde, protection et détention, garanties propres aux ventes d'animaux ; textes réglementaires et transitions utiles. |
| Code civil | Contrat, preuve, propriété/garde, responsabilité du fait d'un animal, articulation des garanties ; qualification et conditions propres à l'action envisagée. |
| Code de la consommation | Applicabilité réelle à la prestation ou vente, qualité du professionnel, exclusions et articulation avec le régime animal ; aucune transposition automatique. |
| Code pénal et textes de procédure | Faits allégués et orientation pénale ; ANM-006 ne livre pas une consultation pénale. |
| Textes locaux et d'espèce | Mesures municipales/préfectorales, catégories et espèces protégées/non domestiques ; textes UE et conventions dans leur champ seulement. |
| Information officielle | [Ministère de l'Agriculture](https://agriculture.gouv.fr/), fiches Service-Public, autorité locale et opérateur du fichier d'identification selon besoin ; guides distincts des normes. |

Pistes non ouvertes pendant DOM-033 : aucune règle, liste universelle de
documents, durée, âge minimal, barème ou jurisprudence n'est validé ici.
Chaque implémentation ouvrira le texte exact, vérifiera version, territoire,
déclencheur, exceptions et dispositions transitoires, et gardera la trace de
lecture. Appliquer BASE-005 `1.3.0` (ou version ultérieure explicitement
relue), BASE-010 pour les voies d'accès et BASE-014 pour les sources du lot.

## Extensions non couvertes

Contrat de soins vétérinaires, élevage professionnel complet, équidés au fond,
animaux de rente, assistance, reproduction, décès et prestations funéraires
animalières, transport international et contentieux judiciaire devront faire
l'objet de nouvelles stories si sélectionnés. ANM-007 est une qualification
préalable ; elle ne prétend pas couvrir toutes les espèces.
