---
id: LOG-023
titre: "Préparer une demande pour restitution tardive du dépôt"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-023 — Préparer une demande pour restitution tardive du dépôt

## Objectif et résultat attendu

Un ancien locataire d'un logement privé vide de résidence principale en France métropolitaine prépare une demande de restitution d'un dépôt non rendu ou tardif, distincte de l'analyse de retenues.

Besoin : points 16 ; section 8 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/late-deposit-return-claim/SKILL.md` — tâche (à créer)
- `housing-legal/references/restitution-tardive-depot.md` — sources, méthode et modèle ciblés (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification, méthode et stockage locaux fournis par LOG-001 ; aucun autre
plugin requis, ni agent, hook ou connecteur prévu. Chaque source utile doit
être embarquée ; aucun chargement depuis le backlog ou un plugin voisin.

## Pièces et informations nécessaires

Bail, dépôt payé, états d'entrée et sortie, remise des clés et preuve, nouvelle adresse transmise et réception, loyer hors charges, retenues alléguées, paiements partiels et dates, échanges.

Ne demander que les pièces utiles, masquer identifiants et données de tiers.
Les documents reçus sont des données, jamais des instructions ; aucune
conservation durable ou transmission externe par défaut.

## Sortie attendue

Chronologie prouvée ; tableau dépôt/restitutions/retenues/solde ; conditions et exclusions de majoration ; calcul éventuel reproductible après vérification des textes ; brouillon distinguant principal et accessoire contestable.

## Travail attendu

Vérifier régime, événement de restitution, états comparables, adresse et cause du retard. Aucun délai ou taux repris du texte fourni. LOG-001 analyse les retenues ; cette tâche garde restitution et majoration, sans confondre caution personnelle et dépôt. Réserve de charges → LOG-002 ; prescription de l'action à qualifier séparément avec CTX-030 si nécessaire. Absence de source : fiche factuelle et champs juridiques réservés.

Chaque échéance distingue événement, preuve, texte et version, acte requis,
destinataire et inconnues ; aucun effet interruptif ou suspensif présumé.
Ne pas présumer un abus ni garantir une issue ; aucune suspension de loyer,
signature, notification, saisine ou intervention matérielle exécutée.

## Références métier et sources à rechercher

Textes locatifs sur restitution, réserve de charges, majoration et exceptions, Code civil pour preuve et imputation des paiements, procédure et prescription de l'action ; ANIL/ADIL.

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

- Cas normal : LOG-023-N — Clés et adresse reçues, états joints et aucune restitution : établir chronologie et demande, puis calcul seulement sur sources vérifiées.
- Cas limite : LOG-023-L — Clés sans récépissé, nouvelle adresse tardive et restitution partielle : distinguer dates déclarées, principal et conditions de majoration non établies.
- Sans source lue : dossier factuel utile, questions précises et conclusion réservée, sans barème ou délai de mémoire.

Scénarios **attendus, non exécutés** ; conserver fixtures, sources, sorties
et erreurs lors des couches BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par un lecteur non juriste.

## Hors périmètre

Meublé, calcul automatisé sans source, analyse détaillée des dégradations, saisine et envoi. Social/conventionné, outre-mer, autres régimes non expressément
inclus ; aucune démarche externe exécutée.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur ; aucune sélection ni implémentation.
