---
id: BNK-018
titre: "Réagir à une réduction de concours ou à un refus de financement professionnel"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-005]
---

# BNK-018 — Réagir à une réduction de concours ou à un refus de financement professionnel

## Objectif et résultat attendu

Un indépendant ou dirigeant confronté à une rupture de trésorerie prépare un dossier de demande à la banque et identifie le canal de médiation du crédit pertinent.

Besoin issu des frictions 91–93, 96, 99 de la [matrice utilisateur](../dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/business-credit-response/SKILL.md` — le skill (à créer)
- `banking-legal/references/financement-professionnel.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Statut de l'activité, convention de concours et durée, lettre de réduction ou rupture et réception, refus de financement, trésorerie et échéances documentées, échanges et garanties.

## Sortie attendue

Fiche du concours et de la décision ; calendrier contractuel ou légal à vérifier ; conséquences documentées ; brouillon à la banque et dossier d'orientation vers la Médiation du crédit. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Distinguer refus initial de financer, réduction et rupture d'un concours existant, durée déterminée ou indéterminée. Vérifier préavis et exceptions selon les textes lus ; ne pas transposer le crédit de consommation ni promettre un financement. Caution → BNK-012 ; difficultés globales de l'activité → qualification séparée, pas automatiquement DOM-024.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, concours aux entreprises et rupture (piste L313-12) ; Banque de France, Médiation du crédit, conditions et exclusions à vérifier. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] La sortie identifie le concours, recherche notification et exceptions puis prépare le dossier de médiation approprié.
- [ ] Le refus initial est distingué de la rupture et aucun préavis n'est appliqué automatiquement.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : PRO01 — Une banque réduit une autorisation de trésorerie avant une échéance fournisseur.
- Cas limite : PRO02 — Refus initial de prêt, sans concours antérieur ; la personne invoque un préavis.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Négociation exécutée, financement garanti, procédure collective, plan de restructuration, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-decoupage-banque.md).
