---
id: CONSO-010
titre: "Réclamer pour un contenu ou service numérique non fourni ou défectueux"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-002]
---

# CONSO-010 — Réclamer pour un contenu ou service numérique non fourni ou défectueux

## Objectif et résultat attendu

Une personne qui a payé un contenu ou un service numérique (jeu, logiciel,
application, film) qu'elle ne peut pas utiliser obtient la fiche de son
achat, les pièces utiles et un brouillon de réclamation au fournisseur.

## Périmètre et fichiers

- `consumer-legal/skills/digital-content-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/contenus-numeriques.md` — régime et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

`garanties-legales.md` (CONSO-002) est relu, pas réécrit.

## Pièces et informations nécessaires

Preuve d'achat ; fournisseur et plateforme ; ce qui ne fonctionne pas et
depuis quand ; mises à jour ; échanges ; compte concerné.

## Sortie attendue

Fiche, pièces, brouillon de réclamation, limites.

## Travail attendu

Compte suspendu ou décision de modération → DOM-034, en tâche distincte.
Données → privacy. Bien avec éléments numériques → CONSO-002. Accès internet
ou mobile → DOM-022.

## Références métier et sources à rechercher

Code de la consommation, dispositions transposant la directive (UE)
2019/770, version à la date d'achat.

## Critères d'acceptation
- [ ] D01 produit fiche et brouillon sur pièces.
- [ ] D02 sépare la suspension de compte (DOM-034) et la réclamation d'achat.
- [ ] D03 et D04 identifient régime et dates ; une renonciation alléguée à la rétractation ne tranche pas la demande de conformité.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : D01 — Jeu payé qui ne se lance plus après une mise à jour.
- Cas limite : D02 — Compte suspendu avec des achats inaccessibles.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contestation de modération, données personnelles, télécoms, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 54, 76–77, 92 de la [matrice des besoins](../dom-001-annexes/dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Compléter la sortie par chronologie de disponibilité et tableau des fonctionnalités promises, versions et mises à jour, perte constatée et éléments techniques manquants. Distinguer contenu autonome, service continu et bien avec éléments numériques (CONSO-002). Une demande de remboursement ne suppose pas une rétractation ; les conditions de perte de ce droit sont examinées par CONSO-003. Résiliation récurrente chez CONSO-009 ; suppression ou modération de compte chez DOM-034.

- Cas limite : D03 — Logiciel dégradé après mise à jour, fournisseur invoquant une renonciation à la rétractation : distinguer non-conformité, rétractation et preuve technique.
- Cas limite : D04 — Service facturé pendant une indisponibilité sans dates précises : demander historique avant remède ou décompte.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-annexes/dom-001-decoupage-consommation.md).
