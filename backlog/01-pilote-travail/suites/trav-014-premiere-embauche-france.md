---
id: TRAV-014
titre: "Préparer les questions d'une première embauche en France par un employeur étranger"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-014 — Préparer les questions d'une première embauche en France par un employeur étranger

## Objectif

Une petite entreprise étrangère prévoit un premier salarié privé en France et doit identifier les travaux préalables.

Résultat : Liste de questions et tâches distinctes avec responsables, hypothèses et pièces ; aucune structure réputée licite sans recherche.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : expansion-kickoff ; international-expansion.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Employeur envisagé, activité, rôle réel, lieux, calendrier, structure envisagée, effectif et interlocuteurs.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Remplacer US parent/EOR/entity comme défauts ; vérifier emploi direct, prestataire/intérim/portage sans équivalence ; corriger l'en-tête non commenté du modèle YAML et séparer projets/délais légaux.

Sources primaires à rechercher : Sources officielles emploi, déclarations sociales, droit au travail, représentation et CCN ; fiscalité/implantation et données à confier aux propriétaires ciblés.
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

- Cas normal : Premier recrutement en France, employeur étranger : questions structurées et dépendances visibles.
- Limite : EOR non qualifié ou pouvoir de signer des contrats : questions à spécialistes, aucun statut fiscal ou social déduit.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Création d'entité, conseil fiscal chiffré, immigration complète, contractualisation du prestataire et envoi de brief.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
