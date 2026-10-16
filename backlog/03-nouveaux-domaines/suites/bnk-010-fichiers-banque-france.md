---
id: BNK-010
titre: "Lire une inscription à un fichier de la Banque de France"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-007]
---

# BNK-010 — Lire une inscription à un fichier de la Banque de France

## Objectif et résultat attendu

Une personne informée d'une inscription à un fichier d'incidents comprend le
fichier concerné, la cause indiquée et les démarches à vérifier pour la
consulter ou la contester.

## Périmètre et fichiers

- `banking-legal/skills/banque-de-france-file-reading/SKILL.md` — le skill (à créer)
- `banking-legal/references/fichiers-incidents.md` — fichiers, consultation, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Courrier d'information ; incident à l'origine ; régularisation éventuelle ;
établissement déclarant.

## Sortie attendue

Fichier identifié ; cause recopiée ; démarches de consultation et de
contestation à vérifier ; limites. Aucune durée d'inscription affirmée sans
texte lu.

## Travail attendu

Surendettement → DOM-024. Données personnelles au sens large → privacy.

## Références métier et sources à rechercher

Code de la consommation et textes de la Banque de France sur les fichiers
d'incidents.

## Critères d'acceptation

- [ ] I01 identifie le fichier et la démarche sans durée non sourcée.
- [ ] I02 oriente la procédure de surendettement vers DOM-024.

## Vérification

- Cas normal : I01 — Courrier annonçant une inscription après des impayés de crédit.
- Cas limite : I02 — Inscription liée à un dossier de surendettement.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Demande d'effacement envoyée, procédure, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 67–68 et tableau initial du texte sur le chèque impayé : [matrice](../dom-004-frictions-utilisateurs.md).

- [ ] I03 — Projet de FICP : rechercher information préalable, réception, cause et pièces de régularisation ; aucun délai uniforme sans régime identifié.
- [ ] I04 — Inscription maintenue après paiement : préparer demande de mise à jour à l'établissement déclarant, avec preuves de paiement et réponse ; distinguer mise à jour et effacement automatique.
- [ ] I05 — Chèque impayé : distinguer FCC, FICP et interdiction d'émettre des chèques ; vérifier les démarches de régularisation et de consultation propres au fichier.

Scénarios I03–I05 **attendus, non exécutés** : avis préalable, paiement suivi d'un maintien allégué, chèque régularisé sans notification de mise à jour. Sources : textes propres à chaque fichier et procédure du déclarant, à vérifier à la date des faits.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
