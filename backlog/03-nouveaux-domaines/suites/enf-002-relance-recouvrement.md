---
id: ENF-002
titre: "Répondre à une relance de recouvrement amiable"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-002 — Répondre à une relance de recouvrement amiable

## Objectif et résultat attendu

Une personne relancée par une société de recouvrement, ou par un commissaire
de justice en phase amiable, comprend ce que la lettre peut et ne peut pas
produire, et obtient un brouillon de demande de justificatifs.

## Périmètre et fichiers

- `enforcement-legal/skills/collection-letter-response/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/recouvrement-amiable.md` — mentions, frais, justificatifs, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

`recouvrement-amiable.md` est relu par ENF-008, qui ne le réécrit pas.

## Pièces et informations nécessaires

Lettre complète ; créancier d'origine et éventuel cessionnaire ; contrat,
factures, date de la dette ; frais réclamés ; paiements faits ; échanges.

## Sortie attendue

Nature de la lettre ; ce qui manque pour établir la dette ; frais réclamés et
question de leur charge, selon la source lue ; questions de prescription à
vérifier, sans calcul ; brouillon de demande de justificatifs ou de
contestation motivée par les pièces ; limites.

## Travail attendu

Ne pas trancher l'existence de la dette : le domaine du fond l'examine
(télécoms, énergie, consommation, logement, banque). Une menace de saisie sans
titre mentionné est notée comme affirmation à vérifier. Pressions ou menaces
alléguées : récit factuel et question à DOM-002.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, frais de recouvrement (piste L111-8)
et recouvrement amiable pour autrui (pistes R124-1 et suivants) ; règles de
prescription selon la nature de la créance.

## Critères d'acceptation

- [ ] R01 qualifie la lettre d'amiable et prépare la demande de justificatifs.
- [ ] R02 garde le même raisonnement quand l'auteur est un commissaire de justice.
- [ ] Aucun délai de prescription calculé sans source et date établie.

## Vérification

- Cas normal : R01 — Société de recouvrement pour un ancien abonnement télécom, frais de dossier ajoutés.
- Cas limite : R02 — Lettre « phase amiable » sur papier d'un commissaire de justice.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Examen de la dette au fond, plainte, envoi, paiement.

## Complément issu des frictions des commissaires de justice

Points 1, 3–5, 8–10 et 45–46 de la [matrice utilisateur](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

- [ ] R05 — Décompte avec indemnité, frais de dossier et intérêts : demander principal, bases, taux, périodes, clause, texte ou décision ; ne pas présumer que la seule présence du professionnel justifie les frais.
- [ ] R06 — Dette cédée ou déjà payée : identifier créancier d'origine et actuel, qualité du demandeur, pièces de cession ou de mandat pertinentes ; demander historique des règlements et imputation, avec justificatifs.
- [ ] R07 — Dette ancienne et versement proposé : réunir exigibilité, titre éventuel, reconnaissances, paiements et actes invoqués ; distinguer prescription, forclusion et durée d'exécution du titre. Le calcul reste hors périmètre et le fond garde son domaine.
- [ ] R08 — Pressions par appels ou visites : conserver messages, dates et propos exacts ; privilégier le brouillon écrit et orienter selon les faits vers ENF-015, un signalement à vérifier ou DOM-002, sans qualification automatique.
- [ ] R09 — Le brouillon demande identité, origine, exigibilité, décompte et nature de l'intervention ; il ne prétend pas remplacer un recours judiciaire. Une formule « sans reconnaissance » ne garantit pas l'absence de tout effet d'un engagement ou paiement.

Scénarios R05–R09 **attendus, non exécutés** : indemnité sans base fournie ; paiement absent d'une créance cédée ; dette ancienne et versement symbolique proposé ; appels documentés ; demande de justificatifs alors qu'une signification distincte vient d'être reçue. Sources supplémentaires à rechercher : champ des règles du recouvrement pour autrui selon le professionnel, charge des frais et exceptions, cession, reconnaissance, prescription et forclusion selon la dette. Invitation simplifiée : ENF-017 ; échéancier : ENF-008.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-annexes/dom-003-decoupage-execution.md).
