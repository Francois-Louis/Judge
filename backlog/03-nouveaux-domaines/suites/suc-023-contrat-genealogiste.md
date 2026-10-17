---
id: SUC-023
titre: "Lire un contrat de révélation de succession proposé par un généalogiste"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-023 — Lire un contrat de révélation de succession proposé par un généalogiste

## Objectif et périmètre

« Un généalogiste inconnu exige un pourcentage pour révéler une succession. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Contrat et annexes, courrier/facture, identité affichée, mission et mandat allégués, information déjà connue, décès déclaré, honoraires, signature, démarchage et échanges.

## Sortie attendue

Une grille mission/mandat/information/prestation/rémunération/preuve et questions à vérifier par une voie indépendante, avec brouillon de demande d’explication sans admission de dette.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/contrat-genealogiste/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire règles sectorielles du mandat de recherche successorale, Code civil sur contrat et preuve, consommation selon qualité et mode de conclusion. Créer `references/contrat-revelation.md` ; distinguer authenticité de l’interlocuteur et bien-fondé de sa facture.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune mission authentifiée par le courrier seul, dette ou abus présumés. Consentement général → DOM-001 ; infraction alléguée → DOM-002 ; qualité successorale → SUC-013 ; aucun envoi de données ou paiement.
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

- C45 : projet de contrat sans signature et pourcentage annoncé → mission et rémunération expliquées comme mentions, questions ciblées.
- C46 : facture menaçante sans mandat ni contrat → pièces et vérification indépendante demandées, avocat si procédure, aucune dette reconnue.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
