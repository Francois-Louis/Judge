---
id: IA-007
titre: "Documenter les obligations d'un déployeur pour un usage"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-004]
---

# IA-007 — Documenter les obligations d'un déployeur pour un usage

## Objectif et résultat attendu

Un déployeur qualifié obtient une fiche bornée des obligations pour un usage et une version, avec calendrier, pièces et actions attribuées.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/aia-generation/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/obligations-deployeur.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

IA-002/004 ou équivalent vérifié, rôle et qualification établis/conditionnels, notice fournisseur, organisation d'usage, contrôle humain, journaux, personnes affectées et dates.

## Travail attendu

Pour un usage RH de présélection, rechercher les obligations propres au déployeur et justifier chaque ligne source/champ/date/preuve/manque/action. Contrôle humain et surveillance ne sont pas présumés réalisés depuis une politique. Séparer obligation légale, instruction fournisseur, mesure interne et échéance d'équipe. Une qualification conditionnelle donne plusieurs branches et réserves. Fournir questions ciblées sur information/consultation travail, AIPD/privacy, besoin de FRIA ; aucune de ces procédures n'est réputée exécutée. Ne pas ajouter obligations fournisseur dans la même colonne.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher obligations déployeur du règlement IA, dispositions applicables à l'usage et transitions ; autorités françaises compétentes à identifier pour la question précise. Les règles RH et RGPD ont une recherche sectorielle distincte.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Aucune ligne n'est déclarée satisfaite depuis le seul profil ; une échéance nécessite source, déclencheur, preuve de date et calcul, sinon a-determiner.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : D01 — Présélection RH : rapprochement notice, responsables, contrôle réel et obligations sourcées, avec preuve manquante conservée.
- Cas limite : D02 — Système déjà exploité avant une date transitoire alléguée puis substantiellement modifié : chronologie et version à rechercher, pas d'exemption depuis l'ancienneté.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Obligations de tous les acteurs, audit technique, décision d'emploi, enregistrement officiel et notification d'incident.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
