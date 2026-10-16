---
id: ETU-008
titre: "Relire un brouillon de dissertation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-007]
---

# ETU-008 — Relire un brouillon de dissertation

## Objectif et résultat attendu

Un retour distingue délimitation du sujet, démonstration et cohérence du plan selon les attentes fournies.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/legal-writing/SKILL.md` : adaptation ciblée à cette tâche.


Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Sujet, consigne, brouillon et sources ; grille de correction si disponible.

## Travail attendu

- Ajouter les critères dissertation au dispatch de legal-writing, sans réécriture substantielle.
- Localiser hors-sujet, juxtaposition d’arguments et références non établies ; demander à l’apprenant de reformuler.
- Ne pas déduire une note d’examen du nombre de parties, de citations ou de retours antérieurs.

## Sources à rechercher lors de l'implémentation

Consigne/grille réelle, corpus du cours et références lues ; typographie/citation selon établissement plutôt que Bluebook/ALWD imposés.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Les observations citent le brouillon et sont distinctes d’une validation du droit applicable.
- [ ] Les exemples de formulation restent abstraits et ne remplissent pas le devoir.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : RD01 — Deux parties répétitives : relever les passages et demander la distinction argumentative.
- Cas limite : RD02 — Consigne impose un format différent du modèle habituel : appliquer la consigne, sans imposer deux parties/deux sous-parties.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

