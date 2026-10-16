---
id: SOC-020
titre: "Créer le contexte isolé d'une acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-020 — Créer le contexte isolé d'une acquisition

## Objectif et résultat attendu

Un repreneur crée une fiche datée de son opération et sait quelles pièces et questions conditionnent les tâches suivantes.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/cold-start-interview/SKILL.md (--new-deal)`
- `corporate-legal/CLAUDE.md (contexte deal et priorité des données)`
- `corporate-legal/references/deal-context-template.md (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Code stable, acheteur/vendeur/cible et identifiants, formes/pays, côté du demandeur, type d'opération, phase et dates/preuves, corpus accessible, responsables connus et éventuel dossier actif.

## Travail attendu

Distinguer cession de titres/actifs/fusion à qualifier, signature/réalisation envisagée/prouvée, cible/filiales, parties et droit applicable des différents actes. Reprendre juste les préférences nécessaires, pas de questionnaire métier global imposé. Définir liaison explicite matter/deal et chemin canonique avant écriture, vérifier collision et préserver ancien contexte ; un actif incohérent n'autorise pas la lecture d'un autre dossier. Seuils/dates internes n'écrasent pas les clauses ou textes. Produire fiche préparatoire si pièces manquent ; l'initialisation ne crée aucune checklist ou conformité par anticipation.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Pièces et déclarations datées ; architecture BASE-003/008, méthode BASE-005. Qualification juridique de structure à rechercher avant analyse métier.

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

- Cas normal : A01 reprise d'une SAS avec filiale allemande : entités/phase et preuves distinguées, lien vers dossier choisi.
- Cas limite : Code réutilisé ou dossier actif B pendant demande A : pas d'écrasement ni mélange, demander le rattachement nécessaire en poursuivant la fiche non persistée.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Conseil de structuration, validation juridique du contrat et initialisation automatique des trackers.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

