---
id: CRIM-015
titre: "Faire le point après une interpellation"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-015 — Faire le point après une interpellation

## Objectif et résultat attendu

Une personne interpellée puis relâchée, ou un proche, comprend ce qui s'est
passé, les documents remis, le sort des objets retenus et la suite possible,
et prépare les questions à un avocat. Pendant une mesure en cours : CRIM-002.
Ajout du 16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/arrest-follow-up/SKILL.md` — le skill (à créer)
- `criminal-legal/references/interpellation.md` — mesures possibles, documents, restitution, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Récit daté ; lieu et service ; documents remis (procès-verbal, convocation,
inventaire d'objets) ; mesure annoncée ; blessures et certificats ; témoins.

## Sortie attendue

Chronologie ; mesure probable et documents qui la montrent ; suite possible
(convocation, poursuite, classement) à vérifier ; démarche de restitution à
vérifier ; questions à un avocat ; limites.

## Travail attendu

Violences alléguées lors de l'interpellation : récit factuel et canaux à
vérifier (plainte, inspection, Défenseur des droits), sans qualification.
Personne étrangère : question de séjour à DOM-028. Mineur : CRIM-011.

## Références métier et sources à rechercher

Code de procédure pénale, interpellation, garde à vue et restitution des
objets ; compétences du Défenseur des droits.

## Critères d'acceptation

- [ ] A01 produit chronologie, documents et questions sans qualification.
- [ ] A02 renvoie une mesure encore en cours vers CRIM-002.

## Vérification

- Cas normal : A01 — Interpellation à la sortie d'un bar, relâché après quelques heures, téléphone conservé.
- Cas limite : A02 — Message envoyé pendant que la personne est encore retenue.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Assistance pendant l'interpellation, plainte rédigée, défense au fond, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 31, 48–58, 85 et 96 de la [matrice](../dom-002-frictions-utilisateurs.md). Compléter par horaires des mesures successives, documents de saisie et scellés, effets personnels/inventaire, propos rapportés, constats médicaux et séquences vidéo complètes.

- [ ] A03 — Après blessures ou menottage, santé et preuves à conserver → CRIM-020 ; plainte → CRIM-004 ; signalement → CRIM-021. Ne pas attendre une identification complète de l'agent pour structurer les faits.
- [ ] A04 — Version du PV contestée ou allégation d'outrage/rébellion : séparer citations du document, faits déclarés, observations et pièces ; avocat, sans qualification ni fabrication d'une version. Présence dans une foule ≠ participation établie par le seul récit.

Scénarios **attendus, non exécutés** : coups allégués après maîtrise ; interpellation en manifestation sans acte individuel décrit ; téléphone retenu sans document. Perquisition domiciliaire → CRIM-019. Aucun retour automatique des objets promis.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-decoupage-penal.md).
