---
id: SOC-019
titre: "Personnaliser les préférences sociétés sans imposer un profil de grande entreprise"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-019 — Personnaliser les préférences sociétés sans imposer un profil de grande entreprise

## Objectif et résultat attendu

Un associé ou dirigeant choisit ses préférences utiles et peut les modifier ; une demande ponctuelle reste possible sans équipe juridique ni anciens modèles.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/cold-start-interview/SKILL.md (hors --new-deal)`
- `corporate-legal/skills/customize/SKILL.md`
- `corporate-legal/CLAUDE.md (scaffold, setup, modules, sources et sorties)`
- `corporate-legal/README.md (publics, état et commandes)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Rôle réel, sociétés/formes/juridictions et dates déclarées, préférences de format, périmètre souhaité, profil existant et progression éventuelle ; outils seulement si utiles.

## Travail attendu

Conserver reprise et édition ciblée par digest, séparation partagé/domaine et accès réellement testé. Aucun default juridique US ni import d'autre distribution. Profil facultatif pour lecture ponctuelle, faits déterminants demandés par tâche ; pièces juridiques ne se déduisent pas d'un format ou poste. Retirer Board/GC obligatoire, seeds imposés pour accéder à l'aide, seuil interne pilotant annexe PA et protection attorney work product attribuée automatiquement. Public Company n'a pas de skill : retirer promesses SEC/§16/10-K/10-Q et marquer non adapté/hors tranche ; aucun remplacement implicite par calendrier coté français. État précis des 13 skills et sept connecteurs, pas de prétendue connexion ou installation depuis cwd. Préserver les réponses existantes et n'ajouter que préférences validées.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Architecture BASE-003, méthode BASE-005, isolation BASE-008 et protocole USAGE-001 ; droit des rôles/secret à rechercher seulement si une protection est affirmée.

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

- Cas normal : Associé de petite SARL sans GC ni modèles : préférences facultatives de langue/format conservées, aucune composition de board inventée.
- Cas limite : Ancien profil Public Company et module public demandé : conserver l'historique/les réponses mais expliquer absence de workflow France/UE, sans calendrier SEC appliqué.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Adaptation juridique de tous skills, droit des sociétés cotées, profil importé et synchronisation divergente d'une copie commune.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

