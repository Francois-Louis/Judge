# EXIST-011 — Découpage du hub de gestion des skills

Vingt suites **proposées**, sans implémentation dans le paquet. L’[inventaire
exhaustif](exist-011-inventaire-hub.md) couvre 30 fichiers, dix skills
(neuf invocables et skill-manager non invocable) et un agent. Le hub reste
facultatif, un plugin principal pour gestion technique, pas moteur de droit.

## Suites bornées et préalables

Toutes dépendent de EXIST-011, PILOTE-003, BASE-005/006 et BASE-008/009.
Les autres dépendances sont ci-dessous ; la numérotation ne fixe pas l’ordre.

| Suite | Tâche | Résultat attendu | Autres préalables |
|---|---|---|---|
| [HUB-001](../suites/hub-001-identite-provenance.md) | Identifier l’origine et la version d’un skill | Une fiche distingue paquet interne du fork, skill communautaire suivi, copie personnalisée et contenu éditeur ; provenance et chemin ne sont jamais déduits du seul nom. | Aucun autre HUB |
| [HUB-002](../suites/hub-002-politique-confiance.md) | Unifier la politique de confiance du hub | Le défaut restrictif est cohérent partout ; une politique absente, illisible ou mal formée n’entraîne aucune installation permissive implicite. | HUB-001 |
| [HUB-003](../suites/hub-003-registres-cache.md) | Gérer les registres surveillés et leur cache | Un catalogue identifie registres surveillés, autorisation distincte et date/couverture du cache, avec ajout ou pause explicite. | HUB-001, HUB-002 |
| [HUB-004](../suites/hub-004-decouverte-portee.md) | Afficher la portée des skills découverts | Une fiche de découverte affiche juridiction, tâche, limites et statut de lecture ; un skill américain reste visiblement américain dans une recherche française. | HUB-001, HUB-003 |
| [HUB-005](../suites/hub-005-suggestions-contextuelles.md) | Borner les suggestions aux données autorisées | Une suggestion facultative repose sur la tâche partagée et sa portée, sans lecture globale d’autres dossiers ou déclencheur supposé installé. | HUB-003, HUB-004 |
| [HUB-006](../suites/hub-006-profil-hub.md) | Configurer un profil minimal de gestion des skills | Un entretien minimal renseigne besoins, territoire et contexte d’usage sans imposer un métier, une entreprise ou un starter pack déjà adapté. | HUB-001, HUB-002, HUB-004 |
| [HUB-007](../suites/hub-007-personnaliser-preferences.md) | Modifier les préférences sans affaiblir les contrôles | Une modification ciblée de préférences conserve politique, journal et contrôles obligatoires ; aucun paramètre n’active auto-application ou contournement REFUSE. | HUB-002, HUB-003, HUB-006, HUB-010 |
| [HUB-008](../suites/hub-008-preparer-candidat.md) | Préparer un candidat exact pour la revue | Un dossier de revue montre l’intégralité du candidat épinglé, ses dépendances et les transformations prévues, avant activation. | HUB-001, HUB-002, HUB-009, HUB-010, HUB-011, HUB-012 |
| [HUB-009](../suites/hub-009-licence-provenance.md) | Documenter la licence d’un candidat | Une fiche conserve licence déclarée, pièce effectivement lue, correspondance et limites selon l’usage prévu, sans autoriser une licence depuis du texte non fiable. | HUB-001, HUB-002 |
| [HUB-010](../suites/hub-010-qa-securite.md) | Rendre cohérents les verdicts de sécurité | Un vocabulaire de verdict distingue observation heuristique, besoin de revue et refus non contournable ; tous consommateurs appliquent la même priorité. | HUB-001, HUB-002 |
| [HUB-011](../suites/hub-011-qa-pertinence-fr-ue.md) | Évaluer séparément la pertinence France et UE | Le rapport sépare sécurité, conception et pertinence documentaire pour la tâche/juridiction ; un skill US bien sourcé n’est pas qualifié prêt pour la France. | HUB-001, HUB-004, HUB-010 |
| [HUB-012](../suites/hub-012-fraicheur-references.md) | Distinguer fraîcheur du code et des références | Un état de fraîcheur documentaire distingue déclaration auteur, vérification effective et rappel, indépendamment d’un nouveau commit. | HUB-001, HUB-002 |
| [HUB-013](../suites/hub-013-installer-candidat-revu.md) | Installer uniquement le candidat communautaire revu | Une installation active ne concerne que le candidat exact revu et autorisé, dans un nouveau chemin communautaire du fork. | HUB-008, HUB-019 |
| [HUB-014](../suites/hub-014-mise-a-jour-personnalisee.md) | Préserver les adaptations lors d’une mise à jour | Une mise à jour compare version source de base, installation réelle et nouveau candidat ; les modifications locales sont préservées et aucune fusion n’est appliquée silencieusement. | HUB-001, HUB-008, HUB-019 |
| [HUB-015](../suites/hub-015-restaurer-version.md) | Restaurer une sauvegarde communautaire identifiée | Un rollback restaure uniquement une sauvegarde enregistrée et intacte, après revue de sa portée et des écarts ; ce n’est pas une garantie de validité actuelle. | HUB-010, HUB-012, HUB-019 |
| [HUB-016](../suites/hub-016-desactiver-reactiver.md) | Désactiver et réactiver un skill suivi | Une seule identité communautaire suivie change d’état via helper, avec fichiers/prérequis et limites de prise d’effet visibles. | HUB-001, HUB-019 |
| [HUB-017](../suites/hub-017-desinstaller-skill-suivi.md) | Désinstaller uniquement le skill communautaire suivi | Une suppression bornée retire le seul répertoire suivi après présentation des chemins, en conservant configuration et sauvegardes. | HUB-001, HUB-019 |
| [HUB-018](../suites/hub-018-sync-notifications.md) | Séparer synchronisation et notifications | Un relevé de nouveautés ne fait aucune installation ; une notification externe exige canal/destinataire et autorisation réels, sinon résultat local. | HUB-003, HUB-004, HUB-007 |
| [HUB-019](../suites/hub-019-journal-projections.md) | Conserver le journal comme seule autorité de gestion | Journal canonique, tables de profil, cache et décisions de fraîcheur ont des responsabilités distinctes, sans import ou réécriture d’événement. | HUB-001 |
| [HUB-020](../suites/hub-020-documentation-capacites.md) | Documenter les capacités réellement livrées du hub | La documentation distingue découverte, revue, gestion du communautaire et effets effectifs ; aucune promesse de validation juridique ou de fonctionnement passif non installé. | HUB-001, HUB-002, HUB-004, HUB-010, HUB-011, HUB-018, HUB-019 |

Première tranche suggérée : **HUB-001**, identité/provenance, puis HUB-002 pour
politique cohérente. Aucune tranche n’est sélectionnée par ce cadrage. Les
dépendances 008/009/010/011/012 définissent le dossier revu avant installation
013 ou update 014 ; 019 fixe la consommation du journal déjà existant.
Une future implémentation doit prendre une tâche et ses seuls préalables
nécessaires, sans réécriture générale ni installation d’un starter pack complet.

PILOTE-003 est clos après BASE-011 ; le préalable au découpage est satisfait,
sans extension choisie. Les limites H01 complet et lecteur indépendant restent
consignées dans le bilan du pilote. Elles ne deviennent pas recette du hub.

## Identité et gestion : qui peut être modifié

| Objet identifié | Découverte/revue | Cycle de vie autorisé dans le futur hub |
|---|---|---|
| Paquet interne du fork, éventuellement adapté localement | Inventaire et revue possibles sur pièces autorisées | Aucune mise à jour communautaire de son contenu ; lot du paquet concerné. |
| Skill communautaire installé et suivi par ce hub | Source/commit/digest/metadata et limites de portée visibles | Helper uniquement, gates et accord sur version exacte ; état local modifié entraîne préservation et comparaison. |
| Copie manuelle, journal absent/ancien/étranger | Lecture bornée et état inconnu signalé | Aucune adoption ou migration implicite ; profil/cache ne reconstitue pas l’autorité. |
| Plugin/contenu éditeur | Origine et portée montrées sans modification | Hors mutation automatique du hub ; mécanisme du produit et éditeur distincts. |

Ni préfixe technique, rôle déclaré, nom de registre ni bonne citation ne
certifient provenance ou autorité. Journal et octets réels, pas table du profil,
établissent l’installation communautaire suivie.

## Ordre de revue et protections conservées

1. Identifier source et politique active avant de lire le contenu non fiable.
   Mode absent/invalide ne devient pas permissive ; registre surveillé n’est
   pas automatiquement source autorisée.
2. Préparer un candidat épinglé en contexte de lecture aux capacités réellement
   bornées ; aucun code du candidat exécuté. Staging de revue et activation
   sont des étapes différentes, leurs écritures sont précisément documentées.
3. Présenter source brute, annexes, licence/provenance, capacités, sorties de
   contrôle et transformations prévues (préfixe/préambule compris).
4. Séparer sécurité technique, conception et pertinence documentaire FR/UE.
   Le refus concret de sécurité reste non contournable ; une langue ou un
   registre réputé ne valide pas le droit. Coverage partielle reste explicite.
5. Recueillir une décision sur ce candidat précis et ses limites ; modification
   de commit, fichiers ou transformation invalide cette décision.
6. Revalider état/empreintes et appeler le helper existant pour l’unique mutation
   autorisée ; journal via helper puis projection. Aucun renforcement d’autorité
   depuis metadata, table ou texte candidat.

Ces protections décrivent les futures tâches, sans constituer une demande
d’installation à l’utilisateur pendant le cadrage. BASE-009 a déjà supprimé
l’auto-application ; EXIST-011 conserve ce résultat et borne les contradictions
restantes. Une notification, un passage de cadence à weekly ou l’option
`--apply` ne vaut pas approbation d’une version.

## Préserver une adaptation : comparaison avant remplacement

HUB-014 doit montrer trois états s’ils existent : base source connue, arbre
réel installé (préfixes/préambules/adaptations inclus), nouveau candidat.
Diff upstream A→B seul est incomplet si l’état local est A+L.
Le helper BASE-008 refuse déjà A+L quand son empreinte ne correspond plus au
journal ; la [simulation](exist-011-simulation-resultats.json) observe ce refus
sans toucher au home réel.

Ce refus reste utile. Préserver/exporter et comparer ne signifie pas fusionner
automatiquement ni modifier une empreinte de journal pour adopter L.
Réconciliation ou import exigeraient un lot technique explicite distinct :
pas de nouveau mécanisme d’adoption inventé par HUB-014/019. Base absente,
conflit, backup modifié ou destination occupée restent des états à examiner.
Aucun contenu éditeur n’est modifié automatiquement.

## Portée France et UE indépendante de la sécurité

| Dimension de contrôle | Preuve utile | Limite |
|---|---|---|
| Sécurité/capacités | Fichiers exacts, permissions, hooks/MCP, chemins, preuves de scan et couverture | Scan heuristique propre ne certifie pas absence de malveillance ; `--approved` est une attestation du workflow. |
| Conception/méthode | Tâche, entrées, sortie, limites, dépendances et scénarios | Format correct ne prouve ni performance ni pertinence pour une autre juridiction. |
| Pertinence documentaire | Territoire/date/matière, sources effectivement lues et état de version | Candidat Californie ne devient pas adapté France parce qu’il est bien sourcé ou traduit. Fond juridique à vérifier séparément. |
| Fraîcheur | Déclaration auteur distincte de vérification, versions et fenêtre active | Commit/date avancés ou rappel ignoré ne certifient pas droit applicable actuel. |

HUB-004 affiche portée déclarée et constatée, HUB-011 conserve ces dimensions
dans QA, HUB-020 les garde dans documentation et présentation. Pas de moyenne
ou badge READY global pour le besoin français si juridiction incompatible ou
inconnue. Le hub prépare preuves et limites, pas certification juridique.

## Responsabilités de fichiers et noms

Les noms techniques existants restent canoniques ; pas de traduction des
répertoires ni de nouvelle commande annoncée. skill-manager reste non invocable,
chargé par disable et uninstall ; ces deux entrées restent publiques.
Les références futures sont chacune à créer par une seule suite propriétaire.

HUB-019 possède contrat d’état/projections ; community_store.py reste seul
écrivain lifecycle. HUB-002 possède politique de confiance ; HUB-003 catalogue,
watchlist et cache ; HUB-010 possède priorité des verdicts ; HUB-012 fraîcheur ;
HUB-018 notifications. Les autres consommateurs ne réinventent pas ces règles.
Les helpers et cinq copies partagées sont conservés à l’identique ; tout besoin
de changement de moteur ou schéma exige un lot distinct.

Plusieurs suites touchent installer, updater, profil et README : les exécuter
séparément, préserver les branches déjà livrées et rejouer les cas concernés.
Chaque lot adapte documentation/version/NOTICE à sa portée et synchronise
marketplace si champs communs du manifeste changent. HUB-020 est une revue
de cohérence finale ; elle ne dispense pas les autres lots de leur documentation.

## Sources, preuves et validation futures

Règles officielles du produit et permissions réelles, provenance des registres,
fichiers exacts de licences et attributions sont à lire lors des implémentations.
Aucune disponibilité de service ou revue de registre n’est vérifiée sur le
réseau par EXIST-011. Une source juridique éventuelle doit suivre la méthode
locale BASE-005/BASE-010, sans abonnement PISTE imposé et sans importer un
outil de maintenance comme dépendance runtime.

Installation disque, découverte/rechargement client, exécution de prompts,
authentification et notification sont des résultats distincts. Agent et hook
décrits ne prouvent pas une planification configurée. Tests de schéma/paquet
extrait BASE-006, scénarios métier/limites et revue indépendante restent aux
lots sélectionnés. La [vérification](exist-011-verification.md) distingue la
simulation réellement exécutée et la relecture de sorties futures sur fixtures.

