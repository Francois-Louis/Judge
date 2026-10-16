---
id: CRIM-006
titre: "Lire un acte de poursuite ou un jugement pénal"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-006 — Lire un acte de poursuite ou un jugement pénal

## Objectif et résultat attendu

Une personne qui reçoit une citation, une convocation devant un tribunal,
une ordonnance pénale ou un jugement comprend l'acte, son stade, la date
éventuelle d'audience et les questions à poser à un avocat.

## Périmètre et fichiers

- `criminal-legal/skills/court-document-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/references/actes-poursuite.md` — types d'actes, stades, voies de recours à vérifier, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte complet ; juridiction ; qualité de la personne (prévenue, victime,
témoin) ; date de signification ou de remise ; date d'audience ; avocat
désigné ou non ; ressources si l'aide juridictionnelle est envisagée.

## Sortie attendue

Fiche de l'acte et stade ; dates recopiées et prouvées ; voies de recours à
vérifier, sans délai calculé ; recours à un avocat et à l'aide
juridictionnelle à vérifier ; questions ; limites.

## Travail attendu

Une victime citée comme telle reçoit une sortie distincte de celle d'une
personne poursuivie. Ne jamais prédire la décision ni la peine.

## Références métier et sources à rechercher

Code de procédure pénale, modes de saisine des juridictions, ordonnance
pénale, voies de recours ; textes sur l'aide juridictionnelle.

## Critères d'acceptation

- [ ] J01 identifie l'acte, l'audience et le besoin d'avocat sans délai calculé.
- [ ] J02 distingue la position de victime et oriente vers la constitution de partie civile à vérifier.

## Vérification

- Cas normal : J01 — Citation devant le tribunal correctionnel dans un mois.
- Cas limite : J02 — Avis d'audience adressé à une victime.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Défense au fond, rédaction de conclusions, exécution de la peine.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 94–97 de la [matrice](../dom-002-frictions-utilisateurs.md). Le périmètre de lecture inclut la proposition de composition pénale reçue par une personne mise en cause ; ne pas la confondre avec ordonnance pénale, CRPC, jugement ou alternative adressée à la victime (CRIM-007).

- [ ] J03 — Composition : identifier stade, reconnaissance ou consentement sollicités et conséquence annoncée ; préparer les questions à l'avocat avant décision, sans conseiller acceptation ni refus.
- [ ] J04 — Ordonnance pénale : identifier matière, sanction, remise ou notification, pièces et voie d'opposition à vérifier ; ne pas appliquer un délai unique aux matières contraventionnelle et délictuelle. Aucun calcul ni acte d'opposition rédigé dans cette story.
- [ ] J05 — Version des faits contestée : tableau mention du document, récit déclaré, pièce contradictoire et question à l'avocat ; aucune déclaration reconstituée comme certaine. Acte administratif → DOM-010.

Scénarios **attendus, non exécutés** : composition présentée comme simple formalité ; ordonnance reçue sans audience et sans preuve de notification ; décision administrative prise pour jugement. CPP et notification des actes à rechercher pour chaque voie ; les délais du texte fourni ne font pas preuve.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
