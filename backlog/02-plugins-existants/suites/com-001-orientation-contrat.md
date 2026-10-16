---
id: COM-001
titre: "Qualifier et orienter une demande sur un contrat"
statut: a-verifier
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-001 — Qualifier et orienter une demande sur un contrat

## Objectif et résultat attendu

Une personne fournit un contrat ou un récit ; elle obtient le domaine principal, la tâche retenue, les pièces utiles et les questions qui conditionnent la suite.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/review/SKILL.md`
- `commercial-legal/CLAUDE.md (accès sans profil et routage)`
- `commercial-legal/references/orientation-commerciale.md` (créé par ce lot)

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Demande et objectif, qualité et rôle des deux parties pour cet acte, objet réel, pays/territoires, dates, clauses de loi et de juge, documents et annexes disponibles.

## Travail attendu

Conserver le repérage des titres puis lire la substance nécessaire à la qualification. Distinguer B2B, consommation, secteur, emploi, contentieux et exécution ; ne pas déduire B2B du seul statut du demandeur. Séparer loi applicable, juge et préférence du playbook. Prévoir les branches revue, NDA, SaaS, avenants, échéance et les futures tâches de paiement/rupture avec leur état réel. Ne pas lancer un skill hérité lorsque sa branche reste non adaptée.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Architecture BASE-003 et protocole USAGE-001 ; textes de qualification des parties et instruments de conflit France/UE à rechercher selon les faits.

Pistes **non vérifiées pour cette proposition** : lire textes, passages,
versions et transitions lors de l'implémentation. Tracer les accès réels,
y compris les voies officielles alternatives BASE-010 si nécessaire ; réserver
la conclusion dépendante lorsqu'une source ou une pièce manque.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable sur le cas normal, avec renvois aux pièces.
- [ ] Le cas limite réserve les conclusions dépendantes et propose une suite utile.
- [ ] Faits, clauses, hypothèses de droit et préférences de négociation restent distincts.
- [x] Sources exactes, versions, temporalité et applicabilité sont tracées selon BASE-005 (cadrage R1/R2 lus ; F1/F2 inaccessibles, conclusions réservées).
- [x] Le paquet détaché contient ses références locales et conserve l'isolation BASE-008 (contrôles de fichiers/helper ; chargement effectif en skill non exécuté).
- [ ] La sortie est comprise par une personne sans formation juridique ; aucune action externe implicite.
- [x] Documentation, métadonnées et NOTICE reflètent seulement le périmètre réellement adapté.

## Vérification

- Cas normal : Artisan achetant une prestation à une société française : domaine commercial, côté achat, pièces et hypothèses identifiés.
- Cas limite : Le même artisan facture un particulier pour des travaux : orientation sectorielle/B2C expliquée, sans déclarer le futur plugin disponible.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Revue juridique complète, profil professionnel obligatoire, lancement automatique des autres COM.

## Implémentation — 16 octobre 2026

Tranche sélectionnée par l'utilisateur : « implémente la story COM-001 ».
`review` et la référence locale sont réécrits ; exception de profil bornée à
l'orientation, sans modifier les références communes. Version commerciale
`0.2.0`, marketplace synchronisé. Aucune autre COM adaptée ou lancée.

Voir le [bilan par couche](com-001-verification.md), les
[pièces fictives](com-001-recette/pieces-fictives.md), les
[sorties de relecture du rédacteur](com-001-recette/sorties-relecture.md) et les
[preuves techniques](com-001-recette/resultats-paquet.json).

Schémas officiels et installation locale jetable réussis ; contrôle statique
incomplet (42 points de relecture, aucun défaut de structure). 14 tests BASE-008
réussis, 2 ignorés avec motif ; 13 tests du contrôleur réussis. **Invocation de
`review` non exécutée** : aucune authentification dans la configuration jetable,
aucun identifiant personnel importé. Reformulation par un lecteur réel non
exécutée. Les critères métier non cochés restent ouverts ; statut `a-verifier`.

Autres fichiers repris : README et NOTICE racine, manifeste marketplace,
manifeste/README/NOTICE commerciaux, fixture de version BASE-008. Backlog :
présente story, bilan et dossier de recette, état du découpage et index README.
L'inventaire EXIST-001 demeure un relevé historique, sans mise à jour de ses
empreintes comme si le plugin était resté inchangé.
