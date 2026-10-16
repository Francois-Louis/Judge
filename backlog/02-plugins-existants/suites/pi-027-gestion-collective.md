---
id: PI-027
titre: "Comprendre l'adhésion et les relevés d'une société de gestion collective"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-027 — Comprendre l'adhésion et les relevés d'une société de gestion collective

## Objectif et résultat attendu

Un auteur ou un artiste comprend ce qu'implique l'adhésion à une société de gestion collective, lit un relevé de répartition et prépare une question ou une réclamation. Ajout du 16 octobre 2026 ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/portfolio/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/gestion-collective.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Société concernée, statuts ou contrat d'apport, déclarations d'œuvres, relevés de répartition, échanges, période.

## Travail attendu

Distinguer apport de droits, déclaration des œuvres et répartition ; lire le relevé sans recalculer les sommes. Statut social et fiscal → DOM-042. Contrat d'édition → PI-026.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d'action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit,
œuvre ou objet, acteur et qualité, territoire, dates, sources lues, manques et
conclusion réservée ; aucun lancement automatique d'un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Code de la propriété intellectuelle, organismes de gestion collective ; statuts et règlements de la société concernée ; autorité de contrôle compétente, à vérifier.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles, le champ et les transitions ; une source inaccessible donne une voie
officielle alternative BASE-010 puis la réserve de la seule conclusion
dépendante.

## Critères d'acceptation

- [ ] Le relevé est lu poste par poste, sans recalcul ni présomption d'erreur.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.

## Vérification

- Cas normal : G01 — Compositeur qui ne comprend pas un relevé de droits de diffusion radio.
- Cas limite : G02 — Œuvre jamais déclarée à la société, droits réclamés pour des diffusions passées.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Adhésion faite à la place de la personne, contentieux avec la société, fiscalité.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Statut `proposee` : aucune tranche sélectionnée, aucun skill adapté.
Contrat commun : [découpage EXIST-008](../exist-008-decoupage-pi.md).
