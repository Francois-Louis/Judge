---
id: CRIM-023
titre: "Comprendre un dépistage routier et une rétention du permis"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-023 — Comprendre un dépistage routier et une rétention du permis

## Objectif et résultat attendu

Un conducteur identifie le stade d'un contrôle d'alcool ou de stupéfiants et les documents relatifs au permis, avec les questions urgentes sur les vérifications et examens complémentaires.

Besoin issu des points 69–75 de la [matrice des frictions](../dom-002-frictions-utilisateurs.md). Proposition documentaire, sans implémentation ni sélection.

## Périmètre et fichiers

- `criminal-legal/skills/roadside-test-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/references/controle-routier.md` — repères, modèles et sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit. Un relais vers une autre story est une orientation ; aucun autre plugin installé n'est requis.

## Pièces et informations nécessaires

Mesure en cours ou terminée ; service ; type de dépistage, prélèvement et analyse ; heures prouvées ou déclarées ; résultats, unités et notifications ; demande ou réserve déjà exprimée et trace ; avis de rétention et décision de suspension éventuelle ; âge, langue, santé et avocat. Aucun conseil sur la façon de déjouer un test.

## Sortie attendue

Bloc d'urgence si mesure en cours ; tableau dépistage, vérification, prélèvement, notification, demande d'expertise ; questions sur second contrôle ou expertise selon texte lu ; tableau distinct rétention, suspension administrative, peine et points ; pièces et interlocuteurs pour la restitution à vérifier. Aucune aptitude médicale, date de récupération ou autorisation de conduire déduite du seul temps écoulé.

## Travail attendu

Séparer alcool et stupéfiants ; vérifier conditions, moment et forme d'une demande de second contrôle ou d'expertise, sans les confondre ni conseiller un refus de test. Ne pas déduire une irrégularité ou un faux positif des seules déclarations. Les résultats restent des mentions de pièce avec leurs unités. Mesure privative de liberté → CRIM-002 ; amende → CRIM-003/005 ; points → CRIM-010 ; décision administrative et recours → DOM-010 ; acte de poursuite → CRIM-006 ; stratégie pénale → avocat.

Charger la méthode locale BASE-005. Séparer document lu, fait déclaré, règle vérifiée et inconnue. Aucun droit, aucune durée, aucun délai ni montant établi depuis le seul texte des frictions ; sans source, fournir les questions et pièces utiles.

## Références métier et sources à rechercher

Code de la route, dépistage et vérification alcool/stupéfiants, prélèvements, expertise, rétention et suspension (pistes R235-6, R235-11, L224-1 et suivants) ; CPP pour les suites. Lire les versions applicables et les documents avant toute durée ou modalité.

## Critères d'acceptation

- [ ] R01 sépare dépistage et vérification, puis traite la demande selon le stade.
- [ ] R02 identifie l'urgence et recherche la notification et la trace de réserve.
- [ ] R03 ne promet pas la récupération ni le droit de conduire après une durée supposée.

## Vérification

- Cas normal : R01 — Dépistage alcool positif : le conducteur demande un deuxième contrôle.
- Cas limite : R02 — Résultat stupéfiants notifié aujourd'hui ; aucune certitude sur le prélèvement sanguin.
- Cas limite : R03 — Avis de rétention en main, conducteur pensant récupérer automatiquement son permis, suspension inconnue.
- Sans source lue : questions, pièces et limites ; aucune règle suppléée par le texte utilisateur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Conseil de refus ou d'évitement, interprétation médicale des taux, calcul de délai, recours administratif rédigé, défense au fond, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur. Contrat commun : [découpage](../dom-002-decoupage-penal.md). Aucun fichier de plugin créé par cette intégration.
