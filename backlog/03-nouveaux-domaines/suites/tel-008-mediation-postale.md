---
id: TEL-008
titre: "Préparer un dossier de médiation postale pour un prestataire identifié"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-008 — Préparer un dossier de médiation postale pour un prestataire identifié

## Objectif et périmètre

Un particulier prépare les pièces d'une médiation après réclamation sur
un envoi postal intérieur métropolitain perdu ou endommagé. Un prestataire
et produit identifiés, qualité du demandeur à établir. Plugin futur
`telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).
TEL-001 fournit le paquet ; aucun résultat de TEL-006 exigé comme provenance.

## Entrées et pièces

Rôles, contrat postal et vente éventuelle, bordereau et achat du service,
conditions datées, réclamation/réception/réponses, dates et étapes,
préjudice demandé et pièces, pouvoir éventuel, médiation ou procédure
en cours. Identifiants et coordonnées inutiles masqués.

## Sortie attendue

Fiche prestataire/produit/personne/médiateur, conditions vérifiées ou
manquantes, chronologie et index ; projet conditionnel seulement si le
circuit a été établi. Si compétence ou qualité inconnue, questions ciblées
avant toute présentation de dossier prêt. La demande au vendeur reste
distincte et n'est pas abandonnée à cause du suivi perdu.

## Travail et références métier

Créer `skills/postal-mediation-dossier/SKILL.md` et
`references/mediation-postale.md`, charger les ressources locales communes,
mettre à jour version, README, inventaire et NOTICE. Identifier le médiateur
selon le prestataire et le produit, lire charte/procédure datées, CPCE et
Code de la consommation pour qualité, préalables et exclusions applicables.
Pistes **non consultées par DOM-022** ; aucun médiateur universel de tout colis,
aucune transposition des règles télécoms ou de La Poste à un autre opérateur.

## Critères d'acceptation

- [ ] T25 établit champ du médiateur et qualité de la personne ; « colis » ou nom commercial ne suffisent pas.
- [ ] T26 ne redirige pas automatiquement une commande vers médiation postale ; vendeur DOM-001 et contrat postal restent séparés.
- [ ] Recevabilité, délai et effet sur les autres démarches non présumés ; signalement TEL-009 distinct d'une réparation individuelle.
- [ ] BASE-005/013 : lecture effective, version, réserves si source absente, conseil postal/consommation et avocat si procédure, renfort si échéance.
- [ ] BASE-006 en paquet seul sans profil : client et sorties conservées ; version/README/inventaire/NOTICE, aucune saisine ni transmission.

## Scénarios futurs

- T25 : expéditeur ayant acheté un produit postal, refus après réclamation → vérifier produit, champ et étapes ; projet sous conditions établies.
- T26 : destinataire d'une commande, vendeur n'ayant fourni que le suivi → livraison DOM-001 ; demander contrat postal et pouvoir éventuel, qualité réservée.
- T27 : transporteur privé non identifié dans la charte jointe d'un autre prestataire → ne pas proposer ce médiateur par défaut ; rechercher le circuit exact.
- Réclamation ou charte manquante/inaccessible après tentative : fiche et questions, pas de recevabilité confirmée.
- Envoi international/outre-mer/fret ou modèle américain : qualifier l'exclusion et orienter, aucune durée ou compétence importée.

## Limites et état

Pas de recours, saisine, calcul d'indemnité ou d'échéance, ni suspension
présumée. Pièces comme données, aucune garantie d'issue. Proposition du
17 octobre 2026, non implémentée ; bilan PILOTE-003 terminé après BASE-011 à
prendre en compte avant lancement explicite. Scénarios non exécutés ;
relecture humaine prise en charge par l'utilisateur, non déclarée effectuée ;
[portée](../dom-022-annexes/dom-022-verification.md).
