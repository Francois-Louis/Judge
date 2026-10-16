---
id: CRIM-009
titre: "Lire une réquisition reçue par une organisation"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-009 — Lire une réquisition reçue par une organisation

## Objectif et résultat attendu

Une organisation (entreprise, association, cabinet) qui reçoit une
réquisition d'une autorité pénale comprend l'acte, ce qui est demandé, les
questions de secret et de données à vérifier, et prépare un inventaire. Rien
n'est transmis.

## Périmètre et fichiers

- `criminal-legal/skills/requisition-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/references/requisitions.md` — fondements à vérifier, secret, données, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte complet ; autorité et fondement indiqués ; données ou documents demandés ;
délai indiqué par l'acte ; secret professionnel applicable ; responsable du
traitement des données.

## Sortie attendue

Fiche de l'acte ; périmètre de la demande ; questions sur le secret et les
données (relais privacy) ; inventaire des éléments existants ; limites.

## Travail attendu

Ne pas assimiler l'acte à un « subpoena » ni à une demande de pièces civile
(EXIST-006). Ne pas conseiller de refuser ou de retarder ; ne pas supprimer de
données. Vérifier l'authenticité de l'acte par un canal officiel.

## Références métier et sources à rechercher

Code de procédure pénale, réquisitions (pistes 60-1, 77-1-1, 99-3) ; textes
sur le secret professionnel du secteur concerné ; RGPD et loi Informatique et
libertés pour la transmission.

## Critères d'acceptation

- [ ] Q01 produit fiche et inventaire sans transmission.
- [ ] Q02 traite d'abord l'authenticité d'un acte reçu par courriel.

## Vérification

- Cas normal : Q01 — Association recevant une réquisition sur les coordonnées d'un adhérent.
- Cas limite : Q02 — Courriel non signé se présentant comme une réquisition urgente.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Réponse à l'autorité, perquisition, conservation de preuves au-delà de
l'inventaire, transmission.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
