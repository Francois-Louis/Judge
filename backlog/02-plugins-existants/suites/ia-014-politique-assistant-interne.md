---
id: IA-014
titre: "Préparer une politique pour un assistant rédactionnel interne"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-014 — Préparer une politique pour un assistant rédactionnel interne

## Objectif et résultat attendu

Une petite structure dispose d'un projet de politique limité à la rédaction interne avec un assistant, adapté aux sections choisies et aux usages réels.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/policy-starter/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/politique-assistant-interne.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Organisme/public interne, usages/outils, données autorisées envisagées, contrôle/destinataires, politique existante et contrats disponibles, sections demandées et responsables possibles.

## Travail attendu

Accepter un périmètre déjà exprimé, proposer un périmètre minimal si besoin puis recueillir seulement les faits manquants. Séparer règle interne choisie, obligation légale recherchée et mesure non réalisée. Rédiger usages/données/contrôle/signalement selon sections retenues, avec choix ouverts et preuves manquantes ; ne pas promettre confidentialité ou absence d'entraînement sans contrat. Préciser adoption, information, formation/littératie et volet RH à instruire selon faits ; pas de sanction automatique. Les modèles publics sont des inspirations identifiées, pas droit applicable. Aucun GC, seed ou profil complet imposé.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher règlement IA pour les points pertinents, CNIL et sources officielles françaises/Commission selon usage ; obligations RH et règles professionnelles françaises seulement si public concerné. Vérifier statut des guides et modèles, sans socle ABA/NIST par défaut.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Le projet n'affirme aucune conformité ou adoption ; engagements proposés, faits prouvés et décisions à prendre sont distingués, avec sources réellement lues.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : P01 — Association choisissant usages, données et contrôle pour un assistant interne : brouillon compréhensible, responsables non inventés et choix restants visibles.
- Cas limite : P02 — Demande discipline ou outil d'évaluation des salariés : expliciter changement de périmètre et relais travail ; ne pas étendre discrètement la politique rédactionnelle.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Politique de tous les usages IA, règlement intérieur, procédure disciplinaire, certificat de formation et diffusion.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
