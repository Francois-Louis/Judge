---
id: TRAV-012
titre: "Préparer un projet de charte de télétravail pour un périmètre privé"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-012 — Préparer un projet de charte de télétravail pour un périmètre privé

## Objectif

Une petite entreprise privée veut un projet de charte de télétravail lisible pour un périmètre précis.

Résultat : Projet de charte et notes de mise en place, questions ouvertes et acteurs à consulter ; pas de texte réputé en vigueur.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : policy-drafting.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Objectif, bénéficiaires, sites/territoires, accords existants, organisation et représentation collective.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Remplacer state supplements, disclaimer « not a contract » et hypothèse absence de variation ; qualifier accord/charte/contrat et rechercher formalités pertinentes.

Sources primaires à rechercher : Code du travail, accords/CCN, règles de santé/frais/égalité/données selon le périmètre ; sources officielles aux dates utiles.
Ces pistes sont **non vérifiées pour cette story**. Lire les dispositions,
versions et transitions applicables lors de l'implémentation ; conserver
le relevé des accès et réserves BASE-005. Utiliser les voies officielles
alternatives de BASE-010 si une page web échoue, sans confondre lecture et validation.

Charger la méthode locale versionnée et embarquer les références utiles.
Conserver la frontière de stockage BASE-008 ; nommer les accès externes
nécessaires/optionnels et prévoir la sortie utile si la recherche reste empêchée.

## Critères d'acceptation

- [ ] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous.
- [ ] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie.
- [ ] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement.
- [ ] Sources et données sont traçables ; le paquet isolé ne requiert aucun fichier voisin du dépôt.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche.
- [ ] Le périmètre adapté et le reste non adapté sont explicitement distingués.

## Vérification

- Cas normal : Un site et règles collectives identifiées : projet cohérent et lisible.
- Limite : Accord contradictoire, territoire étranger ou représentants inconnus : procédure et conclusion réservées.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Toutes politiques RH, négociation d'accord, déploiement et information effective des salariés.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
