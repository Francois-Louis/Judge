---
id: CTX-033
titre: "Préparer des observations sur une expertise civile"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-032]
---

# CTX-033 — Préparer des observations sur une expertise civile

## Objectif et résultat attendu

Un projet local d’observations factuelles sur un prérapport d’expertise judiciaire civile, avec pièces et questions techniques à relire.

Issue des [125 frictions contentieuses](../exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/observations-expertise/SKILL.md` ;
- `litigation-legal/references/observations-expertise.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-032. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Mission, prérapport et annexes, convocations et calendrier, observations antérieures, pièces contradictoires, destinataires et rôle de la personne.

## Travail attendu

Construire point du prérapport / constat contesté / pièce / question à l’expert ; distinguer fait, opinion technique et allégation. Recenser points non traités dans la mission et date de réponse à vérifier. Vérifier modalités de communication contradictoire avec le conseil. Un rapport définitif ou une échéance dépassée appelle une orientation spécifique, sans fabriquer un dire recevable.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, expertise, observations et dires des parties, contradictoire ; mission et instructions effectives de l’expert, jurisprudence sur la discussion du rapport.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Prérapport contredisant une facture datée : observation précise et pièce jointe proposée, sans accusation de partialité.
- Cas limite : Rapport final ou calendrier manquant : statut explicite et question au conseil, sans date ni droit de réponse inventés.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Avis d’expert technique, envoi aux parties, contestation judiciaire complète du rapport. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-frictions-verification.md).
