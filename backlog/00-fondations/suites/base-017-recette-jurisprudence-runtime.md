---
id: BASE-017
titre: "Recetter la recherche de jurisprudence d'un skill dans un client isolé"
statut: en-cours
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

- [ ] Les cinq scénarios sont exécutés et journalisés dans le client isolé.
- [ ] Aucune sortie ne présente une décision non ouverte comme lue.
- [ ] Les écarts observés sont rapportés aux stories concernées sans être corrigés dans cette story.

## Vérification

La recette elle-même ; le critère 1 reste non coché tant qu'elle n'est pas exécutée.

## Hors périmètre

Évaluation de la justesse juridique des solutions, autres plugins, lecteur indépendant.

## Exécution partielle — 17 octobre 2026

Preuves : [pièces](base-017-annexes/base-017-pieces-fictives.md),
[script](base-017-annexes/base-017-recette.py) et
[résultats](base-017-annexes/base-017-resultats.json) (inventaire, commandes,
outils, refus, sorties ; identifiants masqués).

- **Environnement.** Claude Code 2.1.299 embarqué, `claude-opus-5-5`,
  connexion claude.ai faite par l'utilisateur. Variables jetables
  (`CLAUDE_CONFIG_DIR`, `HOME`, `USERPROFILE`, `TEMP`, `TMP`), même compte
  Windows ; home et configuration vides avant installation. Paquet
  `employment-legal` 0.3.5 extrait de `62b233a` (38 fichiers), seul plugin
  installé ; copie identique à l'inventaire ; `--schema` : `SCHEMA OK`.
  Mode `dontAsk`, Bash/PowerShell/Write/Edit refusés.
- **S1 normal : réussi.** Arrêts du 10 juillet 2002 et du 15 novembre 2006
  ouverts sur Légifrance pendant la réponse, cités avec passages des motifs ;
  le second est noté `partiel` pour la lecture du jour, la fiche embarquée
  étant mentionnée à part. Conclusion sur l'argument « salaire pendant le
  contrat » réservée ; phrase finale de portée présente (critère 4 de TRAV-062).
- **S2 recherche vide : réussi.** Recherche Légifrance décrite (termes, date,
  première page), absence de résultat non prise pour une absence de
  jurisprudence, conclusion réservée, voie indiquée. L'arrêt de 2012, non
  rouvert, est cité depuis la fiche avec sa date de relecture.
- **S3, S4, S5 : non exécutés.** Le client a répondu « You've hit your session
  limit · resets 11:40am (Europe/Paris) » sans appeler d'outil (code 1).
- **Écart.** Un fichier `.tmp` vide est apparu dans le `%TEMP%` réel pendant
  S1 et S2 ; origine non attribuée (le `TEMP` du client était redirigé).

Aucune sortie exécutée ne présente une décision non ouverte comme lue. Les
critères restent non cochés tant que S3 à S5 ne sont pas rejoués
(`base-017-recette.py run <racine> S3`, nouvelle racine si l'ancienne est effacée).
