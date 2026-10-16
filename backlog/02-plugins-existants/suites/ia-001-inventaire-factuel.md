---
id: IA-001
titre: "Inventorier un système IA sans le classer"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-001 — Inventorier un système IA sans le classer

## Objectif et résultat attendu

Une petite structure obtient une fiche factuelle d'un assistant interne, identifiée et versionnée, avec usages, acteurs déclarés, stade et pièces manquantes.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/ai-inventory/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/inventaire-factuel.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Nom de l'outil, version/configuration connues, usages, organisme, responsable, données décrites sans contenu personnel, composants/fournisseurs, pays et dates déclarées, pièces disponibles.

## Travail attendu

Séparer enregistrement et classification. Prévoir list/add/edit/show avec identifiant stable, provenance par champ, inconnue explicite et rattachement système/version/usage. Garder rôle juridique, catégorie et obligations non déterminés tant qu'ils ne sont pas analysés. Une modification factuelle marque l'analyse précédente à revoir sans l'écraser. Distinguer inventaire et registre interne d'autorisations. Afficher couverture et date interne de revue sans la présenter comme délai légal. Corriger le dispatch classify vers la future qualification ou une fiche de questions, sans exécuter le classement hérité.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

La fiche factuelle ne fixe aucune obligation de registre réglementaire. Si une telle obligation est invoquée, rechercher champ, rôle et texte exact du règlement IA avant de la qualifier ; contrat et notice fournis restent des sources de faits allégués.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Un ajout conserve source et inconnues ; un edit d'un seul champ préserve les autres fiches et signale les qualifications devenues possiblement obsolètes.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : I01 — Association décrivant un assistant rédactionnel : fiche utile sans profil ni registre préalable ; aucune catégorie juridique créée.
- Cas limite : I02 — Même outil utilisé pour résumer des notes puis pour filtrer des CV : deux usages liés, versions et manques visibles, pas de classement commun automatique.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Classification juridique, obligations, import massif, dédoublonnage silencieux, autorisation de déploiement.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
