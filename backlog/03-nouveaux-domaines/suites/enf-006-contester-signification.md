---
id: ENF-006
titre: "Documenter une remise d'acte contestée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-006 — Documenter une remise d'acte contestée

## Objectif et résultat attendu

Une personne qui conteste la date ou la régularité de la remise d'un acte
réunit les faits et preuves utiles à un avocat, sans conclusion sur la
validité de l'acte.

## Périmètre et fichiers

- `enforcement-legal/skills/service-dispute/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/remise-acte.md` — modes de remise, mentions, preuves, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte et mentions de remise ; avis de passage ; lettre reçue ensuite ; adresse
à la date de l'acte ; preuves d'absence, de déménagement ou d'erreur
d'adresse.

## Sortie attendue

Comparaison mentions de l'acte et faits déclarés ; preuves à réunir ;
questions à un avocat ; urgence si un délai peut courir ; limites.

## Travail attendu

Garder la date portée par l'acte comme mention, et la date de découverte
comme déclaration. Ne pas affirmer qu'un délai n'a pas couru. Recours contre
la décision signifiée → contentieux.

## Références métier et sources à rechercher

Code de procédure civile, modes de signification et mentions (pistes 654 à
659) ; règles sur les effets d'une irrégularité, à lire.

## Critères d'acceptation

- [ ] S01 compare mentions et faits sans conclure à la nullité.
- [ ] S02 signale l'urgence d'un délai possible sans le calculer.

## Vérification

- Cas normal : S01 — Remise « à l'étude » pendant une hospitalisation documentée.
- Cas limite : S02 — Signification d'un jugement découverte trois semaines après la date de l'acte.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Demande en nullité, recours contre la décision, envoi.

## Complément issu des frictions des commissaires de justice

Points 11–12 et 18 de la [matrice utilisateur](../dom-003-frictions-utilisateurs.md).

- [ ] S03 — Ancienne adresse : conserver adresse utilisée, situation réelle à la date, preuves de déménagement, diligences de recherche mentionnées et annexes ; distinguer erreur alléguée et irrégularité établie.
- [ ] S04 — Mentions absentes ou inexactes : comparer acte complet et exigences propres à sa nature selon les textes lus ; documenter le grief allégué sans nullité automatique.
- [ ] S05 — Avis de passage et retrait tardif : garder date de signification, date de découverte et date de retrait séparées ; ne pas affirmer que l'absence de remise à personne empêche tout délai de courir.

Scénarios S03–S05 **attendus, non exécutés** : acte à l'ancien domicile ; mention erronée avec conséquences décrites ; avis retrouvé tardivement. Sources à rechercher : signification, recherches, effets et régime des nullités selon la procédure. Le recours contre la décision reste une démarche distincte.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
