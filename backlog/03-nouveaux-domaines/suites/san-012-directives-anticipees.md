---
id: SAN-012
titre: "Préparer des directives anticipées et la désignation d'une personne de confiance"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-012 — Préparer des directives anticipées et la désignation d'une personne de confiance

## Objectif et résultat attendu

Une personne qui veut exprimer à l'avance ses volontés sur sa fin de vie ou
désigner une personne de confiance comprend la différence entre les deux,
les conditions de forme à vérifier, et obtient un brouillon structuré à
relire avec son médecin.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/advance-directives-preparation/SKILL.md` — le skill (à créer)
- `health-legal/references/directives-personne-confiance.md` — rôles, forme, conservation, sources lues (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Volontés exprimées par la personne ; personne envisagée comme personne de confiance.
- Mesure de protection éventuelle.
- Documents antérieurs déjà rédigés.

## Sortie attendue

1. Résumé : directives anticipées et personne de confiance, deux actes distincts.
2. Brouillon structuré de directives, avec les volontés exprimées et sans formulation médicale ajoutée.
3. Brouillon de désignation de la personne de confiance.
4. Conditions de forme, conservation et révision à vérifier, avec la source lue.
5. Suites : mesure de protection → DOM-026.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `directives-personne-confiance.md` et l'appliquer : aucune
suggestion de choix médical ; modèle officiel signalé comme information ;
personne de confiance distinguée d'un représentant légal et d'un mandataire.

## Références métier et sources à rechercher

Code de la santé publique (pistes L1111-6, L1111-11) ; modèles officiels du
ministère de la Santé comme information.

## Critères d'acceptation

- [ ] V01 structure les volontés exprimées sans les compléter.
- [ ] V02 distingue personne de confiance et tuteur pour une personne protégée, avec relais DOM-026.
- [ ] La sortie se termine par la phrase BASE-013 nommant le médecin traitant pour la relecture médicale et un notaire ou un avocat pour la forme.

## Vérification

- Cas normal : V01 — Personne âgée souhaitant refuser l'acharnement thérapeutique.
- Cas limite : V02 — Personne sous tutelle désignant sa sœur.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Conseil médical, mandat de protection future, dépôt ou enregistrement,
envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
