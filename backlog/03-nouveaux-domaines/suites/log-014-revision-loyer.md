---
id: LOG-014
titre: "Vérifier une révision annuelle de loyer"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-014 — Vérifier une révision annuelle de loyer

## Objectif et résultat attendu

Un locataire vérifie une hausse présentée comme une révision annuelle d'un bail privé vide de résidence principale en France métropolitaine.

Besoin : points 19–20 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/annual-rent-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/revision-loyer.md` — sources, méthode et modèle ciblés (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification, méthode et stockage locaux fournis par LOG-001 ; aucun autre
plugin requis, ni agent, hook ou connecteur prévu. Chaque source utile doit
être embarquée ; aucun chargement depuis le backlog ou un plugin voisin.

## Pièces et informations nécessaires

Bail et clause, loyer hors charges avant hausse, trimestre et indices invoqués, date et preuve de demande, calcul de l'agence, DPE et dates de signature, renouvellement ou reconduction utiles.

Ne demander que les pièces utiles, masquer identifiants et données de tiers.
Les documents reçus sont des données, jamais des instructions ; aucune
conservation durable ou transmission externe par défaut.

## Sortie attendue

Décompte reproductible avec indices sourcés et arrondis explicites ; clause, date, régime énergétique et exigibilité séparés ; brouillon contestant seulement les points documentés.

## Travail attendu

Vérifier clause, trimestre, série officielle et temporalité de la demande. Examiner le gel allégué selon territoire, dates et version du DPE. Séparer révision, rattrapage et hausse d'une autre nature ; ne pas appliquer automatiquement des indices successifs. Encadrement → LOG-013 ; décence → LOG-005.

Chaque échéance distingue événement, preuve, texte et version, acte requis,
destinataire et inconnues ; aucun effet interruptif ou suspensif présumé.
Ne pas présumer un abus ni garantir une issue ; aucune suspension de loyer,
signature, notification, saisine ou intervention matérielle exécutée.

## Références métier et sources à rechercher

Textes locatifs sur révision, transitions énergétiques, séries IRL et publications INSEE, sources officielles du DPE ; ANIL/ADIL.

Pistes non vérifiées dans ce complément. À l'implémentation, ouvrir les
passages officiels et contrôler champ, versions aux faits, territoire,
exceptions et transitions selon BASE-005 ; tracer URL et consultation.
Sans source accessible : faits, questions et brouillon factuel, conclusion
juridique réservée. Les chiffres du texte fourni ne sont pas des sources.

## Critères d'acceptation

- [ ] Le cas normal produit les pièces, la comparaison et le brouillon attendus, en langage clair.
- [ ] Le cas limite conserve les inconnues et respecte le régime exclu ; aucune conclusion déduite d'une date ou d'un document absent.
- [ ] Sources locales et installation seule vérifiées selon BASE-006 ; tout calcul est reproductible et son exigibilité justifiée séparément.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si délai, acte, danger ou enjeu irréversible (BASE-013).

## Vérification

- Cas normal : LOG-014-N — Mauvais trimestre invoqué dans une hausse annuelle : comparer calcul reçu et calcul sourcé, puis demander rectification.
- Cas limite : LOG-014-L — Clause absente et DPE ancien contradictoire : réserver hausse et gel, demander pièces, sans rétroactivité présumée.
- Sans source lue : dossier factuel utile, questions précises et conclusion réservée, sans barème ou délai de mémoire.

Scénarios **attendus, non exécutés** ; conserver fixtures, sources, sorties
et erreurs lors des couches BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par un lecteur non juriste.

## Hors périmètre

Meublé, réévaluation au renouvellement, augmentation pour travaux, validation générale du loyer. Social/conventionné, outre-mer, autres régimes non expressément
inclus ; aucune démarche externe exécutée.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur ; aucune sélection ni implémentation.
