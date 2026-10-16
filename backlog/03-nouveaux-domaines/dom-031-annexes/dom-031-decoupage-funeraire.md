# DOM-031 — Découpage du domaine décès et prestations funéraires

Propositions du **16 octobre 2026**. Les 12 stories FUN restent `proposee`.
La [relecture documentaire](dom-031-verification.md) éprouve le routage sur
les trois scénarios de la story et sur des cas limites. Aucun répertoire de
plugin n'est créé par ce cadrage.

## Plugin retenu et contrat d'installation

**Nom conservé : `funeral-legal`**, identifiant publié `judge-fr-eu-funeral-legal`
(BASE-008). Le domaine traite les prestations et décisions funéraires :
devis, bon de commande, contrat et facture d'un opérateur funéraire ;
volonté du défunt et personne qui décide des funérailles ; concession,
sépulture, destination des cendres, exhumation ; organisation des premières
démarches ; prise en charge des frais, pour la seule identification des
questions et des interlocuteurs. Il ne règle pas la succession et ne lit pas
la garantie d'un contrat d'assurance. Public premier : le proche qui
organise ou conteste des obsèques, et la personne qui veut exprimer ses
propres volontés, sans formation juridique. L'opérateur funéraire n'est pas
un public visé par les tâches proposées.

| Élément | Décision du cadrage |
|---|---|
| Installation | Le paquet fonctionne seul : skills, références métier locales, copie BASE-005 et copies BASE-008 exigées par les contrôles. Aucun autre plugin requis ; un relais est une orientation. |
| Création du paquet | Par FUN-001, avec son premier skill. Aucun paquet vide. Inscription au marketplace et décompte des paquets dans les tests BASE-008 : décision explicite au moment de sélectionner FUN-001, coordonnée avec les autres premières tranches DOM retenues. |
| Profil et stockage | Aucun profil requis. Aucun registre de défunt, de famille ou de dossier n'est tenu ; les pièces servent à la réponse en cours. |
| Agents, hooks, connecteurs | Aucun prévu. Aucun accès à l'état civil, à un fichier des décès, à la liste des opérateurs habilités, à un registre de concessions, à un comparateur de prix ou à une messagerie. Les pièces sont fournies par la personne. |
| Envoi | Brouillons seulement ; le plugin n'envoie aucune réclamation et ne contacte ni opérateur, ni mairie, ni banque, ni assureur, ni médiateur, ni proche. |

## Garde-fous propres au domaine

- **Un moment de deuil.** La sortie commence par ce qui doit être décidé
  maintenant et ce qui peut attendre, dans des phrases courtes et sans
  jargon. Elle ne pousse ni à signer, ni à refuser, ni à réclamer ; elle ne
  porte aucun jugement sur un choix religieux, philosophique ou familial.
- **Trois qualités à ne pas confondre.** Le signataire du devis ou du bon
  de commande, la personne qui a qualité pour décider des funérailles et la
  personne éventuellement tenue au paiement sont qualifiés séparément, à
  partir des pièces et des faits déclarés. Aucune de ces qualités n'est
  déduite du seul lien familial, du seul fait d'être présent ou du seul fait
  d'avoir payé un acompte.
- **Volonté du défunt : écrite, déclarée ou supposée.** Un écrit, une
  parole rapportée et une supposition sont distingués ; le plugin ne dit pas
  laquelle l'emporte ni ce que le défunt « aurait voulu ».
- **Aucune présomption contre l'autre partie.** L'opérateur n'est pas
  présumé abusif, une prestation n'est pas présumée inutile, un proche n'est
  pas présumé de mauvaise foi. Une commande alléguée sans trace est notée
  comme inconnue, pas comme absence établie.
- **Aucune promesse d'issue.** Ni remboursement, ni prise en charge par la
  succession, une banque, une caisse, un contrat ou la commune n'est
  annoncé ; la sortie décrit une demande et ce qui reste à établir.
- **Aucun délai, plafond, prix ni montant inventé.** Délais d'inhumation
  ou de crémation, durée de concession, plafond d'un prélèvement sur les
  comptes du défunt, prix courants et montants d'aide ne sont donnés
  qu'avec la source lue et les dates établies. Les montants sont recopiés
  des pièces ; un écart entre deux montants recopiés est présenté comme une
  simple différence, sans qualification.
- **Urgence d'abord.** Quand une décision doit être prise vite (corps en
  attente, désaccord bloquant, autorisation refusée), la sortie le dit en
  tête et nomme l'interlocuteur à joindre sans attendre, sans calculer de
  délai non sourcé.
- **Aucun choix d'opérateur.** Le plugin ne recommande, ne classe ni ne
  compare des opérateurs ; il recopie la mention d'habilitation lue sur la
  pièce et dit où la vérifier.
- **Collecte minimale.** La cause du décès, les données de santé du défunt,
  le numéro de sécurité sociale, un code bancaire ou la copie intégrale d'un
  acte d'état civil ne sont pas demandés ; seules les mentions utiles à la
  tâche sont recopiées.

## Points d'entrée sans vocabulaire juridique

La personne part de son problème ; le skill qualifie ensuite. Ces phrases
servent de contrôle d'orientation pour chaque lot.

| Ce que la personne dit | Tâche proposée |
|---|---|
| « Les pompes funèbres m'ont donné un devis, je ne sais pas si tout est obligatoire » ; « dois-je signer ce soir ? » | FUN-001 |
| « La facture des obsèques ne correspond pas au devis » ; « on nous facture des soins que personne n'a demandés » | FUN-002 |
| « Ma sœur veut une crémation, papa voulait être enterré » ; « qui décide pour les obsèques ? » | FUN-003 |
| « Les pompes funèbres me réclament le paiement alors que je n'ai rien signé » | FUN-004 |
| « Qui doit payer les obsèques ? » ; « peut-on payer avec le compte de maman ? » | FUN-005 |
| « Elle avait un contrat obsèques et on nous demande un supplément » | FUN-006 |
| « La mairie dit que la concession est échue » ; « a-t-on le droit d'être enterré dans le caveau de famille ? » | FUN-007 |
| « Mon père vient de mourir, qu'est-ce qu'on doit faire maintenant ? » | FUN-008 |
| « Je veux que mes proches sachent ce que je veux pour mes obsèques » | FUN-009 |
| « Le marbrier a gravé une erreur sur la tombe » ; « le monument n'est pas celui du devis » | FUN-010 |
| « Peut-on garder l'urne à la maison ? » ; « on ne s'entend pas sur les cendres » | FUN-011 |
| « On veut transférer le corps dans un autre cimetière » | FUN-012 |

Une phrase mêlant plusieurs objets (« mon frère a signé, on n'est pas
d'accord sur la crémation et on nous réclame déjà un acompte ») produit une
sortie par objet, dans l'ordre d'urgence : décision bloquée sur les
funérailles, puis engagement ou paiement réclamé, puis contenu des
prestations.

## Qualification commune

FUN-001 crée `funeral-legal/references/qualification-funeraire.md`, réutilisée
par les autres skills du paquet.

| Axe | Faits à recueillir | Ce qui peut changer |
|---|---|---|
| Personnes et qualités | Défunt ; personne qui organise ; signataire du devis ou du bon de commande ; personne qui se dit habilitée à décider ; proches en désaccord ; personne à qui le paiement est réclamé ; représentant d'un majeur protégé. | Les trois qualités de la section suivante ; mesure de protection → DOM-026. |
| Volontés connues | Écrit du défunt (testament, déclaration, contrat obsèques), paroles rapportées et par qui, absence de volonté connue. | FUN-003 ; aucune volonté supposée. |
| Opérateurs et intervenants | Opérateur funéraire et mention d'habilitation lue, chambre funéraire, crématorium, thanatopracteur, marbrier, commune gestionnaire du cimetière, établissement de santé ou médico-social. | Interlocuteur et pièce à demander ; habilitation recopiée, jamais vérifiée en ligne. |
| Pièces | Devis, bon de commande, contrat, facture, contrat obsèques, titre de concession, autorisations reçues, échanges, preuves de paiement. | Distinguer pièce fournie, fait déclaré et inconnu. |
| Dates | Décès, premier contact avec l'opérateur, devis, signature, prestations, cérémonie, facture, demande de paiement, échéance alléguée. | Aucun délai calculé sans texte lu et date prouvée. |
| Lieu et éléments étrangers | Commune du décès, de la cérémonie et de la sépulture ; décès ou sépulture hors de France. | Règles locales à rechercher ; élément étranger → point ouvert. |
| Financement | Fonds du défunt, contrat obsèques, capital décès allégué, aide alléguée, avance par un proche. | FUN-005 ; chaque mécanisme reste à son propriétaire. |
| Urgence | Corps en attente, désaccord bloquant, autorisation refusée ou retardée, signature demandée immédiatement. | Renfort en tête ; interlocuteur immédiat nommé. |

## Signataire, personne qui décide et personne tenue au paiement

Ces trois qualités sont la colonne vertébrale du domaine. Chaque skill les
affiche dans une fiche distincte, avec la pièce ou le fait déclaré qui les
fonde, ou la mention « à établir ».

| Qualité | Question posée | Ce qui la fonde | Ce qui ne suffit pas |
|---|---|---|---|
| Signataire | Qui s'est engagé envers l'opérateur, pour quelles prestations ? | Signature du devis ou du bon de commande, accord écrit retrouvé. | Présence au rendez-vous, nom porté sur un courriel de l'opérateur, lien familial. |
| Personne qui décide | Qui a qualité pour pourvoir aux funérailles et arbitrer leurs conditions ? | Volonté exprimée du défunt, désignation par lui, règle à lire selon la situation. | Lien familial seul, accord d'une partie des proches, initiative prise en premier. |
| Personne tenue au paiement | Qui peut être tenu de payer, à quel titre ? | Engagement signé, règle successorale ou familiale à lire, contrat. | Lien familial seul, réception de la facture, paiement d'un acompte. |

Une même personne peut cumuler ces qualités ou n'en avoir aucune. Quand les
pièces ne permettent pas de les établir, la sortie le dit et liste ce qui
manque ; elle ne choisit pas une réponse unique pour « la famille ».

## Frontières

| Domaine | Ce qui lui revient | Ce que funeral garde |
|---|---|---|
| Successions — DOM-016 | Règlement de la succession, qualité d'héritier, option successorale, frais funéraires comme passif de la succession, comptes du défunt et leur déblocage (y compris un paiement de la facture sur ces comptes). | Le contenu et la facture des prestations ; l'identification des questions de prise en charge (FUN-005). |
| Assurance — DOM-005 | Contrat obsèques comme contrat d'assurance : garantie, capital, bénéficiaire, refus de versement (INS-004, INS-011) ; allocation obsèques d'une complémentaire ou d'une prévoyance (INS-009). | Les prestations prévues au contrat obsèques et leur exécution par l'opérateur (FUN-006). |
| Consommation — DOM-001 | Repli CONSO-014 tant que funeral-legal n'est pas livré, avec les règles sectorielles annoncées comme non examinées ; démarchage hors du secteur funéraire (CONSO-020) ; médiation générale (CONSO-006). | Devis, contrat et facture funéraires (découpage DOM-001). |
| Banque — DOM-004 | Paiement contesté (BNK-001), prélèvement (BNK-006), compte bloqué d'une personne vivante (BNK-014). | Rien, hors question bornée ; comptes du défunt → DOM-016. |
| Protection sociale — DOM-012 | Capital décès ou prestation d'un organisme social, ses conditions et sa contestation. | Mention de la piste dans la carte des financements (FUN-005). |
| Santé — DOM-007 | Accès d'un ayant droit au dossier médical (SAN-003), soins avant le décès, réclamation contre un établissement. | Chambre mortuaire et transfert du corps sous l'angle des prestations et des frais. |
| Protection des majeurs — DOM-026 | Pouvoirs d'un tuteur ou curateur, contrat obsèques souscrit ou payé pendant une mesure. | Lecture des prestations une fois les pouvoirs établis. |
| Police et pénal — DOM-002 | Obstacle médico-légal, enquête, atteinte alléguée à la volonté du défunt ou à une sépulture comme infraction (CRIM-004). | La décision civile sur les funérailles et les prestations. |
| Contentieux — litigation | Procédure une fois la voie qualifiée (CTX-025, CTX-026), lecture d'un jugement (CTX-028). | Préparation des éléments de volonté et de qualité avant toute saisine (FUN-003). |
| Exécution — DOM-003 | Relance de recouvrement (ENF-002), injonction de payer (ENF-012), acte d'exécution (ENF-001). | La question de fond : qui a signé, quoi est facturé (FUN-004). |
| Administratif — DOM-010 | Recours contre une décision du maire hors cimetière, accès à un document administratif ; état civil en général. | Concession, autorisations funéraires et cimetière, sous l'angle des questions à poser (FUN-007, FUN-008, FUN-012). |
| Famille — DOM-013 | Obligations entre membres de la famille hors funérailles. | Rien ; contribution aux frais d'obsèques sans actif → point ouvert. |
| Dettes — DOM-024 | Difficulté globale à payer plusieurs dettes. | La contestation d'une facture funéraire précise. |
| Construction — DOM-015 | Travaux de bâtiment hors cimetière. | Monument et caveau (FUN-010). |
| Animaux — DOM-033 | Sort du corps d'un animal, prestations d'un crématorium animalier. | Rien. |
| Données personnelles — privacy | Données d'un défunt détenues par un service en ligne, souhaits numériques. | Rien. |

Les relais sont des orientations : une question bornée, les seules pièces
utiles, sans dépendance d'installation ni appel à un skill absent.

## Tâches hiérarchisées

Le rang combine l'utilité directe (situation S-30), l'urgence propre au
moment du décès, la vérifiabilité et les dépendances. Il reste une
proposition : aucune story n'est sélectionnée par DOM-031. Toutes dépendent
de DOM-031, PILOTE-003, BASE-005, BASE-006 et BASE-008 ; FUN-001 crée le
paquet. Les rangs 1 à 3 portent la priorité P2, le rang 4 la priorité P3.

| Rang | Story | Skill proposé | Résultat borné | Dépendances métier |
|---|---|---|---|---|
| 1 | [FUN-001](../suites/fun-001-devis-funeraire.md) | `funeral-quote-review` | Devis funéraire lu avant engagement ; prestations demandées et proposées séparées ; demande d'explication | Aucune |
| 2 | [FUN-002](../suites/fun-002-facture-prestations.md) | `funeral-invoice-claim` | Facture comparée au devis et aux commandes retrouvées ; réclamation sur prestations non demandées | FUN-001 |
| 2 | [FUN-003](../suites/fun-003-volonte-decision.md) | `funeral-decision-authority` | Volontés et qualités organisées en cas de désaccord entre proches ; renfort et orientation | FUN-001 |
| 2 | [FUN-004](../suites/fun-004-demande-paiement.md) | `funeral-payment-demand` | Demande de paiement d'un opérateur lue : signataire, personne sollicitée, réponse | FUN-002, FUN-005 |
| 2 | [FUN-005](../suites/fun-005-prise-en-charge-frais.md) | `funeral-cost-funding` | Carte des financements à interroger et des questions de prise en charge, sans promesse | FUN-001 |
| 3 | [FUN-006](../suites/fun-006-contrat-obseques.md) | `prepaid-funeral-plan-review` | Prestations d'un contrat obsèques comparées au devis d'exécution ; supplément expliqué ou réservé | FUN-001 |
| 3 | [FUN-007](../suites/fun-007-concession.md) | `burial-concession-review` | Titre de concession lu ; questions à la commune sur l'inhumation, le renouvellement ou la reprise | FUN-003 |
| 3 | [FUN-008](../suites/fun-008-premieres-demarches.md) | `after-death-first-steps` | Liste ordonnée des démarches et pièces des premiers jours, à vérifier | FUN-001 |
| 3 | [FUN-010](../suites/fun-010-monument-marbrerie.md) | `funeral-monument-works` | Monument, caveau ou gravure comparés au devis du marbrier ; réclamation | FUN-002 |
| 3 | [FUN-011](../suites/fun-011-destination-cendres.md) | `cremation-ashes-decision` | Destination des cendres : volontés, personne qui décide, questions et demande | FUN-003 |
| 4 | [FUN-009](../suites/fun-009-volontes-anticipees.md) | `funeral-wishes-statement` | Expression écrite de ses propres volontés funéraires, sans valeur affirmée | FUN-003 |
| 4 | [FUN-012](../suites/fun-012-exhumation-transfert.md) | `exhumation-transfer-request` | Demande d'exhumation ou de transfert : qui peut demander, pièces, questions | FUN-007 |

FUN-001 possède `qualification-funeraire.md` (qualification commune et
fiche des trois qualités) et `lecture-devis-funeraire.md` (structure d'un
devis, prestations demandées ou proposées, mentions à recopier), relus par
toutes les autres tâches. FUN-003 possède `volonte-et-decision.md`, relue par
FUN-007, FUN-009 et FUN-011. FUN-005 possède `prise-en-charge-frais.md`,
relue par FUN-004 ; FUN-006 y renvoie comme orientation. FUN-007 possède
`concession-funeraire.md`, relue par FUN-012. Les autres références
spécialisées (contrat obsèques, premières démarches, travaux au cimetière,
destination des cendres, exhumation) appartiennent chacune à leur seule
tâche. Une tâche suivante consomme ces références sans les
réécrire. Aucun cycle.

## Première tranche : FUN-001

**Inclus :** un devis remis par un opérateur funéraire établi en France pour
les obsèques d'une personne décédée en France, avant ou juste après sa
signature ; besoin exprimé par la personne (inhumation ou crémation,
cérémonie, lieu) recopié tel quel ; lecture des postes du devis ;
séparation entre prestations demandées, prestations proposées par
l'opérateur et postes dont le caractère obligatoire est à vérifier ;
mentions recopiées (opérateur, habilitation, date, validité, conditions de
paiement) ; brouillon de demande d'explication avant engagement.

**Exclus :** facture après les obsèques (FUN-002) ; désaccord entre proches
(FUN-003) ; paiement réclamé (FUN-004) ; financement et qui paie (FUN-005) ;
contrat obsèques souscrit (FUN-006) ; monument et marbrerie (FUN-010) ;
décès ou sépulture hors de France ; caractère obligatoire d'une prestation,
prix courant, délai ou règle non sourcés ; avis sur le choix d'opérateur ;
envoi.

**Sortie :** ce qui doit être décidé maintenant et ce qui peut attendre ;
fiche de qualification avec les trois qualités ; tableau poste par poste
(prestation, montant recopié, demandée ou proposée selon les pièces,
obligation à vérifier, question à poser) ; mentions recopiées et mentions
absentes ; brouillon de demande d'explication à l'opérateur ; ce qui reste à
vérifier (modèle de devis, prestations obligatoires, habilitation, avec la
source lue ou réservés) ; suites (FUN-003 si les proches ne sont pas
d'accord, FUN-005 pour le financement, FUN-006 si un contrat obsèques
existe) ; limites et phrase BASE-013.

## Points ouverts à découper

- Décès ou sépulture hors de France, rapatriement du corps ou des cendres :
  articulation avec le droit étranger, les autorités consulaires et le
  transport international ; aucun propriétaire décidé.
- Don du corps à la science et prélèvements après le décès : relation avec
  la santé (DOM-007) et les établissements ; pas de story tant que le
  propriétaire n'est pas arrêté.
- Enfant né sans vie et décès périnatal : démarches, état civil et
  funérailles propres, à cadrer avec une attention particulière au ton.
- Saisine urgente du juge sur les conditions des funérailles : aucune story
  litigation ne couvre cette procédure ; FUN-003 oriente vers un avocat sans
  préparer la saisine.
- Contribution des enfants, du conjoint ou d'autres proches aux frais
  d'obsèques en l'absence d'actif successoral : propriétaire à arrêter avec
  DOM-013 et DOM-016 ; FUN-005 nomme seulement la question.

Ces besoins ne reçoivent aucune story tant que leur propriétaire n'est pas
arrêté ; ils ne sont pas couverts par les suites ci-dessus.

## Plan de recherche pour les futures implémentations

Ces lignes sont des **pistes à vérifier**, pas des règles actuelles. Ouvrir
le texte et sa version à la date des faits, citer le passage lu selon
BASE-005. Les voies officielles BASE-010 servent en maintenance, jamais au
runtime.

| Question | Sources à ouvrir lors du lot | Propriétaire |
|---|---|---|
| Devis et information des familles | Code général des collectivités territoriales, service extérieur des pompes funèbres (pistes L2223-19 et suivants), devis (piste L2223-21-1) et habilitation (piste L2223-23) ; règlement national des pompes funèbres (pistes R2223-24 et suivants) ; arrêté fixant le modèle de devis des prestations funéraires, à identifier dans sa version en vigueur ; fiches DGCCRF et Service Public comme information. | FUN-001 |
| Facture et réclamation | Pistes FUN-001 ; Code civil, preuve des obligations (pistes 1353, 1359 et suivants) et inexécution (pistes 1217 et suivants) ; Code de la consommation, médiation (pistes L612-1 et suivants). | FUN-002 |
| Volonté et personne qui décide | Loi du 15 novembre 1887 sur la liberté des funérailles, à lire dans sa version en vigueur ; Code civil, respect dû au corps après la mort (piste 16-1-1) ; Code de procédure civile, contestation sur les conditions des funérailles (piste 1061-1), pour l'orientation seule ; Code pénal, atteinte à la volonté du défunt (piste 433-21-1), pour l'orientation DOM-002. | FUN-003 |
| Demande de paiement | Pistes FUN-002 ; Code civil, engagement du signataire et frais funéraires (pistes 806 et 2331), à vérifier ; pistes DOM-016 pour la succession. | FUN-004 |
| Prise en charge des frais | Code monétaire et financier, prélèvement sur les comptes du défunt pour les frais funéraires (piste L312-1-4), pour l'orientation DOM-016 ; Code de la sécurité sociale, capital décès (pistes L361-1 et suivants), pour l'orientation DOM-012 ; CGCT, obsèques des personnes dépourvues de ressources (piste L2223-27) ; Code civil, obligation alimentaire (pistes 205 et suivants), pour le point ouvert. | FUN-005 |
| Contrat obsèques | CGCT, formules de financement en prévision d'obsèques (pistes L2223-33-1, L2223-34-1 et suivants) et interdiction de certaines offres de services (piste L2223-33) ; Code des assurances pour la seule qualification, orientation DOM-005. | FUN-006 |
| Concession | CGCT, concessions dans les cimetières (pistes L2223-13 et suivants), reprise des concessions en état d'abandon (piste L2223-17) et dispositions réglementaires (pistes R2223-12 et suivants) ; police des cimetières (pistes L2213-7 et suivants) ; règlement du cimetière communal comme pièce. | FUN-007 |
| Premières démarches | Code civil, déclaration et acte de décès (pistes 78 et suivants) ; CGCT, certificat de décès (piste L2223-42), opérations consécutives au décès et autorisations d'inhumation ou de crémation (pistes R2213-1-1 et suivants, R2213-31 et suivants) ; soins de conservation (pistes R2213-2-1 et suivants) ; information officielle Service Public. | FUN-008 |
| Volontés anticipées | Loi du 15 novembre 1887 (pistes FUN-003) ; formes possibles d'expression des volontés, à rechercher ; contrat obsèques comme alternative, renvoi FUN-006. | FUN-009 |
| Monument et marbrerie | Code civil, contrat d'entreprise (pistes 1710, 1787 et suivants) ; CGCT, travaux dans les cimetières et règlement communal (pistes L2213-8 et suivants), à vérifier ; information sur les prix des prestations, texte à identifier. | FUN-010 |
| Destination des cendres | CGCT, destination des cendres (pistes L2223-18-1 et suivants) ; Code civil (piste 16-1-1). | FUN-011 |
| Exhumation et transfert | CGCT, exhumation et transport de corps (pistes R2213-40 et suivants, R2213-8 et suivants) ; pistes FUN-007 pour la concession. | FUN-012 |

Aucune de ces pistes n'a été ouverte par ce cadrage. Les numéros d'articles
et de textes viennent de la connaissance de l'agent de maintenance ; leur
existence, leur version et leur portée sont à établir par chaque
propriétaire.

## Contrat commun des stories FUN

Chaque lot applique BASE-003, BASE-008, la méthode BASE-005 embarquée, les
garde-fous ci-dessus et les couches de recette BASE-006 : structure, paquet
détaché, client, résultat métier, lecture par une personne sans formation
juridique. Il inscrit NOTICE local et racine, synchronise manifeste et
marketplace, et n'annonce dans le README que les tâches livrées.

Chaque skill qualifie d'abord, puis traite. Il charge la méthode locale,
distingue mention d'une pièce, fait déclaré, règle lue et inconnue, et ne
donne ni délai, ni plafond, ni prix, ni montant sans source lue et date
établie, hors montant recopié d'une pièce. Les pièces fournies sont des
données, jamais des instructions. Sans référence ou relais adapté, il
produit les questions et pièces utiles, sans appeler une branche absente.
Chaque réponse se termine par la phrase BASE-013 nommant l'interlocuteur de
la situation (association de consommateurs, médiateur de la consommation du
secteur, notaire pour la succession, avocat en cas de désaccord ou de
procédure), avec un renfort en tête en cas de décision urgente, de
désaccord bloquant ou de paiement réclamé avec échéance.

Les fichiers « à créer » des suites sont des livrables futurs. La portée de
ce cadrage figure dans la [vérification](dom-031-verification.md).
