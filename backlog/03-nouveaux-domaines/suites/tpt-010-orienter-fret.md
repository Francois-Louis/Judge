---
id: TPT-010
titre: "Qualifier un incident de transport de marchandises avant orientation"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-010 — Qualifier un incident de transport de marchandises avant orientation

## Objectif et résultat attendu

Un expéditeur ou destinataire professionnel identifie contrat, acteurs, mode et pièces. La sortie oriente la recherche sectorielle sans trancher la responsabilité ni rédiger de demande indemnitaire.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/freight-incident-orientation/SKILL.md` — le skill (à créer)
- `transport-legal/references/orienter-fret.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Qualité et activité des parties ; vente séparée du transport ; ordre et lettre de transport ; modes, ruptures de charge, pays et dates ; transporteur, commissionnaire et sous-traitants ; marchandise, garde, livraison, réserves ; assurance et acte douanier utiles.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Carte des contrats et acteurs ; chronologie de garde et réserves déclarées ; inventaire ; questions de régime et d’urgence ; orientation transport, commercial, douanes ou assurance selon l’objet.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Qualification du fret professionnel seulement. Aucun régime passager ni protection consommateur présumé. Distinguer vente, transport, commission, assurance et douane ; multimodal ne vaut pas régime unique. Échéance alléguée signalée sans calcul non sourcé.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Code des transports et contrats-types pertinents ; conventions selon mode et trajet (CMR, Montréal/Varsovie, COTIF/CIM et textes maritimes à identifier) ; contrats commerciaux. Vérifier les sources avant toute qualification juridique définitive.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Vente, transport, commission, assurance et acte douanier apparaissent séparément.
- [ ] La sortie reste une orientation factuelle, sans responsabilité, plafond ni demande indemnitaire au fond.
- [ ] Le fret ne reçoit aucun régime passager ; le colis personnel n’est pas qualifié professionnel sans faits.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Palette abîmée en transport routier international : carte vente/transport/assurance, sans barème passager.
- Cas limite : Colis personnel importé avec avis de droits : DOM-009 et vente DOM-001, sans fret professionnel automatique.
- Cas limite : Mer-route avec intervenant contractuel inconnu : demander ordre et documents, régime et responsabilité réservés.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Responsabilité, plafonds, réserves juridiquement suffisantes et prescription au fond ; postal (DOM-022), livraison d’un achat de consommation (DOM-001), formalités douanières (DOM-009).

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).

## Complément des frictions transports — 16 octobre 2026

Points 126 si marchandise professionnelle de la [matrice transports](../dom-008-annexes/dom-008-frictions-utilisateurs.md).

Maintenir la qualification passager/fret ; aucune règle des 128 frictions de voyageurs ne devient une garantie professionnelle.

- [ ] Le résultat conserve ces distinctions et les pièces correspondantes ; chiffres et délais du texte vérifiés sur sources à l’implémentation.

Scénario **attendu, non exécuté** : Un professionnel voyage pour son travail avec un colis : qualifier transport personnel et contrat éventuel de marchandise sans assimiler déplacement professionnel et fret.
