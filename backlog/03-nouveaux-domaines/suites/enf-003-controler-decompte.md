---
id: ENF-003
titre: "Contrôler le décompte d'un acte d'exécution"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-003 — Contrôler le décompte d'un acte d'exécution

## Objectif et résultat attendu

Une personne compare le décompte d'un acte au titre exécutoire et à ses
paiements, repère les postes non justifiés et obtient une demande de
ventilation.

## Périmètre et fichiers

- `enforcement-legal/skills/statement-check/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/decompte.md` — postes, justificatifs, tarifs à vérifier, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte et décompte ; titre exécutoire et ses condamnations ; paiements avec
preuves ; actes antérieurs.

## Sortie attendue

Tableau : poste, montant recopié, fondement indiqué, justificatif, écart ou
question. Postes non ventilés signalés ; brouillon de demande de ventilation ;
limites. Aucun intérêt ni tarif recalculé sans source lue.

## Travail attendu

Distinguer principal, intérêts, frais et émoluments. Un total global sans
détail est une absence de ventilation, pas une erreur établie. Frais bancaires
liés à la saisie → DOM-004.

## Références métier et sources à rechercher

Titre exécutoire visé ; tarifs réglementés des commissaires de justice
(Code de commerce et arrêtés) ; règles sur la charge des frais d'exécution.

## Critères d'acceptation

- [ ] D01 produit le tableau et la demande de ventilation sans recalcul.
- [ ] D02 rapproche un paiement prouvé non déduit, sans conclure à une faute.

## Vérification

- Cas normal : D01 — Total « principal, intérêts et frais » sans détail.
- Cas limite : D02 — Acompte versé au créancier absent du décompte.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Calcul d'intérêts, contestation devant le juge, envoi.

## Complément issu des frictions des commissaires de justice

Points 4, 9, 23, 25 et 40–42 de la [matrice utilisateur](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

- [ ] D03 — Saisies multiples et versements directs : tableau arrêté à une date précise, distinguant montants réclamés, paiements reçus, fonds seulement bloqués et sommes déjà versées ; ne pas déduire deux fois la même opération.
- [ ] D04 — Principal, intérêts, indemnités, frais, émoluments, débours et honoraires : demander détail, bases et pièces. Séparer facture de la banque (BNK-003) et frais d'exécution ; ne pas déclarer une somme fictive sans examen du fondement.
- [ ] D05 — Actes répétés ou tarif douteux : relever date, libellé et pièce ; remettre ces éléments à ENF-014, qui possède la préparation de la contestation de frais. ENF-003 garde le rapprochement et la ventilation.

Scénarios D03–D05 **attendus, non exécutés** : deux mesures et virement direct ; total mêlant frais de banque et étude ; actes homonymes sur deux dates. Aucun calculateur d'intérêts ou de tarifs n'est ajouté.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-annexes/dom-003-decoupage-execution.md).
