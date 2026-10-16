---
id: ENF-012
titre: "Préparer l'opposition à une ordonnance d'injonction de payer"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-012 — Préparer l'opposition à une ordonnance d'injonction de payer

## Objectif et résultat attendu

Un particulier à qui une ordonnance d'injonction de payer est signifiée
comprend ce qu'elle produit, ce qui est urgent, et obtient un brouillon
d'opposition motivé par ses pièces, avec les conditions de forme à vérifier.
Ajout du 16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `enforcement-legal/skills/payment-order-opposition/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/injonction-de-payer.md` — étapes, forme de l'opposition, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

`qualification-acte.md` (ENF-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Ordonnance et acte de signification complets ; mode et date de remise ;
juridiction ; créance réclamée et ses justificatifs ; contestations de la
personne ; paiements déjà faits.

## Sortie attendue

Bloc d'urgence (un délai peut courir depuis la signification, à vérifier dans
le texte) ; fiche de l'ordonnance ; motifs de contestation fondés sur les
pièces ; brouillon d'opposition ; juridiction, forme et représentation à
vérifier ; limites. Aucun délai calculé sans texte lu et date établie.

## Travail attendu

Le fond de la dette reste examiné avec son domaine (consommation, télécoms,
banque, logement). Ordonnance déjà revêtue de la formule exécutoire ou saisie
engagée : relire ENF-001 et ENF-004. Ne pas conseiller une opposition sans
motif pour gagner du temps.

## Références métier et sources à rechercher

Code de procédure civile, injonction de payer et opposition (pistes 1405 et
suivants, 1412 et suivants) ; règles de représentation selon le montant et
la juridiction.

## Critères d'acceptation

- [ ] O01 signale l'urgence sans délai calculé et prépare un brouillon motivé.
- [ ] O02 renvoie la saisie déjà engagée vers ENF-001/ENF-004.

## Vérification

- Cas normal : O01 — Ordonnance signifiée à personne pour un crédit renouvelable que la personne dit avoir soldé.
- Cas limite : O02 — Ordonnance découverte lors d'une saisie sur compte.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Dépôt de l'opposition, représentation à l'audience, défense au fond, envoi.

## Complément issu des frictions des commissaires de justice

Points 13–14 et 17–18 de la [matrice utilisateur](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

- [ ] O03 — Signification autre qu'à personne et découverte par une saisie : réunir ordonnance, signification, premiers actes ultérieurs et dates prouvées ; faire vérifier le déclencheur propre à l'opposition sans confondre les recours ENF-012 et ENF-019.
- [ ] O04 — Délai de signification de l'ordonnance : relever date de décision et date de signification ; rechercher texte modificatif, entrée en vigueur et dispositions transitoires. La transition annoncée en septembre 2026 par le texte fourni n'est pas présumée exacte ni applicable.
- [ ] O05 — Courriel de contestation à l'étude : expliquer la formalité d'opposition au tribunal compétent selon le texte lu ; ne pas présenter le courriel comme suffisant ou suspensif.

Scénarios O03–O05 **attendus, non exécutés** : ordonnance ancienne découverte à la saisie ; deux décisions de part et d'autre de la transition annoncée ; contestation amiable seule. Sources supplémentaires à rechercher : délai de signification, caractère non avenu éventuel, point de départ de l'opposition, mode de saisine et transition normative. Si dates ou textes manquent, garder le point réservé et l'urgence visible.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-003-annexes/dom-003-decoupage-execution.md).
