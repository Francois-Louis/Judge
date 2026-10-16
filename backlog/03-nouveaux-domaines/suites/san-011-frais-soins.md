---
id: SAN-011
titre: "Comparer une facture de soins à l'information reçue sur les frais"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-011 — Comparer une facture de soins à l'information reçue sur les frais

## Objectif et résultat attendu

Un patient surpris par une facture d'un professionnel ou d'un établissement
de santé compare ce qui est facturé à l'information et au devis reçus, sait
ce qui relève du soignant et ce qui relève du remboursement, et obtient un
brouillon de demande d'explication.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/care-bill-review/SKILL.md` — le skill (à créer)
- `health-legal/references/information-frais.md` — information sur les frais, devis, sources lues (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Facture, devis, affichage ou information reçue avant le soin.
- Professionnel ou établissement ; date des soins.
- Remboursements reçus de la caisse et de la complémentaire, s'ils sont connus.

## Sortie attendue

1. Résumé : ce qui est facturé et ce que la personne conteste.
2. Tableau : poste, montant recopié, information ou devis préalable, écart.
3. Ce qui relève du soignant et ce qui relève du remboursement.
4. Brouillon de demande d'explication.
5. Suites : remboursement de la caisse → DOM-012 ; complémentaire → INS-009 ; recouvrement → DOM-003.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `information-frais.md` et l'appliquer : montants recopiés, jamais
recalculés ; aucun tarif ou plafond de dépassement affirmé sans source lue ;
absence de devis notée comme fait, sans conclusion sur son caractère
obligatoire.

## Références métier et sources à rechercher

Code de la santé publique, information sur les frais (piste L1111-3 et
textes d'application) ; Code de la sécurité sociale pour le seul vocabulaire
de remboursement.

## Critères d'acceptation

- [ ] F01 compare facture et devis et prépare une demande d'explication.
- [ ] F02 sépare le reste à charge après remboursement et la facture du soignant.
- [ ] La sortie se termine par la phrase BASE-013 nommant le professionnel ou l'établissement, puis une association d'usagers.

## Vérification

- Cas normal : F01 — Dépassement d'honoraires supérieur au devis remis.
- Cas limite : F02 — Patient contestant un reste à charge qu'il attribue au chirurgien.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Calcul du remboursement, tarifs conventionnels affirmés, recouvrement,
envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
