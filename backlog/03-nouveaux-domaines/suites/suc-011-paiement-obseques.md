---
id: SUC-011
titre: "Préparer une demande bancaire de règlement d’une facture d’obsèques"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-011 — Préparer une demande bancaire de règlement d’une facture d’obsèques

## Objectif et périmètre

« La banque peut-elle régler cette facture sans que j’avance la somme ? »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Facture/commande, signataire, décès, qualité du demandeur, compte et fonds connus, réponse bancaire, sommes déjà avancées, tarif et date pertinente.

## Sortie attendue

Un dossier de demande à la banque : prestation et montant recopiés, pièces et condition/plafond à vérifier, question sur règlement direct ou remboursement d’avance, sans confusion avec la charge finale.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/paiement-obseques/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code monétaire et financier sur opérations autorisées après décès, texte d’application et montant versionné selon opération. Créer `references/paiement-obseques-banque.md`. Vérifier champ, justificatifs et fonds disponibles avant toute conclusion.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucun paiement exécuté ni droit au déblocage promis. Prix/prestations → FUN-002 ; financement et contribution → FUN-005 ; dette réclamée → SUC-007 ; ne pas réutiliser un seuil de petite succession.
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

- C21 : facture et réponse « compte bloqué » → demande documentée et mécanisme précis à vérifier.
- C22 : avance personnelle déjà faite et solde inconnu → remboursement distinct du règlement direct, aucun droit acquis.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
