---
id: INS-001
titre: "Analyser un refus de garantie à partir du contrat et du courrier"
statut: a-verifier
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# INS-001 — Analyser un refus de garantie à partir du contrat et du courrier

## Objectif et résultat attendu

Un particulier qui reçoit un refus de son assureur comprend le motif invoqué,
la clause citée, ce qu'il faut vérifier pour ce type de motif et les pièces
manquantes, et obtient un brouillon de demande d'explication ou de réexamen.
Cette tranche crée le paquet `insurance-legal` avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `insurance-legal` (`judge-fr-eu-insurance-legal`). Les
chemins « à créer » sont des livrables futurs.

- `insurance-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0` (à créer)
- `insurance-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `insurance-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `insurance-legal/NOTICE` — entrée datée du lot (à créer)
- `insurance-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `insurance-legal/references/shared/research-citation-method.md` — copie BASE-005 `1.0.0` identique (à créer)
- `insurance-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `insurance-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `insurance-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `insurance-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `insurance-legal/references/qualification-assurance.md` — qualification commune et garde-fous (à créer)
- `insurance-legal/references/motifs-refus.md` — catégories de motifs, conditions à vérifier, sources lues (à créer)
- `insurance-legal/skills/claim-denial-review/SKILL.md` — le skill (à créer)
- `insurance-legal/skills/claim-denial-review/references/demande-reexamen.md` — modèle de demande (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Courrier de refus complet, avec la clause citée.
- Conditions générales dans la version applicable à la date du sinistre ; conditions particulières ; avenants.
- Déclaration de sinistre et ses dates ; pièces envoyées ; échanges ; rapport d'expertise s'il existe.
- Organisme (assureur, mutuelle) ; intermédiaire ; contrat individuel ou collectif.
- Nature du risque et du sinistre.

## Sortie attendue

1. Résumé : ce que l'assureur refuse et pourquoi, en quelques phrases.
2. Fiche du refus : motif cité, clause, catégorie invoquée (absence de garantie, exclusion, déchéance, nullité, autre, indéterminée), version du contrat.
3. Ce qui reste à vérifier pour cette catégorie, avec la source lue ; rien n'est conclu.
4. Pièces manquantes, en premier lieu les conditions particulières.
5. Brouillon de demande d'explication ou de réexamen.
6. Suites : médiation (INS-005), responsabilité de l'auteur du dommage (DOM-035 ou secteur) en tâche distincte.
7. Limites.

## Travail attendu

Créer `qualification-assurance.md` et `motifs-refus.md` selon le
[découpage](../dom-005-annexes/dom-005-decoupage-assurance.md) et les appliquer :

- emprunteur, santé, prévoyance, construction, vie ou décès → orientation vers INS-008 à INS-011 ;
- contrat professionnel → qualification, puis questions propres ;
- prescription opposée par l'assureur → question, sans calcul ;
- fausse déclaration alléguée → catégorie et faits à établir, sans conclusion ;
- garantie émise par un vendeur et non par un assureur → DOM-001.

Charger la méthode locale BASE-005 et citer les sources réellement lues.

## Références métier et sources à rechercher

Code des assurances, mentions des exclusions et déchéances, exclusions,
obligations de l'assuré, nullité et réduction (pistes L112-4, L113-1,
L113-2, L113-8, L113-9) ; prescription (pistes L114-1, L114-2).

## Critères d'acceptation

- [ ] R01 classe le motif invoqué comme exclusion et liste ce qui reste à vérifier, sans conclure.
- [ ] R02 demande les conditions particulières avant toute lecture de plafond ou de franchise.
- [ ] R03 oriente l'assurance emprunteur vers INS-008.
- [ ] La sortie se comprend sans formation juridique ; le paquet détaché fonctionne seul.

## Vérification

- Cas normal : R01 — Dégât des eaux refusé pour « défaut d'entretien, article 7.3 des conditions générales ».
- Cas limite : R02 — Vol à domicile, conditions particulières perdues, refus partiel.
- Cas limite : R03 — Refus de prise en charge d'échéances de prêt après un arrêt de travail.
- Sans source lue : fiche et questions, règle réservée.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-005](../dom-005-annexes/dom-005-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Régimes isolés au-delà de l'orientation, calcul d'indemnité ou de délai,
responsabilité de l'auteur du dommage, procédure, envoi.

## Complément issu des frictions assurance

Points 2, 17, 23–24, 31–32, 37, 58–59 et 79 de la [matrice](../dom-005-annexes/dom-005-frictions-utilisateurs.md). Recueillir aussi présentation matérielle de la clause, questions et réponses initiales si le risque est discuté, factures d'entretien, photos antérieures et faits invoqués.

- [ ] R04 — Retard : distinguer clause de déchéance, date de connaissance, déclaration, préjudice allégué par l'assureur et circonstances de force majeure ; aucune déchéance automatique.
- [ ] R05 — Exclusion ou définition restrictive : qualifier le motif avant de vérifier précision, limitation, présentation et application aux faits ; aucune exclusion tenue pour valable du seul fait de sa présence.
- [ ] R06 — Entretien, dommage antérieur ou déclaration du risque : demander preuves et raisonnement exacts, sans déduire cause ni intention ; correction du risque → INS-015.
- [ ] R07 — Refus oral : préparer une demande écrite de clause/version, faits, pièces et postes refusés, sans inventer une obligation générale de motivation.

Scénarios R04–R07 **attendus, non exécutés** : refus pour retard sans préjudice expliqué ; vol sans effraction invoqué tantôt comme définition tantôt comme exclusion ; facture d'entretien ignorée ; refus uniquement téléphonique. La qualification d'une GAV exige ses clauses et reste dans la borne de lecture, sans évaluation corporelle. Contrat professionnel au-delà de la qualification → INS-019 ; calendrier → INS-021. Sources à ouvrir : catégories de refus, charge de preuve et version applicable.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-005-annexes/dom-005-decoupage-assurance.md).

## Implémentation — 17 octobre 2026

La demande explicite « implémente la story ins-001 » sélectionne cette tranche,
autorise son inscription au marketplace et la mise à jour du décompte BASE-008.
L'état de proposition ci-dessus reste un historique. Le paquet autonome
`insurance-legal` `0.1.0` contient le seul skill `claim-denial-review`, sans
profil, stockage durable, calcul ou envoi. R01–R07 et les orientations sont
intégrés aux instructions ; les autres suites INS ne sont pas implémentées.

La méthode embarquée est la version courante BASE-005 `1.2.0`, copie entière
identique remplaçant la piste `1.0.0` de la proposition. Les copies BASE-008
et la licence sont identiques à leurs sources. Les références métier portent
les qualifications, catégories, questions et réserves ; seul L113-8 a pu
être ouvert et lu, les autres textes demeurent réservés après les tentatives
officielles consignées. Aucun extrait de moteur traité comme texte lu.

Preuves : [bilan par couche](ins-001-annexes/verification.md),
[fixtures R01–R12](ins-001-annexes/fixtures.json),
[paquet détaché et installation](ins-001-annexes/resultats-paquet.json),
[tentatives runtime](ins-001-annexes/executions/results.json) et
[journal des sources](ins-001-annexes/sources/lectures.md).

Structure sans erreur bloquante, schémas et installation locale jetable
contrôlés. Les douze commandes ont été reconnues au chargement, mais le
quota Claude a empêché toute lecture des références et toute réponse métier.
Les cases d'acceptation restent ouvertes : instructions présentes ne valent
pas comportement observé. Relecture des sources réservées, recette runtime
et compréhension par un utilisateur sans formation juridique restent à faire.
Statut `a-verifier`, sans scénario simulé présenté comme exécution réussie.
