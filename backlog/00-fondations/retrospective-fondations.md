# Rétrospective de l'epic 00-fondations

Établie le **15 octobre 2026 (Europe/Paris)** sur BASE-001 à BASE-008, après
relecture des livrables et nouvelle exécution des contrôles. Les corrections
qui ne demandaient aucune décision sont tracées dans
[BASE-009](base-009-corrections-retrospective.md).

## Bilan

Les fondations sont solides et leurs preuves distinguent nettement ce qui est
vérifié, simulé ou non exécuté. L'epic n'est pas clos : BASE-008 reste
`en-cours` et le choix de BASE-002 appartient à l'utilisateur.

| Story | Statut | Point ouvert |
|---|---|---|
| BASE-001 | terminee | Réglages GitHub distants non inspectés |
| BASE-002 | terminee | **Choix A/B/C à décider** ; bouton « Leave fork network » non vérifié |
| BASE-003 | terminee | — |
| BASE-004 | terminee | Mise en œuvre par BASE-008 |
| BASE-005 | terminee | Plusieurs sources officielles inaccessibles à l'outil (403, JavaScript) |
| BASE-006 | terminee | Aucune installation réelle ni exécution de skill |
| BASE-007 | terminee | Rulesets GitHub distants non vérifiés |
| BASE-008 | en-cours | Recette en session authentifiée ; liens symboliques réels |
| BASE-009 | terminee | — |

## Ce qui a bien marché

- Discipline de preuve : outils absents, scénarios fictifs et limites signalés.
- Passage cadrage → implémentation : BASE-004 a fixé le contrat, BASE-008 l'a
  vérifié sur les vrais paquets détachés, pas sur le modèle.
- Architecture : un propriétaire par tâche, aucun plugin fourre-tout, méthode
  commune embarquée par copie identique dans chaque paquet.
- Aucune action distante non autorisée.

## Écarts constatés

1. Aucun commit : l'epic entier n'existait que dans le worktree.
2. README du backlog périmé après BASE-008 (statuts, synchronisation, limites).
3. Statut `en_cours` hors du vocabulaire `en-cours`.
4. Liens vers `.github/workflows/cla.yaml`, supprimé par BASE-007.
5. Preuves non reproductibles sur un poste neuf : `python3` du Microsoft Store,
   `jq` et `jsonschema` absents ; un second test était alors ignoré.
6. BASE-008 volumineuse (150 skills, environ 235 fichiers) : justifiée par
   l'atomicité du changement de namespace, mais difficile à relire.
7. Contradiction sur l'auto-update du hub relevée par BASE-001, toujours présente.
8. Chemins de profil fondés sur le home du système : `CLAUDE_CONFIG_DIR` ne
   les déplace pas. La recette doit isoler le home lui-même.

## Suites

| Action | Traitement |
|---|---|
| Commit sur une branche dédiée, sans push | Réalisé après BASE-009 |
| Points 2 à 5 et 7 | Corrigés dans BASE-009 |
| Choix du lien de fork | BASE-002, décision de l'utilisateur |
| Recette authentifiée, liens symboliques | BASE-008, hôte autorisant les liens symboliques et session jetable authentifiée |
| Point 8 | Rappelé dans la recette BASE-008 ; pas de changement de contrat |
| Taille des stories | Au-delà d'environ 50 fichiers modifiés, prévoir une relecture par une seconde personne |
