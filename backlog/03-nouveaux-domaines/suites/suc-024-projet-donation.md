---
id: SUC-024
titre: "Préparer les questions sur un projet de donation"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-024 — Préparer les questions sur un projet de donation

## Objectif et périmètre

« Je veux donner un bien ou une somme et comprendre le projet avant de signer. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Intention concrète du donateur, projet complet, bénéficiaires, liens familiaux, capacité/représentation, propriété et régime matrimonial, donations antérieures, réserve d’usufruit ou charges prévues, pays et dates.

## Sortie attendue

Une fiche objectif/acte proposé/clauses/effets à expliquer/pièces manquantes et questions au notaire avant engagement, distinguant don actuel et dispositions pour le décès.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/projet-donation/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur donation, capacité, forme, charges et effets civils ; qualifier don manuel, donation simple, donation-partage ou donation entre époux sans transposer leurs règles. Créer `references/lecture-projet-donation.md`.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune stratégie patrimoniale, acte prêt à signer, validité, réserve, rapport ou réduction calculés. Impôts/déclaration → DOM-011 ; couple → DOM-013 ; pouvoirs majeur protégé → DOM-026 ; donation passée omise → SUC-015.
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

- C47 : projet de donation avec usufruit et charges → clauses et questions présentées en langage courant.
- C48 : bien commun, enfant mineur et don déjà effectué à l’étranger → pouvoirs et régimes réservés, tâches séparées avant toute signature.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
