---
id: PILOTE-003
titre: "Vérifier le pilote avant d'étendre l'adaptation"
statut: terminee
priorite: P1
nature: validation
dependances: [PILOTE-002]
---

# PILOTE-003 — Vérifier le pilote avant d'étendre l'adaptation

## Objectif

Vérifier que le découpage, les sources et l'installation fonctionnent sur un cas réel de skill.

## Points de départ

- [employment-legal/skills/hiring-review/SKILL.md](../../employment-legal/skills/hiring-review/SKILL.md)
- [employment-legal/README.md](../../employment-legal/README.md)
- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [backlog/](../../backlog/)

## Travail attendu

- Exécuter les contrôles de BASE-006 sur l'artefact du plugin, puis les scénarios du pilote.
- Relire les conclusions, limites et sources ; rechercher les effets indirects du profil, des agents et des commandes d'initialisation hérités.
- Établir un bilan court : points confirmés, défauts à corriger et décisions d'architecture restant ouvertes.
- Créer les stories d'implémentation suivantes à partir de l'inventaire, en gardant une tâche métier et un résultat vérifiable par story.

## Critères d'acceptation

- [x] Les résultats observés et les vérifications impossibles sont rapportés séparément dans le bilan du 15 octobre 2026.
- [x] Aucun simple contrôle de structure n'est présenté comme une validation juridique.
- [x] Les défauts du pilote ont une correction identifiée avant généralisation ; leur correction effective reste à vérifier.
- [x] L'extension à un autre skill ou domaine est un choix explicite ; elle n'est pas lancée automatiquement par cette story.

## Vérification

Installer le plugin seul dans un environnement de test et rejouer au moins un scénario sans profil préalable et un scénario sans accès à une source.

## Bilan d'exécution — 15 octobre 2026

Le [bilan de recette](pilote-003-annexes/pilote-003-verification.md) distingue les constats,
les contrôles impossibles, les défauts et leurs corrections. Les
[preuves techniques](pilote-003-annexes/pilote-003-controles.json) portent sur un paquet détaché
de 36 fichiers, version `0.2.0`, sans modifier le plugin de PILOTE-002.
La [relecture des scénarios](pilote-003-annexes/pilote-003-relecture.md) couvre H01–H14 et ajoute
deux pièces complémentaires ; les [lectures officielles](pilote-003-annexes/pilote-003-sources-lues.json)
sont conservées séparément des sorties rédactionnelles.

Les suites existantes TRAV-001 à TRAV-016 sont reprises sans les lancer.
[PILOTE-004](pilote-004-preferences-candidat.md) borne la correction du parcours
de préférences ; [TRAV-017](suites/trav-017-clause-non-concurrence.md) propose
l'approfondissement d'une seule clause. Le [découpage actualisé](pilote-001-annexes/pilote-001-decoupage-travail.md)
relie ces propositions aux défauts constatés et maintient le choix explicite
d'une prochaine tranche.

**Portée :** contrôles statiques et essais du helper sur données fictives
effectués ; relecture par l'agent de maintenance, sans avis juridique
indépendant. Installation, invocation réelle sans profil/sans source et
compréhension par un participant réel **non exécutées** : aucun client isolé
et authentifié de test, moteur Docker indisponible, aucun participant. Les
schémas officiels plugin et marketplace ont été passés en reprise
([preuve](pilote-003-annexes/pilote-003-schema-cli.json)). Une copie détachée n'est pas
une installation ni un environnement inaccessible au checkout et au profil
réel. PILOTE-002 et PILOTE-003 restent `a-verifier` jusqu'à la recette décrite
dans le bilan ; les cases de compte rendu cochées ne valent pas clôture.
La généralisation n'est pas engagée. La recette en client est portée par
[BASE-011](../00-fondations/base-011-recette-client-isole.md).

## Hors périmètre

Publier une version, installer des plugins sur le compte de l'utilisateur ou poursuivre tous les domaines dans la foulée.

## Recette en client — 16 octobre 2026

[BASE-011](../00-fondations/base-011-recette-client-isole.md) a exécuté la vérification de cette story : plugin installé seul dans un
client jetable connecté (copie identique à l'inventaire, `SCHEMA OK`), H12
sans profil et H11a/H11b sans source. Les trois scénarios réussissent : aucun
fichier créé, refus d'accès tracés, conclusions dépendantes réservées
([résultats](../00-fondations/base-011-annexes/base-011-resultats.json)). La story passe à `terminee`. Restent dans PILOTE-002 le nominal H01
complet (D02) et le lecteur réel (D07) ; l'extension reste un choix explicite.
