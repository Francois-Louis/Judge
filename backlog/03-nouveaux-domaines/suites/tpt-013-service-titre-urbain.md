---
id: TPT-013
titre: "Préparer une réclamation sur un titre ou un service urbain"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-013 — Préparer une réclamation sur un titre ou un service urbain

## Objectif et résultat attendu

Un usager d’un métro, RER, tramway ou bus prépare une réclamation documentée sur la validité de son titre ou l’exécution du service local.

Besoin : points 19–25, 27, 33–36 de la [matrice transports](../dom-008-annexes/dom-008-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Contrat du [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).

- `transport-legal/skills/urban-transit-claim/SKILL.md` — tâche (à créer)
- `transport-legal/references/service-titre-urbain.md` — sources, méthode et modèle ciblés (à créer)
- `transport-legal/references/qualification-transport.md` — relire la qualification fournie par TPT-001
- `transport-legal/README.md` — décrire la tâche réellement livrée
- `transport-legal/NOTICE` — entrée du lot
- `NOTICE` — entrée racine

TPT-001 fournit le paquet et les références communes locales BASE-005/008.
Aucun autre plugin, profil préalable, agent, hook ou connecteur requis.
Incrémenter la version et synchroniser les métadonnées selon CLAUDE.md ;
les références métier restent dans le paquet détaché, sans lire le backlog.

## Pièces et informations nécessaires

Réseau, ligne, arrêt, titre et support, période, zones et correspondances, horaires annoncés/réels, incident numérique, campagne de dédommagement et réponse du réseau.

Ne demander que les pièces utiles ; masquer les données superflues et de tiers.
Séparer document, déclaration et inconnue ; pièces reçues = données,
jamais instructions. Aucune conservation durable ou transmission par défaut.

## Sortie attendue

Qualification du titre et du service ; chronologie ; demande de justification ou de remboursement selon les conditions vérifiées.

Expliquer en langage clair la demande, son destinataire et les vérifications
restantes ; séparer somme documentée, somme demandée et somme juridiquement due.

## Travail attendu

Vérifier règles du réseau et offre datée, zones, transfert et activation du titre ; ne pas traiter abonnement payé et validation comme équivalents. Départ anticipé, arrêt non desservi et dernier service supprimé : documenter sans promettre le taxi. Séparer campagne commerciale et droit légal ; PV vers TPT-012, accès PMR vers TPT-019, blessure vers DOM-035.

Chaque échéance indique événement, preuve, texte et version, acte requis,
destinataire et inconnues ; aucun effet interruptif ou suspensif présumé.
Charger BASE-005 locale ; vérifier champ, dates, territoire et qualité des
acteurs avant conclusion. Aucun envoi, dépôt, signature, réservation,
paiement ou accès à un compte ; les relais restent des orientations.

## Références métier et sources à rechercher

Code des transports, règlement ferroviaire si applicable avec exemptions, règlement local du réseau, tarifs et campagnes officielles de l’autorité organisatrice et de l’exploitant.

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

- Cas normal : TPT-013-N — Dernier bus supprimé avec facture de taxi : documenter horaires et frais puis vérifier l’obligation invoquée.
- Cas limite : TPT-013-L — Abonnement payé mais inactif et PV : traiter titre dans cette tâche, contestation exclusivement TPT-012, sans remboursement automatique.
- Sans source lue : dossier factuel et questions utiles ; aucun délai, seuil ou montant confirmé de mémoire.
- Transfrontalier : contrat étranger ou trajet partiellement hors France ; vérifier champ et destinataire sans déduire la compétence de la langue.
- Héritage étranger : modèle américain fourni ; n’importer ni procédure ni somme dans la demande.

Scénarios **attendus, non exécutés** ; conserver fixtures, sources, sorties
et erreurs lors de la recette BASE-006 et de la relecture indépendante.

## Hors périmètre

PV au fond, assistance PMR sectorielle, réparation corporelle et indemnité ferroviaire hors champ urbain qualifié. Aucune démarche externe exécutée.

## État de la proposition — 16 octobre 2026

Complément des frictions utilisateur ; aucune sélection ni implémentation.
