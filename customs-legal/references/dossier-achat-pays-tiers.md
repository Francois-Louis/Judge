# Dossier d'un achat privé expédié d'un pays tiers

Version `1.0.0` — 19 octobre 2026 (Europe/Paris), DOU-001.
Méthode métier, repères datés et modèle de sortie pour un particulier qui
prépare les pièces d'un achat pour usage personnel, expédié sans voyageur
depuis un pays tiers vers la France métropolitaine. Elle ne calcule ni droit,
ni TVA, ni frais, ne fixe ni classement, ni origine, ni valeur, et ne prépare
aucune déclaration prête à déposer.

## Périmètre de la tâche

**Inclus** : un particulier, un achat pour son usage personnel, une
marchandise ordinaire identifiée, un envoi non accompagné d'un pays tiers vers
la France métropolitaine. Résultat : fiche, inventaire des pièces et
questions ciblées. La détection des exclusions est incluse, leur traitement
non (voir la [qualification commune](qualification-douanes.md)).

**Exclus** : outre-mer, voyageur, cadeau, véhicule, usage professionnel ou
revente, exportation, retour ou réparation, réimportation, transit, régime
temporaire ou particulier, franchise alléguée, produit réglementé ou prohibé,
acte de la douane déjà notifié, sanction et contentieux.

## Distinctions à tenir dans la fiche

| Distinction | Ce qui est établi par les repères lus | Ce qui reste à demander |
|---|---|---|
| Provenance / origine | L'origine non préférentielle est celle du pays où la marchandise a été entièrement obtenue ou a subi sa dernière transformation substantielle (U1, art. 60) ; la douane peut demander la preuve d'une origine déclarée (U1, art. 61). | Pays de fabrication indiqué et sa pièce ; lieu d'expédition ; un vendeur ou un entrepôt dans un pays ne prouve pas l'origine. |
| Territoire douanier / territoire fiscal | Le territoire douanier de l'Union comprend la France, hors pays et territoires d'outre-mer de la quatrième partie du TFUE (U1, art. 4) ; certains territoires français de l'article 349 et 355 § 1 TFUE sont dans le territoire douanier mais hors du champ de la directive TVA (U4, art. 6). | Ville et territoire de destination ; tout trajet outre-mer sort de cette tâche (DOU-002). La liste de l'article 4 lue dans la consolidation 2022 mentionne encore le Royaume-Uni : statut après son retrait, et cas de l'Irlande du Nord, à vérifier séparément. |
| Prix / valeur en douane / base de la TVA | La valeur transactionnelle part du prix effectivement payé ou à payer, après ajustements (U1, art. 70) ; la base de la TVA à l'importation est la valeur en douane, augmentée notamment des droits dus en raison de l'importation et des frais de transport et d'assurance jusqu'au premier lieu de destination (U4, art. 85-86). | Prix, devise, remises, frais de port et d'assurance facturés, liens entre parties. Ne rien additionner : ces éléments servent les questions, pas un calcul. |
| Dette douanière / frais privés | À la mise en libre pratique, la dette naît à l'acceptation de la déclaration ; le déclarant est débiteur, et en représentation indirecte la personne pour le compte de qui elle est faite aussi (U1, art. 77) ; représentation directe ou indirecte (U1, art. 18). | Qui a déclaré, sous quelle représentation, quel document l'établit ; intitulé de chaque somme réclamée : droit, TVA, frais de dédouanement, frais de stockage, avance de frais. |
| TVA collectée par le transporteur | Pour les envois d'une valeur intrinsèque jusqu'à 150 EUR hors produits soumis à accises et hors IOSS, un régime particulier permet à la personne qui présente les biens en douane de percevoir la TVA auprès du destinataire, qui en est redevable (U4, art. 369 sexvicies et septvicies). | Le transporteur invoque-t-il ce régime ? Quels montants, sous quel intitulé, et quelle pièce les détaille ? |
| IOSS / « taxes incluses » | Une importation déclarée sous le régime IOSS est exonérée de TVA à l'importation si le numéro IOSS du fournisseur ou de son intermédiaire a été fourni au bureau de douane au plus tard au dépôt de la déclaration (U4, art. 143 § 1 c bis). | Mention IOSS ou « TVA payée au panier » sur la commande ou la facture ; le transporteur a-t-il reçu ou utilisé ce numéro ? Ne pas demander ni recopier le numéro IOSS dans la fiche : la question porte sur sa transmission par le vendeur. |
| Seuil de 150 € | Depuis le 1er juillet 2026, la franchise de droits fondée sur ce seuil est supprimée (U2, U3 art. 1 et 4). Du 1er juillet 2026 au 1er juillet 2028, un droit de douane de 3 EUR par article contenu dans un envoi d'une valeur intrinsèque totale jusqu'à 150 EUR s'applique à sa place lorsque l'importation est exonérée de TVA au titre de l'IOSS ou que les marchandises sont dans un envoi postal (U3, art. 2) ; ailleurs, le tarif douanier commun continue de s'appliquer (U3, considérant 6). L'art. 2 vise ces deux catégories d'envois, sans critère tiré de la qualité du destinataire ; l'exclusion du B2B vient du guide G1. | Date d'importation, IOSS ou non, envoi postal ou express, valeur intrinsèque, nombre et nature des articles. Aucun montant appliqué au colis : le sens d'« article » (G1 : ligne d'article de même position tarifaire) et la définition d'envoi postal (U5) restent à vérifier pour le cas. |
| Annonces non vérifiées | Taxe française sur les petits colis présentée comme suspendue au 1er juillet 2026 et « redevance pour frais de gestion » européenne annoncée au 1er novembre 2026 (G4, communiqué) ; Commission tenue d'évaluer chaque mois depuis octobre 2026 un détournement des flux (U3, art. 3). | Texte juridique non lu : ne pas dire qu'une taxe ou redevance s'applique ou non au colis ; demander l'intitulé et le fondement de toute somme de ce type au prestataire. |

## Pièces et questions selon le cas

Demander seulement ce qui fait avancer, données superflues masquées (adresse
complète, numéro de carte, identifiants) :

1. Confirmation de commande et facture : vendeur et pays d'établissement,
   désignation, quantité, prix, devise, frais de port/assurance, mentions
   « taxes incluses », « DDP » ou IOSS.
2. Preuve de paiement masquée : date, montant, devise ; aucune donnée de carte.
3. Description de la marchandise : matière ou composition, fonction, usage
   personnel, état ; fiche produit si la désignation est vague.
4. Trajet : lieu d'expédition, transporteur ou opérateur postal, numéro de
   suivi, étapes avec dates et pays, lieu d'arrivée annoncé.
5. Message ou demande reçue, en intégralité : auteur, canal, date, pièces
   demandées, somme et intitulé, référence de dossier.
6. Déclaration ou document douanier, s'il est déjà disponible : seulement les
   références et les rubriques utiles.

Inconnues qui bloquent tout calcul fiable, à nommer même avec une facture
complète : date d'importation et version des textes, territoire, classement
tarifaire, origine et preuve éventuelle, valeur et frais retenus, devise et
conversion, régime de TVA (IOSS, régime particulier, autre), nature de l'envoi
(postal ou non) et mesures particulières applicables à la marchandise.

Questions types, à adapter au destinataire réel :

- Au transporteur ou à son prestataire : « Pouvez-vous me transmettre le
  détail des sommes demandées en distinguant droits, TVA et vos propres frais,
  la référence de la déclaration et la qualité dans laquelle vous agissez ? »
  ; « Quelles pièces vous manquent exactement, et à quelle étape est l'envoi ? »
- Au vendeur : « Le numéro IOSS a-t-il été transmis pour cette commande ? » ;
  « Pouvez-vous confirmer le pays de fabrication et fournir une facture
  détaillée ? » (sans engager le vendeur sur une qualification douanière).
- À la douane (service d'information) : « Le message reçu émane-t-il de vos
  services ? Quel interlocuteur est compétent pour cet envoi ? »

## Modèle de sortie

1. **En bref** : ce qui est arrivé, ce qui manque et la prochaine étape, en
   quelques phrases ; signal d'alerte éventuel en tête.
2. **Fiche** : marchandise ; personnes et rôles ; opération et usage ;
   territoires et trajet ; provenance et origine ; prix et frais ; dates ;
   chaque ligne marquée « pièce (auteur) », « déclaré », « source lue » ou
   « inconnu ».
3. **Pièces** : tableau reçu / manquant / à confirmer, avec la raison.
4. **Questions** : par destinataire identifié (transporteur, vendeur, douane).
5. **Relais** : volets voisins avec leur question et leurs pièces.
6. **Sources et limites** : repères utilisés avec date de lecture, réserves,
   rien de calculé ; puis la phrase finale de la qualification commune.

## Sources et relecture de maintenance

Textes lus le **19 octobre 2026** par l'outil `legal_sources.py` du dépôt
(EUR-Lex répond par un défi, reproduction officielle CELLAR lue) ou par
l'outil web. Les consolidations sont des outils de documentation ; seules les
versions publiées au Journal officiel font foi. Une page de guide n'est pas
la règle. Les articles du Code des douanes français, recodifié au 1er mai
2026 selon G3, n'ont pas été lus : aucune disposition nationale n'est citée.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 4, 5 (définitions), 18, 56, 59-61, 70, 77 et 172 lus. CELLAR ne liste aucun acte modificatif postérieur au règl. (UE) 2022/2399 ; une réforme ultérieure reste à rechercher à la date des faits. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence |
| U2 — [Règl. (CE) n° 1186/2009 relatif aux franchises, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02009R1186-20260701) | Chapitre V (envois de valeur négligeable) supprimé par U3 ; art. 25-27 (envois de particulier à particulier) lus, hors tranche. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence |
| U3 — [Règl. (UE) 2026/382 du Conseil du 11 février 2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R0382) | Texte intégral lu : suppression de la franchise fondée sur un seuil, droit de 3 EUR par article du 1er juillet 2026 au 1er juillet 2028 (IOSS ou envoi postal), évaluations art. 3, application au 1er juillet 2026. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · prorogation ou extension possibles à surveiller |
| U4 — [Directive 2006/112/CE (TVA), consolidée au 14.04.2025](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02006L0112-20250414) | Art. 5-7, 30, 60-61, 85-87, 143 § 1 c bis, 369 sexvicies à septvicies ter lus. Dernière consolidation listée par CELLAR ; transposition française non lue. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · première lecture de référence |
| U5 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Défi EUR-Lex, puis erreur de transport CELLAR ; même échec sur la consolidation du 25.02.2025. Définitions d'« envoi postal » et de « valeur intrinsèque » non lues. | 2026-10-19 · inaccessible · legal_sources.py eu · réserve : ne pas qualifier un envoi de postal ni fixer sa valeur intrinsèque |
| U6 — [Règl. d'exécution (UE) 2026/1200 du 5 juin 2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32026R1200) | Intitulé et considérants 1 à 4 lus : modalités du droit de 3 EUR (garanties, bureau de douane compétent) ; dispositif non exploité. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · lecture partielle, aucune modalité appliquée |
| G1 — [Douane, fiche « Droit de douane forfaitaire de 3 euros »](https://www.douane.gouv.fr/fiche/droit-de-douane-forfaitaire-de-3-euros-sur-les-ventes-distance-de-biens-importes) | Guide mis à jour le 10/07/2026 : droit par ligne d'article de même position tarifaire ; B2B et envois de particulier à particulier jusqu'à 45 € exclus ; hiérarchie des redevables, importateur particulier ; non remboursable hors cas de l'art. 116 CDU. Interprétation administrative, pas la règle. | 2026-10-19 · inchangee · outil web · guide, non opposable sans vérification du texte |
| G2 — [Douane, questions-réponses sur le droit de 3 euros](https://www.douane.gouv.fr/fiche/principales-questions-et-reponses-autour-du-droit-de-douane-forfaitaire-de-3-euros) | Guide mis à jour le 10/07/2026 : intégration du droit forfaitaire dans la base de TVA selon le régime ; remboursement limité aux cas de l'art. 116 CDU. | 2026-10-19 · inchangee · outil web · guide, à vérifier sur texte avant tout effet |
| G3 — [Douane, actualité du 1er mai 2026 sur la recodification](https://www.douane.gouv.fr/actualites/recodification-le-code-des-douanes-entrera-en-vigueur-le-1er-mai-2026) | Code recodifié « à droit constant », trois parties en vigueur au 1er mai 2026, ordonnance prise sur l'art. 36 de la loi n° 2023-610 ; numéros non donnés, articles non lus. | 2026-10-19 · inchangee · outil web · réserve : aucun article national cité |
| G4 — [Ministère de l'Économie, communiqué n° 850 du 30 juin 2026](https://presse.economie.gouv.fr/?p=180373) | Taxe nationale sur les petits colis instaurée le 1er mars 2026 et suspendue au 1er juillet ; redevance européenne pour frais de gestion annoncée au 1er novembre 2026, modalités à définir. Texte juridique non cité. | 2026-10-19 · inchangee · outil web · réserve : annonce, texte juridique à lire |
| G5 — [Gouvernement, « Taxe sur les petits colis : ce qui change »](https://www.info.gouv.fr/actualite/taxe-sur-les-petits-colis-ce-qui-change) | HTTP 403 à l'ouverture. | 2026-10-19 · inaccessible · outil web · réserve : contenu non lu |

Pendant une réponse, relire les sources utiles si un outil de lecture existe
et vérifier la version à la date des faits. Sans lecture possible, citer les
repères ci-dessus avec leur date de maintenance et leur limite (méthode,
section 10.6), et garder la fiche factuelle complète : aucune règle de
mémoire, aucun seuil, taux, montant, franchise ou délai appliqué au colis.
TARIC et Access2Markets aident à formuler une question de classement ; ils ne
fournissent pas ici un taux applicable.
