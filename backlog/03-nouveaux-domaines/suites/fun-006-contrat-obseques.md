---
id: FUN-006
titre: "Comparer les prestations d'un contrat obsèques au devis d'exécution de l'opérateur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-001]
---

# FUN-006 — Comparer les prestations d'un contrat obsèques au devis d'exécution de l'opérateur

## Objectif et résultat attendu

Des proches qui découvrent un contrat obsèques souscrit par le défunt
voient quelles prestations y étaient prévues, ce que l'opérateur propose ou
facture au moment des obsèques, ce qui diffère, et obtiennent un brouillon
de demande d'explication sur un supplément ou une prestation manquante.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/prepaid-funeral-plan-review/SKILL.md` — le skill (à créer)
- `funeral-legal/references/contrat-obseques.md` — formules de contrat, prestations prévues, part relevant de l'assurance, sources lues (à créer)
- `funeral-legal/references/lecture-devis-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Contrat obsèques, conditions générales et particulières, descriptif des prestations, avenants.
- Organisme qui garantit le capital et opérateur désigné, tels qu'ils figurent sur les pièces.
- Devis ou facture de l'opérateur au moment des obsèques.
- Volontés exprimées dans le contrat ; échanges avec l'assureur ou l'opérateur.

## Sortie attendue

1. Résumé : prestations prévues, prestations proposées ou facturées, écart.
2. Tableau : prestation, prévue au contrat (pièce), devis ou facture, montant recopié, question.
3. Séparation entre prestations à exécuter (ici) et capital ou garantie (DOM-005).
4. Volontés figurant au contrat, transmises à FUN-003 si elles sont contestées.
5. Brouillon de demande d'explication à l'opérateur désigné.
6. Suites : refus ou retard de versement du capital → DOM-005 (INS-004, INS-011) ; contrat souscrit pendant une mesure de protection → DOM-026.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `contrat-obseques.md` et l'appliquer : le skill lit le descriptif des
prestations et ne se prononce pas sur la garantie, le capital ou leur
revalorisation. Un supplément n'est pas présumé injustifié ; il est rapproché
des pièces. Un démarchage allégué est noté comme fait déclaré, sans
qualification.

## Références métier et sources à rechercher

CGCT, formules de financement en prévision d'obsèques (pistes L2223-33-1,
L2223-34-1 et suivants) et interdiction de certaines offres de services
(piste L2223-33) ; Code des assurances pour la seule qualification,
orientation DOM-005.

## Critères d'acceptation

- [ ] C01 compare prestations prévues et facturées, sans se prononcer sur la garantie.
- [ ] C02 oriente le refus de versement du capital vers DOM-005 sans le traiter.
- [ ] Ni l'opérateur ni l'assureur ne sont présumés fautifs ; aucune prise en charge n'est promise.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs ou le médiateur compétent.

## Vérification

- Cas normal : C01 — Supplément demandé pour un cercueil et une cérémonie différents de ceux du descriptif.
- Cas limite : C02 — Opérateur désigné disant ne pas avoir reçu le capital de l'assureur.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Garantie et capital d'assurance, souscription d'un nouveau contrat,
résiliation, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
