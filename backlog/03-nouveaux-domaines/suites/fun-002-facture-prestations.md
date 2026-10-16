---
id: FUN-002
titre: "Comparer une facture funéraire au devis et préparer une réclamation sur des prestations non demandées"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-001]
---

# FUN-002 — Comparer une facture funéraire au devis et préparer une réclamation sur des prestations non demandées

## Objectif et résultat attendu

Un proche qui reçoit la facture des obsèques voit, ligne par ligne, ce qui
avait été commandé selon les pièces, ce qui apparaît sans commande retrouvée
et ce qui diffère du devis, et obtient un brouillon de réclamation ou de
demande de justification adressé à l'opérateur.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/funeral-invoice-claim/SKILL.md` — le skill (à créer)
- `funeral-legal/skills/funeral-invoice-claim/references/reclamation-facture.md` — modèle de réclamation (à créer)
- `funeral-legal/references/qualification-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/references/lecture-devis-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Facture ; devis et bon de commande signés ; avenants ou commandes complémentaires.
- Échanges avec l'opérateur : courriels, messages, notes d'un appel (date, interlocuteur, contenu allégué).
- Signataire de chaque pièce ; personne qui a donné un accord oral allégué.
- Paiements déjà faits et par qui ; facture adressée à qui.

## Sortie attendue

1. Résumé : ce qui est facturé, ce qui était commandé selon les pièces, ce qui est contesté.
2. Fiche des trois qualités, reprise de FUN-001, appliquée à chaque commande.
3. Tableau : ligne facturée, montant recopié, devis ou commande retrouvé, signataire, écart.
4. Prestations sans commande retrouvée marquées comme inconnues, ni retenues ni écartées.
5. Brouillon de réclamation ou de demande de justification, sans remboursement annoncé.
6. Ce qui reste à vérifier : forme exigée de la commande, information préalable, avec la source lue ou réservés.
7. Suites : paiement réclamé → FUN-004 ; prise en charge → FUN-005 ; médiateur du secteur à identifier ; repli CONSO-014 tant que le paquet n'est pas livré.
8. Limites et phrase BASE-013.

## Travail attendu

Appliquer les références de FUN-001 à la facture. Une prestation absente du
devis n'est pas présumée imposée ; un accord oral allégué par l'opérateur
n'est ni tenu pour donné ni pour refusé. Les montants sont recopiés, jamais
recalculés à partir d'un prix supposé. Une commande signée par un autre proche
est rattachée à son signataire sans en déduire qui doit payer.

## Références métier et sources à rechercher

Pistes FUN-001 ; Code civil, preuve des obligations (pistes 1353, 1359 et
suivants) et inexécution (pistes 1217 et suivants) ; Code de la
consommation, médiation (pistes L612-1 et suivants).

## Critères d'acceptation

- [ ] I01 produit le tableau des écarts et une réclamation mesurée, sans présumer l'opérateur de mauvaise foi.
- [ ] I02 rattache chaque commande à son signataire sans répondre pour « la famille ».
- [ ] Aucun remboursement ni geste commercial n'est promis.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs ou le médiateur du secteur.

## Vérification

- Cas normal : I01 — Facture comprenant des soins de conservation et un maître de cérémonie absents du devis signé.
- Cas limite : I02 — Prestation complémentaire commandée par téléphone par un cousin, sans écrit.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Devis avant engagement, monument, recouvrement, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
