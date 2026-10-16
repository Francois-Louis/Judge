---
id: ETU-021
titre: "Isoler et documenter les données d’apprentissage"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-021 — Isoler et documenter les données d’apprentissage

## Objectif et résultat attendu

Un contrat local sépare cours/année/exercice, modèles installés et données de l’apprenant, sans fusion ou migration implicite.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/CLAUDE.md` : adaptation ciblée à cette tâche.
- `law-student/README.md` : adaptation ciblée à cette tâche.
- `law-student/skills/session/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/study-plan/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/flashcards/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/study-data-contract.md` : à créer, propriétaire ETU-021.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Racine de configuration active BASE-008, modèles et formats inline existants, contextes d’apprentissage autorisés et politique de conservation effective.

## Travail attendu

- Définir identifiants de contexte, provenance, version et portée d’accès des plans/cartes/journaux/trackers ; pas de nouveaux fichiers d’état dans le paquet.
- Garder judge_store.py et isolation.md byte pour byte ; appeler le helper déjà livré pour toute écriture et ne pas ajouter de chemin d’origine ou fallback au répertoire courant.
- Traiter plan.session_history et session-history.yaml comme états existants distincts jusqu’à migration explicite/idempotente avec préservation ; ETU-014 possède le producteur unique des événements.
- Clarifier dans README les stockages contradictoires et les treize skills, dont customize oublié dans la table actuelle ; aucun état étudiant, tâche de notification ou connecteur français n’est livré aujourd’hui.

## Sources à rechercher lors de l'implémentation

Contrat BASE-008, formats existants réellement lus, règles de conservation/accès effectivement fournies ; aucun nouveau droit de stockage présumé.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Deux cours/années ne lisent pas leurs cartes ou résultats mutuellement sans sélection autorisée.
- [ ] Échec du garde d’écriture reste échec explicite, aucun contournement par fichier local ou modèle installé.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : DA01 — Deux cours autorisés : sélection explicite de contexte, écriture via helper dans la seule racine active.
- Cas limite : DA02 — Ancien journal présent et nouveau plan vide : pas de perte/merge automatique ; signaler les états et proposer une procédure de migration documentée.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

