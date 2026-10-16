---
id: SOC-002
titre: "Préparer un projet d'autorisation bancaire SAS ou SARL"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-001]
---

# SOC-002 — Préparer un projet d'autorisation bancaire SAS ou SARL

## Objectif et résultat attendu

Le représentant d'une petite société obtient un projet marqué à relire et une liste des pouvoirs/signataires à confirmer pour l'ouverture d'un compte ou une habilitation bancaire précisément définie.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/written-consent/SKILL.md (rédaction et sortie)`
- `corporate-legal/CLAUDE.md (format et limites des décisions écrites)`
- `corporate-legal/references/autorisation-bancaire.md (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Fiche SOC-001 établie pour cet acte, statuts et pouvoirs retenus, banque, compte/objet, limites de montant et durée, identité des personnes habilitées, date et modalités de décision, précédent facultatif.

## Travail attendu

Borner le premier acte à une autorisation bancaire sans crédit, caution, sûreté ni opération sur capital. Produire projet conditionné à la modalité qualifiée, objet précis, pouvoirs limités, annexes et signataires avec provenance. Le précédent apporte un style, pas une validation. Supprimer unanimité du board, ratification rétroactive, délégation générale et équivalence signature électronique/original comme formules par défaut. Signaler les lacunes dans les notes et ne prétendre ni adoption, ni signature, ni envoi. Absence de précédent : structure française documentée ou fiche préparatoire utile, sans blocage pour seule préférence de style.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Sources SOC-001 pour pouvoirs/décision et Code civil pour preuve/signature ; règlement eIDAS si la question se pose, avec champ/version ; exigences bancaires fournies comme pièces.

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

- Cas normal : S01 avec compétence/modalité vérifiées dans le futur lot : projet limité à l'habilitation nommée, pièces et personnes à contrôler.
- Cas limite : La banque joint un emprunt et une caution au formulaire d'ouverture : isoler ces actes, réserver le projet qui en dépend et expliquer le besoin de qualification propre.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Crédit, garanties, capital, acquisitions, envoi en signature ou suivi effectif des signatures.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

