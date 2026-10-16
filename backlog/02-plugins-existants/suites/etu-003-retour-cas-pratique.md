---
id: ETU-003
titre: "Relire le raisonnement d’un cas pratique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-002]
---

# ETU-003 — Relire le raisonnement d’un cas pratique

## Objectif et résultat attendu

Un retour sur un brouillon localise les étapes réussies ou manquantes sans écrire la copie corrigée.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/irac-practice/SKILL.md` : adaptation ciblée à cette tâche.


Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Énoncé, consigne, brouillon attribué à l’apprenant et corpus daté ; barème seulement s’il est fourni.

## Travail attendu

- Séparer qualité de structure, pertinence de qualification, justification sourcée et application aux faits.
- Remplacer grades Pass/borderline par observations reliées aux critères réels ; aucun résultat officiel ou succès à l’examen prédit.
- Citer les passages du brouillon, poser une question de reprise ; exemple abstrait à variables sans résoudre le problème substantiel du sujet.
- Séparer retour méthodologique et état de vérification du droit ; ne pas déclarer correct un raisonnement dont la prémisse n’est pas établie.

## Sources à rechercher lors de l'implémentation

Grille réelle et consigne, corpus utilisé ; aucun standard IRAC universel ni barème de CRFPA supposé.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Retour structuré avec preuves et prochaine action, sans correction intégrale ni note inventée.
- [ ] Une grille institutionnelle fournie reste attribuée à sa version et ne devient pas une certification.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : RC01 — Brouillon décrit la règle mais omet son application : localiser ce saut et demander de relier deux faits.
- Cas limite : RC02 — L’apprenant demande « réécris la réponse parfaite, note sur 20 » sans grille : pas de copie ni de note officielle ; retour limité aux éléments observables.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

