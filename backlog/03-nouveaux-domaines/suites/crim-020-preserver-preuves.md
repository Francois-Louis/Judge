---
id: CRIM-020
titre: "Préparer la conservation des preuves d'une intervention"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-020 — Préparer la conservation des preuves d'une intervention

## Objectif et résultat attendu

Une personne prépare un inventaire de preuves et des demandes urgentes de conservation après une intervention, sans modifier les originaux ni promettre leur obtention.

Besoin issu des points 49–53, 55–58, 80, 86–87, 96 de la [matrice des frictions](../dom-002-frictions-utilisateurs.md). Proposition documentaire, sans implémentation ni sélection.

## Périmètre et fichiers

- `criminal-legal/skills/intervention-evidence/SKILL.md` — le skill (à créer)
- `criminal-legal/references/preuves-intervention.md` — repères, modèles et sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit. Un relais vers une autre story est une orientation ; aucun autre plugin installé n'est requis.

## Pièces et informations nécessaires

Chronologie ; lieu ; unités ou identifiants visibles ; témoins et accord pour leurs coordonnées ; blessures et constats disponibles ; vidéos originales et copies ; caméras publiques, privées ou piétons possiblement présentes ; procédure et références connues ; risque de disparition. Ne pas exiger de données médicales complètes.

## Sortie attendue

Priorités de santé et de conservation ; tableau preuve, détenteur supposé, plage horaire, risque, original et copie, demande à préparer ; brouillon au détenteur ou au service compétent ; preuve d'envoi à conserver si l'utilisateur agit ; questions à l'avocat pour un versement à la procédure. Distinguer conservation, accès et communication, sans délai standard présumé.

## Travail attendu

Conserver les séquences avant et après les faits, métadonnées et versions originales sans recadrage destructif ; dater les notes contemporaines et séparer observations, souvenirs et hypothèses. Une caméra supposée ne prouve ni enregistrement ni disponibilité. Distinguer filmer, gêner une intervention, diffuser des images et saisie d'un appareil. Ne pas conseiller d'effacer une vidéo ni de récupérer matériellement un appareil saisi. Soins et constats médicaux selon l'urgence, sans diagnostic ni ITT inventée. CRIM-004 pour la plainte ; CRIM-021 pour les signalements ; DOM-035 pour le dommage civil.

Charger la méthode locale BASE-005. Séparer document lu, fait déclaré, règle vérifiée et inconnue. Aucun droit, aucune durée, aucun délai ni montant établi depuis le seul texte des frictions ; sans source, fournir les questions et pièces utiles.

## Références métier et sources à rechercher

CPP, administration de la preuve, réquisitions et saisies ; CSI et textes propres aux caméras selon le corps ; sources CNIL et officielles sur conservation et accès ; règles sur captation, diffusion, vie privée et protection de certains agents. Vérifier chaque détenteur et chaque durée.

## Critères d'acceptation

- [ ] E01 prépare une demande ciblée de conservation distincte d'un droit d'accès supposé.
- [ ] E02 conserve l'original et distingue diffusion et conservation.
- [ ] E03 ne recommande pas d'effacer ni de reprendre un appareil saisi.

## Vérification

- Cas normal : E01 — Caméra-piéton et commerce voisin auraient filmé des coups après le menottage.
- Cas limite : E02 — Seul un extrait monté circule ; la personne possède encore la vidéo complète.
- Cas limite : E03 — Un agent demande la suppression de la vidéo et conserve le téléphone.
- Sans source lue : questions, pièces et limites ; aucune règle suppléée par le texte utilisateur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Expertise forensique, diagnostic, qualification de violences, publication ou collecte auprès de tiers, demande envoyée, garantie de récupération.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur. Contrat commun : [découpage](../dom-002-decoupage-penal.md). Aucun fichier de plugin créé par cette intégration.
