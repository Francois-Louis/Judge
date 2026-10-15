---
id: DOM-001
titre: "Cadrer un plugin de droit de la consommation"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-001 — Cadrer un plugin de droit de la consommation

## Objectif

Donner aux litiges de consommation leur propre plugin, distinct des contrats commerciaux B2B.

Nom de plugin proposé : `consumer-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualité des parties, canal de vente, territoire, rôle des plateformes et pièces nécessaires.
- Tâches candidates : revue de CGV B2C, rétractation, garanties, inexécution, réclamation et médiation.
- Frontières avec banque, assurance, voyages et données ; éviter un second plugin qui reproduit toutes leurs procédures.
- Répartir les litiges sectoriels avec [travaux](dom-015-construction-travaux.md), [énergie/eau](dom-021-energie-eau.md), [télécoms/poste](dom-022-telecoms-poste.md), [véhicules](dom-023-vehicules-garages.md), [prestations funéraires](dom-031-deces-obseques.md) et [services numériques](dom-034-numerique-plateformes.md). Les règles générales utiles peuvent être réutilisées, sans créer deux traitements concurrents du même dossier.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code de la consommation, Code civil, textes UE applicables, DGCCRF et CEC France pour l'orientation transfrontalière.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de réclamation pour non-livraison, à borner après cadrage.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une commande en ligne jamais livrée.
- Un produit défectueux et une garantie commerciale invoquée.
- Un achat professionnel présenté à tort comme achat de consommateur.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

