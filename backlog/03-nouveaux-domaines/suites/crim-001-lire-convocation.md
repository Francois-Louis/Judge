---
id: CRIM-001
titre: "Lire et qualifier une convocation par la police ou la gendarmerie"
statut: a-verifier
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# CRIM-001 — Lire et qualifier une convocation par la police ou la gendarmerie

## Objectif et résultat attendu

Une personne majeure convoquée par la police ou la gendarmerie comprend ce
que le document dit et ne dit pas, ce qu'elle doit faire maintenant, et quelles
questions poser au service et à un avocat. Cette tranche crée le paquet
`criminal-legal` avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `criminal-legal` (`judge-fr-eu-criminal-legal`). Les
chemins « à créer » sont des livrables futurs.

- `criminal-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0` (à créer)
- `criminal-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `criminal-legal/CLAUDE.md` — modèle minimal, aucun profil ni stockage (à créer)
- `criminal-legal/NOTICE` — entrée datée du lot (à créer)
- `criminal-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `criminal-legal/references/shared/research-citation-method.md` — copie BASE-005 `1.0.0` identique (à créer)
- `criminal-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `criminal-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `criminal-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `criminal-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `criminal-legal/references/qualification-penale.md` — qualification commune et garde-fous (à créer)
- `criminal-legal/skills/summons-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/skills/summons-reading/references/convocation.md` — repères, sources lues, modèle de fiche (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Document complet, recto et verso, ou texte exact du message reçu.
- Autorité et service émetteurs, nom ou qualité du signataire, référence.
- Date, heure et lieu de la convocation ; mode et date de réception.
- Qualité indiquée (témoin, victime, personne soupçonnée) ou absence de mention.
- Objet ou affaire mentionnés ; pièces demandées.
- Âge de la personne ; besoin d'un interprète ; mesure de protection juridique.

Sans document, le skill travaille sur la description, marquée comme
déclarée, et demande d'abord la date de convocation.

## Sortie attendue

1. Maintenant : si la date est proche, les deux ou trois actions utiles (relire le document complet, contacter un avocat, appeler le service au numéro du document pour préciser l'objet).
2. Fiche du document : chaque mention avec son statut (lue, déclarée, absente).
3. Ce que le document ne permet pas de savoir, en premier lieu la qualité.
4. Questions au service émetteur et à un avocat.
5. Pièces à apporter selon le document.
6. Droits à vérifier selon le statut, une fois celui-ci établi, avec la source lue.
7. Limites.

## Travail attendu

Créer `qualification-penale.md` selon le [découpage](../dom-002-annexes/dom-002-decoupage-penal.md)
et l'appliquer :

- convocation devant un tribunal, citation, ordonnance ou jugement → fiche minimale et orientation (CRIM-006, proposée) ;
- mineur → orientation (CRIM-011, proposée) et recours à un avocat ;
- convocation administrative, douanière, de préfecture ou d'employeur → domaine concerné ;
- message non vérifiable (SMS, courriel avec lien ou demande de paiement) → vérifier l'authenticité par un canal officiel avant toute suite ;
- violences intrafamiliales évoquées → DOM-038 d'abord.

Ne jamais conseiller de ne pas se présenter ; les conséquences d'une absence
sont une question pour l'avocat et pour la source lue. Ne pas préparer le
contenu des déclarations. Charger la méthode locale BASE-005 et citer les
sources réellement lues dans `convocation.md`.

## Références métier et sources à rechercher

Code de procédure pénale, audition libre et comparution sur convocation
(pistes 61-1, 78) ; directives 2012/13/UE, 2013/48/UE et 2010/64/UE. Pages
publiques d'information comme orientation, distinctes du texte. Aucun
équivalent étranger.

## Critères d'acceptation

- [ ] C01 produit une fiche où la qualité reste inconnue, avec questions et actions immédiates, sans liste de droits non rattachée à un statut.
- [ ] C02 traite d'abord l'authenticité du message.
- [ ] C03 oriente la citation devant le tribunal vers CRIM-006 avec une fiche minimale.
- [ ] Aucune sortie ne conseille de ne pas se présenter ou d'altérer une preuve.
- [ ] La sortie se comprend sans formation juridique ; le paquet détaché fonctionne seul.

## Vérification

- Cas normal : C01 — Courrier « pour affaire vous concernant », commissariat, date dans six jours, aucune qualité.
- Cas limite : C02 — SMS « convocation gendarmerie » avec un lien et un numéro inconnu.
- Cas limite : C03 — Document intitulé « citation à comparaître » devant le tribunal correctionnel.
- Sans source lue : fiche et questions, droits réservés.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-002](../dom-002-annexes/dom-002-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Mesure en cours, mineur, acte de juridiction, qualification d'infraction,
préparation des déclarations, prédiction de la suite, contact du service,
envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 32–36 de la [matrice](../dom-002-annexes/dom-002-frictions-utilisateurs.md). Ne pas présenter la convocation comme une formalité sans effet ni déduire le statut du ton du message. Distinguer se présenter, répondre et pouvoir quitter une audition ; les droits sont vérifiés pour le statut établi. Audition déjà commencée → CRIM-002, sans préparation des réponses.

- [ ] C04 — Convocation présentée comme informelle : demander qualité, faits annoncés, accès à l'avocat et interprète selon le statut, sans promettre l'absence de poursuites.

Scénario **attendu, non exécuté** : appel « venez juste discuter », qualité inconnue, personne persuadée de ne pas avoir besoin d'avocat.

## Implémentation — 17 octobre 2026

Tranche sélectionnée par la demande utilisateur d'implémenter CRIM-001.
Paquet `criminal-legal` `0.1.0` créé avec son seul skill `summons-reading` ;
inscription au marketplace et décompte BASE-008 inclus dans cette sélection,
CONSO-001 et BNK-001 déjà intégrées : **14 paquets, 137 skills** pour CRIM-001
seule ; **15 paquets, 138 skills** avec ENF-001 commitée pendant ce chantier. Aucun tri
global du marketplace, agent, hook ou connecteur ajouté. Le préalable
PILOTE-003 est satisfait ; BASE-008 fournit le contrat technique déjà utilisé,
sans prétendre que sa validation globale restante est achevée.

Tous les fichiers du périmètre « à créer » sont présents. La méthode commune
est embarquée à l'identique en **1.2.0**, version courante incluant BASE-013
et BASE-016, plutôt que l'ancienne 1.0.0 visée lors du cadrage. Les autres
copies BASE-008 et la licence sont identiques aux sources racine. Le skill
charge les seules références locales ; aucun profil ni stockage du dossier.

Les directives ont été récupérées et lues dans leur publication initiale
française via CELLAR ; Service-Public a été lu comme information générale.
CPP 61-1 et 78 : accès web et Python refusé, texte/version et conclusions
réservés. Aucun contenu reconstitué depuis les résultats du moteur.

Voir le [bilan par couche](crim-001-annexes/verification.md), les
[fixtures C01–C10](crim-001-annexes/fixtures.json), le
[contrôleur reproductible](crim-001-annexes/controles.py) et les
[preuves de paquet](crim-001-annexes/resultats-paquet.json).
Les cases comportementales restent ouvertes tant que les sorties réelles
et la compréhension par un lecteur sans formation juridique ne sont pas
vérifiées. Statut `a-verifier`, sans recette fictivement déclarée réussie.
