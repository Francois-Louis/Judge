---
id: SUC-002
titre: "Organiser les avoirs et dettes avant une décision successorale"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, SUC-001]
---

# SUC-002 — Organiser les avoirs et dettes avant une décision successorale

## Objectif et périmètre

« Je ne sais pas ce que mon parent possédait ni ce qu’il devait. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Décès, qualité déclarée, statut du couple et régime matrimonial connu, titres, relevés datés, contrats, dettes, garanties, créances à recevoir, donations connues et actes accomplis. Pour chaque poste : détenteur, date, montant déclaré ou documenté, justificatif.

## Sortie attendue

Un inventaire préparatoire actif/passif/créance à recevoir/inconnu, avec provenance, titularité à vérifier, pièces et interlocuteur ; les montants incomplets ne deviennent pas un actif net certain.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/actif-passif/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Étendre le paquet créé par SUC-001 et augmenter sa version ; ne pas charger la lecture de courrier pour une demande qui ne la concerne pas.

Rechercher Code civil sur composition successorale, obligations et droits démembrés ; identifier liquidation préalable du régime du couple. Créer `references/inventaire-preparatoire.md`. Recenser salaires et prestations encore dus sans déterminer ici le droit sectoriel.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Ce tableau ne remplace pas un inventaire formel SUC-005 et ne justifie aucun partage. Couple → DOM-013 ; créance employeur → emploi privé ou DOM-037 ; caisse → DOM-012/036 ; assurance-vie → INS-011 ; choix → SUC-003.
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

- C03 : deux relevés et dette sans décompte → postes sourcés, passif inconnu et questions au créancier.
- C04 : compte joint, assurance-vie et salaire restant dû → titularité et tâches sectorielles séparées, aucun total distribuable.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
