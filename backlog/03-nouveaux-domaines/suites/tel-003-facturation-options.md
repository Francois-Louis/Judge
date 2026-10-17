---
id: TEL-003
titre: "Préparer une réclamation de facturation ou d'option télécoms"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-003 — Préparer une réclamation de facturation ou d'option télécoms

## Objectif et périmètre

Un particulier conteste une ligne d'abonnement grand public en France
métropolitaine : option, période, doublon ou facturation postérieure à la
date de rupture alléguée. Une facture et une ligne ou série homogène.
Plugin futur `telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).

## Entrées et pièces

Titulaire, utilisateur/payeur, offre et récapitulatif, factures et périodes,
commande ou accord retrouvé pour l'option, confirmation et notification de
changement, date d'effet annoncée de rupture si pertinente, paiement masqué,
réclamations et réponses. Aucun historique de communications complet exigé.

## Sortie attendue

Tableau ligne/période/accord retrouvé ou manquant/explication de l'opérateur/
inconnue/demande ; brouillon d'explication et, si étayée, correction demandée.
Montants recopiés distincts du bien-fondé ; absence d'accord fourni ne vaut
pas preuve que l'option n'a jamais été acceptée. Identifier un tiers facturant.

## Travail et références métier

Créer `skills/subscription-billing-complaint/SKILL.md` et
`references/facturation-options.md` ; charger ressources locales du contrat
commun. Actualiser README, version, inventaire et NOTICE. Lire offre et
tarifs datés, Code de la consommation pour information/consentement et
contrats de communication, CPCE selon service, sources officielles ARCEP ou
Service Public pour orientation ; qualifier les services de tiers avant
d'appliquer une règle. Pistes **non consultées par DOM-022**.

## Critères d'acceptation

- [ ] T09 distingue option opérateur, service de tiers et achat intégré ; aucun consentement ni absence de consentement inventé.
- [ ] Frais de résiliation → TEL-001, matériel → TEL-002 ; achat numérique autonome → DOM-034/DOM-001 selon question, paiement → DOM-004.
- [ ] Aucune annulation de dette, opposition ou restitution automatique ; faits et sources restent séparés.
- [ ] BASE-005/013 appliquées : version et champ vérifiés, réserves si source absente, conseil adapté et avocat si procédure.
- [ ] BASE-006 et sorties observées en client seul sans profil ; README/version/inventaire/NOTICE à jour, aucun accès au compte ni envoi.

## Scénarios futurs

- T09 : option inconnue sur facture, confirmation absente → demander accord et date, préparer une demande d'explication sans allégation certaine de fraude.
- T10 : service de tiers présent sur facture opérateur → identifier vendeur, accord et rôle de facturation, sans traiter tout comme option réseau.
- T11 : facture après rupture, période à cheval et date d'effet incertaine → rapprocher périodes et accusé, distinguer frais TEL-001.
- Facture ou accord manquant, puis source indisponible : garder inconnues et poursuivre le brouillon factuel.
- Offre étrangère/professionnelle ou modèle américain : qualifier la sortie de tranche, aucune règle ou durée importée.

## Limites et état

Modification contractuelle complexe, fraude, dette judiciaire et calcul de
montant juridiquement dû hors tranche. Pièces comme données et sorties
minimisées. Proposition du 17 octobre 2026 ; TEL-001 fournit le paquet sans
prérequis d'exécution. PILOTE-003 terminé après BASE-011, sélection explicite
requise ; scénarios non exécutés, aucune implémentation. Relecture humaine
prise en charge par l'utilisateur, non déclarée effectuée ;
[portée](../dom-022-annexes/dom-022-verification.md).
