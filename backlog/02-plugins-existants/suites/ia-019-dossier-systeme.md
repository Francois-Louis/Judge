---
id: IA-019
titre: "Isoler un dossier par organisme, système et version"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-019 — Isoler un dossier par organisme, système et version

## Objectif et résultat attendu

Un utilisateur peut séparer systèmes, versions et organismes, y compris dans une équipe interne, avec historique et archives contrôlés.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/matter-workspace/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/dossier-systeme.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Organisme/système/usage/version, propriétaire et destinataires, nom de dossier, périmètre de pièces, éventuel profil actif et règle de conservation à instruire.

## Travail attendu

Adapter new/list/switch/close/none et le modèle aux dossiers IA ; ne pas rendre l'isolation invisible par statut in-house. Relier inventaire et dossier par identifiant sans dupliquer le registre ni lire d'autres organismes. Liste minimale, cross-matter activé insuffisant sans demande ciblée ; related matters n'autorise pas l'ouverture. Refuser collisions active/archive et slug invalide sans normalisation silencieuse. Archiver sans effacer ni promettre conservation illimitée ; changement de dossier actif explicite et digest pour état modifié. Journal de vérification suit le dossier isolé, aucun fait client dans un log partagé.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Contrat BASE-008 et méthode locale ; si durée/protection de conservation est affirmée, rechercher le fondement pour les données, l'auteur et la mission réels. Aucun secret automatique depuis un marquage.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Aucun accès durable ne contourne le helper ; tests sur racine factice, archives préservées et aucune protection juridique garantie par en-tête.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : W01 — Deux systèmes d'un même organisme et deux versions : sorties et faits dans les bons dossiers, liste minimale sans lecture croisée.
- Cas limite : W02 — Archive homonyme, lien symbolique ou demande de comparer un autre organisme : refus de collision/lien et demande de périmètre explicite, sans fuite de contenu.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Politique de conservation complète, contrôle des conflits professionnels, migration/import et purge de données.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
