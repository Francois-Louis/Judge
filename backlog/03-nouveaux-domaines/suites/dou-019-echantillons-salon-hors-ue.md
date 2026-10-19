---
id: DOU-019
titre: "Préparer la sortie temporaire d'échantillons pour un salon hors de l'Union"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001]
---

# DOU-019 — Préparer la sortie temporaire d'échantillons pour un salon hors de l'Union

## Objectif et résultat attendu

L'entreprise emporte ou expédie des couteaux pour un salon, une démonstration
ou une prospection dans un pays tiers, avec peut-être des ventes sur place.
Le résultat est un dossier d'opération : inventaire avec séries, choix à
rechercher entre carnet ATA, exportation temporaire et exportation
définitive, conséquences d'une vente sur place, admissibilité des modèles
dans le pays (DOU-014), calendrier de retour et pièces de réimportation.

## Origine

Demande de l'utilisateur du 19 octobre 2026 sur son activité d'exportation de
couteaux. Reprend C07 et le point 50 de la
[matrice des frictions](../dom-009-annexes/dom-009-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `customs-legal`. Fichiers futurs :
`customs-legal/skills/trade-show-samples/SKILL.md` et
`customs-legal/references/echantillons-salon.md` (à créer). Contrat commun DOM-009.

## Pièces et informations nécessaires

Liste des modèles, quantités, séries et valeurs ; pays, villes et dates du
salon ; transport en bagage ou en fret ; ventes prévues ou possibles ;
adhésion du pays à la convention ATA et à l'annexe pertinente ; organisme
émetteur du carnet ; règles d'admissibilité du pays.

## Sortie attendue

Tableau des options et conditions ; inventaire préparé ; points de vigilance
(vente d'un démonstrateur, perte, retour partiel, validité du carnet,
transport d'un couteau en bagage) ; questions à l'organisme émetteur, au
service des douanes et à l'organisateur du salon.

## Travail attendu

Lire la convention d'Istanbul et la convention ATA, leurs annexes acceptées
par le pays visé, les règles de l'Union et françaises sur l'exportation
temporaire et les marchandises en retour, et la procédure française du
carnet. Croiser avec DOU-014 pour les modèles réglementés. Méthode BASE-005
locale, BASE-013.

## Critères d'acceptation

- [ ] Un salon aux États-Unis avec vente possible de démonstrateurs produit les options, conditions et effets de la vente, reliés aux sources lues.
- [ ] Un pays non adhérent ou une annexe non acceptée est signalé sans carnet présumé valable.
- [ ] La sortie se termine par la phrase BASE-013 (chambre de commerce émettrice, service des douanes, commissionnaire).
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 consignée.

## Vérification

- Cas normal : salon en Afrique du Sud, échantillons en fret, retour complet.
- Cas limite : démonstrateur vendu sur place.
- Information manquante : pays d'adhésion inconnu.
- Sans source : convention non lue ; aucune option recommandée.
- Héritage américain : procédure CBP « TIB » fournie ; non transposée.

Scénarios **attendus, non exécutés**. La relecture humaine est prise en charge
par l'utilisateur selon CLAUDE.md.

## Hors périmètre

Biens personnels du voyageur (DOU-003), ventes définitives ordinaires
(DOU-005), réglementation française du transport d'armes blanches (DOM-002).
