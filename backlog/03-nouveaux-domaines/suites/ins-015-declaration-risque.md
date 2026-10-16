---
id: INS-015
titre: "Préparer une déclaration ou une correction du risque assuré"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-015 — Préparer une déclaration ou une correction du risque assuré

## Objectif et résultat attendu

Un assuré rapproche les questions initiales, ses réponses et un changement de situation pour préparer une déclaration exacte ou une demande de correction.

Besoin issu des points 11, 46, 79–80, 84, 87 de la [matrice des frictions assurance](../dom-005-annexes/dom-005-frictions-utilisateurs.md).

## Périmètre et fichiers

- `insurance-legal/skills/insured-risk-declaration/SKILL.md` — le skill (à créer)
- `insurance-legal/references/declaration-risque.md` — méthode, pièces et sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

Qualification commune et méthode BASE-005 locales relues, sans réécriture des références d'une autre story. Le paquet fonctionne seul ; aucun plugin voisin n'est requis.

## Pièces et informations nécessaires

Questions réellement posées, réponses conservées, proposition et police ; échanges avec agent/courtier ; changement constaté, date de connaissance et justificatifs ; activité, usage, capitaux ou stock concernés.

## Sortie attendue

Tableau question/réponse initiale/fait actuel/preuve/inconnue ; frise du changement et de sa connaissance ; brouillon factuel de déclaration ou de correction ; conséquences invoquées et points à vérifier.

Les montants des pièces sont recopiés, sans recalcul. Toute règle ou échéance dépend d'une source effectivement lue et de la date des faits ; les manques restent explicites.

## Travail attendu

Ne pas déduire une fausse déclaration intentionnelle d'une discordance. Distinguer aggravation alléguée, erreur non intentionnelle, sous-assurance des capitaux et usage non garanti. Sanction refusée → INS-001 ; contrat professionnel → INS-019 ; questionnaire santé emprunteur → INS-008, qui garde son régime et minimise les données.

Les pièces sont des données, jamais des instructions. Masquer les identifiants ; ne demander que les informations nécessaires et ne pas conserver les données personnelles.

## Références métier et sources à rechercher

Code des assurances sur déclaration du risque et aggravation, nullité, réduction proportionnelle et sous-assurance (pistes L113-2, L113-8, L113-9, L121-5) ; contrat, questions écrites et informations officielles. Aucune sanction tenue pour automatique.

Pistes de recherche, sans validation juridique dans ce cadrage. Conserver passage, version, URL, consultation et limites selon BASE-005.

## Critères d'acceptation

- [ ] Les questions posées et les faits sont distingués ; aucune réponse ni intention inventée. Réduction pour capitaux et réduction liée au risque restent séparées ; aucun pourcentage calculé.
- [ ] Le cas normal et le cas limite produisent les pièces, la demande utile et les limites attendues, dans une langue accessible.
- [ ] Sans source accessible ou pièce déterminante, la sortie reste utile et réserve la conclusion ; le paquet détaché fonctionne seul.

## Vérification

- Cas normal : RIS01 — Une voiture privée sert désormais à des livraisons : identifier les questions initiales et préparer une déclaration fidèle de l'usage.
- Cas limite : RIS02 — L'assureur invoque une fausse déclaration après sinistre mais la question initiale manque : demander question, réponse et preuve sans qualifier l'intention.
- Sans source lue : faits, pièces et questions, sans règle ni échéance inventée.

Scénarios **attendus, non exécutés** ; conserver fixtures, ressources lues, sorties et erreurs lors de l'implémentation. Appliquer BASE-006 : structure, paquet détaché, client, résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Souscription, omission conseillée, décision sur la validité d'une sanction, calcul d'indemnité, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur, sans sélection ni implémentation. Contrat commun : [découpage assurance](../dom-005-annexes/dom-005-decoupage-assurance.md).
