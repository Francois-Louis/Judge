---
id: CTX-018
titre: "Présenter l’état des dossiers autorisés"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-014]
---

# CTX-018 — Présenter l’état des dossiers autorisés

## Objectif et résultat attendu

Une vue délimitée agrège seuls dossiers autorisés avec états, dates qualifiées, couverture et anomalies.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/portfolio-status/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_log.yaml` (blocs nécessaires à cette tranche)
- `litigation-legal/references/etat-portefeuille.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Registre/corpus autorisé, filtres, date de référence, accès, devises et provenance des montants.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Conserver filtres/ancienneté ; séparer risques internes et droit. Aucun total mélangeant devises, coûts, estimations et créances sans comparabilité. Détecter doubles dossiers, conflits non résolus et dates non vérifiées ; retirer hold universel et comptabilité US implicite. Respecter clients distincts et accès minimal. Dashboard utile seulement, échappement local et mêmes limites.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Méthode d’agrégation/provenance ; aucun avis comptable, de solvabilité ou financier depuis les scores de litige.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Couverture, devises et unités sont explicites ; registre vide ou accès partiel ne devient pas portefeuille sans risque.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : PF01 — Trois dossiers autorisés même devise : compte documenté et dates avec statut.
- Cas limite : PF02 — Deux devises et autre client non autorisé : pas de total trompeur ni lecture croisée, couverture limitée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Réserves réglementaires, analyse financière et accès global aux clients.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

