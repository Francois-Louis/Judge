---
id: ANM-001
titre: "Lire les documents d'acquisition d'un chien en France"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013]
---

# ANM-001 — Lire les documents d'acquisition d'un chien en France

## Objectif et résultat attendu

À partir de « le vendeur ne m'a pas donné les papiers », un particulier
comprend son contrat de vente de chien de compagnie, les pièces à vérifier
et la question à poser au cédant. Première tranche proposée, sans lancement.

## Périmètre et fichiers

Plugin principal futur : `animal-legal` (`judge-fr-eu-animal-legal`).
Vente et remise en France, professionnel ou particulier identifié ; lecture
avant ou après signature, sans examen au fond d'une maladie contestée.

- `animal-legal/skills/dog-acquisition-document-review/SKILL.md` (à créer).
- `animal-legal/references/acquisition-chien-documents.md` (à créer).
- `animal-legal/references/qualification-animal.md` — socle du découpage (à créer).
- `animal-legal/.claude-plugin/plugin.json` — version initiale `0.1.0` (à créer).
- `animal-legal/README.md` et `animal-legal/CLAUDE.md` — tâche et modèle sans profil obligatoire (à créer).
- `animal-legal/references/shared/research-citation-method.md` — copie identique de BASE-005 (à créer).
- `animal-legal/references/isolation.md` et `animal-legal/scripts/judge_store.py` — copies identiques BASE-008 (à créer).
- `animal-legal/references/company-profile-template.md` et `animal-legal/references/dashboard-template.md` — copies BASE-008 (à créer).
- `animal-legal/LICENSE` et `animal-legal/NOTICE` (à créer).
- `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py`, `NOTICE` — inscription, décompte, version et traçabilité au seul lancement de cette tranche.

Le [découpage](../dom-033-annexes/dom-033-decoupage-animaux.md) fixe
l'autonomie, les frontières et le questionnaire à embarquer ; aucun lien vers
le backlog ne sera nécessaire à l'exécution du paquet.

## Pièces et informations nécessaires

Annonce, contrat/projet et conditions, prix et sommes versées, identité et
qualité déclarée du cédant, lieu/dates de signature et de remise, espèce/âge
déclarés, justificatif d'identification et documents effectivement reçus.
Demander seulement les passages utiles, avec données de tiers masquées.

## Sortie attendue

Résumé, tableau engagement du cédant / engagement de l'acquéreur / pièce /
inconnue, sommes prévues et versées sans solde dû présumé ; documents reçus,
documents dont l'exigibilité est vérifiée ou réservée ; brouillon de questions
au cédant et prochaine étape. Absence dans le dossier ne signifie pas refus
de remise ni manquement établi.

## Travail attendu

Charger méthode locale BASE-005 et qualification commune. Distinguer vente,
cession gratuite et adoption associative ; demander la qualité du vendeur
avant de choisir un régime. Vérifier les règles de cession du chien selon
date, âge et situation, sans liste universelle de documents. L'identification
ne tranche pas seule la propriété. État allégué → ANM-005 ; association →
ANM-002 ; espèce ou statut particulier → qualification avant conclusion.

## Références métier et sources à rechercher

Code rural et de la pêche maritime : cession de chiens, identification,
information et documents ; Code civil : contrat et preuve ; articulation avec
Code de la consommation selon parties et date. Ministère de l'Agriculture
et Service-Public comme guides distincts. Pistes non ouvertes dans DOM-033 :
textes exacts, versions, exceptions, transitions et jurisprudence à lire et
tracer selon BASE-005 ; relecture du lot selon BASE-014.

## Critères d'acceptation

- [ ] Le récit ordinaire aboutit à une lecture du contrat et à une demande de pièces ciblée, sans questionnaire juridique préalable.
- [ ] Qualité du cédant, dates, espèce, sommes et engagements des deux parties sont établis ou laissés conditionnels ; aucun remboursement promis.
- [ ] Le régime animal et ses documents sont vérifiés sans importer mécaniquement la garantie d'un bien courant ; aucun diagnostic vétérinaire.
- [ ] Les cas hors tranche sont orientés avec leur disponibilité réelle ; aucune commande proposée n'est annoncée utilisable.
- [ ] Le paquet fonctionne seul sans profil ni connecteur ; BASE-006 distingue structure, schéma, installation, exécution et compréhension observée.
- [ ] La phrase finale BASE-013 nomme avocat ou juriste compétent ; renfort de tête sur signature imminente, procédure ou échéance sensible.
- [ ] Les sources sont tracées avec version et statut ; toute décision est lue pendant la réponse ou présentée comme fiche/piste selon BASE-005, jamais restituée de mémoire.

## Vérification

- Cas normal : vente par un professionnel, contrat et facture fournis mais justificatif d'identification non fourni : qualifier le manque et préparer une demande sans conclure à une infraction.
- Cas limite : vente entre particuliers : aucune garantie de consommation présumée.
- Cas limite : « adoption » avec frais associatifs, chien annoncé d'une catégorie particulière ou remise depuis l'étranger : réserve et orientation explicites.
- Sans source : tableau factuel et questions utiles, aucune obligation documentaire ou délai confirmé depuis la mémoire.
- Sans profil/connecteur : lecture des seules pièces fournies et références locales dans le paquet isolé.

Scénarios **attendus, non exécutés**. À l'implémentation, conserver sorties,
ressources lues et erreurs ; vérifier USAGE-001 `1.0.0` et BASE-006. La
relecture revient à l'utilisateur ; ne déclarer aucune compréhension observée
sans résultat réel.

## Hors périmètre

Action en garantie, diagnostic, élevage pour l'activité, adoption associative,
pension, transport/importation, modification d'un registre ou envoi externe.

## État de la proposition — 17 octobre 2026

Issue de DOM-033 ; PILOTE-003 terminé après BASE-011, sans sélection de tranche.
