---
id: CTX-014
titre: "Ouvrir une fiche de dossier contentieux"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-014 — Ouvrir une fiche de dossier contentieux

## Objectif et résultat attendu

Une fiche d’ouverture et son registre partagent un identifiant et distinguent faits, rôles et validations.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/matter-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_log.yaml` (blocs nécessaires à cette tranche)
- `litigation-legal/matters/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/fiche-dossier-contentieux.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Identité/qualité, litige, parties, procédure supposée, pièces, dates prouvées, conseil/mandat éventuel et conservation.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Posséder schéma métier matter/log, échanger identifiant avec CTX-022 sans double ouverture. Corriger commentaire HTML initial de _log.yaml en commentaire YAML et vérifier chargement réel. Slug présent ne prouve pas contrôle des conflits : méthode/date/auteur/preuve/état distincts, pending/not-run/override non cleared. Particulier suivant son affaire non soumis à contrôle cabinet fictif. Retirer discovery/hold/ASC 450 par défaut ; dates gardent preuve/statut.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

CPC/compétence si procédure qualifiée, règles professionnelles conflits/mandat selon qualité, données/conservation ; registre ne certifie aucun conflit.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Le modèle YAML chargé ne contient que les clés de schéma attendues ; identifiant unique et conflits non établis restent visibles sans écrasement.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : DO01 — Particulier ouvre litige civil : fiche et identifiant unique sans GC, société ou hold obligatoire.
- Cas limite : DO02 — Cabinet avec conflits pending et slug existant : pas de cleared implicite ou d’écrasement ; signaler collision et validation manquante.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Contrôle certifié, compétence/délai calculés et migration de tous registres.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

