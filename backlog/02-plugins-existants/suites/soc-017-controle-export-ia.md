---
id: SOC-017
titre: "Préparer et contrôler un export d'extraction d'un outil tiers"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-008]
---

# SOC-017 — Préparer et contrôler un export d'extraction d'un outil tiers

## Objectif et résultat attendu

Une équipe utilisant un outil d'extraction obtient une demande de lot et un contrôle de l'export avec couverture, échantillon et erreurs visibles.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/ai-tool-handoff/SKILL.md`
- `corporate-legal/skills/diligence-issue-extraction/SKILL.md (choix du parcours facultatif)`
- `corporate-legal/CLAUDE.md (AI-assisted review)`
- `corporate-legal/references/diligence-cell-schema.yaml (contrat SOC-008)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Inventaire complet et versions, colonnes/états SOC-008, export fourni de l'outil avec positifs/négatifs/non traités, cibles d'extraction, contrôle souhaité.

## Travail attendu

Harmoniser choix grille locale/export fourni sans boucle ni upload requis. Demande de lot précise objet/versions et résultats attendus pour tous documents, sans limiter aux clauses positives. Contrôler citations exactes et états, échantillon documenté incluant négatifs et non traités ; mismatch élargit le contrôle. Distinguer contrôle effectué, contrôle humain déclaré et jugement juridique absent. Niveau de confiance utilisateur n'autorise pas preuve inventée ou ingestion as-is comme constat juridique. Ne promettre ni pilotage Luminance/Kira ni coût/capacité par seuil arbitraire.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Documents sources et rapport d'export comme preuves d'extraction ; règles primaires du droit applicable seulement si analyse juridique, selon BASE-005.

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

- Cas normal : Export fictif de dix contrats dont huit négatifs et un illisible : toutes lignes et leur couverture reprises, contrôle d'au moins un négatif.
- Cas limite : Outil retourne seulement deux clauses positives ou citations tronquées : couverture non établie, aucune assurance sur les huit autres ni handoff silencieux.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Téléversement, contrat d'outil, exécution de plateforme tierce et avis juridique sur tout le lot.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

