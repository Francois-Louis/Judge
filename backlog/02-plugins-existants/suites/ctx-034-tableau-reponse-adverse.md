---
id: CTX-034
titre: "Préparer un tableau de réponse aux arguments adverses"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-011]
---

# CTX-034 — Préparer un tableau de réponse aux arguments adverses

## Objectif et résultat attendu

Un tableau argument adverse / réponse factuelle possible / pièce / question juridique ouverte pour un jeu d’écritures civiles identifié.

Issue des [125 frictions contentieuses](../exist-006-annexes/exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/tableau-reponse-adverse/SKILL.md` ;
- `litigation-legal/references/tableau-reponse-adverse.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-011. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Écritures adverses complètes et leurs versions, bordereaux et pièces reçues, demandes propres, chronologie, stade et calendrier de procédure.

## Travail attendu

Identifier chaque demande, fondement nouveau, contradiction et pièce citée absente ; distinguer demande nouvelle, moyen nouveau et simple reformulation à faire qualifier. Conserver le contexte des échanges. Signaler preuve contestée ou rapport privé sans affirmer inadmissibilité ni autorité irréfragable ; question de recevabilité d’un enregistrement réservée à une recherche spécifique. Les pièces manquantes passent par CTX-005 ; le temps de réponse par CTX-035.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, prétentions/moyens, contradictoire et communication des pièces ; droit de la preuve et jurisprudence applicable à la loyauté/proportionnalité selon la pièce.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Écritures volumineuses et rapport privé : demandes, arguments et preuves sont reliés sans omission silencieuse.
- Cas limite : Fil de messages tronqué et enregistrement clandestin : contexte demandé, aucune preuve déclarée recevable par défaut.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Conclusions complètes, qualification autonome de tous moyens sectoriels, stratégie dilatoire. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-annexes/exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-annexes/exist-006-frictions-verification.md).
