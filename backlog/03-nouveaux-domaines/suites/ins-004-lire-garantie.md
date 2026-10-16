---
id: INS-004
titre: "Lire une garantie pour un événement donné"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-004 — Lire une garantie pour un événement donné

## Objectif et résultat attendu

Une personne qui se demande si son contrat couvre un événement identifie les
clauses pertinentes, les conditions, plafonds et franchises indiqués, et ce
qui manque pour répondre.

## Périmètre et fichiers

- `insurance-legal/skills/coverage-review/SKILL.md` — le skill (à créer)
- `insurance-legal/references/lecture-garantie.md` — méthode de lecture d'un contrat (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`lecture-garantie.md` est relu par INS-007, qui ne le réécrit pas.

## Pièces et informations nécessaires

Conditions générales et particulières en vigueur ; avenants ; description de
l'événement réel ou envisagé.

## Sortie attendue

Clauses pertinentes recopiées ; conditions ; plafonds et franchises lus ;
exclusions possibles à examiner ; pièces manquantes ; limites. Pas de verdict
« couvert » sans les conditions particulières.

## Travail attendu

Distinguer définition de la garantie, exclusion et condition. Une question
de devoir de conseil de l'intermédiaire est notée, sans analyse.

## Références métier et sources à rechercher

Code des assurances, information et mentions du contrat ; directive (UE)
2016/97 pour la distribution, selon la question.

## Critères d'acceptation

- [ ] L01 recopie les clauses et réserve la réponse aux pièces manquantes.
- [ ] L02 ne conclut pas « couvert » sur les seules conditions générales.

## Vérification

- Cas normal : L01 — « Mon assurance habitation couvre-t-elle un vélo volé dans le garage collectif ? »
- Cas limite : L02 — Conditions générales seules fournies.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Comparaison d'offres, conseil de souscription, envoi.

## Complément issu des frictions assurance

Points 1, 3–8, 12–14, 31–36, 41–45, 58–59 et 70–72 de la [matrice](../dom-005-annexes/dom-005-frictions-utilisateurs.md).

- [ ] L03 — Produire une grille garantie/définition/condition/exclusion/option/effet/carence/franchise/plafond/sous-plafond, avec unité, période et référence de chaque clause ; comparer avenants et conditions sans résoudre une contradiction par intuition.
- [ ] L04 — Habitation : distinguer effraction, dispositifs de sécurité, inhabitation, dépendances et objets précieux ; absence de clause ou de preuve de valeur reste explicite.
- [ ] L05 — Auto : séparer RC tiers, dommages du véhicule et garantie conducteur ; lire prêt du volant et franchise annoncée.
- [ ] L06 — Carte et voyage : distinguer assistance et assurance, paiement exigé ou non, bénéficiaires, durée, territoire, activation et motif d'annulation ; obligations du transporteur → DOM-008.
- [ ] L07 — Accident de la vie : relever définition et seuil contractuels sans seuil universel ni expertise médicale ; dommage corporel → DOM-035.

Scénarios L03–L07 **attendus, non exécutés** : plafond mobilier et bijoux différent, option au récapitulatif contredite ailleurs, vol dans garage d'un logement inoccupé, blessures d'un conducteur assuré au tiers, assistance de carte sans paiement du voyage, GAV sous un seuil allégué. Aucun montant de prestation recalculé. Assurance accessoire → INS-016 pour la souscription/renonciation ; risque professionnel → INS-019 ; sinistre eau → INS-017 ; Cat Nat → INS-018. La question de conseil reste une orientation vers INS-016, pas une comparaison d'offres ici.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 90–94, 106 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FO01 — Contrat obsèques : lire capital, forme des cotisations, période garantie, carence, exclusions, revalorisation et faculté de rachat annoncée ; montants documentés séparés, sans performance prédite ni épargne récupérable présumée.
- [ ] FO02 — Distinguer capital et prestations FUN-006 ; décès temporaire et garantie viagère ne sont pas assimilés. L’exercice d’un rachat obsèques reste à découper dans DOM-005, INS-012 n’étant pas automatiquement étendue à ce régime.

Scénarios supplémentaires **attendus, non exécutés** : primes viagères déjà versées au-delà du capital indiqué ; garantie temporaire expirée avant décès ; demande de remboursement de toutes les primes sur la seule promesse « épargne obsèques ».

Sources à ouvrir lors de l’implémentation : assurance vie/décès et financement obsèques, notices, clauses de rachat et information ; régime de l’organisme et contrat daté.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-annexes/dom-005-decoupage-assurance.md).

## Complément des frictions santé — 16 octobre 2026

Points 21 et 123–126 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Lire base de remboursement, plafond/période, forfait, carence, exclusion et bénéficiaire dans le contrat applicable ; la garantie exprimée en pourcentage n'est pas un pourcentage automatique de facture.
- [ ] FS02 — Demander une simulation écrite avant soin si utile ; en relever conditions et limites sans garantir le remboursement ni recalculer le reste à charge.

Scénarios **attendus, non exécutés** : promesse orale « tout remboursé »,
garantie en pourcentage de base et plafond annuel ; conditions particulières
absentes, réponse réservée. Contrat de mutuelle/institution/assureur à
qualifier par son code, pas assimilé au seul Code des assurances ; INS-009
garde le refus et DOM-012 la caisse. [Portée](../dom-007-annexes/dom-007-frictions-verification.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 93, 126, 139–141, 149–150 et 174 de la [matrice véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md).

- [ ] AUTO01 — Assistance : rapprocher franchise kilométrique, destination, accord préalable et plafonds rapatriement/hébergement ; garanties de mobilité distinctes d'un prêt du garage VEH-014, aucun droit général à un véhicule de remplacement.
- [ ] AUTO02 — Location et LOA : identifier qui assure quoi, qualité du locataire/bailleur et nature du rachat de franchise ; lire exclusions pneus/jantes/vitrage et perte financière, sans solde de dette présumé couvert. Revue bancaire BNK-005 ; frais du loueur VEH-006/017.
- [ ] AUTO03 — Choix du réparateur : séparer liberté de choix à vérifier dans le texte exact, avance de frais/règlement et prestation du garage VEH-001 ; aucun paiement direct identique dans tous les garages supposé.

Pièces supplémentaires : contrat d'assistance, décision d'accord/refus, location et option signée, règlement annoncé. Cas attendus : assistance proche domicile ; contrat perte financière sans conditions particulières ; réparateur hors réseau avec avance de frais. Scénarios **attendus, non exécutés** ; refus effectif → INS-001. Le lien légal du texte utilisateur reste à ouvrir et dater avant conclusion.

[Portée et vérification documentaire](../dom-023-annexes/dom-023-frictions-verification.md) ; aucune implémentation ni droit validé par ce complément.
