---
id: SOC-007
titre: "Repérer les pièces manquantes d'un dossier de société"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-007 — Repérer les pièces manquantes d'un dossier de société

## Objectif et résultat attendu

Un associé ou dirigeant obtient une liste motivée des documents à réunir pour comprendre la situation d'une SAS/SARL et préparer une revue.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/entity-compliance/SKILL.md (Mode 4)`
- `corporate-legal/CLAUDE.md (Entity Management et limites de l'audit)`
- `corporate-legal/references/audit-pieces-societes.md (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Identité/forme et événements, statuts et versions, extrait/justificatif de registre daté, nominations, décisions, registre SOC-004 facultatif, organigramme et conventions intragroupe connues.

## Travail attendu

Borner l'audit à cohérence et lacunes documentaires : statuts anciens, chaîne de nominations, pièces de décision manquantes, relations intragroupe à clarifier. Dire quelle pièce répond à quelle question et à qui la demander. Ne pas certifier solvabilité ou conformité, ni substituer Kbis/RNE au good standing US. Retirer recommandation de dissolution pour entité dormante de plus de cinq ans et présomption foreign qualification depuis une adresse. Une opération étrangère appelle pièces et spécialiste local, sans diagnostic automatique.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil, Code de commerce et procédures officielles de registres selon la question ; extraits et statuts sont des pièces datées à rapprocher.

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

- Cas normal : SARL dont statuts et nomination du gérant sont fournis mais PV d'une modification manque : demande de pièce reliée à l'incohérence.
- Cas limite : Société inactive depuis six ans : relever statut déclaré et documents manquants, sans recommander dissolution ni conclure perte de capacité.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Audit juridique exhaustif, choix de restructuration et formalités de dissolution.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

## Complément de besoins — formalités, 16 octobre 2026

Points 20–21, 65–70 de la [matrice formalités](../exist-002-annexes/exist-002-frictions-utilisateurs.md) : identifier justificatif et exercice réellement nécessaires, pièces de décisions de l'associé unique, demande de confidentialité et preuve de dépôt. Distinguer accès public, occultation d'adresse et conservation interne. L'archivage demande une qualification par catégorie et finalité avec durée à rechercher ; pas de délai unique ni purge. L'audit ne certifie pas les comptes et renvoie la question fiscale à DOM-011/039.
