---
id: PILOTE-003
titre: "Vérifier le pilote avant d'étendre l'adaptation"
statut: proposee
priorite: P1
nature: validation
dependances: [PILOTE-002]
---

# PILOTE-003 — Vérifier le pilote avant d'étendre l'adaptation

## Objectif

Vérifier que le découpage, les sources et l'installation fonctionnent sur un cas réel de skill.

## Points de départ

- [employment-legal/skills/hiring-review/SKILL.md](../../employment-legal/skills/hiring-review/SKILL.md)
- [employment-legal/README.md](../../employment-legal/README.md)
- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [backlog/](../../backlog/)

## Travail attendu

- Exécuter les contrôles de BASE-006 sur l'artefact du plugin, puis les scénarios du pilote.
- Relire les conclusions, limites et sources ; rechercher les effets indirects du profil, des agents et des commandes d'initialisation hérités.
- Établir un bilan court : points confirmés, défauts à corriger et décisions d'architecture restant ouvertes.
- Créer les stories d'implémentation suivantes à partir de l'inventaire, en gardant une tâche métier et un résultat vérifiable par story.

## Critères d'acceptation

- [ ] Les résultats observés et les vérifications impossibles sont rapportés séparément.
- [ ] Aucun simple contrôle de structure n'est présenté comme une validation juridique.
- [ ] Les défauts du pilote ont une correction identifiée avant généralisation.
- [ ] L'extension à un autre skill ou domaine est un choix explicite ; elle n'est pas lancée automatiquement par cette story.

## Vérification

Installer le plugin seul dans un environnement de test et rejouer au moins un scénario sans profil préalable et un scénario sans accès à une source.

## Hors périmètre

Publier une version, installer des plugins sur le compte de l'utilisateur ou poursuivre tous les domaines dans la foulée.

