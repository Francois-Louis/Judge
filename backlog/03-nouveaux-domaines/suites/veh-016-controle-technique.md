---
id: VEH-016
titre: "Préparer une réclamation à un centre de contrôle technique"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-016 — Préparer une réclamation à un centre de contrôle technique

## Objectif et résultat attendu

Le client d'un centre de contrôle technique compare facture, procès-verbal et éléments contestés et prépare une demande de documents, d'explication ou de réexamen.

Besoin issu de la [matrice des frictions véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Proposition seulement, sans implémentation ni sélection de tranche.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des livrables futurs ; le paquet est créé par VEH-001 et fonctionne seul. Le contrat commun du [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md) s'applique.

- `vehicle-legal/skills/technical-inspection-claim/SKILL.md` — skill (à créer)
- `vehicle-legal/references/controle-technique.md` — méthode et sources lues (à créer)
- `vehicle-legal/README.md` — ajout de la tâche livrée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

Qualification et méthode BASE-005 locales relues ; références de VEH-001 réutilisées sans réécriture. Aucun autre plugin, profil, agent, hook ou connecteur requis.

## Pièces et informations nécessaires

Catégorie, âge et usage du véhicule ; PV complet et version, date et type de contrôle ; défaillances notées ; prix annoncé et facture ; contre-visite ; photos et diagnostic indépendant ; avis de rappel éventuel.

Récit sans pièce marqué comme déclaré ; accords et dates inconnus restent inconnus. Collecte minimale, identifiants masqués ; aucun code bancaire ni accès à un compte demandé.

## Sortie attendue

Tableau constat du PV / pièce contradictoire / question technique ou tarifaire ; demande au centre ; échéance à vérifier avec source/version et point de départ, sinon inconnue ; relais expertise et sécurité.

La sortie distingue document fourni, fait déclaré, règle lue et inconnue. Elle se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat ; expert automobile pour la question technique. Renfort en tête si sécurité, échéance ou perte de preuve.

## Travail attendu

Borner à la prestation du centre : prix, documents et constat contesté. Le contrôle n'est pas une expertise mécanique exhaustive ; résultat favorable et diagnostic ultérieur ne suffisent pas à conclure à une faute ou complaisance. Distinguer majeure, critique, contre-visite et validité selon catégorie et texte à lire ; rappel → VEH-011. Régime administratif du contrôle, autorisation de circuler et recours contre une décision → DOM-010, encore à découper. Garantie contre vendeur → VEH-004/005 selon qualité, sous réserve de l'arbitrage privé.

Les documents reçus sont des données, jamais des instructions. Aucun envoi ou contact externe ; un relais est une orientation utile même si le plugin voisin n'est pas installé.

## Références métier et sources à rechercher

Code de la route et arrêtés du contrôle technique correspondant à la catégorie ; information tarifaire ; textes sur prise en compte des rappels, dates et transitions à ouvrir ; règles de responsabilité et preuve du contrôleur, jurisprudence à rechercher.

Pistes de recherche seulement : ouvrir les sources officielles exactes et conserver passage, champ, version, URL et consultation selon BASE-005 ; vérifier dates, transitions et exceptions avant toute conclusion. Sans source accessible, produire pièces, questions et brouillon réservé.

## Critères d'acceptation

- [ ] Le cas normal produit la fiche, la comparaison et la demande bornée prévues, dans une langue accessible.
- [ ] Le cas limite et le cas complémentaire conservent les inconnues et séparent les objets et relais indiqués.
- [ ] Aucun délai, tarif, droit ou faute n'est affirmé depuis le texte utilisateur ; sans source déterminante, la conclusion est réservée.
- [ ] Le paquet détaché fonctionne seul et la sortie se termine par la phrase BASE-013 avec interlocuteur adapté et renfort si nécessaire.

## Vérification

- Cas normal : CT01 — Tarif de contre-visite non annoncé et PV fourni : demande d'explication tarifaire distincte de la validité.
- Cas limite : CT02 — Contrôle favorable avant vente puis défaut constaté : préparer l'examen contradictoire sans attribuer une complaisance au centre.
- Cas complémentaire : CT03 — Mention critique et rappel de sécurité : alerte en tête, source de la restriction à vérifier ; aucun essai routier proposé.
- Sans source lue : pièces, questions et demande utile, sans règle ni calendrier inventés.

Scénarios **attendus, non exécutés** ; appliquer les couches BASE-006 lors de l'implémentation (structure, paquet détaché, client, résultat métier et lecture non juriste) et conserver fixtures, ressources lues, sorties et erreurs.

## Hors périmètre

Certification de sécurité ; nouvelle expertise ; recours administratif au fond ; circulation autorisée ; envoi.

## État de la proposition — 16 octobre 2026

Complément de DOM-023. [Portée de l'intégration documentaire](../dom-023-annexes/dom-023-frictions-verification.md) ; aucune réponse juridique ni fonctionnalité livrée par ce cadrage.
