---
id: TRAV-008
titre: "Signaler les points à vérifier avant un retour d'arrêt maladie"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006, TRAV-007]
---

# TRAV-008 — Signaler les points à vérifier avant un retour d'arrêt maladie

## Objectif

Le registre de la tranche TRAV-007 comporte un retour envisagé après maladie ordinaire ; une personne veut connaître les démarches à vérifier.

Résultat : Alertes ciblées avec fondement, propriétaire de l'action, preuve, incertitude et prochaine vérification, seulement lors d'une invocation réelle.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : leave-tracker ; agents/leave-tracker.md.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Registre sourcé, dates/prévisions, contexte contractuel/collectif, événements et obligations déjà documentés.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Remplacer compteurs FMLA, épuisement ADA/USERRA et exclusions PTO ; rechercher les obligations françaises pertinentes au retour ; distinguer prévision et délai calculable.

Sources primaires à rechercher : Code du travail et textes de santé au travail, règles conventionnelles et computation applicables à la situation.
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

- Cas normal : Retour documenté : alerte utile reliée à une obligation vérifiée.
- Limite : Date ou régime absent : pas de statut « aucun risque », pas de rupture automatique ; données manquantes identifiées.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Ordonnanceur, rupture/inaptitude, avis médical, tous congés et registre santé exhaustif.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
