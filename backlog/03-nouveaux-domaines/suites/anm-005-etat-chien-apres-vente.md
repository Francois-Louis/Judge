---
id: ANM-005
titre: "Préparer un dossier sur l'état allégué d'un chien après vente"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, ANM-001]
---

# ANM-005 — Préparer un dossier sur l'état allégué d'un chien après vente

## Objectif et résultat attendu

Un acquéreur particulier en France rassemble contrat, dates et pièces
vétérinaires strictement utiles après l'apparition d'un problème allégué chez
son chien. Il prépare des questions au vendeur et à son conseil sans recevoir
de diagnostic, d'affirmation de vice ou de promesse de remboursement.

## Périmètre et fichiers

Plugin principal : futur `animal-legal` (`judge-fr-eu-animal-legal`).
Vente d'un chien de compagnie par un professionnel ou un particulier,
conclue et remise en France ; un problème allégué identifié. Pas d'adoption
associative ni de régime général de garantie pour toutes les espèces.

- `animal-legal/skills/dog-sale-health-dispute-file/SKILL.md` (à créer).
- `animal-legal/references/etat-chien-apres-vente.md` (à créer).
- `animal-legal/references/qualification-animal.md` — créé par ANM-001, à relire.
- `animal-legal/README.md`, `animal-legal/NOTICE`, `NOTICE` — tâche et traçabilité.
- `animal-legal/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py` — version et métadonnées synchronisées.

Charger méthode locale BASE-005 et socle ; contrat de paquetage du
[découpage](../dom-033-annexes/dom-033-decoupage-animaux.md).

## Pièces et informations nécessaires

Annonce, promesses et contrat, qualité du vendeur, dates de vente/remise,
premiers signes déclarés, consultation et découverte, certificat/compte rendu
utile avec auteur/date, facture de soins, échanges et demandes déjà faites.
Distinguer observation de l'acquéreur et constat vétérinaire ; limiter les
pièces de santé à la question, sans analyser soi-même une image ou un examen.

## Sortie attendue

Chronologie attribuée aux pièces, tableau promesse / état allégué / constat /
inconnue, demandes de documents ou d'explication au vendeur, dossier pour
avocat ou juriste compétent. Chaque voie éventuelle reçoit ses conditions
et réserves seulement après lecture des sources ; aucune action choisie
automatiquement et aucun délai calculé dans cette tranche.

## Travail attendu

Qualifier d'abord animal, contrat, parties et dates. Rechercher séparément
régime rural des ventes d'animaux, éventuelle garantie civile, clause
conventionnelle et champ/exclusions de la consommation. Ne pas appliquer au
chien un tableau de garantie d'un objet courant. Ni proximité temporelle ni
facture vétérinaire ne prouvent seules antériorité, causalité ou faute.
Signaler rapidement l'enjeu possible de délais spécifiques sans attendre
le dossier complet ; soin nécessaire à discuter avec un vétérinaire.

## Références métier et sources à rechercher

Code rural et de la pêche maritime : garanties et vices rédhibitoires selon
espèce, conditions et procédure propres ; Code civil : garanties/preuve et
articulation contractuelle ; Code de la consommation : champ et exclusions
à la date de vente. Jurisprudence d'articulation à lire si invoquée. Pistes
non ouvertes dans DOM-033 : versions, déclencheurs, exceptions et transitions
à vérifier selon BASE-005 ; sources du lot relues selon BASE-014.

## Critères d'acceptation

- [ ] Le dossier distingue signes déclarés, constat vétérinaire et preuve juridique sans diagnostic ni causalité inventée.
- [ ] Chaque régime envisagé est qualifié ou réservé ; aucune garantie de bien courant appliquée par défaut ni liste de maladies reconstituée de mémoire.
- [ ] Les engagements des deux parties et les pièces contraires sont examinés ; aucune faute, résolution ou prise en charge des frais présumée.
- [ ] Les dates utiles et l'enjeu de vérification rapide sont visibles, sans délai générique ni calcul automatique.
- [ ] Le paquet autonome passe la recette BASE-006, dont absence de source ; références indispensables embarquées.
- [ ] Phrase BASE-013 avec avocat ou juriste compétent et renfort de tête sur délai possible ; vétérinaire nommé pour santé animale.
- [ ] Les décisions et textes sont lus ou leur statut limité est explicité selon BASE-005, jamais restitués de mémoire.

## Vérification

- Cas normal : consultation après remise, compte rendu et annonce disponibles : chronologie et questions, pas de défaut antérieur conclu.
- Cas limite : certificat sans date ou problème déjà mentionné au contrat : pièce insuffisante/contraire visible, aucune faute présumée.
- Cas limite : vendeur particulier et ancien modèle de garantie de téléphone joint : modèle écarté, régimes propres recherchés.
- Sans source : dossier factuel, enjeu de vérification rapide et conseil, aucune condition de garantie ni durée confirmée.

Scénarios **attendus, non exécutés** ; sorties, lectures et erreurs à conserver
selon BASE-006 et USAGE-001 `1.0.0`. Relecture par l'utilisateur ; aucune
compréhension attestée sans observation. Aucune tranche sélectionnée.

## Hors périmètre

Diagnostic, choix de soins, qualification de vice acquise, calcul de délai,
demande automatique de remboursement, expertise ou action judiciaire, envoi.
