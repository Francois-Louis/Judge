---
id: CRIM-002
titre: "Orienter une personne ou un proche pendant une mesure en cours"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-002 — Orienter une personne ou un proche pendant une mesure en cours

## Objectif et résultat attendu

Un proche, ou la personne elle-même, pendant une garde à vue ou une retenue
en cours, obtient en quelques lignes ce qui peut être fait maintenant, ce qui
doit être demandé et à qui, sans durée calculée ni promesse.

## Périmètre et fichiers

- `criminal-legal/skills/custody-orientation/SKILL.md` — le skill (à créer)
- `criminal-legal/references/mesure-en-cours.md` — repères par mesure, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Mesure annoncée et par qui ; heure de début connue ou déclarée ; lieu et
service ; âge ; santé et traitement ; langue ; avocat déjà désigné ou non ;
lien de la personne qui écrit avec la personne retenue.

## Sortie attendue

Bloc court en tête : actions possibles maintenant (avocat, informations à
transmettre au service, santé) ; heure de début notée comme fait avec sa
source ; ce qu'un proche peut et ne peut pas faire, selon la source lue ;
questions ; limites. Aucune heure de fin ni prolongation calculée sans texte
lu et heure établie.

## Travail attendu

Déterminer d'abord la mesure : garde à vue, audition libre, vérification
d'identité, retenue douanière (DOM-009), retenue pour vérification du droit
au séjour (DOM-028). Mineur : orientation renforcée (CRIM-011). Ne pas
aider à joindre la personne par un moyen interdit, ni à faire passer un
message à un témoin ou une victime.

## Références métier et sources à rechercher

Code de procédure pénale, garde à vue et notification des droits (pistes
62-2 et suivants, 63-1 et suivants) ; Code de la justice pénale des mineurs ;
directives 2013/48/UE et (UE) 2016/800 ; modalités d'accès à un avocat de
permanence, à vérifier auprès des sources officielles.

## Critères d'acceptation

- [ ] M01 met l'action immédiate en tête, note l'heure de début sans calculer de fin.
- [ ] M02 traite la minorité possible avant tout autre point.
- [ ] M03 oriente la retenue pour le droit au séjour vers DOM-028.
- [ ] Aucune consigne de contournement ou de pression.

## Vérification

- Cas normal : M01 — « Mon frère est en garde à vue depuis 7 h au commissariat ; il n'a pas d'avocat. »
- Cas limite : M02 — Même message, âge inconnu, « il est au lycée ».
- Cas limite : M03 — « Retenu pour vérifier ses papiers. »

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contenu des déclarations, contestation de la régularité de la mesure,
contact du service, désignation d'un avocat à la place de la personne.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
