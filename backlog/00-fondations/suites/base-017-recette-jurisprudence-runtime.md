---
id: BASE-017
titre: "Recetter la recherche de jurisprudence d'un skill dans un client isolé"
statut: terminee
priorite: P1
nature: validation
dependances: [BASE-016, BASE-011, TRAV-062]
---

# BASE-017 — Recetter la recherche de jurisprudence d'un skill dans un client isolé

## Objectif

Observer, sur un skill installé seul, que la conduite de la section 10 de la
méthode `1.2.0` est suivie pendant une vraie réponse. Issue du cadrage
[BASE-015](../base-015-jurisprudence-runtime.md), qui n'a testé les voies que
depuis la session de maintenance.

## Périmètre

- Client et isolation de [BASE-011](../base-011-recette-client-isole.md) ;
  paquet `employment-legal` portant la méthode `1.2.0` et la référence
  corrigée par TRAV-062.
- Skill `hiring-review` sur un contrat fictif avec clause de non-concurrence.

## Travail attendu

Scénarios, chacun journalisé (outils, adresses, refus, sortie) :

1. **Normal** : outil web autorisé ; la sortie cite une décision de la Cour de
   cassation lue sur Légifrance, avec fiche et passage des motifs.
2. **Recherche vide** : question sans jurisprudence diffusée (par exemple une
   clause inhabituelle) ; réponse réservée, recherche décrite, voie indiquée.
3. **Doctrine seule** : décision de cour d'appel connue par un commentaire ;
   citée comme doctrine, décision non lue.
4. **Légifrance refusé** (permission refusée) : repli tracé, aucune solution
   jugée restituée de mémoire.
5. **Sans outil web** : seules les décisions de la référence embarquée, avec
   leur date de relecture ; à comparer avec l'écart H11b de BASE-011.

## Critères d'acceptation

- [x] Les cinq scénarios sont exécutés et journalisés dans le client isolé.
- [x] Aucune sortie ne présente une décision non ouverte comme lue. Non atteint au premier passage (S3, et S2 en tête de note, écart 1) ; atteint au rejeu de S2 à S4 par BASE-019 avec la méthode 1.3.0.
- [x] Les écarts observés sont rapportés aux stories concernées sans être corrigés dans cette story.

## Vérification

La recette elle-même ; le critère 1 reste non coché tant qu'elle n'est pas exécutée.

## Hors périmètre

Évaluation de la justesse juridique des solutions, autres plugins, lecteur indépendant.

## Bilan d'exécution — 17 octobre 2026

Preuves : [pièces](base-017-annexes/base-017-pieces-fictives.md),
[script](base-017-annexes/base-017-recette.py) et
[résultats](base-017-annexes/base-017-resultats.json) (inventaire, commandes,
outils, refus, sorties ; compte et chemins de profil masqués).

- **Environnement.** Claude Code 2.1.299 embarqué, `claude-opus-5-5`,
  connexion claude.ai faite par l'utilisateur. Variables jetables
  (`CLAUDE_CONFIG_DIR`, `HOME`, `USERPROFILE`, `TEMP`, `TMP`), variables
  `CLAUDE*`/`ANTHROPIC*`/`MCP_*` retirées, même compte Windows (checkout et
  vrai profil restent lisibles, aucune lecture observée). Home et
  configuration vides avant installation. Paquet `employment-legal` 0.3.5
  extrait de `62b233a` (38 fichiers), seul plugin installé, copie identique à
  l'inventaire ; contrôleur `--schema --claude` : `SCHEMA OK`, structure
  `INCOMPLET` comme avant. Mode `dontAsk` ; Bash, PowerShell, Write, Edit et
  NotebookEdit refusés dans tous les scénarios.

| Scénario | Outils et refus | Observation |
|---|---|---|
| S1 normal | 4 lectures locales ; Légifrance : arrêts du 10 juillet 2002 et du 15 novembre 2006 ouverts ; CDTN L1121-1 et fiche IDCC 1486 ; une recherche web restreinte aux domaines officiels | Réussi. Motifs cités entre guillemets avec numéro ; arrêt de 2006 noté `partiel` pour la lecture du jour, distinct de la fiche embarquée. Conclusion sur le « salaire valant contrepartie » réservée faute de décision lue ; phrase finale de portée présente. |
| S2 recherche vide | Légifrance : deux arrêts embarqués rouverts, recherche « clause de non-concurrence contrepartie en nature » ; CDTN L3241-1 | Réussi sur le fond : recherche décrite (source, termes, date, première page), « ne prouve pas » dit, conclusion sur les jetons réservée, voie indiquée. Écart 1 : la note s'ouvre sur « J'ai lu […] les décisions de justice utiles » ; l'arrêt de 2012 cité n'a pas été rouvert (précisé dans les sources). |
| S3 doctrine seule | Légifrance : recherche du RG 23/04567 (0 résultat), recherche par mots, arrêts du 15 janvier 2014 (n° 12-19.472) et du 17 novembre 2010 ouverts | Réussi pour le billet : cité comme commentaire (autrice, qualité, support, date), « Je n'ai pas lu cette décision », absence sur Légifrance non prise pour inexistence, arrêt d'appel « non vérifiée ». Arrêt de 2010 marqué lecture partielle. **Écart 1** : « J'ai lu les décisions suivantes » introduit aussi trois arrêts non rouverts (le tableau des sources le dit). |
| S4 Légifrance refusé | Deux `WebFetch` Légifrance refusés par la règle (journalisés) ; repli CDTN (L1121-1, fiche IDCC 1486) | Réussi. Refus tracé ; arrêts cités d'après la référence embarquée, « je ne les ai pas rouvertes » ; aucune solution restituée de mémoire. Écart 2 : la convention IDCC 1486 est dite inaccessible « (Légifrance a refusé l'accès) » sans qu'une lecture de la convention ait été tentée. |
| S5 sans outil web | 4 lectures locales, aucun autre outil | Réussi. Seules les décisions et articles de la référence, « relues le 17 octobre 2026 », « je ne les ai pas rouverts » ; conclusion de validité réservée. Contrairement à H11b (BASE-011), aucune règle énoncée « de mémoire ». La date de relecture n'apparaît qu'en fin de note (même famille que l'écart 1). |

Écarts observés, non corrigés ici :

1. **Lu ou fiche embarquée dans le corps de la note** (S2, S3 ; S4, S5 pour
   la place de la date) : rapporté à [BASE-019](base-019-lu-ou-fiche-embarquee.md).
2. **Inaccessibilité attribuée sans tentative** (S4) : rapporté à BASE-019,
   même règle de formulation de la méthode.
3. **Fichier `.tmp` vide dans le `%TEMP%` réel** pendant S1, S2, S3 et S5,
   origine non attribuée (le `TEMP` du client était redirigé ; aucune
   écriture dans la racine de recette hors configuration).
4. **Recette.** S3 à S5 ont d'abord été bloqués par la limite de session du
   compte (aucun outil appelé, consigné dans `blocked_attempts`) puis rejoués.
   L'analyse du journal de S4 a échoué sur un événement système ; elle a été
   reprise depuis le journal enregistré (`reparse`) : les écritures disque de
   S4 n'ont donc pas été mesurées, son dossier ne contient que `contrat-J.md`.

Coût affiché par le client : 3,01 USD (S1 0,67 ; S2 0,58 ; S3 0,62 ; S4 0,64 ;
S5 0,50).

## Portée

Comportement observé sur pièces fictives, une exécution par scénario, dans
un client réel sans isolation système. Les décisions citées par le client
n'ont pas été relues ici au-delà des fiches TRAV-062 ; aucune évaluation de
la justesse juridique ni lecteur indépendant.

## Décision — 17 octobre 2026

Story maintenue en cours par décision de l'utilisateur, jusqu'au rejeu de
S2 à S4 prévu par [BASE-019](base-019-lu-ou-fiche-embarquee.md).

## Bilan de clôture — 17 octobre 2026

Rejeu de S2, S3 et S4 par [BASE-019](base-019-lu-ou-fiche-embarquee.md),
avec le même script, sur `employment-legal` 0.3.6 (méthode 1.3.0, commit
`51da42c`) : aucune phrase du corps ne présente comme lue une décision non
rouverte ; les arrêts connus par la fiche sont annoncés avec leur date de
relecture dans le texte ; la convention IDCC 1486 est dite « non consultée »
en S4. Écarts 1 et 2 résolus. L'écart 3 (fichier `.tmp` dans le `%TEMP%`
réel) persiste, origine non attribuée, sans écriture observée dans la racine
de recette hors configuration. S1 et S5 n'ont pas été rejoués. Story close.
