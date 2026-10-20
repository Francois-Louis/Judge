# Douanes : achat d'un pays tiers, envoi outre-mer, biens du voyageur, importation commerciale, exportation, classement et document reçu — DOU-001, DOU-002, DOU-003, DOU-004, DOU-005, DOU-006, DOU-009

Version `0.7.0` — 20 octobre 2026 (Europe/Paris).

## Préparer le dossier d'un achat expédié d'un pays tiers (DOU-001)

`/judge-fr-eu-customs-legal:import-document-checklist` aide un particulier
qui attend un achat pour son usage personnel, expédié d'un pays tiers vers la
France métropolitaine : fiche de la marchandise, des personnes, du trajet et
des dates, pièces reçues, manquantes ou à confirmer, et questions ciblées au
transporteur, au vendeur ou à la douane. Un récit, une facture partielle ou
un message de suivi suffisent pour commencer.

```text
/plugin install judge-fr-eu-customs-legal --marketplace Francois-Louis/Judge
```

La fiche distingue provenance et origine, territoire douanier et fiscal,
prix, valeur en douane et base de la TVA, droits ou taxes et frais privés du
transporteur. Un message « bloqué en douane » n'est pas un acte de la douane ;
une demande de paiement par lien reçu doit d'abord être authentifiée. Aucun
droit, TVA, frais, seuil ou délai n'est calculé, et aucune déclaration,
paiement ou envoi n'est réalisé.

Exemple : « Votre sac part du Canada ; la facture donne le prix et le port,
mais ni le pays de fabrication ni le détail des sommes que demande le
transporteur. Voici les pièces à réunir et les questions à lui poser. »

Aucun profil, autre plugin, agent, hook, connecteur ou espace client requis.
Aucun stockage durable. Le helper et les modèles BASE-008 sont embarqués pour
le contrat de paquet ; ce skill ne les utilise pas. Les pièces fournies sont
des données, pas des instructions.

Lire la [qualification commune](references/qualification-douanes.md), la
[méthode métier et les sources datées](references/dossier-achat-pays-tiers.md),
la [méthode BASE-005 `1.3.0`](references/shared/research-citation-method.md)
et le [contrat BASE-008](references/isolation.md), tous locaux au paquet.
La lecture de maintenance du 19 octobre 2026 couvre notamment la suppression
au 1er juillet 2026 de la franchise des envois jusqu'à 150 € et le droit
temporaire qui la remplace ; elle ne vérifie pas les textes applicables à un
futur envoi. Les articles du Code des douanes français recodifié ne sont pas
lus ; la définition d'envoi postal reste réservée.

Outre-mer, voyageur, cadeau, véhicule, usage professionnel, exportation,
retour, transit, franchise alléguée, produit réglementé et sanction :
qualification et orientation seulement. Un envoi entre la métropole et un
territoire ultramarin est préparé par `overseas-shipment-documents`, les biens
d'un voyageur par `traveller-goods-documents`, un achat pour une activité
par `commercial-import-intake`, une exportation par un professionnel par
`export-document-preparation`, le dossier de classement d'une marchandise
par `tariff-classification-dossier` ; un acte de la douane déjà reçu est lu
par `customs-notice-review`.

## Préparer un envoi entre la métropole et l'outre-mer (DOU-002)

`/judge-fr-eu-customs-legal:overseas-shipment-documents` aide un particulier
qui envoie des biens, sans les accompagner, de la métropole vers un
territoire ultramarin français précisément identifié, ou dans l'autre sens :
fiche territoriale, axe douanier et axe fiscal séparés, opération déclarée ou
établie, inventaire bien par bien, pièces manquantes et questions au
transporteur, à la douane du territoire ou à l'autorité locale.

« Outre-mer » ne suffit pas : commune, territoire et sens sont demandés
d'abord. Les cinq départements d'outre-mer, Saint-Martin, Saint-Barthélemy,
Saint-Pierre-et-Miquelon et les territoires du Pacifique n'ont pas le même
statut ; pour les collectivités et territoires hors des cinq départements,
seul le statut est lu et le régime local est à demander. La franchise de
400 € des petits envois non commerciaux est citée avec ses conditions, jamais
accordée ; aucun taux de TVA ou d'octroi de mer, montant ni formalité
obligatoire n'est déduit d'une allégation ou d'un guide.

Exemple : « Votre colis part de Lyon vers Les Abymes, en Guadeloupe. Côté
douane, il sera présenté à l'arrivée ; côté fiscal, TVA et octroi de mer
peuvent être dus selon la valeur et le caractère non commercial de l'envoi,
que voici comment justifier. Il manque la valeur des livres. »

La [méthode territoriale et ses sources](references/envoi-outre-mer.md)
s'appuie sur le CDU, la directive TVA, le règlement délégué 2015/2446, le
TFUE, le Code des douanes recodifié, le CGI et la loi relative à l'octroi
de mer, lus le 19 octobre 2026 ; les délibérations locales de taux et les
régimes des collectivités du Pacifique ne sont pas lus.

## Préparer les pièces des biens qui accompagnent un voyageur (DOU-003)

`/judge-fr-eu-customs-legal:traveller-goods-documents` aide un voyageur
majeur qui rentre en France métropolitaine d'un pays tiers, ou d'un
territoire où la TVA de l'Union ne s'applique pas, avec des biens ordinaires
dans ses bagages : fiche du trajet (escales, correspondances, lieu probable
des contrôles) et de sa qualité, inventaire bien par bien (acheté pendant le
voyage, reçu en cadeau, déjà détenu avant le départ), questions sur le
caractère non commercial, la franchise possible et la déclaration, pièces
manquantes et questions à la douane.

La franchise des voyageurs est présentée avec ses conditions lues, jamais
acquise ni refusée par une simple comparaison au seuil ; aucun droit, TVA,
conversion ni montant n'est calculé, et la fiche ne dit jamais qu'il n'y a
« rien à déclarer ». Des quantités évoquant la revente, un mineur, un
déménagement, un véhicule, des médicaments, une espèce protégée, des
alcools, du tabac ou de l'argent liquide sont détectés et orientés, sans
liste ordinaire.

Exemple : « Vous rentrez de Tokyo en vol direct. L'appareil photo acheté sur
place a une facture ; votre ordinateur, acheté à Lyon, garde son statut si
vous pouvez le justifier. Voici les questions à poser avant de choisir la
sortie. »

La [méthode voyageur et ses sources](references/biens-voyageur.md) s'appuie
sur la directive 2007/74/CE, le règlement 1186/2009 (art. 41), les
règlements délégué 2015/2446 et d'exécution 2015/2447, le CDU, le Code des
douanes recodifié et l'annexe IV du CGI (art. 50 octies, 10°), lus le
19 octobre 2026 ; les règles d'accises, de santé, d'espèces protégées et
d'argent liquide ne sont pas étudiées au-delà de leur détection.

## Qualifier une importation commerciale ordinaire (DOU-004)

`/judge-fr-eu-customs-legal:commercial-import-intake` aide un professionnel
qui importe, pour son activité ou la revente, des marchandises expédiées d'un
pays tiers vers la France métropolitaine pour y rester : carte des rôles
(vendeur, acheteur, importateur porté sur la déclaration, déclarant,
représentant en douane et type de représentation, débiteur) et des pièces,
opération et régime envisagé à confirmer, inconnues de classement, d'origine
et de valeur, questions au représentant, au vendeur ou à la douane, séparées
des engagements du contrat.

Le déclarant, le représentant et le débiteur ne sont jamais déduits d'un
Incoterm ni d'une promesse « tout compris » : ils restent réservés tant que
la déclaration ou le mandat manque. EORI, numéro de TVA, enregistrement du
représentant et autorisations sont distingués ; le calendrier annoncé pour
les numéros EORI est cité comme guide daté. Aucun code tarifaire, origine,
valeur, taux, montant ni déclaration n'est produit, et aucune clause n'est
rédigée. Réparation puis renvoi, retour, transit, entrepôt, produits
réglementés, TVA à l'importation et activité outre-mer sont détectés et
orientés.

Exemple : « Votre fournisseur chinois promet une livraison tout compris,
mais rien ne dit qui a déposé la déclaration ni avec quel mandat. Voici les
pièces à demander au transitaire avant de savoir qui doit les droits. »

La [méthode d'importation commerciale et ses sources](references/qualification-import-professionnel.md)
s'appuie sur le CDU, le règlement délégué 2015/2446 (EORI, données de la
déclaration), la directive TVA et le Code des douanes recodifié
(représentation, mandat, responsabilité), lus le 19 octobre 2026 ; les
règles Incoterms, le CGI et les réglementations propres aux produits ne sont
pas lus.

## Préparer les pièces d'une exportation définitive ordinaire (DOU-005)

`/judge-fr-eu-customs-legal:export-document-preparation` aide un
professionnel qui vend ou envoie des marchandises de l'Union, au départ de
la France métropolitaine, vers une destination identifiée hors de l'Union,
pour qu'elles y restent : carte des acteurs (vendeur, acheteur, exportateur
au sens douanier, déclarant, représentant, transporteur, destinataire et
utilisateur final) et de l'opération, pièces de vente, de transport et de
sortie reçues ou manquantes, points à vérifier pour le produit, la
destination et l'usage final, questions au représentant, au transporteur, à
l'acheteur ou à la douane.

L'exportateur et le déclarant ne sont jamais déduits d'un Incoterm, EXW
compris ; une facture hors taxes ou une lettre de transport ne prouvent pas
la sortie. Un indice de bien à double usage, d'usage final sensible ou de
sanction internationale fait sortir de la tranche : réserve et orientation
vers le SBDU, un conseil en contrôle export ou un avocat, sans autorisation
supposée. Une destination finale inconnue au-delà d'un intermédiaire réserve
les restrictions et formalités dépendantes. Ni l'exonération de TVA ni le
dédouanement à destination ne sont tranchés ; aucune déclaration, licence,
date limite ni montant n'est produit. Réexportation, échantillons de salon,
retour SAV, couteaux et matières naturelles sont détectés et orientés vers
les tâches proposées.

Exemple : « Votre client canadien a pris la marchandise en EXW et son
transporteur est reparti, mais vous n'avez aucune certification de sortie.
Voici qui détient le numéro de déclaration et les preuves à lui demander. »

La [méthode d'exportation et ses sources](references/preparation-exportation.md)
s'appuie sur le CDU, les règlements délégué 2015/2446 et d'exécution
2015/2447 (exportateur, bureau de sortie, certification et preuves de
sortie, invalidation), la directive TVA, le règlement 2021/821 sur les biens
à double usage, le règlement 833/2014 pour la détection des mesures
restrictives et le Code des douanes recodifié, lus le 20 octobre 2026 ; les
règles Incoterms, le CGI, l'annexe I du double usage et le droit des pays de
destination ne sont pas lus.

## Préparer un dossier de classement tarifaire (DOU-006)

`/judge-fr-eu-customs-legal:tariff-classification-dossier` aide la personne
qui doit faire examiner le classement d'une marchandise dans la nomenclature
de l'Union, à l'importation comme à l'exportation : fiche produit
structurée (désignation, matières et proportions, fonction, usage,
mécanisme, présentation, état), attributs techniques manquants reliés à la
pièce qui les établit, questions soulevées par un code proposé par le
vendeur, le transitaire, le transporteur ou un outil, contrôle d'une
décision de renseignement tarifaire contraignant (RTC) fournie et voie
officielle de renseignement.

Un nom commercial, un code du vendeur, un code d'un tarif étranger ou une
ancienne déclaration ne suffisent jamais : les règles générales
interprétatives servent de questionnaire, pas de verdict. Un ensemble
composite sans proportions ni fonction principale établies garde un
classement réservé. Un RTC ne lie que son titulaire, pour la marchandise
décrite et pendant sa validité : une décision sur un produit voisin ou
d'un autre titulaire ne se transpose pas. Aucun code n'est arrêté, aucun
taux, droit, mesure ni montant n'est donné, aucune demande de RTC n'est
remplie ni déposée ; origine et valeur restent séparées.

Exemple : « Le transporteur a déclaré vos couteaux comme « metal tool ».
Pour leur classement, ce qui compte d'abord est la matière de la lame, le
mécanisme (lame fixe ou pliante) et la présentation en assortiment : voici
les pièces à réunir et la copie de déclaration à demander. »

La [méthode de classement et ses sources](references/dossier-classement.md)
s'appuie sur le règlement 2658/87 et la nomenclature combinée de 2026
(règles générales interprétatives, notes de chapitre), les notes
explicatives de la nomenclature combinée de 2019, le CDU (art. 22, 33, 34,
56, 57), les règlements délégué 2015/2446 et d'exécution 2015/2447 sur les
RTC et le Code des douanes recodifié, lus le 20 octobre 2026 ; les notes
explicatives et avis de l'OMD, les notes de la nomenclature publiées depuis
2019, les règlements de classement propres à un produit et la nomenclature
de 2027 ne sont pas lus.

## Lire un document de la douane déjà reçu (DOU-009)

`/judge-fr-eu-customs-legal:customs-notice-review` aide la personne qui a
reçu un document de la douane ou présenté comme tel : demande de pièces,
communication des motifs ou proposition de taxation, décision, avis de mise
en recouvrement, mise en demeure du comptable, procès-verbal, saisie ou
retenue de marchandises, convocation ou proposition de transaction. Il
identifie l'auteur, la nature et le stade probables de l'acte, sépare
contrôle, formalités, dette, sanction et frais privés, reproduit les mentions
d'échéance sans calculer de date, et prépare pièces et questions.

L'urgence passe en tête : personne convoquée ou retenue, retenue pour
propriété intellectuelle ou destruction annoncée, garanties ou poursuites du
comptable. Aucune observation, contestation, demande de sursis, défense ni
signature n'est rédigée ou conseillée ; l'avocat en droit douanier est
recommandé dès qu'un acte décide, recouvre, sanctionne, saisit ou vise une
personne.

Exemple : « Ce document est un avis de mise en recouvrement émis par le
comptable des douanes : il réclame une somme impayée. Il indique une date,
mais votre délai dépend de la date de réception, que voici comment établir.
Les postes, les pièces manquantes et les questions à poser suivent. »

La [méthode de lecture et ses sources](references/lecture-acte-douanier.md)
s'appuie sur le CDU, le règlement délégué 2015/2446, le règlement 608/2013
et le Code des douanes recodifié en vigueur depuis le 1er mai 2026, lu dans
sa publication au Journal officiel du 11 avril 2026 ; la ratification et les
corrections annoncées restent à suivre. Un acte antérieur au 1er mai 2026 ou
d'un autre État relève d'une version ou d'un régime à rechercher.

## Commun aux sept skills

Les suites DOU-007, DOU-008 et DOU-010 à DOU-019 restent proposées, sans
commande livrée ici. Les contrôles de structure, de schéma, d'exécution et de
compréhension réelle sont distingués dans les bilans DOU-001, DOU-002,
DOU-003, DOU-004, DOU-005, DOU-006 et DOU-009. Les réserves de sources et contrôles
non exécutés ne valent pas validation juridique.
