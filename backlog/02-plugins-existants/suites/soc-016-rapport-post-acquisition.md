---
id: SOC-016
titre: "Mettre à jour et expliquer le suivi des engagements post-acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-014]
---

# SOC-016 — Mettre à jour et expliquer le suivi des engagements post-acquisition

## Objectif et résultat attendu

Le dirigeant obtient les modifications traçables du plan et un rapport daté des engagements ouverts, preuves manquantes et démarches utiles.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/integration-management/SKILL.md (Modes 3 à 5, hors modification des accords/contrats de SOC-015)`
- `corporate-legal/references/integration-tracker-schema.yaml (contrat SOC-014)`
- `corporate-legal/CLAUDE.md (sorties et rapport)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Plan SOC-014, preuves/déclarations sur engagements et responsables, instantané facultatif SOC-015, date de référence/horizon et précédent rapport.

## Travail attendu

Rapprocher par identifiant/version/entité, consigner provenance, auteur, ancien/nouvel état et date ; rapport contradictoire ne remplace pas la preuve. Reporter accords/contrats en lecture avec états exacts si adaptés par SOC-015, sinon rubrique non couverte. Distinguer objectifs internes, dates contractuelles et points juridiques non vérifiés. Totaux et évolutions sur périmètre connu ; retard du registre ne prouve pas inexécution. Export neutre et dashboard facultatif avec réserves ; enregistrement last_status_report n'est pas preuve d'envoi. Ne pas dire obligation PA satisfaite parce que tous les tiers ont un statut obtenu, ni déclarer absence de recours à expiration affichée.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Obligations et preuves du plan et de ses mises à jour ; textes applicables au mécanisme à rechercher si conséquence juridique demandée.

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

- Cas normal : A01 justificatif daté concernant une obligation, autre obligation ouverte : changement local précis et rapport qui conserve inconnues.
- Cas limite : Mise à jour orale « tous les accords sont obtenus » avec condition de garantie manquante : accord conditionnel reste ouvert ; pas de clôture du PA.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Mise à jour juridique des accords SOC-015, garantie/recours, diffusion et gestion métier RH/IT/finance.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

