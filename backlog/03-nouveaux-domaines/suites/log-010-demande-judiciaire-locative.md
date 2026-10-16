---
id: LOG-010
titre: "Préparer une demande judiciaire locative de délais et suspension de clause"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-009]
---

# LOG-010 — Préparer une demande judiciaire locative de délais et suspension de clause

## Objectif et résultat attendu

Dans une instance locative identifiée, le locataire prépare pour relecture
par son conseil un projet de demande de délais de paiement et, si applicable,
de suspension de clause. Bail privé vide de résidence principale, France
métropolitaine ; voie procédurale et compétence préalablement vérifiées.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/rent-relief-court-preparation/SKILL.md` — tâche (à créer)
- `housing-legal/references/demande-judiciaire-locative.md` — procédure choisie et sources (à créer)
- `housing-legal/skills/rent-relief-court-preparation/references/projet-demande.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Réutiliser conditions LOG-009, décompte LOG-008 et qualification LOG-001 ;
aucun plugin contentieux ou exécution obligatoire.

## Pièces et informations nécessaires

Pièces de LOG-009 strictement utiles et actualisées ; assignation complète,
juridiction, numéro de dossier, audience et preuve de notification, demandes
adverses, représentation connue, décisions déjà rendues et proposition
de paiement étayée. Ne pas déduire une capacité contributive de chiffres incomplets.

## Sortie attendue

Fiche de procédure et points réservés ; chronologie sourcée ; projet de
demande avec faits, conditions, arguments à vérifier et demandes distinctes ;
bordereau de pièces ; questions au conseil. Champs non établis visibles,
aucun dépôt ni décision promis.

## Travail attendu

Vérifier compétence, représentation, forme, stade et modalités de communication
avant de produire un projet procédural. Si l'une manque, limiter la sortie
au dossier de rendez-vous et aux questions. Ne pas convertir automatiquement
un courrier amiable en écrit judiciaire. Jugement ou commandement de quitter
les lieux : nouvelle qualification, acte et délais d'exécution → ENF-005 ;
aucun réexamen implicite d'une décision définitive. Ne pas demander le dossier
entier à un autre plugin pour rédiger.

## Références métier et sources à rechercher

Textes locatifs et conditions LOG-009, Code de procédure civile, Code de
l'organisation judiciaire, compétence et représentation du juge concerné,
communication et contradictoire, dispositions transitoires ; sources
officielles de la juridiction identifiée. Versions et textes lus traçables.

## Critères d'acceptation

- [ ] J01 rattache chaque fait et demande à une pièce ou condition lue, sans issue garantie.
- [ ] J02 bloque le projet procédural si compétence, voie ou stade restent inconnus ; dossier de rendez-vous maintenu.
- [ ] J03 sépare demande locative et délai d'expulsion après jugement ; aucun dépôt automatique.
- [ ] Recette BASE-006 avec paquet seul, sources locales et scénario sans source ; celui-ci ne produit pas de formulaire juridique rempli de mémoire.
- [ ] Renfort en tête avec urgence à vérifier et avocat en droit du logement ; phrase finale d'information selon BASE-013.

## Vérification

- Cas normal : J01 — Instance et audience documentées, décompte rapproché, pièces de ressources utiles ; projet pour relecture, sous réserve des vérifications officielles de procédure.
- Cas limite : J02 — Simple récit d'une audience, assignation absente ; questions au conseil, aucun acte prêt à déposer.
- Cas limite : J03 — Jugement d'expulsion déjà rendu ; qualifier la nouvelle demande et orienter l'exécution, sans promettre réouverture du fond.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006. Suite distincte exigée par les points
35–36 de la [matrice exécution](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

## Hors périmètre

Autres régimes locatifs, appel ou autre recours, contestation d'exécution,
demande de délai pour quitter, représentation, dépôt, signature et envoi.
