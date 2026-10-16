---
id: BASE-013
titre: "Rendre systématique l'avertissement et l'interlocuteur compétent"
statut: proposee
priorite: P1
nature: implementation
dependances: [BASE-005, BASE-008]
---

# BASE-013 — Rendre systématique l'avertissement et l'interlocuteur compétent

## Objectif

Chaque réponse d'un skill adapté indique, en une phrase courte, qu'elle
informe sans remplacer l'avis d'un professionnel compétent, et nomme le bon
interlocuteur pour le domaine : avocat, juriste d'une association ou d'un
point d'accès au droit, notaire, commissaire de justice, expert-comptable,
médiateur ou service de l'organisme. Un renfort placé en tête s'ajoute quand
il y a délai, procédure, pénal, mesure en cours ou enjeu irréversible.
Décision de l'utilisateur du 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

## Périmètre

- Méthode commune [BASE-005](../../references/research-citation-method.md) :
  nouvelle section, version `1.1.0`, puis synchronisation identique dans les
  douze paquets (`references/shared/`) et contrôle des copies BASE-008.
- Skills déjà adaptés : `employment-legal:hiring-review` et
  `commercial-legal:review`, avec leurs README et NOTICE.
- [Modèle de story](../story-template.md) : critère d'acceptation commun pour
  toutes les futures adaptations.

## Travail attendu

- Rédiger une phrase type courte et neutre : la réponse aide à comprendre et à
  préparer une démarche ; elle ne remplace pas l'avis du professionnel compétent
  nommé pour la situation. Pas de formule anglaise ni de bandeau répété.
- Définir le renfort de tête : délai ou prescription possible, acte de
  procédure, mesure pénale ou privative de liberté, signature imminente,
  enjeu irréversible. Il nomme l'interlocuteur et l'urgence, sans calcul.
- Tableau des interlocuteurs par domaine, repris de la colonne
  « interlocuteur » de BASE-003. L'autorité qui mène une procédure (officier de
  police judiciaire, administration, organisme) est un interlocuteur pour
  l'information sur le dossier, pas un conseil : en matière pénale, le conseil
  à recommander reste l'avocat.
- Vérifier, lors de l'implémentation, le cadre légal de la consultation
  juridique et de l'information juridique (piste : loi n° 71-1130 du
  31 décembre 1971, titre II), pour que les skills restent du côté de
  l'explication et de la préparation.

## Critères d'acceptation

- [ ] La méthode `1.1.0` contient la phrase type, le renfort et la règle de choix de l'interlocuteur ; les douze copies sont identiques à la source.
- [ ] `hiring-review` et `review` produisent la phrase en fin de réponse et le renfort dans un cas sensible, observé sur fixtures.
- [ ] La phrase reste d'une ou deux lignes et ne remplace pas l'explication utile.
- [ ] Le modèle de story impose le critère aux futures adaptations.

## Vérification

- Cas normal : lecture d'une offre d'emploi sans urgence → phrase finale avec « un avocat ou un juriste en droit du travail ».
- Cas limite : convocation pénale dans trois jours (scénario CRIM) → renfort en tête, avocat nommé, OPJ présenté comme autorité et non comme conseil.
- Cas limite : décompte de frais de notaire → interlocuteur notaire puis instance, sans formule d'avocat par défaut.

## Hors périmètre

Rédiger des conditions générales d'utilisation, adapter les skills hérités non
encore réécrits, ou valider le périmètre légal de la consultation juridique.
