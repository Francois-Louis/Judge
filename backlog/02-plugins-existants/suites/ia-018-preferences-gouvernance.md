---
id: IA-018
titre: "Configurer des préférences de gouvernance IA volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-018 — Configurer des préférences de gouvernance IA volontaires

## Objectif et résultat attendu

Une configuration volontaire, minimale et reprenable conserve les réponses confirmées ; un changement ciblé ne relance pas tout l'entretien.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/cold-start-interview/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/skills/customize/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Demande de configuration/modification, profil fork et partagé s'ils existent via helper, sections souhaitées, réponses et seules pièces expressément données.

## Travail attendu

Aligner modèle embarqué, modèle inline, quick/full/redo/check-integrations et customize. Séparer faits d'organisme, préférence, décision documentée et règle juridique ; rôle et catégorie restent attachés aux systèmes. Préserver pause, sections voisines et inconnues, sans US defaults, import cache ni déduction personnelle. Une réponse ponctuelle ne force pas configuration complète. Si profil durable absent, entretien neuf BASE-008 avant création. Distinguer connecteur déclaré/testé et capacité réelle, sans appel de test inutile. Le champ partagé ne peut être créé depuis une simple promesse du texte ; évolution du format commun hors tranche.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Méthode BASE-005 et contrat BASE-008 embarqués. Toute règle chiffrée ou juridique énoncée en entretien reste alléguée jusqu'à vérification officielle ; préférence de risque ne la rend pas applicable.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Quick/full et customize produisent un schéma cohérent ; aucune reclassification des systèmes ni réécriture des évaluations depuis un changement d'appétence.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : C05 — Petite structure sans historique choisit seulement destinataire et format : réponses confirmées, champs juridiques non remplis par défaut.
- Cas limite : C06 — Profil interrompu puis changement d'un contact avec modification concurrente : reprise sans perte, digest requis et conflit signalé avant écriture.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Import d'une autre distribution, synchronisation transverse des modèles, qualification exhaustive des systèmes et connexion de comptes.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
