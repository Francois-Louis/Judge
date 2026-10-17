---
id: SUC-010
titre: "Préparer une recherche de comptes et avoirs oubliés d’un défunt"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-010 — Préparer une recherche de comptes et avoirs oubliés d’un défunt

## Objectif et périmètre

« Je pense qu’il existait un ancien compte, mais je n’ai pas de preuve de transfert. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Décès, qualité et mandat éventuel, noms/variantes utiles, indices de comptes, banques, produits, coffres, dates de clôture et notifications de transfert ; pas de mots de passe ni pièces d’identité complètes dans la conversation.

## Sortie attendue

Un plan de recherches avec pour chaque indice détenteur possible, voie banque/FICOBA/Ciclade, qualité à établir, pièce et interlocuteur, et limites d’un résultat négatif.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/recherche-comptes/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire sources DGFiP sur FICOBA et voies d’accès selon qualité, Code monétaire et financier et textes de transfert/inactivité, documentation Caisse des Dépôts. Créer `references/recherche-avoirs-defunt.md` ; distinguer liste de comptes, soldes/opérations et fonds transférés.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucun accès, localisation exhaustive ou restitution promis ; aucune recherche nominative exécutée. Assurance-vie et bénéficiaire → INS-011, y compris si piste Ciclade ; compte d’un vivant → BNK-017. Fonds trouvés ne valent pas droits établis.
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

- C19 : ancien livret sans transfert prouvé → pistes banque/FICOBA et Ciclade distinctes, justificatifs identifiés.
- C20 : Ciclade négatif et coffre évoqué → absence d’exhaustivité expliquée, autres indices conservés, aucune absence de patrimoine conclue.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
