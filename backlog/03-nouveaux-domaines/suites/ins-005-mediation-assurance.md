---
id: INS-005
titre: "Escalader une réclamation d'assurance jusqu'au médiateur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-005 — Escalader une réclamation d'assurance jusqu'au médiateur

## Objectif et résultat attendu

Après un refus maintenu ou une absence de réponse, une personne identifie le
service réclamations puis le médiateur compétent, et prépare la saisine avec
les conditions à vérifier.

## Périmètre et fichiers

- `insurance-legal/skills/insurance-mediation/SKILL.md` — le skill (à créer)
- `insurance-legal/references/mediation-assurance.md` — étapes, médiateurs, rôle des autorités, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Réclamation et réponse ; dates ; médiateur indiqué au contrat ; organisme
(assureur, mutuelle, institution de prévoyance) ; procédure éventuelle.

## Sortie attendue

Étape suivante ; médiateur identifié selon l'organisme ou manque ; conditions
de recevabilité à vérifier ; question de prescription posée sans calcul ;
brouillon de saisine ; limites.

## Travail attendu

Accepter la sortie d'INS-001, INS-003 ou une réclamation fournie. Un
signalement à l'autorité de contrôle n'est pas présenté comme un recours.

## Références métier et sources à rechercher

Médiation de l'assurance et médiateurs des mutuelles et institutions de
prévoyance ; Code de la consommation, médiation ; prescription (pistes L114-1,
L114-2 du Code des assurances).

## Critères d'acceptation

- [ ] M01 prépare la saisine sans délai non sourcé.
- [ ] M02 identifie un médiateur différent pour une mutuelle.

## Vérification

- Cas normal : M01 — Refus maintenu après réclamation écrite.
- Cas limite : M02 — Refus d'une mutuelle santé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Procédure judiciaire, envoi.

## Complément issu des frictions assurance

Sections délais et recours, points 30 et 90 de la [matrice](../dom-005-frictions-utilisateurs.md). Conserver réclamation initiale et preuve de réception, accusé, réponse définitive ou absence de réponse, niveaux internes proposés, statut de consommateur ou professionnel et procédure parallèle éventuelle.

- [ ] M03 — Réponse finale ou silence : vérifier accès, date limite et médiateur compétent sans imposer par principe un deuxième niveau interne.
- [ ] M04 — Distinguer recommandation ACPR, obligation légale, règles de recevabilité du médiateur et date de suivi interne ; aucun délai universel pour tous les organismes.
- [ ] M05 — Signalement ACPR : expliquer son rôle distinct ; ne pas lui attribuer le pouvoir de trancher ce litige et d'ordonner le versement individuel.
- [ ] M06 — Prescription : conserver une question autonome et orienter vers INS-021 ; aucune réclamation ou saisine tenue pour automatiquement interruptive ou suspensive.
- [ ] M07 — Contrat professionnel : vérifier accès au dispositif concerné ; ne pas promettre la médiation gratuite de consommation.

Scénarios M03–M07 **attendus, non exécutés** : réponse finale avant le délai de silence, deuxième service interne présenté comme obligatoire, recommandé d'indemnisation distinct d'une relance simple, professionnel visant le médiateur de consommation. Sources à ouvrir : règles du médiateur, traitement des réclamations, recommandation ACPR et communiqué allégué en avril 2026, sans leur conférer le même statut.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
