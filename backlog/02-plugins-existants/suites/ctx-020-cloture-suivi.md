---
id: CTX-020
titre: "Clore administrativement le suivi d’un dossier"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-014]
---

# CTX-020 — Clore administrativement le suivi d’un dossier

## Objectif et résultat attendu

Une clôture de suivi attribuée conserve issue déclarée, pièces et obligations ouvertes sans constater extinction juridique.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/matter-close/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_log.yaml` (blocs nécessaires à cette tranche)
- `litigation-legal/references/cloture-suivi.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Dossier, motif/auteur/date, accord/jugement, exécution/recours connus, conservation et frais documentés.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Séparer fond, exécution, recours et fermeture du suivi. Conserver historique/inconnues ; CTX-008 réexamine conservation sans levée implicite. Transaction rédigée non réputée signée/exécutée. Ne pas solder dette/garantie ou supprimer pièces depuis closed. Préparer relais DOM-003 sur acte d’exécution distinct.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Effets de l’acte effectivement fourni et régime procédural si conclusion demandée, données/conservation et règles professionnelles.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] La clôture est administrative ; elle n’efface dette, recours ou conservation et toute correction garde sa provenance.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : CL01 — Accord signé et paiement partiel restant : clôture administrative choisie et obligations restantes signalées.
- Cas limite : CL02 — « On a gagné » sans jugement/réception : noter déclaration, pas de décision définitive ni destruction autorisée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Extinction certifiée, exécution, recours et effacement.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

