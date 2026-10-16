# Gouvernance IA — Vérification de l'intégration des besoins

Intégration documentaire du **16 octobre 2026**, liée à la [matrice des 50 points](exist-005-frictions-utilisateurs.md). Relevé distinct des contrôles du cadrage initial EXIST-005 ; ses résultats et empreintes historiques restent conservés.

## Contrôles exécutés

Contrôles ponctuels Python en UTF-8 avec PyYAML : comparaison des octets et empreinte, frontmatter, graphes de dépendances, numérotation et liens locaux. `git diff --check` exécuté sur l'état de travail.

| Contrôle | Résultat |
|---|---|
| Archive source | Copie identique octet pour octet à la pièce jointe. SHA-256 : `5d85b2bc0994a0a9e12a5e2facd1d0006a8be09a54362cc7bd418742cc0cca2e`. |
| Couverture | Source et matrice contiennent exactement 1 à 50, dans le même ordre, avec libellés identiques ; aucun manque ni doublon. Sections pratiques et douze scénarios F01 à F12 présents. |
| Nouvelles propositions | IA-021 à IA-024 et PRV-035 : toutes `proposee`, nature `implementation`, champs requis et cas normal/limite présents. |
| Dépendances | 495 identifiants uniques sur le backlog courant ; aucune dépendance absente ni cycle. |
| Statuts et index | 36 `terminee`, une `en-cours`, une `a-verifier`, 457 `proposee` ; compteur du README synchronisé sur l'état courant, ajouts simultanés compris. IA-001 à IA-024 et PRV-001 à PRV-035 figurent une fois et dans l'ordre dans leurs tableaux. |
| Situations quotidiennes | 63 identifiants uniques S-01 à S-63. Les quatre ajouts IA portent S-57 à S-59 et S-63 ; la collision avec une entrée créée dans une autre session a été résolue en renumérotant seulement l'entrée IA concernée. |
| Liens et format | 489 liens Markdown locaux résolus sur les 30 fichiers Markdown du lot ; fins de fichier et absence d'espaces finaux vérifiées. `git diff --check` passe. |
| Périmètre | 31 fichiers du lot, tous sous `backlog/`, dont l'archive texte. Les autres travaux présents ne sont pas inclus dans ce lot. |

## Relecture documentaire

La relecture a distingué les demandes de la personne affectée et les tâches de l'organisation, l'explication et le recours au fond, l'opposition hors prospection et la réponse organisme, la fiche incident et la notification réglementaire, les justificatifs fournisseur et une certification. Les douze scénarios F01 à F12 et les cas des cinq propositions décrivent des recettes attendues, sans exécution métier revendiquée.

IA-021 à IA-024 et PRV-035 ont chacun leurs entrées, un résultat borné, des fichiers futurs, des sources à rechercher, des critères, un cas normal, un cas limite et des exclusions. Ils restent `proposee`. Les tâches sectorielles encore sans story sont précisées dans travail privé/public, administratif, protection sociale, éducation, plateformes, expression, pénal et propriété intellectuelle. Le simple fait qu'un système soit qualifié d'IA ne crée pas une discrimination, une infraction, un droit universel au réexamen humain ou un droit de voir tout le code.

Le calendrier « AI Omnibus » est isolé comme assertion du texte fourni. La version, le passage officiel, le rôle, le champ et la disposition temporelle doivent être recherchés avant toute conclusion ; une annonce ne devient pas texte modificatif. Les délais des différentes procédures ne sont pas copiés comme paramètres par défaut. Les références juridiques générées doivent être comparées aux textes lus ; une recherche infructueuse ne prouve pas leur inexistence.

## Fichiers du lot

- Archive source, matrice et présent relevé.
- Cinq propositions : IA-021 à IA-024 et PRV-035.
- EXIST-005, EXIST-003 et leurs découpages courants ; compléments IA-003/005/012/013/020, PRV-022/031 et EXIST-008.
- Compléments du découpage travail et des cadrages DOM-002/010/012/027/029/034/037/043.
- Index du backlog et matrice des situations quotidiennes.

## Portée

Intégration documentaire et contrôles statiques par l'agent de maintenance ; aucune recherche juridique externe, validation du calendrier/des règles fournis, adaptation ou exécution de skill, recette client ou lecture indépendante. Les nouveaux fichiers runtime sont des cibles futures. Aucun plugin, manifeste, référence embarquée, contenu éditeur ou NOTICE modifié par ce lot limité à `backlog/`. Les travaux déjà présents et les ajouts d'autres sessions sont conservés ; les décomptes globaux décrivent l'état de travail au moment du contrôle. Aucun envoi, dépôt, révocation, effacement, notification ou déploiement exécuté.
