---
id: VEH-007
titre: "Préparer la revue d'une annonce, d'un bon de commande et des garanties alléguées avant l'achat d'un véhicule"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-004]
---

# VEH-007 — Préparer la revue d'une annonce, d'un bon de commande et des garanties alléguées avant l'achat d'un véhicule

## Objectif et résultat attendu

Une personne qui s'apprête à acheter un véhicule sait ce que disent
l'annonce, le bon de commande et les garanties présentées, ce qui manque ou
se contredit, quelles pièces demander avant de signer ou de payer, et obtient
une liste de questions au vendeur.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/vehicle-purchase-precheck/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/revue-avant-achat.md` — points de lecture, pièces à demander, sources lues (à créer)
- `vehicle-legal/references/vente-vehicule.md` — relue, créée par VEH-004
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Annonce (capture datée), bon de commande ou projet de contrat, conditions de garantie présentées.
- Qualité déclarée du vendeur ; mode de paiement demandé ; versement déjà fait ou non.
- Kilométrage, date de première mise en circulation, contrôle technique, historique déclaré.
- Financement envisagé et reprise de l'ancien véhicule éventuels.

## Sortie attendue

1. Résumé : véhicule, vendeur, engagements présentés.
2. Tableau : élément annoncé, élément du bon de commande, garantie alléguée, écart ou silence.
3. Pièces à demander avant de signer ou de payer.
4. Signaux de prudence sur le paiement, présentés comme points à vérifier, sans accusation.
5. Questions au vendeur.
6. Suites : financement → DOM-004 ; vendeur suspect → CONSO-015 pour la vérification d'un vendeur, DOM-002 si une infraction est alléguée ; litige après achat → VEH-004 ou VEH-005.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `revue-avant-achat.md` et l'appliquer : une garantie « alléguée »
n'est retenue que si un document en précise le garant et le contenu ; un
silence du bon de commande est noté, pas interprété. Aucun avis sur le prix
ou l'état technique. Aucune démarche en ligne effectuée à la place de la
personne.

## Références métier et sources à rechercher

Informations précontractuelles (piste L111-1 du Code de la consommation) ;
pistes VEH-004 et VEH-005 ; information officielle sur l'historique et la
situation administrative du véhicule.

## Critères d'acceptation

- [ ] A01 compare annonce, bon de commande et garanties et liste les pièces à demander.
- [ ] A02 signale une garantie mentionnée sans document comme non établie.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat, et un professionnel de l'automobile pour l'état du véhicule.

## Vérification

- Cas normal : A01 — Annonce mentionnant une garantie, bon de commande silencieux.
- Cas limite : A02 — Vendeur demandant un virement avant toute visite du véhicule.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Avis sur le prix ou l'état technique, offre de crédit, démarches
d'immatriculation, envoi ou paiement.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
