---
id: IA-017
titre: "Analyser un changement de texte pour un système et un rôle"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-002]
---

# IA-017 — Analyser un changement de texte pour un système et un rôle

## Objectif et résultat attendu

Un changement déterminé produit une note de delta : ancienne/nouvelle exigence, champ/date, preuves actuelles et actions proposées pour un rôle.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/reg-gap-analysis/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/ecart-evolution-reglementaire.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Texte modificatif ou guide invoqué, versions ancienne/nouvelle, IA-002 et qualifications complémentaires si nécessaires, rôle, système/version, pièces des pratiques et dates.

## Travail attendu

Vérifier statut du changement avant extraction : projet, adopté, publié, applicable et transitions. Un guide nouveau ne modifie pas à lui seul une obligation. Borner une passe au changement indiqué, au système et au rôle ; ne pas refaire tous les régimes. Comparer exigences réellement applicables et preuves de réalisation, pas seulement profil. Distinguer manque de preuve, écart établi, mesure proposée et risque accepté ; cette acceptation ne rend pas l'obligation satisfaite. Toute date d'action interne est étiquetée ; échéance légale nécessite calcul. Pas d'absence de besoin depuis seules sanctions futures.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher texte original/modificatif et actes liés sur EUR-Lex ou publication nationale officielle pertinente, puis éventuels guides d'autorités avec statut ; préciser ce qui change réellement et quand pour l'acteur.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Aucune exigence ni date n'est tirée d'un résumé seul ; no gaps signifie seulement aucun écart établi sur la couverture lue, jamais conformité globale.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : V01 — Acte modificatif précisément identifié : delta avant/après, rôle déployeur et preuves du système, sans conformité globale.
- Cas limite : V02 — Brief affirmant que Digital Omnibus a reporté toutes les dates, sans texte fourni : statut et portée à vérifier, ancien calendrier non remplacé de mémoire.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Veille permanente, analyse de tous les systèmes, corrections techniques, dépôt, notification et action externe.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
