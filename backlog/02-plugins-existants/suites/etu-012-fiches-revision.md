---
id: ETU-012
titre: "Construire des fiches de révision à partir du cours"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-012 — Construire des fiches de révision à partir du cours

## Objectif et résultat attendu

Un support de révision conserve les sources et contributions de l’apprenant, sans remplir un cours de mémoire.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/outline-builder/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/revision-notes.md` : à créer, propriétaire ETU-012.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Cours/plan daté, objectif de révision, notes de l’apprenant, version et périmètre du corpus.

## Travail attendu

- Conserver trame et méthode inductive ; retirer l’exception permettant de produire une majority rule de mémoire sans marqueur.
- Séparer contenu du cours, propos de l’apprenant et règle extérieure vérifiée ; un document fourni ne certifie pas son actualité.
- Nom visible « fiches/support de révision », chemin outline-builder conservé au départ ; pas de confusion avec plan de dissertation ou fiche d’arrêt.
- Divergences de sources signalées ; actualisation d’un point relève de ETU-017 et ne remplace pas silencieusement un cours historique.

## Sources à rechercher lors de l'implémentation

Cours et syllabus versionnés, consigne de révision ; textes officiels seulement pour une actualisation explicitement demandée.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Les rubriques remplies sont attribuées à une source ou à l’apprenant.
- [ ] La demande de remplir tout le cours n’active aucun override de règle non sourcée.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : FR01 — Plan et notes datées : trame, références et questions pour compléter les lacunes.
- Cas limite : FR02 — Deux notes contradictoires sans texte : conserver divergence et demander vérification, pas sélectionner la règle qui paraît familière.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

