---
id: VEH-001
titre: "Comparer une facture de garage aux travaux autorisés"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# VEH-001 — Comparer une facture de garage aux travaux autorisés

## Objectif et résultat attendu

Un particulier surpris par la facture d'un garage voit, ligne par ligne, ce
qui a été facturé, ce qui avait été accepté selon les pièces et ce qui reste
sans trace, et obtient un brouillon de demande d'explication ou de
rectification. Cette tranche crée le paquet `vehicle-legal` avec ce seul
skill.

## Périmètre et fichiers

Plugin principal : `vehicle-legal` (`judge-fr-eu-vehicle-legal`). Les chemins
« à créer » sont des livrables futurs.

- `vehicle-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0` (à créer)
- `vehicle-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `vehicle-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `vehicle-legal/NOTICE` — entrée datée du lot (à créer)
- `vehicle-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `vehicle-legal/references/shared/research-citation-method.md` — copie BASE-005 identique (à créer)
- `vehicle-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `vehicle-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `vehicle-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `vehicle-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `vehicle-legal/references/qualification-vehicule.md` — qualification commune et garde-fous (à créer)
- `vehicle-legal/references/accords-travaux.md` — devis, ordre de réparation, accord et preuve, sources lues (à créer)
- `vehicle-legal/skills/garage-invoice-review/SKILL.md` — le skill (à créer)
- `vehicle-legal/skills/garage-invoice-review/references/demande-explication.md` — modèle de demande (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Facture du garage ; devis, ordre de réparation ou bon de dépôt s'ils existent.
- Accords donnés : signature, message, courriel, appel allégué (date, interlocuteur, contenu).
- Motif du dépôt tel que la personne l'a exprimé ; diagnostic remis.
- Véhicule : immatriculation, kilométrage au dépôt ; usage privé ou professionnel.
- Paiement effectué ou non ; véhicule rendu ou retenu ; pièces remplacées restituées ou non.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente.

## Sortie attendue

1. Résumé : ce qui est facturé, ce qui était accepté selon les pièces, ce qui est contesté.
2. Fiche de qualification : garage, véhicule, dates, pièces fournies, usage déclaré.
3. Tableau : opération facturée, montant recopié, devis ou accord retrouvé, preuve, écart.
4. Accords allégués sans trace marqués comme inconnus, sans conclusion.
5. Brouillon de demande d'explication ou de rectification, sans tarif ni obligation affirmés faute de source lue.
6. Ce qui reste à vérifier : information préalable exigée, forme de l'accord, avec la source lue ou réservés.
7. Suites : véhicule retenu → VEH-002 ; panne persistante → VEH-003 ; état à conserver → VEH-010 ; médiateur à identifier.
8. Limites et phrase BASE-013.

## Travail attendu

Créer `qualification-vehicule.md` et `accords-travaux.md` selon le
[découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md) et les
appliquer :

- véhicule retenu ou frais de gardiennage → objet distinct, VEH-002, traité en premier ;
- contestation de la qualité de la réparation → VEH-003, sans avis technique ;
- assureur payeur ou expert d'assurance → la facture reste lue ici, la garantie relève de DOM-005 ;
- usage professionnel du véhicule → qualification conditionnelle, orientation commercial ;
- enlèvement en fourrière décidé par une autorité → orientation DOM-010 ; facture de dépannage contractuel, y compris autoroutier → VEH-015.

Charger la méthode locale BASE-005 et citer les sources réellement lues.
Un accord allégué sans trace n'est ni retenu ni écarté ; un montant n'est
jamais recalculé à partir d'un tarif supposé.

## Références métier et sources à rechercher

Code de la consommation, information sur les prix et conditions des
prestations (piste L112-1 et textes d'application) ; arrêté relatif à la
publicité des prix des prestations de réparation et d'entretien automobile,
à identifier dans sa version en vigueur ; Code civil, contrat d'entreprise
(pistes 1710, 1787 et suivants) et preuve (pistes 1353, 1359 et suivants) ;
fiches DGCCRF comme information.

## Critères d'acceptation

- [ ] V01 produit le tableau des écarts et un brouillon adressé au garage, sans tarif ni obligation non sourcés.
- [ ] V02 marque un accord téléphonique allégué comme inconnu, sans le tenir pour donné ni pour refusé.
- [ ] V03 sépare la facture et le véhicule retenu en deux objets et traite d'abord la restitution.
- [ ] Le garage n'est pas présumé de mauvaise foi ; aucun remboursement n'est promis.
- [ ] La sortie se comprend sans formation juridique ; le paquet détaché fonctionne seul.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat selon la situation.

## Vérification

- Cas normal : V01 — Facture supérieure au devis signé, avec une ligne absente du devis.
- Cas limite : V02 — Opération supplémentaire facturée après un appel dont le contenu est contesté.
- Cas limite : V03 — Garage refusant de rendre le véhicule tant que la facture contestée n'est pas payée.
- Sans source lue : tableau et brouillon, obligations d'information et tarifs réservés.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-023](../dom-023-annexes/dom-023-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Gardiennage et rétention, qualité de la réparation, garantie d'assurance,
véhicule professionnel, avis technique, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 3, 5–6, 11, 14–15, 23–24, 29, 138, 165–166, 171–172 et 180 de la [matrice](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Exigences supplémentaires du futur skill, sans implémentation.

- [ ] F01 — Diagnostic/devis facturé, accord seulement oral, forfait et main-d'œuvre opaques : demander preuve de l'information préalable, méthode et contenu ; ne pas déclarer devis/ordre systématiquement obligatoires. Vérifier champ et seuil de la note détaillée sur texte/version, jamais sur le chiffre du guide.
- [ ] F02 — Pièce annoncée neuve/constructeur, échange standard ou consigne : comparer nature, référence, prix annoncé et mention facturée ; demander traçabilité et conditions du remboursement de consigne sans diagnostiquer l'installation.
- [ ] F03 — Prestation suspectée non réalisée et paiement pour reprendre la voiture : conserver rapports, réserves et preuve du règlement ; aucune fraude ou renonciation déduite. VEH-003/010 pour constat, VEH-002 si rétention.

Les cas F ci-dessus constituent les scénarios complémentaires **attendus, non exécutés**. Recueillir les pièces nommées, produire la comparaison et le brouillon prévus par la story ; sans source accessible, réserver droit, tarif, calendrier et effet de la clause. Rechercher les textes sectoriels et jurisprudence pertinents avec version, champ et dates ; le texte utilisateur n'est pas une source juridique. [Portée et vérification](../dom-023-annexes/dom-023-frictions-verification.md).
