---
id: BNK-001
titre: "Qualifier un paiement contesté et préparer la réclamation au prestataire"
statut: a-verifier
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# BNK-001 — Qualifier un paiement contesté et préparer la réclamation au prestataire

## Objectif et résultat attendu

Une personne qui conteste une opération sur son compte sait si elle relève
d'un paiement non autorisé, d'une opération validée sous tromperie ou d'un
litige avec le commerçant, fait d'abord ce qui est urgent, et obtient la
réclamation adaptée à son prestataire. Cette tranche crée le paquet
`banking-legal` avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `banking-legal` (`judge-fr-eu-banking-legal`). Les chemins
« à créer » sont des livrables futurs.

- `banking-legal/.claude-plugin/plugin.json` — manifeste initial `0.1.0`, final `0.1.1` après relecture
- `banking-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `banking-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `banking-legal/NOTICE` — entrée datée du lot (à créer)
- `banking-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `banking-legal/references/shared/research-citation-method.md` — copie BASE-005 courante `1.2.0` identique
- `banking-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `banking-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `banking-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `banking-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `banking-legal/references/qualification-bancaire.md` — qualification commune et garde-fous (à créer)
- `banking-legal/references/paiements.md` — instruments, consentement, sources lues (à créer)
- `banking-legal/skills/payment-dispute/SKILL.md` — le skill (à créer)
- `banking-legal/skills/payment-dispute/references/reclamation-paiement.md` — modèle de réclamation (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Relevé ou capture de l'opération : date, montant, libellé, bénéficiaire (numéros masqués).
- Instrument : carte, virement, autre ; compte personnel ou professionnel.
- Ce que la personne a fait : rien, validation dans l'application, code reçu et saisi, appel d'un « conseiller ».
- Dates de découverte, d'opposition, de signalement au prestataire.
- Échanges avec le prestataire et avec le commerçant.
- Prestataire et pays.

Le skill ne demande jamais de code, de mot de passe ni de numéro complet.

## Sortie attendue

1. Maintenant : opposition et signalement par les canaux officiels du prestataire, si ce n'est pas fait.
2. Fiche de l'opération : chaque fait avec sa source (relevé, déclaration) et son statut.
3. Branche retenue et faits qui la décident : non autorisée, validée sous tromperie, litige commercial ; branche ouverte si les faits manquent.
4. Pièces à réunir.
5. Brouillon de réclamation au prestataire pour l'opération non autorisée, sans délai ni franchise affirmés sans texte lu.
6. Suites : médiation (BNK-004), plainte (DOM-002), vendeur (DOM-001), BNK-002 pour la tromperie.
7. Limites.

## Travail attendu

Créer `qualification-bancaire.md` et `paiements.md` selon le
[découpage](../dom-004-annexes/dom-004-decoupage-banque.md) et les appliquer :

- opération validée sous tromperie → actions urgentes, fiche et orientation BNK-002 ;
- litige commercial → orientation DOM-001 ; un mécanisme de réseau est une règle privée à demander au prestataire, pas un droit ;
- compte professionnel → qualification, puis orientation ;
- prélèvement → BNK-006 ; actif numérique → BNK-011 ;
- négligence opposée par la banque → question, sans conclusion.

Charger la méthode locale BASE-005 et citer les sources réellement lues.

## Références métier et sources à rechercher

Code monétaire et financier, services de paiement (pistes L133-18, L133-19,
L133-23, L133-24) ; directive (UE) 2015/2366 ; ABE Infoservice et Banque de
France comme information.

## Critères d'acceptation

- [ ] P01 qualifie l'opération inconnue de non autorisée et produit la réclamation, sans délai ni franchise non sourcés.
- [ ] P02 laisse la branche ouverte quand la personne a validé un code, met l'urgence en tête et oriente vers BNK-002.
- [ ] P03 oriente le litige commercial vers DOM-001 sans promettre de remboursement bancaire.
- [ ] Aucun code ni numéro complet demandé ; la sortie se comprend sans formation juridique ; le paquet détaché fonctionne seul.

## Vérification

- Cas normal : P01 — Trois paiements par carte en ligne inconnus, carte toujours en possession de la personne.
- Cas limite : P02 — Paiement validé dans l'application pendant l'appel d'un prétendu conseiller.
- Cas limite : P03 — Paiement par carte d'une commande jamais livrée.
- Sans source lue : fiche et questions, règle réservée.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-004](../dom-004-annexes/dom-004-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Compte professionnel au-delà de la qualification, prélèvement, chèque,
crédit, actif numérique, opposition faite à la place de la personne, plainte,
envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 28–29, 31–32, 34–36, 38–41 de la [matrice](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

Pièces supplémentaires : captures et messages d'authentification masqués, refus écrit et preuves invoquées par le prestataire ; heures de l'opposition et des opérations, pays des deux prestataires et devise ; frais directement consécutifs.

- [ ] P04 — Code validé, plainte exigée et « négligence grave » invoquée : le brouillon demande séparément preuve du consentement, faits et preuves de la faute alléguée, fondement de la plainte exigée et motif écrit ; aucune conclusion sur la négligence.
- [ ] P05 — Remboursement différé pour enquête : la chronologie distingue signalement, réponse, remboursement et exception invoquée ; demande de réexamen selon les textes lus, sans délai chiffré non vérifié.
- [ ] P06 — Frais après la fraude ou débit affiché après opposition : distinguer autorisation et comptabilisation ; demander remise en état documentée, avec BNK-003 pour le détail des frais.
- [ ] P07 — Prestataire hors EEE ou achat non livré : qualifier pays et contrat avant le régime de délai ; pour la vente, demander les conditions et délais privés de chargeback sans les présenter comme un remboursement légal automatique.

Cas supplémentaires **attendus, non exécutés** : code saisi pendant un appel ; enquête prolongée ; opposition horodatée suivie d'un débit ; un prestataire hors EEE. Sources à rechercher : preuve, responsabilité, information et champ territorial des services de paiement ; règles contractuelles du réseau pour la rétrofacturation. Le calcul de délai et de franchise reste exclu.

## État de la proposition — 16 octobre 2026

État historique : issue de DOM-004, sans implémentation au 16 octobre.
Préalable PILOTE-003 satisfait après BASE-011. Contrat commun :
[découpage](../dom-004-annexes/dom-004-decoupage-banque.md).

## Implémentation — 17 octobre 2026

La demande d'implémentation sélectionne cette tranche et son paquet avec le
seul skill payment-dispute. Décision d'intégration : inscription au marketplace
sans réordonner les entrées existantes, et extension des contrôles BASE-008.
Le dépôt compte désormais 13 paquets / 136 skills, y compris consumer-legal
intégré par un travail parallèle. La méthode actuelle `1.2.0` remplace la
version `1.0.0` prévue au cadrage, sans modifier sa source ; copies identiques.
Tous les fichiers métier listés sont créés ; aucun autre skill, connecteur,
hook ou stockage n'est ajouté. Les relais restent des orientations proposées.

Version `0.1.0` enregistrée dans le commit concurrent bee80d1 pendant le travail ;
version finale `0.1.1` pour les corrections issues des sorties client. Pas de
réécriture de cet historique partagé.

Preuves : [bilan de vérification](bnk-001-annexes/verification.md),
[fixtures](bnk-001-annexes/fixtures.json),
[exécuteur](bnk-001-annexes/recette.py),
[résultats client](bnk-001-annexes/executions/results.json).
P01/P02/P03/P04/P06 ont produit une sortie en client, sans accès web ;
P05/P07–P12 sont bloqués par la limite de session du compte.
Les cases ci-dessus restent ouvertes : corrections finales non réexécutées,
sources partiellement inaccessibles, installation isolée et lecteur réel
non validés. L'implémentation est livrée, la recette complète reste à vérifier.

## Reprise des tests client — 17 octobre 2026

Sonde P01 en 0.1.1, puis P01–P03 en 0.1.2 intermédiaire. Les réserves de preuve et de téléservice sont améliorées. P03 appelle encore une correction livraison/remboursement et opposition ; formulation finale 0.1.3 non rejouée. P04–P12 sans nouveau résultat.

La relecture est prise en charge par l'utilisateur et ne bloque pas la
clôture. Le statut reste `a-verifier` pour les défauts/rejeux et tests
non exécutés, après épuisement du quota annoncé jusqu'à 16 h 40
(Europe/Paris). Aucun critère métier non observé n'est déclaré réussi.

[Bilan transversal et commande de reprise](../../recette-2026-10-17.md).
