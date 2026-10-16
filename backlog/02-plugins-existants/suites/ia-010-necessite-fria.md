---
id: IA-010
titre: "Déterminer si une FRIA doit être instruite"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-004]
---

# IA-010 — Déterminer si une FRIA doit être instruite

## Objectif et résultat attendu

Une fiche vérifie les critères de nécessité d'une analyse d'impact sur les droits fondamentaux, ou indique précisément les faits empêchant de conclure.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/aia-generation/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/necessite-fria.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

IA-002/004, qualité exacte du déployeur, activité/service rendu, usage et domaine, parties affectées, dates et éventuelles analyses existantes.

## Travail attendu

Rechercher le champ de la FRIA et ses exceptions à partir du rôle, du type d'organisme/service et du cas d'usage. Ne pas déduire nécessité de la résidence UE, du seul haut risque ou du seul mot public. Distinguer autorité publique, organisme et opérateur privé assurant un service avec pièces à l'appui. Une conclusion hors champ ne vaut ni conformité ni absence d'AIPD. Si une analyse préexiste, contrôler version/portée ; ne pas la substituer par intitulé. La fiche prépare IA-011 seulement lorsque le besoin et le périmètre sont établis.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher disposition FRIA complète du règlement IA, renvois, exceptions, champ personnel/matériel, calendrier et documents officiels pertinents, avec statut des guides/formulaires distinct.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Nécessaire/non établie/hors champ est motivé par source et faits ; une pièce ou version manquante reste visible et l'AIA ne ferme pas la question.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : R01 — Organisme déclarant assurer un service public utilisant un outil d'accès : demander sa qualité, la mission et le fonctionnement avant conclusion motivée.
- Cas limite : R02 — RH privé ou assurance/crédit invoqués avec haut risque allégué : vérifier chaque critère propre, pas de FRIA universelle ni d'exclusion depuis privé.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Projet FRIA complet, analyse sectorielle de crédit/assurance, AIPD et notification à l'autorité.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
