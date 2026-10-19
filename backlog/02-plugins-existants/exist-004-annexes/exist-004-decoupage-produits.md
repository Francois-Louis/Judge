# EXIST-004 — Découpage produits et publicité

Propositions du **16 octobre 2026**, issues de l'[inventaire complet](exist-004-inventaire-produits.md).
Les 25 stories PDT restent `proposee`. La [relecture documentaire](exist-004-verification.md)
éprouve lancement B2C France, campagne environnementale et cas limites.

## Contrat commun et première tranche

Toutes les suites dépendent d'EXIST-004, PILOTE-003, BASE-005 et BASE-006.
Le bilan PILOTE-003 est terminé après BASE-011 ; ce préalable satisfait ne
sélectionne aucune extension. Ses limites H01 complet et lecteur indépendant
restent consignées. Chaque livraison applique BASE-003, BASE-008, la méthode
BASE-005 `1.0.0` embarquée et les couches de recette BASE-006.

**Première tranche proposée : PDT-001**, une fiche de qualification pour une
TPE préparant la vente en ligne d'un produit à des particuliers en France.
Entrée : description, pièces disponibles et date visée ; sortie : acteur,
public, marché, catégorie, canal, rôles et pièces manquantes, puis contrôles
à instruire. Aucun avis de conformité, aucune CGV ni campagne complète.
Elle produit un dossier utile sans service juridique, profil complet,
historique, compte connecté ou autre plugin installé. Ce choix de séquence
est une proposition, pas le lancement de la suite par EXIST-004.

Chaque tranche corrige ses propres descriptions, blocs setup, sorties et
routage dans les seuls fichiers qu'elle touche. PDT-013/014 ne sont pas des
préalables imposés. En lecture ponctuelle, recueillir les faits nécessaires
en conversation ; tout accès durable respecte le helper BASE-008, y compris
profil absent/interrompu, sans import automatique. Le modèle de profil n'est
pas un fichier effectif. Les identifiants techniques existants sont conservés ;
les nouveaux modes visibles sont décrits avec leur portée limitée.

## Stories et dépendances métier

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [PDT-001](../suites/pdt-001-qualifier-lancement.md) | Fiche de qualification d'un lancement B2C France | Aucune |
| [PDT-002](../suites/pdt-002-preparer-lancement-b2c.md) | Note de préparation d'une vente en ligne de bien courant | PDT-001 |
| [PDT-003](../suites/pdt-003-evolution-fonctionnalite.md) | Fiche des changements d'une fonctionnalité existante | Aucune |
| [PDT-004](../suites/pdt-004-analyser-risque-produit.md) | Options et mesures pour un risque produit déterminé | PDT-003 |
| [PDT-005](../suites/pdt-005-inventorier-allegations.md) | Tableau exhaustif des allégations d'un support délimité | Aucune |
| [PDT-006](../suites/pdt-006-allegations-factuelles.md) | Revue d'une allégation factuelle et de sa preuve | PDT-005 |
| [PDT-007](../suites/pdt-007-allegation-environnementale.md) | Revue d'une allégation environnementale précise | PDT-005 |
| [PDT-008](../suites/pdt-008-publicite-comparative.md) | Revue d'une comparaison publicitaire déterminée | PDT-005 |
| [PDT-009](../suites/pdt-009-avis-influence.md) | Revue d'un témoignage ou contenu d'influence | PDT-005 |
| [PDT-010](../suites/pdt-010-role-service-numerique.md) | Fiche de rôle et champ d'un service numérique projeté | PDT-001 |
| [PDT-011](../suites/pdt-011-dossier-securite-produit.md) | État des justificatifs de sécurité d'un bien de consommation | PDT-001 |
| [PDT-012](../suites/pdt-012-question-ponctuelle.md) | Orientation d'une question produit sans verdict automatique | Aucune |
| [PDT-013](../suites/pdt-013-preferences-produits.md) | Préférences produit volontaires et modification ciblée | Aucune |
| [PDT-014](../suites/pdt-014-dossier-produit.md) | Dossier isolé par produit/version/campagne | Aucune |
| [PDT-015](../suites/pdt-015-radar-lancements.md) | Rapport ponctuel des lancements à instruire | PDT-012 |
| [PDT-016](../suites/pdt-016-cookbook-radar.md) | Variante headless bornée du radar | PDT-015 |
| [PDT-017](../suites/pdt-017-checklist-actualite.md) | Checklist d'actualité produit/publicité traçable | Aucune |
| [PDT-018](../suites/pdt-018-prix-promotions.md) | Examiner une annonce de prix ou de promotion | PDT-005 |
| [PDT-019](../suites/pdt-019-parcours-commercial.md) | Documenter les engagements d’un parcours commercial | Aucune |
| [PDT-020](../suites/pdt-020-qualifier-rep.md) | Qualifier une mise sur le marché au regard de la REP | Aucune |
| [PDT-021](../suites/pdt-021-preparer-declaration-rep.md) | Rapprocher les pièces d’une déclaration REP | PDT-020 |
| [PDT-022](../suites/pdt-022-verifier-idu.md) | Vérifier les justificatifs et la communication d’un IDU | PDT-020 |
| [PDT-023](../suites/pdt-023-marquage-emballage.md) | Examiner le marquage d’un emballage pour un marché | Aucune |
| [PDT-024](../suites/pdt-024-dossier-emballage-ppwr.md) | Constituer la fiche factuelle d’un emballage PPWR | Aucune |
| [PDT-025](../suites/pdt-025-calendrier-ppwr.md) | Préparer le calendrier PPWR d’un emballage identifié | PDT-024 |

PDT-001 possède le contrat de fiche lancement ; PDT-002 la grille locale
unique, sans doublon inline. PDT-003 possède la fiche avant/après et PDT-004
consomme cette fiche ou son instantané manuel. PDT-005 possède le contrat
d'allégation : texte/visuel exact, localisation, interprétation, public,
produit, date, canal, preuves et états. PDT-006 à PDT-009 ne réécrivent pas
cette collecte. Une même publicité peut appeler plusieurs examens ; les
retouches proposées par l'un ne résolvent pas les inconnues des autres.

PDT-002 reste utile sans PDT-006 à PDT-011 : il marque ces contrôles
« à instruire » avec pièces/interlocuteur, sans conclusion globale. Il ne
rejoue pas les branches héritées pour combler un manque. Aucun cycle de
dépendances : les relais métier sont des fiches de questions, pas des
prérequis d'installation. Le radar n'est jamais un moteur d'approbation.

## Répartition des contrôles

| Domaine principal | Travail propre et relais |
|---|---|
| Produit/publicité | Qualification du lancement, cohérence des engagements et pièces, risque du changement, allégations et preuves, rôle opérateur et dossier sécurité bornés. |
| Consommation — DOM-001 | Revue de CGV B2C, rétractation, garanties, essai/abonnement et réclamation d'un acheteur. Produit relève la question et les écrans nécessaires ; pas de deuxième revue des CGV. Les règles de pratiques commerciales utiles à la publicité restent embarquées chez produit. |
| Données — EXIST-003/PRV | Traitement par finalité, bases, information, traceurs/prospection, AIPD, sous-traitance et droits. Une notice ou une PIA fournie n'est pas une preuve suffisante du lancement. |
| IA — EXIST-005 | Qualification de l'usage/système/rôle, obligations IA et contrat fournisseur IA. AIPD et analyse IA restent distinctes, sans double évaluation automatique. |
| Numérique — DOM-034 | Contestations d'utilisateurs et modération ; PDT-010 qualifie l'opérateur et les questions de champ, sans recours individuel. |
| Contrats/PI/secteurs | B2B chez commercial, marque/OSS/licence chez IP, santé/finance/emploi/etc. dans le domaine compétent. Règle sectorielle seulement après faits déclencheurs ; pas d'avis sectoriel universel. |

## Plan de recherche pour les futures implémentations

Les lignes suivantes sont des **pistes à vérifier**, pas des règles actuelles
ni des dates d'application validées. Ouvrir les textes et versions applicables
à la date des faits, établir champ/rôle/transitions, citer le passage réellement
lu selon BASE-005. Distinguer loi, acte UE, jurisprudence, guide d'autorité,
recommandation professionnelle et règle privée de plateforme. Les voies
officielles BASE-010 sont disponibles en maintenance en cas d'accès bloqué ;
ni ces scripts racine ni un abonnement ne sont une dépendance runtime.

| Question | Sources et faits à rechercher lors du lot | Propriétaire |
|---|---|---|
| Qualité des parties et marché | Code de la consommation, Code civil, textes UE pertinents ; activité et destinataires effectifs, professionnel/consommateur/non-professionnel, canal, langue, pays ciblés, dates. Association ou professionnel acheteur n'est pas assimilé mécaniquement à un consommateur. | PDT-001/002/003/012 |
| Engagements de lancement | Offre/écrans/docs/contrats versionnés, dispositions de consommation utiles à l'information et aux pratiques commerciales, accessibilité selon service/acteur/date ; DGCCRF et autorités désignées à identifier. Rétractation/CGV complètes restent chez consommation. | PDT-002 |
| Allégations et pratiques | Code de la consommation et textes français de publicité correspondant au support, textes UE pertinents et jurisprudence officielle ; exactitude, présentation globale, omissions, langue/mentions. DGCCRF et autorité sectorielle selon champ ; ARPP est une référence déontologique distincte de la loi. | PDT-005/006 |
| Environnement | Dispositions françaises consommation/environnement sur allégations, neutralité carbone, labels, mentions et preuves ; actes UE relatifs aux pratiques commerciales/environnement effectivement applicables. Vérifier adopté/proposé, transposition et application ; ne pas présenter « Green Claims » ou Digital Omnibus comme droit en vigueur depuis leur seul nom. DGCCRF/ADEME comme guides à distinguer des textes. Périmètre produit/emballage/activité, cycle de vie, compensation, méthode, date et base de comparaison. | PDT-007 |
| Comparaison | Code de la consommation, textes UE et jurisprudence sur publicité comparative ; concurrents identifiables, biens/besoins comparables, critères, échantillon, date et dénigrement. PI pour usage de marque distinct. | PDT-008 |
| Avis et influence | Textes français d'influence commerciale/publicité, consommation et actes UE dans le champ ; relation commerciale, gratuité/avantage, éditeur/annonceur/agence, audience mineure, support, modifications d'image/contenu synthétique si pertinentes. DGCCRF et autorité compétente selon secteur ; règle privée du réseau séparée. | PDT-009 |
| Service numérique | DSA/LCEN et textes complémentaires seulement si fonctions/rôle/champ le justifient ; service propre, hébergement, marketplace et autre intermédiation à distinguer. Taille, établissement, destinataires UE et éventuelle désignation à rechercher avant obligation ; ARCOM/Commission selon compétence à vérifier. DMA, Data Act et autres actes ne sont pas chargés par défaut : question et critères de champ d'abord. | PDT-010 |
| Sécurité d'un bien | Règlement UE sur la sécurité générale des produits et articulation avec textes sectoriels, Code de la consommation et textes français pertinents ; fabricant/importateur/distributeur, catégorie, mise sur marché/date, lot, notice, traçabilité et évaluations disponibles. Autorité/notification/rappel à rechercher si signal de danger. Pas de CE universel, expertise ni test de laboratoire déduit d'un document. | PDT-011 |
| Risque et évolution | Obligation applicable malgré absence de veille/sanction récente ; preuve de mesure réalisée versus prévue, version produit, préjudice pour personnes et engagement contractuel. Sources ciblées par risque ; goût du risque ne supprime pas une obligation. | PDT-003/004 |
| Secret et diffusion | Textes français et jurisprudence pertinents selon auteur, qualité, objet et destinataire ; politique de confidentialité interne séparée de protection légale. Aucun label ne garantit le secret ou un canal « safe ». | Chaque tranche, PDT-013/014 pour le profil |
| Actualité | Source émettrice, statut, version, date de publication/application, mesure transitoire et périmètre effectivement relu. Une sanction ou réforme annoncée n'est pas un calendrier général. | PDT-017 et chaque tranche |

## Exclusions et livraisons

Pas de lancement/publication, avis de conformité générale, notification
d'autorité, rappel produit, certification, audit technique, test de sécurité,
modification de ticket, diffusion Slack ou configuration de scheduler dans
ce cadrage. Le signal de danger reçoit une orientation urgente ciblée ;
la procédure de rappel/notification devra être découpée séparément.
PDT-010 ne livre pas tous les contrôles des plateformes et PDT-011 ne livre
pas une homologation de toutes les catégories de produits.

Les fichiers « à créer » des suites sont des livrables futurs, jamais des
ressources annoncées disponibles. Chaque lot reste autonome dans son paquet,
documente sa couverture et ses modes encore hérités, inscrit NOTICE local et
racine s'il touche le paquet, et synchronise les métadonnées modifiées. La
sortie doit expliquer faits, inconnues, pièces et prochaine démarche en
langage clair selon USAGE-001, avec lecture par une personne non juriste
dans la recette future. La portée de ce cadrage figure dans la
[vérification](exist-004-verification.md).

## Complément marketing et emballages — 16 octobre 2026

La [matrice des 140 frictions](exist-004-frictions-utilisateurs.md) ajoute PDT-018 à PDT-025 : annonce de prix, parcours commercial, qualification REP d’un flux, préparation de déclaration, IDU, marquage, fiche d’emballage PPWR et calendrier conditionnel. Les tableaux de rôles REP et PPWR sont distincts. PDT-007/009 gardent leurs revues d’allégations et d’influence, IA-005 la transparence IA, commercial le contrat d’éco-organisme ou d’agence, consommation la réclamation de l’acheteur.

PDT-020 possède la fiche flux/pays/filière/rôle REP ; PDT-021 consomme cette fiche ou son équivalent manuel et possède le rapprochement de déclaration ; PDT-022 possède la preuve d’identification et de communication. PDT-023 possède la revue de marquage d’une maquette pour un marché. PDT-024 possède la nomenclature, les usages et les rôles PPWR ; PDT-025 possède le calendrier par disposition et ses conditions, sans double qualification REP. Le calendrier métier est embarqué chez produit ; la veille ne remplace pas ces références.

Les huit ajouts sont proposés et ne changent pas la première tranche suggérée PDT-001. Les bilans et empreintes historiques couvrent les 17 propositions initiales ; portée et contrôles de l’ajout dans le [relevé dédié](exist-004-frictions-verification.md).

## Complément emballages export — 19 octobre 2026

Sur remarque de l'utilisateur, exportateur de couteaux, trois stories
`proposee` complètent PDT-020 à PDT-025 sans implémentation :

| Story | Sortie bornée | Dépendance |
|---|---|---|
| [PDT-026](../suites/pdt-026-fabricant-emballage-ppwr.md) | Rôle de fabricant PPWR d'une boîte à son nom ou sa marque et obligations documentaires | PDT-024 |
| [PDT-027](../suites/pdt-027-rep-emballages-autres-pays.md) | REP emballages d'une vente directe dans un autre État membre ou un pays tiers | PDT-020 |
| [PDT-028](../suites/pdt-028-ventiler-emballages-export.md) | Ventilation des emballages déclarés entre France, Union et export | PDT-020, PDT-021 |

Le volet emballages de la fiche pays douanière DOU-017 renvoie à PDT-027.
