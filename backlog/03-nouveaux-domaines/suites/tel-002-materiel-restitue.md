---
id: TEL-002
titre: "Préparer une contestation de matériel télécoms facturé après retour"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-002 — Préparer une contestation de matériel télécoms facturé après retour

## Objectif et périmètre

Un particulier prépare sa réclamation pour une box ou des accessoires
facturés alors qu'il déclare les avoir rendus. Abonnement grand public en
France métropolitaine, un retour et une facture identifiés. Plugin futur
`telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).
TEL-001 fournit le paquet, sans obligation d'exécuter son skill.

## Entrées et pièces

Titulaire et opérateur facturant, contrat et inventaire, consignes et
étiquette de retour, dépôt, poids si disponible, suivi et réception, preuve
du contenu et accusé de l'opérateur, numéro utile masqué, facture, échanges.
Ne pas exiger de preuve impossible à reconstituer : conserver l'inconnue.

## Sortie attendue

Tableau équipement attendu/déclaré rendu/preuve de dépôt/preuve de réception/
contenu reconnu/ligne facturée ; chronologie et brouillon demandant
rapprochement ou correction. Une preuve de réception d'un colis ne valide
pas automatiquement son contenu ; une affirmation de l'opérateur n'est pas
prise pour une preuve définitive d'absence ou de dommage.

## Travail et références métier

Créer `skills/equipment-return-complaint/SKILL.md` et
`references/materiel-restitue.md` dans le plugin ; charger qualification,
référence et copie locale BASE-005 ; mettre à jour README, version,
inventaire attendu et NOTICE. Références à ouvrir : contrat et modalités
datées de retour, Code de la consommation/CPCE selon poste facturé, Code
civil selon preuve et obligation, guides officiels de réclamation utiles.
Pistes **non consultées par DOM-022**, aucun délai ni barème vérifié.

## Critères d'acceptation

- [ ] T06 distingue dépôt, réception et contenu ; accessoires ou appareil manquants restent des questions, sans tort présumé.
- [ ] Les frais de rupture → TEL-001, une perte de retour par le prestataire → TEL-006 après qualification du contrat postal ; aucune responsabilité automatique de l'usager.
- [ ] Sources/version, exceptions et pièces sont tracées selon BASE-005 ; source absente : conclusion réservée et fiche utile.
- [ ] BASE-006 inclut paquet seul sans profil, invocation client et sorties des scénarios ; version/README/inventaire/NOTICE cohérents.
- [ ] BASE-013 nomme association de consommateurs ou juriste en télécoms, avocat si procédure ; renfort si acte ou échéance, aucune démarche externe.

## Scénarios futurs

- T06 : box facturée, récépissé et suivi livré → rapprocher dates/référence et demander reconnaissance du contenu, sans remboursement acquis.
- T07 : box reconnue reçue mais accessoire contesté → isoler l'accessoire, demander inventaire et motif, préserver le désaccord.
- T08 : colis de retour perdu, étiquette fournie par l'opérateur → demander qui a acheté la prestation et ses conditions ; TEL-006 pour la question distincte.
- Retirer la preuve de dépôt ou refuser l'accès à une source : poursuivre les faits, réserver la conclusion dépendante.
- Modifier territoire ou usage professionnel : requalifier et orienter ; modèle américain sans présomption ni délai transposé.

## Limites et état

Pas d'expertise du contenu, d'authentification du suivi, de barème, de montant
juridiquement dû, de délai calculé ou de remboursement promis. Aucun compte
consulté ni réclamation envoyée ; données minimisées, pièces non exécutables.
Proposition du 17 octobre 2026, scénarios non exécutés, aucune implémentation.
PILOTE-003 terminé après BASE-011, lancement explicite requis. Relecture
humaine prise en charge par l'utilisateur, non déclarée effectuée ;
[portée du cadrage](../dom-022-annexes/dom-022-verification.md).
