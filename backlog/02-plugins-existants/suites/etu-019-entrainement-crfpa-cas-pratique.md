---
id: ETU-019
titre: "Entraîner un cas pratique dans un contexte CRFPA défini"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-002, ETU-003, ETU-018]
---

# ETU-019 — Entraîner un cas pratique dans un contexte CRFPA défini

## Objectif et résultat attendu

Un exercice fictif et un retour guidé respectent l’épreuve qualifiée, sans questions américaines traduites ou note prédictive.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/bar-prep-questions/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/irac-practice/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/crfpa-cas-pratique.md` : à créer, propriétaire ETU-019.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Contexte ETU-018, matière précisément retenue, sources, consigne et aide autorisée ; tentative de l’apprenant.

## Travail attendu

- Borner le premier exercice à une matière et une consigne choisies dans le lot ; ne pas couvrir tout le CRFPA en une suite.
- Réutiliser méthode et retour cas pratique, pas générer un corrigé complet ; hypothèses et règle de correction sourcées.
- Retirer NCBE/majority/state law et grades de réussite comme gabarit ; toute durée/grille vient de la consigne vérifiée, sinon inconnue.
- La progression mesurée est celle de l’exercice fait, pas une prédiction de réussite ni une valeur comparable aux cartes autoévaluées.

## Sources à rechercher lors de l'implémentation

Règles officielles de l’épreuve/session réellement retenue, consigne et corpus de la matière ; aucun contenu de préparation protégé réutilisé sans droit.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] L’exercice documente fictif, cible, sources et limite ; sortie distincte d’un QCM MBE.
- [ ] Un corpus absent interdit de corriger comme vraie une règle de mémoire, sans bloquer les questions de structure.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : EC01 — Épreuve/matière qualifiées et corpus : exercice fictif borné, réponse de l’apprenant puis retour sur application.
- Cas limite : EC02 — Demande d’ensemble de toutes épreuves ou de corrigé à remettre : borner la tâche et garder les restrictions d’aide.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

