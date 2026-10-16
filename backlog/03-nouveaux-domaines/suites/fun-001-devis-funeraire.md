---
id: FUN-001
titre: "Lire un devis funéraire et préparer les demandes d'explication avant engagement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# FUN-001 — Lire un devis funéraire et préparer les demandes d'explication avant engagement

## Objectif et résultat attendu

Un proche qui reçoit un devis d'obsèques voit, poste par poste, ce qui
correspond au besoin qu'il a exprimé, ce que l'opérateur propose en plus et
ce dont le caractère obligatoire reste à vérifier, et obtient un brouillon
de demande d'explication avant de s'engager. Cette tranche crée le paquet
`funeral-legal` avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `funeral-legal` (`judge-fr-eu-funeral-legal`). Les chemins
« à créer » sont des livrables futurs.

- `funeral-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0` (à créer)
- `funeral-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `funeral-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `funeral-legal/NOTICE` — entrée datée du lot (à créer)
- `funeral-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `funeral-legal/references/shared/research-citation-method.md` — copie BASE-005 identique (à créer)
- `funeral-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `funeral-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `funeral-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `funeral-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `funeral-legal/references/qualification-funeraire.md` — qualification commune, fiche des trois qualités et garde-fous (à créer)
- `funeral-legal/references/lecture-devis-funeraire.md` — structure d'un devis, prestations demandées ou proposées, mentions, sources lues (à créer)
- `funeral-legal/skills/funeral-quote-review/SKILL.md` — le skill (à créer)
- `funeral-legal/skills/funeral-quote-review/references/demande-explication.md` — modèle de demande (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Devis de l'opérateur ; bon de commande s'il est déjà signé ; documents remis avec le devis.
- Besoin exprimé : inhumation ou crémation, cérémonie, lieu, prestations explicitement refusées.
- Personnes : qui organise, qui a signé ou doit signer, qui se dit habilité à décider, désaccord connu.
- Volontés connues du défunt et leur forme ; contrat obsèques éventuel.
- Lieu du décès et lieu envisagé pour la sépulture ou la crémation ; corps en attente ou non.
- Acompte versé ou demandé ; échéance de signature alléguée.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente.

## Sortie attendue

1. En tête : ce qui doit être décidé maintenant et ce qui peut attendre, en phrases courtes.
2. Fiche de qualification : défunt, opérateur et mention d'habilitation recopiée, dates, pièces fournies.
3. Fiche des trois qualités : signataire, personne qui décide, personne tenue au paiement, chacune fondée ou « à établir ».
4. Tableau : poste, montant recopié, demandé ou proposé selon les pièces, obligation à vérifier, question à poser.
5. Mentions recopiées et mentions absentes du devis, sans conclure à une irrégularité.
6. Brouillon de demande d'explication à l'opérateur, sans prix courant ni obligation affirmés faute de source lue.
7. Ce qui reste à vérifier : modèle de devis, prestations obligatoires, habilitation, avec la source lue ou réservés.
8. Suites : désaccord entre proches → FUN-003 ; financement → FUN-005 ; contrat obsèques → FUN-006 ; facture après les obsèques → FUN-002.
9. Limites et phrase BASE-013.

## Travail attendu

Créer `qualification-funeraire.md` et `lecture-devis-funeraire.md` selon le
[découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md) et les
appliquer :

- désaccord sur l'inhumation, la crémation ou le lieu → objet distinct, FUN-003, traité en premier avec renfort ;
- devis déjà signé par une autre personne → fiche des trois qualités, sans déduire l'engagement du lien familial ;
- contrat obsèques existant → les prestations prévues sont lues en FUN-006, la garantie relève de DOM-005 ;
- question de qui paie → FUN-005, sans réponse unique pour « la famille » ;
- décès ou sépulture hors de France → point ouvert du découpage, sortie limitée aux questions.

Charger la méthode locale BASE-005 et citer les sources réellement lues.
Une prestation proposée n'est pas présumée inutile ; une prestation dite
obligatoire par l'opérateur n'est ni confirmée ni contestée sans source lue.
Aucun montant n'est comparé à un prix courant supposé.

## Références métier et sources à rechercher

Code général des collectivités territoriales, service extérieur des pompes
funèbres (pistes L2223-19 et suivants), devis (piste L2223-21-1) et
habilitation (piste L2223-23) ; règlement national des pompes funèbres
(pistes R2223-24 et suivants) ; arrêté fixant le modèle de devis des
prestations funéraires, à identifier dans sa version en vigueur ; fiches
DGCCRF et [Service Public sur les frais d'obsèques](https://www.service-public.gouv.fr/particuliers/vosdroits/F17059?lang=fr)
comme information.

## Critères d'acceptation

- [ ] Q01 produit le tableau des postes et un brouillon adressé à l'opérateur, sans prix courant ni obligation non sourcés.
- [ ] Q02 sépare signataire, personne qui décide et personne tenue au paiement, sans réponse déduite du seul lien familial.
- [ ] Q03 traite d'abord le désaccord entre proches comme objet distinct, avec renfort en tête.
- [ ] L'opérateur n'est pas présumé abusif ; aucune économie ni aucun remboursement n'est promis.
- [ ] La sortie se comprend sans formation juridique et dans un moment de deuil ; le paquet détaché fonctionne seul.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat selon la situation.

## Vérification

- Cas normal : Q01 — Devis pour une inhumation comprenant des soins de conservation et une cérémonie non évoqués par la famille.
- Cas limite : Q02 — Devis à signer par un neveu présent, alors que les enfants du défunt sont joignables et n'ont rien décidé.
- Cas limite : Q03 — Devis de crémation demandé par un enfant pendant qu'un autre affirme que le défunt voulait être inhumé.
- Sans source lue : tableau et brouillon, prestations obligatoires et modèle de devis réservés.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-031](../dom-031-annexes/dom-031-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Facture après les obsèques, désaccord entre proches, financement, contrat
obsèques, monument, élément étranger, choix d'un opérateur, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
