---
id: TEL-009
titre: "Préparer un signalement télécoms ou postal au régulateur"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-009 — Préparer un signalement télécoms ou postal au régulateur

## Objectif et périmètre

Un particulier prépare une alerte factuelle sur une prestation télécoms ou
postale en France métropolitaine, dans le champ d'un canal officiel vérifié.
Une situation et un prestataire identifiés. Plugin futur
`telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).

## Entrées et pièces

Service/produit, prestataire et rôle, lieux et dates, incident ou pratique
décrite sans qualification présumée, pièces utiles, démarches/réponses,
objectif de la personne : alerter, être remboursée, rétablir ou obtenir une
décision. Aucun accès au portail ou compte de l'usager.

## Sortie attendue

Fiche champ du canal vérifié/inconnu/hors champ, résumé factuel minimal et
liste des pièces utiles ; brouillon si canal approprié. Rubrique séparée
sur la demande individuelle : réclamation TEL-001 à TEL-006, médiation
TEL-007/008 ou orientation précise si tâche absente. Alerte jamais présentée
comme une décision d'indemniser ou comme une protection automatique d'un délai.

## Travail et références métier

Créer `skills/telecom-postal-regulator-report/SKILL.md` et
`references/signalement-regulateur.md`, charger qualification et méthode
locales, actualiser version, README, inventaire et NOTICE. Ouvrir ressources
officielles ARCEP sur mission, champ, fonctionnement et suites du canal,
CPCE et textes pertinents selon service ; distinguer information, alerte,
médiation et éventuelle procédure sectorielle spécifique hors tranche.
Pistes **non consultées par DOM-022** ; ne pas affirmer un effet du portail
depuis sa seule page d'accueil ni promettre une intervention individuelle.

## Critères d'acceptation

- [ ] T28 distingue demande de réparation et alerte ; le canal n'est jamais présenté comme arbitre automatique du litige.
- [ ] Champ et rôle du régulateur/canal vérifiés pour télécoms ou poste ; hors champ, réserve et relais précis plutôt que dépôt générique.
- [ ] Les démarches individuelles continuent d'être identifiées séparément ; aucune échéance réputée préservée par le signalement.
- [ ] BASE-005/013 : sources/version, réserves si absentes, conseil consommation/secteur et avocat si procédure, renfort si acte ou échéance.
- [ ] BASE-006 : paquet seul sans profil, invocation et sorties conservées ; version/README/inventaire/NOTICE cohérents, aucun signalement envoyé.

## Scénarios futurs

- T28 : usager veut « que l'ARCEP rembourse mes frais » → expliquer les objectifs distincts après lecture des missions ; réclamation individuelle et alerte factuelle séparées.
- T29 : répétition de rendez-vous fibre manqués → champ du canal à vérifier, faits datés, TEL-004 pour la prestation et facture.
- T30 : colis commandé non livré, demande de signalement contre le vendeur → DOM-001 pour la vente ; prestation postale et champ à établir, pas d'alerte présumée appropriée.
- Source de fonctionnement du canal indisponible : résumé factuel utile mais compétence et effets réservés ; ne pas inventer une procédure.
- Service étranger/professionnel/hors champ ou modèle américain : qualifier et orienter, pas d'autorité ni procédure importée.

## Limites et état

Aucun dépôt, demande de sanction, procédure de règlement de différend,
représentation, indemnité ou délai calculé. Pièces comme données, sorties
minimisées et aucune faute présumée. Proposition du 17 octobre 2026 ;
TEL-001 fournit le paquet sans invocation préalable. PILOTE-003 terminé après
BASE-011, sélection explicite requise, aucune implémentation. Scénarios non
exécutés ; relecture humaine prise en charge par l'utilisateur, non déclarée
effectuée ; [portée](../dom-022-annexes/dom-022-verification.md).
