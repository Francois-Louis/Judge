---
id: FUN-003
titre: "Organiser volontés du défunt et qualité pour décider en cas de désaccord entre proches"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-001]
---

# FUN-003 — Organiser volontés du défunt et qualité pour décider en cas de désaccord entre proches

## Objectif et résultat attendu

Des proches en désaccord sur les obsèques (inhumation ou crémation, lieu,
cérémonie) voient clairement ce que le défunt a exprimé et sous quelle
forme, qui revendique la décision et sur quel fondement, ce qui reste à
établir, et savent qui joindre sans attendre quand la décision est bloquée.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/funeral-decision-authority/SKILL.md` — le skill (à créer)
- `funeral-legal/references/volonte-et-decision.md` — formes de volonté, qualité pour décider, urgence, sources lues (à créer)
- `funeral-legal/references/qualification-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Écrits du défunt : testament, lettre, déclaration, contrat obsèques ; paroles rapportées, par qui et quand.
- Proches concernés et position de chacun, sans jugement sur leurs motifs.
- Décision déjà prise, devis signé, opérateur choisi ; corps en attente et lieu.
- Mesure de protection du défunt connue ; désignation éventuelle d'une personne par le défunt.

## Sortie attendue

1. En tête : décision bloquée ou non, interlocuteur à joindre sans attendre si elle l'est.
2. Tableau des volontés : contenu, forme (écrite, rapportée, supposée), source, date.
3. Tableau des positions : proche, demande, fondement invoqué, pièce.
4. Fiche des trois qualités, sans désigner la personne qui décide à partir du seul lien familial.
5. Questions à établir et pièces à réunir ; options de dialogue sans en recommander une.
6. Suites : saisine du juge → avocat (point ouvert, aucune story de procédure) ; atteinte alléguée comme infraction → DOM-002 ; destination des cendres → FUN-011 ; succession → DOM-016.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `volonte-et-decision.md` et l'appliquer : le skill ne dit pas quelle
volonté l'emporte ni qui doit décider ; il organise les éléments et nomme ce
qu'un juge ou un avocat examinerait. Aucun délai de saisine ou de décision
n'est donné sans source lue ; l'urgence est signalée sans être chiffrée. Le
ton reste neutre envers chaque proche.

## Références métier et sources à rechercher

Loi du 15 novembre 1887 sur la liberté des funérailles, à lire dans sa
version en vigueur ; Code civil, respect dû au corps après la mort (piste
16-1-1) ; Code de procédure civile, contestation sur les conditions des
funérailles (piste 1061-1), pour l'orientation seule ; Code pénal, atteinte
à la volonté du défunt (piste 433-21-1), pour l'orientation DOM-002.

## Critères d'acceptation

- [ ] W01 distingue volonté écrite, rapportée et supposée, sans dire laquelle l'emporte.
- [ ] W02 place l'urgence en tête et oriente vers un avocat sans préparer de saisine.
- [ ] Aucune qualité pour décider n'est déduite du seul lien familial ; aucun proche n'est présumé de mauvaise foi.
- [ ] La sortie se termine par la phrase BASE-013 nommant un avocat, avec renfort en tête si la décision est bloquée.

## Vérification

- Cas normal : W01 — Enfants divisés entre crémation et inhumation, une lettre manuscrite non datée retrouvée.
- Cas limite : W02 — Corps en chambre funéraire, l'opérateur refusant d'agir tant que les proches ne s'accordent pas.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Saisine du juge, plainte, succession, médiation familiale menée par le
plugin, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
