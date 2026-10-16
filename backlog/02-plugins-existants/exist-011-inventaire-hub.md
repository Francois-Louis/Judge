# EXIST-011 — Inventaire du hub de gestion des skills

Lecture locale du **16 octobre 2026** : **30 fichiers, dix skills dont neuf
invocables et une référence non invocable, un agent**. Aucun cookbook propre
ne référence ce hub. Les tableaux couvrent tout `legal-builder-hub`, y compris
les fichiers cachés, helpers et références imbriquées. Les décisions sont des
adaptations futures, pas des changements du paquet par EXIST-011.

## Les dix skills

Chemins relatifs à `legal-builder-hub/skills/`.

| Fichier | Contenu et dépendances constatés | Décision individuelle et raison | Suites |
|---|---|---|---|
| `auto-updater/SKILL.md` | Notify/manual, commit épinglé, diff complet, rescan QA, revue humaine ; fraîcheur sans nouveau commit ; helper lifecycle prioritaire, profil et journal. BASE-009 a retiré auto-application. | Conserver nom et revue par version ; réécrire comparaison avec état local et données de fraîcheur. Ne pas rétablir auto, ne pas écraser customisations ni paquets internes/éditeur. Corriger exemples rollback sans SHA explicite et lecture des champs de journal sous metadata. | HUB-001, 008, 010, 012, 014, 015, 019 |
| `cold-start-interview/SKILL.md` | Interview du fork, profil partagé, starter pack, modes confiance, licences et fenêtres ; succès MCP seulement sur appel réussi. Promet permissive quick start puis impose restrictive sauf choix ; déduit scope du cwd et s’adresse au lawyer. | Conserver entretien/continuité et limites d’intégration ; réécrire pour public réel, contexte minimal, politique cohérente. Retirer collecte d’entreprise imposée, déduction du scope par cwd, conseils de licence généraux et sélection du pack comme autorisation d’installer. | HUB-002, 006, 009, 012 |
| `customize/SKILL.md` | Édition de profil, registries, starter pack, intégrations, cadence et QA strictness ; refuse auto depuis BASE-009, mais propose de désactiver QA/failure-mode checks et cite des commandes courtes non canoniques. | Conserver utilitaire et changements ciblés ; réécrire sans désactivation des contrôles, modification du journal ou confusion cadence/scheduler. Table d’installations informative, pas autorité. Corriger les commandes courtes quand la tâche concernée est livrée. | HUB-002, 007, 010 |
| `disable/SKILL.md` | Entrée publique qui charge skill-manager ; renames SKILL et hooks, consulte journal et table, accord avant action ; helper chargé en tête. | Conserver nom et bascule disable/enable ; réécrire vers helper unique et journal comme preuve. Ne pas promettre arrêt d’un processus ou d’une tâche externe depuis un rename disque. | HUB-016 |
| `registry-browser/SKILL.md` | Watchlist du profil, index GitHub/frontmatter, cache sept jours, noms/descriptions, aperçu brut ; ajout registre en le fetchant puis confirmation. | Conserver découverte, réécrire origine/portée et autorisation d’accès avant contenu. Ajouter juridiction déclarée/observée, manques et cache daté. Surveillance ≠ confiance ; candidat américain reste hors portée France. | HUB-003, 004 |
| `related-skills-surfacer/SKILL.md` | Lit profil/cache, recherche par mots-clés et activités d’autres plugins, surfaced.json ; Stop hook possible mais non câblé ; « pas installé » assimilé à rejet, silence et decision tree en tension. | Conserver suggestion brève facultative ; réécrire accès au seul contexte autorisé, portée juridique et états affiché/rejeté. Retirer lecture implicite de tous dossiers, rejet inféré et promesse passive ; silence sans résultat reste silence. | HUB-005 |
| `skill-installer/SKILL.md` | Allowlist avant fetch, licences, brut, surface technique, QA/role, accord, helper communautaire ; read-only obligatoire en restrictive. Permissive si politique absente, commit ou tag encore mentionné, fraîcheur transformée à Step 7 après accord. | Conserver gates et identité, réécrire ordre revue/transformation/accord, politique absente et pin exact. Pas d’installation dans un paquet interne/éditeur ; rôle professionnel ne prouve pas autorité technique. Ancien accord ne couvre pas de nouveaux octets. | HUB-001, 002, 008–013, 019 |
| `skill-manager/SKILL.md` | **Non invocable** (`user-invocable: false`), référence de disable/uninstall ; journal/digest protègent identité, mais étapes rename/append YAML héritées subsistent sous contrat lifecycle prioritaire. | Conserver référence et nom ; réécrire workflows qui doivent appeler le helper, retirer écritures directes et snippets legacy ambigus. Aucun second moteur, suppression ou adoption d’installation non suivie. | HUB-001, 016, 017, 019 |
| `skills-qa/SKILL.md` | Treize paramètres, carte des dépendances, scan heuristique, trois failure modes et verdict REFUSE en plus de trois bandes annoncées ; Step 1.5 émet REFUSE sur régression puis permet override, fin « verdict advisory ». Allowlist standalone n’est que passive. | Conserver scan, preuves/limites et qualité de conception ; réécrire priorité des verdicts sans contourner REFUSE. Ajouter dimension FR/UE indépendante de sécurité/forme. Le navigateur ne devient pas moteur de fond et QA propre ne valide pas la règle américaine pour un besoin français. | HUB-010, 011, 012 |
| `uninstall/SKILL.md` | Entrée publique vers skill-manager, liste chemins, accord explicite ; journal et table du profil, config conservée ; helper prioritaire. | Conserver suppression bornée, réécrire preuve par journal seul et délégation au helper. Aucun paquet interne/éditeur, fichier local modifié ou arborescence arbitraire supprimés. | HUB-017 |

## L’agent livré

Chemin relatif à `legal-builder-hub/`.

| Fichier | Contenu et dépendances constatés | Décision et suite |
|---|---|---|
| `agents/registry-sync.md` | Décrit cadence hebdomadaire, index/cache et digest ; outils Read, Write, WebFetch, wildcard Slack send. Depuis BASE-009 ne fait qu’annoncer, renvoie vers auto-updater pour revue. Aucun scheduler livré par cette définition. | Conserver sync de métadonnées, aucune application. HUB-018 borne droits d’écriture et notification, destination/autorisation et preuve d’envoi ; absence de scheduler/Slack reste explicite. HUB-003/004 fournissent catalogue/portée consommés. |

## Les dix-neuf autres fichiers du plugin

Chemins relatifs à `legal-builder-hub/`.

| Fichier | Contenu et dépendance | Décision individuelle et responsable |
|---|---|---|
| `.claude-plugin/plugin.json` | Identité judge-fr-eu-legal-builder-hub 0.1.0, adaptation juridique pending ; auteur/attribution hérités et dépôt du fork. | Conserver identité/attribution. HUB-020 documente seulement capacités réellement livrées et synchronise champs communs avec marketplace si changés ; pas de modification actuelle. |
| `.gitignore` | Exclusions du paquet propres au hub. | Conserver sans uniformisation ; état utilisateur hors paquet selon BASE-008. |
| `.mcp.json` | Déclare Slack, Google Drive, Lawve AI, catégories registre/chat/documents. | Conserver sans inférer connexion, publication de registre, capacités exactes ou droit français couvert. HUB-018 ne retient que capacité réellement disponible/autorisée, sinon relevé local. |
| `CLAUDE.md` | Modèle du profil, pas contexte installé automatiquement : rôle, intégrations, starter pack, watchlist ; prérequis setup en tête mais réponse générique sans setup plus bas ; pas de sections Sources I trust/Freshness reminders complètes malgré attentes des skills. Garde-fous et assertions US/UK/UE sur privilege. | Conserver filet partagé et frontière ; HUB-006 qualifie public et profil, 002 politique, 011 pertinence, 012 fraîcheur, 019 projections. Retirer équivalence marquage/protection, recours au framework US sous caveat en France et effet d’install depuis table déclarative ; revue du fond distincte. |
| `hooks/hooks.json` | Stub vide. | Conserver ; HUB-005 ne promet aucun Stop hook effectif et HUB-018 aucun cron fourni. Câblage futur exige lot/capacités explicites. |
| `LICENSE` | Licence héritée. | Conserver inchangée. Lecture d’une licence de candidat ne remplace pas celle du paquet et n’autorise pas la modification des contenus éditeur. |
| `NOTICE` | Attribution et entrées BASE-008/009. | Conserver ; future suite modifiant le paquet inscrit son entrée datée. Pas d’entrée pour EXIST-011 limité au backlog. |
| `README.md` | Huit commandes publiques, omet customize ; table neuf skills omet aussi customize ; parle de permissive default et registres reviewed, activité passive et agents scheduled. Auto désactivé par BASE-009. | Réécrire documentation en HUB-020 ; dix skills/neuf invocables, défaut cohérent HUB-002, capacités réelles HUB-018. Retirer confiance juridique implicite depuis registre/scan et activité non câblée. |
| `references/allowlist-default.yaml` | Modèle restrictive, trois dépôts, deux publishers, zéro connector, six licences. Commentaire HTML initial chargé comme **clé YAML parasite**, pas comme commentaire. | Conserver protections et modèle en lecture seule ; HUB-002 corrige forme/schéma et divergences avec absent=permissive de l’installer/référence. Aucune valeur du candidat n’écrit cette politique. |
| `references/community-lifecycle.md` | Contrat prioritaire BASE-008 : helper seul écrivain, namespace, journal JSON schéma 1, digests, backup/rollback, identité préfixée ; refuse local edits, liens et états inconnus. Pas de migration automatique. | Conserver comme frontière existante. HUB-001/008/013–019 précisent consommation du contrat ; pas de suppression des refus pour « faciliter » l’adaptation locale. |
| `references/company-profile-template.md` | Copie embarquée du modèle partagé. | Conserver identique ; HUB-006 n’impose pas de profil entreprise à tous publics. |
| `references/dashboard-template.md` | Copie partagée embarquée de visualisation et échappement. | Conserver identique ; un indicateur de scan/format n’est pas certification FR/UE. |
| `references/isolation.md` | Copie BASE-008, chargée aux dix entrées et à l’agent. Racine active du fork et données durables hors paquet. | Conserver byte pour byte ; aucune lecture/import de configuration d’origine, écriture dans modèle ou fallback cwd. |
| `references/shared/research-citation-method.md` | Copie locale BASE-005 1.0.0. Sa présence n’atteste pas chargement ni actualité du contenu d’un candidat. | Conserver identique ; chaque future entrée adaptée lit méthode et références nécessaires embarquées. |
| `scripts/community_store.py` | Stage filesystem existant sans fetch ni exécution ; CLI --approved, faux home possible ; communauté standalone, journal/digest, backups et lock ; refuse modification locale avant update/rollback/disable/uninstall. | Conserver dans ce cadrage et les suites de consommation. --approved est attestation du workflow, pas vérification indépendante d’un accord humain ; helper ne fait ni allowlist ni QA juridique. Limites techniques nécessitent un lot distinct. |
| `scripts/judge_store.py` | Helper BASE-008 partagé embarqué, contrôles de chemins et écritures gardées. | Conserver identique à racine et autres paquets ; ne pas ajouter un second moteur pour cache/profil/état. |
| `skills/registry-browser/references/registries.yaml` | Modèle livré avec seul lpm-skills, description héritée « 14 skills », last_synced null ; même clé HTML parasite au chargement YAML. | HUB-003 corrige forme et source canonique du catalogue ; conserver distinction watchlist/allowlist. Nombre et réputation non vérifiés en ligne dans cet inventaire. |
| `skills/skill-installer/references/allowlist.md` | Schéma et listes indépendantes, mais défaut permissive et permissive si absent opposés au modèle restrictive ; affirme mécanisme structurel alors que lecture/enforcement sont encore en prompt. | HUB-002 unifie sans affaiblir et distingue contrat prescrit/garantie observée ; HUB-009 précise licence comme gate séparé. Aucun verdict de conformité depuis présence sur liste. |
| `skills/skill-installer/references/freshness.md` | Tokens/date/fenêtres/URLs stricts, catégories dont stable ; explique comparaison à today + window, formule opposée à la suite du workflow qui part de last_verified. | HUB-012 corrige calcul et limites : date auteur et nouveau commit ne certifient pas références, échéance/versions/portée distinctes, préambule revu avant accord. |

## Dépendances de contenu et frontières

- Graphe hérité : profil/watchlist → browser/cache → recommandations/interview ;
  allowlist → installer → QA → revue → helper → journal → projection profil ;
  sync → nouveautés/diff → revue auto-updater, jamais application par sync.
  Disable/uninstall chargent skill-manager et le contrat lifecycle prioritaire.
- Les registres sont des **déclarations locales** : allowlist contient lpm-skills
  et deux dépôts Lawvable, watchlist livrée seulement lpm-skills. Aucun dépôt
  n’a été consulté ni sa provenance/licence/revue actuelle certifiée par ce lot.
  Aucun service Lawve AI ou connecteur n’a été authentifié.
- Données utilisateur non livrées : profil actif, allowlist active, registry-cache.json,
  surfaced.json, freshness-review.yaml, install-log.yaml, staging et backups.
  Journal JSON valide YAML sous namespace judge-fr-eu, append-only via helper.
  Starter pack est projection ; métadonnées sont sous `metadata`, pas clés legacy.
- Les assertions de scan, licence, fraîcheur et rôle restent indépendantes :
  allowlist ne sécurise pas tout contenu d’un publisher, licence ne prouve pas
  pertinence juridique, professionnel déclaré ne prouve pas autorité d’installer,
  date auteur ne prouve pas droit actuel. Trois dimensions de QA restent visibles.
- Protections BASE-009 conservées : aucune application automatique annoncée
  dans agent/updater/customize/README. Contradictions restantes : défauts de
  confiance, QA override/advisory, réglages QA, table/journal, tag/commit,
  transformation après accord et routine passive/scheduled non câblée.
- Base, adaptation locale et nouveau candidat sont trois états distincts ;
  la base peut manquer. Le helper refuse déjà les edits locaux ; le cadrage
  prévoit préservation et comparaison, pas un merge caché ou journal falsifié.
- Pas de cookbook propre ; le hub reste facultatif pour les autres domaines.
  Il ne devient ni moteur de droit de fond ni dépendance imposée pour étudier,
  relire un contrat ou gérer un dossier. Les futurs relais restent proposés.

Le [découpage](exist-011-decoupage-hub.md) attribue vingt tâches ; la
[vérification](exist-011-verification.md) distingue relecture des futures sorties
et simulation filesystem réellement exécutée sur le helper existant.
