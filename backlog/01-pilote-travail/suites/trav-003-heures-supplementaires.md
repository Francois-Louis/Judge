---
id: TRAV-003
titre: "Relire un décompte d'heures supplémentaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006, TRAV-002]
---

# TRAV-003 — Relire un décompte d'heures supplémentaires

## Objectif

Un salarié dispose de plannings et bulletins et veut comprendre un écart sur une période limitée.

Résultat : Décompte conditionnel par période, formule et sources près des montants, pièces et démarche suivante.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : wage-hour-qa ; renvoi depuis termination-review.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Relevés datés, horaires et pauses, contrat, accord d'aménagement éventuel, paiements déjà effectués.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Retirer FLSA, 0,5/1,5, doublement automatique et prescription 2/3 ans ; qualifier travail effectif, seuil, période et majoration ; isoler paiement et preuve.

Sources primaires à rechercher : Code du travail, accords de durée/aménagement et jurisprudence officielle sur temps et preuve, aux dates pertinentes.
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

- Cas normal : Horaire hebdomadaire documenté : calcul explicite avec paiements déduits.
- Limite : Forfait, temps partiel ou aménagement non établi : réserver la branche non couverte, pas de calcul standard.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Paie complète, tout forfait jours, contentieux et délai de recours calculé.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
