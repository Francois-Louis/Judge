---
id: DOM-008
titre: "Cadrer un plugin transports et voyages"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-008 — Cadrer un plugin transports et voyages

## Objectif

Séparer les réclamations selon le mode, le trajet et le contrat de transport.

Nom de plugin proposé : `transport-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Mode, trajet, dates, transporteur effectif, vendeur, réservation unique ou contrats distincts, passager ou marchandise.
- Tâches candidates : retard/annulation aérienne, trajet ferroviaire, bagage, forfait touristique et réclamation transporteur.
- Distinguer remboursement, réacheminement, prise en charge et indemnisation ; ne pas appliquer un barème aérien au train ni le régime passager au fret.
- L'achat et la réparation d'un véhicule sont cadrés dans [DOM-023](dom-023-vehicules-garages.md), les prestations postales dans [DOM-022](dom-022-telecoms-poste.md). Réserver ici les obligations propres au trajet, au voyage ou au transport.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des transports, Code du tourisme, règlements UE et conventions dans leur champ, Your Europe et autorités françaises compétentes.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de réclamation pour un mode et un type d'incident, à choisir au cadrage.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un vol annulé avec correspondance.
- Un retard ferroviaire.
- Un bagage perdu lors d'un voyage à forfait.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

