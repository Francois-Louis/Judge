# Frictions contentieuses — Relevé d’intégration

Intégration documentaire du **16 octobre 2026**, à la demande de l’utilisateur. Le [texte fourni](../sources/contentieux-frictions-2026-10-16.txt) est conservé intégralement ; la [matrice](exist-006-frictions-utilisateurs.md) trace les 125 points, les tableaux, les douze étapes pratiques et les tâches encore à découper.

## Contrôles de production exécutés

- Archive comparée à la pièce jointe octet pour octet ; SHA-256 : `01dc02ebcae2021698845203a9b07038021be2df209a3326d06d70308049cd68`.
- Extraction et unicité des points : ensemble exact 1 à 125 dans la source et dans la répartition générée, sans point omis.
- Douze nouvelles stories CTX-030 à CTX-041 : statut `proposee`, nature `implementation`, entrées, sortie, fichiers cibles, travail attendu, sources à rechercher, exclusions et cas normal/limite. Aucun champ ne revendique une exécution.
- Découpage CTX : 41 propositions ; lecture, prescription, échéance de procédure et appel borné conservent des sorties distinctes. Source utilisateur archivée, pièces de contrôle historiques non réécrites.
- Index recalculé depuis les identifiants du backlog courant : 495 stories ; répartition `{"a-verifier": 1, "en-cours": 1, "proposee": 457, "terminee": 36}`.
- Situations quotidiennes : S-47 précisée ; S-60 expertise, S-61 jugement et S-62 accord avant échéance ajoutées.

## Relecture documentaire

Les 125 rattachements sont des exigences de sortie. Les tâches d’exécution existantes sont réutilisées ; injonction créancier et opposition débiteur sont séparées. Les tâches administratives ne sont pas transposées depuis le suivi TJ, la protection sociale conserve sa qualification sectorielle, et le pénal garde ses voies et calendriers. Les sorties encore sans story d’implémentation restent indiquées « à découper » dans la matrice et dans leurs cadrages propriétaires.

Les quinze scénarios de la matrice et les cas des douze stories sont des recettes futures, non des résultats métier observés.

## Contrôles statiques finaux exécutés

- 29 fichiers du lot, dont 12 nouvelles stories, la source archivée, la matrice et le présent relevé ; les autres fichiers prolongent les cadrages, propositions et index existants.
- 125 libellés comparés à la source, dans l’ordre, sans point omis ni doublon ; la partie avant une éventuelle flèche de défense est conservée.
- 41 lignes CTX présentes une fois et dans l’ordre dans le tableau de découpage ; chaque nouvelle proposition contient les champs, entrées, critères et scénarios attendus.
- 495 identifiants de story uniques dans l’état courant du backlog ; toutes les dépendances existent, aucun cycle détecté. Ce total inclut les autres travaux présents dans le workspace, sans les attribuer à cette intégration.
- 624 liens Markdown locaux résolus sur les 28 fichiers Markdown du lot ; aucun lien absent au contrôle final. Le relevé IA qui manquait lors d’un contrôle intermédiaire existe désormais dans l’autre lot.
- Fins de fichier et absence d’espaces finaux contrôlées ; `git diff --check` passe.
- S-60 à S-62 sont chacune présentes une fois. D’autres ajouts ont eu lieu pendant l’intégration : l’état global contient 63 lignes de situation et un doublon S-56 entre les entrées emballages et orientation IA, hors des trois entrées contentieuses. Ce doublon est signalé sans renuméroter les entrées ni les références des autres lots.

Ces vérifications portent sur les documents et leurs liens, pas sur la validité juridique ou l’exécution des futurs skills. Les deux scripts temporaires de production/contrôle sont retirés ; aucun outil n’est ajouté au plugin.

## Portée

Intégration et relecture par le seul agent de maintenance. Aucune recherche juridique externe, validation des règles/seuils/délais/réformes fournis, consultation résolue, exécution de skill, installation, recette client ni lecture indépendante. Aucun plugin, manifeste, référence embarquée, contenu éditeur ou NOTICE modifié. Aucun envoi, dépôt, signature, publication ou déploiement. Les propositions ne sélectionnent aucune tranche de développement. Les modifications déjà présentes dans le workspace sont conservées.
