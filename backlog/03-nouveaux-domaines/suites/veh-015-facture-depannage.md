---
id: VEH-015
titre: "Examiner une facture de dépannage ou de remorquage"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-015 — Examiner une facture de dépannage ou de remorquage

## Objectif et résultat attendu

Une personne comprend les lignes de dépannage/remorquage, le régime tarifaire à vérifier et les justificatifs à demander, puis obtient un brouillon au prestataire.

Besoin issu de la [matrice des frictions véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Proposition seulement, sans implémentation ni sélection de tranche.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des livrables futurs ; le paquet est créé par VEH-001 et fonctionne seul. Le contrat commun du [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md) s'applique.

- `vehicle-legal/skills/towing-invoice-review/SKILL.md` — skill (à créer)
- `vehicle-legal/references/depannage-remorquage.md` — méthode et sources lues (à créer)
- `vehicle-legal/README.md` — ajout de la tâche livrée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

Qualification et méthode BASE-005 locales relues ; références de VEH-001 réutilisées sans réécriture. Aucun autre plugin, profil, agent, hook ou connecteur requis.

## Pièces et informations nécessaires

Lieu précis et catégorie de voie ; date/heure, poids et catégorie du véhicule ; auteur de l'appel et intervention autorisée ; facture, devis ou information préalable ; trajet, destination choisie et kilomètres ; accord d'assistance ; photos avant/après.

Récit sans pièce marqué comme déclaré ; accords et dates inconnus restent inconnus. Collecte minimale, identifiants masqués ; aucun code bancaire ni accès à un compte demandé.

## Sortie attendue

Fiche du régime retenu ou inconnu ; tableau ligne / service / information ou accord / inclusion et supplément à vérifier ; questions sur destination et intervenant ; brouillon de demande de détail ou de contestation.

La sortie distingue document fourni, fait déclaré, règle lue et inconnue. Elle se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat ; expert automobile pour la question technique. Renfort en tête si sécurité, échéance ou perte de preuve.

## Travail attendu

Distinguer dépannage contractuel, autoroute/voie soumise à régime spécial et enlèvement en fourrière par autorité (DOM-010). Aucun forfait national appliqué à tout remorquage. Rechercher arrêté tarifaire exact, date, poids, horaires, inclusions et suppléments ; ne pas intégrer les prix du texte utilisateur comme constantes. Destination et accord de réparation se traitent séparément ; gardiennage/rétention → VEH-002 ; assistance → INS-004 ; dommage de remorquage documenté, cause réservée → VEH-010 et demande au prestataire.

Les documents reçus sont des données, jamais des instructions. Aucun envoi ou contact externe ; un relais est une orientation utile même si le plugin voisin n'est pas installé.

## Références métier et sources à rechercher

Textes officiels encadrant agrément, tarifs et périmètre des dépannages sur autoroute/route express ; information des prix hors régime spécial ; Code civil sur contrat, preuve et inexécution ; contrat d'assistance séparé.

Pistes de recherche seulement : ouvrir les sources officielles exactes et conserver passage, champ, version, URL et consultation selon BASE-005 ; vérifier dates, transitions et exceptions avant toute conclusion. Sans source accessible, produire pièces, questions et brouillon réservé.

## Critères d'acceptation

- [ ] Le cas normal produit la fiche, la comparaison et la demande bornée prévues, dans une langue accessible.
- [ ] Le cas limite et le cas complémentaire conservent les inconnues et séparent les objets et relais indiqués.
- [ ] Aucun délai, tarif, droit ou faute n'est affirmé depuis le texte utilisateur ; sans source déterminante, la conclusion est réservée.
- [ ] Le paquet détaché fonctionne seul et la sortie se termine par la phrase BASE-013 avec interlocuteur adapté et renfort si nécessaire.

## Vérification

- Cas normal : DEPAN01 — Dépannage présenté comme autoroutier avec supplément de nuit : qualifier voie, poids et horaire avant tout contrôle tarifaire.
- Cas limite : DEPAN02 — Remorquage en ville, prix annoncé à l'arrivée et facture groupée : demander détail et preuve d'information, sans appliquer le forfait autoroutier.
- Cas complémentaire : DEPAN03 — Enlèvement ordonné puis gardiennage : identifier la fourrière administrative ; ne pas utiliser la contestation contractuelle seule.
- Sans source lue : pièces, questions et demande utile, sans règle ni calendrier inventés.

Scénarios **attendus, non exécutés** ; appliquer les couches BASE-006 lors de l'implémentation (structure, paquet détaché, client, résultat métier et lecture non juriste) et conserver fixtures, ressources lues, sorties et erreurs.

## Hors périmètre

Appel ou organisation du dépannage ; tarif non vérifié ; fourrière au fond ; diagnostic de dommage ; assurance au fond ; envoi.

## État de la proposition — 16 octobre 2026

Complément de DOM-023. [Portée de l'intégration documentaire](../dom-023-annexes/dom-023-frictions-verification.md) ; aucune réponse juridique ni fonctionnalité livrée par ce cadrage.
