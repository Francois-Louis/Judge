---
id: IA-006
titre: "Distinguer modèle GPAI et système utilisateur"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-002]
---

# IA-006 — Distinguer modèle GPAI et système utilisateur

## Objectif et résultat attendu

Une fiche de modèle liée aux systèmes utilisateurs distingue objet, version, rôle de l'acteur et questions de portée GPAI/risque systémique.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/ai-inventory/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/qualification-modele-gpai.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Modèle/version, documentation et mise à disposition, capacités, entraînement/modifications déclarées, acteur sous son nom, licence, calcul documenté et désignation alléguée.

## Travail attendu

Séparer modèle et intégration applicative ; ne pas remplacer la catégorie du système par gpai. Rechercher critères de généralité, risque systémique, présomptions/désignations, exceptions et transitions avec leurs preuves. Une API tierce ne fait pas automatiquement de l'acheteur un fournisseur de modèle ; un poids ouvert ne prouve pas exemption générale. Une donnée de calcul absente reste inconnue et n'est pas estimée depuis la réputation. Produire questions et sources à obtenir ; les obligations complètes du fournisseur de modèle restent hors tranche.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher chapitre modèles GPAI du règlement IA et actes associés à jour sur EUR-Lex, documents officiels Commission/Bureau IA et éventuelle désignation. Distinguer texte contraignant, guide et code de pratique, sans seuil figé de mémoire.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Modèle, système, acteur et version sont séparés ; catégories et seuils ont source/statut ou restent à établir, sans case gpai qui écrase haut risque.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : G01 — Même modèle intégré dans un assistant et un filtre RH : fiche modèle unique référencée, qualifications des deux systèmes distinctes.
- Cas limite : G02 — Modèle open weights modifié dont le calcul et le statut sont inconnus : aucune exemption ni absence de risque systémique déclarée.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Audit de calcul, entraînement, obligations exhaustives du fournisseur de modèle et validation de licence PI.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
