---
id: FUN-012
titre: "Préparer une demande d'exhumation ou de transfert d'un corps ou d'une urne"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-007]
---

# FUN-012 — Préparer une demande d'exhumation ou de transfert d'un corps ou d'une urne

## Objectif et résultat attendu

Une personne qui souhaite déplacer un corps ou une urne vers une autre
sépulture comprend qui peut demander, auprès de qui, avec quelles pièces et
quelles questions restent ouvertes, et obtient un brouillon de demande.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/exhumation-transfer-request/SKILL.md` — le skill (à créer)
- `funeral-legal/references/exhumation-transfert.md` — demandeur, autorisations, pièces, sources lues (à créer)
- `funeral-legal/references/concession-funeraire.md` — relue, créée par FUN-007
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Titre de la concession d'origine et, s'il existe, de la concession d'accueil.
- Lien déclaré du demandeur avec le défunt ; position connue des autres proches.
- Date de l'inhumation ; communes concernées.
- Motif de la demande, dans les mots de la personne.

## Sortie attendue

1. Résumé : ce qui est envisagé, d'où vers où.
2. Questions sur la qualité du demandeur et l'accord d'autres proches, sans réponse déduite du seul lien familial.
3. Liste des interlocuteurs et pièces, avec la source lue ou réservée.
4. Brouillon de demande à la commune.
5. Suites : désaccord → FUN-003 ; concession d'accueil → FUN-007 ; élément étranger → point ouvert.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `exhumation-transfert.md` et l'appliquer : aucune condition, aucun
délai ni coût n'est affirmé sans source lue. Le skill n'organise pas
l'opération et ne choisit pas l'opérateur.

## Références métier et sources à rechercher

CGCT, exhumation et transport de corps (pistes R2213-40 et suivants,
R2213-8 et suivants) ; pistes FUN-007 pour la concession.

## Critères d'acceptation

- [ ] E01 prépare la demande et liste les pièces, sans condition non sourcée.
- [ ] E02 signale l'accord d'autres proches comme question ouverte, sans le présumer nécessaire ou inutile.
- [ ] La sortie se termine par la phrase BASE-013 nommant un avocat en cas de désaccord.

## Vérification

- Cas normal : E01 — Veuve souhaitant transférer le corps de son mari dans la commune où elle s'installe.
- Cas limite : E02 — Frère s'opposant au transfert demandé par la veuve.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Transfert international, organisation de l'opération, procédure, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 47 et tableau D03 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FE01 — Séparer exhumation, réduction/réunion de corps, déplacement de l’urne et transport avant mise en bière ; identifier opération exacte et autorité sans les traiter comme un régime unique.
- [ ] FE02 — Réunir demandeur, titre d’origine/d’accueil, accord contesté, autorisation, commande et devis détaillé ; conditions sanitaires uniquement comme questions à l’autorité, sans donnée médicale non nécessaire.
- [ ] FE03 — Distinguer possibilité d’autoriser, accord de l’opérateur et prix : aucun transfert engagé, coût inventé ou autorisation déduite du devis signé. FUN-008 garde le transport initial avant obsèques.

Scénarios supplémentaires **attendus, non exécutés** : devis regroupant ouverture, réduction et transfert sans autorisation fournie ; déplacement d’une urne décrit comme transport de corps avant mise en bière.

Sources à ouvrir lors de l’implémentation : régimes CGCT propres aux opérations identifiées, qualité du demandeur et autorisations ; règlement local et pièces de commande, sans transport international traité.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
