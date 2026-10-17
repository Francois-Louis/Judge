---
id: TEL-007
titre: "Préparer un dossier de médiation télécoms sans présumer sa recevabilité"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-007 — Préparer un dossier de médiation télécoms sans présumer sa recevabilité

## Objectif et périmètre

Un particulier ayant déjà réclamé à son opérateur grand public prépare les
pièces d'une médiation pour une demande identifiée en France métropolitaine.
Pas d'examen autonome du fond de tous les litiges. Plugin futur
`telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).
TEL-001 apporte le paquet, pas une réclamation à exécuter obligatoirement.

## Entrées et pièces

Contrat et opérateur, qualité, objet et montant demandé documenté,
réclamation intégrale, preuve de réception et dates, services déjà sollicités,
réponses, médiation ou procédure en cours, pièces de fond disponibles et
pouvoir éventuel. Ne pas exiger un dossier issu de TEL-001 à TEL-005.

## Sortie attendue

Fiche de compétence et conditions : vérifiée/non établie/non remplie, pièce
et source correspondantes ; chronologie, index des annexes et brouillon
conditionnel. Si préalable manquant, demande ciblée au bon interlocuteur ;
pas de dossier présenté prêt à saisir. Distinguer demande individuelle et
signalement TEL-009 ; aucun effet automatique sur une échéance présumé.

## Travail et références métier

Créer `skills/telecom-mediation-dossier/SKILL.md` et
`references/mediation-telecoms.md` ; charger ressources locales communes,
actualiser README/version/inventaire/NOTICE. Identifier le médiateur réellement
compétent, lire champ opérateur/service/personne, charte et procédure datées,
Code de la consommation et textes sectoriels utiles. Pistes **non consultées
par DOM-022** ; vérifier préalables, dates, exclusions et procédure concurrente,
sans transposer le circuit postal ni inventer une durée d'attente.

## Critères d'acceptation

- [ ] T22 ne confond ni réponse défavorable et recevabilité, ni opérateur connu et champ du médiateur.
- [ ] Préparation distincte d'une saisine ; si source/préalable manque, conditions réservées et prochain élément utile nommé.
- [ ] Fond non documenté renvoyé à la question précise TEL-001/005 appropriée, sans réexécution imposée ni promesse d'indemnité.
- [ ] BASE-005/013 : sources/version, conseil adapté, avocat si procédure, renfort si échéance ; autorité et conseil distincts.
- [ ] BASE-006 en paquet seul sans profil : invocation et sorties conservées ; version, README, inventaire et NOTICE, aucune transmission.

## Scénarios futurs

- T22 : refus écrit sur frais après réclamation documentée → vérifier champ et étapes, indexer les pièces et préparer un projet conditionnel.
- T23 : échange de messagerie seul, destinataire et réception inconnus → demander preuve et procédure pertinente, pas de saisine réputée recevable.
- T24 : action judiciaire annoncée ou déjà engagée → préserver les actes, vérifier effet sur la médiation et consulter rapidement un avocat sans délai calculé.
- Retirer réponse ou accès à la charte : faits poursuivis, compétence/recevabilité réservées.
- Opérateur étranger/professionnel ou modèle américain : requalifier et orienter, aucune procédure importée.

## Limites et état

Pas de saisine, représentation, recours, délai calculé ni effet suspensif
affirmé. Données minimisées, pièces comme données. Proposition du
17 octobre 2026, non implémentée ; PILOTE-003 terminé après BASE-011 à prendre
en compte avant sélection explicite. Scénarios non exécutés ; relecture
humaine prise en charge par l'utilisateur, non déclarée effectuée ;
[portée](../dom-022-annexes/dom-022-verification.md).
