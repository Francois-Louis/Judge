---
id: SUC-003
titre: "Lire une demande d’option ou une sommation successorale"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-003 — Lire une demande d’option ou une sommation successorale

## Objectif et périmètre

« On me dit de choisir immédiatement si j’accepte la succession. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Décès, qualité, document intégral, auteur, émission, notification et preuve de réception, options ou actes déjà déclarés, actif/passif disponible, autres courriers et échéances fiscales annoncées.

## Sortie attendue

Une fiche des options à faire expliquer, du stade établi et des échéances à vérifier séparément ; tableau événement/preuve/règle/point de départ réservé et questions au notaire ou à l’avocat.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/option-sommation/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Rechercher Code civil sur option, sommation, effet du silence, prorogation et transition ; CPC et forme de l’acte. Créer `references/option-sommation.md`. Examiner la régularité alléguée avant tout calcul et ne pas confondre délai général et effet propre d’une sommation.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune option conseillée ou déclaration rédigée pour dépôt. Fiscalité → DOM-011 ; actes possibles d’acceptation → SUC-004 ; formalités protégées → SUC-005 ; titre d’exécution distinct → DOM-003.
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

- C05 : sommation reçue et déclaration fiscale annoncée proche → urgence en tête, deux calendriers et deux questions distinctes.
- C06 : courriel familial disant « vous avez encore des années » sans acte complet → demande des notifications, aucune protection générale déduite.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
