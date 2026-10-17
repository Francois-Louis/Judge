---
id: SUC-007
titre: "Lire une créance réclamée au titre d’une succession"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-007 — Lire une créance réclamée au titre d’une succession

## Objectif et périmètre

« Un créancier me demande de payer la dette du défunt. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Demande et décompte, contrat/titre allégué, identité du débiteur, qualité du demandeur, décès, option prouvée ou inconnue, engagement personnel éventuel, paiements, réception et pièces justificatives.

## Sortie attendue

Une fiche créance/débiteur/qualité/option/justification manquante et un brouillon de demande de pièces, sans reconnaissance de dette ni conclusion sur la personne tenue.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/creance-reclamee/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code civil sur dettes et effets de l’option ; distinguer dette du défunt, dette de succession et engagement propre du signataire. Créer `references/creance-successorale.md` ; vérifier le régime sectoriel de la dette si nécessaire.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Ni paiement ni refus définitif conseillés. Acte d’exécution → DOM-003 en priorité ; facture funéraire → FUN-004 ; récupération de prestation → DOM-012/036 ; option → SUC-003.
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

- C13 : facture et relance adressées à un enfant sans preuve de qualité → justificatifs et option demandés, dette personnelle non admise.
- C14 : saisie jointe et engagement de caution allégué → urgence DOM-003 et question bancaire séparée, simple demande de pièces insuffisante.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
