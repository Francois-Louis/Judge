---
id: LIV-001
titre: "Préparer une livraison limitée au périmètre adapté"
statut: terminee
priorite: P2
nature: livraison
dependances: [BASE-004, PILOTE-003]
---

# LIV-001 — Préparer une livraison limitée au périmètre adapté

## Objectif

Rendre installable et vérifiable un petit lot, sans laisser croire que tout le dépôt est adapté.

## Points de départ

- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [README.md](../../README.md)
- [QUICKSTART.md](../../QUICKSTART.md)
- [LICENSE](../../LICENSE)
- [backlog/](../../backlog/)

## Travail attendu

- Lister les skills et plugins effectivement adaptés, leur version et leurs limites. Choisir le lot après vérification des stories concernées.
- Vérifier que l'identité du fork, les chemins et la coexistence prévus en BASE-004 sont réellement en place pour ce lot ; sinon ouvrir les corrections nécessaires avant livraison.
- Aligner les métadonnées et les instructions d'installation du lot. Conserver les attributions et signaler les modifications conformément à la licence.
- Vérifier l'artefact installable et documenter les résultats des contrôles disponibles.
- Préparer les notes de version et les commandes éventuelles pour le fork, sans publication distante dans cette story.

## Critères d'acceptation

- [x] Le périmètre annoncé correspond exactement aux stories terminées et vérifiées. Lot : `employment-legal` 0.2.1 (PILOTE-002 à 004) ; vérification client sur fixtures avec lecteur non indépendant, comme consigné par ces stories.
- [x] L'installation ne récupère pas silencieusement les versions ou configurations de l'origine. Observé en configuration jetable ; refus réel des liens symboliques non testé (BASE-008, critère 4).
- [x] Les manifestes du lot et le catalogue restent cohérents ; les contenus éditeur sont distingués des adaptations.
- [x] Les commandes de publication éventuellement préparées ciblent le fork choisi et ne créent pas de PR vers l'origine. Préparées, non exécutées.
- [x] Aucune publication, aucun push ni aucun détachement de fork n'est effectué par cette story.

## Vérification

Installer seulement le lot depuis son artefact, ouvrir ses références, invoquer une commande adaptée et vérifier les scénarios retenus. Noter les outils indisponibles au lieu de les compter comme réussis.

## Hors périmètre

Attendre que tous les domaines soient terminés pour livrer, modifier un compte distant ou annoncer une validation juridique globale.

## Bilan d'exécution — 16 octobre 2026

- **Lot choisi** : `judge-fr-eu-employment-legal` 0.2.1 seul, `hiring-review`
  et parcours candidat. COM-001 (`a-verifier`), les dix plugins à isolation
  technique seule, CoCounsel et les cookbooks sont exclus. Les skills hérités
  du plugin livré restent dans le paquet recetté et sont signalés comme non
  adaptés. Détail dans la [vérification](liv-001-annexes/liv-001-verification.md).
- **Métadonnées** : version 0.2.1 ; manifeste, entrée du marketplace, README
  et NOTICE du plugin alignés sur la recette BASE-011 ; README et NOTICE
  racine ; version attendue dans `scripts/test-base008-isolation.py`. Aucune
  instruction de skill ni référence juridique modifiée : 34 fichiers sur 37
  identiques au paquet recetté.
- **Artefact** : [`scripts/build-lot.py`](../../scripts/build-lot.py) produit
  hors du checkout un dossier et une archive reproductible : plugin choisi,
  marketplace `judge-fr-eu` à une entrée, LICENSE, NOTICE, [notes de version](liv-001-annexes/liv-001-notes-version.md)
  et inventaire SHA-256. Il refuse sortie dans le checkout, fichiers non
  suivis, liens et divergence marketplace/manifeste.
- **Vérification** : [vérificateur](liv-001-annexes/liv-001-verifier-lot.py) et
  [relevé](liv-001-annexes/liv-001-resultats.json). Archive conforme à l'inventaire,
  périmètre à un plugin, aucun chemin actif de l'origine, `SCHEMA OK`,
  `claude plugin validate` réussi, installation jetable réussie et copie
  installée identique. Suites rejouées après modification : BASE-008 14
  réussis et 2 ignorés, contrôleur 13 réussis, lint des cookbooks, JSON et
  `git diff --check` propres.
- **Publication** : commandes préparées vers `Francois-Louis/Judge` avec
  `--repo` explicite ; rien n'est exécuté.

**Reste à vérifier** : invoquer `hiring-review` depuis l'artefact 0.2.1 dans
une session authentifiée par l'utilisateur (procédure dans la vérification).
La story reste `a-verifier` jusque-là ; BASE-011 a exécuté les scénarios sur
des fichiers de skill identiques, ce qui ne remplace pas cette invocation.

**Portée :** contrôles techniques en configuration jetable sur le même compte
Windows ; aucune session de modèle sur 0.2.1, aucun lecteur indépendant,
aucune relecture juridique. Les fichiers du lot ne sont pas commités :
l'artefact vérifié provient de l'arbre de travail (`e31ea94` plus cinq
fichiers listés dans son inventaire) et doit être reconstruit avec `--rev`
après commit. Aucun tag, push ni release.

## Clôture — 16 octobre 2026

Close par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : la recette
BASE-011 est acceptée pour le lot 0.2.1, dont les fichiers de skill sont
identiques à ceux recettés. L'invocation sur l'artefact 0.2.1 n'a pas été
exécutée et n'est pas présentée comme vérifiée. Les skills hérités restent
dans le lot, signalés. Publication uniquement vers `Francois-Louis/Judge`.
