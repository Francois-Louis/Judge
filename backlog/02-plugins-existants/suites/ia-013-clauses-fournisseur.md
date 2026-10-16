---
id: IA-013
titre: "Proposer une modification ciblée de clause IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-012]
---

# IA-013 — Proposer une modification ciblée de clause IA

## Objectif et résultat attendu

Un écart IA documenté produit une modification minimale et une explication du risque résiduel pour la négociation.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/vendor-ai-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/clauses-fournisseur.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Carte IA-012 ou équivalent, clause exacte et contexte/hiérarchie, objectif de l'acheteur, droit à rechercher, positions et interlocuteur s'ils existent.

## Travail attendu

Borner une passe à un écart, par exemple réutilisation des entrées ou engagement répercuté aux fournisseurs amont. Distinguer exigence légale, choix interne et demande commerciale. Proposer ajout/suppression au plus petit niveau lisible avec clause d'origine et conséquence ; si remplacement total nécessaire, justifier. Vérifier cohérence avec définitions, responsabilité, suppression et contrat principal dans la couverture fournie. Ne pas garantir opposabilité, propriété des sorties ni acceptation. Une position absente produit options explicites sans créer de préférence durable ni feu rouge automatique.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher droit applicable et textes IA utiles à la clause précise ; distinguer obligations légales de clauses volontaires. Privacy/IP/commercial gardent leur analyse propre, sans dépendance installée.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Texte initial, modification, objectif, source et limite sont rapprochés ; aucun modèle anglais ou fallback automatique n'est présenté comme règle française.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : C03 — No training promis mais aucune répercussion documentée : proposition ciblée avec portée et responsable contractuel identifiés.
- Cas limite : C04 — Amendement demandé alors que clause de priorité manque et aucune position interne n'existe : options conditionnelles, demande de pièce et risque résiduel, pas de signature conseillée.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Contrat complet, réécriture globale, validation RGPD/PI, envoi au fournisseur et signature.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
