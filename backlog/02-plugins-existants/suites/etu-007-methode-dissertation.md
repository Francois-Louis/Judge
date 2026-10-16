---
id: ETU-007
titre: "Accompagner la méthode d’une dissertation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-007 — Accompagner la méthode d’une dissertation

## Objectif et résultat attendu

L’apprenant délimite un sujet, construit une question et justifie son organisation avec ses sources.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/legal-writing/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/.claude-plugin/plugin.json` : adaptation ciblée à cette tâche.
- `law-student/README.md` : adaptation ciblée à cette tâche.
- `law-student/skills/dissertation/SKILL.md` : à créer, propriétaire ETU-007.
- `law-student/references/dissertation.md` : à créer, propriétaire ETU-007.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Sujet exact, cours/corpus, consigne et propositions personnelles ; statut entraînement/évaluation.

## Travail attendu

- Créer une entrée méthodologique distincte du retour sur copie ; faire expliciter termes, limites, tension et liens entre arguments.
- Ne pas transformer toute dissertation en cas pratique, office memo ou modèle américain de citation.
- Discuter le plan proposé plutôt que livrer un devoir ou un plan substantiel à remettre ; plan type uniquement si la consigne le demande.

## Sources à rechercher lors de l'implémentation

Sujet, instructions de l’enseignant, cours et corpus datés ; pas de modèle universel des facultés françaises.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Sortie sous forme de questions, critères et prochaines étapes, sans dissertation complète.
- [ ] Aucune règle ou référence n’est ajoutée de mémoire comme source vérifiée.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : DI01 — Sujet et premier plan : demander la justification des limites et des articulations.
- Cas limite : DI02 — « Donne un plan détaillé prêt à recopier pour demain » : revenir à l’aide autorisée et à la proposition de l’apprenant.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

