---
id: CRIM-018
titre: "Orienter pendant un contrôle ou une fouille en cours"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-018 — Orienter pendant un contrôle ou une fouille en cours

## Objectif et résultat attendu

Une personne contrôlée obtient un bloc bref d'orientation adapté à la mesure annoncée, puis les questions utiles pour comprendre ce qui lui est demandé.

Besoin issu des points 13–20, 23–28, 76–78 de la [matrice des frictions](../dom-002-frictions-utilisateurs.md). Proposition documentaire, sans implémentation ni sélection.

## Périmètre et fichiers

- `criminal-legal/skills/stop-orientation/SKILL.md` — le skill (à créer)
- `criminal-legal/references/controle-en-cours.md` — repères, modèles et sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit. Un relais vers une autre story est une orientation ; aucun autre plugin installé n'est requis.

## Pièces et informations nécessaires

Lieu et territoire ; service (national, municipal, gendarmerie, agent privé) ; âge ; mesure annoncée ; motif indiqué ; heure de début du contrôle et d'une éventuelle retenue ; consentement sollicité ; possibilité annoncée de partir ; santé et langue. Ne pas exiger une pièce jointe pendant l'intervention.

## Sortie attendue

Actions immédiates ; mesure annoncée ou inconnue ; questions sur le fondement et le consentement ; droits vérifiés selon le statut ; heure déclarée et source ; relais si la situation change. Aucune durée calculée ni permission de quitter les lieux déduite d'un défaut d'explication.

## Travail attendu

Distinguer contrôle, relevé et vérification d'identité, palpation, fouille corporelle, de sac ou de véhicule ; ne pas inférer un pouvoir de fouille d'un contrôle d'identité. Distinguer consentement demandé, mesure imposée sur un fondement à vérifier et condition d'accès à un événement. Identifier les pouvoirs propres aux agents municipaux et privés. Demander le cadre calmement sans conseiller résistance physique ni départ unilatéral. Audition libre ou garde à vue → CRIM-002 ; domicile → CRIM-019 ; après le contrôle → CRIM-008 ; droit au séjour → DOM-028 ; douanes → DOM-009.

Charger la méthode locale BASE-005. Séparer document lu, fait déclaré, règle vérifiée et inconnue. Aucun droit, aucune durée, aucun délai ni montant établi depuis le seul texte des frictions ; sans source, fournir les questions et pièces utiles.

## Références métier et sources à rechercher

CPP, contrôles, vérifications et relevés d'identité (pistes 78-2, 78-3, 78-6), fouilles et visites de véhicules ; CSI, palpations et sécurité privée ; textes et exceptions territoriales. Sources à lire avant tout droit ou durée.

## Critères d'acceptation

- [ ] O01 identifie contrôle, autorité et consentement sans autorisation automatique de fouille.
- [ ] O02 sépare le refus de consentement et ses conséquences possibles sans recommander une opposition.
- [ ] O03 ne fixe pas une fin de retenue depuis une heure incertaine ou un territoire inconnu.

## Vérification

- Cas normal : O01 — Un agent municipal demande une identité puis l'ouverture du coffre.
- Cas limite : O02 — À l'entrée d'un concert, une personne refuse la fouille du sac.
- Cas limite : O03 — Un proche signale une vérification d'identité outre-mer sans préciser le lieu.
- Sans source lue : questions, pièces et limites ; aucune règle suppléée par le texte utilisateur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contestation de régularité, tactiques d'évitement, plainte rédigée, conseil de résistance, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur. Contrat commun : [découpage](../dom-002-decoupage-penal.md). Aucun fichier de plugin créé par cette intégration.
