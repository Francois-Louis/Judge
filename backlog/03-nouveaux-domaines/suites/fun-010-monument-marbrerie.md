---
id: FUN-010
titre: "Comparer les travaux d'un marbrier au devis et préparer une réclamation"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-002]
---

# FUN-010 — Comparer les travaux d'un marbrier au devis et préparer une réclamation

## Objectif et résultat attendu

Une personne qui a commandé un monument, un caveau ou une gravure voit ce
qui avait été commandé, ce qui a été livré ou facturé et ce qui diffère, et
obtient un brouillon de réclamation au marbrier.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/funeral-monument-works/SKILL.md` — le skill (à créer)
- `funeral-legal/references/travaux-cimetiere.md` — devis de marbrerie, réception, règlement du cimetière, sources lues (à créer)
- `funeral-legal/references/lecture-devis-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Devis ou bon de commande signé ; maquette, texte de gravure validé.
- Facture ; photos du monument livré ; date de pose.
- Échanges avec le marbrier ; autorisation de travaux de la commune s'il en est fait mention.
- Signataire de la commande ; titulaire de la concession.

## Sortie attendue

1. Résumé : ce qui était commandé, ce qui est livré, ce qui est contesté.
2. Tableau : élément, commande (pièce), livré ou facturé, photo, écart.
3. Erreur de gravure comparée au texte validé, sans conclure sur la responsabilité.
4. Brouillon de réclamation demandant correction ou explication.
5. Suites : concession → FUN-007 ; médiateur à identifier ; repli CONSO-017 pour un devis ou une avance tant que le paquet n'est pas livré.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `travaux-cimetiere.md` et l'appliquer : le marbrier n'est pas présumé
fautif ; une malfaçon alléguée est une question technique nommée, non
tranchée. Aucun prix courant ni délai de réalisation n'est donné sans pièce
ou source lue.

## Références métier et sources à rechercher

Code civil, contrat d'entreprise (pistes 1710, 1787 et suivants) ; CGCT,
travaux dans les cimetières et règlement communal (pistes L2213-8 et
suivants), à vérifier ; information sur les prix des prestations, texte à
identifier.

## Critères d'acceptation

- [ ] T01 compare commande et livraison et prépare une réclamation mesurée.
- [ ] T02 rapproche l'erreur de gravure du texte validé sans conclure sur la faute.
- [ ] Aucune reprise gratuite ni remboursement n'est promis.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs ou le médiateur du secteur.

## Vérification

- Cas normal : T01 — Monument posé dans une teinte de granit différente de celle du devis.
- Cas limite : T02 — Date de naissance erronée gravée, le bon à graver signé portant la même erreur.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Expertise technique, concession, travaux hors cimetière, procédure, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 46–47 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FT01 — Séparer travaux nécessaires à l’opération envisagée, rénovation et embellissement ; rattacher caveau, ouverture/fermeture et gravure aux documents fournis et autorisations à vérifier.
- [ ] FT02 — Préparer demande de descriptif, prix et justification, sans expertise ni conclusion qu’un ouvrage neuf est obligatoire ; réduction/exhumation → FUN-012 pour l’opération distincte.

Scénarios supplémentaires **attendus, non exécutés** : rénovation globale proposée avec une simple ouverture de caveau ; frais d’autorisation et de fermeture mélangés au prix du monument.

Sources à ouvrir lors de l’implémentation : contrat d’entreprise, devis et prix, règlement du cimetière et autorisations locales applicables ; actes relatifs aux opérations funéraires séparés.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
