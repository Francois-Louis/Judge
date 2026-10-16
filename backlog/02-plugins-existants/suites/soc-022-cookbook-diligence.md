---
id: SOC-022
titre: "Adapter le cookbook de grille aux données de diligence traçables"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-008, SOC-018]
---

# SOC-022 — Adapter le cookbook de grille aux données de diligence traçables

## Objectif et résultat attendu

Une équipe dispose d'un cookbook préparé et vérifié hors ligne, aligné sur les grilles et inventaires adaptés, sans service distant activé.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `managed-agent-cookbooks/diligence-grid/agent.yaml`
- `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml`
- `managed-agent-cookbooks/diligence-grid/subagents/extractor.yaml`
- `managed-agent-cookbooks/diligence-grid/subagents/normalizer.yaml`
- `managed-agent-cookbooks/diligence-grid/subagents/grid-writer.yaml`
- `managed-agent-cookbooks/diligence-grid/README.md`
- `managed-agent-cookbooks/diligence-grid/steering-examples.json`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Contrats SOC-008/018, paquet corporate embarqué, fixtures de grille et inventaires incluant noms accentués/Drive/version/illisible, schémas et destinations fictives.

## Travail attendu

Conserver orchestrateur local, MCP au lecteur et Write au writer. Charger méthode et références depuis plugin embarqué, pas checkout ; aligner quatre états, types, schéma/version et états de vérification. Accepter noms français et URL officielles rendues par outil sans les reconstruire. Quote/location requis pour answered, sources tronquées ou impossibles signalées ; garde des tailles ne fabrique pas de citation. Normalizer sans source ne peut vérifier caractère par caractère : retour au lecteur avec preuve source et statut de contrôle explicite, pas suspicion suffisante. Exporter schéma/états/flags/couverture, preuve brute distincte du CSV neutralisé, reprise ciblée sans écraser lignes intactes. Corriger droits réels et promesses Definely/Slack, secret présumé et cadence ; dry-run ne déploie ni n'envoie.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Méthode BASE-005 et contrats SOC-008/018 ; sources juridiques restent celles du cas si analyse. Infrastructure locale, manifestes et schémas comme preuves techniques.

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

- Cas normal : Lot fictif avec nom « Éléonore », URL Drive reçue et avenant versionné : schémas acceptent, sorties gardent états et sources, lint/dry-run propres.
- Cas limite : Citation mismatch et lecture partielle pendant reprise : needs_review, contrôle élargi et anciennes lignes préservées ; aucun handoff exécuté.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Déploiement distant, compte MCP réel, nouvelle infrastructure transverse et génération xlsx headless.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

