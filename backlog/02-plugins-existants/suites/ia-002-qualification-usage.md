---
id: IA-002
titre: "Qualifier un usage IA, ses acteurs et son champ"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-001]
---

# IA-002 — Qualifier un usage IA, ses acteurs et son champ

## Objectif et résultat attendu

Une fiche conditionnelle distingue objet système/modèle, fonction, acteurs, rôles possibles, territoires et dates avant de choisir une branche juridique.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/use-case-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/qualification-usage.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Fiche IA-001 ou instantané manuel équivalent, documentation de fonctionnement/finalité, contrats d'acteurs, nom de commercialisation, modifications, pays et chronologie.

## Travail attendu

Rechercher la définition et les exclusions avant d'appliquer le règlement. Séparer finalité prévue et usage effectif, personne affectée et lieu d'utilisation des sorties. Qualifier chaque acteur pour ce système et cette activité, avec plusieurs rôles possibles. Un fine-tuning, une revente ou une marque propre appelle les critères précis, pas une conversion automatique en fournisseur. Comparer le registre interne seulement après cette collecte ; distinguer préférence, décision interne et droit. Retirer APPROVED et AIA systématique sans correspondance. Orienter vers pratique, haut risque, transparence et modèle selon faits ; ne pas appeler les branches encore héritées.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher règlement IA sur EUR-Lex : définitions, champ personnel/territorial/matériel, exclusions et règles de changement de rôle, dans la version et les transitions pertinentes. Vérifier séparément portée EEE et éventuelles activités hors UE.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Un registre disant approved et un profil disant Both ne remplacent ni qualification par système ni recherche de champ ; une fiche reste possible sans profil complet.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : Q01 — Assistant interne acheté en SaaS, établissement français et usage décrit : acteurs et hypothèses motivés, sans catégorie définitive depuis le mot assistant.
- Cas limite : Q02 — Fournisseur hors UE, sorties utilisées en France et modification de finalité alléguée : rattachements et rôle réservés tant que contrats et fonctionnement manquent.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Avis de conformité, taxonomie universelle, obligation FRIA/AIPD déduite d'un mot, autorisation interne.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
