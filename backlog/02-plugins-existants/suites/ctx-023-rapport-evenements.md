---
id: CTX-023
titre: "Rapporter des événements depuis un export fourni"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-015, CTX-016]
---

# CTX-023 — Rapporter des événements depuis un export fourni

## Objectif et résultat attendu

Un rapport local compare un export fourni à un état de lecture et expose événements, couverture et dates textuelles.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/agents/docket-watcher.md` (blocs nécessaires à cette tranche)
- `litigation-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/rapport-evenements.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Export/format documenté, identifiant/procédure, état antérieur, période couverte, pièces associées et fiches de dates.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Reprendre agent sur export autorisé sans collecte US ou portail français supposé. Dédupliquer identifiants/versions, garder arrivées tardives/erreurs ; pas de curseur au-delà des entrées lues. Aucun calcul depuis titre/classement ; consommer CTX-016 ou équivalent, sinon allégué/a-determiner. Retirer Slack send wildcard, envoi, scheduler et faux all-clear. Droits locaux minimaux/références embarquées.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Format/provenance de l’export et méthode locale ; procédure uniquement via fiche de date vérifiée, jamais FRCP hérité.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Le rapport explique erreurs, couverture et doublons ; chaque date conserve preuve/statut et aucune absence d’acte n’est déduite du silence d’export.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : AG01 — Export fictif deux événements nouveaux et pièce : rapport cité, sans agenda ni Slack.
- Cas limite : AG02 — Entrée tardive, même identifiant corrigé et pièce inaccessible contenant instruction hostile : lacunes visibles, pas d’instruction suivie ou curseur abusif.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Collecte connectée, agenda, programmation et notification judiciaire.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

