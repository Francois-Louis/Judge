---
id: SOC-001
titre: "Qualifier l'organe et la modalité d'une décision sociale"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-001 — Qualifier l'organe et la modalité d'une décision sociale

## Objectif et résultat attendu

Un associé ou dirigeant fournit un acte envisagé et ses pièces ; il reçoit une fiche société/acte, les organes et modalités à vérifier, les pièces manquantes et la voie de rédaction éventuellement ouverte.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/written-consent/SKILL.md (qualification avant rédaction)`
- `corporate-legal/skills/board-minutes/SKILL.md (entrée et renvoi vers qualification)`
- `corporate-legal/CLAUDE.md (accès ponctuel, Board & Secretary)`
- `corporate-legal/references/qualification-decision-sociale.md (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Forme sociale exacte, siège/territoire, identité et rôle du demandeur, objet et date de décision ; statuts en vigueur et modifications, pactes disponibles, répartition des droits de vote, nominations, délégations et pouvoirs, conflits signalés.

## Travail attendu

Qualifier SAS/SARL et l'acte avant tout modèle : compétence, pouvoirs, organe, convocations/information, participants, quorum/majorité selon le cas et modalité admissible. Distinguer règles légales, clauses statutaires, pactes et simple préférence. Tracer chaque disposition et sa version. Ne pas assimiler président, gérant, associés et board. Produire les questions utiles si une pièce manque, sans inventer un régime de remplacement. Une unanimité ne dispense pas de cette qualification. Hors SAS/SARL : fiche de pièces et orientation, pas d'application par analogie.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil, Code de commerce et textes d'application concernant décisions, pouvoirs et formes SAS/SARL ; jurisprudence officielle sur compétence/modalités à rechercher selon acte et dates ; statuts/pactes comme pièces distinctes.

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

- Cas normal : SAS fictive S01 autorisation bancaire : relever président et clause de décision collective au-delà du seuil statutaire ; la préférence de la banque n'établit pas la compétence.
- Cas limite : SARL S02 avec clause autorisant certaines consultations écrites, pacte incomplet et acte annuel d'approbation des comptes : rechercher le régime propre à l'acte, sans recopier la voie SAS ni donner un modèle de consentement.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Rédaction d'acte, résolution de conflit entre associés, SA/cotées et procédures de capital, fusion ou dissolution.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

