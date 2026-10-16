---
id: ETU-020
titre: "Configurer les préférences d’un apprenant"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-021]
---

# ETU-020 — Configurer les préférences d’un apprenant

## Objectif et résultat attendu

Un profil minimal et modifiable renseigne cursus, objectifs et préférences déclarées sans autoriser des aides interdites ou prévoir l’examen.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/cold-start-interview/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/customize/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/CLAUDE.md` : adaptation ciblée à cette tâche.
- `law-student/references/learner-preferences.md` : à créer, propriétaire ETU-020.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Préférences utiles déjà données, cours/cursus déclarés et sources choisies ; accès explicite aux documents à indexer.

## Travail attendu

- Remplacer 1L/2L/3L/JD/bar jurisdiction comme schéma imposé par champs neutres et facultatifs.
- Ne pas exiger 10–20 documents/notes personnelles pour démarrer ; LIMITED DATA décrit couverture réelle sans seuil prétendument validé.
- Séparer préférence de feedback, consigne d’évaluation, droits sur les supports et validité du droit ; pas de profilage du professeur ou de diagnostic de learning style.
- Fin d’interview : bilan et choix de prochaine tâche, aucune séance MBE automatique ; customize ne lève ni intégrité ni isolation.
- Conserver les garde-fous partagés en corrigeant localement toute consigne answer-anyway qui prétendrait contourner aide autorisée ou sources.

## Sources à rechercher lors de l'implémentation

Déclarations de l’apprenant, consignes réelles et permissions d’usage des supports ; contrat d’isolation local et données minimales.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Démarrage utile sans connecteur, profil d’entreprise ni historique de notes ; aucune lecture globale de cours par défaut.
- [ ] La préférence « donne toujours la réponse » ne produit pas de devoir substitutif ni de règle non vérifiée.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : PA01 — Étudiant fournit seulement matière et objectif : profil minimal attribué, prochaine tâche proposée sans collecte obligatoire.
- Cas limite : PA02 — Changement de cursus/année ou refus de donner ses notes : garder ancien contexte distinct, démarrer sans ces données.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

