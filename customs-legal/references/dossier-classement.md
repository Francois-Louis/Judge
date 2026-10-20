# Préparer un dossier de classement tarifaire

Version `1.0.1` — 20 octobre 2026 (Europe/Paris), DOU-006 ; relais de
l'origine mis à jour par DOU-007.
Méthode métier, repères datés et modèle de sortie pour une personne
(professionnel le plus souvent, particulier possible) qui veut réunir les
éléments nécessaires à l'examen du classement tarifaire d'une marchandise
dans la nomenclature de l'Union : fiche technique structurée, attributs
manquants, questions soulevées par un code proposé, contrôle d'une décision
fournie et voie officielle de renseignement. Elle n'arrête aucun code, ne
calcule ni droit ni taxe, ne dépose aucune demande et ne remplace pas
l'analyse d'un laboratoire.

## Périmètre de la tâche

**Inclus** : une marchandise (ou un ensemble présenté ensemble) à importer,
à exporter ou déjà déclarée, avec ou sans code proposé par un vendeur, un
transitaire, un transporteur, un outil ou une ancienne déclaration ; une
décision de renseignement tarifaire contraignant (RTC) fournie à contrôler.
Résultat : fiche produit, attributs techniques manquants, comparaison
motivée des questions soulevées par le code proposé, sources et voie
officielle de renseignement à vérifier, sans code arrêté.

**Exclus** : code garanti ou « le bon code », demande de RTC remplie ou
déposée (tâche à découper), taux, droits, taxes ou montant, mesures TARIC
appliquées au cas, origine (`goods-origin-dossier`) et valeur (DOU-008 proposée)
arrêtées, expertise de laboratoire, contestation d'un classement retenu par
la douane, rectification d'une déclaration, admissibilité ou transport d'un
produit réglementé (couteau : DOU-014 proposée). Leur détection est incluse,
leur traitement non. Formalités de l'opération : `commercial-import-intake`,
`export-document-preparation`, `import-document-checklist`,
`traveller-goods-documents`, `overseas-shipment-documents` ; acte de la
douane reçu : `customs-notice-review`.

## 1. Ce que « classer » veut dire

Classer une marchandise, c'est déterminer la sous-position de la
nomenclature combinée (NC) ou d'une nomenclature qui la reprend dans
laquelle elle doit être classée (U1 art. 57 § 1-2) ; cette sous-position
sert à appliquer les mesures qui lui sont liées (U1 art. 57 § 3). Les droits
à l'importation ou à l'exportation reposent sur le tarif douanier commun, et
d'autres mesures de l'Union sont appliquées selon le classement (U1 art. 56
§ 1-2).

| Niveau | Repère lu | Effet pour la fiche |
|---|---|---|
| Système harmonisé (SH), 6 chiffres | Les six premiers chiffres d'un code NC sont ceux des positions et sous-positions du SH (N1 art. 3 § 1 a). | Seuls ces six chiffres sont communs à d'autres pays utilisant le SH (G4) ; un code étranger plus long n'est pas une sous-position NC. |
| Nomenclature combinée, 8 chiffres | Établie par la Commission, figure à l'annexe I avec les taux (N1 art. 1) ; 7e et 8e chiffres = sous-positions NC (N1 art. 3 § 1 b). | Le code à 8 chiffres se lit dans la version de l'année des faits. |
| TARIC, 10 chiffres et codes additionnels | Repose sur la NC et reprend les mesures de l'Union (N1 art. 2, 3 § 2-3, 5) ; codes additionnels nationaux (CANA) consultables dans RITA (G4). | Les mesures attachées à un code ne sont pas appliquées ici : elles se vérifient dans TARIC ou RITA, à la date et pour l'origine, par le représentant ou la douane. |

**Version annuelle.** La Commission adopte chaque année un règlement
reprenant la version complète de la NC, publié au plus tard le 31 octobre
et applicable au 1er janvier suivant (N1 art. 12 § 1). La NC applicable en
2026 est celle de l'annexe I consolidée au 1er janvier 2026 (règlement
d'exécution (UE) 2025/1926 du 22 septembre 2025). La version de 2027 n'avait
pas été trouvée lors de la recherche du 20 octobre 2026 : pour des faits de
2027, la version est à rechercher. Un code valable une année peut ne plus
exister ou ne plus viser le même produit l'année suivante.

Classement, origine et valeur sont trois questions distinctes (G4) : la
fiche ne déduit ni l'origine du code, ni la valeur du classement.

## 2. Ce qui fait foi et ce qui aide seulement

| Élément | Valeur | Usage dans la fiche |
|---|---|---|
| Libellés des positions et notes de sections ou de chapitres | Le classement est déterminé légalement d'après ces termes ; les titres de sections et de chapitres n'ont qu'une valeur indicative (N1 annexe I, première partie, titre I A, règle 1). | Lire d'abord le texte de la position et les notes de section et de chapitre, à la version de l'année. |
| Règles générales interprétatives (RGI 1 à 6) | Font partie de la NC (N1 annexe I, titre I A). | Méthode d'examen, section 3. |
| Règlements de classement de la Commission | Mesures adoptées pour déterminer le classement de marchandises (U1 art. 57 § 4) ; présentés par la douane comme ayant force légale (G3, G4). | À rechercher pour la marchandise : un règlement visant un produit voisin n'est pas transposé, ses motifs se citent comme indice. |
| Décision RTC | Contraignante seulement entre les autorités et son **titulaire**, pour les marchandises décrites (U1 art. 33 § 2) ; un opérateur ne peut pas utiliser un RTC dont il n'est pas titulaire (G1). | Section 5. Une décision d'un autre titulaire, trouvée dans la base EBTI (T2), est un indice à citer, jamais une règle pour la personne. |
| Notes explicatives de la NC (NENC) | Adoptées par la Commission (N1 art. 9 § 1 a) ; complémentaires des notes du SH et à consulter avec elles (N2, préface) ; instrument d'interprétation sans force légale selon la douane (G3, G4). | Citer la note lue, avec sa publication ; elle aide à interpréter, elle ne remplace pas le texte. |
| Notes explicatives du SH (NESH) et avis de classement de l'Organisation mondiale des douanes | Sans force légale selon la douane (G3, G4) ; publiées par l'OMD, accès complet sur abonnement (G2). | Non lues : ne pas les citer de mémoire ; demander au représentant ou à la douane s'il s'y réfère. |
| TARIC, RITA, Access2Markets, base EBTI | Outils de consultation (T1 à T3, G2) ; RITA ne dispense pas de consulter les bases légales (G2). | Un résultat d'outil est un indice daté, jamais une décision. |
| Code du vendeur, du fabricant, du transporteur, d'une ancienne déclaration ou d'un logiciel | Aucune valeur propre. | Indice à contrôler (section 4) ; noter qui l'a donné, quand, pour quelle version et sur quelles pièces. |

## 3. Méthode d'examen : les règles générales comme questionnaire

Les RGI se lisent dans l'ordre ; on ne passe à la suivante que si la
précédente ne permet pas de classer (N1 annexe I, titre I A). La fiche s'en
sert pour **identifier les faits qui décident**, jamais pour conclure à la
place de la douane. Hors des passages lus ci-dessous, aucune position, aucun
chapitre ni aucune catégorie du tarif n'est nommé, même sans numéro ou comme
« piste » : les positions concurrentes restent « à identifier en lisant le
texte » à partir des attributs documentés.

| Règle (texte lu) | Question à poser sur la marchandise |
|---|---|
| RGI 1 : titres indicatifs ; classement d'après les termes des positions et des notes. | Quelles positions emploient des termes qui couvrent le produit ? Quelle note de section ou de chapitre l'inclut ou l'exclut ? |
| RGI 2 a : article incomplet ou non fini présentant les caractéristiques essentielles de l'article fini ; article démonté ou non monté. | Le produit est-il complet, fini, démonté ? Que manque-t-il ? |
| RGI 2 b : une matière mentionnée couvre la matière pure, mélangée ou associée ; les ouvrages composites relèvent de la règle 3. | Quelles matières, en quelles proportions ? |
| RGI 3 a : position la plus spécifique ; positions également spécifiques si chacune ne vise qu'une partie des matières ou des articles d'un assortiment. | Quelles positions concurrentes, et lesquelles ne visent qu'une partie du produit ? |
| RGI 3 b : produits mélangés, ouvrages composites et assortiments conditionnés pour la vente au détail classés d'après la matière ou l'article qui leur confère leur caractère essentiel, lorsqu'on peut le déterminer. | Quel composant joue le rôle principal ? Proportions en poids et en valeur, fonction de chaque élément, présentation ensemble à la vente. La règle ne définit pas le caractère essentiel : ne pas énoncer de critère de mémoire. |
| RGI 3 c : à défaut, dernière position par ordre de numérotation parmi celles valablement envisageables. | Ne s'applique qu'après échec de 3 a et 3 b : le signaler, sans l'appliquer à la place de la douane. |
| RGI 4 : articles les plus analogues. | Produit sans équivalent : demander l'avis de la douane. |
| RGI 5 a et b : étuis et contenants spécialement aménagés, emballages. | L'étui, le coffret ou l'emballage est-il vendu avec le produit, réutilisable, ou confère-t-il le caractère essentiel ? |
| RGI 6 : sous-positions comparées seulement au même niveau, d'après leurs termes et les notes de sous-positions. | Quel attribut distingue les sous-positions voisines (matière, dimension, puissance, mécanisme, usage) ? Est-il documenté ? |

**Exemple de lecture, chapitre 82 (NC 2026).** La note 1 du chapitre limite
celui-ci, sauf exceptions, aux articles pourvus d'une lame ou d'une partie
travaillante en métal commun, en carbures métalliques ou cermets, en pierres
gemmes ou matières abrasives sur support métallique ; la note 3 classe dans
la position 8215 les assortiments d'un ou plusieurs couteaux du 8211 et d'un
nombre au moins égal d'articles du 8215. Dans la position 8211, les
sous-positions distinguent les couteaux de table à lame fixe, les autres
couteaux à lame fixe et les couteaux autres qu'à lame fixe, y compris les
serpettes fermantes (N1 annexe I, chapitre 82). Pour un couteau, la matière
de la lame, le mécanisme (lame fixe, pliante, à ouverture assistée ou
automatique) et la présentation en assortiment sont donc des attributs à
documenter avant toute discussion de code. « Outil » ou « metal tool » sur
une facture ne range pas à lui seul une marchandise dans ce chapitre, et le
classement ne dit rien de l'admissibilité ou du port d'un couteau (DOU-014
proposée). Ce passage illustre la lecture ; il ne classe aucun produit.

## 4. La fiche technique : attributs à réunir

Chaque ligne indique la valeur, son statut (« pièce (auteur) », « déclaré »,
« source lue (repère) » ou « inconnu ») et la pièce qui la ferait avancer.

| Attribut | Pourquoi il compte | Pièce utile |
|---|---|---|
| Désignation précise, nom commercial, référence fabricant | Le nom commercial ne fixe pas l'espèce tarifaire (G4) ; la désignation doit permettre de reconnaître la marchandise (U2 annexe A, E.D. 35 01 020, colonne RTC). | Fiche produit, catalogue. |
| Matières et composition, proportions en poids et en valeur | RGI 2 b et 3 ; certaines positions dépendent de la matière. | Fiche technique, nomenclature des composants, fiche de données de sécurité, certificat d'analyse existant. |
| Fonction principale et fonctions secondaires | Termes des positions ; caractère essentiel d'un ensemble (RGI 3 b). | Notice, mode d'emploi, schéma fonctionnel. |
| Usage prévu et utilisateur | Certaines positions visent un usage ; une destination particulière ne se suppose pas. | Fiche produit, description commerciale, contrat. |
| Mode de fonctionnement, mécanisme, alimentation | Distingue souvent les sous-positions (RGI 6). | Notice, schéma, photos de détail. |
| Présentation : unitaire, assortiment, kit, démonté, conditionnement, étui | RGI 2 a, 3 b, 5. | Photos de l'emballage de vente, liste du contenu. |
| État : neuf, usagé, fini, semi-fini, pièce détachée | RGI 2 a ; parties classées avec l'article ou spécialement dénommées selon les notes. | Facture, photos. |
| Dimensions, poids, puissance, capacité, autres caractéristiques chiffrées | Critères de certaines sous-positions. | Fiche technique. |
| Quantité, date et opération (import, export, usage) | Version de la NC à la date des faits ; RTC seulement pour une utilisation prévue (U1 art. 33 § 1 b). | Facture, commande, date prévue de déclaration. |
| Code proposé, son auteur, sa date et la version visée | Indice à contrôler (section 2). | Facture, échange avec le vendeur ou le transitaire, ancienne déclaration. |
| Décision RTC ou autre décision fournie | Section 5. | Texte intégral de la décision. |

Demander les seules pièces utiles ; masquer les données superflues (prix
détaillés, noms de clients) sauf si elles sont l'attribut lui-même. Une
analyse de laboratoire, un prélèvement ou un échantillon relèvent de la
douane ou d'un laboratoire ; la fiche indique seulement si le classement
semble en dépendre (U1 art. 188 d ; U2 annexe A, E.D. 35 01 020 et 38 04,
colonne RTC).

## 5. Code proposé et décision fournie : contrôler sans transposer

**Code proposé.** Comparer, sans trancher :

1. provenance (vendeur, fabricant, transitaire, transporteur, logiciel,
   ancienne déclaration), date et version de la NC visée ;
2. nombre de chiffres et pays du tarif (6 chiffres SH, 8 NC, 10 TARIC ; code
   d'un tarif étranger) ;
3. texte de la position et notes lus pour ce code, et positions voisines
   que les mêmes faits pourraient viser ;
4. attribut qui sépare ce code des voisins et pièce qui le documente ;
5. questions qui restent ouvertes.

Présenter « ce que le code suppose » et « ce que les pièces montrent », pas
un verdict. Une concordance apparente ne valide pas le code ; une
discordance ne prouve pas l'erreur : elle appelle une question.

**Décision RTC fournie.** Vérifier sur le texte intégral, sans l'étendre :

| Point | Repère lu | Question |
|---|---|---|
| Titulaire | Contraignante pour les autorités vis-à-vis du titulaire et pour le titulaire (U1 art. 33 § 2) ; on ne peut utiliser un RTC dont on n'est pas titulaire (G1). | La personne est-elle le titulaire ? Sinon, la décision n'est qu'un indice. |
| Marchandise | Contraignante pour les marchandises décrites ; en régime particulier, preuve qu'elles correspondent « à tous égards » (U1 art. 33 § 2, § 4 a). | Le produit actuel est-il identique (matière, fonction, présentation, référence) ? Toute différence est listée. |
| Date d'effet et validité | Valable trois ans à compter de sa prise d'effet (U1 art. 33 § 3). | Date d'effet lue sur la décision ; durée restante non calculée ici. |
| Fin anticipée | Cesse d'être valable si une modification de la nomenclature ou un règlement de classement la rend non conforme (U1 art. 34 § 1) ; révoquée après des notes explicatives, un arrêt de la Cour de justice ou une décision de l'OMD incompatibles (art. 34 § 7) ; annulée si fondée sur des informations inexactes ou incomplètes du demandeur (art. 34 § 4) ; jamais modifiée (art. 34 § 6). | La nomenclature a-t-elle changé depuis ? La décision figure-t-elle encore comme valable dans EBTI (T2) ? Question au représentant ou au pôle RTC. |
| Utilisation prolongée | Possible pour des contrats fermes conclus avant la fin de validité, sur demande dans un délai fixé (U1 art. 34 § 9 ; U3 art. 22). | Signaler seulement que la question existe ; aucun délai calculé. |
| Mention sur la déclaration | Numéro de référence de la décision indiqué dans la déclaration (U3 art. 20). | Le représentant l'a-t-il reporté ? |
| Export | Non directement opposable aux administrations des pays tiers (G1). | Classement à destination : question à l'acheteur ou au courtier local. |

Une **ancienne décision sur un produit voisin** (autre titulaire, autre
référence, autre version de la NC) ne se transpose pas : relever ce qui
diffère et poser la question.

## 6. Voie officielle de renseignement : la préparer, ne pas la déposer

La douane prend sur demande des décisions RTC (U1 art. 33 § 1). La demande
fournit les informations nécessaires (U1 art. 22 § 1) ; elle est déposée
auprès de l'autorité de l'État membre d'établissement ou de celui où la
décision doit être utilisée (U2 art. 19 § 1). Elle n'est pas acceptée si le
demandeur est déjà titulaire d'une décision pour les mêmes marchandises, ou
si elle ne correspond à aucune utilisation prévue (U1 art. 33 § 1). Une
demande ne vise que des marchandises dont les différences sont sans
pertinence pour le classement (U3 art. 16 § 2). Le demandeur consent à la
publication des données de la décision, sauf informations confidentielles
(U2 art. 19 § 2). Le formulaire demande notamment le code attendu, une
description détaillée permettant le classement, la composition et les
méthodes d'examen si le classement en dépend, les échantillons, photos ou
brochures fournis, et les décisions détenues ou connues pour des
marchandises identiques ou similaires (U2 annexe A, E.D. 32 01, 32 02,
35 01 010, 35 01 020 et 38 04, colonne RTC). Délais généraux : acceptation
vérifiée dans les trente jours, décision dans les cent vingt jours suivant
l'acceptation, sauf dispositions contraires (U1 art. 22 § 2-3 ; U2 art. 20) :
ils ne se calculent pas ici.

Guides de la douane (G1, G5) : demande en ligne dans le service EBTI depuis
le 15 octobre 2024, compte certifié et habilitation, EORI au format SIREN
pour les nouvelles demandes depuis le 11 juin 2025, documents en français,
gratuité, pôle RTC de la douane à Metz (CSMR ou SND2R selon les pages).
Coordonnées sur le site officiel, jamais de mémoire.

Hors RTC : service d'information de la douane pour une question générale,
représentant en douane pour son propre classement, conseiller de la douane
aux entreprises (G2). Leur réponse n'est pas une décision RTC.

La fiche peut lister les pièces d'une future demande ; elle ne remplit ni ne
dépose le formulaire (tâche à découper).

## 7. Signaux d'alerte

- **Proposition de choisir un code « plus avantageux » ou de décrire le
  produit autrement** pour échapper à un droit, une mesure ou une
  restriction : ne pas aider. La déclaration ou la demande rend son auteur
  responsable de l'exactitude des renseignements (U1 art. 15 § 2) ; la
  fausse déclaration dans l'espèce, la valeur ou l'origine, lorsqu'un droit
  ou une taxe s'en trouve éludé ou compromis, est une contravention (F1
  R. 515-5, 2°). Avocat en droit douanier si c'est déjà fait.
- **Acte de la douane reçu** (contrôle, demande de pièces, résultat
  d'analyse, avis de classement retenu, notification de dette) : renfort en
  tête, `customs-notice-review`, avocat en droit douanier ; aucune réponse
  au fond.
- **Opérations répétées sur un même produit au code incertain** : signaler
  l'intérêt d'une question à la douane ou d'un RTC, sans le déposer.
- **Produit sensible** (arme, couteau, double usage, produit chimique,
  médicament, aliment, végétal, animal) : le classement ne dit rien de
  l'autorisation ; volet réglementé orienté selon la qualification commune.
  Hors de cette liste, ne jamais affirmer qu'un produit n'est pas sensible
  ou n'est soumis à aucune mesure : la question reste posée au
  représentant ou au service compétent.

## 8. Pièces à réunir et questions types

1. Désignation, référence et fiche technique du fabricant.
2. Composition et proportions ; fiche de données de sécurité si produit
   chimique.
3. Notice, schéma fonctionnel, photos d'ensemble, de détail et de
   l'emballage de vente.
4. Code proposé et son auteur (facture, courriel, ancienne déclaration).
5. Décision RTC ou autre décision fournie, texte intégral.
6. Date prévue de l'opération et sens (import, export).

Questions, à adapter :

- Au fabricant ou au vendeur : « Pour [référence], pouvez-vous fournir la
  composition en pourcentage du poids et de la valeur, la fonction
  principale, le mécanisme et une photo de l'emballage de vente ? Sur
  quelle base avez-vous indiqué le code [code], pour quel pays et quelle
  année ? »
- Au représentant ou au transitaire : « Quel code avez-vous retenu (ou
  retiendrez-vous) pour [référence], sur quels texte de position, notes et
  pièces ? Avez-vous consulté un règlement de classement ou une décision
  RTC ? »
- À la douane (service d'information ou pôle RTC, coordonnées sur le site
  officiel) : « Pour [désignation, composition, fonction], quelles positions
  sont à examiner et quelles pièces faut-il pour une demande de RTC ? »

## Modèle de sortie

1. **En bref** : marchandise et opération comprises, état du dossier
   (attributs réunis, manquants), code proposé et sa provenance, décision
   fournie, prochaine étape ; aucun code arrêté ; alerte éventuelle en tête.
2. **Fiche produit** : tableau attribut, valeur, statut (« pièce
   (auteur) », « déclaré », « source lue (repère) », « inconnu ») et pièce
   qui ferait avancer.
3. **Attributs techniques manquants**, du plus décisif au moins décisif,
   chacun relié à sa pièce et à son interlocuteur.
4. **Code proposé : questions soulevées** : provenance, version, texte et
   notes à lire, positions voisines, attribut séparateur documenté ou non ;
   « ce que le code suppose » face à « ce que les pièces montrent ».
5. **Décision fournie** (si présente) : titulaire, marchandise, date d'effet,
   fin anticipée possible, portée ; ce qui ne se transpose pas.
6. **Voie officielle de renseignement** : RTC (pièces d'une future demande,
   non déposée), service d'information, représentant ; classement, origine
   et valeur séparés.
7. **Questions** prêtes à copier, par destinataire.
8. **Sources et limites** : repères lus et leur date, version de la NC,
   réserves, rien de déposé ni calculé ; puis la phrase finale :
   « Cette fiche aide à préparer le dossier de classement de votre
   marchandise ; elle ne remplace pas l'avis d'un avocat en droit
   douanier. »

## Interlocuteurs et orientations

La douane renseigne sur le classement et délivre les RTC ; le représentant
mandaté retient un code pour les déclarations qu'il dépose et répond de ses
opérations ; le fabricant détient les données techniques. Aucun n'est le
conseil de la personne. Conseil : avocat en droit douanier pour un
contrôle, une contestation du classement retenu par la douane, un
contentieux ou un volet pénal. Origine : `goods-origin-dossier`. Relais
proposés, non livrés : DOU-008 (valeur), DOU-014 (admissibilité d'un couteau à
destination), demande de RTC et rectification (tâches à découper). Ne
jamais présenter une tâche proposée comme une commande disponible.

## Sources et relecture de maintenance

Textes lus le **20 octobre 2026**. Les consolidations de l'Union sont des
outils de documentation ; seules les publications au Journal officiel font
foi. Le Code des douanes recodifié, en vigueur depuis le 1er mai 2026, a été
lu dans sa publication au Journal officiel du 11 avril 2026 ; pour des faits
antérieurs, la version de l'ancien code est à rechercher. Une page de guide
n'est pas la règle ; TARIC, RITA, Access2Markets et la base EBTI sont des
outils de consultation.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| N1 — [Règl. (CEE) n° 2658/87 (nomenclature tarifaire et statistique, tarif douanier commun), consolidé au 01.01.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:01987R2658-20260101) | Art. 1, 2, 3, 5, 9, 12 ; annexe I, première partie, titre I A (règles générales 1 à 6) ; section XV, notes 1 et 2 ; chapitre 82, notes 1 à 3 et position 8211 lus. Annexe I de 2026 issue du règlement d'exécution (UE) 2025/1926 ; reproduction CELLAR de 22,5 Mo téléchargée directement. Version 2027 non trouvée le 20 octobre 2026. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · version de l'année des faits à vérifier |
| N2 — [Notes explicatives de la nomenclature combinée, JOUE C 119 du 29.3.2019](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:52019XC0329%2802%29) | Préface lue (adoption au titre de l'art. 9 de N1, complémentarité avec les notes du SH, notes publiées après le 4 janvier 2019 restant en vigueur hors de cette édition) ; chapitre 82 parcouru, aucune note sur la position 8211. Notes ultérieures non recensées. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · réserve : notes publiées depuis 2019 non lues |
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 15, 22, 23, 27, 28, 33, 34, 56, 57 et 188 lus. Dernière consolidation listée ; réforme ultérieure à rechercher à la date des faits. | 2026-10-20 · inchangee · legal_sources.py eu, CELLAR · lecture de la tâche |
| U2 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Art. 19 à 22 ; annexe A, notes des E.D. 31 02, 32 01, 32 02, 35 01 010, 35 01 020 et 38 04 pour la colonne RTC lues ; reproduction CELLAR de 29,6 Mo. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture limitée aux passages cités |
| U3 — [Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2447-20260701) | Art. 16 à 23 lus (demande, cohérence, mention sur la déclaration, système RTC, utilisation prolongée, suspension) ; reproduction CELLAR de 42 Mo. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture limitée aux passages cités |
| F1 — [Code des douanes, partie réglementaire, annexe au décret n° 2026-266 du 8 avril 2026, archive JORF du 11 avril 2026](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | R. 515-5 lu (2° : fausse déclaration dans l'espèce, la valeur ou l'origine). Parties législative et réglementaire parcourues sur « classement tarifaire », « renseignement tarifaire » et « espèce » : aucune autre disposition propre au classement relevée. | 2026-10-20 · inchangee · DILA JORF, archive lue hors outil · réserve : version consolidée non lue |
| G1 — [Douane, « Obtenir un renseignement tarifaire contraignant (RTC) pour sécuriser votre nomenclature »](https://www.douane.gouv.fr/demarche/obtenir-un-renseignement-tarifaire-contraignant-rtc-pour-securiser-votre-nomenclature) | Page sans date ; contenu de la demande, échantillons, français, gratuité, validité, portée pour le titulaire, export non opposable aux pays tiers ; réponses de valeur indicative. | 2026-10-20 · inchangee · outil web · guide, non opposable |
| G2 — [Douane, « Connaître la nomenclature de votre marchandise »](https://www.douane.gouv.fr/demarche/connaitre-la-nomenclature-de-votre-marchandise) | Page sans date ; espèce tarifaire, SH, NC, TARIC, RITA (ne dispense pas des bases légales), EBTI, NESH sur abonnement, service d'information. | 2026-10-20 · inchangee · outil web · guide |
| G3 — [Douane, « Informations et aides complémentaires à l'encyclopédie tarifaire RITA »](https://www.douane.gouv.fr/fiche/informations-et-aides-complementaires-lencyclopedie-tarifaire-rita) | Mise à jour le 13/10/2026 ; NESH et avis de l'OMD sans force légale ; NENC instrument d'interprétation ; règlements de classement ayant force légale. | 2026-10-20 · inchangee · outil web · guide |
| G4 — [Douane, « Espèce tarifaire des marchandises »](https://www.douane.gouv.fr/fiche/espece-tarifaire-des-marchandises) | Mise à jour le 24/04/2026 ; définition de l'espèce tarifaire, structure SH/NC/TARIC, CANA, valeur des notes. | 2026-10-20 · inchangee · outil web · guide |
| G5 — [Douane, service en ligne « EBTI »](https://www.douane.gouv.fr/service-en-ligne/ebti) | Mise à jour le 29/09/2026 ; dépôt dans EBTI depuis le 15 octobre 2024, EORI SIREN pour les nouvelles demandes depuis le 11 juin 2025, compte certifié et habilitation. | 2026-10-20 · inchangee · outil web · guide, conditions à revérifier |
| T1 — [Commission européenne, consultation TARIC](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp?Lang=fr) | Outil de consultation par code, origine et date ; aucun produit consulté. | 2026-10-20 · inchangee · outil web · outil |
| T2 — [Commission européenne, consultation des RTC (EBTI)](https://ec.europa.eu/taxation_customs/dds2/ebti/ebti_consultation.jsp?Lang=fr) | Recherche par code, mots clés, pays, validité ; option d'inclure les RTC non valides ; aucun avertissement juridique restitué. | 2026-10-20 · inchangee · outil web · outil, aucun produit consulté |
| T3 — [Commission européenne, Access2Markets](https://trade.ec.europa.eu/access-to-markets/fr/home) | Version 2026.10.1.3 du 14 octobre 2026 ; recherche des conditions d'échange et des règles d'origine par produit ; aucun produit consulté. | 2026-10-20 · inchangee · outil web · outil |

Non lus : notes explicatives et avis de classement de l'OMD (abonnement),
notes explicatives de la NC publiées depuis le 29 mars 2019, règlements de
classement de la Commission pour un produit donné, jurisprudence de la Cour
de justice sur le classement, nomenclature de 2027, ancien Code des douanes
pour des faits antérieurs au 1er mai 2026, voies de recours contre une
décision RTC. Pendant une réponse, relire les sources utiles si un outil de
lecture existe et vérifier la version à la date des faits. Sans lecture
possible, citer les repères ci-dessus avec leur date de maintenance et leur
limite (méthode, sections 5 et 10.6), et garder la fiche factuelle complète :
aucun code arrêté, aucune règle de mémoire, aucun taux, montant, mesure,
franchise, délai ni formalité obligatoire déduit d'une allégation.
