---
id: BNK-012
titre: "Lire un engagement de caution ou un appel en garantie"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-005]
---

# BNK-012 — Lire un engagement de caution ou un appel en garantie

## Objectif et résultat attendu

Une personne qui va se porter caution d'un prêt, ou qui est appelée à payer
comme caution, comprend ce qu'elle garantit, les mentions et informations à
vérifier, et les questions à poser. Ajout du 16 octobre 2026
([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `banking-legal/skills/guarantee-review/SKILL.md` — le skill (à créer)
- `banking-legal/references/caution.md` — engagement, mentions, information, régimes dans le temps, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

`credit.md` (BNK-005) est relu, pas réécrit.

## Pièces et informations nécessaires

Acte de cautionnement ; prêt garanti ; date de l'engagement ; patrimoine et
revenus déclarés à la signature ; informations reçues depuis ; mise en
demeure ou appel ; lien avec l'emprunteur (dirigeant, proche).

## Sortie attendue

Fiche de l'engagement : montant et durée recopiés, mentions présentes ou
absentes ; régime applicable selon la date, à vérifier ; questions ;
brouillon de demande d'information ; limites. Aucune conclusion sur la
validité ni sur la disproportion.

## Travail attendu

Le régime du cautionnement a été réformé : établir la date de l'engagement
avant toute règle. Caution d'un dirigeant pour sa société : questions de
société → EXIST-002. Caution entre époux : DOM-013 pour le volet familial.
Plusieurs dettes → DOM-024.

## Références métier et sources à rechercher

Code civil, cautionnement (pistes 2288 et suivants, version selon la date de
l'engagement) ; Code de la consommation et Code monétaire et financier pour
l'information de la caution, selon le régime.

## Critères d'acceptation

- [ ] C01 recopie l'engagement et rattache le régime à sa date, sans conclure.
- [ ] C02 sépare la question de société et celle de la caution.

## Vérification

- Cas normal : C01 — Parent caution du prêt étudiant de son enfant, appel reçu.
- Cas limite : C02 — Gérant caution du prêt de sa SARL en difficulté.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Action contre la banque, négociation, procédure, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Point 97 de la [matrice](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

- [ ] C03 — Garantie personnelle d'un concours professionnel : distinguer dette de l'entreprise, engagement personnel, montant/durée/conditions recopiés et recours à vérifier ; ne pas confondre caution et sûreté sur un bien.
- [ ] C04 — Rupture du concours et appel de caution simultanés : produire deux questions ; le concours et la Médiation du crédit relèvent de BNK-018, sans suspension présumée de l'appel.

Scénarios C03/C04 **attendus, non exécutés** ; aucune extension à une action contre la banque.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
