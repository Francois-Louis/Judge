---
id: INS-011
titre: "Accompagner un bénéficiaire d'assurance-vie ou de capital décès"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-011 — Accompagner un bénéficiaire d'assurance-vie ou de capital décès

## Objectif et résultat attendu

Une personne qui pense être bénéficiaire d'un contrat après un décès sait
comment le vérifier, quelles pièces fournir et comment relancer l'assureur.

## Périmètre et fichiers

- `insurance-legal/skills/life-insurance-beneficiary/SKILL.md` — le skill (à créer)
- `insurance-legal/references/assurance-vie.md` — recherche, pièces, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Acte de décès ; contrat ou indice d'existence ; clause bénéficiaire connue ;
courriers de l'assureur ; lien avec le défunt.

## Sortie attendue

Démarches de recherche à vérifier ; pièces ; brouillon de demande ou de
relance ; limites. Aucune fiscalité ni délai affirmés sans texte lu.

## Travail attendu

Succession → DOM-016 ; fiscalité → DOM-011 ; rendement ou gestion du
placement → hors domaine. Clause bénéficiaire contestée entre proches :
question à un avocat ou au notaire, sans arbitrage.

## Références métier et sources à rechercher

Code des assurances, assurance sur la vie (pistes L132-1 et suivants) ;
dispositifs officiels de recherche des bénéficiaires.

## Critères d'acceptation

- [ ] V01 décrit la recherche et prépare la demande.
- [ ] V02 ne tranche pas un désaccord sur la clause bénéficiaire.

## Vérification

- Cas normal : V01 — Enfant pensant être bénéficiaire du contrat de son père.
- Cas limite : V02 — Deux proches revendiquant le même capital.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Succession, fiscalité, conseil de placement, envoi.

## Complément issu des frictions bancaires

Point 85 de la [matrice utilisateur](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

- [ ] V03 — Capital non versé malgré les pièces remises : frise connaissance du décès/demande de pièces/réception/paiement ; demande motivée de versement et d'intérêts éventuels selon les sources lues, sans calcul.
- [ ] V04 — Pièce manquante ou discutée : la sortie distingue complétude, réception et qualité du bénéficiaire ; aucun délai de paiement déclenché par une date supposée.

Pièces : demandes successives de l'assureur et preuves de remise, en plus du
contrat et du décès. Sources à rechercher : délais de demande des pièces et de
versement, point de départ, intérêts de retard et dispositif de recherche.
Scénarios V03/V04 **attendus, non exécutés**. Le rachat par le souscripteur
vivant est distinct : INS-012. La succession et les comptes du défunt restent
DOM-016.

## Complément issu des frictions assurance

Point 69 de la [matrice](../dom-005-annexes/dom-005-frictions-utilisateurs.md).

- [ ] V05 — Contrat inconnu : distinguer recherche AGIRA et recherche Ciclade selon détenteur actuel et situation, avec justificatifs et qualité à vérifier ; ne pas présumer que la qualité d'héritier prouve celle de bénéficiaire.
- [ ] V06 — Résultat de recherche : contrat identifié ne signifie pas capital immédiatement dû ; conserver identification, qualité, demande de pièces et réception avant toute échéance.

Scénarios V05/V06 **attendus, non exécutés** : proche sans référence de contrat ; réponse indiquant un transfert de fonds à rechercher. Sources officielles des dispositifs et règles applicables à ouvrir. Souscripteur vivant modifiant une clause → INS-020 ; frais et rendement → orientation seule BNK-011 ; rachat → INS-012.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 97–103 et D06 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FO03 — Distinguer recherche obsèques, recherche assurance-vie et fonds transférés à la Caisse des dépôts ; demandeur, pièces, réception/transmission et délai propres à chaque dispositif vérifiés séparément.
- [ ] FO04 — Distinguer héritier, organisateur, opérateur et bénéficiaire ; conserver clause et contradiction sans arbitrage. Contrat retrouvé, fonds reçus et facture réglée sont trois faits distincts.
- [ ] FO05 — Pour retard, conserver frise complète et demande d’intérêts éventuels sourcés ; fiscalité DOM-011, cotisations/garantie INS-004, prestations FUN-006 et complémentaire/prévoyance INS-009.

Scénarios supplémentaires **attendus, non exécutés** : contrat obsèques supposé présent mais aucun numéro ; capital annoncé à l’opérateur sans preuve de versement ; assurance-vie et fonds Ciclade recherchés simultanément.

Sources à ouvrir lors de l’implémentation : dispositifs officiels AGIRA obsèques et assurance-vie, Ciclade, qualité et délais de pièces/versement avec déclencheur propre ; ne pas réutiliser le délai d’un dispositif pour l’autre.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-annexes/dom-005-decoupage-assurance.md).
