---
id: TRAV-005
titre: "Expliquer un projet de rupture conventionnelle individuelle"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-005 — Expliquer un projet de rupture conventionnelle individuelle

## Objectif

Un salarié privé reçoit un projet de rupture conventionnelle individuelle et souhaite le comprendre.

Résultat : Lecture des engagements, informations manquantes et étapes à vérifier ; comparaison conditionnelle des montants si les bases sont établies.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : termination-review.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Projet, contrat, dates proposées, rémunération/ancienneté, convention applicable, situation protectrice et consentement.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Distinguer rupture conventionnelle et transaction ; aucun severance contre release ni délai OWBPA ; vérifier procédure, consentement, interlocuteurs et versions.

Sources primaires à rechercher : Code du travail, textes conventionnels, formulaires/procédures officiels et jurisprudence utile, sans figer les délais.
Ces pistes sont **non vérifiées pour cette story**. Lire les dispositions,
versions et transitions applicables lors de l'implémentation ; conserver
le relevé des accès et réserves BASE-005. Utiliser les voies officielles
alternatives de BASE-010 si une page web échoue, sans confondre lecture et validation.

Charger la méthode locale versionnée et embarquer les références utiles.
Conserver la frontière de stockage BASE-008 ; nommer les accès externes
nécessaires/optionnels et prévoir la sortie utile si la recherche reste empêchée.

## Critères d'acceptation

- [ ] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous.
- [ ] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie.
- [ ] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement.
- [ ] Sources et données sont traçables ; le paquet isolé ne requiert aucun fichier voisin du dépôt.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche.
- [ ] Le périmètre adapté et le reste non adapté sont explicitement distingués.

## Vérification

- Cas normal : Projet complet : engagements et montant expliqués.
- Limite : Consentement contesté, statut protecteur ou formulaire incomplet : limites et orientation, pas d'homologation prédite.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Transaction après litige, ruptures collectives, démission et envoi/dépôt.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.

## Complément des frictions travail — 16 octobre 2026

**Consentement et calendrier de rupture conventionnelle.** Points 1 et 10.05–07 : examiner pression, entretiens, remise de l’exemplaire signé, dates de signature/rétractation, dépôt, homologation ou refus et preuve de réception. Distinguer rétractation, instruction administrative et contestation avec leurs déclencheurs et unités propres. Cas ajouté : signature sous pression sans copie, date proposée proche : pièces, inconnues et interlocuteur urgent sans homologation ni annulation prédites. Chiffrage d’une indemnité choisie via TRAV-051, transaction distincte TRAV-055, protection spéciale TRAV-046 ; aucun droit au chômage garanti.

Rattachement complet : [matrice des frictions](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md).
Les critères restent non cochés. Pour ces ajouts, appliquer BASE-013 : phrase
finale nommant le professionnel compétent et renfort en tête si urgence ou
procédure ; sources, paquet détaché, client et compréhension à vérifier selon
BASE-005/006. Portée de l’intégration et lectures préliminaires :
[vérification](../pilote-001-annexes/pilote-001-frictions-verification.md).
