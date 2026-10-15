---
id: TRAV-010
titre: "Ajouter et interroger les pièces autorisées d'une enquête"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006, TRAV-009]
---

# TRAV-010 — Ajouter et interroger les pièces autorisées d'une enquête

## Objectif

Un enquêteur habilité dispose d'un dossier ouvert et de pièces à organiser, puis veut retrouver les éléments d'une question.

Résultat : Journal indexé, couverture réelle, contradictions/lacunes et réponse à IDs, sans assimilation d'allégation à fait établi.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : investigation-add ; investigation-query ; internal-investigation modes 2/3.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Périmètre et habilitations TRAV-009, pièces lisibles autorisées, provenance et journal existant.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Écarter collecte RH générale, automatisme privilege et branche Upjohn ; conserver les critères de sélection transparents et la traçabilité ; charger le seul dossier actif.

Sources primaires à rechercher : Règles de preuve, accès et protection des données du cadre d'enquête retenu ; durées de conservation à rechercher, non déduites du seul archivage.
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

- Cas normal : Lot autorisé puis question : citer les pièces réellement lues et distinguer contradictions.
- Limite : Pièce illisible, collecte non autorisée ou question sans preuve : limite tracée, aucun élément inventé ni lecture d'un autre dossier.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Collecte automatisée de messageries, entretiens, décision de crédibilité définitive et rapport final.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
