---
id: ETU-015
titre: "Construire un plan de révision réaliste"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-021]
---

# ETU-015 — Construire un plan de révision réaliste

## Objectif et résultat attendu

Un planning proposé utilise échéance et disponibilité déclarées sans inventer calendrier officiel ni sujets probables.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/study-plan/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/study-plan-context.md` : à créer, propriétaire ETU-015.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Date cible avec provenance, matières et consignes, disponibilité explicitement donnée, contraintes que l’apprenant souhaite partager.

## Travail attendu

- Retirer calendriers CA/NextGen/UBE, fenêtres et pondérations de fréquence d’examen US comme valeurs françaises.
- Les phases 60/30/10 ou cram 80/20 sont facultatives et discutables, pas prescription universelle ; ne pas exclure un thème du programme sur la base d’annales.
- Réutiliser les contraintes déjà connues, permettre de ne pas détailler la vie personnelle et ne pas diagnostiquer l’apprenant.
- Séparer date déclarée, date officielle vérifiée et séances proposées ; absence d’authentification n’empêche pas un tableau local mais aucun rappel n’est prétendu créé.

## Sources à rechercher lors de l'implémentation

Programme/consignes et disponibilité fournis ; calendrier officiel correspondant à l’examen et l’année seulement s’il est effectivement vérifié.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Chaque date a son statut et le plan est modifiable sans promesse de réussite.
- [ ] Une indisponibilité rend la charge visible et négociable plutôt qu’un rattrapage irréaliste.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : PL01 — Date déclarée dans six semaines, quatre heures par semaine : proposer un plan borné et expliciter les choix.
- Cas limite : PL02 — Date CRFPA incertaine et peu de temps : garder date non vérifiée, demander règle officielle via ETU-018, aucune date américaine de remplacement.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

