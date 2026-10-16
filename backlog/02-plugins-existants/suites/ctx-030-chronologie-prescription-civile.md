---
id: CTX-030
titre: "Reconstituer la prescription d'une action civile déterminée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-011]
---

# CTX-030 — Reconstituer la prescription d'une action civile déterminée

## Objectif et résultat attendu

Une chronologie des événements susceptibles de modifier la prescription d’une action en paiement contractuelle de droit commun, avec calcul conditionnel documenté ou impossibilité motivée. Première tranche bornée hors consommation, travail, bail, dommage corporel et procédures collectives ; les prescriptions spéciales restent au domaine de fond, à découper séparément.

Issue des [125 frictions contentieuses](../exist-006-annexes/exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/chronologie-prescription-civile/SKILL.md` ;
- `litigation-legal/references/chronologie-prescription-civile.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-011. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Action et qualification de fond, parties et qualités, faits datés, connaissance du dommage alléguée, reconnaissances, actes judiciaires, médiation et désistement éventuels, preuves de réception.

## Travail attendu

Distinguer prescription de fond, forclusion et échéance de recours. Pour une seule action, relier chaque événement au texte applicable, au point de départ et aux effets à vérifier. Qualifier suspension et interruption séparément ; négociation, mise en demeure, conciliation, médiation et désistement ne produisent aucun effet présumé. Exposer les hypothèses et dates alternatives sans choisir silencieusement la plus favorable. Régime spécial non étudié : pièce et recherche manquantes, urgence et relais sectoriel.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

Code civil, prescription extinctive et effets de la médiation/demande en justice/désistement ; texte sectoriel de l’action retenue, règles transitoires et jurisprudence de point de départ.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Une créance civile avec accord de médiation et preuve du début : chronologie, sources et effets conditionnels explicites.
- Cas limite : Des pourparlers seuls et un projet de désistement : aucune sauvegarde du délai affirmée ; urgence de vérification par avocat.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Calcul universel de toutes prescriptions, régimes spéciaux de consommation/travail/bail/dommage corporel/procédures collectives, pénal, fiscalité, forclusion spéciale, dépôt interruptif. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-annexes/exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-annexes/exist-006-frictions-verification.md).
