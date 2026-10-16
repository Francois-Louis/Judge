---
id: FUN-007
titre: "Lire un titre de concession funéraire et préparer les questions à la commune"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-003]
---

# FUN-007 — Lire un titre de concession funéraire et préparer les questions à la commune

## Objectif et résultat attendu

Une personne qui souhaite inhumer un proche dans une sépulture existante, ou
qui reçoit un courrier de la commune sur une concession (échéance,
renouvellement, reprise), comprend ce que dit le titre, ce qui reste à
établir sur les droits des personnes concernées, et obtient la liste des
questions et un brouillon de demande à la commune.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/burial-concession-review/SKILL.md` — le skill (à créer)
- `funeral-legal/references/concession-funeraire.md` — types de concession, titulaires, droit d'inhumation, renouvellement, reprise, sources lues (à créer)
- `funeral-legal/references/volonte-et-decision.md` — relue, créée par FUN-003
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Titre de concession ou acte de la commune ; règlement du cimetière s'il est fourni.
- Courrier reçu de la commune et sa date ; affichage ou procès-verbal évoqué.
- Personnes déjà inhumées ; fondateur de la concession ; lien déclaré des demandeurs.
- Projet : inhumation, renouvellement, conversion, travaux, reprise contestée.

## Sortie attendue

1. Résumé : ce que dit le titre, ce que demande la commune ou la personne.
2. Fiche du titre : nature, durée lue, bénéficiaires désignés, dates recopiées.
3. Questions à établir sur le droit d'être inhumé ou de demander, sans réponse déduite du seul lien familial.
4. Brouillon de demande d'information ou de renouvellement à la commune.
5. Suites : exhumation ou transfert → FUN-012 ; recours contre une décision du maire → DOM-010 ; partage de la concession dans la succession → DOM-016.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `concession-funeraire.md` et l'appliquer : aucune durée, aucun tarif ni
délai de renouvellement n'est donné sans source lue ou mention du titre. La
commune n'est pas présumée en tort ; une reprise annoncée est lue comme un
stade de procédure à vérifier. Une échéance proche place un renfort en
tête.

## Références métier et sources à rechercher

CGCT, concessions dans les cimetières (pistes L2223-13 et suivants), reprise
des concessions en état d'abandon (piste L2223-17) et dispositions
réglementaires (pistes R2223-12 et suivants) ; police des cimetières
(pistes L2213-7 et suivants) ; règlement du cimetière communal comme pièce.

## Critères d'acceptation

- [ ] K01 lit le titre et prépare les questions à la commune, sans durée ni tarif non sourcés.
- [ ] K02 ne déduit pas le droit d'être inhumé du seul lien familial.
- [ ] La commune n'est pas présumée en tort ; aucune issue n'est promise.
- [ ] La sortie se termine par la phrase BASE-013 nommant un avocat ou le notaire selon la situation, avec renfort en tête en cas d'échéance.

## Vérification

- Cas normal : K01 — Courrier annonçant l'échéance d'une concession familiale, titre au nom d'un grand-père.
- Cas limite : K02 — Petit-fils demandant l'inhumation de son épouse dans le caveau, une tante s'y opposant.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Recours contentieux, succession, travaux de monument (FUN-010), envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 39–45, 53 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FK01 — Distinguer terrain commun et concession ; lire durée, nature individuelle/collective/familiale, bénéficiaires et conditions d’inhumation à vérifier sans promettre un emplacement.
- [ ] FK02 — Pour échéance, renouvellement, reprise ou abandon : titre, dates, notifications et procédure identifiés séparément ; ne pas transformer un courrier de reprise en perte définitive des droits.
- [ ] FK03 — Renonciation, columbarium ou scellement : recopier objet, durée et conditions ; alerter sur l’enjeu d’une signature irréversible sans arbitrer les droits des ayants droit.

Scénarios supplémentaires **attendus, non exécutés** : concession dite perpétuelle confrontée à une procédure d’abandon ; renonciation présentée comme formulaire banal ; famille sans concession demandant les possibilités d’inhumation.

Sources à ouvrir lors de l’implémentation : CGCT terrain commun, droit à inhumation, concessions, renouvellement/reprise et abandon ; titre, règlement et actes communaux applicables.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
