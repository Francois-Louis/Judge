---
id: SAN-006
titre: "Orienter une demande d'indemnisation d'un dommage lié aux soins"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-005]
---

# SAN-006 — Orienter une demande d'indemnisation d'un dommage lié aux soins

## Objectif et résultat attendu

Une personne qui pense avoir subi un dommage à l'occasion de soins comprend
les voies d'indemnisation à examiner, ce qui les distingue, les faits et
pièces à réunir, et à qui demander conseil. Le skill oriente ; il ne dit pas
si le dommage est indemnisable.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/medical-harm-orientation/SKILL.md` — le skill (à créer)
- `health-legal/references/voies-indemnisation.md` — voies, critères à vérifier, sources lues (à créer)
- `health-legal/references/objets-demarche.md` — relue, créée par SAN-005
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Qualité : victime, représentant, ayant droit.
- Structure et statut public ou privé ; professionnel ; dates des soins et de la découverte du dommage.
- Nature déclarée de l'événement : acte, infection, produit de santé, défaut d'information, autre.
- Dossier médical obtenu ou non (SAN-001) ; démarches déjà faites et réponses ; offre reçue.

## Sortie attendue

1. Résumé : ce qui est allégué et les voies possibles à examiner.
2. Tableau des voies : amiable auprès de l'établissement ou de l'assureur du professionnel, commission de conciliation et d'indemnisation, juge selon le statut ; conditions à vérifier, sans seuil affirmé.
3. Pièces à réunir, en premier lieu le dossier médical.
4. Questions pour l'avocat ou l'association d'aide aux victimes.
5. Échéances : question signalée en tête, aucune date calculée sans source lue.
6. Suites : chiffrage du préjudice corporel → DOM-035 ; procédure → litigation ; plainte pénale → DOM-002.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `voies-indemnisation.md` et l'appliquer : ne qualifier ni faute, ni
aléa, ni infection associée aux soins ; ne pas affirmer de seuil de gravité,
de délai ou de montant ; offre reçue recopiée, non évaluée ; complémentaire
santé ou prévoyance → INS-009.

## Références métier et sources à rechercher

Code de la santé publique, responsabilité et indemnisation (pistes L1142-1
et suivants), commissions de conciliation et d'indemnisation, ONIAM ;
prescription (piste L1142-28) ; information après dommage (piste L1142-4).

## Critères d'acceptation

- [ ] H01 liste les voies à examiner pour un établissement public et un privé, sans conclure.
- [ ] H02 place la question d'échéance en tête sans calculer de date.
- [ ] H03 recopie une offre d'assureur sans l'évaluer et oriente le chiffrage vers DOM-035.
- [ ] La sortie se termine par la phrase BASE-013 nommant un avocat ou une association d'aide aux victimes, avec renfort en tête.

## Vérification

- Cas normal : H01 — Infection après une opération dans un hôpital public.
- Cas limite : H02 — Soins anciens, consolidation déclarée incertaine.
- Cas limite : H03 — Offre de l'assureur d'un dentiste libéral après une extraction.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Qualification de la faute, évaluation médicale, chiffrage, rédaction d'une
saisine ou d'une requête, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).

## Complément des frictions santé — 16 octobre 2026

Points 40, 68–90 et 140 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Reconstituer symptômes déclarés, actes, résultats, transferts et conséquences sans qualifier faute/aléa. Explication écrite du dommage ; dossier CCI → SAN-018, expertise amiable → SAN-019, chiffrage → DOM-035, transaction → CTX-039. Sanction et indemnisation distinctes, aucun effet automatique sur prescription.
- [ ] FS02 — Le scénario ci-dessous produit les distinctions et réserves demandées.

Scénario attendu : Infection, consolidation incertaine et offre définitive : trois questions distinctes, point de départ non déduit des seuls soins.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).
