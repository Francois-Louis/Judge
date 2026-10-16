---
id: COM-016
titre: "Comparer des frais ou pénalités à un contrat B2B"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-002]
---

# COM-016 — Comparer des frais ou pénalités à un contrat B2B

## Objectif et résultat attendu

Une TPE reçoit ou réclame des frais identifiés ; elle obtient la comparaison ligne/clause/preuve/calcul et les questions pour contester ou justifier la somme.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/frais-penalites-b2b/SKILL.md (création proposée)`
- `commercial-legal/skills/review/SKILL.md (orientation)`
- `commercial-legal/references/frais-penalites-b2b.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Facture détaillée, contrat et CGV/version acceptée, événement déclencheur, dates, montant/devise, formule/taux revendiqués, paiements et justificatifs.

## Travail attendu

Séparer prix, indemnité, clause pénale, frais et intérêts sans qualification automatique. Recalculer seulement les lignes dont fondement et entrées sont établis, montrer les hypothèses ; distinguer calcul conforme à la clause et validité juridique encore à vérifier. Aucun forfait légal mémorisé ni application de règle consommateur à partir de la seule taille de l'entreprise. Préparer demande d'explication/correction sans envoi.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Code civil et Code de commerce, jurisprudence officielle sur pénalités/déséquilibre et paiement ; texte UE/transposition le cas échéant ; versions et champ à établir.

Pistes **non vérifiées pour cette proposition** : lire textes, passages,
versions et transitions lors de l'implémentation. Tracer les accès réels,
y compris les voies officielles alternatives BASE-010 si nécessaire ; réserver
la conclusion dépendante lorsqu'une source ou une pièce manque.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable sur le cas normal, avec renvois aux pièces.
- [ ] Le cas limite réserve les conclusions dépendantes et propose une suite utile.
- [ ] Faits, clauses, hypothèses de droit et préférences de négociation restent distincts.
- [ ] Sources exactes, versions, temporalité et applicabilité sont tracées selon BASE-005.
- [ ] Le paquet détaché charge ses références locales ; isolation BASE-008 conservée.
- [ ] La sortie est comprise par une personne sans formation juridique ; aucune action externe implicite.
- [ ] Documentation, métadonnées et NOTICE reflètent seulement le périmètre réellement adapté.

## Vérification

- Cas normal : Prestataire réclame une pénalité de résiliation : clause et formule fournies comparées à la ligne facturée, calcul et question de validité séparés.
- Cas limite : Taux fourni sans version des CGV ni preuve d'acceptation : expliquer l'écart documentaire, pas de montant légal définitif ni conseil de ne pas payer.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Audit comptable/fiscal, barème universel, procédure judiciaire, prélèvement ou remboursement exécuté.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
