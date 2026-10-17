---
id: SUC-012
titre: "Lire une réponse bancaire sur les comptes après décès"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-012 — Lire une réponse bancaire sur les comptes après décès

## Objectif et périmètre

« Le compte est joint ; puis-je utiliser la carte ou la procuration ? »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Convention et type de compte, cotitulaires, mandat, décès et information de la banque, notifications d’opposition/blocage, moyens de paiement, opérations et dates, qualité du demandeur.

## Sortie attendue

Une fiche du fonctionnement annoncé, des pouvoirs invoqués et des pièces à demander à la banque ; opérations autour du décès listées avec provenance, sans les qualifier de détournement.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/fonctionnement-comptes/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code monétaire et financier, Code civil sur mandat et convention applicable. Créer `references/comptes-apres-deces.md` ; séparer accès, fonctionnement du compte et propriété successorale des fonds.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune instruction d’utiliser carte, identifiants ou procuration du défunt ; aucun retrait effectué. Propriété/inventaire → SUC-002 ; opération de paiement contestée → BNK-001 ; mesure d’exécution → DOM-003.
Sans complément disponible, fournir une orientation sur la seule question
distincte, sans installation, transmission ni démarche externe automatiques.

## Critères d’acceptation

- [ ] Les deux scénarios ci-dessous produisent la sortie bornée à partir du récit ou des pièces, sans qualification juridique exigée de la personne.
- [ ] Chaque donnée déterminante est reliée à sa provenance ; inconnues et conclusions réservées sont explicites, sans abus présumé ni issue favorable promise.
- [ ] Les limites et frontières propres à cette tâche sont observées ; aucun montant, délai, majorité ou effet d’une décision n’est affirmé sans source exacte lue et applicabilité établie.
- [ ] La sortie se termine par la phrase BASE-013 nommant le notaire ou l’avocat compétent ; renfort en tête si échéance, procédure ou signature imminente. Banque, créancier et administration sont interlocuteurs du dossier, sans être présentés comme conseil indépendant.
- [ ] Toute décision citée est ouverte et lue selon BASE-005 section 10 ; accès incomplet tracé et conclusion concernée réservée, en poursuivant les autres travaux utiles.
- [ ] Paquet détaché BASE-006/008, références locales, schémas, versions et lectures BASE-014 contrôlés ; cas normal et limite exécutés en client avec sorties conservées et défauts traités.

## Vérification prévue

- C23 : compte joint et carte au nom du défunt → convention et pouvoirs demandés, propriété des fonds réservée.
- C24 : ancien mandataire présentant une procuration et retraits contestés → dates et actes conservés, pouvoirs non prolongés par présomption.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
