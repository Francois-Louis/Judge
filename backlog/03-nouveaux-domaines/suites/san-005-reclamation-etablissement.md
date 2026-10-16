---
id: SAN-005
titre: "Préparer une réclamation sur une prise en charge auprès d'un établissement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-005 — Préparer une réclamation sur une prise en charge auprès d'un établissement

## Objectif et résultat attendu

Un patient ou un proche mécontent d'une prise en charge identifie ce qu'il
cherche (explication, sanction, signalement, indemnisation), sait que ces
objets ont des interlocuteurs distincts, et obtient un brouillon de
réclamation adressé à l'établissement pour l'explication et la médiation.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/care-complaint/SKILL.md` — le skill (à créer)
- `health-legal/references/objets-demarche.md` — quatre objets, interlocuteurs, sources lues (à créer)
- `health-legal/references/reclamation-etablissement.md` — réclamation, médiation, commission des usagers (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Qualité du réclamant ; établissement, service, dates du séjour ou de la consultation.
- Faits reprochés, décrits par la personne ; conséquences alléguées.
- Objectifs exprimés ; démarches déjà faites et réponses.
- Informations de santé strictement nécessaires à la compréhension des faits.

## Sortie attendue

1. Résumé : ce que la personne reproche et ce qu'elle cherche.
2. Tableau des objets : explication, sanction, signalement, indemnisation ; interlocuteur à vérifier pour chacun.
3. Brouillon de réclamation à l'établissement : faits datés, questions, demande d'explication ou de médiation.
4. Ce qui reste à vérifier : circuit interne, rôle de la commission des usagers, avec la source lue.
5. Suites : indemnisation → SAN-006 ; sanction → SAN-007 ; signalement → SAN-008.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `objets-demarche.md` et `reclamation-etablissement.md` et les
appliquer : ne jamais qualifier une faute ; ne pas présenter la réclamation
comme interrompant un délai ou ouvrant une indemnisation ; distinguer
établissement et professionnel libéral exerçant dans l'établissement ;
structure médico-sociale → point ouvert, orientation seulement.

## Références métier et sources à rechercher

Code de la santé publique, commission des usagers et médiation en
établissement (pistes L1112-3, R1112-79 et suivants, R1112-91 et suivants).

## Critères d'acceptation

- [ ] C01 produit une réclamation datée et factuelle pour une explication.
- [ ] C02 sépare sanction et indemnisation demandées dans le même message, avec deux suites distinctes.
- [ ] C03 n'emploie aucun terme de faute ou d'erreur médicale comme acquis.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'établissement, une association d'usagers ou un avocat selon l'objet.

## Vérification

- Cas normal : C01 — Attente prolongée aux urgences et absence d'information de la famille.
- Cas limite : C02 — « Je veux que le chirurgien soit puni et être indemnisé. »
- Cas limite : C03 — Récit affirmant une erreur de dosage sans pièce.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Appréciation médicale, plainte ordinale, signalement, demande
d'indemnisation, structures médico-sociales au fond, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
