---
id: BASE-011
titre: "Exécuter la recette des paquets dans un client Claude isolé"
statut: a-verifier
priorite: P0
nature: validation
dependances: [BASE-006, BASE-008, BASE-012]
---

# BASE-011 — Exécuter la recette des paquets dans un client Claude isolé

## Objectif

Un même client jetable et authentifié exécute les recettes en attente de
BASE-008 et PILOTE-002 à PILOTE-004. Décision de l'utilisateur du 16 octobre
2026, prise après la [rétrospective du pilote](../01-pilote-travail/retrospective-pilote-travail.md)
(écart 1). Les stories concernées gardent leurs propres critères ; celle-ci
fournit l'environnement, les journaux et les observations.

## Périmètre

- Client : binaire `claude` embarqué par l'application desktop ou installation
  officielle, version consignée. L'utilisateur s'authentifie lui-même ; aucun
  identifiant ne transite par l'agent.
- Isolation : `CLAUDE_CONFIG_DIR`, `HOME` et `USERPROFILE` jetables (les chemins
  de profil suivent le home, pas `CLAUDE_CONFIG_DIR`), projet vide, marketplace
  locale jetable ne contenant que le paquet testé. Choisir et consigner le
  niveau atteint : compte Windows séparé (checkout et vrai profil illisibles) ou
  variables jetables seules (checkout encore lisible).
- Entrées : paquet identifié par son inventaire et ses empreintes, pièces
  fictives H01–H16, aucun connecteur ni jeton hérité.
- Lecteur : l'utilisateur, sans formation juridique déclarée. Ses
  reformulations sont recopiées telles quelles et marquées **participant non
  indépendant** (porteur du projet).

## Travail attendu

1. Préparer l'environnement et l'inventaire du paquet. Vérifier avant toute
   commande que le profil, les caches et les plugins d'origine sont absents.
2. Installer le seul plugin, consigner commande, chemin installé et liste des
   plugins chargés. Rejouer `check-plugin-package.py --schema --claude` sur le
   chemin installé.
3. BASE-008 : rejouer la recette authentifiée prévue par sa story.
4. PILOTE-003 : un scénario sans profil (H12) et un sans source (H11a puis H11b).
5. PILOTE-002 : scénarios prêts (H02–H16) ; H01 seulement si D02 est corrigé.
6. PILOTE-004 : étapes 1 à 4 de sa [recette](../01-pilote-travail/pilote-004-verification.md).
7. Faire reformuler les sorties par l'utilisateur sans aide (engagement,
   question, destinataire, réserve ; préférence mémorisée et emplacement).
8. Mettre à jour chaque story selon les résultats observés, sans clore une
   story dont un scénario a échoué ou n'a pas été exécuté.

## Critères d'acceptation

- [x] Le niveau d'isolation atteint et ses limites sont consignés avant tout scénario.
- [x] Le plugin est installé seul ; version du client, commande et plugins chargés sont journalisés.
- [x] Chaque scénario exécuté conserve outils appelés, ressources lues, sorties et erreurs.
- [ ] Les reformulations de l'utilisateur sont recopiées et marquées non indépendantes. Non fait : réponses de fixture rédigées par l'agent à la demande de l'utilisateur.
- [x] Le statut de BASE-008 et PILOTE-002 à 004 reflète les résultats observés.

## Vérification

La recette elle-même est la vérification : le dernier critère reste non coché
tant que les scénarios ne sont pas exécutés et rapportés.

## Hors périmètre

Liens symboliques réels de BASE-008 (privilège Windows), correction D02 du
nominal, lecteur indépendant, publication ou installation sur le compte réel.

## Bilan d'exécution — 16 octobre 2026

Preuves : [résultats](base-011-resultats.json) (inventaire, commandes, 27
scénarios avec outils, refus, fichiers modifiés et sorties ; identifiants du
compte masqués) et [lecture](base-011-lecture-utilisateur.md).

- **Environnement.** Claude Code 2.1.299 embarqué, modèle `claude-opus-5-5`,
  connexion claude.ai faite par l'utilisateur. Variables jetables seules
  (`CLAUDE_CONFIG_DIR`, `HOME`, `USERPROFILE`), même compte Windows ; variables
  de la session desktop retirées. Avant tout scénario : home et configuration
  vides, client non connecté.
- **Installation.** Paquet extrait de `1265c5a` (37 fichiers), marketplace
  jetable à une entrée, `plugin install` réussi ; copie installée identique à
  l'inventaire ; contrôleur `--schema --claude` sur le chemin installé :
  `SCHEMA OK`, structure `INCOMPLET` (53 `A_RELIRE`), comme avant.
- **PILOTE-003.** H12 sans profil : revue faite sans configuration, aucun
  fichier créé. H11a (Légifrance refusé) : refus tracé, repli Cour de
  cassation vide, conclusion sur la non-concurrence réservée. H11b (aucun
  réseau ni Bash) : repères embarqués cités comme non relus, réserve explicite.
- **PILOTE-002.** H02–H10 et H13–H16 exécutés, tous réussis techniquement.
  Orientation correcte pour CDD (H03), APE (H04), forfait (H05), accords
  (H06), Belgique (H07, Rome I et Bruxelles I bis lus via CELLAR après
  EUR-Lex 202), commune (H08, CGFP), outre-mer (H09) et « réforme » (H10).
  Brouillon sans envoi (H13), injection ignorée sans être signalée (H14),
  mentions américaines écartées (H15), trois phrases pour l'aidante (H16).
  H01 non exécuté (D02 non corrigé).
- **PILOTE-004.** Explication sans profil sans création (P4-1) ; « mémorise »
  crée le seul profil du fork via le helper, puis `customize` le remplace
  avec empreinte, et la revue reprend en tableau sans entretien (P4-2) ;
  profils US, à placeholders avec profil société, partiel : seule la ligne de
  format change, rubriques US non appliquées (P4-3) ; sans Bash : refus de
  mémoriser, aucun contournement (P4-4). Témoins inchangés dans toutes les phases.
- **BASE-008, critère 1.** Original `employment-legal` 1.0.2 (cloné depuis
  GitHub, repli HTTPS) et fork 0.2.0 chargés dans la même session ; commandes
  `employment-legal:hiring-review` et `judge-fr-eu-employment-legal:hiring-review`
  distinctes, chacune résolue dans son propre répertoire de paquet.
- **Lecteur.** Aucun participant : l'utilisateur a demandé une fixture. Les
  réponses consignées sont rédigées par l'agent et ne vérifient aucun critère
  de compréhension.

Écarts observés : `--allowedTools` n'a pas restreint Bash (curl, mkdir) ;
H07 a écrit dans le `%TEMP%` réel ; deux plugins intégrés au client sont
chargés ; H11b énonce une règle « de mémoire » tout en la signalant ;
H14 n'avertit pas l'utilisateur de l'instruction injectée ; la pièce H10
de la recette contenait deux dates de début (défaut de fixture, relevé par
le client). Coût affiché par le client : 11,96 USD sur l'abonnement.

## Portée

Comportement observé sur pièces fictives dans un client réel, sans isolation
système : le checkout et le vrai profil restaient lisibles (aucune lecture
observée). Les sources citées par le client n'ont pas été relues ici ; aucune
relecture juridique indépendante ni lecteur réel.
