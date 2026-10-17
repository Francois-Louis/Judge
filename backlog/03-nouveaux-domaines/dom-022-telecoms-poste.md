---
id: DOM-022
titre: "Cadrer un plugin télécoms et services postaux"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-022 — Cadrer un plugin télécoms et services postaux

## Objectif

Aider à contester des frais, une résiliation ou une prestation défaillante de télécommunication ou de service postal.

Nom de plugin proposé : `telecom-postal-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer une réclamation de facturation, engagement, option ou frais de résiliation.
- Organiser les preuves de panne, non-installation ou interruption de service.
- Qualifier la demande après perte ou dommage d'un envoi selon le rôle de l'usager et le contrat.

## Qualification et frontières

Opérateur, service, titulaire, offre, engagement, dates, interventions, preuve de retour du matériel et rôle d'expéditeur/destinataire pour un envoi.

Le contrat avec l'opérateur est ici ; l'obligation de livraison du vendeur reste en DOM-001, le fret spécialisé en DOM-008 et la modération de plateforme en DOM-034.

## Sources à prévoir et vérifier

Code des postes et des communications électroniques, Code de la consommation, règles du transport ou du service selon l'objet et sources de l'ARCEP.

- [Contrat de téléphone, internet ou télévision — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F19061)
- [ARCEP](https://www.arcep.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Préparer une réclamation pour des frais de résiliation contestés sur un abonnement de particulier.

## Critères d'acceptation

- [x] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [x] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [x] Le cadrage distingue médiation, signalement au régulateur et demande de réparation ; il identifie le bon cocontractant pour un colis.
- [x] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un opérateur facture du matériel pourtant restitué.
- La fibre n'est pas installée mais l'abonnement est facturé.
- Un destinataire attend une commande dont le colis est déclaré perdu.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Bilan d'exécution — 17 octobre 2026

- [Découpage télécoms et poste](dom-022-annexes/dom-022-decoupage-telecoms-poste.md) :
  nom `telecom-postal-legal` conservé, identifiant publié futur
  `judge-fr-eu-telecom-postal-legal`, qualification des contrats, personnes,
  territoires, dates, incidents et objectifs ; autonomie de paquetage prévue.
- Neuf propositions TEL-001 à TEL-009 dans `suites/`, chacune avec entrées,
  sortie, pièces, limites, référence métier future et scénarios. Première
  tranche TEL-001 limitée à la réclamation de frais de résiliation d'un
  abonnement particulier en France métropolitaine, sans calcul de somme due.
- Matériel, facturation/options, non-installation, interruption et envoi
  postal séparés ; médiations télécoms et postale distinctes, signalement
  au régulateur séparé d'une demande de réparation individuelle.
- Livraison de vente conservée en DOM-001 ; qualité de l'expéditeur,
  destinataire et cocontractant postal établie par les contrats et pièces,
  sans recours exclusif imposé au transporteur. Frontières fret DOM-008,
  douanes DOM-009 et plateformes DOM-034 explicites.
- [Vérification documentaire](dom-022-annexes/dom-022-verification.md) des
  trois scénarios demandés et des limites, distincte des
  [résultats statiques](dom-022-annexes/dom-022-resultats.json).
- Matrice BASE-003 et situation S-12 précisées ; famille TEL ajoutée au
  générateur et index ETAT régénéré. Lot limité à `backlog/` : présente story,
  trois annexes, neuf propositions, architecture, usages, générateur et index.
  Aucun changement de plugin, de version ou de NOTICE.

**Portée :** cadrage documentaire, aucun plugin ni skill créé ou exécuté,
aucune installation ou démarche externe. Sources métier non consultées et
versions applicables à vérifier lors des futures implémentations ; aucun
délai, montant ou résultat juridique validé. PILOTE-003 est terminé après
BASE-011 ; son bilan ne sélectionne pas automatiquement de tranche. Toutes
les suites restent `proposee`.

La relecture humaine est prise en charge par l'utilisateur selon AGENTS.md
du 17 octobre 2026 ; elle n'est pas déclarée effectuée. La compréhension par
un lecteur réel n'a pas été observée. DOM-022 est close sur ses livrables et
contrôles de cadrage, sans attendre cette relecture.


## Complément des frictions douanes — 17 octobre 2026

Points 1, 5–6 et 13–24, 52 et 75 : V01 ajoute les frais privés de dédouanement/stockage/retour et l'inaction du prestataire aux tâches postales à découper. TEL-006 garde perte/dommage dans son périmètre ; ne pas prétendre qu'il couvre tous les honoraires. Recueillir rôle/contrat, facture ventilée, tarif, suivi, pièces demandées/transmises et dates ; sortie future : historique, fondement contractuel à rechercher et brouillon de réclamation. Cas : suivi douane sans acte ; facture après livraison ; destruction annoncée par le prestataire. Séparer décision officielle DOU-009/C16/C17, obligations du vendeur DOM-001, fret DOM-008 et assurance DOM-005. Médiation postale TEL-008 ne remplace pas un recours douanier ; aucune gratuité, suppression des frais ou suspension présumée.

Exigences de la [matrice des 75 points](dom-009-annexes/dom-009-frictions-utilisateurs.md), sans sélection de tranche ni capacité annoncée comme livrée. [Portée et contrôles](dom-009-annexes/dom-009-frictions-verification.md).
