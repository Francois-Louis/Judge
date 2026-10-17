---
id: SUC-001
titre: "Décrypter un courrier de règlement de succession"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-016, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013]
---

# SUC-001 — Décrypter un courrier de règlement de succession

## Objectif et périmètre

« Le notaire me demande des papiers et une signature que je ne comprends pas. »
Une tâche proposée de `inheritance-legal`, un seul résultat préparatoire.
Le [contrat commun DOM-016](../dom-016-annexes/dom-016-decoupage-successions.md)
fixe qualification, autonomie, recherche, frontières et format des sorties.

## Entrées et pièces

Courrier intégral, annexes et projet à signer, date et preuve de réception, décès, lien familial déclaré, actes déjà accomplis, échéance annoncée et objectif. Sans pièce, conserver le récit comme déclaré.

## Sortie attendue

Une fiche demande/pièce disponible/pièce manquante/question au notaire ; les décisions et signatures mentionnées sont séparées de la simple remise de documents. Dates et sommes sont recopiées avec leur provenance. Terminer par un brouillon de questions, sans engagement.
Faits documentés, déclarations et inconnues restent visibles, avec une
prochaine étape compréhensible et un interlocuteur nommé.

## Travail et fichiers futurs

Créer `skills/courrier-notaire/SKILL.md`, un modèle local de la sortie et les références
métier décrites ci-dessous. Créer avec ce premier skill le paquet réel proposé `judge-fr-eu-inheritance-legal` : manifeste et entrée marketplace cohérents, version initiale, README, profil facultatif, LICENSE/NOTICE et copies BASE-005/008 du contrat. Mettre à jour les contrôles d’inventaire et de versions. Aucun paquet vide.

Lire le vocabulaire et la fonction affichée de chaque acte. Rechercher Code civil sur preuve de la qualité, option et partage, et procédure pertinente au document exact. Créer `references/lecture-courrier-succession.md` et un modèle local de fiche. Ne pas qualifier une signature par son seul intitulé.
Les sources primaires et versions applicables restent à lire à l’implémentation ;
les guides du cadrage ne les valident pas. Charger les références locales et
la méthode embarquée BASE-005 ; tracer les lectures selon BASE-014.

## Limites et frontières

Aucune recommandation de signer, option choisie, dévolution ou partage calculés. Option → SUC-003 ; passif → SUC-002 ; honoraires et mission du notaire → DOM-041 ; déclaration fiscale → DOM-011.
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

- C01 : courrier demandant état civil et signature, annexe fournie → demandes expliquées et questions ciblées, distinction qualité/option/partage.
- C02 : seule photo tronquée, signature demandée le lendemain → alerte en tête, acte complet demandé et notaire nommé, sans signature validée.

## État et hors périmètre

Proposition issue de DOM-016, sans skill créé ni scénario exécuté en client.
Information et préparation seulement ; aucun acte, option, déclaration,
paiement, signature ou envoi effectués. Les recettes futures ne conditionnent
pas la clôture du seul cadrage. [Portée](../dom-016-annexes/dom-016-verification.md#portée).
