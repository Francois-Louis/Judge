---
id: IA-020
titre: "Tracer sources, actualité et calendrier IA par disposition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-020 — Tracer sources, actualité et calendrier IA par disposition

## Objectif et résultat attendu

Une checklist d'actualité, un relevé de recherche et une fiche temporelle rendent chaque obligation alléguée vérifiable sans calendrier global figé.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/references/currency-watch.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/sources-calendrier.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Question/disposition, système/usage/acteur, versions des textes, dates des faits/marché/service/modification, sources consultables et chronologie probante.

## Travail attendu

Remplacer la watch list par pistes et statut par entrée : passage/version, URL, tentative/consultation réelle, champ, statut documentaire et applicabilité séparés. Distinguer règlement adopté/publié/entré en vigueur et application par disposition, transition et rôle ; réforme alléguée sans texte reste non vérifiée. Identifier autorités françaises par compétence réelle, sans CNIL universelle ni transposition présumée. Pour un délai, nature/fondement/déclencheur/preuve/calcul/exceptions et contrôle adapté ; sinon a-determiner. Dates de revue internes séparées. Une entrée actualisée ne rafraîchit pas les autres ; journal versionné et cloisonné, avis ancien non repris sans vérifier faits et source.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher EUR-Lex/JO pour règlement IA, rectificatifs/modifications/actes associés ; Commission/Bureau IA, textes officiels français de compétence et autorités dont CNIL selon question. Guides, normes et codes de pratique gardent statut/effet distincts. Accès alternatifs BASE-010 sans abonnement requis.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Complément des frictions IA

Points 33 et 42 et calendrier de la [matrice](../exist-005-annexes/exist-005-frictions-utilisateurs.md) : vérifier l'« AI Omnibus » et les dates alléguées sur texte officiel, sans reprendre le tableau source comme référence. Ajouter un cas de recette où une annonce de report n'a aucun texte modificatif identifié : statut non vérifié et conclusion dépendante réservée, sans calendrier de substitution.

Pour une référence juridique fournie par une IA, comparer identifiant, juridiction/auteur, date, passage et version réellement consultée à la proposition qu'elle prétend soutenir. Sortie attendue : référence confirmée, texte trouvé mais hors champ, introuvable après recherches tracées ou inaccessible ; ne pas affirmer une inexistence depuis un simple échec d'accès. BASE-005 s'applique à chaque sortie du dépôt sans dépendre de l'exécution de cette story. Les études scientifiques ou les performances d'un produit ne sont pas validées par ce contrôle juridique.

## Critères d'acceptation

- [ ] Mise à jour partielle garde les autres entrées anciennes ; un guide ou communiqué ne devient pas texte modificatif, et une échéance interne n'est jamais légale.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : S01 — Une disposition et un acteur avec événement daté prouvé : relevé temporel sourcé ou réserve explicite, sans généraliser aux autres dispositions.
- Cas limite : S02 — URL officielle inaccessible, modification alléguée et date de mise en service inconnue : alternatives tracées, pas de consultation inventée ni de date butoir substituée.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Corpus exhaustif, calendrier certifié de tout le règlement, abonnement API, veille planifiée et calcul sans déclencheur prouvé.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
