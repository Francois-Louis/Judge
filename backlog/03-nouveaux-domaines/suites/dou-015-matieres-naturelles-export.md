---
id: DOU-015
titre: "Identifier les contrôles liés aux matières naturelles d'un couteau exporté"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001]
---

# DOU-015 — Identifier les contrôles liés aux matières naturelles d'un couteau exporté

## Objectif et résultat attendu

Un coutelier exporte un couteau dont le manche, les mitres, l'étui ou
l'emballage contiennent des matières naturelles (bois, corne, os, bois de
cerf, ivoire fossile, nacre, cuir, peau). Le résultat est une fiche
matière × trajet : identification de l'espèce ou de la matière, statut
CITES et règles de l'Union à l'export, exigences du pays de destination
(permis, biosécurité, interdictions locales de vente), documents à obtenir et
inconnues bloquantes.

## Origine

Demande de l'utilisateur du 19 octobre 2026 sur la vente de couteaux dans de
nombreux pays tiers. Reprend le candidat C22, le dossier K02 et le point 55 de
la [matrice des frictions](../dom-009-annexes/dom-009-frictions-utilisateurs.md),
avec DOM-014 pour la question sanitaire ou environnementale autonome.

## Périmètre et fichiers

Plugin principal : `customs-legal`. Fichiers futurs :
`customs-legal/skills/knife-materials-check/SKILL.md` et
`customs-legal/references/matieres-naturelles-export.md` (à créer), README et
NOTICE du lot. Le [contrat commun](../dom-009-annexes/dom-009-decoupage-douanes.md)
s'applique.

## Pièces et informations nécessaires

Nom commercial et nom scientifique de chaque matière, fournisseur, facture et
date d'acquisition, documents CITES ou certificats intra-UE reçus, traitement
(stabilisation, résine, teinture), quantité, pays de destination et trajet,
canal (B2B, B2C, cadeau), emballage en bois éventuel (C23 distinct).

## Sortie attendue

Tableau matière / identification prouvée ou alléguée / statut à l'export UE /
exigence à destination / document à obtenir / inconnue. Distinguer annexe
CITES, réglementation de l'Union (règlement (CE) n° 338/97 et règlement
d'application), dérogations éventuelles par annotation, règles nationales
plus strictes à destination (par exemple interdiction locale de vente de
l'ivoire fossile, biosécurité australienne ou néo-zélandaise pour bois, corne,
os et cuir). Questions au fournisseur, à l'autorité CITES française et au
service compétent du pays.

## Travail attendu

- Lire les annexes CITES et celles du règlement (CE) n° 338/97 en vigueur à la
  date de l'envoi, avec annotations ; vérifier en particulier les bois
  souvent utilisés en coutellerie (palissandres, ébènes, bois de fer) sans
  présumer leur inscription.
- Lire la procédure française de permis d'exportation CITES et l'autorité
  compétente actuelle.
- Rechercher pour les pays prioritaires de DOU-014 les exigences de
  biosécurité et d'interdiction locale, en commençant par l'Australie et les
  États-Unis.
- Ne déclencher aucune procédure CITES pour tout bois ou cuir ; ne déduire
  aucune exemption du nom commercial (« bois de rose », « ivoire de mammouth »).

Charger la méthode BASE-005 locale ; appliquer BASE-013 et BASE-014.

## Critères d'acceptation

- [ ] Un manche annoncé « ivoire de mammouth » sans preuve d'identification produit une inconnue bloquante et les règles à vérifier par destination, sans exemption présumée.
- [ ] Un manche en bois d'espèce inscrite à une annexe donne l'annexe, l'annotation applicable et le document à obtenir, chacun relié à la source lue.
- [ ] Biosécurité à destination et CITES sont présentées comme deux contrôles distincts.
- [ ] La sortie se termine par la phrase BASE-013 (autorité CITES, service vétérinaire ou phytosanitaire, avocat en droit de l'environnement selon le cas).
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 consignée.

## Vérification

- Cas normal : couteau à manche en corne de bovin vers l'Australie.
- Cas limite : manche en bois exotique au nom commercial seul.
- Cas complémentaire : ivoire fossile vers un État américain à interdiction locale.
- Information manquante : facture fournisseur absente ; demande ciblée.
- Sans source : annexes CITES inaccessibles ; aucune conclusion de statut.
- Héritage américain : modèle Lacey Act fourni ; non transposé à l'export UE.

Scénarios **attendus, non exécutés**. La relecture humaine est prise en charge
par l'utilisateur selon CLAUDE.md.

## Hors périmètre

Emballage bois et NIMP 15 (C23), admissibilité mécanique du couteau (DOU-014),
importation des matières premières dans l'UE, infraction ou saisie.
