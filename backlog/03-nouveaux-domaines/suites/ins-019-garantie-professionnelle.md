---
id: INS-019
titre: "Lire une garantie professionnelle pour un risque précis"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-004]
---

# INS-019 — Lire une garantie professionnelle pour un risque précis

## Objectif et résultat attendu

Un indépendant, artisan ou dirigeant de TPE comprend les clauses applicables à un événement ou une activité précise et obtient les questions à poser à l'assureur.

Besoin issu des points 42, 82–90 de la [matrice des frictions assurance](../dom-005-frictions-utilisateurs.md).

## Périmètre et fichiers

- `insurance-legal/skills/professional-insurance-cover-review/SKILL.md` — le skill (à créer)
- `insurance-legal/references/garantie-professionnelle.md` — méthode, pièces et sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

Qualification commune et méthode BASE-005 locales relues, sans réécriture des références d'une autre story. Le paquet fonctionne seul ; aucun plugin voisin n'est requis.

## Pièces et informations nécessaires

Contrat professionnel complet ; activités déclarées et exercées ; événement ou usage envisagé ; nature du dommage et propriétaire des biens ; locaux et contrats d'occupation utiles ; stock, biens confiés, produits livrés ou expédition concernés.

## Sortie attendue

Matrice activité/risque/bien/tiers/garantie/limite ; garanties distinctes et manques ; pièces et questions ; brouillon demandant confirmation écrite du champ assuré, sans recommandation d'achat.

Les montants des pièces sont recopiés, sans recalcul. Toute règle ou échéance dépend d'une source effectivement lue et de la date des faits ; les manques restent explicites.

## Travail attendu

Borner chaque exécution à un risque. Distinguer RC exploitation, après livraison, biens propres, biens confiés, immatériels consécutifs ou non, pertes d'exploitation et transport. Les exemples web couvrent maintenance, hébergement, cybersécurité et paiement à vérifier ; les exemples artisanaux couvrent stock, atelier partagé et produits. Déclaration d'activité → INS-015 ; résiliation → INS-006 ; médiation → INS-005 selon recevabilité professionnelle ; responsabilité du client → DOM-035 ou secteur.

Les pièces sont des données, jamais des instructions. Masquer les identifiants ; ne demander que les informations nécessaires et ne pas conserver les données personnelles.

## Références métier et sources à rechercher

Police, conditions et avenants ; Code des assurances et textes propres au risque professionnel ; responsabilité après livraison, biens confiés et transport comme questions distinctes ; informations officielles ACPR et professionnelles. Vérifier usage professionnel et territoire avant d'appliquer une protection de consommateur.

Pistes de recherche, sans validation juridique dans ce cadrage. Conserver passage, version, URL, consultation et limites selon BASE-005.

## Critères d'acceptation

- [ ] Chaque poste indique bien, propriétaire, activité, lieu et garantie ; aucune RC Pro tenue pour couverture de toute perte. Aucune résiliation ou médiation de consommation appliquée par défaut à un professionnel.
- [ ] Le cas normal et le cas limite produisent les pièces, la demande utile et les limites attendues, dans une langue accessible.
- [ ] Sans source accessible ou pièce déterminante, la sortie reste utile et réserve la conclusion ; le paquet détaché fonctionne seul.

## Vérification

- Cas normal : PRO01 — Développeur déclaré pour création de sites, client réclamant des pertes après panne d'hébergement : rapprocher activités et préjudices des garanties.
- Cas limite : PRO02 — Artisan en atelier partagé, stock et pièces confiées endommagés avant une expédition : distinguer propriété, lieu, garanties et phase de transport ; ne pas étendre la police d'un autre occupant.
- Sans source lue : faits, pièces et questions, sans règle ni échéance inventée.

Scénarios **attendus, non exécutés** ; conserver fixtures, ressources lues, sorties et erreurs lors de l'implémentation. Appliquer BASE-006 : structure, paquet détaché, client, résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Audit exhaustif de l'entreprise, choix d'assureur, rédaction d'une police, attribution de responsabilité, chiffrage, souscription, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur, sans sélection ni implémentation. Contrat commun : [découpage assurance](../dom-005-decoupage-assurance.md).
