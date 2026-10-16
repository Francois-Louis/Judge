---
id: FUN-004
titre: "Répondre à un opérateur funéraire qui réclame un paiement quand les signataires ne sont pas identifiés"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-002, FUN-005]
---

# FUN-004 — Répondre à un opérateur funéraire qui réclame un paiement quand les signataires ne sont pas identifiés

## Objectif et résultat attendu

Une personne à qui un opérateur funéraire réclame le paiement des obsèques
comprend ce qui lui est demandé et à quel titre apparent, ce que les pièces
disent de son engagement, ce qui reste à établir, et obtient un brouillon de
réponse demandant les pièces d'engagement et le décompte.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/funeral-payment-demand/SKILL.md` — le skill (à créer)
- `funeral-legal/skills/funeral-payment-demand/references/reponse-demande-paiement.md` — modèle de réponse (à créer)
- `funeral-legal/references/qualification-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/references/prise-en-charge-frais.md` — relue, créée par FUN-005
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Demande de paiement ou relance, sa date, son destinataire et l'échéance alléguée.
- Devis, bon de commande et facture, avec signatures visibles ou absentes.
- Rôle de la personne lors de l'organisation : présente, a choisi, a signé, a seulement été informée.
- Paiements déjà faits, par qui ; fonds du défunt ou contrat obsèques connus.
- Autres proches sollicités ou non.

## Sortie attendue

1. En tête : échéance alléguée et stade de la demande (amiable, recouvrement, acte d'un commissaire de justice).
2. Fiche des trois qualités appliquée à la personne sollicitée, chaque qualité fondée ou « à établir ».
3. Tableau : pièce, signataire visible, prestations couvertes, montant recopié.
4. Pistes de prise en charge à interroger, reprises de FUN-005, sans réponse sur qui doit payer.
5. Brouillon de réponse demandant copie des pièces signées et décompte, sans reconnaissance ni refus de dette.
6. Suites : contenu de la facture → FUN-002 ; succession → DOM-016 ; relance de recouvrement → DOM-003 (ENF-002) ; injonction de payer → DOM-003 (ENF-012).
7. Limites et phrase BASE-013.

## Travail attendu

Appliquer la fiche des trois qualités : avoir été présent, être enfant ou
conjoint, ou avoir reçu la facture ne vaut pas signature. Le skill ne
conseille ni de payer, ni de refuser, et ne dit pas qui doit payer ; il
documente ce que les pièces établissent et ce qui manque. Un acte de
commissaire de justice place un renfort en tête et oriente vers DOM-003.

## Références métier et sources à rechercher

Pistes FUN-002 ; Code civil, engagement du signataire et frais funéraires
(pistes 806 et 2331), à vérifier ; pistes DOM-016 pour la succession.

## Critères d'acceptation

- [ ] P01 prépare une réponse demandant pièces signées et décompte, sans reconnaître ni contester la dette.
- [ ] P02 ne déduit aucune obligation de payer du seul lien familial et le dit dans la sortie.
- [ ] L'opérateur n'est pas présumé abusif ; aucune dispense de paiement n'est promise.
- [ ] La sortie se termine par la phrase BASE-013 nommant un notaire, une association de consommateurs ou un avocat selon la situation, avec renfort en tête en cas d'échéance ou d'acte.

## Vérification

- Cas normal : P01 — Relance adressée à une fille du défunt, le bon de commande ne portant qu'une signature illisible.
- Cas limite : P02 — Opérateur réclamant le solde à chacun des trois enfants, aucun n'ayant signé selon eux.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Règlement de la succession, défense en justice, exécution forcée, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 76, 134, 136 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FP01 — Distinguer engagement signé envers l’opérateur, contribution finale entre proches et passif successoral. Renonciation déclarée ne vaut ni dispense de frais affirmée ni reconnaissance de dette.
- [ ] FP02 — Si émetteur, facture ou coordonnées de paiement divergent, relever les écarts et préparer une vérification par un canal connu ; ne pas utiliser les coordonnées contestées comme seule preuve. Paiement déjà effectué sous tromperie → BNK-002 ; infraction alléguée → DOM-002.

Scénarios supplémentaires **attendus, non exécutés** : signataire demandant aux autres enfants de tout rembourser ; facture reprenant le nom d’un opérateur connu avec coordonnées de paiement modifiées.

Sources à ouvrir lors de l’implémentation : engagement contractuel, preuve de la demande et frais funéraires ; voies de réclamation bancaire ou pénale pour leurs seuls objets.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
