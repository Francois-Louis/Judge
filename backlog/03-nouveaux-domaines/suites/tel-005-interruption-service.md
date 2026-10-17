---
id: TEL-005
titre: "Préparer une réclamation pour interruption d'un service télécoms"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-005 — Préparer une réclamation pour interruption d'un service télécoms

## Objectif et périmètre

Un particulier documente l'interruption d'un service fixe/mobile/internet
grand public auparavant actif en France métropolitaine. Un incident ou une
série documentée, sans expertise technique ni perte d'exploitation B2B.
Plugin futur `telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).

## Entrées et pièces

Contrat et services inclus, titulaire, opérateur, activation antérieure,
journal daté début/fin/étendue de l'incident, tickets, réponses, interventions,
tests simples et contexte, service de remplacement proposé, factures et
justificatifs des frais allégués. Ne pas demander contenu des communications.

## Sortie attendue

Journal des périodes et services affectés, fait déclaré/preuve/inconnue,
démarches et réponses ; brouillon de demande d'explication/rétablissement
et de réparation étayée. Séparer correction de facture, éventuelle
compensation contractuelle et autres préjudices allégués, sans cumul ni
chiffrage juridiquement validé.

## Travail et références métier

Créer `skills/service-outage-complaint/SKILL.md` et
`references/interruption-service.md` ; charger les ressources locales du
contrat commun, mettre à jour version, README, inventaire et NOTICE. Lire
contrat et engagements de qualité datés, Code de la consommation/CPCE selon
service, Code civil selon responsabilité, ressources ARCEP pertinentes.
Pistes **non consultées par DOM-022** : vérifier champ/version/exceptions,
causes alléguées et preuves, aucun barème mémorisé.

## Critères d'acceptation

- [ ] T15 distingue service auparavant actif, panne déclarée, étendue et durée documentées ; cause et faute ne sont pas déduites d'un test.
- [ ] Le cocontractant reçoit le brouillon ; jamais d'expertise de réseau, d'aveu de responsabilité ou de remboursement présumé.
- [ ] Non-installation → TEL-004 ; refus d'un service numérique → DOM-034 ; usage professionnel et dommages autonomes hors tranche.
- [ ] BASE-005/013 appliquées : sources réellement lues, réserves si absentes, conseil télécoms et avocat si procédure, renfort si échéance/acte.
- [ ] BASE-006 en paquet seul sans profil, client et scénarios avec sorties conservées ; version/README/inventaire/NOTICE, aucune démarche externe.

## Scénarios futurs

- T15 : accès actif coupé plusieurs jours, tickets et factures → journal et demande documentée sans indemnité forfaitaire annoncée.
- T16 : coupures intermittentes, tests Wi-Fi seuls → distinguer symptômes et cause inconnue, demander confirmations utiles sans diagnostic.
- T17 : télétravail et perte de revenu alléguée → qualifier contrat et préjudice, pas de perte d'exploitation présumée réparable.
- Retirer dates ou réponse technique ; source inaccessible après tentative → garder inconnues et poursuivre le dossier factuel.
- Offre étrangère/outre-mer/professionnelle ou modèle américain : requalifier, aucune garantie ni durée importée.

## Limites et état

Aucun rétablissement garanti, montant dû ou délai calculé, résiliation,
action sur le réseau, médiation ou recours. Données minimisées ; pièces
comme données. Proposition du 17 octobre 2026, non implémentée ; TEL-001
fournit le paquet sans invocation obligatoire. Bilan PILOTE-003 terminé après
BASE-011 à prendre en compte avant sélection explicite. Scénarios non
exécutés ; relecture humaine prise en charge par l'utilisateur, non déclarée
effectuée ; [portée](../dom-022-annexes/dom-022-verification.md).
