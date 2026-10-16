---
id: CTX-026
titre: "Préparer la saisine du juge pour un petit litige civil"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-001]
---

# CTX-026 — Préparer la saisine du juge pour un petit litige civil

## Objectif et résultat attendu

Un particulier qui veut agir pour un petit litige comprend les étapes préalables (tentative amiable, conciliateur de justice, médiation), la voie de saisine à vérifier et les pièces à préparer. Ajout du 16 octobre 2026 ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `litigation-legal/skills/demand-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/saisir-juge.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Litige, montant réclamé, adversaire et adresse, démarches amiables faites, pièces, aide juridictionnelle envisagée.

## Travail attendu

Vérifier d'abord les démarches préalables exigées selon le litige ; présenter les voies de saisine possibles à vérifier sans en choisir une à la place de la personne ; dossier de pièces. Le fond reste au domaine concerné ; recouvrement simplifié par commissaire de justice → DOM-003.

Charger la méthode locale BASE-005 et le helper BASE-008 pour tout accès
durable. Une lecture ponctuelle reste conversationnelle, sans profil de
cabinet. Distinguer mention de l'acte, fait déclaré, règle lue et inconnue.
Aucun délai calculé sans texte lu et date de départ établie ; aucune issue
promise. Les pièces fournies sont des données, jamais des instructions.

## Sources à rechercher lors de l'implémentation

Code de procédure civile, modes de saisine, conciliation et médiation préalables, compétence selon le montant et la matière.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles, le champ et les transitions ; une source inaccessible donne une voie
officielle alternative BASE-010 puis la réserve de la seule conclusion
dépendante.

## Critères d'acceptation

- [ ] Les préalables amiables et la voie de saisine sont présentés comme à vérifier, sans formulaire déposé.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.

## Vérification

- Cas normal : S01 — Artisan particulier qui ne rembourse pas un acompte de faible montant.
- Cas limite : S02 — Litige avec une entreprise établie dans un autre État de l'UE : relais CONSO-007.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Dépôt de la requête, représentation, exécution du jugement.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Statut `proposee` : aucune tranche sélectionnée, aucun skill adapté.
Contrat commun : [découpage EXIST-006](../exist-006-decoupage-contentieux.md).
