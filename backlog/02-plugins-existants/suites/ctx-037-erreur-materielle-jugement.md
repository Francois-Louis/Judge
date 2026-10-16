---
id: CTX-037
titre: "Documenter une erreur matérielle alléguée dans un jugement civil"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-028]
---

# CTX-037 — Documenter une erreur matérielle alléguée dans un jugement civil

## Objectif et résultat attendu

Une fiche comparant la décision civile et les pièces pour une erreur de nom, de transcription ou de calcul alléguée, avec démarche de rectification à vérifier.

Issue des [125 frictions contentieuses](../exist-006-annexes/exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/erreur-materielle-jugement/SKILL.md` ;
- `litigation-legal/references/erreur-materielle-jugement.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-028. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Jugement complet, écritures et pièces originales, erreur précise, notification, exécution et recours en cours.

## Travail attendu

Reproduire passage, pièce contradictoire et correction demandée ; distinguer anomalie matérielle alléguée et désaccord sur le raisonnement ou les droits jugés. Rechercher compétence, forme et procédure de rectification. Maintenir la vérification séparée des voies de recours : aucune suspension déduite d’une demande de correction.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, rectification des erreurs et omissions matérielles et articulation avec les recours ; jurisprudence délimitant erreur matérielle et modification des droits.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Addition manifestement discordante avec les postes du dispositif : comparaison sourcée et question au conseil.
- Cas limite : Personne contestant l’indemnité appréciée par le juge : désaccord de fond, aucune rectification promise.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Requête déposée, révision du jugement, recours contre appréciation du fond ; omission de statuer vers CTX-038. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-annexes/exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-annexes/exist-006-frictions-verification.md).
