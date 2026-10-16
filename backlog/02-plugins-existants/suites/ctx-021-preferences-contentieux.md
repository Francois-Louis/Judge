---
id: CTX-021
titre: "Gérer des préférences contentieuses volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-021 — Gérer des préférences contentieuses volontaires

## Objectif et résultat attendu

Particulier/TPE ou professionnel choisit/modifie des préférences explicites sans en faire des règles de droit.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/cold-start-interview/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/skills/customize/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/preferences-contentieux.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Demande ciblée, profil éventuel, rôle déclaré et périmètre du changement.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Garder entretien neuf, pause/reprise, provenance et digest BASE-008 ; harmoniser modèles inline/profil. Lecture ponctuelle sans profil professionnel. Séparer ton/contacts/rangement de droit, preuve, délai, mandat et secret. Retirer defaults GC/US, test obligatoire des connecteurs et secret garanti. Changement de préférence ne modifie pas tous dossiers.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Contrats BASE-008 et méthode locale ; règles professionnelles si champ pose question de qualité/mandat, sans validation présumée.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] La modification reste ciblée et attribuée ; une préférence ne change aucune conclusion juridique et un profil absent n’est pas créé hors entretien neuf.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : PR01 — Particulier veut langage simple et change contact : modification ciblée, pas d’entretien cabinet complet.
- Cas limite : PR02 — Profil absent/interrompu ou changement concurrent : réponse ponctuelle possible, pas d’écrasement/création sans entretien neuf.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Qualification automatique et migration amont/globale.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

