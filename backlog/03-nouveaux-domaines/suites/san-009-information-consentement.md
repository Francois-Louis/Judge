---
id: SAN-009
titre: "Préparer les questions et la demande d'information sur un acte de soins"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-001]
---

# SAN-009 — Préparer les questions et la demande d'information sur un acte de soins

## Objectif et résultat attendu

Un patient qui doit décider d'un acte, ou qui estime ne pas avoir été
informé avant un acte réalisé, obtient la liste des questions à poser, ce
que l'information doit permettre de comprendre selon la source lue, et un
brouillon de demande d'information écrite.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/care-information-request/SKILL.md` — le skill (à créer)
- `health-legal/references/information-consentement.md` — information, consentement, refus, sources lues (à créer)
- `health-legal/references/qualification-sante.md` — relue, créée par SAN-001
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Acte prévu ou réalisé, tel que décrit par la personne ; date.
- Documents remis : notice, formulaire de consentement, devis.
- Qualité : patient, parent d'un mineur, représentant.
- Urgence déclarée.

## Sortie attendue

1. Résumé : moment de la décision et ce qu'il faut comprendre avant.
2. Questions à poser au professionnel : bénéfices, risques, alternatives, conséquences d'un refus, frais.
3. Brouillon de demande d'information écrite.
4. Après un acte : défaut d'information allégué noté comme question, orientation SAN-006 si un dommage est invoqué.
5. Limites et phrase BASE-013.

## Travail attendu

Créer `information-consentement.md` et l'appliquer : aucune
recommandation médicale ; refus de soins présenté comme une décision à
éclairer avec le professionnel ; urgence médicale → secours en tête ;
mineur ou majeur protégé → SAN-002 pour la qualité ; frais → SAN-011.

## Références métier et sources à rechercher

Code de la santé publique, information et consentement (pistes L1111-2,
L1111-4) ; Code civil (piste article 16-3).

## Critères d'acceptation

- [ ] I01 produit des questions avant une opération programmée, sans avis médical.
- [ ] I02 note un défaut d'information allégué après l'acte comme question et oriente un dommage vers SAN-006.
- [ ] La sortie se termine par la phrase BASE-013 nommant le professionnel de santé pour l'information médicale et un avocat ou une association d'usagers pour le droit.

## Vérification

- Cas normal : I01 — Opération du genou proposée, consentement à signer.
- Cas limite : I02 — Complication non annoncée découverte après l'acte.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Avis sur l'opportunité d'un soin, consentement pour autrui, indemnisation,
envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
