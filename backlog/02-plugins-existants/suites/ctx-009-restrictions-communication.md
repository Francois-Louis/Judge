---
id: CTX-009
titre: "Examiner les restrictions de communication par pièce"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-009 — Examiner les restrictions de communication par pièce

## Objectif et résultat attendu

Un tableau interne par pièce distingue restriction alléguée, source, faits, portée, incertitude et décision à instruire.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/privilege-log-review/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/restrictions-communication.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Pièce/annexes, auteur/qualité à date, mission, destinataires/diffusions, objet, procédure/autorité, pays et finalité.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Définir tableau avant renommage visible, conserver chemin technique provisoire. Séparer secret professionnel, régime du juriste d’entreprise à rechercher, confidentialité contractuelle, données et restriction judiciaire. Examiner pièces jointes séparément. Retirer avocat en copie/header protecteur/waiver automatique et France/UE régime unique. Source ou faits absents : à instruire, pas certainement privileged/non privileged. Tableau interne distinct du bordereau externe.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Règles professionnelles et textes actuels secret/confidentialité, procédure, secteurs, droit UE dans son champ, données et accords ; réformes/transitions juristes d’entreprise à vérifier.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Chaque restriction dépend de faits et source actuelle ; avocat en copie, titre de juriste et en-tête ne prouvent ni protection ni perte de protection.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : S01 — Courriel à avocat et facture préexistante jointe : deux objets examinés séparément, mission et destinataires demandés.
- Cas limite : S02 — Avis interne France ancien, diffusion incertaine et source inaccessible : réserver régime temporel, sans appliquer Akzo à toute procédure.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Décision finale de communiquer/refuser, audit tous pays, levée du secret et log transmis.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

