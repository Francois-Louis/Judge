---
id: FUN-001
titre: "Lire un devis funéraire et préparer les demandes d'explication avant engagement"
statut: a-verifier
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

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 1–6, 10–11, 13–17, 20–23, 134 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FQ01 — À partir d’un devis ou d’une demande de signature sans devis, séparer modèle réglementaire, notice d’information, bon de commande, options, quantités, frais de tiers et taxes alléguées ; mention absente ne vaut pas manquement établi.
- [ ] FQ02 — Comparer, si fournis, plusieurs devis pour les mêmes besoins : lignes équivalentes ou non, inclusions, exclusions, quantités, total recopié et inconnues ; ne classer ni recommander les opérateurs. Une différence arithmétique documentée ne suffit pas à conclure à une surfacturation.
- [ ] FQ03 — Examiner séparément cercueil/crémation, capiton, urne, toilette, conservation, cérémonie, véhicules et chambre funéraire : exigence technique sourcée, circonstance particulière et choix esthétique distingués ; pas d’obligation générale présumée.
- [ ] FQ04 — Préparer une demande de devis complet, de notice et de variantes répondant au besoin exprimé, sans signature conseillée sous pression. Expliquer que signataire, décideur et personne supportant les frais restent trois qualités distinctes.

Scénarios supplémentaires **attendus, non exécutés** : deux devis dont l’un exclut le transport et annonce des soins obligatoires ; refus oral de devis et signature exigée le soir même ; devis daté autour d’un changement de modèle ou de notice.

Sources à ouvrir lors de l’implémentation : textes CGCT et consommation sur devis/commande/information, arrêtés et annexes applicables au modèle et à la notice, règles techniques selon les opérations ; identifier champ, dates et transitions sans adopter celles annoncées dans le texte.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).

## Implémentation — 17 octobre 2026

La demande explicite « implémente la story fun-001 » sélectionne cette tranche
et autorise la création du paquet, son inscription au marketplace et la mise
à jour du décompte BASE-008. Historique de proposition ci-dessus conservé.
Le paquet `funeral-legal` `0.1.0` livre un seul skill `funeral-quote-review`,
sans profil ni stockage durable. FQ01–FQ04 sont intégrés : documents distincts,
comparaison des devis fournis à mêmes besoins, lecture de chaque prestation
et brouillon de demande complète/variantes. Aucun choix d'opérateur ni envoi.

Les références embarquent BASE-005 `1.2.0` et BASE-008 à l'identique, les trois
qualités, les frontières et les sources datées. La notice d'octobre 2026 et
sa correction de septembre sont prises en compte. Modèle intégral récent,
certains articles CGCT et consolidation de l'arrêté de prix restent réservés
après les échecs d'accès consignés, sans règle reconstituée de mémoire.

Preuves et bilan : [vérification](fun-001-annexes/verification.md),
[fixtures Q01–Q12](fun-001-annexes/fixtures.json),
[contrôles du paquet](fun-001-annexes/resultats-paquet.json) et
[journal des tentatives client](fun-001-annexes/executions/results.json).
Structure sans erreur bloquante, schéma et installation locale jetable
contrôlés ; les trois signalements statiques des copies partagées restent
documentés. Les commandes Q01–Q12 sont reconnues au chargement mais toutes
les tentatives sont refusées par le quota du client avant lecture des
ressources métier : aucun scénario comportemental réussi, aucune sortie
juridique simulée présentée comme exécution. Lecteur réel non exécuté.

Le statut reste `a-verifier` : rejouer les scénarios après disponibilité du
client, relire les sources réservées et vérifier la compréhension d'un proche.
Les cases d'acceptation et de friction ci-dessus restent ouvertes en attente
de ces observations ; instructions présentes ne valent pas comportement validé.

## Reprise des tests client — 17 octobre 2026

Douze scénarios préparés, sans nouvelle invocation : arrêt global après le refus de quota observé sur CRIM-001. Les anciennes preuves sont conservées et les cas sont marqués not-run-quota, pas réussis.

La relecture est prise en charge par l'utilisateur et ne bloque pas la
clôture. Le statut reste `a-verifier` pour les défauts/rejeux et tests
non exécutés, après épuisement du quota annoncé jusqu'à 16 h 40
(Europe/Paris). Aucun critère métier non observé n'est déclaré réussi.

[Bilan transversal et commande de reprise](../../recette-2026-10-17.md).
