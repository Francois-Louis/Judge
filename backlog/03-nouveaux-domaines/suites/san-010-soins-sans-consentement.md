---
id: SAN-010
titre: "Lire une mesure de soins psychiatriques sans consentement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-010 — Lire une mesure de soins psychiatriques sans consentement

## Objectif et résultat attendu

Une personne admise en soins psychiatriques sans son consentement, ou un
proche, comprend la décision reçue, qui l'a prise, les contrôles et droits
à vérifier, et à qui s'adresser sans attendre, en premier lieu un avocat.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/involuntary-care-orientation/SKILL.md` — le skill (à créer)
- `health-legal/references/soins-sans-consentement.md` — types de mesures, contrôles, droits, sources lues (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Décision ou notification reçue ; auteur (directeur d'établissement, préfet) ; date.
- Qualité du demandeur ; personne concernée majeure ou mineure.
- Audience annoncée, avocat désigné ou non ; isolement ou contention mentionnés.
- Aucune pièce exigée si elle n'est pas disponible pendant la mesure.

## Sortie attendue

1. Renfort en tête : mesure en cours, avocat et audience à vérifier immédiatement.
2. Fiche : type de mesure invoqué, auteur, date, contrôles annoncés.
3. Droits et contrôles à vérifier, avec la source lue : information, recours devant le juge, commission départementale.
4. Questions pour l'avocat.
5. Suites : accès au dossier après la mesure → SAN-001 avec modalités particulières ; mesure de protection → DOM-026.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `soins-sans-consentement.md` et l'appliquer : aucune appréciation de
l'état de santé ou de la nécessité des soins ; aucune date d'audience ou de
contrôle calculée ; mineur → régime à rechercher, sans assimilation ;
détenu → orientation particulière à rechercher ; garde à vue → CRIM-002.

## Références métier et sources à rechercher

Code de la santé publique (pistes L3211-1 et suivants, L3212-1, L3213-1,
L3211-12, L3211-12-1, L3222-5-1) ; contrôle par le juge judiciaire ;
commission départementale des soins psychiatriques.

## Critères d'acceptation

- [ ] P01 place l'avocat et l'audience en tête et lit la décision sans juger l'état de santé.
- [ ] P02 distingue décision du directeur et arrêté préfectoral, à vérifier sur la pièce.
- [ ] P03 traite l'isolement mentionné comme question à soumettre, sans conclusion.
- [ ] La sortie commence par le renfort BASE-013 et se termine par la phrase nommant un avocat.

## Vérification

- Cas normal : P01 — Admission à la demande d'un tiers, audience annoncée sans date connue.
- Cas limite : P02 — Notification illisible, auteur incertain.
- Cas limite : P03 — Proche signalant un placement à l'isolement.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Rédaction d'une requête, appréciation médicale, calcul de délai, mineurs et
détenus au fond, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).

## Complément des frictions santé — 16 octobre 2026

Points 148–149 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Séparer admission, maintien, programme, isolement/contention et communications ; décisions/fondements à demander, avocat et contrôle judiciaire à vérifier immédiatement sans date inventée. Accès aux soins psychiatriques → SAN-013.
- [ ] FS02 — Le scénario ci-dessous produit les distinctions et réserves demandées.

Scénario attendu : Contention et appels restreints sans notification : avocat et pièces sans inventer audience ou nécessité médicale.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).
