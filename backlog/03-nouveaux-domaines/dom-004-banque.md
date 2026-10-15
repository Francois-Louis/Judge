---
id: DOM-004
titre: "Cadrer un plugin bancaire"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-004 — Cadrer un plugin bancaire

## Objectif

Organiser les tâches bancaires indépendamment de l'assurance et de la consommation générale.

Nom de plugin proposé : `banking-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Statut du client, prestataire, pays, contrat, opération et dates ; distinguer compte, paiement, crédit et investissement.
- Tâches candidates : contestation de paiement, réclamation bancaire, lecture d'une offre de crédit, frais/clôture de compte et incidents.
- Séparer paiement non autorisé, virement effectué sous tromperie et litige commercial ; prévoir les frontières avec surendettement et AMF.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code monétaire et financier, Code de la consommation selon le produit, textes UE applicables, Banque de France, ABE Infoservice, ACPR et AMF selon le sujet.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de qualification d'une contestation de paiement et de préparation de la réclamation.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un paiement par carte contesté.
- Un virement validé après une usurpation d'identité.
- Une réclamation sur des frais de compte professionnel.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

