# Données personnelles — Vérification de l'intégration des besoins

Intégration documentaire du **16 octobre 2026**, liée à la [matrice des 60 points](exist-003-frictions-utilisateurs.md). Relevé distinct de la vérification historique d'EXIST-003 : les résultats et empreintes de ce lot initial sont conservés.

## Contrôles exécutés

Contrôles par script ponctuel Python en UTF-8, PyYAML et Git, puis `git diff --check` :

| Contrôle | Résultat |
|---|---|
| Archive source | Copie identique octet pour octet à la pièce jointe. SHA-256 : `91555906d2f6a92f56c84cfcff46ddb015fc5bb3fdf4506e6357d5605afa3f4c`. |
| Numérotation | Source et matrice contiennent exactement 1 à 60, dans le même ordre, sans manque ni doublon. |
| Ajouts | Treize stories PRV-022 à PRV-034, toutes `proposee`, nature `implementation` ; champs requis, entrées, travail attendu, sources à rechercher, exclusions et cas normal/limite présents. |
| Dépendances | 462 identifiants uniques dans le backlog ; aucune dépendance absente ni cycle. |
| Statuts | 36 `terminee`, une `en-cours`, une `a-verifier`, 424 `proposee`. |
| Index PRV | PRV-001 à PRV-034 figurent une fois, dans l'ordre, dans le tableau de découpage ; README du backlog synchronisé. |
| Situations quotidiennes | S-01 à S-52 présentes une fois ; S-42 précisée, S-51 fuite et S-52 démarchage/traceurs ajoutées. |
| Liens et format | 570 liens Markdown locaux résolus sur les 56 fichiers Markdown modifiés ou ajoutés de l'état de travail, travaux antérieurs compris ; fins de fichier et absence d'espaces finaux vérifiées. `git diff --check` passe. |
| Périmètre | Tous les chemins modifiés ou ajoutés de l'état de travail restent sous `backlog/`. Les travaux antérieurs présents ont été conservés. |

## Relecture documentaire

La relecture a séparé les demandes du particulier de la réponse organisme, le retrait source du déréférencement et la plainte CNIL de la réparation. Les attributions sont des exigences de sortie ; elles ne répondent pas juridiquement aux situations du texte.

Deux erreurs de routage ont été traitées : DOM-007 porte le dossier médical (DOM-009 concerne les douanes) ; BNK-006 porte le prélèvement et ne peut recevoir le refus de crédit. La correction médicale porte sur le découpage courant, avec erratum dans EXIST-003 ; les anciennes pièces de preuve restent conservées. Le refus de crédit au particulier est indiqué à découper dans DOM-004, avec PRV-031 pour la demande relative au traitement automatisé.

La relecture a également vérifié les limites de l'opposition PRV-023, bornée à la prospection : une réutilisation IA hors prospection passe par PRV-026 avant choix d'un droit ou nouvelle tranche. Une observation d'interface PRV-027 ne vaut pas audit technique. PRV-032 vise la victime ; la réponse à incident côté organisme reste à découper.

Les compléments sectoriels précisent les besoins encore à découper : dossier médical, justificatifs locatifs, surveillance et sanction au travail privé/public, diffusion des registres d'EI, refus de crédit, dommage et recours juridictionnels. Les douze scénarios de la matrice et les cas des treize nouvelles stories sont des recettes attendues, sans résultats métier revendiqués.

## Portée

Contrôles documentaires et statiques, avec relecture par l'agent de maintenance ; aucune recherche juridique externe, validation des statistiques/règles/dates fournies, exécution de skill, recette client ou lecture indépendante. Les treize stories restent proposées. Aucun plugin, manifeste, référence embarquée, script, contenu éditeur ou NOTICE n'est modifié par cette intégration. Aucun envoi, dépôt, suppression, accès à un système ou déploiement n'est réalisé. Les règles et canaux cités devront être vérifiés dans chaque lot d'implémentation.
