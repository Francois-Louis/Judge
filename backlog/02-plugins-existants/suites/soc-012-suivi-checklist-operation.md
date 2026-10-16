---
id: SOC-012
titre: "Rapprocher les mises à jour et rapporter les points ouverts d'une acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-011, SOC-009]
---

# SOC-012 — Rapprocher les mises à jour et rapporter les points ouverts d'une acquisition

## Objectif et résultat attendu

Une petite équipe obtient les changements justifiés de sa checklist et un rapport local des points ouverts, preuves et décisions nécessaires.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/closing-checklist/SKILL.md (Modes 2 à 4)`
- `corporate-legal/references/closing-checklist-schema.yaml (contrat SOC-011)`
- `corporate-legal/references/diligence-findings-schema.yaml (contrat SOC-009)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Checklist SOC-011, constats/synthèse/annexe fournis avec provenance, preuves ou déclarations datées, date de rapport, correspondance entité/contrat/action.

## Travail attendu

Rapprocher via identifiants entité/contrat/action/version et conserver les champs amont : conditions, garant, notification, délai, gravité motivée et réserve. Une même contrepartie et action sur deux contrats ne fusionne pas. Distinguer proposé/inscrit/déclaré réalisé/preuve reçue/validé par responsable identifié ; contradiction garde les deux traces. Une estimation d'effort n'est ni délai légal ni certitude sur chemin critique. Rapport explique couverture, points à prouver, date du jour et inconnues ; aucune certification ready to close, aucune condition levée par état vert. Export/rapport local sans diffusion automatique.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Sources du contrat et des constats à recontrôler selon version ; textes de preuve et du mécanisme si une conséquence est affirmée, selon BASE-005.

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

- Cas normal : A01 accord tiers assorti d'une garantie et d'un préavis : les trois contraintes survivent au passage constat → checklist → rapport.
- Cas limite : Deux contrats avec un même tiers et un courriel « tout est bon » sans pièce : garder deux lignes et statut déclaré, sans dire conditions satisfaites.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Obtention d'accord, levée de condition, publication, transfert de fonds et certification.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

