---
id: BASE-008
titre: "Appliquer l'identité Judge FR/UE et isoler les configurations"
statut: en-cours
priorite: P0
nature: implementation
dependances: [BASE-004]
---

# BASE-008 — Appliquer l'identité Judge FR/UE et isoler les configurations

## Objectif

Installer et utiliser le fork avec l'original dans une même session sans
collision de commandes, lecture croisée de profils ou écrasement de données.
Cette isolation technique ne vaut pas adaptation des tâches juridiques.

## Périmètre

- Appliquer les décisions du [cadrage BASE-004](base-004-strategie-identite-configurations.md),
  sa correspondance des 12 plugins et son ordre de migration.
- Partir de l'[inventaire de fichiers](base-004-inventaire-references.tsv), à
  régénérer avant modification. Examiner aussi les chemins sans ancien nom,
  notamment installations/sauvegardes du hub et sorties des cookbooks.
- Modifier les deux niveaux de manifestes, profils modèles, entretiens,
  lectures/écritures des skills et agents, références de commandes et docs.
  Les répertoires de domaines et les noms des 150 skills restent conservés.
- Retirer seulement l'entrée éditeur du marketplace du fork, sans modifier
  `external_plugins/cocounsel-legal/` ni distribuer une copie renommée.

## Travail attendu

1. Utiliser `judge-fr-eu` pour le marketplace et la racine de configuration,
   `judge-fr-eu-<domaine>` pour les identifiants publiés et les commandes.
   Garder `source` pointant au répertoire existant et les auteurs d'origine ;
   distinguer maintien du fork, affichage et provenance. Démarrer le cycle
   technique du fork à `0.1.0`, sans annoncer l'adaptation juridique complète.
2. Appliquer tous les chemins du contrat BASE-004, y compris profil partagé,
   dossiers actifs/archivés, sorties, registres et journaux. Supprimer les
   reprises automatiques depuis le cache et tout fallback vers l'original.
3. Démarrer un entretien neuf si le profil du fork manque. Préserver un profil
   existant et ses réponses ; ne copier ni règles américaines ni dossiers.
   Réserver tout outil d'import assisté à une story supplémentaire.
4. Isoler le cycle de vie communautaire : nom/dossier préfixé, journal,
   sauvegarde, mise à jour, désactivation, restauration et désinstallation.
   Refuser une destination existante, les chemins sortant de la racine et les
   liens/jonctions. Ne pas installer dans un paquet interne ou utiliser le
   journal de l'original pour autoriser une opération.
5. Actualiser commandes, attribution, notices de fichiers modifiés et docs
   sans substitution globale aveugle. Préserver licence et mentions historiques
   utiles ; assurer la concordance marketplace/manifeste `name/description/author`.
6. Vérifier les paquets migrés hors ligne, puis dans un environnement Claude
   Code jetable avec les deux installations et les mises à jour automatiques
   du fork désactivées. Vérifier la syntaxe et les règles dans les références
   officielles listées par BASE-004 ; consigner la version réelle du client.

## Critères d'acceptation

- [ ] Original et fork sont simultanément installés et chargés ; leurs commandes
  qualifiées distinctes appellent le bon paquet.
- [x] Deux profils, profils partagés et dossiers de même slug conservent leurs
  marqueurs respectifs ; les accès réels restent dans le bon namespace.
- [x] Si seul le profil original ou son ancien cache existe, le fork propose
  un entretien neuf sans les lire/importer. Aucune destination n'est écrasée.
- [ ] Les lectures/écritures annexes et le cycle du hub utilisent seulement les
  chemins du fork ; les tests refusent traversée, lien symbolique et jonction.
- [x] Une mise à jour puis un retour à la version précédente préservent profils,
  dossiers et personnalisations durables ; les changements restent relisibles.
- [x] Les validations de manifestes et contrôles applicables passent ; chaque
  commande documentée résout un skill présent dans le paquet isolé.
- [x] Le relevé résiduel de l'ancien nom ne contient que des usages historiques
  ou d'attribution justifiés ; aucune lecture/écriture active ne vise l'original.
- [x] Notices et licence accompagnent les paquets ; les docs distinguent la
  migration technique des tâches France/UE effectivement adaptées.

## Vérification

Utiliser des profils factices, jamais un profil personnel. Rejouer les cas
de BASE-004 sur les **paquets migrés**, en observant leurs accès aux fichiers
et en comparant les empreintes ; le modèle de BASE-004 ne suffit pas.
Tester le hub avec un skill communautaire factice de même nom dans chaque
distribution : mise à jour, rollback, disable et uninstall du fork laissent
l'installation originale intacte. Tester les sorties/déploiements des cinq
cookbooks en mode hors ligne dans des répertoires distincts.

## Hors périmètre

Adapter le droit des 150 skills, renommer leurs dossiers, modifier le plugin
éditeur, importer automatiquement un profil, déployer un agent distant ou
publier une release. Méthode et autonomie des références : BASE-005/006.
Contributions/CLA : BASE-007 ; publication : LIV-001.

## Bilan d'exécution — 15 octobre 2026

Implémentation technique réalisée. La story reste `en-cours` jusqu'à la recette
interactive et au scénario de lien symbolique réel, sans considérer ces limites
comme des validations réussies. Les cases cochées ci-dessus décrivent les
opérations des assistants embarqués et contrôles exécutés ; le comportement
du modèle doit encore être observé dans la session de recette.

- Les 12 plugins portent `judge-fr-eu-<domaine>` et la version `0.1.0` ; source,
  auteurs et noms des 150 skills conservés. Marketplace/config : `judge-fr-eu`.
  Entrée CoCounsel retirée, fichiers éditeur et licence racine inchangés.
- Profils, profil partagé, dossiers/archives, registres, journaux et sorties
  isolés ; aucune reprise du cache. Contrat et assistant Python 3.12 embarqués
  dans chaque paquet, chargés par les points d'entrée. Copies des modèles et
  de la méthode BASE-005 présentes pour l'autonomie des paquets.
- Cycle communautaire confié à l'assistant du hub : identité/dossier préfixés,
  journal propre au fork, sauvegardes, update/rollback, disable/enable/uninstall,
  empreintes et vérification des chemins. Les gates de confiance et d'accord
  existantes restent applicables. Sorties des cinq cookbooks par déploiement.
- [Inventaire avant migration](base-008-inventaire-avant.tsv) régénéré avant
  modification : 221 fichiers. Notices par paquet et [NOTICE racine](../../NOTICE).
- [Tests BASE-008](../../scripts/test-base008-isolation.py) sur vrais paquets
  détachés et profils factices : 16 tests, 15 passent et 1 ignoré. Jonctions
  Windows et liens physiques refusés en conditions réelles ; création de lien
  symbolique impossible ici (WinError 1314), scénario restant à rejouer.
- Les cinq cookbooks passent leur dry-run, sans déploiement distant. Le
  contrôleur BASE-006 ne trouve plus d'erreur structurelle ; les chemins
  dynamiques et appels interplugins gardent leurs statuts de relecture.
- CLI officielle **Claude Code 2.1.301** installée en répertoire temporaire :
  marketplace et 12 plugins validés. Original emploi `1.0.2` et fork emploi
  `0.1.0` installés simultanément et activés dans la configuration jetable,
  mises à jour automatiques désactivées par environnement. L'original est
  obtenu depuis `anthropics/claude-for-legal`, son nom réservé étant refusé
  depuis une copie locale. Voir la [preuve client](base-008-resultats-client.json).
- Limite : `auth status` indique une session non authentifiée. Le chargement
  dans une session de modèle, les commandes réellement invoquées et leurs
  traces de fichiers restent à vérifier. Aucun profil personnel utilisé,
  import, publication, push, PR ni déploiement distant effectué.

Le [relevé de validation](../../references/base008-validation.md) détaille les
preuves, références officielles consultées, limites et recette restante.
Cette migration technique n'adapte pas les tâches juridiques France/UE.

### Reprise après rétrospective — 15 octobre 2026

[BASE-009](base-009-corrections-retrospective.md) a rendu les scripts de
cookbooks portables et documenté les dépendances de test. Rejoué avec ces
dépendances : suite BASE-008 à 15 réussis et 1 ignoré, dry-run des cinq
cookbooks réussi. Sans `jsonschema`, le test de l'orchestrateur est ignoré :
c'est une absence d'outil, pas une réussite. Restent ouverts le critère 1
(session de modèle authentifiée) et le critère 4 (liens symboliques réels).
La recette doit isoler le home du système : `CLAUDE_CONFIG_DIR` ne déplace pas
les chemins `~/.claude/plugins/config/judge-fr-eu/`.
