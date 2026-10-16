---
id: CTX-015
titre: "Consigner un événement de dossier"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-014]
---

# CTX-015 — Consigner un événement de dossier

## Objectif et résultat attendu

Un événement attribué rejoint l’historique et le registre sans effacer les états antérieurs.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/matter-update/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_log.yaml` (blocs nécessaires à cette tranche)
- `litigation-legal/references/evenement-contentieux.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Dossier/identifiant, pièce ou déclaration, auteur, dates du fait/de saisie, état précédent et correction éventuelle.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Posséder événement avec provenance et états allégué/proposé/décidé/notifié/exécuté. Corriger par nouvelle entrée, garder ancienne trace. Modifier seuls champs justifiés ; date demandée/brouillon ne remplace pas échéance validée. Consommer fiche CTX-016 ou équivalente pour tout calcul, sans calcul ad hoc. Contrôler cohérence dossier/log et répétition d’import.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Méthode locale et source procédurale exacte pour qualifier acte/délai ; décision et réception restent séparées.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Un import répété ne duplique pas l’événement ; une correction conserve la trace antérieure et un brouillon ne devient pas acte notifié.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : EV01 — Ordonnance fournie : ajouter source/date/statut, notification distincte.
- Cas limite : EV02 — Courriel annonce nouvelle date sans décision : noter allégation, conserver ancienne fiche, demander preuve.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Calcul de délai et réécriture rétroactive.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

