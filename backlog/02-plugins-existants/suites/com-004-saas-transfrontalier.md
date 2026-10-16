---
id: COM-004
titre: "Revoir une souscription SaaS B2B transfrontalière"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-002]
---

# COM-004 — Revoir une souscription SaaS B2B transfrontalière

## Objectif et résultat attendu

Une TPE française achète un SaaS à un fournisseur établi dans un autre pays ; elle obtient une revue intégrée du contrat, du bon et des annexes disponibles.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/saas-msa-review/SKILL.md`
- `commercial-legal/skills/vendor-agreement-review/SKILL.md (interface de surcouche)`
- `commercial-legal/skills/review/SKILL.md (branche SaaS)`
- `commercial-legal/CLAUDE.md (positions SaaS/IA)`
- `commercial-legal/references/saas-b2b-fr-ue.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Contrat, bon, SLA, DPA et politiques avec versions, établissements, dates, prix/devise, usages, données, chaîne de prestataires et clause loi/juge.

## Travail attendu

Reprendre prix/hausse, reconduction, notification, SLA, changement de service et réversibilité. Distinguer sous-traitance technique et rôles RGPD, transferts, droits d'entraînement IA explicites ou incorporés. Qualifier chaque texte UE et sa temporalité sans convertir HIPAA/FTC ou le droit consommateur en droit B2B. DPA non lu reste une lacune. Fournir une fiche d'échéance avec provenance ; appel au registre seulement après adaptation COM-006, sinon remise manuelle. Les compléments privacy/IA restent facultatifs et ne certifient pas la revue.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Code civil/commerce, Rome I/Bruxelles I bis ; RGPD, règlement sur les données et règlement IA selon champ et calendrier à vérifier ; décisions officielles et orientation CNIL/CEPD distinguées.

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

- Cas normal : SaaS français/irlandais avec bon promotionnel, SLA et DPA fournis : exceptions de prix, sortie et hypothèses de loi distinguées des préférences.
- Cas limite : Fournisseur américain, DPA par URL inaccessible et politique modifiable : analyse des pièces lues, droit étranger et transferts réservés, aucune validation RGPD complète.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Audit complet données/IA/cybersécurité, arbitrage définitif de droit étranger, signature ou migration technique.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
