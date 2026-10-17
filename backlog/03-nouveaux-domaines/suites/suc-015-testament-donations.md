---
id: SUC-015
titre: "Documenter un testament ou des donations omis du dossier"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-015 — Documenter un testament ou des donations omis du dossier

## Objectif et périmètre

« On me dit qu’un testament ou une donation n’a pas été communiqué. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Copie et provenance de l’acte, original localisé ou inconnu, dates, auteur, bénéficiaires déclarés, liens familiaux, donation antérieure, dossier notarial et échanges ; recherche déjà faite dans les fichiers compétents.

## Sortie attendue

Un inventaire des libéralités et informations manquantes, divergences avec le dossier et questions au notaire sur authenticité, portée civile et recherches nécessaires.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/testament-donations/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur testament, donations, rapport et réduction, preuve et recherche officielle des dispositions de dernières volontés. Créer `references/testament-donations-connus.md` ; ne pas confondre inscription d’un acte et lecture de son contenu.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune authenticité, nullité, recel, réserve ou quotité calculés. Projet de donation → SUC-024 ; fiscalité → DOM-011 ; infraction alléguée → DOM-002 ; élément étranger → SUC-025.
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

- C29 : acte de donation communiqué après premier inventaire → provenance et différences relevées sans accusation.
- C30 : photographie d’un testament non daté, original inconnu → original et contexte demandés, validité et bénéficiaires réservés.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
