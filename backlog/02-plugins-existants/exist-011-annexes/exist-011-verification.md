# EXIST-011 — Vérification du cadrage du hub

Relecture par l’agent de maintenance le **16 octobre 2026**. Deux niveaux de
preuve : une simulation filesystem réellement exécutée sur le helper BASE-008
existant, en faux home temporaire, et une relecture des futures spécifications
sur fixtures fictives. Aucun skill de hub ou modèle n’a été invoqué ; aucune
installation dans le home réel, connexion ou notification externe.

## V01 — Mise à jour d’un skill communautaire personnalisé

Le [script de simulation](exist-011-simulation.py) crée deux candidats fictifs
sans outils/actions, avec SKILL.md et une référence de méthode. Il appelle
le helper existant par tableau d’arguments avec `--home` explicitement limité
au faux home et `--approved` pour cette fixture technique. Ce drapeau n’est
pas une preuve d’une revue humaine réelle et ne teste pas l’interface d’accord.

1. Installation de fixture à un commit fictif exact, journal du fork créé.
2. Modification du SKILL.md installé **et** de sa référence, représentant
   une adaptation locale après installation, sans réécrire l’empreinte du journal.
3. Proposition d’une mise à jour vers un second commit/candidat fictifs.
4. Comparaison des fichiers et du journal avant/après, du nouveau candidat
   et des événements ; contrôle qu’aucun backup n’a été créé pour cette opération refusée.

**Résultat observé :** refus, code de sortie 1 :
`installation changed since review; preserve and compare local edits`.
Les deux fichiers personnalisés, le candidat et le journal gardent leurs
empreintes. Le journal contient seulement l’événement install initial, pas
update ; aucune sauvegarde créée. Le répertoire temporaire a été supprimé
après vérification de son chemin absolu dans le parent temporaire attendu.
Les [résultats de simulation](exist-011-simulation-resultats.json) conservent
messages, empreintes, états et limites ; aucune donnée utilisateur réelle.

**Attendu du cadrage HUB-001/014/019 :** garder ce refus et montrer base connue,
version locale réelle et nouveau candidat, avec base absente explicitée si besoin.
Préservation/comparaison n’est pas fusion automatique ni adoption en modifiant
le journal. Le diff upstream seul ne suffit pas. Pour une adaptation d’un
paquet interne ou un plugin éditeur, le lifecycle communautaire n’intervient pas.
Ces variantes sont dans les [fixtures documentaires](exist-011-scenarios.json).

**Observation de relecture :** HUB-014 MA02 impose préservation et comparaison,
HUB-019 JR02 refuse l’autorité fabriquée depuis profil/ancien journal ; HUB-001
sépare origines et chemins. Le comportement physique actuel satisfait la
préservation testée, mais le nouvel affichage à trois états n’est pas implémenté.

Deux vérifications complémentaires réellement exécutées par la même fixture :
identité interne commercial-legal refusée sans mutation du journal ; CLI sans
`--approved` refusée avant staging. Elles ne valident ni allowlist, ni QA,
ni approbation réelle, que le helper ne réalise pas lui-même.

Commande : `python -X utf8 backlog/02-plugins-existants/exist-011-annexes/exist-011-simulation.py --output backlog/02-plugins-existants/exist-011-annexes/exist-011-simulation-resultats.json`.

## V02 — Découverte d’un skill propre à la Californie

**Fixture fictive, pas recherche réseau :** demande « méthode de procédure civile
pour un dossier en France ». L’index de démonstration contient un candidat
communautaire fixture-california-procedure, uniquement Californie, références
annoncées US, pas de méthode FR/UE. URL example.invalid non consultée.
La structure est supposée lisible et sans capacité dangereuse dans la fixture ;
aucun scanner ou moteur juridique n’a effectivement évalué ce candidat.

**Affichage attendu des futures tâches :**

| Champ | Valeur attendue pour cette fixture |
|---|---|
| Origine | Communautaire, distinct du fork et du contenu éditeur |
| Source/version | Index de démonstration et commit fictif identifiés ; pas réputation vérifiée |
| Juridiction | **US — Californie**, portée annoncée et limitée par le texte fourni |
| Besoin demandé | France ; **hors portée France demandée** |
| Sécurité | Scan non exécuté dans ce lot ; même propre, ne prouverait pas adéquation juridique |
| Conception | Lisibilité supposée dans la fixture, pas recette réelle |
| Fond juridique | Non évalué ; pas de transposition ou conclusion de droit français |
| Prochaine action | Afficher limites et proposer recherche de portée pertinente ; aucune installation/exécution |

**Observation de relecture :** HUB-004 DP01 prescrit la fiche et l’écart,
HUB-011 QF01 sépare trois dimensions sans READY global pour la France, HUB-020
DC02 conserve cette limite et HUB-005 empêche promotion contextuelle par mot-clé.
La sécurité technique ou la qualité des citations ne peut compenser la juridiction.
Ce résultat est une **relecture des attendus**, pas une trace de discovery ou QA
de modèle réellement exécutées. L’ancien navigateur affiche surtout nom,
description et registre ; il reste à implémenter cette présentation dans HUB-004.

## V03 — Contradictions et variantes relues

| Cas documentaire | Constat local / futur attendu |
|---|---|
| Allowlist active absente | Référence et installer disent permissive, modèle dit restrictive. HUB-002 CF02 refuse downgrade implicite, garde la politique indépendante des candidats. |
| Commentaire HTML en tête des deux YAML | PyYAML charge une clé parasite `<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15)` ; document parseable mais schéma pollué. Correction future attribuée HUB-002 et HUB-003 ; fichiers actuels préservés. |
| Registre surveillé mais pas autorisé | HUB-002/003 gardent distinction surveillance/confiance ; aucun fetch du candidat ne vient élargir la politique depuis sa propre description. |
| QA Step 1.5 émet REFUSE puis autorise override ; fin dit advisory | HUB-010 QS02 rend le refus concret non contournable dans tous consommateurs ; une variation heuristique seule ne devient pas preuve de malware. |
| Préférence QA off ou lenient | HUB-007 PR02 conserve contrôles/refus, sans réactiver auto neutralisé par BASE-009. |
| Métadonnée MIT mais fichier contradictoire | HUB-009 garde les deux preuves et gate licence distinct de confiance publisher ; pas de modification de l’allowlist depuis le texte candidat. |
| Même SHA, références trop anciennes | HUB-012 FR01 conserve date/version et état à revoir ; rappel accepté ne vérifie pas le droit. |
| Préambule fraîcheur ajouté après accord | HUB-008 le fait valider/montrer avant décision ; empreinte différente rend la revue précédente insuffisante. |
| Profil prétend installation mais journal absent | HUB-019 JR02 et HUB-001 refusent gestion ; aucune adoption ou ancien journal d’origine importé. |
| Backup modifié ou chemin occupé | HUB-015 RV02 garde refus et octets ; pas d’écrasement de collision pour réparer. |
| Disable sur disque mais processus/tâche externe encore actif | HUB-016 AC02 ne certifie pas arrêt de toutes exécutions depuis rename ; limite client à vérifier. |
| Agent décrit weekly et Slack, hooks vides | HUB-018 distingue cadence et scheduler réellement configuré ; pas d’envoi sans autorisation/destination, pas auto-applied. |
| Suggestion sans hook et silence antérieur | HUB-005 ne promet pas activité passive, ne lit pas tous dossiers et ne transforme pas silence en rejet ou autorisation. |
| Rôle déclaré avocat, non administrateur de l’installation | HUB-006 sépare rôle professionnel et autorité technique ; pas pouvoir acquis depuis un champ de profil. |

## Contrôles effectivement réalisés et limites

Le [contrôleur documentaire](exist-011-controles.py) produit le
[rapport général](exist-011-resultats.json) : inventaire exact 30 fichiers,
dix skills dont neuf invocables et une référence, un agent, aucun cookbook ;
vingt suites proposées et chaque skill/agent ciblé ; nouveaux fichiers avec
propriétaire unique ; frontmatters/dépendances sans cycle, liens/index/format,
copies partagées et contrats lifecycle préservés. Repérages des défauts,
override, pinning, routines et chemins de journal conservés avec lignes.
Parse des deux YAML consigné avec clé parasite, sans les « réparer » dans le plugin.

La fixture locale est contrôlée depuis ses résultats enregistrés et l’empreinte
du helper courant ; pas réexécutée par chaque contrôle documentaire. Les
empreintes du lot et comparaison à l’instantané de début de tâche protègent
le paquet et travaux antérieurs. Les différences concurrentes éventuelles
hors lot sont consignées sans attribution. JSON du dépôt, lint des droits
cookbook et espaces vérifiés ; pas de validation de schéma plugin/client.

Commande : `python -X utf8 backlog/02-plugins-existants/exist-011-annexes/exist-011-controles.py`.
Ajouter `--baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-011-annexes/exist-011-resultats.json`
pour conserver rapport et comparaison ; l’instantané est local/temporaire.

Aucune source externe, règle actuelle du produit, licence de candidat réel,
provenance de registre distante ou doctrine juridique n’est validée par EXIST-011.
Pas de lecteur indépendant, installation/client/reload, contenu éditeur modifié,
exécution de skill, connexion authentifiée, notification, publication ou déploiement.
Les futures suites doivent exécuter leurs scénarios et leurs contrôles de paquet
extrait, capacités réelles et pertinence documentaire dans la portée sélectionnée.
