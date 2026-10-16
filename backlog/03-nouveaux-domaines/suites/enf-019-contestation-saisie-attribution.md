---
id: ENF-019
titre: "Préparer un dossier de contestation d'une saisie-attribution bancaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001, ENF-004]
---

# ENF-019 — Préparer un dossier de contestation d'une saisie-attribution bancaire

## Objectif et résultat attendu

Une personne saisie sur son compte rassemble un dossier exploitable par le professionnel chargé d'une contestation judiciaire et comprend les formalités à vérifier sans attendre une réponse amiable.

## Périmètre et fichiers

- `enforcement-legal/skills/bank-seizure-dispute-preparation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/contestation-saisie-attribution.md` — qualification, pièces, modèle de sortie et sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

Le paquet et `qualification-acte.md` sont créés par ENF-001. Chaque référence consommée est embarquée dans le paquet ; aucun plugin voisin n'est requis. Appliquer le contrat commun du [découpage](../dom-003-annexes/dom-003-decoupage-execution.md).

## Pièces et informations nécessaires

Procès-verbal de saisie et dénonciation complets ; titre et sa signification ; dates, modes de remise et découverte ; banque, débiteur et cotitulaires ; décompte, paiements, mouvements, origine des fonds ; renonciation ou accord éventuels ; démarches et audience déjà prévues.

## Sortie attendue

Bloc d'urgence ; frise des dates avec niveau de preuve ; griefs factuels et pièces ; délai et point de départ vérifiés ou réservés ; checklist juridiction, représentation, assignation, informations du commissaire et de la banque, preuve d'envoi et remise au greffe ; synthèse à remettre au professionnel, sans acte prêt à signifier.

## Travail attendu

Borner à une saisie-attribution civile sur compte. Vérifier recevabilité, modes et délais de dénonciation et contestation, destinataires, placement au greffe et effets exacts du recours. Distinguer fonds bloqués, attribution et versement ; examiner droits du cotitulaire, paiement antérieur, renonciation ou consentement au versement anticipé. Ne pas annoncer que toute contestation suspend indistinctement tous les effets de la saisie. Injonction de payer découverte : ENF-012, recours distinct à examiner. SATD : régime propre et orientation, pas de transposition. ENF-004 conserve la lecture et la demande de disponibilité des sommes protégées.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, saisie-attribution, dénonciation et contestations (pistes R211-3, R211-11 et suivants) ; compétence du JEX, représentation et saisine ; règles de computation et prorogation applicables ; textes concernant cotitulaires, fonds protégés et paiement anticipé. Sources lues à la date des faits, sans recopier le calendrier fourni comme règle.

## Critères d'acceptation

- [ ] Le cas normal produit la sortie utile avec chaque fait attribué à sa pièce ou marqué comme déclaré.
- [ ] Le cas limite explicite les manques et distingue les procédures sans promettre d'issue favorable.
- [ ] Aucune règle, somme, compétence ou échéance n'est affirmée sans source lue et faits nécessaires ; un point réservé garde une action utile.
- [ ] Le résultat est compréhensible sans formation juridique ; le paquet installé seul contient les références et la méthode BASE-005 nécessaires.

## Vérification

- Cas normal : J01 — Dénonciation reçue, dette dite payée et virement prouvé : dossier de pièces, point de départ et checklist des formalités sans attendre la réponse du cabinet.
- Cas limite : J02 — Compte joint, dénonciation découverte tard et formulaire de versement signé : conserver dates distinctes et effets à vérifier, sans recevabilité ni suspension promises.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Assignation prête à signifier, dépôt ou placement, représentation, mainlevée réalisée, contestation de SATD, calculateur général de délais, envoi.

## État de la proposition — 16 octobre 2026

Issue des points 20, 22 et 24 de la [matrice des frictions](../dom-003-annexes/dom-003-frictions-utilisateurs.md). Exigence de backlog, sans sélection ni implémentation.
