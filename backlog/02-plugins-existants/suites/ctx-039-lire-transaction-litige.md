---
id: CTX-039
titre: "Lire la portée d'une transaction proposée dans un litige civil"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-001]
---

# CTX-039 — Lire la portée d'une transaction proposée dans un litige civil

## Objectif et résultat attendu

Une fiche des engagements, paiements, renonciations et points à clarifier avant signature d’une transaction civile déterminée.

Issue des [125 frictions contentieuses](../exist-006-annexes/exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/lire-transaction-litige/SKILL.md` ;
- `litigation-legal/references/lire-transaction-litige.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-001. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Projet complet et annexes, parties et pouvoirs, litige couvert, demandes et préjudices, calendrier judiciaire, propositions et budget disponibles.

## Travail attendu

Relier chaque renonciation à ses demandes et procédures ; signaler périmètre général ambigu, échéances de paiement et conséquences d’un défaut à examiner. Comparer scénarios uniquement avec montants documentés et incertitudes, sans prédire l’issue. Séparer promesse d’accord, accord signé, désistement et exécution ; aucun délai tenu pour sauvegardé ni confidentialité garantie par une formule.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

Code civil, transaction, objet et portée des renonciations ; CPC, désistement, exécution/homologation selon le cas ; règles professionnelles des échanges.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Accord incluant créance et frais : tableau des engagements et demandes conservées ou possiblement abandonnées.
- Cas limite : Offre reçue la veille d’une échéance et clause de renonciation générale : urgence distincte, réserve sur portée et avis d’avocat avant signature.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Négociation envoyée, signature, désistement, rédaction complète d’accord ou garantie de confidentialité. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-annexes/exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-annexes/exist-006-frictions-verification.md).
