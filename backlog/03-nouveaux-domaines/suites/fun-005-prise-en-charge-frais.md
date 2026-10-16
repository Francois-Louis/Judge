---
id: FUN-005
titre: "Identifier les financements à interroger et les questions de prise en charge des frais d'obsèques"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-001]
---

# FUN-005 — Identifier les financements à interroger et les questions de prise en charge des frais d'obsèques

## Objectif et résultat attendu

Une personne qui se demande qui paiera les obsèques obtient la carte des
financements possibles à interroger (fonds du défunt, contrat obsèques,
organismes, commune), les pièces à réunir pour chacun et l'interlocuteur
propriétaire de la question, sans réponse unique ni montant promis.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/funeral-cost-funding/SKILL.md` — le skill (à créer)
- `funeral-legal/references/prise-en-charge-frais.md` — carte des financements et de leurs propriétaires, sources lues (à créer)
- `funeral-legal/references/qualification-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Devis ou facture ; montant déjà avancé et par qui.
- Existence connue de comptes, d'un contrat obsèques, d'une assurance-vie, d'une complémentaire ou d'une prévoyance.
- Statut déclaré du défunt (salarié, retraité, autre) pour orienter vers l'organisme, sans données de santé.
- Notaire saisi ou non ; actif ou absence d'actif déclaré.

## Sortie attendue

1. Résumé : qui a avancé ou doit avancer, ce qui est cherché.
2. Carte des financements : piste, condition à vérifier, pièce, propriétaire (DOM-016, DOM-005, DOM-012, commune).
3. Fiche des trois qualités, la qualité de personne tenue au paiement restant « à établir ».
4. Questions à poser à chaque interlocuteur, sans plafond ni montant non sourcés.
5. Suites : paiement sur les comptes du défunt → DOM-016 ; contrat obsèques ou capital → DOM-005 (INS-004, INS-011) ; capital décès d'un organisme → DOM-012 ; contribution des proches sans actif → point ouvert.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `prise-en-charge-frais.md` et l'appliquer : chaque mécanisme reste à
son propriétaire et n'est décrit que pour la question à poser. Aucun
plafond, condition d'ouverture ou montant n'est donné sans source lue. Le
skill ne dit pas qui doit finalement supporter les frais et ne promet aucun
remboursement de l'avance.

## Références métier et sources à rechercher

Code monétaire et financier, prélèvement sur les comptes du défunt pour les
frais funéraires (piste L312-1-4), pour l'orientation DOM-016 ; Code de la
sécurité sociale, capital décès (pistes L361-1 et suivants), pour
l'orientation DOM-012 ; CGCT, obsèques des personnes dépourvues de
ressources (piste L2223-27) ; Code civil, obligation alimentaire (pistes 205
et suivants), pour le point ouvert.

## Critères d'acceptation

- [ ] F01 produit une carte des financements avec propriétaire et pièces, sans montant ni plafond non sourcés.
- [ ] F02 ne désigne pas la personne tenue au paiement à partir du seul lien familial.
- [ ] Aucune prise en charge ni aucun remboursement n'est promis.
- [ ] La sortie se termine par la phrase BASE-013 nommant le notaire chargé de la succession ou un avocat selon la situation.

## Vérification

- Cas normal : F01 — Fils ayant avancé les frais, défunte titulaire d'un compte bancaire et peut-être d'une complémentaire.
- Cas limite : F02 — Défunt sans actif connu, enfants éloignés sollicités par la mairie.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Règlement de la succession, lecture d'une garantie d'assurance, demande à un
organisme social, contentieux familial, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 55–56, 74, 105, 113–116, 134–135 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FF01 — Distinguer avance, règlement bancaire direct, capital privé, prestation publique, prise en charge communale et charge finale ; pour chaque piste : interlocuteur, pièce, date et inconnu, sans addition des droits supposés.
- [ ] FF02 — Préparer les questions à la banque/notaire et à la commune du lieu du décès, sans plafond non vérifié ni prise en charge garantie. La demande CPAM distingue priorité et demande ordinaire ; réversion vers DOM-036.
- [ ] FF03 — Si une renonciation successorale est invoquée, ne conclure ni que les frais disparaissent ni que chaque enfant est tenu ; conserver le point ouvert DOM-013/016 sur la contribution familiale sans actif.

Scénarios supplémentaires **attendus, non exécutés** : famille sans liquidités mais compte du défunt connu ; enfant renonçant sollicité par la commune ; proches demandant en même temps capital CPAM et garantie de prévoyance.

Sources à ouvrir lors de l’implémentation : paiement bancaire des obsèques, prise en charge communale, capital décès selon organisme et régime, articulation successorale/familiale ; uniquement pour orientation dans ce skill.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
