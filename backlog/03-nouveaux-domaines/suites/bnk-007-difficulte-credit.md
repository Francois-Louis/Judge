---
id: BNK-007
titre: "Faire face à des échéances de crédit impayées"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-005]
---

# BNK-007 — Faire face à des échéances de crédit impayées

## Objectif et résultat attendu

Un emprunteur en difficulté sur un crédit identifié comprend sa situation,
les options à vérifier (report, réaménagement, délais) et prépare une demande
au prêteur.

## Périmètre et fichiers

- `banking-legal/skills/credit-repayment-difficulty/SKILL.md` — le skill (à créer)
- `banking-legal/references/difficulte-credit.md` — options, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

`credit.md` (BNK-005) est relu, pas réécrit.

## Pièces et informations nécessaires

Contrat ; échéancier ; impayés et courriers ; déchéance du terme annoncée ou
non ; assurance emprunteur ; autres dettes.

## Sortie attendue

Situation du crédit ; options à vérifier ; brouillon de demande au prêteur ;
questions ; limites. Aucun montant recalculé.

## Travail attendu

Plusieurs dettes → DOM-024. Prise en charge par l'assurance → DOM-005.
Acte de recouvrement ou de saisie → DOM-003. Inscription à un fichier → BNK-010.

## Références métier et sources à rechercher

Code de la consommation, défaillance de l'emprunteur ; Code civil, délais de
grâce (piste 1343-5).

## Critères d'acceptation

- [ ] C01 prépare la demande au prêteur sans montant recalculé.
- [ ] C02 oriente la situation globale vers DOM-024.

## Vérification

- Cas normal : C01 — Deux échéances de prêt auto impayées après une perte d'emploi.
- Cas limite : C02 — Trois crédits et des retards de loyer.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Dossier de surendettement, procédure, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 65–66 et 69 de la [matrice](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

- [ ] C03 — Déchéance du terme annoncée : lire clause, mises en demeure, réception et échéances ; ventiler sommes réclamées et décompte à demander, sans recalcul.
- [ ] C04 — Ancien impayé et proposition de nouvel accord : distinguer délai de grâce, prescription et forclusion ; relever incident, régularisations, accords, actes et dates puis orienter l'analyse contentieuse, sans déclarer la créance éteinte ni recommander une signature.
- [ ] C05 — Demande de délai : exposer aménagement contractuel et voie judiciaire à vérifier comme options distinctes, sans les promettre.

Scénarios C03–C05 **attendus, non exécutés** : exigibilité globale après relances, crédit à la consommation ancien avec réaménagement, perte temporaire de revenus. Sources supplémentaires : déchéance, forclusion et point de départ selon les faits, effet éventuel des accords ; contentieux → EXIST-006 et actes de recouvrement → DOM-003. Aucun calcul de forclusion livré par cette tranche.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
