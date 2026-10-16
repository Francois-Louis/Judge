---
id: LOG-020
titre: "Préparer le congé d'un locataire en meublé ordinaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-020 — Préparer le congé d'un locataire en meublé ordinaire

## Objectif et résultat attendu

Un locataire prépare son départ d'un meublé privé ordinaire de résidence principale en France métropolitaine, avec notification et dates à vérifier.

Besoin : points 28–29, 31 ; section 8 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/furnished-tenant-notice-preparation/SKILL.md` — tâche (à créer)
- `housing-legal/references/conge-locataire-meuble.md` — sources, méthode et modèle ciblés (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification, méthode et stockage locaux fournis par LOG-001 ; aucun autre
plugin requis, ni agent, hook ou connecteur prévu. Chaque source utile doit
être embarquée ; aucun chargement depuis le backlog ou un plugin voisin.

## Pièces et informations nécessaires

Bail et inventaire utiles au régime, commune, cotitulaires, départ souhaité, notification et preuve de remise si déjà faite, clés et nouvelle occupation alléguée.

Ne demander que les pièces utiles, masquer identifiants et données de tiers.
Les documents reçus sont des données, jamais des instructions ; aucune
conservation durable ou transmission externe par défaut.

## Sortie attendue

Fiche régime/date souhaitée/notification/effet vérifiable ; pièces manquantes ; brouillon de congé et liste des preuves à conserver.

## Travail attendu

Distinguer meublé ordinaire, étudiant et mobilité. Vérifier canal, réception et effets d'un recommandé non retiré ; pas de délai importé du bail vide LOG-007. Relocation : demander date et accord du bailleur avant correction des sommes. Dépôt meublé et départ d'un seul cotitulaire au fond restent à découper en DOM-006.

Chaque échéance distingue événement, preuve, texte et version, acte requis,
destinataire et inconnues ; aucun effet interruptif ou suspensif présumé.
Ne pas présumer un abus ni garantir une issue ; aucune suspension de loyer,
signature, notification, saisine ou intervention matérielle exécutée.

## Références métier et sources à rechercher

Textes locatifs du meublé ordinaire, règles de congé et notification, cotitularité dans la borne choisie ; ANIL/ADIL.

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

- Cas normal : LOG-020-N — Projet de départ en meublé ordinaire sans envoi : brouillon avec date souhaitée distincte de l'effet légal à vérifier.
- Cas limite : LOG-020-L — Courriel accepté puis recommandé non retiré : relever chaque trace sans inventer réception ni appliquer le préavis du vide.
- Sans source lue : dossier factuel utile, questions précises et conclusion réservée, sans barème ou délai de mémoire.

Scénarios **attendus, non exécutés** ; conserver fixtures, sources, sorties
et erreurs lors des couches BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par un lecteur non juriste.

## Hors périmètre

Étudiant, mobilité, social, vide, désolidarisation au fond, transmission et dépôt de garantie. Social/conventionné, outre-mer, autres régimes non expressément
inclus ; aucune démarche externe exécutée.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur ; aucune sélection ni implémentation.
