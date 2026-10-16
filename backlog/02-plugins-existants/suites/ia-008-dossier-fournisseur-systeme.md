---
id: IA-008
titre: "Préparer les pièces d'un fournisseur de système"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-004]
---

# IA-008 — Préparer les pièces d'un fournisseur de système

## Objectif et résultat attendu

Un fournisseur possible d'un système potentiellement à haut risque obtient l'état des pièces à instruire, sans certificat ni conformité réputée acquise.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/aia-generation/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/dossier-fournisseur-systeme.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Qualification par acteur et voie haut risque, finalité/versions, documentation technique fournie, gestion qualité/risques déclarée, produit associé, contrats et calendrier marché/service.

## Travail attendu

Borner à un système intégré proposé par une PME sous son nom. Recenser documents attendus selon les textes réellement applicables : objet, auteur, version, extrait lu, statut et manque. Séparer existence d'un fichier et contenu vérifié ; une AIA interne, un test ou un dossier fournisseur tiers ne prouve pas conformité du système intégré. Identifier procédure, organisme/autorité et expertise à rechercher selon voie, sans promettre auto-évaluation suffisante. Rôle fournisseur modèle et chaîne produit restent distincts. Ne pas simuler l'exécution d'essais ou la clôture d'une évaluation de conformité.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher obligations fournisseur de système et cadre documentaire/procédural dans le règlement IA et textes sectoriels retenus, avec actes, normes et effets de leur publication au JO vérifiés séparément.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] L'état des pièces ne devient jamais déclaration de conformité, marquage ou autorisation ; chaque attente réglementaire est sourcée pour le système et la date.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : F01 — PME commercialisant un outil de présélection sous son nom : matrice des pièces/version/source/manques à instruire.
- Cas limite : F02 — Seul un certificat du modèle amont ou une AIA est fourni : ne pas conclure conformité du système ; rôle et procédure demeurent à établir si faits absents.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Certification, essais, rédaction intégrale du dossier technique, système qualité complet, obligations GPAI et dépôt officiel.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
