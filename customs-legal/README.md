# Douanes : achat d'un pays tiers, envoi outre-mer et document reçu — DOU-001, DOU-002, DOU-009

Version `0.3.0` — 19 octobre 2026 (Europe/Paris).

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
territoire ultramarin est préparé par `overseas-shipment-documents` ; un acte
de la douane déjà reçu est lu par `customs-notice-review`.

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

## Commun aux trois skills

Les suites DOU-003 à DOU-008 et DOU-010 à DOU-012 restent proposées, sans
commande livrée ici. Les contrôles de structure, de schéma, d'exécution et de
compréhension réelle sont distingués dans les bilans DOU-001, DOU-002 et
DOU-009. Les
réserves de sources et contrôles non exécutés ne valent pas validation
juridique.
