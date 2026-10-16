---
id: BNK-016
titre: "Comprendre un double débit, une préautorisation ou un plafond de carte"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-016 — Comprendre un double débit, une préautorisation ou un plafond de carte

## Objectif et résultat attendu

Un titulaire comprend pourquoi une somme ou sa carte reste indisponible et obtient une demande de justification ou de libération des fonds adaptée aux écritures observées.

Besoin issu des frictions 26–27, 30 de la [matrice utilisateur](../dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/card-hold-review/SKILL.md` — le skill (à créer)
- `banking-legal/references/carte-preautorisation.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Relevé distinguant opérations en attente et comptabilisées, reçus, contrat du commerçant, plafond et période contractuels, dates, paiements différés, échanges avec commerçant et banque.

## Sortie attendue

Tableau écriture/statut/date/référence ; reconstitution descriptive du disponible et des plafonds selon le contrat ; demande de levée ou d'explication, sans délai de libération inventé. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Distinguer empreinte, débit définitif et doublon réel ; identifier qui peut demander la levée. Fraude → BNK-001 ; vente → DOM-001 ; fonds retenus d'un commerçant chez son acquéreur → BNK-019.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, blocage et libération des fonds pour opérations par carte ; convention de carte et règles de réseau applicables, distinguées de la loi. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] Le tableau distingue la préautorisation du débit sans présenter chaque empreinte comme une facturation.
- [ ] La demande cherche les références et la période contractuelle avant de conclure à un doublon ou à une erreur de plafond.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : CAR01 — Une station-service apparaît en attente en plus du débit définitif.
- Cas limite : CAR02 — Deux débits comptabilisés portent des références différentes ; carte à plafond glissant atteinte.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Opposition ou levée exécutée, achat du bien, expertise du terminal, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-decoupage-banque.md).
