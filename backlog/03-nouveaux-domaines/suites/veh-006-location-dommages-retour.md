---
id: VEH-006
titre: "Répondre à un loueur qui réclame des dommages au retour du véhicule"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-006 — Répondre à un loueur qui réclame des dommages au retour du véhicule

## Objectif et résultat attendu

Une personne à qui un loueur de courte durée réclame des frais pour des
dommages constatés au retour compare les états de départ et de retour, les
justificatifs et le contrat, sait ce qui reste à établir, et obtient un
brouillon de réponse au loueur.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/rental-return-damage/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/etat-restitution.md` — comparaison des états de départ et de retour, justificatifs (à créer)
- `vehicle-legal/references/location-courte-duree.md` — contrat, franchise, clauses, sources lues (à créer)
- `vehicle-legal/references/qualification-vehicule.md` — relue, créée par VEH-001
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Contrat de location, conditions générales, options et rachat de franchise souscrits.
- État des lieux de départ et de retour, signés ou non ; photos datées ; retour hors présence.
- Facture ou estimation des dommages, devis, photos du loueur ; somme prélevée ou bloquée.
- Carte de paiement utilisée et assurance de la carte évoquée ; échanges.

## Sortie attendue

1. Résumé : dommages réclamés, somme recopiée, contestation.
2. Tableau : dommage, état de départ, état de retour, preuve, justificatif du coût.
3. Clauses du contrat à lire : franchise, rachat, procédure de constat ; avec la source lue ou réservées.
4. Brouillon de réponse au loueur demandant justificatifs ou contestant un poste.
5. Suites : préautorisation ou prélèvement → DOM-004 ; garantie de la carte ou de l'assurance → DOM-005 ; accident avec tiers → DOM-005 ; blessure → DOM-035.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `etat-restitution.md` et `location-courte-duree.md` et les appliquer :
un dommage absent de l'état de départ n'est pas présumé causé pendant la
location, ni l'inverse ; un retour sans état contradictoire est noté comme
fait. Montants recopiés, jamais réévalués. Aucune clause qualifiée d'abusive
sans source lue.

## Références métier et sources à rechercher

Code civil, louage de choses et restitution (pistes 1730 à 1732) ; Code de
la consommation, clauses abusives (piste L212-1) ; recommandations de la
Commission des clauses abusives sur la location de véhicules, à identifier.

## Critères d'acceptation

- [ ] L01 compare états et justificatifs et prépare une réponse sans présumer l'origine du dommage.
- [ ] L02 traite un retour en dehors des horaires comme fait à documenter, sans conclusion.
- [ ] Le prélèvement contesté est orienté vers DOM-004 comme objet distinct.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat.

## Vérification

- Cas normal : L01 — Rayure facturée au retour, absente de l'état de départ signé mais visible sur une photo prise au départ.
- Cas limite : L02 — Véhicule rendu en dehors des horaires, dommage constaté par le loueur seul le lendemain.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Location longue durée ou avec option d'achat (VEH-009), contestation du
paiement, garantie d'assurance, accident, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
