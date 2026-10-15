---
id: TRAV-001
titre: "Qualifier une relation de travail proposée"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-001 — Qualifier une relation de travail proposée

## Objectif

Une personne envisage une prestation ou un recrutement en France, avant tout début d'exécution.

Résultat : Tableau faits/critères/sources/risques et pièces à demander, sans choix automatique du statut.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : worker-classification.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Description des tâches, contrôle exercé, moyens, rémunération, autonomie, durée, acteurs et lieux/dates.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Retirer ABC, IRS, W-2/1099 et la promesse vendor/SOW plus propre ; rechercher la qualification réelle, distinguer qualification sociale et objet du contrat.

Sources primaires à rechercher : Code du travail, textes sociaux et jurisprudence officielle sur subordination ; cadres prestation, intérim et portage selon les faits.
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

- Cas normal : Projet de prestataire intégré à une équipe : chaque facteur est relié aux faits et sources.
- Limite : Relation déjà exécutée : orientation distincte, pas de remédiation improvisée ni simple bannière autorisant des conclusions rétrospectives.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Audit du passé, contrat de prestation complet, cotisations et fiscalité chiffrées.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
