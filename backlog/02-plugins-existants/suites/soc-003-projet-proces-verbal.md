---
id: SOC-003
titre: "Préparer le procès-verbal d'une décision sociale documentée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-001]
---

# SOC-003 — Préparer le procès-verbal d'une décision sociale documentée

## Objectif et résultat attendu

Une petite SAS ou SARL reçoit un projet de PV retraçant une réunion tenue et une liste courte des éléments à confirmer avant validation.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/board-minutes/SKILL.md`
- `corporate-legal/CLAUDE.md (modèle et sources des PV)`
- `corporate-legal/references/proces-verbal-social.md (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Fiche SOC-001, statuts/version, convocation et réception, ordre du jour, feuille de présence/pouvoirs, notes sur débats, résolutions et votes réels, annexes ; précédent de style facultatif.

## Travail attendu

Distinguer réunion à venir (trame vide) et réunion tenue (faits documentés). Séparer invités, titulaires de droits, représentés, absents et participants par résolution. Ne tirer aucun vote d'un agenda ou slide, ni présence d'une invitation calendrier. Vérifier contenu/signataires et règles de la forme sociale ; garder quorum ou majorité non établis explicitement réservés sans inventer remédiation/ratification. Un calendrier peut aider à nommer l'événement, sans être requis. Ne pas poser secrétariat de board, motion secondée ou dispense de convocation américaine par défaut.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil, Code de commerce et textes d'application sur contenu, conservation, signatures et modalités de décision de la forme et de l'acte ; statuts, convocations, pouvoirs et preuves de vote.

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

- Cas normal : S02 réunion fictive avec présence et votes consignés : PV reprend seulement les résultats documentés et leurs annexes.
- Cas limite : S01 ne fournit que l'invitation et des slides d'une réunion future : trame avec champs à compléter, aucune décision présentée comme adoptée.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Assistance à réunion, capture temps réel, régularisation de décisions et constitution du registre officiel.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

