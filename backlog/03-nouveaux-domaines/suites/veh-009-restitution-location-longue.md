---
id: VEH-009
titre: "Comparer les frais de fin de location longue durée ou avec option d'achat au contrat"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-006]
---

# VEH-009 — Comparer les frais de fin de location longue durée ou avec option d'achat au contrat

## Objectif et résultat attendu

Un locataire particulier qui reçoit, à la restitution du véhicule, une
facture de remise en état ou de kilométrage excédentaire compare chaque
poste au contrat, au barème annoncé et aux constats, et obtient un brouillon
de demande d'explication ou de contestation.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/lease-return-charges/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/location-longue-duree.md` — clauses de restitution, barème, qualification, sources lues (à créer)
- `vehicle-legal/references/etat-restitution.md` — relue, créée par VEH-006
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Contrat, conditions générales, barème ou guide de restitution remis.
- Procès-verbal de restitution, rapport d'expertise de restitution, photos.
- Facture de fin de contrat, kilométrage contractuel et constaté recopiés.
- Option d'achat exercée ou non ; échanges.

## Sortie attendue

1. Résumé : frais réclamés et postes contestés.
2. Tableau : poste, montant recopié, clause ou barème, constat, écart.
3. Distinction entre usure et dommage telle que le contrat la définit, avec la source lue ou réservée.
4. Brouillon de demande d'explication ou de contestation.
5. Suites : régime du crédit et offre préalable → DOM-004 ; difficulté de paiement globale → DOM-024.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `location-longue-duree.md` et l'appliquer : la qualification de la
location avec option d'achat au regard du crédit sert seulement à orienter
vers DOM-004 ; aucun barème réévalué, aucune clause qualifiée d'abusive sans
source lue. La définition contractuelle de l'usure est citée, jamais
supposée.

## Références métier et sources à rechercher

Code de la consommation, location avec option d'achat dans le régime du
crédit (pistes L312-1 et suivants), pour la seule qualification ; clauses
abusives (piste L212-1) ; pistes VEH-006 pour la restitution.

## Critères d'acceptation

- [ ] D01 compare chaque poste au barème et au constat et prépare une demande sans réévaluer les montants.
- [ ] D02 oriente la question du financement vers DOM-004 comme objet distinct.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat.

## Vérification

- Cas normal : D01 — Frais de remise en état réclamés pour des éclats que le locataire considère comme de l'usure.
- Cas limite : D02 — Locataire contestant à la fois les frais de restitution et le coût total du financement.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Analyse du crédit, location courte durée (VEH-006), calcul de barème,
procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 118, 121–124 et 127 de la [matrice](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Exigences supplémentaires du futur skill, sans implémentation.

- [ ] F01 — Rayures, usure, expertise après départ et dépréciation sans travaux : distinguer constat, imputation, barème et fondement du poste ; demander photos et chronologie, sans déduire licéité ou illicéité de l'absence de travaux réalisés.
- [ ] F02 — Panne pendant location : relever qualité du bailleur, vendeur, locataire et garant, pouvoir d'agir et interlocuteur ; question de garantie → VEH-011 avec réserve de régime et de qualité ; lecture LLD → VEH-018 ; sortie LOA à découper en DOM-004. Aucune garantie d'un achat direct transposée au locataire.

Les cas F ci-dessus constituent les scénarios complémentaires **attendus, non exécutés**. Recueillir les pièces nommées, produire la comparaison et le brouillon prévus par la story ; sans source accessible, réserver droit, tarif, calendrier et effet de la clause. Rechercher les textes sectoriels et jurisprudence pertinents avec version, champ et dates ; le texte utilisateur n'est pas une source juridique. [Portée et vérification](../dom-023-annexes/dom-023-frictions-verification.md).
