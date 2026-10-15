---
id: EXIST-006
titre: "Découper l'adaptation des workflows de contentieux"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-006 — Découper l'adaptation des workflows de contentieux

## Objectif

Reconstruire les tâches de contentieux selon les procédures concernées, au lieu de traduire les noms des actes américains.

## Points de départ

- [litigation-legal/skills/subpoena-triage/SKILL.md](../../litigation-legal/skills/subpoena-triage/SKILL.md)
- [litigation-legal/skills/deposition-prep/SKILL.md](../../litigation-legal/skills/deposition-prep/SKILL.md)
- [litigation-legal/skills/privilege-log-review/SKILL.md](../../litigation-legal/skills/privilege-log-review/SKILL.md)
- [litigation-legal/skills/legal-hold/SKILL.md](../../litigation-legal/skills/legal-hold/SKILL.md)
- [litigation-legal/skills/demand-draft/SKILL.md](../../litigation-legal/skills/demand-draft/SKILL.md)
- [litigation-legal/skills/claim-chart/references/element-templates.md](../../litigation-legal/skills/claim-chart/references/element-templates.md)

## Travail attendu

- Classer les tâches réutilisables (chronologie, dossier, suivi) et celles nécessitant une refonte juridique.
- Décider du devenir et du nom des tâches subpoena, deposition et privilege log : absence d'équivalent automatique à documenter, tâche française à définir avant renommage.
- Séparer mise en demeure, conservation/production des preuves, rédaction d'écritures et suivi de procédure ; préciser les frontières avec pénal, administratif et exécution.
- Identifier les mentions de work product, discovery et without prejudice qui supposent une analyse de droit applicable.
- Sources à prévoir et à vérifier lors des futures implémentations : Codes de procédure selon la matière, Code civil, règles professionnelles et textes de compétence ; vérifier acte, notification et représentation.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `litigation-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Utiliser une mise en demeure reçue, une demande de production de pièce et une convocation française ; aucun de ces documents ne doit déclencher mécaniquement une procédure américaine.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

