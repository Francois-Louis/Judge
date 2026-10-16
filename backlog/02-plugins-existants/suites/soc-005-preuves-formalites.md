---
id: SOC-005
titre: "Rapprocher une preuve de formalité du registre"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-004]
---

# SOC-005 — Rapprocher une preuve de formalité du registre

## Objectif et résultat attendu

Une personne fournit un reçu ou rapport de mandataire ; elle reçoit le rapprochement par société/formalité/période et les changements d'état réellement justifiés.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/entity-compliance/SKILL.md (Modes 3a/3b/3c)`
- `corporate-legal/references/compliance-tracker-schema.yaml (futur fichier de SOC-004)`
- `corporate-legal/references/formalites-societes.md (futur fichier de SOC-004 ; preuve et états)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Registre SOC-004, reçu, accusé, pièce de validation/rejet ou déclaration datée de l'utilisateur, identifiants d'entité et période, montant/devise si documenté.

## Travail attendu

Distinguer déclaré, transmis, reçu, en attente, validé, rejeté et inconnu. Un numéro de dépôt ou paiement ne suffit pas à marquer toute conformité courante. Rapprocher par identifiant stable et période ; homonymie ou rapport contradictoire produit une proposition à revoir. Conserver pièce, date, auteur, ancien état et modifications ; absence du rapport ne remet pas silencieusement une ligne à zéro. Mise à jour par digest, migration sans effacer historique. Ne pas exiger un rôle avocat pour consigner une pièce factuelle et ne prétendre aucune formalité exécutée par le skill.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Texte et procédure officielle de la formalité à vérifier ; pièces déposées/accusés et décisions de registre comme preuves distinctes des obligations.

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

- Cas normal : Reçu fictif S01 concernant une formalité et une période précises : seule cette ligne passe à reçu, sans validation présumée.
- Cas limite : Rapport « Atelier Rive » sans identifiant rapproche deux sociétés, dont une étrangère : aucun remplacement automatique ; demander la pièce discriminante.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Télétransmission, paiement et décision de l'autorité ; rapport d'échéances SOC-006.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

