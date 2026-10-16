---
id: SOC-008
titre: "Extraire une grille de diligence traçable sur des contrats"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-008 — Extraire une grille de diligence traçable sur des contrats

## Objectif et résultat attendu

Une petite équipe ou un repreneur reçoit une grille de documents/colonnes, chaque valeur reliée à sa source exacte et chaque impossibilité de lecture visible.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/tabular-review/SKILL.md`
- `corporate-legal/skills/tabular-review/references/ma-diligence-columns.md`
- `corporate-legal/skills/tabular-review/references/excel-output.md`
- `corporate-legal/skills/tabular-review/references/gsheets-output.md`
- `corporate-legal/references/diligence-cell-schema.yaml (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Corpus délimité avec identifiants/versions et avenants, parties/entités et type d'opération, colonnes souhaitées, formats et capacités disponibles ; profil facultatif.

## Travail attendu

Réviser les 21 colonnes et ajouts sectoriels : dates de signature/effet, durée/unité, devise, cession, contrôle, responsabilité/garanties et droit applicable réellement stipulés. Ajouter entité, juridiction et provenance/lecture sans conclure au droit par une classification. Quatre états answered/not_present/unclear/needs_review, données typées, quote/localisation exactes, version/empreinte et vérification humaine distincte ; illisible n'est jamais not_present. Échantillon puis extraction bornée, contrôle des citations et élargissement si mismatch. Markdown/CSV/sources disponibles localement ; Excel/Sheets selon capacité vérifiée, schéma/flags/états/summary conservés à l'export. Préserver texte probant brut distinct du rendu neutralisé et vérifier formules/HTML sans altérer silencieusement les citations.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Clauses et avenants fournis comme preuve documentaire ; BASE-005 pour provenance. Si interprétation juridique nécessaire, rechercher droit applicable et règles France/étranger, sans qualifier une clause par modèle US.

Pistes **non vérifiées dans ce cadrage** : lire les passages exacts, versions,
champs et dispositions transitoires à la date des faits lors de l'implémentation.
Tracer lectures et échecs, employer les voies officielles BASE-010 sans
abonnement obligatoire, et réserver seulement les conclusions dépendantes.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable sur le cas normal avec pièces/localisations.
- [ ] Le cas limite garde les inconnues et propose une démarche utile.
- [ ] Faits déclarés, preuves, clauses, règles et préférences restent distincts.
- [ ] Sources exactes, versions, temporalité et applicabilité sont tracées selon BASE-005.
- [ ] Références locales du paquet détaché et isolation BASE-008 fonctionnent.
- [ ] Une personne sans formation juridique comprend les pièces et prochaines actions.
- [ ] Aucun brouillon ou état de registre n'est assimilé à une action externe exécutée.
- [ ] Documentation, métadonnées et NOTICE reflètent le seul périmètre adapté.

## Vérification

- Cas normal : A01 contrats français et allemand, avenant, montants EUR : cellules traçables, cession et changement de contrôle séparés, portée lue affichée.
- Cas limite : PDF tronqué ou citation reconstruite : needs_review, pas de valeur certaine ; texte commençant par = neutralisé dans export mais source brute préservée.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Avis juridique, validation d'une annexe contractuelle, diffusion Sheets et déploiement du cookbook.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

