---
id: BASE-013
titre: "Rendre systématique l'avertissement et l'interlocuteur compétent"
statut: terminee
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

- [x] La méthode `1.1.0` contient la phrase type, le renfort et la règle de choix de l'interlocuteur ; les copies sont identiques à la source (onze paquets depuis le retrait de `legal-clinic`).
- [x] `hiring-review` et `review` produisent la phrase en fin de réponse et le renfort dans un cas sensible, observé sur fixtures. *Cas fictifs, relecture par le rédacteur seulement.*
- [x] La phrase reste d'une ou deux lignes et ne remplace pas l'explication utile. *Après correction D1 ; cas fictifs.*
- [x] Le modèle de story impose le critère aux futures adaptations.

## Vérification

- Cas normal : lecture d'une offre d'emploi sans urgence → phrase finale avec « un avocat ou un juriste en droit du travail ».
- Cas limite : convocation pénale dans trois jours (scénario CRIM) → renfort en tête, avocat nommé, OPJ présenté comme autorité et non comme conseil.
- Cas limite : décompte de frais de notaire → interlocuteur notaire puis instance, sans formule d'avocat par défaut.

## Hors périmètre

Rédiger des conditions générales d'utilisation, adapter les skills hérités non
encore réécrits, ou valider le périmètre légal de la consultation juridique.

## Bilan d'exécution — 17 octobre 2026

- [Méthode BASE-005](../../references/research-citation-method.md) en
  version `1.1.0` : nouvelle section 8 (phrase finale en dernière ligne,
  renfort en tête, règle de choix de l'interlocuteur distinguant conseil et
  autorité, pas d'avocat par défaut, avocat toujours en pénal) et repère S4 ;
  l'ancienne section 8 devient la section 9. Copie identique dans les onze
  paquets ; versions `0.1.1`, `0.2.1` (`commercial-legal`) et `0.3.1`
  (`employment-legal`), descriptions, marketplace et test d'isolation alignés.
- `employment-legal` : `hiring-review` (renfort sur signature, démission ou
  clause difficile à défaire ; phrase finale avec « avocat ou juriste en droit
  du travail ») ; `worker-classification`, déjà doté de la phrase par
  TRAV-001, reçoit le renfort et la méthode `1.1.0`. La reformulation de
  `hiring-review` ne doit plus être remplie par le client (correction D3 de
  TRAV-001 reprise). Profil modèle, README, références et NOTICE mis à jour.
- `commercial-legal` : `review` et l'[orientation locale 1.1.0](../../commercial-legal/references/orientation-commerciale.md),
  avec deux lignes nouvelles (convocation pénale ; frais d'un professionnel du
  droit ou du chiffre). README et NOTICE mis à jour.
- [Modèle de story](../story-template.md) : le critère existant renvoie à la
  section 8 de la méthode.
- Cadre légal lu sur Légifrance : loi n° 71-1130, articles 54, 63, 64 et 66-2
  ([sources lues](base-013-annexes/base-013-sources-lues.json)). La méthode en
  tire seulement la règle de ne pas présenter une réponse comme l'avis
  personnalisé du professionnel ; le périmètre légal n'est pas qualifié.
- Recette : quatre pièces fictives, six exécutions `claude -p`, un défaut
  corrigé (D1, phrase finale suivie d'autres mentions). Détail dans la
  [vérification](base-013-annexes/base-013-verification.md).

## Portée

Voir la portée de la [vérification](base-013-annexes/base-013-verification.md) :
cas fictifs, client réel non isolé, relecture par le rédacteur seulement,
`review` exécuté avant la dernière correction de la méthode,
`worker-classification` non réexécuté. Les skills hérités non adaptés ne sont
pas concernés et ne produisent pas la phrase. L'article 66-2 change de version
le 1er février 2027 ; la nouvelle version n'a pas été lue.
