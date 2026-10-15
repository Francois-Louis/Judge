---
id: PILOTE-001
titre: "Inventorier le plugin travail et découper son adaptation"
statut: proposee
priorite: P1
nature: audit
dependances: [BASE-003, BASE-005]
---

# PILOTE-001 — Inventorier le plugin travail et découper son adaptation

## Objectif

Préparer l'adaptation du plugin existant `employment-legal`, skill par skill.

## Points de départ

- [employment-legal/skills/](../../employment-legal/skills/)
- [employment-legal/agents/leave-tracker.md](../../employment-legal/agents/leave-tracker.md)
- [employment-legal/CLAUDE.md](../../employment-legal/CLAUDE.md)
- [employment-legal/.mcp.json](../../employment-legal/.mcp.json)
- [employment-legal/README.md](../../employment-legal/README.md)

## Travail attendu

- Examiner les 20 skills, le profil, l'agent et les références ; ne pas se limiter aux descriptions.
- Pour chaque workflow, distinguer logique réutilisable, règles américaines à remplacer et prérequis français à rechercher.
- Relever notamment at-will, classification exempt/non-exempt, FLSA, FMLA et modèles de rupture ; les remplacer exige une analyse métier, pas une traduction.
- Proposer les stories suivantes : qualification de la relation, rémunération/temps, rupture, congés, enquête interne, politiques et implantation. Fractionner une tâche encore trop large.

## Critères d'acceptation

- [ ] Chaque skill existant a une ligne dans l'inventaire avec ses dépendances de contenu.
- [ ] Les règles collectives, le secteur public/privé et les rattachements territoriaux sont prévus lorsque pertinents.
- [ ] Le skill `hiring-review` a une liste de sections à modifier et des scénarios de contrôle.
- [ ] Le reste du plugin reste explicitement non adapté à ce stade.

## Vérification

Suivre les appels de `leave-tracker` et des commandes d'enquête jusqu'aux agents et fichiers réellement utilisés pour éviter de manquer du droit américain indirect.

## Hors périmètre

Réécrire le plugin entier ou traiter les 20 skills dans la même livraison.

