---
id: CRIM-005
titre: "Préparer la contestation d'une amende"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-003]
---

# CRIM-005 — Préparer la contestation d'une amende

## Objectif et résultat attendu

Une personne qui veut contester une amende obtient le brouillon de la
démarche adaptée au stade identifié par CRIM-003, avec les pièces à joindre
et les conditions à vérifier.

## Périmètre et fichiers

- `criminal-legal/skills/fine-contest/SKILL.md` — le skill (à créer)
- `criminal-legal/references/contestation-amende.md` — démarches par stade, modèles, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`amendes.md` (CRIM-003) est relu, pas réécrit.

## Pièces et informations nécessaires

Fiche CRIM-003 ou avis complet ; motif de contestation ; preuves (vente du
véhicule, vol, conducteur différent, paiement) ; consignation éventuelle
demandée par l'avis.

## Sortie attendue

Démarche identifiée et conditions à vérifier ; brouillon ; pièces ; mode
d'envoi indiqué par le document ; limites. La désignation d'un autre
conducteur n'est proposée que sur faits déclarés exacts.

## Travail attendu

Ne pas proposer de désignation fictive ni de motif non étayé. Si le stade est
incertain, retour à CRIM-003. Un jugement de police ou une ordonnance pénale
relèvent de CRIM-006.

## Références métier et sources à rechercher

Code de procédure pénale, requête en exonération et réclamation (pistes 529-2,
530) ; Code de la route (piste L121-3) ; ANTAI comme service d'information.

## Critères d'acceptation

- [ ] K01 produit le brouillon adapté au stade, avec conditions à vérifier.
- [ ] K02 refuse la désignation d'un conducteur non réel et l'explique.

## Vérification

- Cas normal : K01 — Véhicule vendu avant l'infraction, certificat de cession disponible.
- Cas limite : K02 — « C'est moi qui conduisais, mais je veux désigner un ami pour garder mes points. »

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Procédure devant le tribunal de police, paiement, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 59–68 et 79 de la [matrice](../dom-002-frictions-utilisateurs.md). Recueillir motif exact, mode de constatation, photographie demandée ou reçue, écrit et témoin possibles, justificatifs de cession et enregistrement, adresse et notifications, justificatifs de paiement ou consignation.

- [ ] K03 — PV contesté : rechercher la règle de preuve propre au régime (piste CPP 537), les mentions et les éléments contraires ; ni croire le PV irréfragable ni promettre qu'une déclaration suffit.
- [ ] K04 — Photo radar demandée : suivre séparément la demande et le recours ; aucun effet suspensif présumé. Responsabilité du titulaire, conducteur réel et éventuelle obligation de désignation sont vérifiées séparément.
- [ ] K05 — Véhicule cédé, avis sans interception, stationnement ou avis initial non reçu : demander les pièces adaptées et le régime exact, sans annulation automatique. Signalisation, emplacement, horaires et arrêté sont rapprochés pour le stationnement interdit ; FPS → DOM-010.
- [ ] K06 — Paiement déjà fait, consignation ou remise gracieuse : reprendre CRIM-003 et vérifier la recevabilité avant le brouillon ; conserver la distinction contestation de l'infraction/remise financière.

Scénarios **attendus, non exécutés** : conducteur différent sans désignation inventée ; cession non enregistrée ; PV et témoignage contradictoires ; cliché toujours attendu ; stationnement interdit confondu avec FPS. Aucun délai générique ni recours envoyé.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
