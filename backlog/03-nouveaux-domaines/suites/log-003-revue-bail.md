---
id: LOG-003
titre: "Relire un bail vide de résidence principale avant signature"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-003 — Relire un bail vide de résidence principale avant signature

## Objectif et résultat attendu

Un futur locataire comprend les engagements d'un projet de bail privé vide
en France métropolitaine et obtient des questions au bailleur avant signature.
La revue porte sur les clauses et annexes, sans audit de tout le logement.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/residential-lease-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/revue-bail-vide.md` — clauses, annexes, sources et réserves locales (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale fournie par LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Projet complet et annexes disponibles, date de signature envisagée, commune,
usage réel et qualité des parties ; clause de loyer/charges, dépôt et frais,
annonce si elle éclaire une contradiction. Aucun justificatif financier personnel requis.

## Sortie attendue

Résumé des engagements ; tableau clause/effet/source lue/question ou
proposition ; annexes absentes ; points territoriaux ou temporels réservés ;
questions au bailleur et prochaine étape avant signature.

## Travail attendu

Qualifier résidence principale, privé/vide et date avant toute analyse.
Repérer encadrement, diagnostics et clauses particulières à rechercher
localement ; sans texte local exact, réserver ces points, sans valider un
loyer. Cautionnement distinct à orienter ; justificatifs de candidature →
LOG-011 ; bail meublé ou commercial hors tranche. Une clause ne devient
pas valable du seul fait de sa signature.

## Références métier et sources à rechercher

Loi n° 89-462 du 6 juillet 1989, contrats types et annexes du régime vide,
Code civil, règles de frais et diagnostics ; textes locaux exacts si un
encadrement est allégué ; ANIL/ADIL. Versions, champ et transitions à ouvrir
lors du lot, sans validation générale de conformité.

## Critères d'acceptation

- [ ] B01 explique les clauses et demande les annexes utiles absentes.
- [ ] B02 réserve l'encadrement si la source locale manque ; B03 oriente le régime exclu.
- [ ] Sources locales chargées et paquet seul vérifiés selon BASE-006 ; absence de source explicitée dans la revue.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si signature imminente, délai ou procédure (BASE-013).

## Vérification

- Cas normal : B01 — Projet de bail vide et annexe manquante ; tableau accessible et questions avant signature.
- Cas limite : B02 — Annonce évoquant un encadrement sans arrêté fourni ni source accessible ; aucun loyer déclaré conforme.
- Cas limite : B03 — Bail meublé présenté comme vide ; relever la contradiction et réserver le régime.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Social/conventionné, meublé, commercial, saisonnier, cautionnement au fond,
calcul du loyer légal, négociation automatique, signature et envoi.

## Complément des frictions logement — 16 octobre 2026

Points 2, 4, 8 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

Durée courte : qualifier bailleur personne physique/morale et justification particulière avant d'expliquer la clause. Diagnostics : inventorier dates, versions, annexes, références vérifiables et cohérence sans certifier l'installation ni déclarer automatiquement le bail nul. Demander inventaire si le vide est contesté puis orienter LOG-021 ; les effets au fond d'un meublé ne sont pas absorbés par cette revue. Encadrement → LOG-013, surface → LOG-015, honoraires → LOG-016 ; la revue signale le besoin sans refaire ces tâches.

- [ ] Le scénario complémentaire produit les distinctions, pièces et réserves ci-dessous, dans la borne de la story.

Scénario **attendu, non exécuté** : Bail vide court, diagnostic périmé allégué et prélèvement imposé : restituer questions distinctes et annexes manquantes, sans validation générale de conformité.
Les montants et délais du texte utilisateur ne sont pas validés ; appliquer
les sources locales et la recette de la story avant toute livraison.
