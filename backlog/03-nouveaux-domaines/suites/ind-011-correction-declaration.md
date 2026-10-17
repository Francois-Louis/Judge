---
id: IND-011
titre: "Préparer une correction de déclaration sociale ciblée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-039, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, BASE-014, BASE-019, IND-001, IND-010]
---

# IND-011 — Préparer une correction de déclaration sociale ciblée

## Objectif et résultat attendu

Dossier de correction d'une déclaration identifiée et brouillon à l'Urssaf.

## Périmètre et fichiers

Plugin principal proposé : `self-employed-legal` (`judge-fr-eu-self-employed-legal`).
Skill proposé : `turnover-declaration-correction` ; ces noms ne désignent pas une commande disponible.

- `self-employed-legal/skills/turnover-declaration-correction/SKILL.md` (à créer)
- `self-employed-legal/references/correction-declaration.md` (à créer : méthode métier, sources/version et modèle de sortie)

Le socle et `references/qualification-independant.md` proviennent d'IND-001,
dont cette story dépend. Chaque lot met à jour README, manifeste/version,
NOTICE local/racine et métadonnées synchronisées selon CLAUDE.md.

## Pièces et informations nécessaires

Déclaration initiale, accusé, rapprochement des encaissements, anomalie précise, justificatifs, échanges et canal actuel.
Collecte minimale, données inutiles masquées ; distinguer document, fait déclaré
et inconnu. Ne pas demander d'identifiants de connexion ni de dossier complet
à un autre organisme pour poursuivre une question bornée.

## Travail attendu et sortie

Établir ancienne et nouvelle donnée proposée, preuve et période ; vérifier modalités, calendrier et conséquences sans écraser l'historique. Droit à l'erreur sans remise ni suspension promises.

Produire : résumé en langage courant, faits/pièces et chronologie, tableau
propre au résultat annoncé, incertitudes, prochaine étape et destinataire.
Les montants recopiés portent leur provenance ; un calcul éventuel porte
sa formule, ses paramètres sourcés et sa date. Aucun montant juridiquement dû
ni calendrier n'est confirmé si un fait ou une source déterminante manque.

## Références métier à vérifier

CSS et textes de régularisation du régime identifié ; procédure Urssaf officielle.

Pistes non ouvertes par DOM-039. Lors du lot, lire textes, champ, versions,
exceptions et transitions aux dates pertinentes ; distinguer guide, doctrine
et norme. Charger la copie locale BASE-005 alors en vigueur (actuellement
1.3.0) ; une décision citée est lue ou traitée selon la section 10 et BASE-019,
jamais restituée de mémoire. Relecture des sources livrées selon BASE-014.

## Critères d'acceptation

- [ ] Le cas normal produit le résultat annoncé et le cas limite réserve ou oriente la question dépendante.
- [ ] Le résultat distingue pièces, déclarations, montants recopiés, calculs sourcés et inconnues sans présumer une erreur de l'organisme ni garantir une issue.
- [ ] Le paquet extrait seul suit toutes ses références locales, sans profil ni autre plugin requis ; contrôles et scénarios BASE-006 consignés par couche.
- [ ] La sortie respecte BASE-013 : phrase finale avec professionnel nommé ; avocat en tête si acte, procédure ou délai incertain, expert-comptable pour les obligations comptables/fiscales. L'Urssaf ou le fisc restent les interlocuteurs du dossier, distincts du conseil.
- [ ] Les scénarios sont exécutés et leurs sorties conservées ; absence de source et de fait déterminant ne produit aucun droit, montant ou délai inventé.

## Vérification

- Cas normal : Encaissement omis avec justificatif retrouvé : tableau avant/après et brouillon de correction.
- Cas limite : Désaccord sur assiette ou mise en demeure : IND-034 distinct, correction seule ne vaut pas recours.
- Information manquante : retirer la preuve de réception ou une pièce déterminante ; inconnue visible, seule conclusion dépendante réservée.
- Source indisponible : poursuivre la fiche factuelle, tracer les accès tentés et réserver la règle dépendante.
- Transfrontalier : activité ou organisme hors France, territoire ultramarin ou opérations étrangères ; champ qualifié, aucune extension automatique du régime français.
- Héritage étranger : joindre un modèle américain ; aucune règle étrangère importée par traduction.

Scénarios **attendus, non exécutés**. Cette proposition ne prétend ni exécuter
un skill ni vérifier la compréhension d'un lecteur. La relecture des livrables
est prise en charge par l'utilisateur selon la décision du 17 octobre 2026 ;
elle n'est pas déclarée effectuée et ne dispense pas des tests techniques.

## Hors périmètre et état

Aucun envoi, dépôt, paiement, déclaration à la place de la personne, accès
aux comptes ni stockage durable de dossier. Les tâches voisines sont des
orientations avec question et pièces minimales, sans appel automatique ni
installation d'un complément absent. Pas de traitement du domaine entier.

Proposition du 17 octobre 2026 issue de DOM-039, rang 3 dans le
[découpage](../dom-039-annexes/dom-039-decoupage-independants.md).
PILOTE-003 est terminé après BASE-011 ; aucune tranche n'est sélectionnée
et aucune implémentation n'est lancée par ce cadrage.
