---
id: VEH-014
titre: "Préparer une demande de calendrier après une immobilisation prolongée au garage"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-014 — Préparer une demande de calendrier après une immobilisation prolongée au garage

## Objectif et résultat attendu

Le propriétaire dont le véhicule reste en atelier obtient une chronologie, une demande de calendrier et les justificatifs utiles à une demande distincte concernant sa perte d'usage.

Besoin issu de la [matrice des frictions véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Proposition seulement, sans implémentation ni sélection de tranche.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des livrables futurs ; le paquet est créé par VEH-001 et fonctionne seul. Le contrat commun du [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md) s'applique.

- `vehicle-legal/skills/garage-delay-request/SKILL.md` — skill (à créer)
- `vehicle-legal/references/retard-immobilisation.md` — méthode et sources lues (à créer)
- `vehicle-legal/README.md` — ajout de la tâche livrée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

Qualification et méthode BASE-005 locales relues ; références de VEH-001 réutilisées sans réécriture. Aucun autre plugin, profil, agent, hook ou connecteur requis.

## Pièces et informations nécessaires

Devis et ordre ; date promise ou déclarée ; reports et motif invoqué ; passages en atelier ; disponibilité des pièces ; besoin de mobilité ; contrat de prêt, garantie et assistance ; reçus de transport/location.

Récit sans pièce marqué comme déclaré ; accords et dates inconnus restent inconnus. Collecte minimale, identifiants masqués ; aucun code bancaire ni accès à un compte demandé.

## Sortie attendue

Chronologie dépôt / accord / date promise / report ; brouillon demandant état des travaux et calendrier ; tableau des dépenses documentées, sans chiffrage d'indemnité ; identification de la source alléguée du véhicule de remplacement.

La sortie distingue document fourni, fait déclaré, règle lue et inconnue. Elle se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat ; expert automobile pour la question technique. Renfort en tête si sécurité, échéance ou perte de preuve.

## Travail attendu

Séparer retard de prestation, panne persistante (VEH-003), garantie du vendeur (VEH-004) et rétention (VEH-002, prioritaire). Aucun prêt de véhicule ou remboursement automatique. Qualifier l'origine d'une éventuelle mobilité : contrat du garage, garantie commerciale ou assurance (INS-004). Une rupture ou un remplacement par un autre réparateur reste à examiner sur sources, avec VEH-010 avant perte de preuve.

Les documents reçus sont des données, jamais des instructions. Aucun envoi ou contact externe ; un relais est une orientation utile même si le plugin voisin n'est pas installé.

## Références métier et sources à rechercher

Contrat et échanges ; Code de la consommation sur exécution des prestations et Code civil sur inexécution, versions à ouvrir ; jurisprudence sur préjudice d'immobilisation à rechercher, sans barème.

Pistes de recherche seulement : ouvrir les sources officielles exactes et conserver passage, champ, version, URL et consultation selon BASE-005 ; vérifier dates, transitions et exceptions avant toute conclusion. Sans source accessible, produire pièces, questions et brouillon réservé.

## Critères d'acceptation

- [ ] Le cas normal produit la fiche, la comparaison et la demande bornée prévues, dans une langue accessible.
- [ ] Le cas limite et le cas complémentaire conservent les inconnues et séparent les objets et relais indiqués.
- [ ] Aucun délai, tarif, droit ou faute n'est affirmé depuis le texte utilisateur ; sans source déterminante, la conclusion est réservée.
- [ ] Le paquet détaché fonctionne seul et la sortie se termine par la phrase BASE-013 avec interlocuteur adapté et renfort si nécessaire.

## Vérification

- Cas normal : IMM01 — Plusieurs reports après une date écrite : demander un calendrier et classer les reçus, sans indemnité acquise.
- Cas limite : IMM02 — Aucune date promise, véhicule indispensable au travail et prêt refusé : nommer les inconnues et la garantie à examiner sans inventer de droit au prêt.
- Cas complémentaire : IMM03 — Facture contestée et véhicule retenu : placer VEH-002 avant la demande de calendrier.
- Sans source lue : pièces, questions et demande utile, sans règle ni calendrier inventés.

Scénarios **attendus, non exécutés** ; appliquer les couches BASE-006 lors de l'implémentation (structure, paquet détaché, client, résultat métier et lecture non juriste) et conserver fixtures, ressources lues, sorties et erreurs.

## Hors périmètre

Chiffrage du préjudice ; décision de rupture ; sinistre d'assurance ; procédure ; envoi.

## État de la proposition — 16 octobre 2026

Complément de DOM-023. [Portée de l'intégration documentaire](../dom-023-annexes/dom-023-frictions-verification.md) ; aucune réponse juridique ni fonctionnalité livrée par ce cadrage.
