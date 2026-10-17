---
id: SUC-013
titre: "Lire une demande de preuve d’héritier dans une petite succession"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-013 — Lire une demande de preuve d’héritier dans une petite succession

## Objectif et périmètre

« La banque exige un acte notarié pour un petit solde. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Demande intégrale, décès, état civil utile et héritiers déclarés, biens dont immobilier, testament et régime du couple connus, solde/actifs, contestations, opération demandée et date.

## Sortie attendue

Un tableau pièce exigée/finalité/conditions à vérifier/alternative à documenter et questions au notaire ou à la banque ; preuve de qualité, option et autorisation d’opérer restent distinctes.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/preuve-qualite/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur preuve de qualité, Code monétaire et financier sur opérations simplifiées, textes et seuils datés, notices officielles. Créer `references/preuve-qualite-hereditaire.md` ; ne pas réduire toutes les conditions à un solde.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune attestation de qualité créée comme certifiée ni déblocage promis ; honoraires → DOM-041. SUC-011 garde le paiement d’obsèques et SUC-003 l’option ; seuils propres à chaque mécanisme.
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

- C25 : petit solde sans immobilier déclaré → finalité et conditions de la pièce demandées avant alternative.
- C26 : même solde mais testament ou héritier contesté → simplification non acquise, vérification notariale.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
