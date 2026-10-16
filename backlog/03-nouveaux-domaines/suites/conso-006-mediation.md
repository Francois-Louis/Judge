---
id: CONSO-006
titre: "Préparer la saisine d'un médiateur de la consommation"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-006 — Préparer la saisine d'un médiateur de la consommation

## Objectif et résultat attendu

Après une réclamation écrite restée sans réponse satisfaisante, une personne
identifie le médiateur compétent, vérifie les conditions de saisine et
obtient un brouillon de demande avec la liste des pièces.

## Périmètre et fichiers

- `consumer-legal/skills/mediation-referral/SKILL.md` — le skill (à créer)
- `consumer-legal/references/mediation.md` — conditions, sources lues, modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Réclamation écrite et sa date ; réponse du vendeur ; médiateur indiqué dans
les CGV, sur le site ou la facture ; pièces du litige ; démarches judiciaires
éventuelles.

## Sortie attendue

Médiateur identifié ou manque signalé ; conditions de recevabilité à
vérifier ; brouillon de saisine ; pièces ; limites (la médiation ne garantit
pas d'accord).

## Travail attendu

Accepter la sortie de CONSO-001 ou une réclamation fournie manuellement. Un
médiateur sectoriel (énergie, télécoms, banque, assurance) renvoie au
domaine du secteur. Conciliateur et juge : orientation vers le contentieux,
sans préparer l'acte.

## Références métier et sources à rechercher

Code de la consommation, médiation de la consommation ; liste officielle des
médiateurs et autorité qui la tient, consultées à la date du lot.

## Critères d'acceptation

- [ ] M01 identifie le médiateur et prépare la saisine sans affirmer de délai non lu.
- [ ] M02 signale l'absence de médiateur indiqué et la démarche pour l'obtenir.
- [ ] M03 oriente vers DOM-005 sans saisir un médiateur de consommation générique.

## Vérification

- Cas normal : M01 — Suite de N01 : réclamation sans réponse, médiateur nommé dans les CGV.
- Cas limite : M02 — Vendeur qui n'indique aucun médiateur.
- Cas limite : M03 — Refus d'un assureur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Envoi de la saisine, conciliation, procédure judiciaire.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
