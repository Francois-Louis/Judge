---
id: BNK-002
titre: "Réclamer après une opération validée sous tromperie"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-002 — Réclamer après une opération validée sous tromperie

## Objectif et résultat attendu

Une personne qui a validé un virement ou un paiement après une usurpation
d'identité (faux conseiller, faux proche, faux placement) organise les faits,
comprend les questions débattues et obtient un brouillon de réclamation, sans
promesse de remboursement.

## Périmètre et fichiers

- `banking-legal/skills/authorised-fraud-claim/SKILL.md` — le skill (à créer)
- `banking-legal/references/fraude-autorisee.md` — questions débattues, jurisprudence lue, sources (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

`qualification-bancaire.md` et `paiements.md` (BNK-001) sont relus, pas réécrits.

## Pièces et informations nécessaires

Opération ; chronologie de l'appel ou des messages ; numéro affiché ; ce qui a
été validé et comment ; alertes reçues de la banque ; vérification du
bénéficiaire affichée ou non ; signalements et plainte.

## Sortie attendue

Chronologie minutée ; ce que la personne a vu et validé ; questions sur
l'autorisation et sur les obligations du prestataire, selon les sources
lues ; demande de rappel des fonds à poser ; brouillon de réclamation ;
plainte (DOM-002) en tâche distincte ; limites.

## Travail attendu

Ne pas conclure à une opération autorisée ni non autorisée : exposer les faits
qui comptent selon la jurisprudence lue. Faux placement : la demande au
prestataire est ici, l'orientation sur le produit en BNK-011.

## Références métier et sources à rechercher

Code monétaire et financier, services de paiement ; jurisprudence récente sur
le « faux conseiller », à lire ; règlement (UE) 2024/886, vérification du
bénéficiaire, date d'application à vérifier.

## Critères d'acceptation

- [ ] F01 produit chronologie et réclamation sans conclure sur l'autorisation.
- [ ] F02 sépare la réclamation bancaire et l'orientation sur le faux placement.

## Vérification

- Cas normal : F01 — Virement validé après l'appel d'un « service fraude » affichant le numéro de l'agence.
- Cas limite : F02 — Virements vers une plateforme de placement inconnue après une publicité.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Plainte, action contre le bénéficiaire, récupération des fonds par un tiers
payant, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 25, 33, 37 de la [matrice](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

- [ ] F03 — Faux conseiller : recueillir les écrans réellement affichés, nom/IBAN partiellement masqué, résultat de la vérification, avertissements, dates et acteurs ; ne pas déduire le consentement de la validation technique.
- [ ] F04 — Vérification absente alléguée : demander les traces et vérifier le champ temporel et territorial du dispositif avant tout grief.

Le brouillon distingue la demande urgente de rappel, la preuve du consentement et les obligations éventuellement manquées. Erreur de saisie sans tromperie → BNK-015. Scénarios F03/F04 **attendus, non exécutés** ; jurisprudence et texte européen à ouvrir lors du lot.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
