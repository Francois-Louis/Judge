---
id: PDT-026
titre: "Déterminer si une entreprise est fabricant d'un emballage au sens du PPWR"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-024]
---

# PDT-026 — Déterminer si une entreprise est fabricant d'un emballage au sens du PPWR

## Objectif et résultat attendu

Un artisan ou une PME fait fabriquer par un fournisseur des boîtes, étuis
cartonnés ou calages à son nom ou à sa marque. Le résultat est une fiche de
rôle pour un emballage identifié : l'entreprise est-elle « fabricant » au sens
du règlement (UE) 2025/40 (PPWR), ou le fournisseur l'est-il au titre de
l'exception de la microentreprise ; et, si elle l'est, la liste des
obligations qui en découlent (évaluation de conformité, documentation
technique, déclaration UE de conformité, identification et coordonnées sur
l'emballage, conservation) avec les pièces à obtenir du fournisseur.

## Origine

Remarque de l'utilisateur du 19 octobre 2026, à la suite des stories export
de couteaux : « on est aussi emmerdé par la REP emballage et le PPWR ». Les
stories PDT-020 à PDT-025 couvrent la REP française, le marquage, la fiche
factuelle et le calendrier, mais pas la bascule de rôle provoquée par une
boîte personnalisée, ni les obligations documentaires applicables depuis le
12 août 2026.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant `judge-fr-eu-product-legal`.

- `product-legal/skills/fabricant-emballage-ppwr/SKILL.md` : skill à créer lors du lot.
- `product-legal/references/fabricant-emballage-ppwr.md` : référence métier à créer et embarquer.
- README, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Contrat de paquet autonome BASE-003, méthode locale BASE-005, stockage BASE-008.
Accepte la fiche PDT-024 ou un équivalent manuel avec provenance et manques.

## Entrées nécessaires

Emballage et version, qui le conçoit, qui le fabrique, sous quel nom ou marque
il est vendu, autres marques visibles, pays d'établissement du fournisseur et
de l'entreprise, taille de l'entreprise au regard de la définition de la
microentreprise (effectif, chiffre d'affaires ou bilan), date de première mise
sur le marché, attestations et fiches remises par le fournisseur.

## Travail attendu

- Appliquer la définition du fabricant (article 3, point 13) et son
  exception pour la microentreprise qui se fournit dans le même État membre,
  sans présumer la taille de l'entreprise.
- Pour le fabricant : article 15 (conformité aux articles 5 à 12, procédure de
  l'article 38, documentation technique de l'annexe VII, déclaration de
  l'article 39, conservation cinq ou dix ans, identification et coordonnées) ;
  distinguer exigences déjà applicables et exigences à date différée
  (PDT-025).
- Pour le fournisseur fabricant : liste des pièces à lui demander et des
  informations à lui transmettre.
- Séparer rôle PPWR (fabricant, importateur, distributeur) et rôle de
  producteur au titre de la REP (PDT-020, PDT-027).
- Ne rédiger aucune déclaration UE de conformité ni attester la conformité.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et
inconnue. Appliquer BASE-013 et BASE-014.

## Sources à rechercher

Règlement (UE) 2025/40, article 3 (définitions), articles 15 à 21, 38 et 39,
annexe VII, article 71 (application), dans leur version consolidée ;
recommandation 2003/361/CE (définition de la microentreprise) ; actes
d'exécution et lignes directrices de la Commission publiés ; éventuelles
mesures françaises d'application.

Lu le 19 octobre 2026 lors du découpage, sans valider l'implémentation, via
`scripts/legal_sources.py eu 32025R0040` (reproduction française actuelle,
statut documentaire non vérifié) : article 3, point 13 (fabricant, y compris
celui qui fait concevoir ou fabriquer sous son nom ou sa marque, et exception
de la microentreprise se fournissant dans le même État membre) ; article 15,
paragraphes 1 à 5 ; article 71 (applicable à partir du 12 août 2026).

## Critères d'acceptation

- [ ] Une PME qui commande des boîtes à son logo à un cartonnier français reçoit une qualification de rôle reliée à l'article 3, point 13, et la liste des obligations de l'article 15.
- [ ] Une microentreprise dans la même situation voit l'exception examinée et la question de taille posée, sans conclusion présumée.
- [ ] Un fournisseur établi dans un autre État membre change le résultat de l'exception et la sortie l'explique.
- [ ] Rôle PPWR et rôle REP restent distincts.
- [ ] La sortie se termine par la phrase BASE-013 (juriste ou avocat en droit de l'environnement, organisme d'évaluation, fournisseur) ; aucune conformité attestée.
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 et BASE-014 consignée.

## Scénarios de contrôle

- Cas normal : coutelier de douze salariés, boîtes cadeau à sa marque fabriquées en France.
- Cas limite : microentreprise, boîtes neutres achetées sur catalogue puis étiquetées à sa marque.
- Cas complémentaire : boîtes fabriquées en Chine et importées par l'entreprise : rôle d'importateur à examiner.
- Information manquante : effectif et chiffre d'affaires inconnus.
- Sans source : actes d'exécution non retrouvés ; obligations datées réservées.

Scénarios attendus, non exécutés. La relecture humaine est prise en charge par
l'utilisateur selon CLAUDE.md.

## Hors périmètre

Essais, évaluation de conformité réalisée, rédaction de la déclaration UE,
REP et éco-contribution (PDT-020, PDT-021, PDT-027), marquage de tri (PDT-023).
