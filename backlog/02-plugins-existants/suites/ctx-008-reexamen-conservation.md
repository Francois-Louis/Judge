---
id: CTX-008
titre: "Réexaminer une mesure de conservation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-007]
---

# CTX-008 — Réexaminer une mesure de conservation

## Objectif et résultat attendu

Une fiche propose maintien, modification ou fin d’une mesure précise avec décision attribuée et points non résolus.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/legal-hold/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/reexamen-conservation.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Plan CTX-007 ou équivalent, exécution prouvée, litiges liés autorisés, état de clôture/recours et obligations actuelles.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Borner refresh/release/status au réexamen d’une mesure. Rechercher obligations restantes et autres finalités ; lier décision à auteur/date/périmètre. Clôture administrative ne libère rien automatiquement. Retirer retour normal retention et notice prétendument envoyée. Exposer supports non couverts et prochaine revue ; aucune suppression ou réalisation sans preuve.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Conservation/procédure, règles sectorielles, RGPD/droit national, politique réelle et versions/transitions.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] La fin du litige ne libère pas automatiquement la mesure ; autres obligations et incertitudes empêchent une suppression générale.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : R01 — Accord clos mais autre dossier portant sur certaines pièces : réexaminer par sous-ensemble et attribuer décisions.
- Cas limite : R02 — Jugement sans réception ni état des recours : réserver fin de mesure, demander pièces, pas de recours réputé clos.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Suppression, collecte, diffusion et avis complet sur recours.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

