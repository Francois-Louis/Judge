---
id: IA-023
titre: "Préparer la fiche de traitement d'un incident IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-023 — Préparer la fiche de traitement d'un incident IA

## Objectif et résultat attendu

Une petite organisation obtient une fiche d'incident documentée : faits, chronologie, personnes exposées, responsable de suivi, traces utiles et mesures à décider. Points 15, 18, 38, 45–47 de la [matrice des frictions](../exist-005-annexes/exist-005-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).

- `ai-governance-legal/skills/ai-incident-intake/SKILL.md` : nouveau parcours proposé.
- `ai-governance-legal/references/fiche-incident.md` : référence locale à créer.
- README et seuls blocs de routage concernés de CLAUDE.md ; liens documentaires avec ai-policy, ai-inventory et ai-policy-audit.

Appliquer le [contrat commun IA](../exist-005-annexes/exist-005-decoupage-ia.md), méthode BASE-005 embarquée, isolation BASE-008 et recette BASE-006. Pas de profil, connecteur, registre existant ni exécution d'IA-022 imposés. Lors de l'implémentation : références locales, métadonnées synchronisées si modifiées et NOTICE racine/local.

## Entrées nécessaires

Signalement, dates de survenance/détection/connaissance distinctes, usage/version, sorties/actions, personnes et données concernées, journaux disponibles, contrats, interlocuteurs et mesures déjà prises avec preuves. Accepter le récit d'un salarié sans connaissance du modèle.

## Travail attendu

- Séparer fait confirmé, hypothèse de cause, impact et inconnue ; ne pas faire d'un dysfonctionnement une violation réglementaire établie.
- Préparer une chronologie, une liste minimale de traces (décision, entrées utiles, configuration/version, tickets, journal d'action), leurs détenteurs et conditions d'accès. Demander une préservation ciblée sans annoncer qu'elle a eu lieu ; minimiser les données et justifier les durées.
- Attribuer les prochaines décisions : limiter l'usage, contacter fournisseur, informer le responsable interne, vérifier effets sectoriels ; responsable et état proposé/confirmé pour chaque mesure. Aucune suspension technique exécutée par la fiche.
- Identifier les régimes de notification à instruire séparément : incident IA, violation de données, engagement contractuel ou secteur. Pour chacun : rôle, critère, destinataire, source/version, événement déclencheur prouvé, délai vérifié ou inconnu. Ni délai RGPD transposé à l'IA, ni même destinataire présumé.
- PRV-032 reste le parcours de la victime. La qualification et la réponse à violation côté organisme restent à découper dans privacy ; le présent lot fournit la fiche et réserve cette conclusion plutôt que simuler une notification.

## Sources à rechercher

Règlement IA et actes/compétences officiels, RGPD/LIL et doctrine CNIL selon faits, textes sectoriels et contrats exacts. Vérifier obligations et applicabilité par rôle et incident, en distinguant obligation légale, délai contractuel et cible interne.

## Critères d'acceptation

- [ ] Fiche avec chronologie, preuves, inconnues, pilote et prochaines décisions compréhensible sans expertise technique.
- [ ] Journaux minimaux et détenteurs identifiés ; aucune conservation illimitée ou donnée sensible rediffusée inutilement.
- [ ] Notification seulement éventuelle tant que régime, compétence et faits ne sont pas établis ; calendriers séparés.
- [ ] Paquet autonome sans profil ni connecteur ; absence de journaux donne une demande utile, pas une cause inventée.
- [ ] Aucune mesure ni transmission annoncée réalisée sans preuve ; rappel BASE-013 et urgence en tête si nécessaire.

## Vérification

- Cas normal : F11, agent ayant envoyé un message malgré instruction de préparer un brouillon ; chronologie, traces et mesures attribuées, sans annulation annoncée.
- Cas limite : document sensible collé dans un outil inconnu, date et conservation incertaines ; questions de vérification, minimisation et relais privacy sans délai de notification inventé.
- Changement de modèle suivi d'une décision différente : distinguer succession temporelle et causalité prouvée.

Recette future BASE-006 : sorties, paquet détaché, client et compréhension ; [contrôles de l'intégration](../exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Investigation technique, certification de sécurité, notification à une autorité, exécution d'un arrêt, audit général des incidents ou traitement complet d'une violation de données.

## État de la proposition — 16 octobre 2026

`proposee`, préalable PILOTE-003 satisfait ; aucune implémentation sélectionnée.
