---
id: SUC-022
titre: "Préparer les pièces sur les droits au logement du survivant"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-022 — Préparer les pièces sur les droits au logement du survivant

## Objectif et périmètre

« On me demande de quitter le logement depuis le décès de mon conjoint. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Statut du couple, décès, occupation effective, titre/bail, propriétaires et droits, testament, actes reçus/signés, volonté exprimée et preuve de réception, départ demandé et date.

## Sortie attendue

Une fiche statut/titre/occupation/droit invoqué/manifestation de volonté/preuve/question au notaire, distinguant protection temporaire, droit viager éventuel et transfert de bail.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/logement-survivant/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur logement du survivant et manifestation de volonté, formes, exclusions et délais propres ; vérifier statut réel et textes territoriaux. Créer `references/logement-survivant.md` ; ne pas déduire qualité d’héritier du seul PACS.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucun droit d’occupation ou expulsion conclu sans titre et régime vérifiés. Transfert de bail → DOM-006 ; statut/régime du couple → DOM-013 ; mesure de départ/exécution → DOM-003 ; litige urgent : avocat.
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

- C43 : conjoint menacé d’un départ immédiat, acte incomplet → alerte et pièces du logement en priorité.
- C44 : partenaire pacsé sans testament connu et droit viager invoqué → statut, vocation et logement examinés séparément sans assimilation au mariage.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
