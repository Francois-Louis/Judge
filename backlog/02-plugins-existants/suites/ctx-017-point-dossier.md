---
id: CTX-017
titre: "Préparer un point sur un dossier"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-014]
---

# CTX-017 — Préparer un point sur un dossier

## Objectif et résultat attendu

Un point daté expose faits récents documentés, questions et couverture d’un dossier.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/matter-briefing/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/point-dossier.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Dossier/history/log ou équivalent, pièces choisies, fiches de dates, date de référence, destinataire et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Conserver résumé/changements/questions ; distinguer information récente et ancienne. Ne pas recalculer exposition, probabilité ou délai depuis score ; reprendre auteur/date/statut et manques. Lister lu/non lu, aucun all-clear depuis absence d’événement. Langage compréhensible par personne suivant son affaire.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Méthode et sources déjà documentées ; toute nouvelle conclusion juridique exige recherche propre.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] La synthèse conserve provenance, ancienneté et inconnues ; aucune nouvelle validation de délai, montant ou exécution depuis l’agrégation.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : PD01 — Ordonnance et deux mises à jour : état de procédure et actions restantes avec sources.
- Cas limite : PD02 — Dernier état ancien et pièces inaccessibles : signaler couverture et demander actualisation, pas aucun changement.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Réévaluation complète, chances de succès et rapport tous dossiers.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

