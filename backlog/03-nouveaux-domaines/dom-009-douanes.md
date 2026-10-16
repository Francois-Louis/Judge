---
id: DOM-009
titre: "Cadrer un plugin douanes et import-export"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-009 — Cadrer un plugin douanes et import-export

## Objectif

Organiser les tâches douanières autour de la marchandise, du territoire et de l'opération.

Nom de plugin proposé : `customs-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Particulier/professionnel, voyageur/vente/importation commerciale, territoires douanier et fiscal, origine, provenance, valeur et usage.
- Tâches candidates : préparation documentaire, qualification d'une importation, lecture d'un contrôle ou avis, demande de remboursement/remise.
- Séparer classement/origine/valeur, formalités, dette et sanction ; expliciter les inconnues qui empêchent un taux ou un montant fiable.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des douanes français et de l'Union, actes associés, Douane française, TARIC et Access2Markets selon le besoin.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de préparation documentaire d'une opération bornée, sans calcul de droits sans données vérifiées.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un achat expédié depuis un pays tiers.
- Un envoi vers un territoire ultramarin.
- Un avis de contrôle ou de perception déjà notifié.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Complément des frictions véhicules — 16 octobre 2026

Points 45 et 191. Prévoir la qualification documentaire de l'importation d'un véhicule de particulier, en distinguant achat dans l'Union et provenance d'un pays tiers, territoires douanier/fiscal, origine, provenance, résidence, usage et éventuel transfert de résidence. Recueillir factures, documents étrangers et douaniers, trajet, vendeur/mandataire et date ; sortie attendue : pièces manquantes et questions à la douane, sans taux ni droit calculé. Le document douanier ne remplace ni quitus fiscal DOM-011 ni immatriculation DOM-010 ; VEH-019 garde l'engagement contractuel de remise. Cas à découper : achat UE pris à tort pour import tiers ; véhicule tiers sans justificatif de dédouanement ; demande de franchise alléguée. Lire sources officielles et textes selon opération, sans transformer le guide en liste universelle de formalités.

Exigences de la [matrice des 195 points](dom-023-annexes/dom-023-frictions-utilisateurs.md), à découper sans sélection de tranche. Sources et scénarios métier non vérifiés ; [portée de l’intégration](dom-023-annexes/dom-023-frictions-verification.md).
