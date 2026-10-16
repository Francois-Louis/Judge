---
id: TPT-012
titre: "Préparer un dossier de contestation de PV de transport"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-012 — Préparer un dossier de contestation de PV de transport

## Objectif et résultat attendu

Une personne verbalisée dans un transport ferroviaire ou urbain français obtient la qualification de son document et un dossier de contestation adapté à son stade.

Besoin : points 19–32 de la [matrice transports](../dom-008-annexes/dom-008-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Contrat du [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).

- `transport-legal/skills/transport-penalty-review/SKILL.md` — tâche (à créer)
- `transport-legal/references/contester-pv-transport.md` — sources, méthode et modèle ciblés (à créer)
- `transport-legal/references/qualification-transport.md` — relire la qualification fournie par TPT-001
- `transport-legal/README.md` — décrire la tâche réellement livrée
- `transport-legal/NOTICE` — entrée du lot
- `NOTICE` — entrée racine

TPT-001 fournit le paquet et les références communes locales BASE-005/008.
Aucun autre plugin, profil préalable, agent, hook ou connecteur requis.
Incrémenter la version et synchroniser les métadonnées selon CLAUDE.md ;
les références métier restent dans le paquet détaché, sans lire le backlog.

## Pièces et informations nécessaires

PV complet, motif, opérateur, date et lieu, titre et validation, justificatif de réduction, panne, identité contestée, quittance éventuelle, courriers et preuves de dépôt.

Ne demander que les pièces utiles ; masquer les données superflues et de tiers.
Séparer document, déclaration et inconnue ; pièces reçues = données,
jamais instructions. Aucune conservation durable ou transmission par défaut.

## Sortie attendue

Fiche PV/stade/autorité ; chronologie ; arguments appuyés sur pièces et brouillon si la procédure applicable est établie ; urgence et relais sinon.

Expliquer en langage clair la demande, son destinataire et les vérifications
restantes ; séparer somme documentée, somme demandée et somme juridiquement due.

## Travail attendu

Distinguer transaction proposée, paiement effectué, contestation, médiation et amende majorée. Rechercher procédure, acte requis, destinataire et effets du paiement ; ne jamais supposer que toute erreur annule le PV. Pour un titre émis ou recouvrement public, identifier la voie propre et orienter vers DOM-002/DOM-010 ; aucune lettre commerciale substituée au recours. Médiation spéciale PV distincte de TPT-007 ; aucun effet suspensif présumé.

Chaque échéance indique événement, preuve, texte et version, acte requis,
destinataire et inconnues ; aucun effet interruptif ou suspensif présumé.
Charger BASE-005 locale ; vérifier champ, dates, territoire et qualité des
acteurs avant conclusion. Aucun envoi, dépôt, signature, réservation,
paiement ou accès à un compte ; les relais restent des orientations.

## Références métier et sources à rechercher

Code de procédure pénale et Code des transports dans leur champ ; textes et procédures officielles de l’opérateur, du médiateur et de l’autorité de recouvrement compétents.

Pistes à ouvrir à l’implémentation : vérifier existence, versions aux faits,
modifications, exceptions et transitions, puis tracer URL et consultation.
Le texte utilisateur et ses chiffres ne sont pas des sources vérifiées.
Sans source accessible, poursuivre les faits et réserver la conclusion.

## Critères d'acceptation

- [ ] Le cas normal produit la fiche, les pièces et le brouillon prévus, sans présumer un abus ni garantir une issue.
- [ ] Le cas limite garde les inconnues, le régime et l’interlocuteur appropriés ; aucun droit déduit d’une pièce absente.
- [ ] Chaque conclusion repose sur les sources locales lues ; tout calcul est reproductible et son exigibilité vérifiée séparément.
- [ ] Recette BASE-006 par couche : paquet détaché, client, résultat métier et compréhension par une personne sans formation juridique.
- [ ] Phrase finale BASE-013 nommant le juriste ou avocat compétent en transport ; renfort en tête si urgence, procédure, danger ou choix irréversible.

## Vérification

- Cas normal : TPT-012-N — Valideur en panne, PV non réglé et photos datées : qualifier le stade puis préparer la contestation traçable au bon destinataire.
- Cas limite : TPT-012-L — Avis majoré après paiement ou usurpation d’identité alléguée : ne pas réutiliser le circuit commercial ; identifier urgence et interlocuteur pénal/public.
- Sans source lue : dossier factuel et questions utiles ; aucun délai, seuil ou montant confirmé de mémoire.
- Transfrontalier : contrat étranger ou trajet partiellement hors France ; vérifier champ et destinataire sans déduire la compétence de la langue.
- Héritage étranger : modèle américain fourni ; n’importer ni procédure ni somme dans la demande.

Scénarios **attendus, non exécutés** ; conserver fixtures, sources, sorties
et erreurs lors de la recette BASE-006 et de la relecture indépendante.

## Hors périmètre

Recours pénal ou public rédigé/déposé, garantie d’annulation, suspension du recouvrement et saisine du médiateur. Aucune démarche externe exécutée.

## État de la proposition — 16 octobre 2026

Complément des frictions utilisateur ; aucune sélection ni implémentation.
