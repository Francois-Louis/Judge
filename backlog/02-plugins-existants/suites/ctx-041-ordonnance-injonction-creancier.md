---
id: CTX-041
titre: "Lire une ordonnance d'injonction de payer côté créancier"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-001]
---

# CTX-041 — Lire une ordonnance d'injonction de payer côté créancier

## Objectif et résultat attendu

Une fiche d’ordonnance d’injonction de payer civile ou commerciale obtenue par un petit créancier, avec montant accordé et formalités de signification à vérifier.

Issue des [125 frictions contentieuses](../exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/ordonnance-injonction-creancier/SKILL.md` ;
- `litigation-legal/references/ordonnance-injonction-creancier.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-001. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Requête et pièces, ordonnance complète, date de décision, montant sollicité/accordé, juridiction, débiteur et identité actuelle, signification ou démarches déjà réalisées.

## Travail attendu

Comparer demandes et dispositif, distinguer accueil total/partiel et rejet, signaler les choix à examiner avant signification et leurs conséquences possibles sur le surplus. Rechercher délai, déclencheur, formalités et transition normative selon date de décision ; ne pas reprendre une durée annoncée en septembre 2026 comme acquise. Ordonnance, titre utilisable et paiement sont distincts. Opposition débiteur → ENF-012 ; exécution avec titre → ENF-010 ; procédure collective → SOC-027.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, injonction de payer, accueil partiel/rejet, signification et effets ; textes modificatifs, dispositions transitoires et compétence civile/commerciale.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Ordonnance accordant une partie du montant : comparaison lisible et question sur le surplus avant signification.
- Cas limite : Décision proche de la transition annoncée ou débiteur en liquidation : recherche versionnée et relais, aucun délai générique ni poursuite automatique.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Requête initiale en injonction à découper séparément, signification exécutée, opposition débiteur, recouvrement forcé. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-frictions-verification.md).
