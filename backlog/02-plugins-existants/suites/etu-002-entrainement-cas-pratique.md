---
id: ETU-002
titre: "Guider un entraînement de cas pratique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-002 — Guider un entraînement de cas pratique

## Objectif et résultat attendu

Un entraînement conduit l’apprenant à qualifier faits et questions, choisir une règle sourcée puis l’appliquer, selon la consigne réelle.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/irac-practice/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/cas-pratique.md` : à créer, propriétaire ETU-002.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Contexte ETU-001, énoncé pédagogique, corpus et tentative de l’apprenant ; hypothèse fictive explicitement identifiée si elle est générée.

## Travail attendu

- Conserver le raisonnement guidé et les questions successives ; ne pas fournir la solution complète du sujet de l’apprenant.
- Réécrire les présupposés US/majority rule ; présenter IRAC comme moyen possible d’organiser le raisonnement, sans équivalence normative avec le cas pratique français.
- Distinguer faits donnés, hypothèses, qualification, règle avec version et application ; laisser la conclusion dépendante d’une règle non vérifiée en réserve.
- Documenter le nom visible « entraînement au cas pratique » ; conserver provisoirement irac-practice comme chemin technique, sans inventer une nouvelle commande.

## Sources à rechercher lors de l'implémentation

Consigne, cours daté et textes/décisions effectivement lus ; actualisation ponctuelle via ETU-017 si nécessaire.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] L’apprenant produit l’application ; pas de syllogisme rempli à sa place ni de règle de mémoire déclarée fiable.
- [ ] Une pièce ou consigne manquante donne une question ciblée, pas une majorité américaine par défaut.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : CP01 — Hypothèse fictive et extrait de cours : faire qualifier les faits puis demander l’application avant tout retour.
- Cas limite : CP02 — Le sujet cite une règle sans texte/version : travailler la structure, demander la source et réserver sa justesse.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

