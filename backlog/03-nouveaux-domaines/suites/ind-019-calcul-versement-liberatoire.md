---
id: IND-019
titre: "Vérifier un versement libératoire pour une période"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-039, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, BASE-014, BASE-019, IND-001, IND-018]
---

# IND-019 — Vérifier un versement libératoire pour une période

## Objectif et résultat attendu

Calcul reproductible d'un versement de l'activité et rapprochement avec le relevé.

## Périmètre et fichiers

Plugin principal proposé : `self-employed-legal` (`judge-fr-eu-self-employed-legal`).
Skill proposé : `discharge-tax-period-calculation` ; ces noms ne désignent pas une commande disponible.

- `self-employed-legal/skills/discharge-tax-period-calculation/SKILL.md` (à créer)
- `self-employed-legal/references/calcul-versement-liberatoire.md` (à créer : méthode métier, sources/version et modèle de sortie)

Le socle et `references/qualification-independant.md` proviennent d'IND-001,
dont cette story dépend. Chaque lot met à jour README, manifeste/version,
NOTICE local/racine et métadonnées synchronisées selon CLAUDE.md.

## Pièces et informations nécessaires

Option établie, période, CA encaissé par activité, taux sourcés, relevé et dates.
Collecte minimale, données inutiles masquées ; distinguer document, fait déclaré
et inconnu. Ne pas demander d'identifiants de connexion ni de dossier complet
à un autre organisme pour poursuivre une question bornée.

## Travail attendu et sortie

Lire assiette, catégories, taux, arrondis et version ; calcul distinct des cotisations, de l'impôt du foyer et d'une comparaison de statuts. Paramètre manquant = montant réservé.

Produire : résumé en langage courant, faits/pièces et chronologie, tableau
propre au résultat annoncé, incertitudes, prochaine étape et destinataire.
Les montants recopiés portent leur provenance ; un calcul éventuel porte
sa formule, ses paramètres sourcés et sa date. Aucun montant juridiquement dû
ni calendrier n'est confirmé si un fait ou une source déterminante manque.

## Références métier à vérifier

CGI et textes applicables au versement libératoire ; paramètres officiels datés.

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

- Cas normal : CA ventilé et option valide : lignes d'impôt séparées des cotisations et écart expliqué.
- Cas limite : Activité mal classée ou période d'option inconnue : pas de taux par défaut.
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

Proposition du 17 octobre 2026 issue de DOM-039, rang 4 dans le
[découpage](../dom-039-annexes/dom-039-decoupage-independants.md).
PILOTE-003 est terminé après BASE-011 ; aucune tranche n'est sélectionnée
et aucune implémentation n'est lancée par ce cadrage.
