---
id: DOM-023
titre: "Cadrer un plugin véhicules, garages et réparations"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-023 — Cadrer un plugin véhicules, garages et réparations

## Objectif

Aider acheteurs et propriétaires à examiner une vente, une facture ou une réparation de véhicule.

Nom de plugin proposé : `vehicle-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer la revue d'une annonce, d'un bon de commande et des garanties alléguées.
- Documenter une panne après achat selon la qualité du vendeur et les pièces.
- Lire devis, ordre de réparation, facture ou frais de gardiennage contestés.

## Qualification et frontières

Vendeur particulier/professionnel, acheteur, type de contrat, kilométrage, historique, dates, diagnostics, réparations et accords donnés.

L'achat, la location et la réparation du véhicule sont ici ; infraction/permis restent en DOM-002, l'assurance en DOM-005 et l'accident corporel requiert le régime identifié avec DOM-035.

## Sources à prévoir et vérifier

Code civil, Code de la consommation et textes automobiles pertinents, DGCCRF et règles de preuve/expertise applicables.

- [DGCCRF](https://www.economie.gouv.fr/dgccrf)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter une facture de garage et la comparer aux travaux autorisés par les pièces fournies.

## Critères d'acceptation

- [x] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [x] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [x] Les régimes de vente entre particuliers, vente professionnelle, location et prestation de réparation ne sont pas confondus.
- [x] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un garage facture une opération sans accord retrouvé.
- Une voiture d'occasion présente une panne peu après l'achat.
- Un loueur réclame des dommages au retour.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.


## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-023-annexes/dom-023-decoupage-vehicules.md) : nom
  `vehicle-legal` conservé (`judge-fr-eu-vehicle-legal`) ; installation
  seule, sans profil, agent, hook, connecteur ni accès à un système
  d'immatriculation ou à un historique en ligne ; garde-fous (aucune
  expertise technique, sécurité d'abord, quatre régimes non confondus,
  aucune présomption contre l'autre partie, aucune promesse d'issue, aucun
  délai, durée de garantie ni montant inventé, conservation de l'état,
  collecte minimale) ; table des points d'entrée en langage courant ;
  qualification commune (parties, contrat, véhicule, dates, accords et
  pièces, diagnostics, urgence) ; frontières avec consommation, pénal,
  assurance, responsabilité, banque, exécution, administratif, transports,
  contentieux, contrats professionnels, données, dettes, plateformes et
  successions.
- 12 propositions VEH-001 à VEH-012 sous `suites/`, en quatre rangs.
  Première tranche : VEH-001, facture de garage comparée au devis et aux
  accords retrouvés, qui crée le paquet avec ce seul skill. Gardiennage et
  rétention, réparation défaillante, occasion chez un professionnel ou un
  particulier et dommages au retour d'une location au rang 2 ; revue avant
  achat, véhicule neuf, fin de location longue, expertise amiable et
  garantie constructeur au rang 3 ; réponse du vendeur particulier au rang 4.
- Vente entre particuliers, vente professionnelle, location et prestation de
  réparation séparées (VEH-005, VEH-004, VEH-006 et VEH-009, VEH-001 à
  VEH-003).
- Arbitrage à confirmer : la décision du 16 octobre 2026 garde les achats
  entre particuliers dans `consumer-legal` ; le cadrage l'applique aux biens
  autres qu'un véhicule et propose VEH-005 et VEH-012 pour le véhicule, avec
  repli vers CONSO-011 si la décision est étendue.
- Cinq points ouverts sans story : engins de déplacement personnel et
  cyclomoteurs, achat dans un autre État membre ou par mandataire,
  contestation d'un contrôle technique, dépannage hors garage choisi, vente
  entre particuliers d'un véhicule tant que l'arbitrage n'est pas rendu.
- [Vérification documentaire](dom-023-annexes/dom-023-verification.md) :
  les trois scénarios de la story (la panne d'occasion suivie avec un vendeur
  professionnel puis un particulier) et quatorze cas limites, sans délai,
  montant ni droit conclu.
- Ligne `vehicle-legal` de la [matrice BASE-003](../00-fondations/base-003-annexes/base-003-dossier-architecture.md)
  précisée ; famille VEH ajoutée au générateur de l'index et index régénéré.
- [Contrôles statiques](dom-023-annexes/dom-023-resultats.json), produits par
  [le contrôleur du lot](dom-023-annexes/dom-023-controles.py), sur le modèle de DOM-007.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 12 propositions `suites/veh-*.md`, ligne de BASE-003,
`backlog/etat.py` et `backlog/ETAT.md`. Le lot reste sous `backlog/`, sans
entrée NOTICE.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.
