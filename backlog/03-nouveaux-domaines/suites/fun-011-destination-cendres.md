---
id: FUN-011
titre: "Préparer les questions et la demande sur la destination des cendres"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-003]
---

# FUN-011 — Préparer les questions et la demande sur la destination des cendres

## Objectif et résultat attendu

Des proches qui doivent décider de la destination des cendres après une
crémation, ou qui ne s'accordent pas, voient les volontés connues, les
options à vérifier, la personne dont la décision est attendue et les
démarches correspondantes, et obtiennent un brouillon de demande à
l'interlocuteur concerné.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/cremation-ashes-decision/SKILL.md` — le skill (à créer)
- `funeral-legal/references/destination-cendres.md` — options, démarches, interlocuteurs, sources lues (à créer)
- `funeral-legal/references/volonte-et-decision.md` — relue, créée par FUN-003
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Volontés du défunt sur les cendres et leur forme.
- Lieu où l'urne se trouve (crématorium, opérateur, domicile) et depuis quand.
- Option envisagée par chacun ; lieu visé (cimetière, site cinéraire, nature).
- Signataire de la crémation ; échanges avec le crématorium ou la commune.

## Sortie attendue

1. En tête : urne en attente ou non, désaccord ou non.
2. Tableau des volontés et des positions, comme en FUN-003.
3. Options à vérifier, chacune avec la source lue ou réservée, sans affirmer ce qui est permis.
4. Démarches et interlocuteurs pour l'option retenue par la personne qui décide.
5. Brouillon de demande au crématorium ou à la commune.
6. Suites : désaccord bloquant → FUN-003 et avocat ; inhumation de l'urne dans une concession → FUN-007.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `destination-cendres.md` et l'appliquer : aucune option n'est
présentée comme permise ou interdite sans source lue ; aucun délai de
conservation de l'urne n'est donné sans texte lu. La personne qui décide
n'est pas désignée par le seul lien familial.

## Références métier et sources à rechercher

CGCT, destination des cendres (pistes L2223-18-1 et suivants) ; Code civil
(piste 16-1-1).

## Critères d'acceptation

- [ ] U01 présente les options avec leur source lue ou réservée et prépare la demande.
- [ ] U02 renvoie un désaccord bloquant vers FUN-003 avec renfort en tête.
- [ ] Aucun choix n'est recommandé ; aucun proche n'est présumé de mauvaise foi.
- [ ] La sortie se termine par la phrase BASE-013 nommant un avocat en cas de désaccord.

## Vérification

- Cas normal : U01 — Volonté écrite de dispersion en pleine nature, urne au crématorium.
- Cas limite : U02 — Un enfant a emporté l'urne chez lui, un autre demande son inhumation.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Saisine du juge, plainte, élément étranger, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 20, 48–54 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FU01 — Qualifier date de crémation, dépôt, lieu actuel, destination envisagée et volonté connue ; domicile, partage, dispersion, urne/scellement et concession sont des questions distinctes.
- [ ] FU02 — Pour chaque destination : formalité, interlocuteur, justificatif et règle lue ou réservée ; identifier déclaration de dispersion, durée temporaire, notification et renouvellement éventuel sans importer un délai non vérifié.
- [ ] FU03 — Ne pas traiter les cendres comme un actif à répartir ; désaccord et décision imminente → FUN-003 avec renfort, sans décider pour les proches.

Scénarios supplémentaires **attendus, non exécutés** : urne au domicile depuis une date inconnue ; dépôt temporaire près de l’échéance alléguée ; dispersion envisagée en mer et deux proches réclamant chacun une partie des cendres.

Sources à ouvrir lors de l’implémentation : CGCT destinations, dépôt temporaire et formalités des cendres ; respect des restes, règles du lieu et concessions, y compris transitions selon la date.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
