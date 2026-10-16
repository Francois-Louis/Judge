---
id: LOG-002
titre: "Comprendre une régularisation de charges et demander les justificatifs"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-002 — Comprendre une régularisation de charges et demander les justificatifs

## Objectif et résultat attendu

Le locataire distingue provisions, dépenses et solde réclamé, puis prépare
une demande de détail au bailleur. Location privée vide de résidence
principale, France métropolitaine, charges au réel seulement.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/rental-charge-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/charges-locatives.md` — catégories, période, répartition et sources (à créer)
- `housing-legal/skills/rental-charge-review/references/demande-justificatifs.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Réutiliser la qualification locale de LOG-001, sans autre plugin requis.

## Pièces et informations nécessaires

Bail, clause charges, décompte annuel et période, provisions effectivement
versées, détail par poste et clé de répartition, justificatifs disponibles,
échanges et qualité des parties. Absence de facture explicitée ; ne pas
demander des données sur les autres occupants.

## Sortie attendue

Tableau poste/période/dépense/provision/clé/justificatif/question ; écarts
arithmétiques reproductibles sans conclure à l'exigibilité ; demande au
bailleur de détail et des modalités de consultation ; limites.

## Travail attendu

Distinguer réel et forfait avant tout rapprochement. Relevé du syndic :
justificatif possible, pas preuve que toute charge du copropriétaire est
récupérable. Contrat direct fournisseur → DOM-021 ; appel au copropriétaire
→ DOM-018 ; dépôt → LOG-001. Ne pas conseiller d'arrêter de payer ni fixer
un délai de contestation depuis la mémoire.

## Références métier et sources à rechercher

Textes locatifs du régime choisi, décret n° 87-713, règles de justification,
répartition, régularisation et prescription ; textes de copropriété pour
lire les justificatifs seulement ; ANIL/ADIL. Vérifier champ, version,
exceptions et transitions selon période ; références métier embarquées.

## Critères d'acceptation

- [ ] C01 demande les justificatifs manquants sans déclarer toute la dette nulle.
- [ ] C02 sépare forfait et réel ; C03 ne transfère pas toutes les charges du syndic au locataire.
- [ ] Sans source : rapprochement factuel et questions, règle réservée ; paquet seul et références locales vérifiés selon BASE-006.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si acte, délai ou enjeu irréversible (BASE-013).

## Vérification

- Cas normal : C01 — Régularisation annuelle sans factures fournies ; tableau des pièces reçues et demande de consultation.
- Cas limite : C02 — Contrat mentionnant un forfait ; arrêter l'analyse au réel et demander la qualification appropriée.
- Cas limite : C03 — Relevé du syndic comprenant travaux et frais de gestion ; ne pas les qualifier récupérables sans texte lu.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Parc social/conventionné, meublé, forfait au fond, facture directe, assemblée
de copropriété, saisine et envoi. Aucun montant légal ni échéance non sourcés.
