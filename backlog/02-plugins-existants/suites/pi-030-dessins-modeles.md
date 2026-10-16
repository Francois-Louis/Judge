---
id: PI-030
titre: "Qualifier la protection d'un dessin ou modèle et documenter une copie alléguée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-030 — Qualifier la protection d'un dessin ou modèle et documenter une copie alléguée

## Objectif et résultat attendu

Un créateur ou une petite entreprise comprend comment une forme ou un design peut être protégé (dépôt en France ou dans l'UE, modèle non enregistré, droit d'auteur) et documente une copie alléguée. Ajout du 16 octobre 2026 ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/clearance/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/dessins-modeles.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Objet ou design, dates de création et de divulgation, dépôts éventuels (numéro, territoire), copie constatée et preuves.

## Travail attendu

Distinguer modèle déposé en France, dessin ou modèle de l'Union enregistré ou non, et droit d'auteur, sans conclure sur la validité. Aucune design patent américaine appliquée. Lève l'exclusion des dessins et modèles du découpage EXIST-008 pour cette seule tâche.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d'action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit,
œuvre ou objet, acteur et qualité, territoire, dates, sources lues, manques et
conclusion réservée ; aucun lancement automatique d'un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Code de la propriété intellectuelle, dessins et modèles ; règlement (CE) n° 6/2002 et ses modifications, version à vérifier ; INPI et EUIPO comme sources d'information.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles, le champ et les transitions ; une source inaccessible donne une voie
officielle alternative BASE-010 puis la réserve de la seule conclusion
dépendante.

## Critères d'acceptation

- [ ] Les voies de protection sont distinguées et la conclusion sur la validité reste réservée.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.

## Vérification

- Cas normal : D01 — Créatrice de bijoux qui découvre une copie de ses boucles d'oreilles en ligne.
- Cas limite : D02 — Meuble divulgué il y a plusieurs années sans dépôt : protection non enregistrée à vérifier.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Dépôt fait à la place de la personne, recherche d'antériorités complète, contentieux.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Statut `proposee` : aucune tranche sélectionnée, aucun skill adapté.
Contrat commun : [découpage EXIST-008](../exist-008-decoupage-pi.md).
