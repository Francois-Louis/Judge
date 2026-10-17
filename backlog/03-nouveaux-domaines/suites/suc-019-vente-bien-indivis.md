---
id: SUC-019
titre: "Lire un projet d’acte portant sur un bien indivis successoral"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-019 — Lire un projet d’acte portant sur un bien indivis successoral

## Objectif et périmètre

« Des héritiers veulent vendre et me disent que ma signature est inutile. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Projet exact, titres, titulaires et droits, démembrement, capacités, accords/mandats, convention, décision judiciaire et notifications ; décès, lieu et dates.

## Sortie attendue

Un tableau acte envisagé/pouvoir allégué/justificatif/accord manquant/voie à vérifier, avec questions avant signature ; nombre de personnes et droits détenus distingués.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/vente-bien-indivis/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur conservation, administration et disposition, procédures de vente, textes spéciaux territoriaux et transitions éventuelles. Créer `references/pouvoirs-bien-indivis.md` ; vérifier la version et la procédure exacte avant toute majorité annoncée.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune vente, majorité universelle, autorisation ou opposition acquise. Compromis et vente immobilière → DOM-017 ; pouvoirs d’un majeur protégé → DOM-026 ; logement survivant → SUC-022.
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

- C37 : vente proposée malgré un désaccord → droits et base de pouvoir demandés, aucune unanimité ou majorité appliquée par défaut.
- C38 : nus-propriétaires, usufruitier et personne protégée, réforme de 2026 invoquée → acte et champ temporel à vérifier, renfort avant signature.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
