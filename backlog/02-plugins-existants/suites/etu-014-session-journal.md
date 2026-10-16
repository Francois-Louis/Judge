---
id: ETU-014
titre: "Router une séance et consigner un seul bilan"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-021]
---

# ETU-014 — Router une séance et consigner un seul bilan

## Objectif et résultat attendu

Une séance choisit une tâche adaptée à la consigne et enregistre un événement unique attribué, sans défaut MBE.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/session/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/bar-prep-questions/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/flashcards/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/irac-practice/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/socratic-drill/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/study-plan/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/study-session-events.md` : à créer, propriétaire ETU-014.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Objectif, contexte, tâche disponible, historique autorisé et résultat réellement travaillé ; un plan n’est pas obligatoire.

## Travail attendu

- Retirer les routes MBE/essay par défaut pour le parcours français ; ne jamais envoyer un commentaire vers un générateur de questions bar américain.
- Définir identifiant, unité, source, état commencé/terminé/interrompu et producteur du bilan ; une seule écriture entre dispatcher et skill feuille.
- Unifier plan.session_history et fallback session-history.yaml sans migration implicite, perte de données ou double compte ; préserver anciens événements avec provenance.
- Ne pas additionner nombre de cartes, autoévaluations et scores de questions comme mesure commune de compétence ; aucun achèvement en cas d’abandon.

## Sources à rechercher lors de l'implémentation

Contrat de stockage BASE-008, historique réel autorisé et schemas inline existants ; aucun besoin de connecteur de calendrier.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Un événement réel de séance donne au plus une entrée, plan présent ou absent ; répétition idempotente documentée.
- [ ] Un skill non adapté/manquant donne une limite et une aide bornée, pas appel silencieux de l’ancien flux US.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : SE01 — Séance de trois cartes terminée sans plan : un bilan autoévalué au journal isolé, pas seconde écriture par session.
- Cas limite : SE02 — Séance interrompue puis reprise avec vieux journal : conserver deux états attribués au même identifiant, pas deux succès ni fusion destructrice.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

