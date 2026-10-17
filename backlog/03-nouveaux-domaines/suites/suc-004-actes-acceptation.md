---
id: SUC-004
titre: "Documenter les actes susceptibles d’affecter l’option successorale"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-004 — Documenter les actes susceptibles d’affecter l’option successorale

## Objectif et périmètre

« J’ai vendu un objet ou payé une facture avant de connaître les dettes. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Chronologie datée, objet et valeur alléguée, qualité de l’auteur, mandat, vente/retrait/paiement/conservation, destinataire, justificatifs, motif déclaré, option et documents déjà signés.

## Sortie attendue

Un tableau acte/preuve/contexte/effet juridique à vérifier, et une liste de questions avant un nouvel acte ; conservation, gestion et disposition restent des qualifications à établir.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/actes-acceptation/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur acceptation expresse ou tacite et actes pouvant être accomplis sans emporter option ; jurisprudence pertinente lue selon BASE-005. Créer `references/actes-et-option.md`.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Ne pas conclure automatiquement qu’un paiement vaut acceptation ni qu’une vente est sans effet. Aucun moyen de contourner une option ; SUC-003 garde la sommation, SUC-008 une dette tardive.
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

- C07 : vente d’un meuble avant découverte du passif → acte et contexte documentés, effet réservé et renfort avant nouvelle disposition.
- C08 : facture présentée comme conservatoire, mandat absent → qualification ouverte, pièces demandées sans assurance d’innocuité.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
