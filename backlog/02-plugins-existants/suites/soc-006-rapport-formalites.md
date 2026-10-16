---
id: SOC-006
titre: "Présenter les échéances et inconnues des formalités suivies"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-004, SOC-005]
---

# SOC-006 — Présenter les échéances et inconnues des formalités suivies

## Objectif et résultat attendu

Le dirigeant lit un rapport local et un export des formalités enregistrées, avec échéances établies, preuves manquantes et prochaines démarches.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/entity-compliance/SKILL.md (Modes 2 et 5)`
- `corporate-legal/references/compliance-tracker-schema.yaml (contrat SOC-004)`
- `corporate-legal/CLAUDE.md (sorties et dashboard)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Registre SOC-004/005, date de référence explicite, horizon, sources/calculs conservés, périmètre couvert et identités des sociétés.

## Travail attendu

Calculer les bandes depuis dates établies ; séparer date inconnue, dépassée selon registre, reçu/en attente et validé. Traiter aujourd'hui et dates hors horizon, version et fraîcheur. « Aucun dépôt enregistré » ne prouve pas absence de dépôt. Afficher entités étrangères et formalités non vérifiées hors totaux de conformité. Export CSV/table avec états, pièces et neutralisation des formules ; dashboard facultatif avec mêmes réserves et échappement HTML. Un rapport ne change pas le registre et n'active aucun rappel ni publication.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Fondements déjà tracés à recontrôler selon date/formalité ; aucune nouvelle règle de délai depuis la mémoire ou le calendrier du mandataire seul.

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

- Cas normal : Registre fictif contenant date du jour, date dépassée et validation documentée : rubriques exactes et pièces lisibles dans export.
- Cas limite : Filiale étrangère sans date et reçu français sans validation : demeurent inconnue et en attente, sans « groupe conforme » ni clôture automatique.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Audit documentaire général, modification de statut, dépôt ou surveillance planifiée.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

## Complément de besoins — formalités, 16 octobre 2026

Points 12, 26–27, 65 et section 10 de la [matrice formalités](../exist-002-frictions-utilisateurs.md) : calculer seulement avec déclencheur, date prouvée, source/version, unité, exceptions et voie de dépôt établis. Distinguer calendrier déclaré par l'utilisateur et échéance vérifiée ; aucun report de jour non ouvré par défaut. L'absence de preuve doit rester visible dans le rapport, sans statut global de conformité ni confusion avec les recours fiscaux/sociaux.
