---
id: SUC-018
titre: "Préparer les questions sur l’occupation d’un bien indivis successoral"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-018 — Préparer les questions sur l’occupation d’un bien indivis successoral

## Objectif et périmètre

« Un héritier habite seul la maison et les autres veulent y accéder. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Titre et droits, convention, accord ou décision d’occupation, dates, usage exclusif allégué, clés/accès, échanges, dépenses et éventuelle demande de départ.

## Sortie attendue

Une fiche occupation/accord/preuve/désaccord et questions au notaire ou à l’avocat sur usage, accès et éventuelle indemnité, sans en fixer le principe ni le montant.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/occupation-indivise/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur usage des biens indivis et décisions applicables, convention et décisions judiciaires exactes. Créer `references/occupation-indivise.md` ; distinguer occupation successorale et droits propres du survivant.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune expulsion, changement de serrure ou entrée forcée conseillés. Conjoint/logement → SUC-022 ; bail → DOM-006 ; comptes → SUC-017 ; vente → SUC-019.
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

- C35 : héritier occupant, accord oral allégué → preuves et objet de l’usage clarifiés sans indemnité acquise.
- C36 : conjoint sommé de partir immédiatement → priorité SUC-022 et avocat, absence de titre fourni ne vaut pas absence de droit.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
