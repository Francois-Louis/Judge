---
id: CTX-001
titre: "Lire et orienter un document entrant"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-001 — Lire et orienter un document entrant

## Objectif et résultat attendu

Un particulier ou une TPE obtient auteur, destinataire, demande, dates textuelles, pièces manquantes et orientation conditionnelle.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/demand-received/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/skills/subpoena-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/inbound/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/orientation-acte.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Document intégral/annexes ou extrait identifié, récit, qualité du destinataire, objectif, pays et dates connues.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Identifier lettre privée, demande de pièces, acte judiciaire ou convocation à partir du contenu et de son auteur. Distinguer qualification établie, déclarée et hypothèse ; relever dates sans calcul. Ne pas déduire exécution de la seule présence d’un commissaire de justice. Ajouter aux deux entrées un mode français explicite sans profil/registre obligatoire ; retirer leurs déclenchements US depuis ces documents. Ne pas analyser le fond ou lancer une suite.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

CPC, Code de l’organisation judiciaire et textes de compétence ; CPP, CJA ou CPCE seulement pour préparer le relais correspondant.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Une lettre, demande de pièces ou convocation française produit une orientation avec inconnues ; aucun déclenchement subpoena/deposition et aucun délai calculé.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : O01 — Mise en demeure reçue demandant huit jours : identifier demande et date alléguée, demander contrat et réception, sans FRE 408 ni hold automatique.
- Cas limite : O02 — Convocation française sans page précisant qualité et autorité : signaler manques et orientation conditionnelle ; ni témoin présumé ni deposition.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Fond du litige, délai, réponse formelle et actes pénaux/administratifs/exécutoires.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

