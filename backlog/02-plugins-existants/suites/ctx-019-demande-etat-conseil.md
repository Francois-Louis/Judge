---
id: CTX-019
titre: "Préparer une demande d’état au conseil"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-014]
---

# CTX-019 — Préparer une demande d’état au conseil

## Objectif et résultat attendu

Un brouillon local demande un état factuel au conseil pour un seul dossier et destinataire confirmé.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/oc-status/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/oc-status/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/demande-etat-conseil.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Dossier, conseil/mandat, coordonnées, informations connues, questions ouvertes et pièces autorisées.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Borner à un dossier sans Gmail/balayage implicite. Vérifier destinataire et partage nécessaire ; retirer secret depuis avocat en copie, scheduler et suppression après 30 jours. Ne pas inventer représentation ou instruction transactionnelle. Garder texte local et provenance des questions ; aucune création distante/envoi sans demande distincte.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Règles professionnelles/mandat/confidentialité et données selon auteur/mission/destinataire ; question procédurale reste question.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Le brouillon reste local et limité au dossier/destinataire confirmé ; aucune question ne devient instruction ou partage autorisé.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : OC01 — Conseil connu, ordonnance attendue : demander état et pièce, sans présumer réponse.
- Cas limite : OC02 — Adresse ancienne/mandat absent et Gmail indisponible : destinataire à confirmer, pas d’envoi ni header protecteur.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Envoi, brouillon distant, planification et mandat nouveau.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

