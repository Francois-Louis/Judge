---
id: SUC-009
titre: "Lire un décompte de frais bancaires successoraux"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-009 — Lire un décompte de frais bancaires successoraux

## Objectif et périmètre

« La banque facture la succession sans expliquer le calcul. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Décès, qualité, établissements et produits, avoirs/assiette allégués, tarif daté, date du service ou prélèvement, décompte détaillé, factures et échanges ; texte ou décision invoqués par la personne.

## Sortie attendue

Un tableau avoir/service/frais/assiette/tarif/fondement à vérifier, puis un brouillon de demande de justification ou de restitution conditionnelle si la base est effectivement établie.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/frais-bancaires/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Lire Code monétaire et financier sur frais successoraux, loi, décret, entrée en application et tarif pertinent ; retrouver toute décision constitutionnelle alléguée dans sa publication officielle, motifs, dispositif et effets temporels. Créer `references/frais-bancaires-successoraux.md`.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucun plafond, gratuité ou suppression de droit affirmés sans textes lus et régime applicable établi. Ne pas mélanger frais bancaires, honoraires notariaux DOM-041 et fiscalité DOM-011 ; médiation bancaire distincte BNK-004.
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

- C17 : frais globaux sans assiette ni tarif → ventilation et pièces demandées, aucun remboursement annoncé.
- C18 : héritier invoquant une décision constitutionnelle de juin 2026 → référence exacte et effets à rechercher, aucune décision supposée existante ou applicable.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
