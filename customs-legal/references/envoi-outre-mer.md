# Envoi de biens entre la métropole et un territoire ultramarin

Version `1.0.1` — 19 octobre 2026 (Europe/Paris), DOU-002 ; relais voyageur
mis à jour par DOU-003.
Méthode métier, repères datés et modèle de sortie pour un particulier qui
prépare les pièces d'un envoi non accompagné (colis, fret, conteneur) entre
la France métropolitaine et un territoire ultramarin français précisément
identifié, dans un seul sens. Elle sépare la question douanière de la
question fiscale, ne calcule ni TVA, ni octroi de mer, ni frais, n'accorde
aucune franchise et ne prépare aucune déclaration prête à déposer.

## Périmètre de la tâche

**Inclus** : un particulier, des biens ordinaires (achetés, offerts ou
personnels), un envoi non accompagné, un trajet métropole → territoire ou
territoire → métropole, documenté dans un seul sens. Résultat : fiche
territoriale, opération déclarée ou établie, inventaire, pièces et
questions ciblées.

**Exclus** : véhicule (DOU-012), achat pour une activité ou revente
(DOU-004), biens accompagnant un voyageur (`traveller-goods-documents`),
achat d'un pays tiers livré outre-mer, envoi entre deux territoires
ultramarins, régimes particuliers (entrepôt, admission temporaire,
perfectionnement), calcul de droits ou taxes, demande de franchise ou
d'exonération, acte de la douane déjà notifié (`customs-notice-review`),
déclaration, dépôt, paiement et conseil fiscal général (domaine fiscal
DOM-011, proposé). Leur détection est incluse, leur traitement non.

## 1. Fixer le territoire et le sens

« Outre-mer », « DOM-TOM », « 97… », un nom d'île ou de ville seul ne
suffisent pas. Demander la commune et le territoire de destination (ou de
départ), les lieux exacts de départ, de transbordement et d'arrivée, la
date prévue et le sens du trajet. Deux sens = deux fiches. Un homonyme se
vérifie : Saint-Pierre (La Réunion) n'est pas Saint-Pierre-et-Miquelon ;
l'île de Saint-Martin est partagée entre la collectivité française de
Saint-Martin et Sint Maarten, pays du Royaume des Pays-Bas (ville de
Philipsburg), qui figure parmi les pays et territoires d'outre-mer de
l'annexe II du TFUE (T2).

| Territoire | Statut au regard de l'Union (repères lus) | Axe douanier | Axe fiscal |
|---|---|---|---|
| Guadeloupe, Martinique, La Réunion | Régions ultrapériphériques (T1 art. 349 et 355 § 1). Dans le territoire douanier de l'Union (U1 art. 4) et le territoire douanier national (F1 L. 121-2) ; hors du champ de la directive TVA (U2 art. 6 § 1 c) : « territoire fiscal spécial » (U3 art. 1 point 35). | Échanges de marchandises de l'Union avec un territoire fiscal spécial (U1 art. 1 § 3) : présentation en douane à l'arrivée dans le même État membre, déclaration d'expédition et d'introduction, document unique ou facture/document de transport possibles selon l'autorité (U3 art. 114 et 134). | TVA française applicable (F3 art. 294 a contrario, 296 : taux propres à ces départements). Entrée d'un bien venant de métropole = importation ; sortie vers la métropole = exportation pour la TVA (F3 art. 294, 2 et 3). Ces articles du CGI sont abrogés au 1er janvier 2027 (TVA reprise dans le CIBS, F6) : voir la section « Versions et transition ». Octroi de mer et octroi de mer régional sur les importations (F4 art. 1, 3, 37). Guadeloupe et Martinique forment le « marché unique antillais » pour l'octroi de mer (F4 art. 1 II). |
| Guyane, Mayotte | Régions ultrapériphériques (T1, T3 pour Mayotte depuis le 1er janvier 2014). Même statut douanier et même exclusion de la directive TVA que ci-dessus. | Même axe que ci-dessus (U1 art. 1 § 3 ; U3 art. 114 et 134). | TVA « provisoirement pas applicable » (F3 art. 294, 1, jusqu'au 31 décembre 2026 ; disposition du CIBS correspondante non lue). L'entrée en métropole d'un bien qui en vient est une importation pour la TVA (F3 art. 294, 3, 1°). Octroi de mer et octroi de mer régional sur les importations (F4 art. 1, 37). |
| Saint-Martin (partie française) | Région ultrapériphérique (T1) ; dans le territoire douanier de l'Union et national (U1 art. 4 ; F1 L. 121-2, L. 730-1) ; hors du champ de la directive TVA (U2 art. 6 § 1 c). | Code des douanes national applicable avec adaptations (F1 L. 730-1 et suivants) ; formalités de l'échange à demander. | Ni l'art. 294 du CGI ni la loi sur l'octroi de mer lus ne visent Saint-Martin : impositions de la collectivité **non étudiées**, à demander à son administration fiscale et à la douane. |
| Saint-Barthélemy, Saint-Pierre-et-Miquelon | Pays et territoires d'outre-mer (T2 ; T4 pour Saint-Barthélemy depuis le 1er janvier 2012) : hors du territoire douanier de l'Union (U1 art. 4, exception des PTOM). Le code national s'y applique avec adaptations et un territoire douanier propre (F1 L. 720-1, L. 721-2, L. 741-2). | Sortie du territoire douanier de l'Union vers le territoire, puis entrée sur son territoire douanier propre : formalités **non étudiées** ici. | Impositions locales **non étudiées** : autorité fiscale de la collectivité. |
| Nouvelle-Calédonie, Polynésie française, Wallis-et-Futuna, Terres australes et antarctiques françaises | Pays et territoires d'outre-mer (T2) ; hors du territoire douanier de l'Union (U1 art. 4). Aucun article du code national recodifié lu ne les vise. | Régime douanier local **non étudié** : service des douanes du territoire. | Impositions locales **non étudiées** : autorité locale compétente. |

Pour les quatre dernières lignes, la fiche reste utile (lieux, inventaire,
pièces, questions) mais aucune règle, formalité ou imposition n'est
transposée de la métropole, d'un département d'outre-mer ou d'un achat venu
d'un pays tiers. Un territoire absent du tableau est signalé et réservé.

## 2. Axe douanier et axe fiscal : deux questions distinctes

- **Douanier** : statut du territoire, statut des marchandises (« de
  l'Union » ou non : un bien acheté en métropole à un vendeur établi dans
  l'Union peut l'être ; un bien acheté dans un pays tiers, ou en escale,
  pose une question distincte), présentation en douane à l'arrivée,
  déclaration ou document qui en tient lieu, personne qui présente (U3
  art. 114 : celui qui introduit les marchandises ou pour le compte duquel
  elles sont introduites — souvent par l'intermédiaire du transporteur ou
  de l'opérateur postal, à vérifier). Les cinq départements d'outre-mer et
  Saint-Martin sont dans le même territoire douanier national que la
  métropole (F1 L. 121-2). Les guides G1 et G2 indiquent
  qu'aucun droit de douane n'est perçu de la métropole vers un département
  d'outre-mer : interprétation administrative, à confirmer pour le cas.
- **Fiscal** : TVA (F3) et octroi de mer (F4), et autres impositions
  locales éventuelles, sur la base et aux taux fixés par leurs textes ; la
  base de l'octroi de mer à l'importation est la valeur en douane (F4 art.
  9) et l'octroi de mer n'entre pas dans la base de la TVA (F4 art. 45).
  Les taux d'octroi de mer sont fixés par délibération de la collectivité
  dans des limites légales (F4 art. 7, 28, 37) : **aucun taux n'est donné
  ni appliqué ici**. L'octroi de mer est perçu et contrôlé par la douane
  (F4 art. 42) et liquidé sur la déclaration en douane à l'importation (F4
  art. 13). Une question fiscale autonome (récupérer la TVA métropolitaine
  payée au vendeur, régime d'un professionnel, impôt local d'une
  collectivité) relève du domaine fiscal, sans dépendance d'installation.

## 3. Opération et franchises : conditions à vérifier, jamais acquises

Qualifier l'opération bien par bien : achat (par qui, auprès de qui, payé
par qui), cadeau, envoi de biens personnels, déménagement ou transfert de
résidence allégué, vente entre particuliers, vente sur une plateforme. Le
lien familial, le mot « cadeau » ou « usage personnel » ne prouvent rien
seuls ; un inventaire mêlé se qualifie ligne par ligne.

| Repère lu | Ce qu'il prévoit | Ce qui reste à établir |
|---|---|---|
| F4 art. 8 (version du 1er avril 2023 au 31 décembre 2026) | Biens en provenance d'un État membre de l'Union importés en franchise de TVA et d'octroi de mer lorsque leur valeur totale n'excède pas 400 € pour les « petits envois non commerciaux » (1 000 € pour les biens transportés par les voyageurs, hors tâche) ; biens importés en franchise de droits et taxes : franchise d'octroi de mer. | Caractère non commercial (non défini par l'article lu) ; valeur totale de l'envoi et sa pièce ; date. L'octroi de mer régional suit les exonérations de l'art. 8 (F4 art. 37). Ne jamais dire la franchise acquise. |
| F4 art. 8 (version au 1er janvier 2027) et F6 art. L. 213-34 | À compter du 1er janvier 2027, l'art. 8 ne prévoit plus que la franchise d'octroi de mer (mêmes montants) et renvoie la TVA aux art. L. 213-33 et L. 213-34 du CIBS ; L. 213-34 exonère de TVA l'importation de biens personnels d'un colis expédié par un particulier à un particulier, dans une limite fixée par arrêté, au plus 45 €, portée à 400 € pour l'importation en Guadeloupe, en Martinique ou à La Réunion de biens venant d'un État membre ; alcools, tabacs, parfums, cafés et thés au-delà de seuils fixés par arrêté exclus. | Date de l'importation ; arrêté fixant la limite (non lu) ; « particulier à particulier » et « biens personnels » à établir. |
| U4 art. 25 § 2 (envois d'un pays tiers, de particulier à particulier) | Définit une importation « dépourvue de tout caractère commercial » : envoi occasionnel, marchandises réservées à l'usage personnel ou familial des destinataires sans intention commerciale, adressé sans paiement d'aucune sorte. | Repris par le guide G2 pour les envois vers les départements d'outre-mer : transposition à confirmer, non établie par F4 art. 8. Questions : fréquence des envois, paiement ou remboursement, usage, quantités. |
| F5 art. 50 octies, 5° et 6° | Exonération de TVA à l'importation des biens d'un envoi d'une valeur intrinsèque jusqu'à 22 € lorsque l'importation est réalisée en Guadeloupe, à La Réunion ou en Martinique ; envois de particulier à particulier jusqu'à 45 € avec limites quantitatives (tabac, alcool, parfums). | Champ exact (provenance, nature commerciale) à confirmer pour le cas ; le guide G1 rattache 22 € aux envois commerciaux. Aucune limite appliquée à un colis. |
| Guides G1, G2, G3 | G1 (Guadeloupe, mis à jour le 1er avril 2026) et G2 : 400 € pour les envois non commerciaux venant de l'Union, 22 € pour les envois commerciaux venant de l'Union, achats sur une plateforme entre particuliers traités comme commerciaux. G3 (Guyane, 22 novembre 2019) cite encore 205 € : guide périmé sur ce point. | Guides, non opposables ; ils servent à formuler les questions. Le seuil de 150 € cité par G1 pour les droits de douane d'un achat hors Union précède la suppression de cette franchise au 1er juillet 2026 (référence DOU-001) : ne pas le reprendre. |

Comparer une valeur déclarée à un seuil lu ne conclut ni à la franchise ni
à son exclusion : la valeur que le texte retient (prix, valeur en douane,
envoi entier), le contenu exact et le caractère non commercial restent à
confirmer par la douane. Une imposition lue se dit « prévue à l'importation
par » son texte, jamais « due » pour l'envoi ; un repère daté (par exemple
la TVA non applicable en Guyane et à Mayotte) se cite avec sa date de
lecture et la version à vérifier à la date du trajet.

Les biens soumis à accise (alcools, tabacs) et les marchandises sensibles
sont signalés et orientés, sans quantité ni franchise appliquée. Un
transfert de résidence, des biens recueillis par succession ou offerts à
l'occasion d'un mariage relèvent de franchises propres (F5 art. 50 octies,
1° à 3°, pour la TVA à l'importation) dont les conditions ne sont pas
étudiées ici : les nommer comme question, sans les accorder.

## Versions et transition

Les repères fiscaux changent au **1er janvier 2027** : les art. 291, 294,
295 et 296 du CGI sont abrogés à cette date et la TVA relève du Code des
impositions sur les biens et services (F6), dont les articles lus portent
des versions en vigueur au 29 juillet 2026 puis modifiées au 1er janvier
2027 ; les art. 3, 4, 6, 8 et 45 de la loi relative à l'octroi de mer
reçoivent une nouvelle rédaction à la même date (F4). L'articulation exacte
entre CGI et CIBS pour un envoi de fin 2026, le champ territorial de la TVA
dans le CIBS (Guyane, Mayotte) et l'arrêté fixant les limites n'ont pas été
lus : pour tout envoi, demander la date d'importation prévue et réserver la
règle fiscale dépendante de la version.

## 4. Sens retour : du territoire vers la métropole

La sortie d'un bien de Guadeloupe, de Martinique ou de La Réunion vers la
métropole est une exportation pour la TVA, et l'entrée en métropole d'un
bien venant de l'un des cinq départements d'outre-mer une importation (F3
art. 294, 2 et 3). Les marchandises de l'Union expédiées d'un territoire
fiscal spécial vers une autre partie du territoire douanier du même État
membre sont présentées en douane à leur arrivée (U3 art. 114 § 2). Les
guides G2 et G1 donnent des seuils pour ce sens : guides seulement. Ne pas
reprendre pour le retour les repères de l'aller.

## 5. Pièces et questions selon le cas

Demander seulement ce qui fait avancer, données superflues masquées
(adresse complète, numéro de carte, identifiants) :

1. Lieux : commune et territoire de départ et d'arrivée, étapes connues,
   date d'envoi prévue ou réelle, sens.
2. Inventaire bien par bien : désignation précise, quantité, état (neuf,
   usagé), usage, propriétaire, valeur et sa pièce ; catégorie sensible ou
   soumise à accise.
3. Opération : facture ou ticket de chaque achat (vendeur, lieu, date,
   prix, TVA facturée), qui a payé et qui rembourse, cadeau déclaré,
   fréquence des envois, déménagement allégué et ses justificatifs.
4. Transport : transporteur, opérateur postal ou transitaire, devis ou
   bordereau, documents qu'il demande (déclaration de contenu, facture),
   frais qu'il annonce et leur intitulé.
5. Message ou demande déjà reçue, en intégralité ; un acte de la douane
   notifié relève de `customs-notice-review`.

Questions types, à adapter au destinataire réel :

- Au transporteur ou à l'opérateur postal : « Quels documents faut-il
  joindre pour un envoi vers [commune, territoire], qui présente l'envoi
  en douane à l'arrivée, et pouvez-vous distinguer vos propres frais des
  taxes perçues pour le compte de l'administration ? »
- Au service de la douane du territoire (coordonnées sur le site officiel
  de la douane) : « Pour un envoi de [biens] d'une valeur de [x], de
  [départ] vers [arrivée], quelles formalités et quelles impositions
  (TVA, octroi de mer, octroi de mer régional) s'appliquent, et à quelles
  conditions un envoi est-il considéré comme non commercial ? »
- À l'autorité locale (collectivité ou territoire hors des cinq
  départements) : « Quelles impositions locales s'appliquent à l'entrée de
  ces biens et quel service les perçoit ? »
- Au vendeur : « La TVA facturée correspond-elle à une livraison en
  métropole ou à une expédition vers [territoire] ? » (question fiscale à
  orienter, sans conclusion sur un remboursement).

## 6. Interlocuteurs et orientations

La douane renseigne sur les formalités et les impositions qu'elle perçoit ;
le transporteur sur ses frais et les pièces qu'il demande ; la collectivité
sur ses propres impositions. Aucun n'est le conseil de la personne. Conseil :
avocat en droit douanier pour un contentieux, un contrôle ou un volet pénal ;
conseil fiscal pour une question fiscale autonome. Relais proposés, non
livrés : DOU-004 (activité), DOU-012 (véhicule), domaine fiscal DOM-011.
Biens accompagnant un voyageur : `traveller-goods-documents`. Acte reçu :
`customs-notice-review`. Ne jamais présenter une tâche proposée comme une
commande disponible.

## Modèle de sortie

1. **En bref** : territoire et sens retenus ou à préciser, ce qui manque,
   prochaine étape ; alerte éventuelle en tête.
2. **Fiche territoriale** : lieux, étapes, date et sens ; statut lu du
   territoire ; **axe douanier** et **axe fiscal** en deux blocs distincts,
   chaque ligne marquée « source lue (repère) », « guide », « déclaré »,
   « pièce (auteur) » ou « inconnu ».
3. **Opération** : déclarée ou établie, conditions des franchises
   possibles et questions qui les vérifient, sans conclusion.
4. **Inventaire et pièces** : tableau bien par bien, puis reçu / manquant /
   à confirmer avec la raison.
5. **Questions** par destinataire, prêtes à copier, puis **relais**.
6. **Sources et limites** : repères utilisés avec date de lecture,
   réserves, rien de calculé ; puis la phrase finale :
   « Cette fiche aide à préparer votre envoi et ses pièces ; elle ne
   remplace pas l'avis d'un avocat en droit douanier ou d'un conseil
   fiscal. »

## Sources et relecture de maintenance

Textes lus le **19 octobre 2026**. Le Code des douanes recodifié
(ordonnance n° 2026-265 du 8 avril 2026, en vigueur le 1er mai 2026) a été
lu dans sa publication au Journal officiel du 11 avril 2026 (version non
consolidée, ratification à suivre). CGI et loi relative à l'octroi de mer
lus dans le fonds LEGI de la DILA (stock du 13 juillet 2025 et lots
quotidiens jusqu'au 19 octobre 2026) ; articles du CIBS lus dans les lots
publiés depuis juin 2026. Les consolidations de l'Union sont
des outils de documentation ; seules les publications au Journal officiel
font foi. Une page de guide n'est pas la règle.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 1 § 3 (échanges avec les parties du territoire où la directive TVA ne s'applique pas) et art. 4 (territoire douanier : France hors PTOM ; Monaco) lus. La liste lue mentionne encore le Royaume-Uni (consolidation 2022). | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · lecture complémentaire de la tâche |
| U2 — [Directive 2006/112/CE (TVA), consolidée au 14.04.2025](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02006L0112-20250414) | Art. 5 à 7 lus : art. 6 § 1 c exclut du champ de la directive les territoires français visés aux art. 349 et 355 § 1 TFUE. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · lecture complémentaire de la tâche |
| U3 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Art. 1 point 35 (territoire fiscal spécial), art. 114 (présentation à l'arrivée, y compris au sein du même État membre), art. 134 (déclarations, document unique, facture ou document de transport selon l'autorité) et art. 188 lus ; reproduction CELLAR complète (29,6 Mo) téléchargée directement. | 2026-10-19 · inchangee · CELLAR, téléchargement direct · lecture limitée aux articles cités |
| U4 — [Règl. (CE) n° 1186/2009 (franchises), consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02009R1186-20260701) | Art. 25 et 26 lus (envois de particulier à particulier depuis un pays tiers) ; sert de définition de comparaison, non appliquée aux envois métropole–outre-mer. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · transposition à confirmer |
| T1 — [TFUE, art. 349](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12016E349) et [art. 355](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12016E355), version consolidée 2016 | Liste des régions ultrapériphériques françaises (Guadeloupe, Guyane, Martinique, Mayotte, La Réunion, Saint-Martin) ; art. 355 § 2 renvoie à l'annexe II pour les PTOM. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence |
| T2 — [TFUE, version consolidée 2016, annexe II](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12016E/TXT) | Annexe II lue : Nouvelle-Calédonie, Polynésie française, Terres australes et antarctiques françaises, Wallis-et-Futuna, Saint-Pierre-et-Miquelon, Saint-Barthélemy ; Sint Maarten parmi les territoires néerlandais. | 2026-10-19 · inchangee · CELLAR, téléchargement direct · première lecture de référence |
| T3 — [Décision 2012/419/UE du Conseil européen (Mayotte)](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32012D0419) | Mayotte région ultrapériphérique à compter du 1er janvier 2014. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence |
| T4 — [Décision 2010/718/UE du Conseil européen (Saint-Barthélemy)](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32010D0718) | Saint-Barthélemy PTOM à compter du 1er janvier 2012. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence |
| T5 — [Décision (UE) 2021/991 du Conseil (octroi de mer)](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32021D0991) | Considérant 1 et art. 1 lus : écarts de taxation autorisés pour des produits locaux jusqu'au 31 décembre 2027. Modifications ultérieures non recherchées. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · texte initial, prorogation à surveiller |
| F1 — [Code des douanes, partie législative, annexe à l'ordonnance n° 2026-265 du 8 avril 2026, archive JORF du 11 avril 2026](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | L. 121-1 à L. 121-3, L. 710-1, L. 720-1, L. 721-2, L. 730-1 et L. 741-2 lus ; livre VII parcouru par ses intitulés pour Saint-Barthélemy, Saint-Martin et Saint-Pierre-et-Miquelon. Aucun article lu pour la Nouvelle-Calédonie, la Polynésie française ou Wallis-et-Futuna. | 2026-10-19 · inchangee · DILA JORF, archive lue hors outil · réserve : version consolidée et ratification à suivre |
| F3 — [Code général des impôts, art. 294](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027978194) et [art. 296](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028419532) | Versions en vigueur depuis le 1er janvier 2014, abrogées au 1er janvier 2027 selon les lots d'août et septembre 2026 (abrogation différée). Art. 291 et 295 parcourus (295 modifié au 21 février 2026, abrogé au 1er janvier 2027). | 2026-10-19 · inchangee · DILA LEGI, stock et lots lus hors outil · Légifrance non tenté ; abrogation au 1er janvier 2027 intégrée |
| F4 — [Loi n° 2004-639 du 2 juillet 2004 relative à l'octroi de mer, art. 8](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000046861224) | Art. 1, 3, 3-1, 4, 6, 7, 8, 9, 10, 13, 28, 37, 42 et 45 lus ; art. 8 en vigueur depuis le 1er avril 2023 ; art. 37 dans sa version du 21 février 2026 ; nouvelles rédactions des art. 3, 4, 6, 8 et 45 au 1er janvier 2027 lues (lot du 28 juillet 2026). Délibérations locales de taux non lues. | 2026-10-19 · inchangee · DILA LEGI, stock et lots lus hors outil · taux locaux non étudiés |
| F6 — [Code des impositions sur les biens et services, art. L. 213-34](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054526397) | Art. L. 213-33, L. 213-34 et L. 213-66 lus dans leurs versions au 1er janvier 2027 (lots de juillet à septembre 2026) ; versions marquées en vigueur au 29 juillet 2026 repérées. Champ territorial de la TVA dans le CIBS et arrêtés fixant les limites non lus. | 2026-10-19 · inchangee · DILA LEGI, lots depuis juin 2026 lus hors outil · réserve : articulation CGI/CIBS à vérifier |
| F5 — [CGI, annexe IV, art. 50 octies](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043584984) | Version en vigueur depuis le 1er juillet 2021 lue (1° à 7°). Renvoie au règl. (CEE) n° 918/83 et à un arrêté du 16 septembre 2004, non lus. | 2026-10-19 · inchangee · DILA LEGI, stock et lots lus hors outil · réserve : textes de renvoi non lus |
| G1 — [Douane, « Recevoir un colis en Guadeloupe (particuliers) »](https://www.douane.gouv.fr/fiche/recevoir-un-colis-en-guadeloupe-particuliers) | Fiche mise à jour le 01/04/2026 ; ne cite aucun texte ; seuils par provenance et nature de l'envoi, taux moyens indicatifs, frais du transporteur distincts. Seuil de 150 € pour un achat hors Union antérieur à sa suppression. | 2026-10-19 · inchangee · outil web · guide, non opposable |
| G2 — [Douane, « Vous effectuez des envois non commerciaux de particulier à particulier »](https://www.douane.gouv.fr/demarche/vous-effectuez-des-envois-non-commerciaux-de-particulier-particulier) | Page sans date de mise à jour ; conditions du caractère non commercial ; métropole vers département d'outre-mer jusqu'à 400 € sans taxation ; cite F4 art. 8, F5 art. 50 octies 6° et le chapitre VI de U4. | 2026-10-19 · inchangee · outil web · guide, non opposable |
| G3 — [Douane, « Foire aux questions : les colis postaux en Guyane »](https://www.douane.gouv.fr/fiche/foire-aux-questions-les-colis-postaux-en-guyane) | Mise à jour le 22/11/2019 ; cite F3 art. 294-1 ; seuil de 205 € périmé (G4). | 2026-10-19 · inchangee · outil web · guide ancien, à ne pas suivre sur les seuils |
| G4 — [Douane, actualité « Colis postaux : le montant de la franchise passe à 400 euros »](https://www.douane.gouv.fr/actualites/colis-postaux-le-montant-de-la-franchise-passe-400-euros) | Publiée le 31 mars 2023 : franchise de TVA et d'octroi de mer portée de 205 € à 400 € au 1er avril 2023 pour les envois non commerciaux depuis l'Union vers un département d'outre-mer ; plateformes entre particuliers à caractère commercial. | 2026-10-19 · inchangee · outil web · guide, non opposable |

Pendant une réponse, relire les sources utiles si un outil de lecture existe
et vérifier la version à la date du trajet. Sans lecture possible, citer les
repères ci-dessus avec leur date de maintenance et leur limite (méthode,
section 10.6), et garder la fiche factuelle complète : aucune règle de
mémoire, aucun taux, montant, seuil appliqué, franchise ou délai donné pour
l'envoi. Les liens Légifrance des repères F3 à F6 sont des adresses de
consultation ; la lecture de maintenance a porté sur les mêmes identifiants
dans le fonds LEGI.
