---
id: PI-029
titre: "Faire valoir le droit moral d'un auteur"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-029 — Faire valoir le droit moral d'un auteur

## Objectif et résultat attendu

Un auteur dont le nom est omis ou dont l'œuvre est modifiée sans accord comprend les prérogatives du droit moral à vérifier et prépare une demande au diffuseur. Ajout du 16 octobre 2026 ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/infringement-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/droit-moral.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Œuvre et auteur, diffusion constatée, modification ou omission, contrat éventuel, échanges.

## Travail attendu

Distinguer paternité, intégrité, divulgation et retrait ; ne pas confondre droit moral et rémunération. Contrat → PI-026 ; reprise par un tiers → PI-028.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d'action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit,
œuvre ou objet, acteur et qualité, territoire, dates, sources lues, manques et
conclusion réservée ; aucun lancement automatique d'un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Code de la propriété intellectuelle, droit moral ; jurisprudence pertinente à lire.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles, le champ et les transitions ; une source inaccessible donne une voie
officielle alternative BASE-010 puis la réserve de la seule conclusion
dépendante.

## Critères d'acceptation

- [ ] La prérogative invoquée est identifiée et les faits manquants nommés, sans conclusion sur l'atteinte.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.

## Vérification

- Cas normal : M01 — Illustration publiée sans le nom de l'illustratrice.
- Cas limite : M02 — Œuvre d'art installée dans un lieu public, modifiée lors de travaux.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Contentieux, négociation financière, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Statut `proposee` : aucune tranche sélectionnée, aucun skill adapté.
Contrat commun : [découpage EXIST-008](../exist-008-decoupage-pi.md).
