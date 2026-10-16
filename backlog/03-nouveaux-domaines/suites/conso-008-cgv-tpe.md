---
id: CONSO-008
titre: "Revoir les CGV de vente en ligne d'une TPE à des particuliers"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-008 — Revoir les CGV de vente en ligne d'une TPE à des particuliers

## Objectif et résultat attendu

Une TPE ou un artisan qui vend des biens en ligne à des particuliers en
France obtient un tableau de ses conditions générales : ce que dit chaque
clause, les questions qu'elle soulève et les sources lues. Pas d'avis de
conformité globale.

## Périmètre et fichiers

- `consumer-legal/skills/b2c-terms-review/SKILL.md` — le skill (à créer)
- `consumer-legal/references/cgv-b2c.md` — thèmes à relire et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

CGV datées ; pages de commande et de livraison ; biens vendus ; pays visés ;
mentions de médiation et de garanties ; modèle d'origine si les CGV sont
reprises d'un autre pays.

## Sortie attendue

Tableau : thème, texte lu, question ou écart, source, proposition de
rédaction prudente, inconnue. Couverture visible (pages lues, absentes).

## Travail attendu

Thèmes : information précontractuelle, livraison, rétractation, garanties,
médiation, clauses potentiellement abusives, langue. Une clause importée
d'un autre droit (« as is », loi étrangère) est relevée comme question, sans
réécriture complète. Données → privacy ; lancement et publicité → PDT.

## Références métier et sources à rechercher

Code de la consommation, information précontractuelle et clauses abusives
(pistes R212-1 et R212-2) ; recommandations de la commission des clauses
abusives comme source non normative.

## Critères d'acceptation

- [ ] V01 produit le tableau avec couverture visible, sans avis global.
- [ ] V02 relève les clauses importées comme questions sourcées.
- [ ] Aucune revue de traitement de données ni de publicité.

## Vérification

- Cas normal : V01 — Atelier Nacre (fiction EXIST-004) vend des carnets en ligne ; CGV de deux pages.
- Cas limite : V02 — CGV reprises d'un modèle américain : garantie « as is », loi du Delaware.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Rédaction complète de CGV, vente de services, conditions d'une place de
marché, publication.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
