---
id: ETU-009
titre: "Accompagner une note de synthèse sur dossier"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-009 — Accompagner une note de synthèse sur dossier

## Objectif et résultat attendu

Une méthode de lecture et de classement aide l’apprenant à synthétiser un dossier délimité selon la consigne.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/legal-writing/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/.claude-plugin/plugin.json` : adaptation ciblée à cette tâche.
- `law-student/README.md` : adaptation ciblée à cette tâche.
- `law-student/skills/note-synthese/SKILL.md` : à créer, propriétaire ETU-009.
- `law-student/references/note-synthese.md` : à créer, propriétaire ETU-009.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Consigne, liste des pièces/pages, textes accessibles et première sélection de l’apprenant ; dossier complet ou couverture explicitement partielle.

## Travail attendu

- Créer une entrée de méthode qui distingue synthèse, dissertation, consultation et résumé pièce par pièce.
- Conserver périmètre documentaire, références des pièces, points communs/divergences et documents manquants.
- Si consigne impose dossier fermé, ne pas enrichir la copie de connaissances ou recherches externes ; une actualisation séparée ne contamine pas l’exercice.
- Faire proposer l’organisation par l’apprenant et expliquer les critères, sans produire une note prête à remettre.

## Sources à rechercher lors de l'implémentation

Dossier fourni et instructions de synthèse ; en contexte CRFPA, règles officielles de la session concernée à vérifier séparément par ETU-018.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Chaque piste renvoie au dossier effectivement lu, la neutralité et le format suivent la consigne réelle.
- [ ] Dossier incomplet donne couverture et manques visibles, pas une synthèse prétendument complète.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : NS01 — Six pièces accessibles et consigne dossier fermé : demander une matrice des thèmes et renvois, sans apport extérieur.
- Cas limite : NS02 — Trois pièces manquent et une source récente contredit le dossier historique : garder les manques, séparer la recherche extérieure de la note.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

