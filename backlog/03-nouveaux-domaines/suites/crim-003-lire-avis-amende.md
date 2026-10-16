---
id: CRIM-003
titre: "Lire un avis d'amende et identifier son stade"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-003 — Lire un avis d'amende et identifier son stade

## Objectif et résultat attendu

Une personne qui reçoit un avis d'amende comprend de quel avis il s'agit, à
quel stade elle se trouve, ce que le document indique, et quelles options
sont à vérifier, y compris si elle a déjà payé ou reçu l'avis tardivement.

## Périmètre et fichiers

- `criminal-legal/skills/fine-notice-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/references/amendes.md` — types d'avis, stades, options, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`amendes.md` est relu par CRIM-005 et CRIM-010, qui ne le réécrivent pas.

## Pièces et informations nécessaires

Avis complet ; date et lieu de l'infraction ; dates d'envoi et de réception
(enveloppe, suivi) ; montant indiqué ; paiement déjà fait (date, moyen,
justificatif) ; titulaire du certificat d'immatriculation et conducteur ;
avis antérieurs reçus ou non.

## Sortie attendue

Fiche : type d'avis, infraction mentionnée, dates et montants recopiés du
document, stade ; paiement déjà fait et justificatif ; options à vérifier à ce
stade et effet possible d'un paiement, selon la source lue ; questions ;
limites. Aucun délai calculé sans texte lu et date établie.

## Travail attendu

Distinguer avis initial, avis majoré et autre acte. Pour un avis reçu
tardivement, documenter les dates d'envoi et de réception sans en conclure
l'irrégularité. Un acte de saisie pour recouvrement relève de DOM-003. Une
contravention non routière est lue de la même façon, sans grille propre.

## Références métier et sources à rechercher

Code de procédure pénale, amende forfaitaire et majorée (pistes 529 et
suivants, 530) ; Code de la route, responsabilité du titulaire et
désignation du conducteur (piste L121-3) ; ANTAI comme service d'information.

## Critères d'acceptation

- [ ] F01 identifie le stade et note le paiement prouvé, sans affirmer son effet sans source.
- [ ] F02 documente les dates d'envoi et de réception sans conclure.
- [ ] F03 oriente l'acte de saisie vers DOM-003.
- [ ] Montants recopiés du document seulement.

## Vérification

- Cas normal : F01 — Avis majoré reçu alors que la personne a payé l'avis initial.
- Cas limite : F02 — Avis reçu plusieurs semaines après la date d'infraction ; la personne ne conduisait pas.
- Cas limite : F03 — Lettre de saisie sur compte pour une amende ancienne.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Rédaction de la contestation (CRIM-005), points du permis (CRIM-010),
paiement, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 59–62, 67–68, 79 et section 7 de la [matrice](../dom-002-frictions-utilisateurs.md). Recueillir avis initial et majoré, avis de paiement ou consignation, mode de notification, adresse du certificat d'immatriculation aux dates utiles et changement d'adresse, sans copier l'adresse complète dans la sortie.

- [ ] F04 — Séparer paiement, consignation, contestation, demande de remise et photo radar ; identifier les effets propres à chaque démarche selon le texte lu, sans promettre que l'une conserve le délai de l'autre.
- [ ] F05 — Distinguer amende routière, amende forfaitaire délictuelle, ordonnance pénale, stationnement interdit et forfait post-stationnement (FPS). Aucune grille de délais routiers appliquée par défaut ; FPS → DOM-010, ordonnance → CRIM-006.
- [ ] F06 — Sans interception ou sans signature : ne pas déduire l'annulation ; préciser le procédé de constatation annoncé et les pièces manquantes.

Scénarios **attendus, non exécutés** : paiement pris pour consignation ; avis majoré sans premier avis et adresse obsolète ; FPS pris pour contravention ; signature refusée. Référence `amendes.md` : les délais de paiement et de recours ont chacun leur point de départ, mode et exception à vérifier. Aucun calculateur ne reprend les constantes du texte utilisateur.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
