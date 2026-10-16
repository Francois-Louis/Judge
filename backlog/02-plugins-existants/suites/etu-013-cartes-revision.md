---
id: ETU-013
titre: "Créer et revoir des cartes sourcées"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-012]
---

# ETU-013 — Créer et revoir des cartes sourcées

## Objectif et résultat attendu

Des cartes rattachées au cours/version sont revues par autoévaluation, sans certifier l’état du droit ni la mémorisation.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/flashcards/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/revision-cards.md` : à créer, propriétaire ETU-013.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Sources et notes choisies, périmètre de cours, préférence de révision et réponses de l’apprenant.

## Travail attendu

- Conserver question/réponse/source mais retirer les réponses de mémoire présentées comme black letter fiable.
- Distinguer right/partial/wrong auto-déclarés d’une correction sourcée ; une source fournie peut être ancienne ou erronée.
- Présenter intervalles Leitner comme convention configurable, pas garantie cognitive ou notification réellement programmée.
- Préserver identifiant/version de carte et lien à un point de droit à actualiser ; aucun écrasement silencieux des cartes historiques.

## Sources à rechercher lors de l'implémentation

Corpus retenu, réponse de l’apprenant et source de correction lue ; actualisation distincte ETU-017.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Chaque carte a provenance, contexte temporel et statut de vérification utile.
- [ ] Une carte incomplète est suspendue ou réservée plutôt qu’enseignée comme droit actuel.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : FC01 — Trois cartes d’un cours daté : demander les réponses, relever autoévaluation et prochaine révision proposée.
- Cas limite : FC02 — Carte de droit ancien demandée pour cours historique : garder sa date, sans la requalifier droit en vigueur ni créer une alerte réelle.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

