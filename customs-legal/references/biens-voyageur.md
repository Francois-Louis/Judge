# Biens accompagnant un voyageur à l'arrivée en France métropolitaine

Version `1.0.1` — 19 octobre 2026 (Europe/Paris), DOU-003 ; relais de
l'importation commerciale mis à jour par DOU-004.
Méthode métier, repères datés et modèle de sortie pour un voyageur majeur
qui prépare les pièces des biens ordinaires qu'il transporte avec lui, pour
son usage privé, en arrivant en France métropolitaine d'un pays tiers ou
d'un territoire où la TVA de l'Union ne s'applique pas. Elle ne calcule ni
droits ni taxes, n'accorde ni ne refuse aucune franchise, ne remplit aucune
déclaration et ne dit jamais qu'il n'y a « rien à déclarer ».

## Périmètre de la tâche

**Inclus** : une personne majeure, des biens ordinaires dans ses bagages
(à main, de soute, y compris un bagage enregistré comme accompagné et
présenté plus tard), achetés pendant le voyage, reçus en cadeau ou déjà
détenus avant le départ, pour son usage personnel ou familial ou pour être
offerts ; un trajet vers la métropole. Résultat : fiche trajet et qualité,
inventaire documenté, questions sur le régime et pièces manquantes,
interlocuteur douanier à confirmer.

**Exclus** : voyageur mineur et biens d'un mineur, franchise chiffrée
appliquée à un inventaire, déménagement ou transfert de résidence, biens
recueillis par succession ou liés à un mariage, véhicule (DOU-012), achat
pour une activité ou la revente (`commercial-import-intake`), colis ou fret envoyé à part
(`import-document-checklist`, `overseas-shipment-documents`), voyage depuis
un autre État membre, produits réglementés et soumis à accise, argent
liquide, infraction, acte de la douane déjà remis (`customs-notice-review`),
déclaration déposée, paiement et réclamation. Leur détection est incluse,
leur traitement non.

## 1. Fixer le trajet et la provenance

Demander, sans les déduire : pays ou territoire de départ ; escales et
correspondances, avec l'aéroport, le port ou le point de passage par lequel
le voyageur entre dans l'Union ; lieu et date d'arrivée en métropole ; mode
de transport (avion ou bateau de ligne, train, voiture, autre) ; bagages
enregistrés jusqu'à quel aéroport. La langue de la facture, la devise ou le
pays du vendeur ne fixent ni la provenance, ni le régime, ni le juge.

| Provenance | Repères lus | Effet sur la fiche |
|---|---|---|
| Pays tiers (hors Union) | Franchise de TVA pour les marchandises des bagages personnels des voyageurs en provenance d'un pays tiers (U2 art. 1, 4 ; F2 10°) ; franchise de droits de douane si l'importation est exonérée de TVA selon ces dispositions (U3 art. 41, al. 1). | Fiche complète ; conditions à vérifier bien par bien. |
| Territoire d'un État membre où la directive TVA ne s'applique pas (Canaries, départements d'outre-mer…) | La directive vise aussi les voyageurs venant d'un « territoire où les dispositions communautaires sur la TVA ou les droits d'accises ne sont pas d'application » (U2 art. 1, art. 3 point 2). U3 art. 41, al. 2 soumet aux mêmes dispositions de franchise de droits les marchandises importées dans les territoires de l'art. 6 § 1 de la directive TVA. Le guide G2 indique : pas de droits de douane, TVA au-delà des mêmes seuils. | Axe douanier et axe fiscal séparés ; le territoire est nommé exactement ; F2 10° vise les « pays tiers » : son application à ces provenances est à confirmer. Un départ d'un département d'outre-mer : repères de statut de `envoi-outre-mer.md`, sans règle d'envoi. |
| Autre État membre de l'Union | Hors du champ de la directive 2007/74 (U2 art. 1). | Hors tâche ; alcools et tabacs relèvent d'autres règles, non lues. |

**Transit et correspondances.** Si le voyage passe par un pays tiers ou part
d'un territoire visé ci-dessus, la directive s'applique sauf si le voyageur
justifie que les biens ont été acquis aux conditions générales d'imposition
d'un État membre sans remboursement de TVA ou d'accises ; un simple survol
n'est pas un transit (U2 art. 2). Pour un vol venant d'un pays tiers avec
correspondance dans l'Union, les contrôles des **bagages à main** ont lieu
au premier aéroport international de l'Union, ceux des **bagages de soute**
transbordés au dernier aéroport où arrive le vol intra-Union (U5 art. 39 ;
art. 37 pour un vol de transit). Lorsque les deux aéroports sont dans le
même État membre (Paris puis Lyon), les bagages de soute **peuvent** aussi
être contrôlés à l'aéroport de correspondance (U5 art. 39 § 2, art. 42) :
le lieu exact se demande.
Les règles appliquées sont celles de l'Union ; aucune règle propre à l'État
de correspondance n'est inventée.

## 2. Qualité du voyageur et propriétaire des biens

- **Âge** : la tâche suppose un voyageur majeur. Les textes lus prévoient un
  seuil réduit pour les moins de 15 ans et excluent les moins de 17 ans des
  franchises de tabac et d'alcool (U2 art. 7 § 2, 10 ; F2 10°) : biens d'un
  mineur signalés, hors tâche, sans seuil appliqué.
- **Mode de transport** : voyageur aérien ou maritime (hors aviation et
  navigation de tourisme privées) ou autre voyageur (U2 art. 3 points 3-4,
  art. 7 § 1 ; F2 10°, 1) ; à demander, il change le repère cité.
- **Résidence en zone frontalière, travail frontalier, personnel d'un moyen
  de transport** : franchise réduite (U2 art. 3 points 5-6, art. 13 ; F2
  10°, 4) ; signaler, demander, ne rien appliquer.
- **Résidence hors de l'Union** : un non-résident peut relever de
  l'admission temporaire de ses effets personnels raisonnablement
  nécessaires pour le voyage (U4 art. 219) : régime particulier signalé,
  non traité.
- **Propriétaire et destinataire** de chaque bien : un bien acheté pour
  autrui et remboursé, ou rapporté « pour le compte » d'un tiers, n'est pas
  établi comme réservé à l'usage du voyageur ou offert en cadeau ; le guide
  G2 exclut les produits transportés pour le compte d'autrui.

## 3. Biens achetés, reçus ou déjà détenus

| Catégorie | Repères lus | Ce qui reste à établir |
|---|---|---|
| Acheté pendant le voyage, dans un pays tiers | Franchise conditionnelle (§ 4). | Facture ou ticket, prix, devise, date, lieu ; boutique hors taxes ou non ; caractère non commercial. |
| Reçu en cadeau pendant le voyage, ou destiné à être offert | « Destinées à être offertes comme cadeau » entrent dans le caractère non commercial (U2 art. 6 b ; U4 art. 1 point 21 b). | Valeur et sa preuve ; le mot « cadeau » ne suffit pas seul. |
| Déjà détenu avant le départ et rapporté (ordinateur, appareil photo, bijou) | Les marchandises de l'Union contenues dans les bagages d'un passager, sans usage commercial, qui ont temporairement quitté le territoire douanier gardent leur statut **si celui-ci est prouvé** (U4 art. 119 § 3 f) ; ce statut est considéré comme prouvé par la déclaration du passager lorsqu'il n'existe aucun doute sur sa véracité (U5 art. 210) ; une facture ou un document de transport peut aussi servir (U5 art. 211, jusqu'à 15 000 €) ; un voyageur peut demander une preuve sur papier (U4 art. 125). Les bagages réimportés après exportation temporaire ne comptent pas dans le seuil de valeur (U2 art. 7 § 4). Marchandises en retour exonérées sous conditions dans les trois ans (U1 art. 203). Guide G3 : facture ou quittance douanière, « carte de libre circulation » délivrée par un bureau de douane. | Preuve disponible (facture, garantie, photo datée, carte G3) ; aucune affirmation que le bien sera ou ne sera pas taxé. Un bien acheté hors Union lors d'un voyage antérieur pose la question du paiement antérieur des droits et taxes. |
| Acheté dans l'Union avec détaxe (TVA remboursée) | U2 art. 2 : la preuve d'un achat aux conditions du marché intérieur « sans remboursement » sert lors d'un transit. | Question : bordereau de détaxe et remboursement obtenu ; aucune conclusion. |

## 4. Caractère non commercial et franchise : conditions, jamais acquises

Sont dépourvues de caractère commercial les importations qui présentent un
caractère occasionnel et portent exclusivement sur des marchandises
réservées à l'usage personnel ou familial des voyageurs ou destinées à être
offertes, sans intention commerciale traduite par leur nature ou leur
quantité (U2 art. 6 ; U4 art. 1 point 21 b). Des quantités identiques, un
remboursement par des tiers, une revente même partielle ou des voyages
répétés pour acheter laissent ce caractère **non établi** : qualifier,
poser les questions et orienter vers `commercial-import-intake`, sans
appliquer la franchise ni la déclarer perdue.

| Repère lu | Ce qu'il prévoit | Ce qui reste à établir |
|---|---|---|
| U2 art. 7 et F2 10°, 1 (version en vigueur depuis le 1er juillet 2021) | Franchise de TVA des biens dont la **valeur totale** n'excède pas 430 € par personne pour les voyageurs aériens ou maritimes et 300 € pour les autres ; seuil réduit pour les moins de 15 ans ; « la franchise ne s'applique que lorsque la valeur d'une même marchandise est inférieure ou égale » au seuil (F2) ; la valeur d'une marchandise ne peut être fractionnée (U2 art. 7 § 3). | Valeur retenue de chaque bien et sa pièce, mode de transport, âge, caractère non commercial, provenance, date d'arrivée et version. La franchise est personnelle : aucun cumul entre voyageurs pour un même bien (U2 art. 7 § 3 ; guide G1). |
| U3 art. 41 (règl. 1186/2009, consolidé au 1er juillet 2026) | Franchise de droits à l'importation pour les marchandises des bagages personnels des voyageurs venant d'un pays tiers, **pour autant** que l'importation soit exonérée de TVA selon les dispositions nationales prises en application de la directive. | Même conditions ; un bien hors franchise de TVA n'est pas couvert par cette franchise de droits. |
| U2 art. 5 et F2 10°, 3 | Bagages personnels : ceux présentés à l'arrivée et ceux présentés ultérieurement s'ils ont été enregistrés comme bagages accompagnés au départ. | Étiquette ou preuve d'enregistrement d'un bagage arrivé plus tard. |
| U2 art. 7 § 4, 8 à 12 et F2 10°, 2 et 10° bis | Médicaments pour les besoins personnels hors seuil de valeur ; tabac, alcools, carburant soumis à des limites quantitatives distinctes et exclus du seuil de valeur. | Volet accises et santé signalé ; **aucune quantité appliquée** dans cette tâche. |
| F3 art. L. 213-33 (CIBS, en vigueur au 1er janvier 2027) | Exonération de TVA à l'importation des biens des bagages personnels d'un voyageur « en provenance d'un territoire tiers », hors marchandises en retour (L. 213-28), dans la limite d'une valeur cumulée fixée par **arrêté** au plus égale à 430 €, différenciable selon le mode de transport, l'âge, la résidence frontalière ou l'activité en territoire tiers ; carburant, alcools et tabacs hors de cette limite, avec seuils quantitatifs fixés par arrêté. | Arrivée à partir du 1er janvier 2027 : arrêté non lu, notion de « territoire tiers » non lue ; aucune limite ni règle de valeur unitaire appliquée (section « Versions et transition »). |
| U2 art. 14 | Faculté pour un État de ne pas percevoir une taxe inférieure ou égale à 10 € ; usage par la France non lu. | Ne pas l'invoquer. |
| Guides G1, G2 | Au-delà, l'objet est déclaré ; TVA et droits sur la totalité du prix d'un objet qui dépasse seul la franchise ; pour plusieurs objets, seule la fraction excédentaire est taxée ; formulaire cerfa 10070 et service DéclareDouane cités. | Guides, non opposables ; ils servent à formuler les questions. |

Comparer une valeur déclarée à un seuil lu ne conclut ni à la franchise ni
à son exclusion : valeur que le texte retient, mode de transport, caractère
non commercial, provenance et version restent à confirmer par la douane.
La fiche ne fait donc pas cette comparaison : elle n'écrit pas qu'un bien
ou un total « dépasse » ou « reste sous » le seuil, ni qu'une déclaration
est « probable » ou « inutile » ; elle indique la valeur à faire retenir,
sa pièce et la question qui tranche. Une
imposition lue se dit « prévue » par son texte, jamais « due » pour la
personne ; aucun taux de droits ni de TVA n'est donné ici, et aucune
conversion de devise n'est faite.

## Versions et transition

Le repère fiscal français change au **1er janvier 2027**. L'ordonnance
n° 2026-671 du 27 juillet 2026 crée l'art. L. 213-33 du Code des
impositions sur les biens et services (F3), en vigueur différée à cette
date, que la DILA rattache par concordance au 10° de l'art. 50 octies de
l'annexe IV (F2), « sauf le 3 » (définition des bagages personnels). Une
version antérieure du même article, prévue au 1er septembre 2026 par
l'ordonnance n° 2025-1247 du 17 décembre 2025, n'est jamais entrée en
vigueur (« mort-née » dans le fonds LEGI). L'art. 50 octies restait en
vigueur sans date de fin dans le dernier lot qui le republie (4 septembre
2026). La nouvelle rédaction renvoie à un arrêté pour la limite de valeur
(au plus 430 €), ses différenciations et les seuils d'alcool et de tabac ;
elle ne reprend pas la règle de la valeur d'une même marchandise. Ni
l'arrêté, ni la définition du « territoire tiers » dans le CIBS, ni le sort
de l'art. 50 octies au 1er janvier 2027 n'ont été lus : pour une arrivée à
partir de cette date, citer F3 comme repère daté, demander la date exacte
d'arrivée et réserver la limite et ses modalités. Les textes de l'Union
(U2, U3, U4, U5) ne changent pas à cette date selon les lectures faites.

## 5. Déclarer : ce que fait le passage au circuit « rien à déclarer »

Toute marchandise placée sous un régime fait l'objet d'une déclaration
(U1 art. 158 § 1). Pour un voyageur, la déclaration de mise en libre
pratique peut être verbale pour les marchandises dépourvues de caractère
commercial et, sous limites, pour des marchandises commerciales de ses
bagages (U4 art. 135 § 1 a et b) ; une déclaration sur papier est possible
(U4 art. 143). Les marchandises non commerciales des bagages qui
**bénéficient** de la franchise de l'art. 41 ou du régime des marchandises
en retour sont considérées comme déclarées par le passage au circuit vert
ou « rien à déclarer », ou par le passage dans un bureau sans double
circuit (U4 art. 138 a, 141 § 1 a et b). Ce passage vaut donc déclaration :
celui qui déclare répond de l'exactitude des informations (U1 art. 15 § 2).
Ces facilités ne s'appliquent pas aux marchandises soumises à prohibition
ou restriction ni à d'autres formalités particulières (U4 art. 142 c et d).

La fiche ne choisit jamais le circuit à la place de la personne : elle
liste les biens dont la franchise reste à confirmer et les questions à
poser **avant** le passage. Une proposition de passer « rien à déclarer »
pour éviter de payer, de répartir un achat entre voyageurs ou de minorer
une valeur n'est pas une solution : ne pas aider à la mettre en œuvre.
La douane peut visiter les bagages, en présence de leur détenteur (F1
L. 422-7, L. 422-13). Infraction, procès-verbal ou transaction : renfort,
`customs-notice-review`, avocat en droit douanier.

## 6. Volets spécialisés à détecter sans liste ordinaire

Médicaments, denrées et produits d'origine animale, végétaux, animaux,
espèces protégées (ivoire, coraux, peaux…), armes et couteaux, contrefaçons,
biens culturels, alcools et tabacs, carburant, argent liquide. Pour ces
biens, la fiche indique seulement qu'un volet spécialisé existe, demande la
désignation exacte et oriente vers la page officielle concernée ou la
douane, sans appliquer la franchise ordinaire, une quantité, un seuil ou
une autorisation de mémoire. Repères : prohibitions et restrictions
exclues des déclarations simplifiées (U4 art. 142 c) ; argent liquide
d'une valeur de 10 000 € ou plus déclaré à l'entrée dans l'Union (U6
art. 3 § 1, avec ses définitions de l'art. 2 ; F1 L. 222-3, L. 222-4) ;
médicaments : guide G5 seulement.

## 7. Pièces et questions selon le cas

Demander seulement ce qui fait avancer, données superflues masquées
(numéro de passeport, adresse complète, numéro de carte) :

1. Trajet : billets ou carte d'embarquement (lieux, escales, dates),
   étiquettes de bagages enregistrés, mode de transport.
2. Qualité : âge (majeur ou non), résidence habituelle, situation
   frontalière ou de personnel de transport.
3. Inventaire : bien par bien, désignation, quantité, état, catégorie
   (acheté, reçu, déjà détenu, pour autrui), valeur et sa pièce (facture,
   ticket, relevé bancaire masqué, photo de l'étiquette), usage.
4. Biens déjà détenus : facture d'achat dans l'Union, garantie, photo
   datée, quittance douanière d'un voyage antérieur, carte de libre
   circulation éventuelle (guide G3).
5. Acte ou papier déjà remis par la douane : intégralité, sans réponse au
   fond (`customs-notice-review`).

Questions types, à adapter :

- Au service d'information de la douane (coordonnées sur le site officiel
  de la douane) : « J'arrive le [date] de [pays] par [mode], avec
  correspondance à [aéroport]. Pour ces biens [liste et valeurs], lesquels
  dois-je déclarer, comment et où, et quelles preuves acceptez-vous pour
  mon [bien déjà détenu] ? »
- À la compagnie de transport : « Pouvez-vous me fournir la preuve que ce
  bagage a été enregistré comme bagage accompagné au départ de [lieu] ? »
- Au vendeur : « Pouvez-vous me délivrer une facture indiquant la
  désignation, la date et le prix payé ? » (sans demander de valeur
  inexacte).

## 8. Interlocuteurs et orientations

La douane renseigne sur les formalités et la compagnie sur les bagages ;
aucune n'est le conseil de la personne. Conseil : avocat en droit douanier
dès qu'une retenue, un procès-verbal, une transaction, une contestation ou
un volet pénal apparaît. Activité ou revente : `commercial-import-intake`.
Relais proposé, non livré : DOU-012 (véhicule) ; déménagement, mineurs et volets spécialisés :
tâches à découper. Acte reçu : `customs-notice-review`. Ne jamais présenter
une tâche proposée comme une commande disponible.

## Modèle de sortie

1. **En bref** : trajet et qualité retenus ou à préciser, ce qui manque,
   prochaine étape ; alerte éventuelle en tête.
2. **Fiche trajet et qualité** : départ, escales, arrivée, date, mode ;
   provenance qualifiée ; lieu probable des contrôles ; âge, résidence,
   situation frontalière ; chaque ligne marquée « source lue (repère) »,
   « guide », « déclaré », « pièce (auteur) » ou « inconnu ».
3. **Inventaire documenté** : tableau bien par bien (catégorie, valeur et
   pièce, usage, volet spécialisé éventuel).
4. **Questions sur le régime et pièces manquantes** : caractère non
   commercial, franchise possible et conditions sans conclusion, biens déjà
   détenus et preuve, déclaration à prévoir ou non à confirmer ; reçu /
   manquant / à confirmer avec la raison.
5. **Interlocuteur douanier à confirmer** et questions prêtes à copier,
   puis **relais**.
6. **Sources et limites** : repères utilisés avec date de lecture,
   réserves, rien de calculé ; puis la phrase finale :
   « Cette fiche aide à préparer les pièces des biens qui vous
   accompagnent ; elle ne remplace pas l'avis d'un avocat en droit
   douanier. »

## Sources et relecture de maintenance

Textes lus le **19 octobre 2026**. Les consolidations de l'Union sont des
outils de documentation ; seules les publications au Journal officiel font
foi. Le Code des douanes recodifié (ordonnance n° 2026-265 du 8 avril 2026,
en vigueur le 1er mai 2026) a été lu dans sa publication au Journal
officiel du 11 avril 2026 (version non consolidée). L'annexe IV du CGI et le
CIBS ont été lus dans le fonds LEGI de la DILA (stock du 13 juillet 2025 et
466 lots quotidiens jusqu'au 18 octobre 2026). Une page de guide n'est pas
la règle.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 15 (informations, responsabilité du déclarant), 158 (déclaration) et 203 (marchandises en retour) lus. Dernière consolidation lue par DOU-001 ; réforme ultérieure à rechercher à la date des faits. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · lecture complémentaire de la tâche |
| U2 — [Directive 2007/74/CE du Conseil du 20 décembre 2007](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32007L0074) | Acte initial (JO L 346 du 29.12.2007) lu en entier, art. 1 à 21 ; applicable depuis le 1er décembre 2008. Aucune modification recherchée au-delà de cette lecture. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence ; modifications à vérifier |
| U3 — [Règl. (CE) n° 1186/2009 (franchises), consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02009R1186-20260701) | Chapitre X, art. 41, lu ; seule modification listée : règl. (UE) 2026/382 (chapitre V supprimé, référence DOU-001). | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · lecture complémentaire de la tâche |
| U4 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Art. 1 points 5 et 21, 104, 119, 125, 126, 135, 136, 138 à 143 et 219 lus ; reproduction CELLAR complète (29,6 Mo) téléchargée directement. | 2026-10-19 · inchangee · CELLAR, téléchargement direct · lecture limitée aux articles cités |
| U5 — [Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2447-20260701) | Art. 37 à 45 (bagages en vol de transit, de transfert, même État membre) et 210 à 212 (preuve du statut des marchandises des bagages) lus ; reproduction CELLAR complète (42 Mo) téléchargée directement. | 2026-10-19 · inchangee · CELLAR, téléchargement direct · première lecture de référence |
| U6 — [Règl. (UE) 2018/1672 (contrôle de l'argent liquide)](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32018R1672) | Acte initial, art. 2 et 3 lus ; modifications non recherchées. Sert à la seule détection. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · détection seulement |
| F1 — [Code des douanes, annexe à l'ordonnance n° 2026-265 du 8 avril 2026, archive JORF du 11 avril 2026](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | Articles de l'archive filtrés sur « voyageur », « bagage » et « argent liquide » ; L. 222-3, L. 222-4, L. 422-7, L. 422-13 et R. 613-1 lus. Aucun article national sur les franchises des voyageurs repéré. | 2026-10-19 · inchangee · DILA JORF, archive lue hors outil · réserve : version consolidée et ratification à suivre |
| F2 — [CGI, annexe IV, art. 50 octies](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043584984) | Version en vigueur depuis le 1er juillet 2021 lue en entier (10°, 10° bis) ; version antérieure (25 juin 2009) comparée : 10° identique. Vise les « pays tiers ». Republié sans date de fin dans les lots des 28 août et 4 septembre 2026, avec concordance vers le CIBS (F3). | 2026-10-19 · inchangee · DILA LEGI, stock et lots lus hors outil · Légifrance non tenté |
| F3 — [Code des impositions sur les biens et services, art. L. 213-33](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054526399) | Version créée par l'ordonnance n° 2026-671 du 27 juillet 2026, en vigueur différée au 1er janvier 2027, lue dans les lots du 28 juillet et du 28 août 2026 ; version du 1er septembre 2026 (ordonnance n° 2025-1247) lue et marquée « mort-née » dans les lots du 28 et 30 juillet 2026 ; art. L. 211-8 parcouru (renvoi à la directive 2007/74). Arrêtés d'application et définition du « territoire tiers » non lus. | 2026-10-19 · inchangee · DILA LEGI, stock et lots lus hors outil · réserve : arrêté et articulation au 1er janvier 2027 |
| G1 — [Douane, « Vous rapportez du tabac, de l'alcool ou d'autres marchandises achetées hors de l'Union »](https://www.douane.gouv.fr/demarche/vous-rapportez-du-tabac-de-lalcool-ou-dautres-marchandises-achetees-hors-de-lunion) | Page sans date ; seuils, objet dépassant seul la franchise taxé en totalité, pas de cumul entre voyageurs, cerfa 10070 ; cite U3 art. 41 et F2 10°. | 2026-10-19 · inchangee · outil web · guide, non opposable |
| G2 — [Douane, « Franchises douanières et fiscales en quantités et en valeurs »](https://www.douane.gouv.fr/fiche/franchises-douanieres-et-fiscales-en-quantites-et-en-valeurs) | Mise à jour le 06/08/2026 ; provenances (pays tiers, collectivités, territoires fiscalement tiers, Canaries, départements d'outre-mer), fraction excédentaire taxée, produits pour le compte d'autrui exclus ; cite l'arrêté du 18 juin 2009 (art. 1er, 10°). | 2026-10-19 · inchangee · outil web · guide, non opposable |
| G3 — [Douane, « Objets personnels et justificatifs — résidents de l'Union européenne »](https://www.douane.gouv.fr/fiche/objets-personnels-et-justificatifs-residents-de-lunion-europeenne) | Mise à jour le 12/09/2023 ; facture ou quittance douanière, carte de libre circulation délivrée par un bureau de douane ; aucun texte cité. | 2026-10-19 · inchangee · outil web · guide ancien, à vérifier |
| G4 — [Douane, « Voyagez en toute tranquillité avec la douane »](https://www.douane.gouv.fr/fiche/voyagez-en-toute-tranquillite-avec-la-douane) | Mise à jour le 30/06/2026 ; déclaration via DéclareDouane au-delà des seuils, produits interdits ou soumis à règles particulières ; aucun texte cité. | 2026-10-19 · inchangee · outil web · guide, non opposable |
| G5 — [Douane, « Vous voyagez avec des médicaments »](https://www.douane.gouv.fr/demarche/vous-voyagez-avec-des-medicaments) | Page sans date ; ordonnance, durée de traitement, régime des stupéfiants ; cite le Code de la santé publique (L. 5111-1), non lu. | 2026-10-19 · inchangee · outil web · guide, détection seulement |

Pendant une réponse, relire les sources utiles si un outil de lecture existe
et vérifier la version à la date d'arrivée. Sans lecture possible, citer les
repères ci-dessus avec leur date de maintenance et leur limite (méthode,
section 10.6), et garder la fiche factuelle complète : aucune règle de
mémoire, aucun taux, montant, seuil appliqué, franchise ou délai donné pour
les biens. Les liens Légifrance des repères F2 et F3 sont des adresses de
consultation ; la lecture de maintenance a porté sur les mêmes identifiants
dans le fonds LEGI.
