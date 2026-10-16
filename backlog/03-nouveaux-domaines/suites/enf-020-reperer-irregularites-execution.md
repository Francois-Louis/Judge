---
id: ENF-020
titre: "Repérer les irrégularités possibles d'un acte d'exécution"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001, ENF-006]
---

# ENF-020 — Repérer les irrégularités possibles d'un acte d'exécution

## Objectif et résultat attendu

Une personne qui reçoit un commandement, un procès-verbal de saisie ou une
dénonciation obtient la liste des mentions et conditions à vérifier, les
points à soumettre à un avocat et l'urgence liée au délai de contestation,
sans conclusion sur la nullité. Ajout du 16 octobre 2026
([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `enforcement-legal/skills/enforcement-defect-review/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/irregularites-execution.md` — mentions prescrites, conditions, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

`qualification-acte.md` (ENF-001) et la référence d'ENF-006 sont relus, pas réécrits.

## Pièces et informations nécessaires

Acte complet ; titre exécutoire visé et sa signification ; mode et date de
remise ; décompte ; actes antérieurs ; contestation déjà engagée.

## Sortie attendue

Bloc d'urgence (un délai de contestation peut courir, à vérifier) ; tableau :
mention ou condition exigée, texte lu, constat sur l'acte (présente, absente,
douteuse), condition à vérifier (grief, régularisation), question à
l'avocat ; limites. Jamais « l'acte est nul ».

## Travail attendu

Remise contestée → ENF-006 pour les faits ; décompte → ENF-003 ; saisie sur
compte → ENF-004 et ENF-019. Ne pas proposer de contestation dilatoire ni
promettre une mainlevée.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution et Code de procédure civile : mentions
prescrites selon l'acte, conditions de la mesure, régime des nullités et
compétence du juge de l'exécution ; jurisprudence sur le grief.

## Critères d'acceptation

- [ ] R01 produit le tableau des mentions avec textes lus, sans conclusion de nullité.
- [ ] R02 place l'urgence en tête sans délai calculé et nomme l'avocat.

## Vérification

- Cas normal : R01 — Procès-verbal de saisie-attribution sans indication relue comme exigée.
- Cas limite : R02 — Commandement de payer reçu il y a longtemps, saisie récente : questions sur le titre et le délai, sans calcul.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Assignation devant le juge de l'exécution, évaluation des chances, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-003-annexes/dom-003-decoupage-execution.md).
