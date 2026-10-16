---
id: ETU-017
titre: "Vérifier un point de droit pour une révision"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-017 — Vérifier un point de droit pour une révision

## Objectif et résultat attendu

Une vérification ponctuelle et sourcée établit l’état documentaire d’un point daté, distinct de la méthode et du contenu historique du cours.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/outline-builder/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/flashcards/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/CLAUDE.md` : adaptation ciblée à cette tâche.
- `law-student/.claude-plugin/plugin.json` : adaptation ciblée à cette tâche.
- `law-student/README.md` : adaptation ciblée à cette tâche.
- `law-student/skills/actualiser-point-droit/SKILL.md` : à créer, propriétaire ETU-017.
- `law-student/references/study-law-refresh.md` : à créer, propriétaire ETU-017.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Point précis, matière/territoire, date de référence, source du cours et motif de la vérification.

## Travail attendu

- Créer une tâche bornée chargeant méthode et isolation embarquées ; chercher/lire texte officiel et version pertinente selon BASE-005/BASE-010.
- Distinguer retrieval, lecture, état de version et applicabilité ; accès à un connecteur ou confiance du modèle ne valent pas vérification.
- Pas de flag-but-don’t-use qui applique comme vraie une règle incertaine ; réserver la seule proposition dépendante et poursuivre l’aide de méthode possible.
- Rattacher résultat au point/source/version, proposer une mise à jour de carte séparée sans écraser cours historique ni enrichir une note à dossier fermé.

## Sources à rechercher lors de l'implémentation

Textes français/UE et décisions officiels réellement pertinents, avec versions et dates d’effet ; corpus officiel via voies accessibles, sans calendrier d’examen implicite.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Sortie contient question, sources réellement lues, versions/date et réserves ; inaccessible n’est pas vérifié.
- [ ] Aucun abonnement PISTE obligatoire ; voies officielles alternatives et limites documentées, sans installer un outil de maintenance comme dépendance runtime.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : AD01 — Point daté dans une carte : comparer au texte officiel lu et proposer une nouvelle version attribuée.
- Cas limite : AD02 — Accès impossible et cours de 2019 : conserver cours daté, recherche à poursuivre et conclusion réservée, pas règle de mémoire actuelle.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

