---
id: CTX-005
titre: "Qualifier une demande civile de communication de pièces"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-001]
---

# CTX-005 — Qualifier une demande civile de communication de pièces

## Objectif et résultat attendu

Une fiche distingue demande d’un contradicteur, mesure ordonnée et acte indéterminé, avec périmètre et vérifications.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/subpoena-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/inbound/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/demande-communication.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Acte intégral/annexes, auteur, destinataire partie/tiers, procédure/juridiction, ordonnance, pièces visées et réception.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Définir tâche française avant renommage visible « Demande de communication de pièces », chemin technique provisoirement conservé. Qualifier fondement et portée, ne pas déduire obligation du mot production. Distinguer communication en instance et mesure avant procès à cadrer séparément. Retirer subpoena/CID/grand jury, motion to quash, privilege log obligatoire et FRCP. Préparer questions d’accès et restrictions ; ni produire ni refuser automatiquement.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

CPC, Code civil et textes spéciaux ; compétence, partie/tiers, pouvoir de demander/ordonner, contradictoire, notification et représentation.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] La fiche cite la portée de la demande ou de la décision ; aucune obligation de privilege log, objection ou délai US n’est créée.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : P01 — Avocat adverse demande trois factures dans une instance civile : distinguer demande/ordonnance, demander calendrier et versions.
- Cas limite : P02 — Injonction à un tiers alléguée sans ordonnance ou réquisition pénale : demander acte, ne pas assimiler à demande entre parties ; relais approprié.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Réponse finale, mesure avant procès complète, saisie, pénal, administratif et transmission.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

