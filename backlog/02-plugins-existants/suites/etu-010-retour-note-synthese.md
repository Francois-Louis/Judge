---
id: ETU-010
titre: "Relire un brouillon de note de synthèse"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-009]
---

# ETU-010 — Relire un brouillon de note de synthèse

## Objectif et résultat attendu

Le retour vérifie couverture du dossier, fidélité et organisation sans ajouter une opinion ou réécrire la note.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/legal-writing/SKILL.md` : adaptation ciblée à cette tâche.


Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Brouillon, dossier avec pages identifiées, consigne et éventuelle grille.

## Travail attendu

- Créer les critères synthèse dans legal-writing ; distinguer ajout externe, déformation d’une pièce et document omis.
- Citer passage du brouillon et pièce support, demander une correction par l’apprenant.
- Ne pas noter favorablement un argument juridique extérieur lorsque la consigne exige un dossier fermé.

## Sources à rechercher lors de l'implémentation

Consigne, pièces lues et grille éventuelle ; pas de recherche de droit actuel nécessaire pour certifier la fidélité à un dossier fermé.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Retour traçable aux pièces, aucune note corrigée générée.
- [ ] Une pièce inaccessible reste non contrôlée, pas implicitement validée.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : RS01 — Brouillon omet la réserve d’une pièce : citer la réserve et demander de la restituer fidèlement.
- Cas limite : RS02 — Bonne règle actuelle mais extérieure au dossier fermé : signaler l’écart méthodologique sans la glisser dans la synthèse.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

