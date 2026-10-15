---
id: DOM-023
titre: "Cadrer un plugin véhicules, garages et réparations"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-023 — Cadrer un plugin véhicules, garages et réparations

## Objectif

Aider acheteurs et propriétaires à examiner une vente, une facture ou une réparation de véhicule.

Nom de plugin proposé : `vehicle-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer la revue d'une annonce, d'un bon de commande et des garanties alléguées.
- Documenter une panne après achat selon la qualité du vendeur et les pièces.
- Lire devis, ordre de réparation, facture ou frais de gardiennage contestés.

## Qualification et frontières

Vendeur particulier/professionnel, acheteur, type de contrat, kilométrage, historique, dates, diagnostics, réparations et accords donnés.

L'achat, la location et la réparation du véhicule sont ici ; infraction/permis restent en DOM-002, l'assurance en DOM-005 et l'accident corporel requiert le régime identifié avec DOM-035.

## Sources à prévoir et vérifier

Code civil, Code de la consommation et textes automobiles pertinents, DGCCRF et règles de preuve/expertise applicables.

- [DGCCRF](https://www.economie.gouv.fr/dgccrf)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter une facture de garage et la comparer aux travaux autorisés par les pièces fournies.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Les régimes de vente entre particuliers, vente professionnelle, location et prestation de réparation ne sont pas confondus.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un garage facture une opération sans accord retrouvé.
- Une voiture d'occasion présente une panne peu après l'achat.
- Un loueur réclame des dommages au retour.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

