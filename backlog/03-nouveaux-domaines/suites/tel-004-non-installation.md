---
id: TEL-004
titre: "Préparer une réclamation pour un accès télécoms non installé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-004 — Préparer une réclamation pour un accès télécoms non installé

## Objectif et périmètre

Un particulier commandant un accès fixe grand public en France
métropolitaine documente l'installation non réalisée et la facturation
alléguée. Une commande ; pas de diagnostic réseau ni recours d'urbanisme.
Plugin futur `telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).

## Entrées et pièces

Commande, offre, opérateur cocontractant et titulaire, date/périmètre de
mise en service annoncés, rendez-vous et comptes rendus, accès au local,
travaux ou autorisation évoqués, activation annoncée, tests et tickets,
factures/paiements masqués, échanges. Ne pas demander plan du domicile ou
coordonnées de tiers sans utilité établie.

## Sortie attendue

Chronologie promesse/rendez-vous/intervention/activation annoncée/service
constaté/facturation ; tableau des pièces et inconnues, questions techniques
à faire confirmer, brouillon à l'opérateur facturant. Demande choisie :
explication, installation ou correction ; effet d'une rupture à examiner
séparément, sans résilier ni promettre l'absence de frais.

## Travail et références métier

Créer `skills/uninstalled-service-complaint/SKILL.md` et
`references/non-installation.md` ; ressources locales communes, README,
version, inventaire et NOTICE à mettre à jour. Lire contrat et conditions
d'installation, Code de la consommation/CPCE selon fourniture et facturation,
ressources officielles ARCEP sur raccordement. Pistes **non consultées par
DOM-022** ; identifier le champ et la version avant toute règle ou durée.

## Critères d'acceptation

- [ ] T12 distingue activation annoncée, installation matérielle et service constaté ; aucun diagnostic ou responsable technique inventé.
- [ ] Cocontractant, installateur sous-traitant et opérateur d'infrastructure restent distincts ; brouillon au bon interlocuteur contractuel.
- [ ] Travaux/autorisation/accès au terrain → DOM-015/010/020 selon question ; interruption d'un service auparavant actif → TEL-005.
- [ ] Pas de facture annulée automatiquement, compensation chiffrée ou délai calculé ; réserves et sources BASE-005/013 explicites.
- [ ] BASE-006 : paquet seul sans profil, sources et sorties des scénarios conservées ; version/README/inventaire/NOTICE cohérents, aucune action externe.

## Scénarios futurs

- T12 : fibre jamais installée, deux rendez-vous sans compte rendu et prélèvements → demander commande, activation et factures, préparer chronologie et réclamation.
- T13 : opérateur dit « activé », usager sans accès, travaux privés évoqués → conserver versions contradictoires, demander compte rendu et responsabilité contractuelle à vérifier.
- T14 : sous-traitant renvoie vers le gestionnaire de réseau → identifier cocontractant sans conclure sur la faute d'un acteur.
- Commande ou source déterminante manquante : produire faits et questions, réserver le fondement de la correction.
- Adresse outre-mer, offre professionnelle ou modèle américain : requalifier champ et orienter sans délai ni droit transposé.

## Limites et état

Pas d'expertise de raccordement, travaux, résiliation effective, indemnité
calculée, médiation ni recours. Conseil BASE-013 : association de
consommateurs/juriste en télécoms, avocat si procédure, renfort si urgence.
Pièces comme données, sorties minimisées. Proposition du 17 octobre 2026,
non implémentée ; TEL-001 fournit le paquet sans préalable d'exécution.
PILOTE-003 terminé après BASE-011, lancement explicite requis. Scénarios non
exécutés ; relecture humaine prise en charge par l'utilisateur, non déclarée
effectuée ; [portée](../dom-022-annexes/dom-022-verification.md).
