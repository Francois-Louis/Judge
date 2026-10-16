---
id: CRIM-021
titre: "Préparer un signalement sur le comportement d'un agent"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-021 — Préparer un signalement sur le comportement d'un agent

## Objectif et résultat attendu

Une personne prépare un signalement factuel au bon interlocuteur et distingue ce qu'elle attend d'une démarche disciplinaire, déontologique ou pénale.

Besoin issu des points 21–22, 49–54, 81, 86 ; section 11 de la [matrice des frictions](../dom-002-frictions-utilisateurs.md). Proposition documentaire, sans implémentation ni sélection.

## Périmètre et fichiers

- `criminal-legal/skills/officer-conduct-report/SKILL.md` — le skill (à créer)
- `criminal-legal/references/signalement-agent.md` — repères, modèles et sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit. Un relais vers une autre story est une orientation ; aucun autre plugin installé n'est requis.

## Pièces et informations nécessaires

Corps et unité, connus ou supposés ; faits, date et lieu ; identifiants visibles sans recherche du domicile ou du nom privé ; pièces ; atteintes alléguées ; démarche recherchée ; plainte, procédure et autres signalements existants ; notifications reçues.

## Sortie attendue

Chronologie avec statut des faits ; tableau objectif, autorité compétente à vérifier, pièces, limites et délai propre à rechercher ; brouillon de signalement adapté au corps ; question pénale séparée vers CRIM-004 et avocat. Aucun envoi, poursuite ou sanction promis.

## Travail attendu

Distinguer police nationale et CRS, gendarmerie, police municipale et agents privés ; ne pas envoyer automatiquement tout fait à l'IGPN. Rechercher compétence et canal de l'IGPN, de l'IGGN, du maire et du Défenseur des droits selon le cas. Ne pas assimiler nom civil et identification professionnelle ; documenter l'absence d'identification sans l'ériger en preuve suffisante d'illégalité. Présenter séparément plainte, signalement et recours contre une décision : aucun effet suspensif ou interruptif présumé. Discrimination → DOM-029 en complément ; preuves → CRIM-020 ; indemnisation → CRIM-013 ou DOM-035 selon la voie.

Charger la méthode locale BASE-005. Séparer document lu, fait déclaré, règle vérifiée et inconnue. Aucun droit, aucune durée, aucun délai ni montant établi depuis le seul texte des frictions ; sans source, fournir les questions et pièces utiles.

## Références métier et sources à rechercher

CSI, déontologie et identification selon corps et exceptions ; textes de compétence du Défenseur des droits ; canaux officiels des inspections et de la collectivité ; CPP pour la plainte. Les portails et formulaires seront vérifiés lors de l'implémentation.

## Critères d'acceptation

- [ ] S01 choisit les interlocuteurs selon le corps et sépare plainte et signalement.
- [ ] S02 n'affirme aucune suspension d'une autre procédure.
- [ ] S03 n'assimile pas refus du nom civil et absence d'identification.

## Vérification

- Cas normal : S01 — Humiliations et refus de plainte par un agent municipal.
- Cas limite : S02 — Un signalement IGGN est en cours alors qu'un avis d'amende doit être contesté.
- Cas limite : S03 — Agent identifié par son numéro qui refuse de donner son nom.
- Sans source lue : questions, pièces et limites ; aucune règle suppléée par le texte utilisateur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Enquête sur l'agent, recherche d'identité privée, qualification définitive, plainte pénale rédigée dans ce skill, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur. Contrat commun : [découpage](../dom-002-decoupage-penal.md). Aucun fichier de plugin créé par cette intégration.
