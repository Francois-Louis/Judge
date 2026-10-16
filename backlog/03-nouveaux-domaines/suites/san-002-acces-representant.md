---
id: SAN-002
titre: "Vérifier la qualité d'un proche ou d'un représentant avant une demande d'accès"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-002 — Vérifier la qualité d'un proche ou d'un représentant avant une demande d'accès

## Objectif et résultat attendu

Un parent, un représentant ou un proche qui veut accéder aux informations de
santé d'une personne vivante sait si sa qualité est établie, quelles pièces
la prouvent et ce qui reste à vérifier ; si elle l'est, il obtient un
brouillon de demande. Sinon, il reçoit les questions utiles, sans demande
rédigée en son nom.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/representative-record-request/SKILL.md` — le skill (à créer)
- `health-legal/references/qualite-demandeur.md` — qualités, pièces probantes, réserves (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/references/acces-dossier.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Lien avec la personne : parent, tuteur, personne habilitée, mandataire, conjoint, enfant, personne de confiance.
- Âge de la personne concernée ; mesure de protection et décision ou mandat s'ils existent.
- Accord ou opposition connus de la personne concernée ; capacité de s'exprimer déclarée.
- Structure, informations visées et période.

## Sortie attendue

1. Résumé : la qualité invoquée et ce qu'elle permet, avec la source lue ou réservé.
2. Fiche de qualité : lien déclaré, pièce qui l'établit, mesure et son étendue à vérifier.
3. Questions à résoudre avant toute demande.
4. Brouillon de demande seulement si la qualité est établie par une pièce et une source lue.
5. Suites : étendue d'une mesure → DOM-026 ; accord de la personne → demande par le patient (SAN-001).
6. Limites et phrase BASE-013.

## Travail attendu

Créer `qualite-demandeur.md` et l'appliquer :

- mineur : autorité parentale et souhait du mineur à rechercher, sans conclusion ;
- majeur protégé : nature de la mesure et pouvoir pour l'acte → DOM-026 ;
- proche sans mesure ni mandat : aucune demande en son nom ; accord ou démarche du patient proposés ;
- personne de confiance : rôle à rechercher, aucun droit d'accès présumé ;
- patient décédé → SAN-003.

## Références métier et sources à rechercher

Code de la santé publique (pistes L1111-5, L1111-7) ; Code civil, autorité
parentale et protection juridique des majeurs selon la mesure ; décision
ou mandat fourni.

## Critères d'acceptation

- [ ] Q01 produit un brouillon pour un parent dont la qualité est établie, avec les réserves sur le mineur.
- [ ] Q02 refuse de rédiger une demande pour un proche sans pouvoir établi et liste les questions.
- [ ] Q03 renvoie l'étendue d'une curatelle vers DOM-026 sans la présumer.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'établissement, le mandataire ou un avocat selon la situation.

## Vérification

- Cas normal : Q01 — Mère d'un enfant de dix ans demandant un compte rendu d'hospitalisation.
- Cas limite : Q02 — Fille aidante d'un père vivant, sans mandat ni mesure.
- Cas limite : Q03 — Curateur demandant le dossier d'une personne sous curatelle.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Étendue d'une mesure de protection au fond, ayant droit, relance,
consentement aux soins pour autrui, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).

## Complément des frictions santé — 16 octobre 2026

Points 100, 153–154 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Distinguer proche, personne de confiance, représentant et patient ; lire le pouvoir et la volonté de la personne. Après décès → SAN-003, sans représentation présumée maintenue.
- [ ] FS02 — Le scénario ci-dessous produit les distinctions et réserves demandées.

Scénario attendu : Personne de confiance demandant tout le dossier d'un résident capable : pouvoir et volonté à vérifier, aucun accès global promis.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).
