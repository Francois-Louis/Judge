---
id: CONSO-014
titre: "Préparer une réclamation de consommation dans un secteur sans plugin disponible"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-014 — Préparer une réclamation de consommation dans un secteur sans plugin disponible

## Objectif et résultat attendu

Une personne en litige avec un professionnel d'un secteur dont le plugin
n'est pas encore disponible (box internet, énergie, travaux, véhicule,
funéraire) obtient une réclamation fondée sur les règles générales de la
consommation, avec l'annonce claire des règles sectorielles non examinées.
Décision du 16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `consumer-legal/skills/general-consumer-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/regles-generales.md` — règles générales mobilisables, secteurs et règles non couvertes, sources lues (à créer)
- `consumer-legal/references/orientation-consommation.md` — état des plugins sectoriels, mis à jour à chaque lot
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Contrat, devis ou conditions ; factures ; échanges ; faits datés ; demande de
la personne ; secteur et professionnel concernés.

## Sortie attendue

Bandeau en tête : secteur identifié, plugin du secteur non disponible, règles
sectorielles non examinées. Puis fiche, règles générales applicables à
vérifier, brouillon de réclamation, médiateur à identifier (sectoriel s'il
existe), limites.

## Travail attendu

Vérifier d'abord dans `orientation-consommation.md` si le plugin du secteur
est livré : s'il l'est, orienter vers lui sans traiter. Ne pas présenter les
règles générales comme suffisantes ni deviner une règle sectorielle. Un
médiateur sectoriel identifié prime sur un médiateur générique.

## Références métier et sources à rechercher

Code de la consommation, règles générales (information, clauses abusives,
exécution, médiation) ; Code civil, inexécution. Sources sectorielles
seulement pour signaler leur existence, sans les appliquer.

## Critères d'acceptation

- [ ] G01 prépare la réclamation avec le bandeau des règles sectorielles non examinées.
- [ ] G02 oriente vers le plugin du secteur quand il est disponible, sans traiter.
- [ ] Aucune règle sectorielle appliquée sans lecture.

## Vérification

- Cas normal : G01 — Frais de résiliation d'une box internet contestés ; plugin télécoms non disponible.
- Cas limite : G02 — Même dossier après livraison du plugin télécoms.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Analyse sectorielle, saisine du médiateur, procédure, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-001-decoupage-consommation.md).
