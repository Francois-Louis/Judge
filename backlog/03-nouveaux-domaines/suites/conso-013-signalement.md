---
id: CONSO-013
titre: "Préparer le signalement d'une pratique commerciale"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-013 — Préparer le signalement d'une pratique commerciale

## Objectif et résultat attendu

Une personne qui constate une pratique commerciale qui lui paraît trompeuse
prépare un signalement factuel et comprend qu'il ne règle pas son propre
litige.

## Périmètre et fichiers

- `consumer-legal/skills/practice-report/SKILL.md` — le skill (à créer)
- `consumer-legal/references/signalement.md` — canaux en vigueur et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Captures datées ; adresse du site ou du magasin ; identité du professionnel ;
faits constatés ; démarche individuelle déjà faite.

## Sortie attendue

Fiche de signalement ; canal à vérifier ; pièces ; distinction signalement et
réclamation ; limites. Aucun envoi.

## Travail attendu

Ne pas qualifier la pratique d'infraction. Escroquerie alléguée → DOM-002 ;
données → privacy. Une demande de remboursement renvoie à CONSO-001 ou
CONSO-006.

## Références métier et sources à rechercher

DGCCRF et service public de signalement en vigueur à la date du lot.

## Critères d'acceptation

- [ ] S01 produit une fiche factuelle sans qualification d'infraction.
- [ ] S02 explique la limite et oriente vers la réclamation individuelle.

## Vérification

- Cas normal : S01 — Site affichant des prix barrés jamais pratiqués selon la personne.
- Cas limite : S02 — Personne qui attend un remboursement du signalement.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Dépôt du signalement, plainte, publication.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
