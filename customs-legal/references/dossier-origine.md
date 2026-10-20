# Préparer les preuves d'origine d'une marchandise

Version `1.0.0` — 20 octobre 2026 (Europe/Paris), DOU-007.
Méthode métier, repères datés et modèle de sortie pour une personne
(professionnel le plus souvent, particulier possible) qui veut réunir les
faits et les preuves utiles à une question d'origine pour une marchandise et
une opération identifiées : chaîne d'expédition, de production et de
transformation, origine non préférentielle et préférence alléguée à
qualifier séparément, portée et lacunes de la preuve fournie, questions au
fournisseur et à l'autorité. Elle ne certifie aucune origine, n'accorde
aucune préférence, ne calcule aucun taux ni droit et ne remplit aucune
preuve d'origine.

## Périmètre de la tâche

**Inclus** : une marchandise (ou un lot de marchandises identiques) à
importer, à exporter ou déjà déclarée, dont l'origine est en question :
mention d'origine sur une facture, une étiquette ou une fiche, certificat,
attestation ou déclaration du fournisseur fournis, préférence tarifaire
invoquée par un vendeur ou un client, production répartie entre plusieurs
pays, marquage d'origine envisagé. Résultat : chaîne documentée, trois
qualifications séparées (provenance, origine non préférentielle, préférence
alléguée), portée de chaque preuve, lacunes reliées à leur pièce et
questions, sans origine arrêtée.

**Exclus** : certificat ou attestation d'origine délivrés ou remplis,
origine garantie, préférence acquise, taux ou droit préférentiel calculé,
franchise, audit complet de la chaîne d'approvisionnement, demande de
renseignement contraignant en matière d'origine (RCO) remplie ou déposée
(tâche à découper), attestation d'origine préférentielle d'une vente à
l'export (DOU-016 proposée), marquage « fabriqué en France » validé,
classement (`tariff-classification-dossier`) et valeur (DOU-008 proposée)
arrêtés, contestation d'une décision de la douane. Leur détection est
incluse, leur traitement non. Formalités de l'opération :
`commercial-import-intake`, `export-document-preparation`,
`import-document-checklist`, `traveller-goods-documents`,
`overseas-shipment-documents` ; acte de la douane reçu :
`customs-notice-review`.

## 1. Trois questions à ne jamais confondre

| Notion | Ce qu'elle désigne | Ce qui la fonde | Ce qui ne suffit pas |
|---|---|---|---|
| **Provenance** (pays d'expédition) | Pays d'où la marchandise est expédiée ou transportée. | Documents de transport. | Elle ne dit rien de l'origine. |
| **Origine non préférentielle** | Origine « de droit commun » : pays où la marchandise est entièrement obtenue ou a subi sa dernière transformation substantielle (U1 art. 60). Elle sert au tarif douanier commun (hors préférences), aux mesures non tarifaires et aux autres mesures de l'Union liées à l'origine (U1 art. 59) ; elle est déclarée à l'importation (G3). | U1 art. 59 à 61 ; U2 art. 31 à 36 et annexe 22-01. | Adresse du vendeur, pays d'expédition, langue de la facture, mention « origine UE » ou « made in » sans éléments de production. |
| **Origine préférentielle** | Caractère originaire au sens d'un régime préférentiel précis (accord de l'Union ou mesure unilatérale), qui peut ouvrir un traitement tarifaire préférentiel (U1 art. 56 § 2, d et e ; art. 64). | Les règles d'origine du régime lui-même : « les règles d'origine préférentielle sont déterminées dans ces accords » (U1 art. 64 § 2). Sans relation préférentielle, pas de cadre (G2). | Une origine non préférentielle, un certificat d'origine non préférentiel, une mention générique « EU origin », un résultat d'outil. |
| **Marquage d'origine** | Mention portée sur le produit ou l'emballage. | Sont prohibés les produits étrangers portant une indication « de nature à faire croire qu'ils sont d'origine française, au sens du code des douanes de l'Union » (F1 L. 231-3). L'information sur l'origine française en vue d'un marquage (IMF) est un avis distinct du RCO (G3). | Un marquage n'est pas une preuve d'origine ; les autres règles de marquage (consommation, secteurs) ne sont pas lues ici. |

Une même marchandise a toujours une origine non préférentielle ; elle peut
en outre être, ou non, originaire au sens d'un régime préférentiel donné, et
ce caractère s'apprécie régime par régime : une marchandise peut être
originaire au sens d'un accord et non d'un autre.

## 2. Ce qui fait foi et ce qui aide seulement

- **Font foi** : le CDU et ses actes délégué et d'exécution (U1, U2, U3) ;
  le texte du régime préférentiel en cause (accord, protocole ou chapitre
  « règles d'origine », annexes de règles par produit, décisions de ses
  organes) dans sa version à la date des faits ; le Code des douanes
  recodifié pour les prohibitions et sanctions nationales (F1).
- **Lie seulement son titulaire** : une décision RCO, pour les marchandises
  et les conditions d'acquisition de l'origine qu'elle décrit, pendant sa
  validité de trois ans, sauf fin anticipée (U1 art. 33 et 34). Elle ne se
  transpose pas à un autre titulaire, un autre produit ou un autre procédé.
- **Aident seulement** : les pages de la Douane (G1 à G4), Access2Markets
  et son outil d'autoévaluation ROSA (T1), un simulateur ou un tableau d'un
  prestataire. Un guide n'est pas la règle ; un résultat d'outil n'est ni
  une preuve ni une décision.
- **Divergence relevée** : une page de la Douane (G1) présente le plafond
  de 6 000 € par envoi pour la déclaration d'origine par tout exportateur
  comme général. Les textes lus le rendent **subsidiaire** : il ne vaut que
  « lorsque le régime préférentiel applicable ne précise pas le seuil »
  (U3 art. 67 § 7 et 68 § 4). Seuil, statut d'exportateur et forme de la
  preuve se lisent donc dans le régime en cause, jamais par défaut.

## 3. La chaîne documentée

Reconstituer, étape par étape, ce qui est arrivé à la marchandise et à ses
matières, avant toute règle :

| Étape | Pays ou territoire | Acteur | Opération | Pièce | Statut |
|---|---|---|---|---|---|
| Matières et composants | par matière | fournisseur | production, achat | facture, déclaration du fournisseur, fiche | pièce (auteur), déclaré, inconnu |
| Fabrication et transformations | par site | fabricant, sous-traitant | usinage, assemblage, finition, conditionnement | gamme de fabrication, bon de travail, photos | idem |
| Expédition et transit | départ, transit, arrivée | vendeur, transporteur | transport, stockage, transbordement | document de transport | idem |
| Vente | pays de facturation | vendeur, intermédiaire | facture, revente | facture | idem |

Règles de lecture :

1. Chaque valeur porte « pièce (auteur) », « déclaré », « source lue
   (repère) » ou « inconnu », avec la pièce qui ferait avancer.
2. Une matière « attribuée » à un fournisseur sans pièce reste **inconnue**
   pour son origine ; une facture d'achat établit l'achat, pas l'origine.
3. Une incohérence entre pièces (pays d'origine différent selon la facture,
   l'étiquette et la déclaration du fournisseur ; dates ; désignations) est
   listée, sans être tranchée.
4. Le pays de facturation, l'adresse du vendeur, la devise ou la langue des
   documents ne sont ni la provenance ni l'origine.

## 4. Origine non préférentielle : le questionnaire

1. **Entièrement obtenue dans un seul pays ?** Liste fermée de U2 art. 31
   (minéraux extraits, végétaux cultivés et récoltés, animaux nés et
   élevés, produits de la chasse et de la pêche, déchets, marchandises
   fabriquées exclusivement à partir de ces produits). Dès qu'une matière
   d'un autre pays intervient, passer à la question 2.
2. **Plusieurs pays interviennent** : dernière transformation ou ouvraison
   substantielle, économiquement justifiée, effectuée dans une entreprise
   équipée à cet effet, aboutissant à un produit nouveau ou à un stade de
   fabrication important (U1 art. 60 § 2).
3. **Le produit figure-t-il à l'annexe 22-01 ?** Pour les marchandises qui
   y sont reprises, l'origine est celle du pays où les règles de l'annexe
   sont remplies (U2 art. 32). L'annexe s'applique **selon le classement
   dans le système harmonisé (SH 2022)** (annexe 22-01, note 2.1) : sans
   classement établi, la règle applicable est **réservée** ; renvoyer à
   `tariff-classification-dossier` seulement si aucune pièce pertinente
   (classement déjà documenté, décision fournie) n'existe. Règles primaires
   (changement de chapitre, de position, de sous-position, valeur ajoutée),
   règles résiduelles et tolérance de 10 % du prix départ usine pour les
   matières non conformes à une règle de changement de classement (note
   2.5) : à lire pour le produit, jamais de mémoire.
4. **Opération minimale ?** Conservation pendant le transport, triage,
   lavage, découpage simple, changement d'emballage, mise en assortiment,
   pose de marques ou d'étiquettes, simple réunion de parties,
   désassemblage, ou leur cumul ne confèrent pas l'origine (U2 art. 34) ;
   l'origine suit alors la règle résiduelle de l'annexe ou, hors annexe, le
   pays d'origine de la majeure partie des matières (en poids ou en valeur
   selon le chapitre).
5. **Opération économiquement injustifiée ?** Réputée telle s'il est établi
   que son objectif était d'éviter une mesure liée à l'origine (U2 art. 33) :
   signal d'alerte, pas une conclusion de la fiche.
6. **Accessoires, pièces de rechange, outillages, éléments neutres et
   emballages** : U2 art. 35 et 36 (énergie, machines, outils et matières
   qui n'entrent pas dans la composition finale non pris en compte).
7. **Preuve** : lorsque l'origine est indiquée dans la déclaration, la
   douane peut exiger que le déclarant la prouve, et demander des éléments
   complémentaires en cas de doute raisonnable (U1 art. 61 § 1 et 2). Un
   document d'origine peut être délivré dans l'Union selon les règles du
   pays de destination (U1 art. 61 § 3).

**Exemple de lecture — chapitre 82 (coutellerie, outils)**. L'annexe 22-01
comporte, pour le chapitre 82, une règle primaire de chapitre sur les
marchandises fabriquées à partir d'ébauches (pays où chaque bord, surface
ou partie travaillante est transformé au-delà de l'état d'ébauche) et une
règle résiduelle (pays de la majeure partie des matières, déterminée sur la
base de leur valeur) ; la liste par position lue porte sur les positions
8201 à 8207. Pour un couteau, la règle applicable au produit précis reste à
vérifier sur le texte à partir du classement établi. Cet exemple ne vaut
pas pour un autre chapitre.

## 5. Préférence alléguée : identifier le régime avant toute règle

1. **Quel régime ?** Accord nommé, parties, sens de l'échange
   (importation dans l'Union ou exportation vers le partenaire), date des
   faits, version du texte et de ses annexes, mesures transitoires. Sans
   régime identifié : « préférence non qualifiable », questions au vendeur
   ou au client, rien d'autre. Ne jamais déduire un régime du pays du
   vendeur ni de l'existence supposée d'un accord.
2. **Exigences générales du régime** : produits entièrement obtenus,
   produits obtenus exclusivement à partir de matières originaires,
   produits satisfaisant aux règles par produit de l'annexe (exemple lu :
   A1 art. 39, accord UE–Royaume-Uni) ; cumul, tolérances, opérations
   insuffisantes, non-modification pendant le transport (A1 art. 40, 42,
   43, 52) : chaque accord a les siens, à lire.
3. **Règle par produit** : liée au classement dans le SH selon la version
   retenue par l'accord ; sans classement, règle **réservée**. Exemple lu
   (A1, annexe 3, chapitre 82) : pour les positions 82.07 à 82.15,
   « CPT ; ou MaxMNO 50 % (PDU) » (changement de position tarifaire, ou
   matières non originaires ne dépassant pas 50 % du prix départ usine). La
   formule et les définitions se lisent dans les notes introductives de
   l'annexe ; aucun pourcentage d'un accord ne se transpose à un autre.
4. **Preuve exigée par le régime** : la forme (certificat de circulation,
   déclaration ou attestation d'origine sur facture, connaissance de
   l'importateur), son auteur, son statut (exportateur agréé, exportateur
   enregistré REX, numéro de référence), son seuil éventuel et sa durée se
   lisent dans le régime. Exemple A1 : demande de l'importateur fondée sur
   une attestation d'origine de l'exportateur ou sur la connaissance de
   l'importateur (art. 54) ; attestation établie par l'exportateur, qui en
   répond, valable douze mois ou plus selon la Partie importatrice
   (art. 56) ; demande a posteriori encadrée (art. 55) ; conservation
   des pièces (art. 59). Ces durées ne valent que pour cet accord, à la date
   des faits, et ne sont jamais calculées pour le cas.
5. **Pièces en amont** : la déclaration du fournisseur communique le
   caractère originaire préférentiel d'une marchandise de l'Union ; elle
   figure sur la facture ou un document commercial identifiant la
   marchandise et peut être à long terme (U3 art. 61 à 63). Elle prouve ce
   qu'elle dit, pour le cadre juridique qu'elle précise (U3 art. 61 § 1 bis),
   et rien de plus.
6. **Demande** : la préférence s'applique à la demande du déclarant, qui
   peut, dans les limites des textes, être introduite a posteriori (U1
   art. 56 § 3) ; le droit dû et toute échéance ne se déduisent pas ici.

## 6. Portée et lacunes de chaque preuve fournie

Pour chaque document, répondre dans un tableau : qui l'a établi (et en
quelle qualité), pour quel régime ou quelle origine, quelle marchandise
(désignation, référence, quantité), quelle période ou quel envoi, ce qu'il
affirme exactement, ce qu'il ne dit pas, incohérences avec les autres
pièces.

- Mention « origine UE » ou « EU origin » sur une facture, sans texte de
  régime ni élément de production : **préférence réservée** ; ce n'est pas
  une attestation d'origine au sens d'un accord tant que le texte exigé par
  ce régime, son auteur et son statut ne sont pas vérifiés.
- Certificat d'origine non préférentiel (souvent délivré par un organisme
  du pays d'exportation) : peut documenter l'origine non préférentielle,
  jamais une préférence.
- Attestation ou déclaration du fournisseur : portée limitée au produit,
  à la période et au cadre juridique qu'elle mentionne.
- Une RCO d'un autre titulaire, sur un produit voisin ou pour un autre
  procédé ne se transpose pas.
- Un document étranger (modèle, règle, seuil ou formulaire d'un pays
  tiers, y compris américain) n'est jamais importé dans l'analyse.

## 7. Signaux d'alerte

- **Acte de la douane reçu** (contrôle a posteriori, demande de
  justification d'origine, refus de préférence, notification de dette) :
  renfort en tête, `customs-notice-review`, avocat en droit douanier ;
  aucune réponse au fond.
- **Demande de modifier une mention d'origine ou de « faire passer »** une
  marchandise par un pays tiers pour changer son origine : ne pas aider. La
  fausse déclaration dans l'origine, lorsqu'un droit ou une taxe s'en trouve
  éludé ou compromis, est une contravention (F1 R. 515-5, 2°) ; une
  opération dont l'objectif est d'éviter une mesure n'est pas
  économiquement justifiée (U2 art. 33) ; une indication faisant croire à
  une origine française est prohibée (F1 L. 231-3). Avocat en droit
  douanier si c'est déjà fait.
- **Mesure liée à l'origine possible** (antidumping, sauvegarde, sanctions,
  contingent) : la nommer comme question au représentant ou au service
  compétent, sans l'affirmer ni l'écarter.
- **Opérations répétées sur un même produit à l'origine incertaine** :
  signaler l'intérêt d'une question à la douane ou d'une RCO, sans la
  déposer.

## 8. Pièces à réunir et questions types

1. Désignation, référence et fiche du produit ; classement documenté et son
   statut.
2. Liste des matières et composants, avec fournisseur, pays d'origine
   allégué, valeur ou poids et pièce correspondante.
3. Description des étapes de fabrication et des sites (gamme, photos,
   bons de travail).
4. Documents de transport (expédition, transit, transbordement).
5. Preuves fournies : attestation ou déclaration d'origine, certificat,
   déclaration du fournisseur, RCO ; texte intégral.
6. Régime invoqué, date prévue de l'opération et sens (import, export).

Questions, à adapter :

- Au fournisseur ou au fabricant : « Pour [référence], dans quel pays et
  sur quel site chaque étape de fabrication est-elle réalisée ? Quelles
  matières non originaires utilisez-vous (pays, position, valeur) ? Sur quel
  régime préférentiel et quelle règle de produit fondez-vous la mention
  [mention], et pouvez-vous fournir la déclaration ou l'attestation
  correspondante et votre statut d'exportateur ? »
- Au client ou au vendeur qui invoque une préférence : « Quel accord
  précis visez-vous, pour quelle date d'envoi, et quelle preuve d'origine
  attend votre douane ? »
- Au représentant ou au transitaire : « Quelle origine non préférentielle
  et quelle préférence avez-vous déclarées (ou déclarerez-vous) pour
  [référence], sur quelles pièces ? »
- À la douane (service d'information ou service de l'origine, coordonnées
  sur le site officiel) : « Pour [désignation, étapes, pays], quelles règles
  d'origine sont à examiner et quelles pièces faut-il pour une demande de
  RCO ? »

## Modèle de sortie

1. **En bref** : marchandise et opération comprises, pays en présence
   (expédition, fabrication, matières), preuve fournie, préférence
   invoquée, prochaine étape ; aucune origine arrêtée ; alerte éventuelle
   en tête.
2. **Chaîne documentée** : tableau étape, pays, acteur, opération, pièce,
   statut ; incohérences listées.
3. **Trois qualifications séparées** : provenance ; origine non
   préférentielle à qualifier (questionnaire, règle réservée si classement
   non établi) ; préférence alléguée (régime identifié ou non, règle et
   preuve à lire).
4. **Preuves fournies : portée et lacunes** : tableau auteur, régime,
   marchandise, période, ce qui est affirmé, ce qui manque.
5. **Pièces manquantes**, de la plus décisive à la moins décisive, chacune
   reliée à son interlocuteur.
6. **Questions** prêtes à copier, par destinataire (fournisseur, client ou
   vendeur, représentant, douane).
7. **Sources et limites** : repères lus et leur date, régime lu ou non,
   réserves, rien de délivré, déposé ni calculé ; puis la phrase finale :
   « Cette fiche aide à préparer les preuves d'origine de votre
   marchandise ; elle ne remplace pas l'avis d'un avocat en droit
   douanier. »

## Interlocuteurs et orientations

La douane renseigne sur l'origine et délivre les RCO ; le représentant
mandaté déclare l'origine et la préférence des déclarations qu'il dépose ;
le fournisseur et le fabricant détiennent les données de production et
établissent leurs déclarations ; l'exportateur répond de l'attestation qu'il
établit. Aucun n'est le conseil de la personne. Conseil : avocat en droit
douanier pour un contrôle, un refus de préférence, un contentieux ou un
volet pénal. Relais proposés, non livrés : DOU-008 (valeur), DOU-016
(attestation d'origine préférentielle d'une vente à l'export), demande de
RCO (tâche à découper). Ne jamais présenter une tâche proposée comme une
commande disponible.

## Sources et relecture de maintenance

Textes lus le **20 octobre 2026**. Les consolidations de l'Union sont des
outils de documentation ; seules les publications au Journal officiel font
foi. Le Code des douanes recodifié, en vigueur depuis le 1er mai 2026, a été
lu dans sa publication au Journal officiel du 11 avril 2026 ; pour des faits
antérieurs, la version de l'ancien code est à rechercher. Une page de guide
n'est pas la règle ; Access2Markets, ROSA et TARIC sont des outils de
consultation.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 33, 34, 56 (§ 2 et 3) et 59 à 68 lus. Dernière consolidation listée ; réforme ultérieure à rechercher à la date des faits. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture de la tâche |
| U2 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Art. 31 à 36 ; annexe 22-01, notes introductives et chapitre 82 lus ; liste des chapitres couverts parcourue. Origine préférentielle unilatérale (art. 37 et suivants, SPG) non lue. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture limitée aux passages cités |
| U3 — [Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2447-20260701) | Art. 57, 61 à 63, 67 et 68 lus (certificat d'origine non préférentiel des régimes particuliers, déclarations du fournisseur, exportateur agréé, enregistrement REX hors SPG, seuils subsidiaires de 6 000 €). Procédures SPG non lues. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · lecture limitée aux passages cités |
| A1 — [Accord de commerce et de coopération UE–Royaume-Uni, JO L 149 du 30.4.2021](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:22021A0430%2801%29) | Exemple d'accord : chapitre « Règles d'origine », art. 37, 39, 54 à 59 lus, art. 40 à 52 repérés par leurs intitulés ; annexe 3, chapitre 82 ; annexe 7 (texte de l'attestation et ses notes). Décisions ultérieures des organes de l'accord non recherchées. | 2026-10-20 · inchangee · CELLAR, téléchargement direct · exemple, ne vaut pour aucun autre accord |
| F1 — [Code des douanes, annexes à l'ordonnance n° 2026-265 et au décret n° 2026-266, archive JORF du 11 avril 2026](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | L. 231-3 (indication d'origine française sur un produit étranger) et R. 515-5, 2° (fausse déclaration dans l'origine) lus ; textes parcourus sur « origine ». | 2026-10-20 · inchangee · DILA JORF, archive lue hors outil · réserve : version consolidée non lue |
| G1 — [Douane, « Origine préférentielle d'une marchandise »](https://www.douane.gouv.fr/fiche/origine-preferentielle-dune-marchandise) | Mise à jour le 20/05/2026 ; preuve exigée, formes de preuve, renvoi aux protocoles de chaque accord et à ROSA ; seuil de 6 000 € présenté comme général (voir section 2). | 2026-10-20 · inchangee · outil web · guide, non opposable |
| G2 — [Douane, « S'assurer de l'origine de votre marchandise : le RCO »](https://www.douane.gouv.fr/demarche/sassurer-de-lorigine-de-votre-marchandise-le-renseignement-contraignant-sur-lorigine-rco) | Page sans date ; RCO pour l'origine non préférentielle à l'import et préférentielle à l'import et à l'export, pièces de la demande, gratuité, service compétent. Délais de traitement non repris. | 2026-10-20 · inchangee · outil web · guide |
| G3 — [Douane, « Connaître et s'assurer de l'origine de votre marchandise »](https://www.douane.gouv.fr/demarche/connaitre-et-sassurer-de-lorigine-de-votre-marchandise) | Page sans date ; origine non préférentielle de droit commun déclarée à l'import, préférence liée à une relation préférentielle, IMF distincte du RCO, service d'information. | 2026-10-20 · inchangee · outil web · guide |
| G4 — [Douane, FAQ « Convention pan-euro-méditerranéenne modernisée »](https://www.douane.gouv.fr/faq-origine-preferentielle-convention-pan-euro-mediterraneenne-modernisee) | Page sans date ; règles modernisées, transition 2025, preuves. Texte de la convention non lu : aucune règle PEM retenue. | 2026-10-20 · inchangee · outil web · guide |
| T1 — [Commission européenne, Access2Markets, présentation de ROSA](https://trade.ec.europa.eu/access-to-markets/fr/content/presentation-du-rosa) | Version 2026.10.1.3 du 14 octobre 2026 ; autoévaluation des règles d'origine par accord ; aucune valeur juridique indiquée ; aucun produit consulté. | 2026-10-20 · inchangee · outil web · outil |

Non lus : texte des autres accords et protocoles d'origine (dont la
convention pan-euro-méditerranéenne), règles d'origine du SPG, règlements de
la Commission sur l'origine de marchandises particulières (U1 art. 67),
règles nationales de marquage (consommation, secteurs), jurisprudence,
décisions des organes des accords, ancien Code des douanes pour des faits
antérieurs au 1er mai 2026. Pendant une réponse, relire les sources utiles
si un outil de lecture existe et vérifier la version à la date des faits.
Sans lecture possible, citer les repères ci-dessus avec leur date de
maintenance et leur limite (méthode, sections 5 et 10.6), et garder la fiche
factuelle complète : aucune origine arrêtée, aucune règle de mémoire, aucun
taux, montant, franchise, seuil, délai ni formalité obligatoire déduit d'une
allégation.
