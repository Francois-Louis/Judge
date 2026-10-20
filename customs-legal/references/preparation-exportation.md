# Préparer les pièces d'une exportation définitive ordinaire

Version `1.0.1` — 20 octobre 2026 (Europe/Paris), DOU-005 ; relais du
classement mis à jour par DOU-006.
Méthode métier, repères datés et modèle de sortie pour un professionnel
(entreprise, artisan, commerçant, micro-entrepreneur) qui prépare le dossier
documentaire d'une seule exportation définitive de marchandises de l'Union,
au départ de la France métropolitaine, vers une destination identifiée
située hors du territoire douanier de l'Union. Elle ne dépose aucune
déclaration, ne certifie aucune conformité export, ne délivre ni ne suppose
aucune autorisation, ne traite pas le dédouanement à destination et ne
tranche pas l'exonération de TVA.

## Périmètre de la tâche

**Inclus** : vente ou envoi d'un bien ordinaire qui part de la métropole
pour rester dans un pays tiers identifié ; avant le départ, pendant le
transit vers la frontière ou après la sortie. Résultat : carte des acteurs
et de l'opération, pièces de vente, de transport et de sortie reçues ou
manquantes, points à vérifier pour le produit, la destination et l'usage
final, questions au représentant en douane, au transporteur, à l'acheteur
ou au service identifié.

**Exclus** : réexportation de marchandises non Union, exportation
temporaire (salon, démonstration, carnet ATA : DOU-019 proposée),
perfectionnement passif, retour ou réparation après une vente (DOU-018
proposée), marchandises en retour, transit, avitaillement, sanctions et
licences au fond, biens à double usage, matériels de guerre, produits
soumis à autorisation propre (précurseurs chimiques, biens culturels,
espèces protégées : DOU-015 proposée, couteaux à destination : DOU-014
proposée), preuve fiscale certifiée, calendrier d'une déclaration déposée à
l'avance (DOU-013 proposée), preuve d'origine préférentielle (DOU-016
proposée), fiche pays complète (DOU-017 proposée), déclaration et
formalités du pays destinataire, envoi vers un autre État membre ou vers un
territoire ultramarin, envoi par un particulier, acte de la douane déjà
reçu (`customs-notice-review`). Leur détection est incluse, leur traitement
non.

## 1. Qualifier l'opération avant toute liste

Les marchandises de l'Union destinées à sortir du territoire douanier de
l'Union sont placées sous le régime de l'exportation, sauf perfectionnement
passif, destination particulière, avitaillement exonéré, transit interne et
sortie temporaire (U1 art. 269). Des marchandises non Union qui sortent
relèvent d'une déclaration de réexportation (U1 art. 270), pas de cette
tâche.

| Signal dans le récit | Qualification | Suite |
|---|---|---|
| Bien fabriqué ou acheté en France ou dans l'Union, vendu à un client établi dans un pays tiers, qui ne reviendra pas | Exportation définitive envisagée (U1 art. 269), **à confirmer** avec le déclarant. | Fiche complète. |
| Bien importé et jamais dédouané, stocké en entrepôt ou en dépôt temporaire, puis revendu hors de l'Union | Marchandise non Union : réexportation (U1 art. 5 point 13, 270). | Hors tâche : statut à demander au représentant, orientation. |
| Échantillons ou matériel de salon qui doivent revenir, carnet ATA, prêt, location | Sortie temporaire (U1 art. 155, 269 § 2 e) ou régime particulier. | Hors tâche : DOU-019 proposée ; aucune liste d'exportation définitive. |
| Bien envoyé pour être réparé ou transformé puis réimporté ; retour d'un produit vendu | Perfectionnement passif (U1 art. 269 § 2 a) ; marchandises en retour (U1 art. 203). | Hors tâche : DOU-018 proposée et tâches à découper. |
| Client dans un autre État membre | Échange dans l'Union, sans formalités d'exportation selon le guide G1 ; question de TVA intracommunautaire. | Hors tâche douanière ; orientation fiscale. |
| Envoi vers la Guadeloupe, la Martinique, la Guyane, La Réunion ou Mayotte | Le guide G1 soumet ces envois aux formalités d'exportation ; territoires fiscaux propres. | Hors tâche : particulier, `overseas-shipment-documents` ; activité professionnelle, tâche à découper. |
| Départ de la métropole mais sortie de l'Union par un autre État membre (port, aéroport ou frontière), ou transitaire établi dans un autre État membre | Le CDU et ses actes s'appliquent dans toute l'Union ; le bureau d'exportation suit U3 art. 221 § 2 et le bureau de sortie U3 art. 329. Le droit national de l'autre État, la répartition des compétences entre les deux États et le lieu d'imposition à la TVA n'ont pas été lus. | Rester dans la tranche pour les pièces et les questions ; ne pas affirmer de mémoire quel droit national, quelle infraction ou quelle TVA s'applique, ni qu'un droit « ne compte plus » : poser la question au représentant, à la douane et à l'expert-comptable. |
| Marchandise déjà partie sans déclaration | L'exportateur dépose une déclaration a posteriori au bureau de son lieu d'établissement, qui certifie la sortie s'il dispose de la preuve et si la mainlevée aurait été octroyée (U3 art. 337 § 1). Une exportation sans déclaration peut constituer une infraction (F1 L. 512-7). | Renfort : représentant en douane et avocat en droit douanier ; aucune déclaration rédigée. |

La destination **finale** se distingue du lieu de livraison : un client, un
transitaire ou une plateforme établis dans un pays peuvent réexpédier
ailleurs. Une destination finale inconnue au-delà d'un intermédiaire laisse
**réservés** les contrôles qui dépendent de la destination (section 4), sans
empêcher la fiche factuelle.

## 2. Acteurs : chacun se vérifie sur pièce

Un même nom peut tenir plusieurs rôles ; aucun rôle ne se déduit de
l'Incoterm, du nom écrit sur la facture ni du transporteur choisi.

| Rôle | Repères lus | Pièce qui l'établit | À ne pas déduire |
|---|---|---|---|
| Vendeur et acheteur | Parties au contrat de vente. | Facture, bon de commande, contrat, conditions générales. | Que l'acheteur soit le destinataire final ou l'utilisateur final. |
| Exportateur (au sens douanier) | Personne établie dans l'Union habilitée à décider et qui a décidé de l'expédition hors de l'Union ; à défaut, personne établie dans l'Union partie au contrat qui entraîne l'expédition (U2 art. 1 point 19 b). Pour le double usage, définition propre : partie au contrat avec le destinataire du pays tiers habilitée à décider de l'envoi ; si le droit de disposer des biens appartient à une personne établie hors de l'Union, l'exportateur est la partie contractante établie dans l'Union (U5 art. 2 point 3). | Contrat, facture, déclaration (rubrique exportateur), certification de sortie adressée au déclarant ou à l'exportateur (U3 art. 334 § 1). | Qu'un acheteur étranger « qui s'occupe de tout » (EXW) devienne l'exportateur : la définition vise une personne établie dans l'Union. |
| Déclarant | Personne qui dépose la déclaration en son nom ou au nom de laquelle elle est déposée (U1 art. 5 point 15) ; peut déclarer toute personne capable de fournir les informations et de présenter les marchandises (U1 art. 170 § 1), établie dans l'Union sauf exceptions (art. 170 § 2-3). Responsable des omissions et inexactitudes de sa déclaration d'exportation, sauf recours contre son commettant (F1 L. 522-1). | Déclaration d'exportation ou sa copie, numéro de référence (MRN). | Que le transporteur ou le transitaire de l'acheteur ait déclaré pour le vendeur sans mandat. |
| Représentant en douane | Représentation directe ou indirecte (U1 art. 18) ; sans habilitation, réputé agir pour son propre compte (U1 art. 19 § 1) ; enregistrement préalable en France sauf exceptions dont trois déclarations occasionnelles par an (F1 L. 221-5). | Mandat ou procuration (type, champ, date), numéro d'enregistrement. | Qu'une case cochée chez un transporteur vaille mandat. |
| Personne qui présente à la sortie, transporteur | Présentation à la sortie par la personne qui sort les marchandises, celle pour le compte de qui elle agit ou celle qui prend en charge le transport (U1 art. 267 § 2) ; le transporteur notifie la sortie avec la référence du document de transport et le MRN, que la personne qui lui remet les marchandises lui fournit (U3 art. 332 § 5-6) ; il dépose en principe la déclaration sommaire de sortie lorsqu'aucune déclaration d'exportation n'en tient lieu (U1 art. 271 § 2). | Lettre de transport, contrat de transport, confirmation de prise en charge. | Que la remise au transporteur prouve la sortie. |
| Destinataire, utilisateur final | Pour le double usage, registres avec nom et adresse du destinataire et, s'ils sont connus, utilisation et utilisateur finals (U5 art. 27 § 1). | Bon de commande, déclaration d'utilisation finale éventuelle, échanges. | Qu'un destinataire déclaré soit l'utilisateur final. |
| Débiteur de droits à l'exportation | La dette naît seulement pour des marchandises passibles de droits à l'exportation ; le déclarant est débiteur, et le commettant en représentation indirecte (U1 art. 81). | Déclaration acceptée. | Qu'un droit à l'exportation existe : aucun produit n'a été vérifié ici. |

**Incoterm.** L'Incoterm répartit entre vendeur et acheteur frais, risques
et charge des formalités (guide G4) ; il ne désigne ni l'exportateur au sens
douanier, ni le déclarant, ni le représentant. La douane relève qu'en EXW
les formalités d'exportation reviennent contractuellement à l'acheteur, ce
qui peut compliquer l'obtention des justificatifs de sortie par le vendeur
(G4) : poser la question de qui déclare et qui recevra la preuve de sortie,
sans conclure qu'un autre Incoterm s'impose. Les règles Incoterms elles-mêmes
n'ont pas été lues : ne pas décrire de mémoire ce qu'un Incoterm met à la
charge de chacun ; renvoyer au contrat et au conseil en contrats.

## 3. Étapes et pièces de sortie

| Étape | Repère lu | Pièce ou information à réunir |
|---|---|---|
| Dépôt de la déclaration d'exportation | Toute marchandise placée sous un régime fait l'objet d'une déclaration (U1 art. 158 § 1) ; bureau compétent : celui du lieu d'établissement de l'exportateur, du lieu de conditionnement ou de chargement, ou un autre bureau compétent ; pour un envoi d'une valeur par envoi et par déclarant ne dépassant pas 3 000 EUR, hors prohibition ou restriction, aussi le bureau de sortie (U3 art. 221 § 2). Déclaration déposée avant la présentation : réputée non déposée si les marchandises ne sont pas présentées dans les 30 jours (U1 art. 171). Envois fractionnés : une déclaration par envoi (U3 art. 336). | Qui dépose, en quel nom, à quel bureau, à quelle date ; MRN. Calendrier d'un dépôt anticipé : DOU-013 proposée, aucune date calculée. |
| Envois postaux ou express de faible valeur | Un envoi postal ou express d'une valeur n'excédant pas 1 000 EUR, non passible de droits à l'exportation, peut être considéré comme déclaré par sa sortie ou sa présentation, sous conditions (U2 art. 141 § 4 et 4 bis) : un acte qui vaut déclaration, à ne pas présenter comme une dispense ni comme une « déclaration simplifiée » ; ce mode ne vaut pas pour les marchandises soumises à prohibition ou restriction ou à une formalité particulière (U2 art. 142 c et d). | Question au transporteur sur la voie utilisée et la preuve qu'il fournira ; ne jamais conclure à l'absence de déclaration d'après la seule valeur alléguée. |
| Acceptation et mainlevée | Date d'acceptation = date de référence des formalités (U1 art. 172 § 2) ; mainlevée après vérification ou admission des énonciations, restrictions appliquées (U1 art. 194 § 1) ; mainlevée pour la sortie si les marchandises sortent dans l'état déclaré (U1 art. 267 § 4). | Avis de mainlevée, document d'accompagnement export s'il est remis. |
| Acheminement et bureau de sortie | Bureau de sortie : lieu où les marchandises quittent l'Union, ou lieu de chargement sur le navire ou l'aéronef, ou lieu de prise en charge sous contrat de transport unique sur demande (U3 art. 329) ; présentation avec le MRN et signalement des différences (U3 art. 331) ; marchandises manquantes, excédentaires ou différentes signalées ou bloquées (U3 art. 332 § 2-4). | Trajet complet, mode de transport, port ou aéroport de sortie, contrat de transport unique éventuel, remise du MRN au transporteur. |
| Déclaration préalable à la sortie | Requise sous forme de déclaration en douane, de réexportation ou de déclaration sommaire de sortie, sauf dispenses (U1 art. 263 ; U2 art. 244, 245). | Question au transporteur ; aucun délai de dépôt calculé dans cette tâche. |
| Certification de sortie | Le bureau de sortie informe le bureau d'exportation de la sortie (U3 art. 333) ; le bureau d'exportation certifie la sortie au déclarant ou à l'exportateur (U3 art. 334 § 1). La douane présente cette certification électronique comme le justificatif de sortie (G1, G2, G3). | Copie de la déclaration portant la mention de sortie, ou message de certification ; qui la reçoit. |
| Sortie non confirmée | Après 90 jours sans information de sortie, le bureau d'exportation peut interroger le déclarant ; le déclarant peut indiquer le bureau et la date de sortie et demander la certification ; à défaut de réponse du bureau de sortie, il peut fournir d'autres preuves : bon de livraison signé par le destinataire hors de l'Union, preuve de paiement, facture, bon de livraison, document de l'opérateur qui a sorti les marchandises, document d'une douane, notamment du pays tiers (U3 art. 335). Après 150 jours sans information ni preuve de sortie, le bureau d'exportation peut invalider la déclaration (U2 art. 248 § 2) ; marchandises non sorties : invalidation immédiate (art. 248 § 3). | Pièces de preuve de sortie disponibles et manquantes, date de mainlevée ; aucune date limite restante calculée. |
| Conservation | Documents conservés au moins trois ans selon le CDU (U1 art. 51) et sous leur forme originale (F1 L. 221-1) ; registres du double usage cinq ans (U5 art. 27 § 3). | Dossier complet : facture, contrat, transport, déclaration, preuve de sortie. |

Une facture « hors taxes », une lettre de transport ou un bon de remise au
transporteur ne prouvent pas, à eux seuls, la sortie de l'Union : la fiche
dit quelle pièce manque et à qui la demander.

## 4. Produit, destination et usage final : vérifier avant de rester dans la tranche

La sortie entraîne l'application des mesures de prohibition ou de
restriction (sécurité, santé, environnement, biens culturels, propriété
intellectuelle, précurseurs, politique commerciale) (U1 art. 267 § 3 e). En
droit français, est prohibée toute marchandise dont l'exportation est
interdite ou soumise à restriction ou formalité particulière (F1 L. 231-1) ;
lorsqu'un document conditionne l'exportation, elle est prohibée sans ce
document (F1 L. 231-4). Ces repères justifient la recherche ; ils ne disent
pas qu'une mesure frappe un produit donné.

| Indice dans le récit | Qualification | Suite |
|---|---|---|
| Produit technique, électronique, logiciel, capteur, laser, drone, machine-outil, produit chimique, matériel de chiffrement, composant « industriel » sans précision | Bien à double usage possible : l'exportation des biens de l'annexe I est soumise à autorisation (U5 art. 3) ; un bien non listé l'est aussi si l'autorité a informé l'exportateur d'un usage préoccupant, et l'exportateur qui a connaissance d'un tel usage doit l'en informer (U5 art. 4 § 1-2). Le classement suit un ordre fixe et, en cas de doute, une demande au SBDU est possible (G6). | **Hors tranche** : réserve, compétence spécialisée (SBDU, conseil en contrôle export, avocat en droit douanier), aucune autorisation ni absence d'autorisation supposée. |
| Usage final militaire, sécuritaire, nucléaire, surveillance ; client lié à une armée ou à une administration ; refus de dire l'usage | Clause attrape-tout possible (U5 art. 4) ; matériels de guerre et autres catégories soumis à autorisation préalable (G7). | **Hors tranche** : même orientation. |
| Destination ou client dans un pays visé par des mesures restrictives ; réexpédition annoncée vers un tel pays ; paiement par un tiers d'un autre pays | Les mesures peuvent interdire l'exportation « directement ou indirectement » pour une utilisation dans un pays (U6 art. 2 § 1) et imposer aux exportateurs vers certains pays tiers une clause contractuelle interdisant la réexportation vers la Russie pour des biens listés (U6 art. 12 octies) ; la DG Trésor invite l'exportateur à identifier le code tarifaire et la sensibilité du bien et à saisir l'autorité compétente (G7). | **Hors tranche** : réserve, aucune liste de pays ni mesure citée de mémoire ; orientation vers l'autorité compétente et un avocat ; sanctions financières et banque : volet séparé. |
| Destination finale inconnue au-delà d'un transitaire, d'une plateforme ou d'un revendeur | Les mesures attachées à la destination et à l'usage final ne peuvent être vérifiées. | Réserve sur restrictions et formalités ; question ciblée sur la destination et l'utilisateur finals ; la fiche factuelle continue. |
| Couteaux et objets tranchants, matières animales ou végétales (bois exotique, corne, os, ivoire, cuir), aliments, plantes, cosmétiques, médicaments, alcools, emballages en bois | Exigences possibles au départ ou à l'arrivée selon le produit et le pays. | Désignation et matières exactes demandées ; DOU-014 (couteaux), DOU-015 (matières naturelles) proposées ; aucune admissibilité certifiée. |
| Bien ordinaire sans aucun de ces indices | La recherche reste à mener par code tarifaire et destination (TARIC T1, guide G7). | Rester dans la tranche, en disant que l'absence de mesure n'est pas établie ici : jamais « aucune autorisation n'est nécessaire ». |

Le droit et les formalités du pays de destination (admission du produit,
droits et taxes, normes, permis d'importation, enregistrement fiscal du
vendeur) ne sont pas traités : Access2Markets (T2) oriente, sans valeur de
règle ; questions à l'acheteur, à l'importateur ou au courtier local ;
DOU-017 proposée. Une conformité au marché français ou un marquage CE ne
prouvent pas l'admission à l'étranger.

Une fausse déclaration destinée à éluder une prohibition, ou une manœuvre
liée à la déclaration d'exportation pour obtenir un avantage de TVA, est
réputée exportation sans déclaration de marchandises prohibées (F1 L. 512-8
2° et 5°) ; l'exportation sans déclaration de biens à double usage soumis à
restriction est spécialement réprimée (F1 L. 513-2). Ces repères servent à
expliquer l'enjeu d'une vérification, jamais à attribuer une faute.

## 5. Origine, classement et valeur : ce qui reste à établir

| Inconnue | Repère lu | Ce qui fait avancer | Tâche |
|---|---|---|---|
| Classement tarifaire | Il conditionne les mesures et restrictions repérées dans TARIC (T1, G7). | Fiche technique, composition, fonction ; code du fabricant ou du transitaire seulement comme indice. | `tariff-classification-dossier` (DOU-006). |
| Origine | Un document prouvant l'origine peut être délivré selon les règles du pays de destination (U1 art. 61 § 3) ; préférence selon l'accord, non lue. | Lieu de fabrication, matières et fournisseurs, attestations. Aucune mention « origine France » improvisée. | DOU-007, DOU-016 proposées. |
| Valeur | Valeur statistique et valeur de facture non étudiées. | Facture, Incoterm et lieu, frais facturés. | Hors tâche. |

La fiche ne propose aucun code, origine, valeur, taux ni montant, même
indicatif.

## 6. TVA à l'exportation : axe séparé, non tranché

Les États membres exonèrent les livraisons de biens expédiés ou
transportés hors de l'Union par le vendeur ou pour son compte, ou par
l'acquéreur non établi ou pour son compte (U4 art. 146 § 1 a et b), dans
les conditions qu'ils fixent (U4 art. 131). La douane présente la mention de
sortie de la déclaration comme justificatif et renvoie, sans certification,
à des preuves alternatives auprès du bureau d'exportation ; elle cite
l'article 262 I du CGI et l'article 74 de l'annexe III, **non lus** ici
(guide G3). La fiche ne dit donc ni que l'exonération est acquise, ni
qu'elle est perdue ; elle relie la preuve de sortie disponible à la question
fiscale et oriente vers l'expert-comptable ou le service des impôts.
Statut de micro-entrepreneur ou absence de numéro de TVA : question au
service des impôts, sans règle ni montant. Un justificatif de transport seul
ne résout pas la TVA.

## 7. Pièces à réunir

Demander seulement ce qui fait avancer, identifiants masqués (garder les
derniers caractères) :

1. Entreprise : activité, lieu d'établissement, EORI et numéro de TVA
   masqués.
2. Vente : facture commerciale, bon de commande ou contrat, Incoterm,
   version et lieu désigné, conditions de paiement et payeur.
3. Acteurs : acheteur, destinataire, utilisateur final et pays de chacun ;
   transitaire ou représentant et mandat (type, champ, date).
4. Marchandise : désignation exacte, fiche technique, matières, usage,
   quantité, photos ; lieu de fabrication ; statut Union ou non Union.
5. Trajet : lieu de départ, mode de transport, pays traversés, port ou
   aéroport de sortie, destination finale, contrat de transport.
6. Déclaration : copie ou MRN de la déclaration d'exportation, avis de
   mainlevée, document d'accompagnement export.
7. Sortie : certification de sortie, ou preuves disponibles (bon de
   livraison signé à destination, document de la douane du pays tiers,
   preuve de paiement, document du transporteur).
8. Documents de contrôle éventuels : licence, autorisation, déclaration
   d'utilisation finale, certificats, avec leur auteur et leur date.
9. Acte de la douane reçu : texte intégral, sans réponse au fond
   (`customs-notice-review`).

Questions types, à adapter :

- Au représentant ou au transitaire : « Pour l'envoi [référence], qui
  dépose la déclaration d'exportation, en quel nom, en représentation
  directe ou indirecte ? Quel est le MRN, la date de mainlevée et le bureau
  de sortie prévu ? Qui recevra la certification de sortie et
  pouvez-vous me la transmettre ? Avez-vous vérifié si des mesures de
  restriction s'appliquent à ce produit et à cette destination, et sur
  quelle base ? »
- Au transporteur : « Avez-vous reçu le MRN ? Par quel point les
  marchandises quitteront-elles l'Union ? Quel document confirmant la
  sortie pourrez-vous fournir ? »
- À l'acheteur : « Quels sont le destinataire et l'utilisateur finals, le
  pays de destination finale et l'usage prévu ? Qui dédouane à l'arrivée ?
  Quelle preuve de livraison pourrez-vous signer ? »
- À la douane (service d'information, coordonnées sur le site officiel) :
  « Pour l'exportation définitive de [désignation] vers [pays], quelles
  formalités et quelles mesures de restriction s'appliquent, et comment
  obtenir la certification de sortie ? »

Séparer ces questions des **engagements contractuels** (Incoterm, qui
déclare, qui paie les frais, qui fournit la preuve de livraison, clause de
non-réexportation éventuelle), qui relèvent de la négociation ou d'un
conseil en contrats.

## 8. Signaux d'alerte propres à la tâche

- Indice de double usage, d'usage final sensible ou de sanction : sortie
  de tranche, réserve en tête, orientation spécialisée, aucune expédition
  conseillée en attendant.
- Client qui demande de facturer un autre pays, de livrer un transitaire
  pour réexpédition sans dire où, de payer par un tiers, ou de décrire le
  bien autrement : ne pas aider ; questions et orientation.
- Proposition de mentionner « échantillon », une valeur minorée, une
  origine improvisée ou une facture sans TVA sans preuve de sortie : ne pas
  aider ; avocat en droit douanier si c'est déjà fait.
- Marchandise déjà partie sans déclaration, ou sortie non confirmée depuis
  longtemps : renfort, représentant en douane, aucun délai restant calculé.
- Acte de la douane reçu (demande de preuve de sortie, contrôle,
  procès-verbal, retenue) : renfort en tête, `customs-notice-review`,
  avocat en droit douanier.

## Modèle de sortie

1. **En bref** : opération comprise ou à préciser, exportation définitive
   envisagée à confirmer, acteurs établis ou réservés, pièces manquantes,
   points de vérification produit, destination et usage final, prochaine
   étape ; réserve ou alerte en tête.
2. **Carte des acteurs et de l'opération** : vendeur, acheteur, exportateur
   au sens douanier, déclarant, représentant, transporteur, destinataire et
   utilisateur final, avec « pièce (auteur) », « déclaré », « source lue
   (repère) » ou « inconnu » ; trajet complet et destination finale.
3. **Pièces de vente, de transport et de sortie** : reçues, manquantes, à
   confirmer, avec la raison de chacune.
4. **Produit, destination et usage final : points à vérifier** ; tout
   indice sensible rend la conclusion réservée et oriente.
5. **Questions** au représentant, au transporteur, à l'acheteur ou à la
   douane, prêtes à copier, puis **engagements contractuels** séparés.
6. **TVA et destination** : questions séparées, sans conclusion.
7. **Sources et limites** : repères utilisés avec leur date de lecture,
   réserves, rien de déposé ni certifié ; puis la phrase finale :
   « Cette fiche aide à préparer le dossier de votre exportation ; elle ne
   remplace pas l'avis d'un avocat en droit douanier. »

## Interlocuteurs et orientations

La douane renseigne sur les formalités et les mesures ; le représentant
mandaté accomplit les formalités confiées et répond de ses opérations (F1
L. 522-2) ; le transporteur renseigne sur ses frais et la preuve de sortie
qu'il délivre ; le SBDU instruit les autorisations de biens à double usage
(G5, G6). Aucun n'est le conseil de l'entreprise. Conseil : avocat en droit
douanier pour un contrôle, une sortie non prouvée, une infraction, un volet
pénal ou une sanction internationale ; conseil en contrôle des exportations
pour un classement double usage ; conseil en contrats pour l'Incoterm et les
clauses ; expert-comptable ou service des impôts pour la TVA. Relais
proposés, non livrés : DOU-013 (calendrier de déclaration), DOU-014
(couteaux), DOU-015 (matières naturelles), DOU-016 (origine préférentielle),
DOU-017 (fiche pays), DOU-018 (retour SAV), DOU-019 (échantillons de
salon), DOU-007 (origine), domaine fiscal (DOM-011). Classement :
`tariff-classification-dossier`.
Ne jamais présenter une tâche proposée comme une commande disponible.

## Sources et relecture de maintenance

Textes lus le **20 octobre 2026**. Les consolidations de l'Union sont des
outils de documentation ; seules les publications au Journal officiel font
foi. Le Code des douanes recodifié (ordonnance n° 2026-265 du 8 avril 2026,
en vigueur le 1er mai 2026) a été lu dans sa publication au Journal officiel
du 11 avril 2026 (version non consolidée) ; pour des faits antérieurs au
1er mai 2026, la version de l'ancien code n'a pas été lue. Une page de guide
n'est pas la règle ; TARIC et Access2Markets sont des outils.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 5 (points 6, 10, 12 à 16, 22 à 24), 18, 19, 51, 61, 81, 155, 158, 170, 171, 172, 194, 203, 263, 267, 269, 270, 271, 272 et 274 lus. Dernière consolidation listée par CELLAR le 20 octobre 2026. | 2026-10-20 · inchangee · legal_sources.py eu, CELLAR · lecture de la tâche |
| U2 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Art. 1 point 19 (exportateur), 141, 142, 244, 245 et 248 lus ; reproduction CELLAR complète téléchargée directement. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture limitée aux passages cités |
| U3 — [Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2447-20260701) | Art. 221, 329 à 337 lus (bureau d'exportation, bureau de sortie, présentation, notification par le transporteur, certification de sortie, procédure de recherche et preuves, envois fractionnés, déclaration a posteriori). | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture limitée aux passages cités |
| U4 — [Directive 2006/112/CE (TVA), consolidée au 14.04.2025](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02006L0112-20250414) | Art. 131 et 146 lus. Transposition française non lue. | 2026-10-20 · inchangee · legal_sources.py eu, CELLAR · réserve : texte français non lu |
| U5 — [Règl. (UE) 2021/821 (biens à double usage), consolidé au 21.09.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02021R0821-20260921) | Art. 2 (points 1 à 3), 3, 4, 9, 10, 12 et 27 lus ; annexe I non consultée pour un produit. | 2026-10-20 · inchangee · legal_sources.py eu, CELLAR · détection seulement, aucun classement |
| U6 — [Règl. (UE) n° 833/2014 (mesures restrictives, Russie), consolidé au 24.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02014R0833-20260724) | Art. 2 § 1 et 12 octies § 1 lus, comme exemples de mesures attachées à la destination ou à l'utilisation indirecte ; annexes et autres régimes non lus. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · détection seulement |
| F1 — [Code des douanes, partie législative, annexe à l'ordonnance n° 2026-265 du 8 avril 2026, archive JORF du 11 avril 2026](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | L. 211-4, L. 221-1, L. 221-5, L. 231-1, L. 231-4, L. 426-1, L. 512-7, L. 512-8, L. 513-2, L. 522-1 et L. 522-2 lus. | 2026-10-20 · inchangee · DILA JORF, archive lue hors outil · réserve : version consolidée et ratification à suivre |
| G1 — [Douane, « Formalités à l'exportation, les notions essentielles »](https://www.douane.gouv.fr/fiche/formalites-lexportation-les-notions-essentielles) | Mise à jour le 23/11/2023 ; étapes de dépôt, mainlevée, sortie et certification électronique ; formalités vers les DOM ; cite encore l'ancien code communautaire. | 2026-10-20 · inchangee · outil web · guide ancien, à vérifier sur U1-U3 |
| G2 — [Douane, « S'assurer de la sortie effective des marchandises du territoire douanier de l'Union »](https://www.douane.gouv.fr/demarche/sassurer-de-la-sortie-effective-des-marchandises-du-territoire-douanier-de-lunion-une) | Page sans date ; l'exportateur reste responsable jusqu'à la sortie ; certification utile à la TVA. | 2026-10-20 · inchangee · outil web · guide |
| G3 — [Douane, « Bénéficier de l'exonération à la TVA à l'exportation »](https://www.douane.gouv.fr/demarche/beneficier-de-lexoneration-la-tva-lexportation) | Page sans date ; mention de sortie de la déclaration comme justificatif, preuves alternatives au bureau d'exportation, conservation ; cite CGI art. 262 I et annexe III art. 74, non lus. | 2026-10-20 · inchangee · outil web · guide, texte fiscal non lu |
| G4 — [Douane, « Les nouvelles règles Incoterms® 2020 et la valeur en douane »](https://www.douane.gouv.fr/les-nouvelles-regles-incotermsr-2020-et-la-valeur-en-douane) | Page sans date ; répartition contractuelle des frais, risques et formalités ; EXW et justificatifs de sortie ; ne désigne pas le déclarant. | 2026-10-20 · inchangee · outil web · guide, non opposable |
| G5 — [Douane, « Exporter des biens et technologies à double usage vers un pays tiers »](https://www.douane.gouv.fr/demarche/exporter-des-biens-et-technologies-double-usage-vers-un-pays-tiers) | Page sans date ; autorisation pour l'annexe I quel que soit le pays tiers, échantillons et envois non facturés compris ; SBDU de la DGE. | 2026-10-20 · inchangee · outil web · guide |
| G6 — [DGE, « Mon bien est-il à double usage ? »](https://www.entreprises.gouv.fr/espace-entreprises/s-informer-sur-la-reglementation/mon-bien-est-il-double-usage) | Mise à jour le 6 décembre 2024 ; ordre du classement, outils indicatifs, demande hors licence au SBDU en cas de doute ou de clause attrape-tout. | 2026-10-20 · inchangee · outil web · guide |
| G7 — [DG Trésor, « Votre bien ou votre service est-il visé par des interdictions ou des restrictions commerciales ? »](https://www.tresor.economie.gouv.fr/services-aux-entreprises/sanctions-economiques/votre-bien-ou-votre-service-est-il-vise-par-des-interdictions-ou-des-restrictions-commerciales) | Publiée le 18 juillet 2025 ; code tarifaire, catégories sensibles et autorités compétentes. | 2026-10-20 · inchangee · outil web · guide, mesures à revérifier à la date des faits |
| T1 — [Commission européenne, consultation TARIC](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp?Lang=fr) | Recherche des mesures par code, zone d'origine ou de destination et date ; données d'une date future possiblement incomplètes. | 2026-10-20 · inchangee · outil web · outil, aucun produit consulté |
| T2 — [Commission européenne, Access2Markets](https://trade.ec.europa.eu/access-to-markets/fr/home) | Version 2026.10.1.3 du 14 octobre 2026 ; conditions d'échange et règles d'origine par produit et marché. | 2026-10-20 · inchangee · outil web · outil, aucun produit ni pays consulté |

Non lus : règles Incoterms (Chambre de commerce internationale), CGI art.
262 I et annexe III art. 74, doctrine fiscale, annexe I du règlement
2021/821 et listes nationales, autres régimes de sanctions et annexes du
règlement 833/2014, carte des sanctions de l'Union (page JavaScript non
restituée), Code de la défense (matériels de guerre), règles du pays de
destination, ancien Code des douanes pour des faits antérieurs au 1er mai
2026. Pendant une réponse, relire les sources utiles si un outil de lecture
existe et vérifier la version à la date des faits. Sans lecture possible,
citer les repères ci-dessus avec leur date de maintenance et leur limite
(méthode, section 10.6), et garder la fiche factuelle complète : aucune
règle de mémoire, aucun taux, montant, code, seuil appliqué, franchise,
délai restant ni formalité obligatoire déduit d'une allégation.
