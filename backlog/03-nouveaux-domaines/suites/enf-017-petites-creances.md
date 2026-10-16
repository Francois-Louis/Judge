---
id: ENF-017
titre: "Comprendre une invitation à la procédure simplifiée des petites créances"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-017 — Comprendre une invitation à la procédure simplifiée des petites créances

## Objectif et résultat attendu

Une personne invitée à une procédure simplifiée comprend les étapes et la portée des accords demandés avant de répondre ou de signer.

## Périmètre et fichiers

- `enforcement-legal/skills/small-claim-invitation-reading/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/petites-creances.md` — qualification, pièces, modèle de sortie et sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

Le paquet et `qualification-acte.md` sont créés par ENF-001. Chaque référence consommée est embarquée dans le paquet ; aucun plugin voisin n'est requis. Appliquer le contrat commun du [découpage](../dom-003-decoupage-execution.md).

## Pièces et informations nécessaires

Invitation intégrale et annexes ; date et mode de réception ; montant ventilé, origine de la dette et créancier ; formulaire, liens ou accord proposé ; réponse ou signature éventuelle ; paiements ; titre déjà délivré s'il existe.

## Sortie attendue

Stade du dossier ; distinction relance, participation, accord sur montant et modalités, puis titre éventuel ; conditions d'éligibilité à vérifier ; effets de l'accord, du refus ou du silence selon le texte lu ; questions et brouillon de demande d'explications, sans acceptation implicite.

## Travail attendu

Ne pas confondre cette procédure avec une injonction de payer (ENF-012), un simple échéancier (ENF-008) ou une saisie. Vérifier plafond, créances admissibles, délai de réponse, consentements, délivrance du titre, frais et incompatibilités éventuelles du professionnel chargé ensuite de l'exécution. Ne jamais présenter l'accord comme une formalité neutre ; si un titre est déjà invoqué, recueillir accords et titre pour orientation urgente. Dette au fond : domaine de la créance.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, procédure simplifiée de recouvrement des petites créances (pistes L125-1 et R125-1 et suivants) ; textes sur le consentement, les coûts et la délivrance du titre ; information officielle à la date des faits. Aucun plafond du texte utilisateur n'est tenu pour vérifié.

## Critères d'acceptation

- [ ] Le cas normal produit la sortie utile avec chaque fait attribué à sa pièce ou marqué comme déclaré.
- [ ] Le cas limite explicite les manques et distingue les procédures sans promettre d'issue favorable.
- [ ] Aucune règle, somme, compétence ou échéance n'est affirmée sans source lue et faits nécessaires ; un point réservé garde une action utile.
- [ ] Le résultat est compréhensible sans formation juridique ; le paquet installé seul contient les références et la méthode BASE-005 nécessaires.

## Vérification

- Cas normal : P03 — Invitation accompagnée d'un échéancier et d'un formulaire : restituer séparément les accords demandés et demander justification de la dette.
- Cas limite : P04 — La personne a déjà signé et reçoit une menace de saisie : reconstituer consentements et titre éventuel sans promettre qu'un retrait efface l'accord.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Acceptation ou refus envoyés, signature, paiement, émission de titre, contestation judiciaire rédigée.

## État de la proposition — 16 octobre 2026

Issue des points 7 de la [matrice des frictions](../dom-003-frictions-utilisateurs.md). Exigence de backlog, sans sélection ni implémentation.
