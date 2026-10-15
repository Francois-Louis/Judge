---
id: DOM-009
titre: "Cadrer un plugin douanes et import-export"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-009 — Cadrer un plugin douanes et import-export

## Objectif

Organiser les tâches douanières autour de la marchandise, du territoire et de l'opération.

Nom de plugin proposé : `customs-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Particulier/professionnel, voyageur/vente/importation commerciale, territoires douanier et fiscal, origine, provenance, valeur et usage.
- Tâches candidates : préparation documentaire, qualification d'une importation, lecture d'un contrôle ou avis, demande de remboursement/remise.
- Séparer classement/origine/valeur, formalités, dette et sanction ; expliciter les inconnues qui empêchent un taux ou un montant fiable.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des douanes français et de l'Union, actes associés, Douane française, TARIC et Access2Markets selon le besoin.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de préparation documentaire d'une opération bornée, sans calcul de droits sans données vérifiées.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un achat expédié depuis un pays tiers.
- Un envoi vers un territoire ultramarin.
- Un avis de contrôle ou de perception déjà notifié.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

