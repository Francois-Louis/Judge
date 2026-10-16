---
id: TPT-008
titre: "Préparer une réclamation pour un trajet en autocar perturbé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-008 — Préparer une réclamation pour un trajet en autocar perturbé

## Objectif et résultat attendu

Un passager d’autobus ou d’autocar obtient une réclamation après annulation ou retard dans un champ vérifié.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/coach-disruption-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/incident-autocar.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Billet, vendeur et transporteur ; service régulier ou occasionnel ; départ et destination, distance pertinente à établir ; dates, horaires, incident ; solutions, dépenses et échanges.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Qualification du service et du trajet ; demandes distinctes selon le champ ; chronologie ; pièces ; brouillon et limites.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Qualifier service et critères de champ avant tout dispositif. Ne pas déduire la distance pertinente de la seule portion parcourue, ni appliquer une indemnité aérienne. Transport local ou scolaire particulier : régime à qualifier d’abord.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Règlement (UE) n° 181/2011 ; Code des transports, exemptions et textes nationaux ; conditions du service ; Your Europe et autorités compétentes à identifier.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Service régulier/occasionnel, distance pertinente et champ sont établis ou réservés.
- [ ] La distance n’est pas déduite de la seule portion parcourue et aucun barème aérien n’est appliqué.
- [ ] Un VTC, covoiturage ou contrat non qualifié est orienté avant traitement.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Service régulier international annulé : qualifier avant toute demande.
- Cas limite : Trajet local sans distance ni type établi : réserver le régime, aucun seuil inventé.
- Cas limite : VTC annulé : orientation TPT-016 selon la qualité du demandeur, sans régime autocar.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Taxi/VTC, location de véhicule, covoiturage, bagages, dommage corporel, forfait et marchandises.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).

## Complément des frictions transports — 16 octobre 2026

Points 66–72, 75 de la [matrice transports](../dom-008-annexes/dom-008-frictions-utilisateurs.md).

Distinguer longueur prévue du service et distance du passager, départ anticipé, arrêt déplacé/non desservi, correspondances indépendantes et assistance. Indemnité supplémentaire pour absence de choix et plainte : conditions et événement propres à vérifier. Bagages TPT-020.

- [ ] Le résultat conserve ces distinctions et les pièces correspondantes ; chiffres et délais du texte vérifiés sur sources à l’implémentation.

Scénario **attendu, non exécuté** : Service long mais court segment acheté, départ anticipé et nuit à l’arrêt : qualifier champ et preuves avant choix, assistance et éventuelle indemnité.
