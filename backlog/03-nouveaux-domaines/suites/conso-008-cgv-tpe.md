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
- [ ] V03 rapproche clause, parcours fourni et source ; les corrections ne sont ni publiées ni présentées comme conformité globale.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : V01 — Atelier Nacre (fiction EXIST-004) vend des carnets en ligne ; CGV de deux pages.
- Cas limite : V02 — CGV reprises d'un modèle américain : garantie « as is », loi du Delaware.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Rédaction complète de CGV, vente de services, conditions d'une place de
marché, publication.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points clauses et parcours de vente, en miroir des points 17–19, 23, 33, 41–50, 58–75, 136–138 de la [matrice des besoins](../dom-001-annexes/dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

La revue des CGV pour une TPE rapproche clauses et parcours effectivement fourni : suppléments, assurance colis, renvoi au transporteur, réserve de livraison, formulaire imposé, avoir, port et retour, exclusion de garantie et médiateur. Séparer défaut de pièce, écart apparent et règle sourcée. Les interfaces peuvent être des pièces de vérification, sans étendre la tâche à l’audit global de publicité (PDT). La demande individuelle d’un acheteur garde son propriétaire CONSO, et les conditions de la plateforme restent hors périmètre.

- Cas limite : V03 — CGV prévoyant avoir systématique, retour exclusivement par formulaire et garantie constructeur seule : tableau des clauses et informations manquantes, sans avis global.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-annexes/dom-001-decoupage-consommation.md).
