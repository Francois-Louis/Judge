---
id: IA-016
titre: "Relire un corpus borné de sorties contre la politique IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-015]
---

# IA-016 — Relire un corpus borné de sorties contre la politique IA

## Objectif et résultat attendu

Un rapport ponctuel de dérive décrit corpus lu/non lu, états des sorties, contradictions et décisions restant à prendre.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/policy-monitor/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/revue-sorties-politique.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Corpus explicitement désigné, politique/version, dernier rapport/jalon revu s'il existe, manifestes de fichiers et métadonnées disponibles, périmètre de dossier.

## Travail attendu

Réutiliser le contrat d'écart IA-015 et préserver source, version, statut et décision réelle. Brouillon AIA, triage conditionnel ou contrat analysé ne prouve pas usage mis en œuvre. Inclure modifications tardives, même date, erreurs de lecture et fichiers hors format ; journaliser couvertures/manques. Un corpus vide donne aucun document examiné, pas politique à jour. Présenter le rapport avant mise à jour du jalon humain, sans sauter les erreurs ou pièces non revues ; un acquittement ne signifie pas conformité. Aucun balayage de dossiers voisins ni ordonnanceur implicite.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Corpus et politique réellement lus ; droit invoqué dans une sortie à revérifier selon version/faits, jamais hérité comme règle vérifiée. Références IA-020 si disponibles dans le paquet, sinon méthode locale et limites explicites.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Le rapport est reproductible à périmètre égal ; gravité amont conservée ou changement motivé, rendu HTML protégé et aucun envoi automatique.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : M03 — Corpus avec AIA brouillon, contrat signé et preuve d'usage : états distincts, seuls faits prouvés qualifiés comme pratique réelle.
- Cas limite : M04 — Corpus vide, fichier illisible et fichier modifié le jour du jalon : couverture incomplète, pas d'all clear ni avance de curseur qui supprime ces éléments.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Veille juridique, scheduler, surveillance de comptes, modification automatique de politique et lecture inter-dossiers.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
