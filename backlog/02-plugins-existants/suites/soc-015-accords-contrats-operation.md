---
id: SOC-015
titre: "Qualifier et suivre les accords tiers sur les contrats d'une opération"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-014]
---

# SOC-015 — Qualifier et suivre les accords tiers sur les contrats d'une opération

## Objectif et résultat attendu

Le repreneur obtient un tableau par contrat distinguant cession, changement de contrôle, clause silencieuse et accord conditionnel, avec les pièces à obtenir.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/integration-management/SKILL.md (Mode 2, contrats/accords et leurs mises à jour)`
- `corporate-legal/references/integration-tracker-schema.yaml (contrat SOC-014)`
- `corporate-legal/references/accords-tiers-operation.md (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Structure de l'opération et droits transférés, parties/entités, contrats et avenants/loi, annexes d'accords requis, clauses et éventuelles lettres d'accord/garanties/notifications.

## Travail attendu

Séparer cession de titres, cession de contrat/actifs, fusion et transfert légal à qualifier ; premier cas implémenté acquisition de titres SAS/SARL, autres mécanismes renvoyés à revue propre. Lire définition de contrôle et clauses avec avenants, conditions, bénéficiaire et préavis. Clause silencieuse n'est pas auto-assign ; simple permission de cession ne réalise aucun transfert. Accord requis au PA distinct d'obligation envers tiers. Statuts demandé/reçu/conditionnel/vérifié/refusé avec preuve/portée/date ; aucun CoC déclenché automatiquement depuis un tier. Corriger renvoi vers written-consent pour lettres de tiers : fournir fiche de questions, pas acte social ni lettre réputée envoyée.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil sur contrats/cession, Code de commerce selon opération, jurisprudence officielle et conflit de lois selon chaque contrat ; clauses, accord tiers et PA sont des pièces distinctes.

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

- Cas normal : A01 acquisition de titres, contrat de maintenance exigeant accord en cas de contrôle indirect : question de déclenchement puis tableau conservant garantie préalable et notification.
- Cas limite : Contrat de filiale allemande silencieux, une clause permet cession aux affiliés sans acte fourni : interprétation étrangère réservée, ni transfert acquis ni statut no_action.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Rédaction/envoi de lettres d'accord, novation, transfert automatique et restructuration de la filiale.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

