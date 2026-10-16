---
id: CTX-040
titre: "Organiser le budget d'un procès civil déterminé"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-001]
---

# CTX-040 — Organiser le budget d'un procès civil déterminé

## Objectif et résultat attendu

Un budget par étape d’un procès civil identifié, séparant avances, coûts certains/estimés, prises en charge annoncées/confirmées et reste à financer.

Issue des [125 frictions contentieuses](../exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/budget-proces-civil/SKILL.md` ;
- `litigation-legal/references/budget-proces-civil.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-001. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Procédure et stade, conventions/devis/factures, provisions et paiements, expertise, assurance et plafonds, dossier d’aide juridictionnelle, recours et exécution envisagés.

## Travail attendu

Séparer honoraires, dépens, frais demandés à l’adversaire et sommes effectivement accordées ou récupérées. Indiquer qui avance chaque dépense et les étapes non couvertes par le forfait. Ne garantir aucun remboursement parce que le procès est gagné. DOM-041 porte honoraires et aide juridictionnelle ; DOM-005 qualifie la protection juridique. Contribution de saisine éventuelle : existence, champ, exceptions, transition et régularisation à rechercher, sans reprendre le montant du texte fourni comme tarif acquis.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, dépens et frais non compris ; textes de contribution de saisine, aide juridictionnelle et protection juridique ; contrats et décisions de prise en charge.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Forfait de première instance, expertise et plafond d’assurance : avances et reste à financer séparés, appel/exécution identifiés.
- Cas limite : Gagnant sans décision sur les frais ou aide seulement envisagée : prise en charge non confirmée, aucun remboursement intégral présumé.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Audit de facturation professionnelle, demande d’aide déposée, garantie d’assurance décidée, estimation des chances de succès. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-frictions-verification.md).
