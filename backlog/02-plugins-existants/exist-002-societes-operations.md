---
id: EXIST-002
titre: "Découper l'adaptation du droit des sociétés et des opérations"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-002 — Découper l'adaptation du droit des sociétés et des opérations

## Objectif

Adapter les tâches de sociétés et d'opérations à la forme sociale et aux actes français, sans reproduire les procédures de Delaware.

## Points de départ

- [corporate-legal/skills/written-consent/SKILL.md](../../corporate-legal/skills/written-consent/SKILL.md)
- [corporate-legal/skills/board-minutes/SKILL.md](../../corporate-legal/skills/board-minutes/SKILL.md)
- [corporate-legal/skills/entity-compliance/SKILL.md](../../corporate-legal/skills/entity-compliance/SKILL.md)
- [corporate-legal/skills/tabular-review/SKILL.md](../../corporate-legal/skills/tabular-review/SKILL.md)
- [corporate-legal/skills/integration-management/SKILL.md](../../corporate-legal/skills/integration-management/SKILL.md)

## Travail attendu

- Inventorier les décisions sociales, procès-verbaux, formalités, diligences et suivi d'opération ; les découper en stories distinctes.
- Qualifier forme sociale, statuts, pactes, pouvoirs, organe compétent et modalités de décision avant tout modèle de consentement écrit.
- Revoir les références et colonnes de due diligence ; conserver la traçabilité documentaire utile et isoler les formalités propres à chaque juridiction.
- Sources à prévoir et à vérifier lors des futures implémentations : Code civil, Code de commerce, textes d'application et formalités françaises à vérifier ; les statuts font partie des pièces nécessaires.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `corporate-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Comparer les tâches attendues pour une SAS et une SARL à partir de statuts fictifs, puis un dossier d'acquisition comportant une filiale étrangère.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

