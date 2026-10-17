---
id: SUC-025
titre: "Qualifier les pièces d’une succession comportant un élément étranger"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-025 — Qualifier les pièces d’une succession comportant un élément étranger

## Objectif et périmètre

« Mon parent vivait dans un autre pays et détenait un bien en France. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Décès, résidence habituelle et preuves, nationalités, pays des biens et procédures, testament et choix de loi allégué, actes étrangers, langue et traductions disponibles, autorité saisie et notifications.

## Sortie attendue

Une carte pays/faits/pièces/autorité et questions séparées de compétence, loi applicable et circulation d’acte ou certificat, avec inconnues et professionnel transfrontalier identifié.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/element-etranger/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire règlement (UE) 650/2012, champ territorial/personnel/temporel, exclusions, dispositions transitoires, consolidations et rectificatifs ; conventions ou droit international privé si hors champ. Créer `references/qualification-transfrontaliere.md` ; ne pas tirer la loi applicable de la seule adresse du bien.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune loi ou compétence retenue sans analyse sourcée du dossier, aucun certificat établi ni acte étranger reconnu automatiquement ; fiscalité → DOM-011, régime matrimonial → DOM-013. Les autres SUC réservent leurs conclusions françaises dépendantes.
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

- C49 : résidence à l’étranger, immeuble français et testament → rattachements et choix allégué distincts, questions au notaire.
- C50 : décès ancien, acte non traduit ou État hors champ → transitions, convention et traduction à vérifier, aucune application automatique du règlement.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
