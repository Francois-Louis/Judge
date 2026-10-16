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

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 18, 32–48 de la [matrice](../dom-002-annexes/dom-002-frictions-utilisateurs.md). L'orientation couvre explicitement une audition libre déjà commencée ; CRIM-001 garde la convocation. Recueillir statut annoncé, faits notifiés, heure de début de toute contrainte, avocat demandé ou renonciation, langue, notification de droits et santé, sans exiger des pièces pendant la mesure.

La sortie sépare identité, déclarations sur les faits, assistance, silence, possibilité de départ et changement de mesure selon le statut vérifié. Ne pas transposer les droits du suspect au témoin. Distinguer PV de plainte et PV d'audition pour la remise d'une copie. Aucun contenu de réponse suggéré.

- [ ] M04 — Suspect entendu librement : rechercher faits notifiés, droit au silence, départ et conditions d'assistance ; ne pas recommander d'ignorer une convocation. Si le service indique une garde à vue, requalifier la mesure et les horaires.
- [ ] M05 — Avocat minimisé ou renonciation proposée pour aller plus vite : fournir la demande d'assistance à vérifier, sans promettre un calendrier. Examiner médecin, traitement, interprète, proche ou employeur à prévenir selon la source et les restrictions.
- [ ] M06 — PV inexact : demander relecture, correction ou mention du désaccord ; expliquer les effets d'un refus de signature seulement après lecture de la règle. Copie non remise ≠ violation présumée.
- [ ] M07 — Menottage, fatigue, pressions ou humiliations : santé et avocat d'abord, horaires et circonstances à préserver ensuite ; preuves → CRIM-020, signalement → CRIM-021, sans diagnostic de nullité.

Scénarios **attendus, non exécutés** : audition libre où le départ est refusé ; témoin devenu suspect ; PV contesté dont une copie est demandée ; proche non averti ; renonciation à l'avocat proposée. Sources supplémentaires à rechercher : CPP audition libre, témoin, vérification d'identité, procès-verbaux et menottage (pistes 61-1, 62, 78-3, 803), droits en garde à vue et exceptions.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-annexes/dom-002-decoupage-penal.md).
