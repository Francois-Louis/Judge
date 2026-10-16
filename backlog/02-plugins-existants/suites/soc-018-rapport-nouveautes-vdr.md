---
id: SOC-018
titre: "Comparer deux inventaires de data room et préparer le rapport des nouveautés"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-018 — Comparer deux inventaires de data room et préparer le rapport des nouveautés

## Objectif et résultat attendu

Une petite équipe reçoit les ajouts/modifications visibles entre deux états d'une data room, avec portée des accès et documents à lire.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/agents/dataroom-watcher.md`
- `corporate-legal/CLAUDE.md (cadence, destinations et sources)`
- `corporate-legal/references/vdr-inventory-schema.yaml (à créer)`
- `corporate-legal/README.md (cadence réellement disponible)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Deux inventaires datés ou accès effectivement autorisé, dossier/opération explicite, identifiants/versions/empreintes, catégories et date de coupure/fuseau.

## Travail attendu

Distinguer nouveau document, nouvelle version, suppression non confirmée, inaccessible et doublon ; garder pointeur antérieur en échec partiel. Catégorie et priorité servent à organiser, pas à exclure de la couverture. Aucun contenu lu ni constat juridique déduit de métadonnées/preview. Produire rapport local ; checklist adaptée facultative en lecture seulement avec périmètre et version. Harmoniser quotidien/hebdomadaire avec déclenchement réel sans prétendre scheduler présent. Réduire outils génériques ; corriger Slack prétendu non livré versus déclaré, capacité configurée/testée et accord de diffusion distincts.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Métadonnées, inventaires et preuves d'accès ; BASE-005 pour provenance ; aucune règle juridique inférée d'un dépôt VDR.

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

- Cas normal : A01 avenant modifié sous même titre, document nouveau et fichier inchangé : trois états exacts et liste de lecture.
- Cas limite : Inventaire partiel ou VDR indisponible : rapport de couverture partielle, pas « aucune nouveauté » ni remplacement du dernier état complet.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Lecture des nouveautés, modification checklist, envoi Slack et activation d'un service planifié.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

