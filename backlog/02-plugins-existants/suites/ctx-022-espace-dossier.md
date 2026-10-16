---
id: CTX-022
titre: "Isoler les espaces de dossiers contentieux"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-022 — Isoler les espaces de dossiers contentieux

## Objectif et résultat attendu

Création/sélection/fermeture d’espace gardent identifiant stable sans collision ni lecture croisée.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/matter-workspace/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/espace-dossier-contentieux.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Personne/organisme, identifiant, action, métadonnées autorisées et modèle métier CTX-014 ou fiche équivalente.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Posséder contrat espace/actif seulement, consommer schéma métier sans double ouverture ou dépendance circulaire. Contrôler slug, collisions, liens/chemins via helper, liste minimale. related_matters ne donne pas droit aux pièces. Archivage/espace et clôture métier distincts ; retirer MSA/Delaware et header protecteur. Aucune migration/suppression automatique.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Contrat BASE-008 et méthode ; données/conservation si changement d’accès, aucune qualification du fond.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Sélectionner un espace ne révèle aucun contenu d’un autre ; collision ou lien est refusé et aucune seconde entrée métier n’est créée.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : ES01 — Deux affaires d’une personne : changement actif garde notes/sorties dans le bon espace.
- Cas limite : ES02 — Slug déjà présent, lien symbolique ou related_matters autre client : refuser écrasement, sortie de racine et lecture liée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Migration transverse, fusion d’affaires et effacement.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

