---
id: VEH-011
titre: "Préparer une demande au constructeur après un refus de garantie ou un rappel"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-004]
---

# VEH-011 — Préparer une demande au constructeur après un refus de garantie ou un rappel

## Objectif et résultat attendu

Un propriétaire à qui le constructeur ou son réseau refuse une prise en
charge, ou dont le véhicule est concerné par un rappel, lit le document de
garantie et le motif du refus, distingue garantie du constructeur et
garanties du vendeur, et obtient un brouillon de demande.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/manufacturer-warranty-claim/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/garantie-constructeur.md` — garantie commerciale, entretien, rappels, sources lues (à créer)
- `vehicle-legal/references/vente-vehicule.md` — relue, créée par VEH-004
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Document de garantie du constructeur, carnet ou historique d'entretien, factures d'entretien.
- Motif du refus et son auteur (constructeur, concessionnaire, réparateur agréé).
- Avis de rappel ou information reçue ; date d'achat et vendeur.

## Sortie attendue

1. Résumé : garantie invoquée, refus ou rappel, demande envisagée.
2. Tableau : condition du document de garantie, pièce fournie, motif du refus, écart.
3. Distinction entre garantie du constructeur et garanties dues par le vendeur.
4. Brouillon de demande au constructeur ou à son réseau.
5. Suites : garanties du vendeur → VEH-004 ; danger signalé → sécurité en tête, rappel officiel à consulter ; dommage causé par le défaut → DOM-035.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `garantie-constructeur.md` et l'appliquer : un refus motivé par un
entretien hors réseau est examiné à partir du document de garantie et des
sources lues, sans affirmer de règle générale. Un rappel lié à la sécurité
place le message de sécurité en tête. Le document de garantie décide du
garant, jamais le logo du réseau.

## Références métier et sources à rechercher

Code de la consommation, garantie commerciale (pistes L217-21 et suivants)
et obligation générale de sécurité (piste L421-3) ; règlement d'exemption de
la distribution automobile et entretien hors réseau (piste règlement (UE)
n° 461/2010, à vérifier dans sa version et sa prorogation) ; site officiel
des rappels comme information.

## Critères d'acceptation

- [ ] C01 compare conditions de garantie et pièces d'entretien et prépare une demande sans règle générale non sourcée.
- [ ] C02 sépare garantie du constructeur et garanties dues par le vendeur.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat, avec renfort de sécurité en tête si un rappel est en cause.

## Vérification

- Cas normal : C01 — Garantie refusée au motif d'un entretien réalisé hors du réseau de la marque.
- Cas limite : C02 — Véhicule acheté d'occasion chez un professionnel, encore sous garantie du constructeur, avec une panne couverte par aucune des deux selon chacun.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Analyse de concurrence, indemnisation d'un dommage, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
