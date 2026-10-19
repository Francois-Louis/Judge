---
id: PDT-028
titre: "Ventiler les emballages déclarés entre France, Union et export"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-020, PDT-021]
---

# PDT-028 — Ventiler les emballages déclarés entre France, Union et export

## Objectif et résultat attendu

Une entreprise qui vend en France, dans d'autres États membres et hors de
l'Union déclare ses emballages à un éco-organisme français. Le résultat est
un tableau de ventilation pour une période : quantités par matériau et par
flux (France ménager, France professionnel, autres États membres, export
hors UE), règle de prise en compte de chaque flux dans la déclaration
française, pièces justificatives (factures, preuves de sortie, déclarations
étrangères) et écarts ou doublons à corriger, sans dépôt.

## Origine

Remarque de l'utilisateur du 19 octobre 2026 sur la REP emballages, dans le
contexte de ses exportations de couteaux. PDT-021 rapproche les pièces d'une
déclaration française, sans traiter la ventilation par destination d'un
exportateur.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant `judge-fr-eu-product-legal`.

- `product-legal/skills/ventiler-emballages-export/SKILL.md` : skill à créer lors du lot.
- `product-legal/references/ventilation-emballages-export.md` : méthode et modèle (à créer).

## Entrées nécessaires

Ventes par pays et canal, nomenclature d'emballage par produit, poids par
matériau, déclarations françaises antérieures, contrat et règles de
déclaration de l'éco-organisme, preuves d'exportation (DOU-005, DOU-013),
inscriptions à l'étranger (PDT-027), filières ménagère et professionnelle.

## Travail attendu

- Lire les dispositions françaises définissant le champ de la REP emballages
  ménagers et professionnels (code de l'environnement, cahiers des charges des
  filières) et les règles de déclaration de l'éco-organisme comme pièces
  contractuelles.
- Établir pour chaque flux s'il entre dans la déclaration française, et quelle
  preuve l'établit ; ne retrancher aucun flux sans source.
- Isoler les doublons possibles avec une déclaration étrangère et les
  régularisations à envisager.
- Calculer uniquement les lignes dont toutes les hypothèses sont documentées.

Appliquer BASE-013 et BASE-014.

## Sources à rechercher

Code de l'environnement, articles relatifs à la REP et aux filières emballages ;
arrêtés portant cahiers des charges des éco-organismes emballages ménagers et
emballages industriels et commerciaux ; règlement (UE) 2025/40, article 3,
point 15, et article 45 ; règles de déclaration de l'éco-organisme
contractant. Pistes non lues lors du découpage.

## Critères d'acceptation

- [ ] Une période avec ventes France, Allemagne et États-Unis produit un tableau reproductible par flux et matériau, avec la règle de prise en compte sourcée.
- [ ] Un flux export sans preuve de sortie reste en écart, sans retrait de la déclaration.
- [ ] Contribution, prix et régularisation contractuelle restent distincts.
- [ ] La sortie se termine par la phrase BASE-013 (éco-organisme, expert-comptable, juriste) ; aucune déclaration déposée.
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 et BASE-014 consignée.

## Scénarios de contrôle

- Cas normal : année avec 60 % de ventes France, 15 % UE, 25 % hors UE.
- Cas limite : emballages d'expédition achetés pour tous les flux sans ventilation.
- Information manquante : poids des calages inconnu.
- Sans source : règles de l'éco-organisme absentes ; ventilation conditionnelle.

Scénarios attendus, non exécutés. La relecture humaine est prise en charge par
l'utilisateur selon CLAUDE.md.

## Hors périmètre

Télédéclaration, paiement, contestation de facture d'éco-contribution
(COM-002/016), obligations dans les autres pays (PDT-027).
