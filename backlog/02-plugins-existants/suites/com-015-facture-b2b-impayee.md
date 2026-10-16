---
id: COM-015
titre: "Reconstituer une facture B2B impayée et ses justificatifs"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-001]
---

# COM-015 — Reconstituer une facture B2B impayée et ses justificatifs

## Objectif et résultat attendu

Un indépendant/artisan a une facture client professionnel impayée ; il obtient le solde documenté, les pièces manquantes et un brouillon de relance factuelle.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/facture-b2b-impayee/SKILL.md (création proposée)`
- `commercial-legal/skills/review/SKILL.md (orientation)`
- `commercial-legal/references/facture-b2b.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Devis/commande/contrat, facture, livraison ou réception de prestation, échéance convenue, contestations, paiements partiels, avoirs, montants/devise et dates.

## Travail attendu

Reconstituer principal facturé moins paiements/avoirs sans certifier la créance. Distinguer preuve fournie et déclaration, exécution contestée et simple absence de paiement ; relance utile sans inventer intérêts, forfait ou prescription. Frais/pénalités chiffrés renvoyés à COM-016 ; absence de titre ne se résout pas par une saisie. Texte local prêt à relire, aucun envoi.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Clauses, Code civil/commerce sur preuve et paiement ; textes UE/transposition concernant retards de paiement à vérifier selon les faits, sans taux par défaut.

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

- Cas normal : Facture de 1 200 EUR, paiement prouvé de 400 EUR, avoir de 100 EUR : solde arithmétique 700 EUR, pièces et relance conditionnelle.
- Cas limite : Client particulier ou prestation contestée sans preuve de livraison : qualification B2C/secteur ou réserve, pas de créance certaine ni de pénalité automatique.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Mise en demeure juridique complète, intérêts calculés sans source, injonction de payer, titre exécutoire, saisie.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.

## Complément de besoins — formalités, 16 octobre 2026

Point 63 de la [matrice formalités](../exist-002-frictions-utilisateurs.md) : lors de la lecture d'une facture B2B ciblée, repérer les mentions fournies/manquantes et leur incidence à rechercher sans transformer l'absence d'une mention en inexistence de dette. Le contrôle exhaustif d'un modèle et ses variantes restent à découper ; mentions fiscales, franchise et réforme électronique → DOM-011/039, demande de paiement trompeuse → COM-019. Aucun taux ou montant forfaitaire repris du texte utilisateur sans source.
