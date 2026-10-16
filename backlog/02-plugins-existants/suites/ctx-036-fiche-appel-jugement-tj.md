---
id: CTX-036
titre: "Préparer la vérification d'un appel de jugement du tribunal judiciaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-028]
---

# CTX-036 — Préparer la vérification d'un appel de jugement du tribunal judiciaire

## Objectif et résultat attendu

Une fiche à remettre à l’avocat pour vérifier l’appel d’un jugement civil au fond du tribunal judiciaire en procédure avec représentation obligatoire.

Issue des [125 frictions contentieuses](../exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/fiche-appel-jugement-tj/SKILL.md` ;
- `litigation-legal/references/fiche-appel-jugement-tj.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-028. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Jugement intégral, notification/signification et annexes, mode et dates prouvées, qualité des parties, domicile, chefs contestés, demandes et conseil constitué.

## Travail attendu

Vérifier d’abord ouverture de l’appel, qualification du jugement et régime de représentation ; absence à l’audience ne suffit pas à choisir appel ou opposition. Pour le régime retenu, documenter déclencheur, calcul, exceptions, chefs à critiquer et formalités à vérifier par l’avocat. Si source ou date incertaine, laisser le terme à déterminer et indiquer l’urgence. Distinguer acte de recours, calendrier ultérieur et exécution provisoire ; suspension ou arrêt à instruire séparément.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, voies de recours, appel avec représentation obligatoire, déclaration et effet dévolutif, délais et notifications ; textes modificatifs et transitions applicables.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Jugement au fond signifié et deux chefs contestés : fiche de délai traçable et questions de déclaration pour l’avocat.
- Cas limite : Jugement par défaut, référé ou décision JEX : régime hors périmètre identifié, orientation sans appliquer le délai civil ordinaire.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Déclaration ou dépôt d’appel, conclusions d’appel, opposition de droit commun, cassation, référé, JEX et procédures collectives. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-frictions-verification.md).
