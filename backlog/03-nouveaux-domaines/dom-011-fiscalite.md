---
id: DOM-011
titre: "Cadrer un plugin de fiscalité"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-011 — Cadrer un plugin de fiscalité

## Objectif

Distinguer l'assistance déclarative, le contrôle et la réclamation fiscale.

Nom de plugin proposé : `tax-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Impôt, période, contribuable, résidence, déclaration, acte reçu et stade de la procédure.
- Tâches candidates : lecture d'avis, préparation de réclamation, lecture de proposition de rectification, constitution de pièces.
- Séparer assiette, contrôle, recouvrement, pénalités et demande gracieuse ; prévoir les conventions et régimes particuliers sans tout traiter d'emblée.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code général des impôts, Livre des procédures fiscales, textes UE ou conventions pertinents, impots.gouv.fr et BOFiP avec portée à vérifier.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture et de qualification d'un document fiscal précisément identifié.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une erreur alléguée sur un avis d'impôt.
- Une proposition de rectification.
- Une demande de délai de paiement.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

