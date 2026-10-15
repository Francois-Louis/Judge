---
id: DOM-021
titre: "Cadrer un plugin énergie, eau et services essentiels"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-021 — Cadrer un plugin énergie, eau et services essentiels

## Objectif

Aider les ménages à comprendre une facture, une modification de contrat ou une interruption de service.

Nom de plugin proposé : `utilities-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Vérifier les données d'une facture contestée : période, index, estimation, prix et régularisation.
- Préparer une réclamation sur une souscription, une modification, un déménagement ou une résiliation.
- Identifier les informations urgentes face à un impayé ou à une interruption annoncée.

## Qualification et frontières

Service, fournisseur/gestionnaire, contrat, compteur, relève, factures, dates, qualité d'abonné et courriers reçus.

Les règles de facturation et d'accès au service sont ici ; les charges du bailleur restent en DOM-006, la rénovation énergétique en DOM-015 et les aides sociales dans leur domaine.

## Sources à prévoir et vérifier

Code de l'énergie, règles de l'eau et des services publics selon l'opérateur, Code de la consommation, textes locaux et autorités sectorielles.

- [Médiateur national de l'énergie — litiges](https://www.energie-mediateur.fr/les-litiges/)
- [Impayés de factures — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F20055)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une régularisation d'électricité et préparer une demande de justification, sans extrapoler un régime à l'eau.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Eau, électricité, gaz, fourniture et réseau sont distingués ; le cadrage ne généralise pas une protection ou un médiateur à tous les services.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une facture augmente après une longue estimation.
- Un abonnement a changé sans accord allégué du client.
- Un courrier annonce une restriction ou une coupure.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

