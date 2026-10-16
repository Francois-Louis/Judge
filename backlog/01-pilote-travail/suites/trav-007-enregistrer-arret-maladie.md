---
id: TRAV-007
titre: "Enregistrer un arrêt maladie sans inventer d'échéance"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-007 — Enregistrer un arrêt maladie sans inventer d'échéance

## Objectif

Un salarié ou gestionnaire veut conserver les dates et pièces d'un arrêt maladie ordinaire du secteur privé.

Résultat : Entrée sourcée d'un registre borné à l'arrêt maladie, inconnues explicites et prochaine information nécessaire.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : log-leave ; schéma de agents/leave-tracker.md.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Identifiant minimisé, régime/territoire, contrat et documents collectifs utiles, dates déclarées et justificatifs, destinataires concernés.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Remplacer FMLA/USERRA/ADA, schéma et délais codés 5/15 jours ; différencier date déclarée/prouvée, obligation employeur/salarié et simple rappel ; supprimer promesse automatique.

Sources primaires à rechercher : Code du travail, textes sociaux et accords applicables à l'arrêt choisi ; règles de minimisation/confidentialité à rechercher.
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

- Cas normal : Dates étayées : ajout sans écraser notes et provenance.
- Limite : Régime ou notification inconnu : échéance à déterminer, aucun diagnostic médical demandé.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Calcul d'IJSS, AT/MP, maternité/parental, congés payés et automatisation.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
