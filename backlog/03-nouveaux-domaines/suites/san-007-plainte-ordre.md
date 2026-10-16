---
id: SAN-007
titre: "Préparer une plainte auprès de l'ordre d'un professionnel de santé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-005]
---

# SAN-007 — Préparer une plainte auprès de l'ordre d'un professionnel de santé

## Objectif et résultat attendu

Une personne qui reproche un manquement à un professionnel de santé sait si
une instance ordinale existe pour sa profession, ce que la procédure peut
et ne peut pas produire, et obtient un brouillon de plainte factuelle.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/professional-board-complaint/SKILL.md` — le skill (à créer)
- `health-legal/references/plainte-ordinale.md` — professions, conciliation, juridiction disciplinaire, sources lues (à créer)
- `health-legal/references/objets-demarche.md` — relue, créée par SAN-005
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Profession et nom du professionnel ; mode d'exercice ; lieu.
- Faits datés, pièces disponibles ; manquement allégué (secret, information, comportement, titre).
- Objectif : sanction ; autres objets signalés séparément.

## Sortie attendue

1. Résumé : instance ordinale à vérifier pour cette profession et ce qu'elle examine.
2. Ce que la plainte ne produit pas : pas d'indemnisation présumée.
3. Brouillon de plainte : faits, dates, pièces, sans qualification déontologique affirmée.
4. Étapes à vérifier : conciliation, transmission, juridiction disciplinaire.
5. Suites : indemnisation → SAN-006 ; infraction alléguée → DOM-002 ; traitement des données → PRV-026.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `plainte-ordinale.md` et l'appliquer : profession sans ordre →
orientation vers l'interlocuteur à rechercher ; professionnel salarié d'un
établissement public → règles particulières à vérifier ; titre usurpé ou
exercice illégal allégué → signalement possible et pénal en DOM-002.

## Références métier et sources à rechercher

Code de la santé publique, conciliation et juridiction disciplinaire
(pistes L4123-2, L4124-1) ; code de déontologie de la profession.

## Critères d'acceptation

- [ ] O01 produit une plainte factuelle pour un médecin libéral.
- [ ] O02 signale qu'un professionnel salarié d'un hôpital public relève de règles à vérifier.
- [ ] O03 sépare la plainte ordinale de la demande d'indemnisation.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'instance ordinale comme interlocuteur et un avocat comme conseil.

## Vérification

- Cas normal : O01 — Médecin ayant divulgué un diagnostic à l'employeur du patient, selon le récit.
- Cas limite : O02 — Interne d'un centre hospitalier public mis en cause.
- Cas limite : O03 — « Je veux sa radiation et des dommages-intérêts. »

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Qualification déontologique ou pénale, indemnisation, représentation à
l'audience, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
