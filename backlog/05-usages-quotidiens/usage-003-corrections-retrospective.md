---
id: USAGE-003
titre: "Appliquer les corrections issues de la rétrospective des usages quotidiens"
statut: terminee
priorite: P1
nature: implementation
dependances: [USAGE-001, USAGE-002]
---

# USAGE-003 — Appliquer les corrections issues de la rétrospective des usages quotidiens

## Objectif

Corriger les écarts relevés par la [rétrospective de l'epic](retrospective-usages-quotidiens.md)
qui ne demandent aucune décision de l'utilisateur : protocole sans consommateur
ni version, critères cochés sur une simple relecture, critère de classement
implicite, situations sans identifiant et historique non commité.

## Périmètre

- Epic 05 : protocole USAGE-001, story et relevé USAGE-001, comparaison USAGE-002,
  matrice des situations, rétrospective.
- Aval : [PILOTE-002](../01-pilote-travail/pilote-002-revue-embauche.md) et la
  [recette BASE-006](../../references/package-validation.md).
- Backlog : README, [modèle de story](../story-template.md), NOTICE.

## Travail attendu

- Relier le protocole aux stories et contrôles qui produiront une sortie
  destinée à une personne sans formation juridique.
- Versionner le protocole et fixer sa règle de reprise dans les paquets.
- Distinguer, sur les critères concernés, relecture du rédacteur et essai réel.
- Écrire le critère déterminant du classement USAGE-002.
- Donner un identifiant stable à chaque situation de la matrice.
- Commiter le travail en cours par lots séparés, sans push.

## Critères d'acceptation

- [x] PILOTE-002 et la checklist d'un skill BASE-006 renvoient au protocole et
  demandent d'en citer la version.
- [x] Le protocole porte une version et indique comment un skill le reprend.
- [x] Aucun critère vérifié seulement sur cas fictifs n'apparaît comme un essai
  réel ; PILOTE-002 porte un critère d'essai réel qui reste non coché sans participant.
- [x] Les 42 situations ont un identifiant `S-01` à `S-42` ; T1 à T5 y renvoient.
- [x] Le travail antérieur est commité en lots distincts sur une branche dédiée,
  sans push.

## Hors périmètre

Choix du pilote, essai de compréhension avec un utilisateur réel, adaptation
d'un skill, politique de recensement dans NOTICE, push, PR ou publication.

## Bilan d'exécution — 15 octobre 2026

- Commits sur la branche `usages-quotidiens/usage-001-003`, sans push :
  PILOTE-001/BASE-010, puis USAGE-001/USAGE-002, puis cette story. Les fichiers
  partagés (README, NOTICE, PILOTE-002) ont été découpés selon la story
  d'origine de chaque passage ; l'état final est inchangé.
- Protocole USAGE-001 en version `1.0.0`. Il n'est pas copié tel quel dans les
  paquets : seule une méthode transverse limitée peut être partagée, et le
  fichier renvoie au backlog. Un skill reprend les exigences utiles à sa tâche
  et cite la version appliquée.
- Recette BASE-006 passée en `1.1.0` : contrôle de la sortie au regard du
  protocole, et contrôle de reformulation noté `non exécuté` sans participant réel.
- PILOTE-002 : renvoi au protocole, deux critères ajoutés (conformité au
  protocole, essai réel consigné), liste « Points de départ » réunifiée.
- USAGE-001 : les deux critères de langage portent la mention « vérifié sur
  cas fictifs par le rédacteur » ; le décompte du relevé est daté.
- README : critère déterminant du classement écrit en une phrase.
- Matrice : colonne `N°`, identifiants `S-01` à `S-42`, règle de numérotation ;
  T1 à T5 renvoient à S-18, S-12, S-29, S-01 et S-02.
- Modèle de story : limites regroupées dans un paragraphe « Portée ».
- Formatage : lignes vides finales retirées de 20 fichiers (16 stories TRAV,
  découpage et inventaire PILOTE-001, PILOTE-002, matrice).

## Portée

Corrections documentaires seulement : aucun skill, plugin, manifeste ou
script modifié. Les contrôles rejoués portent sur la navigation et la forme ;
ils ne valident ni règle juridique ni compréhension par un utilisateur réel.
Restent ouverts : choix du pilote, essai réel (dans PILOTE-002) et politique
de recensement dans NOTICE.
