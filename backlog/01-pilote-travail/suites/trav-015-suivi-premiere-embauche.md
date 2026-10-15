---
id: TRAV-015
titre: "Mettre à jour les tâches d'une première embauche en France"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006, TRAV-014]
---

# TRAV-015 — Mettre à jour les tâches d'une première embauche en France

## Objectif

La personne pilote une première embauche préparée dans TRAV-014 et revient avec des avancées.

Résultat : Tracker mis à jour, tâches débloquées et informations manquantes, en distinguant décision déclarée et obligation vérifiée.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : expansion-update ; schéma international-expansion.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Tracker existant, pièces/confirmations datées, nouvelles décisions et propriétaires.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Aucun avancement ne valide une qualification juridique ; conserver sources/versions, provenance des dates et questions non résolues ; charger explicitement le schéma utilisé.

Sources primaires à rechercher : Mêmes sources que TRAV-014 uniquement pour les questions rouvertes ; recontrôler les règles qui conditionnent une date.
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

- Cas normal : Responsable confirme une tâche sur pièce : dépendances débloquées et notes conservées.
- Limite : Jalon dépassé ou délai légal sans fondement : alerte distincte, pas de calcul ni statut « conformité acquise ».

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Tous pays et tous projets, relance automatique des responsables et décision de conformité globale.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
