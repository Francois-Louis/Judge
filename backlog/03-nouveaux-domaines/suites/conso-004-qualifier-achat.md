---
id: CONSO-004
titre: "Qualifier un achat et orienter la demande"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-004 — Qualifier un achat et orienter la demande

## Objectif et résultat attendu

Une personne qui décrit un problème d'achat sans savoir quelle démarche
choisir obtient le domaine principal, la tâche adaptée et sa disponibilité
réelle, avec les seules questions utiles. Aucune analyse de fond.

## Périmètre et fichiers

- `consumer-legal/skills/purchase-triage/SKILL.md` — le skill (à créer)
- `consumer-legal/references/orientation-consommation.md` — table tâches, domaines et état livré (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

`qualification-achat.md` (CONSO-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Récit, document reçu s'il existe, but de l'achat, vendeur, objet, canal,
pays, ce que la personne veut obtenir.

## Sortie attendue

Domaine principal et tâche ; demandes distinctes s'il y en a plusieurs ;
questions complémentaires ; état réel de chaque tâche (livrée, proposée) ;
interlocuteur. Mise à jour de la table à chaque lot livré.

## Travail attendu

Appliquer `qualification-achat.md` et le protocole USAGE-001. Un achat
professionnel présenté comme privé reçoit une qualification conditionnelle
et les questions qui la tranchent. Ne pas appeler une commande absente ni
transférer les pièces à un autre plugin.

## Références métier et sources à rechercher

Code de la consommation, article liminaire ; dispositions sur le petit
professionnel hors établissement (piste L221-3). Aucune règle de fond
chargée au-delà de la qualification.

## Critères d'acceptation

- [ ] T01 laisse la qualité conditionnelle et nomme les faits manquants.
- [ ] T02 sépare la réclamation au vendeur et la contestation bancaire.
- [ ] T03 oriente l'abonnement mobile vers DOM-022 sans le traiter.
- [ ] La disponibilité annoncée correspond au paquet livré.

## Vérification

- Cas normal : T01 — « J'ai acheté un ordinateur pour mon entreprise, je veux la garantie consommateur. »
- Cas limite : T02 — Commande non livrée et opposition déjà faite sur la carte.
- Cas limite : T03 — Frais de résiliation d'une box internet.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Analyse de fond, brouillon, routage vers des plugins hors du domaine au-delà
d'une orientation.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
