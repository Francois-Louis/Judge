---
id: PI-026
titre: "Lire un contrat d'édition ou de production proposé à un auteur"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-026 — Lire un contrat d'édition ou de production proposé à un auteur

## Objectif et résultat attendu

Un auteur (livre, musique, illustration, audiovisuel) comprend les droits cédés, la rémunération, la durée, le territoire et les obligations de l'éditeur ou du producteur, et prépare ses questions avant de signer. Ajout du 16 octobre 2026 ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/ip-clause-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/contrat-edition-production.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contrat complet et annexes, type d'œuvre, statut de l'auteur, droits et modes d'exploitation visés, rémunération proposée, durée, territoire, échanges.

## Travail attendu

Tableau clause/droit cédé/mode d'exploitation/rémunération/question ; ne pas présumer une cession non écrite ni appliquer un modèle américain de work-for-hire. Statut social et fiscal de l'auteur → DOM-042. Clause de gestion collective → PI-027.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d'action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit,
œuvre ou objet, acteur et qualité, territoire, dates, sources lues, manques et
conclusion réservée ; aucun lancement automatique d'un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Code de la propriété intellectuelle, contrats d'édition, de production audiovisuelle et de cession, formalisme et rémunération ; codes d'usages professionnels comme sources non normatives.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles, le champ et les transitions ; une source inaccessible donne une voie
officielle alternative BASE-010 puis la réserve de la seule conclusion
dépendante.

## Critères d'acceptation

- [ ] Chaque droit cédé est rattaché à un mode d'exploitation, une durée et une rémunération lus ; aucune cession présumée.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.

## Vérification

- Cas normal : E01 — Contrat d'édition d'un premier roman avec cession pour toute la durée de la propriété.
- Cas limite : E02 — Contrat de production musicale rédigé en anglais avec clause « all rights worldwide » : lecture française, questions, aucun droit étranger appliqué.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Négociation, rédaction du contrat, statut social de l'auteur, contentieux.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Statut `proposee` : aucune tranche sélectionnée, aucun skill adapté.
Contrat commun : [découpage EXIST-008](../exist-008-annexes/exist-008-decoupage-pi.md).
