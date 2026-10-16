---
id: ETU-018
titre: "Qualifier une préparation au CRFPA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-018 — Qualifier une préparation au CRFPA

## Objectif et résultat attendu

Une fiche précise année, épreuve, matière/option, consigne et statut des règles consultées avant tout entraînement.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/bar-prep-questions/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/cold-start-interview/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/session/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/crfpa-context.md` : à créer, propriétaire ETU-018.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Examen et session déclarés, établissement/IEJ si pertinent, épreuve visée, consigne, modalités d’aide et pièces officielles disponibles.

## Travail attendu

- Ne pas renommer MBE, MEE, MPT, UBE ou NextGen en CRFPA ; retirer leurs formats/seuils/calendriers des défauts français.
- Nom visible préparation CRFPA seulement après qualification ; bar-prep-questions garde son chemin technique initial mais aucun mode mixed par silence.
- Vérifier les modalités officielles actuelles pour la session ciblée, dates et programme avec provenance ; une date dans le profil reste déclarée.
- Router vers tâche adaptée : cas pratique ETU-019, synthèse ETU-009/010 si consigne correspond, oral ETU-011 seulement dans sa portée ; hors couverture reste explicitement non implémenté.

## Sources à rechercher lors de l'implémentation

Textes officiels et informations officielles de la session/organisateur, consignes de l’IEJ/établissement ; versions et dates à vérifier à l’implémentation.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] « Bar exam » sans précision déclenche clarification, pas choix d’un examen ou d’une matière.
- [ ] Ni durée, coefficient, format ni calendrier français n’est affirmé depuis la mémoire ou des règles américaines.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : CR01 — Candidat fournit session, épreuve et règlement : produire contexte et source/version, puis proposer la tâche correspondante.
- Cas limite : CR02 — « Fais des questions bar prep, je ne sais pas quel examen » : demander cible, méthode générale possible sans MBE ni CRFPA supposé.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

