---
id: VEH-010
titre: "Conserver l'état d'un véhicule et préparer une expertise amiable"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-010 — Conserver l'état d'un véhicule et préparer une expertise amiable

## Objectif et résultat attendu

Une personne en désaccord avec un garage, un vendeur ou un loueur sur
l'état d'un véhicule sait quoi conserver avant toute réparation, comment
organiser un examen contradictoire, quelles questions poser à l'expert, et
obtient un brouillon de convocation de l'autre partie.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/vehicle-evidence-preservation/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/preuve-expertise.md` — conservation, examen contradictoire, mission, sources lues (à créer)
- `vehicle-legal/references/qualification-vehicule.md` — relue, créée par VEH-001
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Objet du désaccord et partie concernée ; tâche VEH d'origine.
- Lieu et état actuel du véhicule ; pièces remplacées conservées ou non ; réparation prévue.
- Rapports, diagnostics et photos existants ; protection juridique d'assurance évoquée.

## Sortie attendue

1. Résumé : désaccord, état à conserver, urgence éventuelle.
2. Liste de conservation : véhicule, pièces, photos datées, documents.
3. Questions à poser à l'expert, formulées sans réponse supposée.
4. Brouillon de convocation de l'autre partie à un examen contradictoire.
5. Ce qui reste à vérifier : effets d'une expertise non contradictoire, avec la source lue ou réservés.
6. Suites : expertise judiciaire → litigation (CTX-032) ; conservation avant procès → CTX-007 ; prise en charge des frais par la protection juridique → DOM-005.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `preuve-expertise.md` et l'appliquer : le skill ne désigne aucun
expert et ne choisit pas entre amiable et judiciaire ; il décrit ce qui
compte pour que l'examen soit utile. Une réparation imminente place un
renfort en tête. Aucune valeur probante affirmée sans source lue.

## Références métier et sources à rechercher

Code civil, preuve ; Code de la route, experts en automobile (pistes L326-1
et suivants) ; Code de procédure civile, mesures d'instruction avant procès
(piste 145), pour l'orientation litigation.

## Critères d'acceptation

- [ ] E01 produit liste de conservation, questions et convocation sans désigner d'expert.
- [ ] E02 signale qu'une réparation déjà faite rend l'état initial manquant, sans conclure sur la preuve.
- [ ] La sortie se termine par la phrase BASE-013 nommant un expert automobile pour la question technique et un avocat pour la stratégie de preuve.

## Vérification

- Cas normal : E01 — Désaccord avec un garage sur l'origine d'une casse moteur, véhicule encore au garage.
- Cas limite : E02 — Véhicule déjà réparé ailleurs, seules des photos subsistent.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Expertise technique, désignation d'un expert, expertise judiciaire,
procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 16, 20, 27, 113–114, 142, 161, 168, 179, 182 et 186 de la [matrice](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Exigences supplémentaires du futur skill, sans implémentation.

- [ ] F01 — Pièces à rendre contre consigne, codes effacés et réparation urgente : demander conservation possible, rapport initial, références, photos et chaîne de détention ; pas d'obligation absolue de restituer toute ancienne pièce, ni conservation mettant en danger.
- [ ] F02 — Rapport du garage seul, centre de contrôle ou dommage après remorquage : identifier auteur, mission et contradictoire ; préparer questions et convocation sans conclure à la force probante ou cause. Contrôle judiciaire → CTX-032/033 ; sécurité et conservation urgente en tête.

Les cas F ci-dessus constituent les scénarios complémentaires **attendus, non exécutés**. Recueillir les pièces nommées, produire la comparaison et le brouillon prévus par la story ; sans source accessible, réserver droit, tarif, calendrier et effet de la clause. Rechercher les textes sectoriels et jurisprudence pertinents avec version, champ et dates ; le texte utilisateur n'est pas une source juridique. [Portée et vérification](../dom-023-annexes/dom-023-frictions-verification.md).
