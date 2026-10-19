---
id: DOU-018
titre: "Préparer le retour pour réparation d'un produit vendu hors de l'Union"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001, DOU-005]
---

# DOU-018 — Préparer le retour pour réparation d'un produit vendu hors de l'Union

## Objectif et résultat attendu

Un client d'un pays tiers renvoie un couteau acheté à l'entreprise pour
réparation, affûtage, échange ou remboursement. Le résultat est un dossier
d'entrée et de réexpédition : qualification du retour (retour en l'état,
réparation sous un régime à rechercher, échange, retour commercial
définitif), pièces qui prouvent l'exportation initiale et l'identité du
produit, mentions à donner au client pour son envoi, formalités de
réexportation, et inconnues sur droits et TVA à l'entrée.

## Origine

Demande de l'utilisateur du 19 octobre 2026 sur son activité d'exportation de
couteaux. Reprend K03, C04, C05 et les points 47 et 48 de la
[matrice des frictions](../dom-009-annexes/dom-009-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `customs-legal`. Fichiers futurs :
`customs-legal/skills/return-repair-documents/SKILL.md` et
`customs-legal/references/retour-reparation.md` (à créer). Contrat commun DOM-009.

## Pièces et informations nécessaires

Déclaration d'exportation initiale (MRN) et preuve de sortie, facture de
vente, numéro de série ou marquage, photos, motif du retour (garantie,
réparation payante, échange, rétractation), dates, pays d'expédition du
retour, transporteur, documents d'exportation du pays du client, intention de
réexpédier.

## Sortie attendue

Arbre de qualification ; pour l'option retenue, régime à rechercher,
conditions (identité, délai, état), pièces disponibles et manquantes ;
consignes au client pour la facture pro forma et la mention du motif ;
formalités de réexportation ; questions au service des douanes ou au
transporteur. Droits à l'importation et TVA traités séparément.

## Travail attendu

Lire les articles du CDU et de ses actes sur les marchandises en retour, le
perfectionnement actif et l'admission temporaire pour réparation, en version
applicable, et la mise en œuvre française. Ne pas présumer une exonération
depuis une facture SAV ; ne pas suggérer une déclaration de vente fictive.
Méthode BASE-005 locale, BASE-013.

## Critères d'acceptation

- [ ] Un couteau sous garantie revenant du Canada avec MRN d'export produit le dossier retour et réexpédition, conditions reliées aux sources lues.
- [ ] Sans preuve d'exportation initiale, la sortie nomme l'inconnue bloquante et les pièces de substitution à rechercher.
- [ ] Échange standard et réparation sont distingués.
- [ ] La sortie se termine par la phrase BASE-013 (service des douanes, commissionnaire) ; aucune exonération garantie.
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 consignée.

## Vérification

- Cas normal : réparation sous garantie et réexpédition.
- Cas limite : retour pour remboursement sans réexpédition.
- Information manquante : numéro de série absent.
- Sans source : régime non lu ; aucune exonération.
- Héritage américain : procédure « American goods returned » fournie ; non transposée.

Scénarios **attendus, non exécutés**. La relecture humaine est prise en charge
par l'utilisateur selon CLAUDE.md.

## Hors périmètre

Réparation hors de l'Union d'un bien de l'entreprise (C06), remboursement ou
remise d'une dette (DOU-010, DOU-011), garantie commerciale et rétractation
(DOM-001, V03).
