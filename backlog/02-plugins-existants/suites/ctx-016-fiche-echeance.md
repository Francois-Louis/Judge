---
id: CTX-016
titre: "Établir une fiche d’échéance de procédure TJ écrite"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-016 — Établir une fiche d’échéance de procédure TJ écrite

## Objectif et résultat attendu

Une fiche documente une échéance TJ écrite qualifiée ou explique pourquoi elle reste à déterminer.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/references/echeance-tj-ecrite.md` (à créer)
- `litigation-legal/skills/procedural-deadline/SKILL.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Juridiction/procédure/stade, acte intégral, nature, texte/décision/calendrier, déclencheur et preuve, mode/destinataire de notification, dates/lieux.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Borner première recette à échéance fixée par calendrier fourni d’une instance TJ écrite. Distinguer lecture de date et calcul juridique ; toute computation exige source/version, déclencheur prouvé, méthode reproductible, exceptions/prorogation et contrôle attribué. Autre délai : a-determiner et questions, sans table générale appel/prescription. Notification inconnue : ne pas substituer date d’acte/téléchargement/dépôt. Aucun FRCP 12/21 jours ni agenda.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

CPC et dispositions spéciales, décision/calendrier complet et notification/computation aux dates pertinentes ; représentation/compétence à confirmer.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Chaque date porte nature et preuve ; source ou déclencheur manquant laisse a-determiner sans substitution de date ni calcul hors régime retenu.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : F01 — Calendrier complet TJ écrit fixe une date de conclusions : date, passage, destinataire et modifications à vérifier.
- Cas limite : F02 — Décision sans preuve de remise ou demande de délai d’appel : pas de date butoir inventée, bornage et recherche/relais propre.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Calendrier universel, appel/prescription tous régimes et inscription agenda.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

