---
id: ETU-016
titre: "Décrire les annales sans prédire le sujet"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-016 — Décrire les annales sans prédire le sujet

## Objectif et résultat attendu

Un relevé descriptif montre corpus, occurrences, changements de programme et limites ; aucune probabilité de futur sujet.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/exam-forecast/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/study-plan/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/outline-builder/SKILL.md` : retirer la consommation des poids prédictifs.
- `law-student/skills/flashcards/SKILL.md` : retirer la consommation des poids prédictifs.
- `law-student/skills/irac-practice/SKILL.md` : retirer la consommation des poids prédictifs.
- `law-student/references/annales-analysis.md` : à créer, propriétaire ETU-016.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Annales dont l’usage est autorisé, programme/version, années et formats ; corpus effectif listé même incomplet.

## Travail attendu

- Retirer la promesse forecast, classements de probabilité, pondérations 3–5x et conseils probably-not-coming-back.
- Intitulé visible « analyse descriptive d’annales » ; conserver exam-forecast comme chemin technique initial clairement présenté comme hérité, sans alias fictif.
- Compter uniquement les éléments observés et montrer dénominateurs/manques ; même un corpus de six examens ne rend pas fiable une prédiction.
- Transmettre au planning une couverture de révision, pas une liste de sujets à ignorer ; ne pas profiler le professeur.
- Retirer les poids prédictifs et leurs renvois dans les fiches, cartes et exercices : aucun consommateur ne réintroduit les prévisions supprimées du producteur.

## Sources à rechercher lors de l'implémentation

Annales et syllabus autorisés/versionnés ; règles d’examen pour le format, aucune source ne permet de garantir le prochain sujet.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] La sortie distingue constat historique et choix personnel de révision, sans taux de chance future.
- [ ] Changement de programme rend les groupes non directement comparables et reste visible.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : AN01 — Quatre annales même programme : tableau des thèmes et années avec couverture et limites.
- Cas limite : AN02 — Une annale manquante et demande de pari de sujet : pas de pourcentage ou thème assuré ; inventaire et manques uniquement.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

