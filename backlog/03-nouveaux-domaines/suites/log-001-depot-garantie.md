---
id: LOG-001
titre: "Contester une retenue sur dépôt après une location privée vide"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# LOG-001 — Contester une retenue sur dépôt après une location privée vide

## Objectif et résultat attendu

L'ancien locataire comprend les postes retenus et prépare une demande au
bailleur, sans remboursement garanti. Cette première tranche crée
`housing-legal` avec son seul skill. Elle reprend la borne T4 d'USAGE-002.

## Périmètre et fichiers

Plugin principal : `housing-legal`, identifiant `judge-fr-eu-housing-legal`.
Location privée vide, résidence principale en France métropolitaine, régime
de la loi du 6 juillet 1989 confirmé ; départ et retenue déjà intervenus.

- `housing-legal/.claude-plugin/plugin.json` — manifeste initial `0.1.0` (à créer)
- `housing-legal/README.md` — tâche disponible, exclusions, installation seule (à créer)
- `housing-legal/CLAUDE.md` — modèle minimal, aucun profil obligatoire (à créer)
- `housing-legal/LICENSE` — copie de la licence (à créer)
- `housing-legal/NOTICE` — entrée datée (à créer)
- `housing-legal/references/shared/research-citation-method.md` — copie BASE-005 `1.0.0` identique, version à relire au lot (à créer)
- `housing-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `housing-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `housing-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `housing-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `housing-legal/references/qualification-logement.md` — qualification commune du découpage (à créer)
- `housing-legal/references/depot-garantie.md` — preuve, retenues, sources et versions (à créer)
- `housing-legal/skills/security-deposit-dispute/SKILL.md` — tâche (à créer)
- `housing-legal/skills/security-deposit-dispute/references/demande-restitution.md` — modèle (à créer)
- `.claude-plugin/marketplace.json` — entrée à la sélection explicite de cette tranche
- `scripts/test-base008-isolation.py` — décompte au même lot
- `NOTICE` — entrée racine de livraison

Pas de stockage durable ; les copies BASE-008 servent au contrat de paquet.
Les autres plugins sont des relais facultatifs, sans dépendance d'installation.

## Pièces et informations nécessaires

Bail et annexes utiles, qualité des parties, localisation, dates ; preuve du
versement du dépôt, états des lieux d'entrée et sortie disponibles, preuve de
remise des clés, décompte du bailleur, justificatifs, restitution et échanges.
Identifier pièce absente, signature contestée et simple déclaration. Masquer
coordonnées bancaires et identifiants inutiles.

## Sortie attendue

Résumé accessible ; régime confirmé ou réservé ; tableau dépôt versé,
restitution, retenue par poste, provenance, rapprochement entrée/sortie,
justificatif et question ; arithmétique reproductible distincte du droit ;
pièces manquantes et brouillon au bailleur ; interlocuteur et limites.

## Travail attendu

Appliquer la qualification du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).
Séparer dégradation alléguée, vétusté, nettoyage et autres dettes ; un devis
ne prouve pas à lui seul l'imputabilité. État des lieux absent ou contradictoire :
réserver les effets juridiques et préparer la demande de pièce, sans supposer
un état parfait. Charges à régulariser → LOG-002 comme tâche distincte ; acte
ou jugement → DOM-003. Aucun calcul de majoration ni de prescription.

## Références métier et sources à rechercher

Loi n° 89-462 du 6 juillet 1989, dépôt et champ du régime ; Code civil,
preuve et bail ; textes sur états des lieux, vétusté et réparations pour les
postes contestés ; ANIL/ADIL pour information. Ouvrir versions, transitions
et passages officiels lors du lot ; aucune règle tenue pour vérifiée ici.

## Critères d'acceptation

- [ ] D01 rapproche pièces et postes sans déduire une dette du seul devis.
- [ ] D02 demande l'état des lieux absent et réserve l'imputabilité.
- [ ] D03 oriente le meublé hors tranche ; D04 réserve toute règle sans source.
- [ ] Le paquet détaché puis installé seul fonctionne sans profil et sans connecteur ; références locales et sources effectivement lues sont tracées.
- [ ] Phrase finale d'information avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si acte, délai ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : D01 — Location vide privée terminée, deux états des lieux fournis, retenue peinture sur devis et restitution partielle ; tableau et demande ciblée sans remboursement promis.
- Cas limite : D02 — État d'entrée manquant et sortie contestée ; demander les pièces avant de qualifier la responsabilité.
- Cas limite : D03 — Même demande pour un meublé ; orientation et borne expliquée, sans appliquer le régime vide.
- Cas limite : D04 — Source inaccessible ; faits et questions conservés, aucune échéance ou majoration inventée.

Scénarios **attendus, non exécutés**. Exécuter fixtures, conserver sorties et
sources lues, puis appliquer les couches BASE-006 ; la relecture DOM-006
ne prouve pas le fonctionnement du futur skill.

## Hors périmètre

Meublé, mobilité, social/conventionné, saisonnier, résidence secondaire,
bail ancien spécial, sous-location, occupant sans bail, cautionnement,
dépôt avant départ, contentieux et envoi. Aucun profil imposé ni plugin vide.

## État de la proposition — 16 octobre 2026

Issue de DOM-006, sans sélection ni implémentation. PILOTE-003 terminé après
BASE-011 ; les limites de recette sont conservées dans son bilan.
