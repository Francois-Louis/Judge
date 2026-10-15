---
id: DOM-022
titre: "Cadrer un plugin télécoms et services postaux"
statut: proposee
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

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage distingue médiation, signalement au régulateur et demande de réparation ; il identifie le bon cocontractant pour un colis.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un opérateur facture du matériel pourtant restitué.
- La fibre n'est pas installée mais l'abonnement est facturé.
- Un destinataire attend une commande dont le colis est déclaré perdu.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

