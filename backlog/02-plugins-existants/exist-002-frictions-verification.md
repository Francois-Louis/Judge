# Formalités des entreprises — Vérification de l'intégration des besoins

Intégration documentaire du **16 octobre 2026**, liée à la [matrice des 100 points](exist-002-frictions-utilisateurs.md). Ce relevé est distinct de la vérification historique d'EXIST-002 ; il ne modifie pas les preuves ou empreintes de ce lot.

## Contrôles exécutés

Contrôles exécutés par un script ponctuel Python (lecture UTF-8, PyYAML et commandes Git), puis contrôle des espaces avec `git diff --check`. Résultats observés :

| Contrôle | Résultat |
|---|---|
| Fidélité de l'archive | Identité octet pour octet avec la pièce jointe. SHA-256 : `8ae096fc1994852ac06c7b00d83682ad28373997600559156f300a58828a4d84`. |
| Points numérotés | Source et matrice contiennent exactement 1 à 100, dans le même ordre, sans manque ni doublon. |
| Propositions ajoutées | SOC-023 à SOC-027, COM-019/020 et TRAV-019 à TRAV-021 : dix identifiants uniques, statut `proposee`, neuf implémentations et un cadrage. Chaque proposition possède entrées, résultat, sources à rechercher, exclusions et deux scénarios attendus. |
| Frontmatter et dépendances | 449 stories identifiées ; aucune référence de dépendance manquante ni cycle. Champs requis présents dans les dix ajouts. |
| Index | 27 SOC, 20 COM et 21 TRAV ; chacune des nouvelles propositions figure une fois dans son tableau. Total du backlog : 36 `terminee`, une `en-cours`, une `a-verifier`, 411 `proposee`. |
| Situations quotidiennes | S-01 à S-50 présentes une fois ; S-49 dossier de formalité bloqué et S-50 demande d'inscription ou abonnement prétendument obligatoire ajoutées sans renumérotation. |
| Liens locaux | 437 liens contrôlés dans les 32 fichiers Markdown modifiés ou ajoutés, tous résolus. |
| Format et périmètre | Fins de fichier et absence d'espaces finaux vérifiées sur les Markdown ; `git diff --check` passe. 33 fichiers modifiés ou ajoutés, tous sous `backlog/`, dont l'archive source préservée. |

La relecture documentaire distingue les branches EI/société, les formes unipersonnelles, les acteurs techniques/de validation, les frais officiels/privés et les recours fiscaux/sociaux. Les attributions du tableau sont des exigences de sortie, pas des réponses aux consultations du texte. Les ajouts parallèles du dépôt, notamment DOM-043 et S-48, sont conservés ; les décomptes tiennent compte de cet état.

## Portée

Le texte utilisateur est une expression du besoin, conservée sans modification. Les vérifications sont documentaires et statiques : aucune recherche juridique externe, exécution de skill, recette en client ou lecture par un utilisateur indépendant. Les douze scénarios de la matrice et ceux des nouvelles stories restent attendus, non exécutés. Les dates, seuils, réformes et voies de recours cités dans la source restent à vérifier dans les futures implémentations.

Les dix nouvelles stories sont proposées (neuf implémentations et le cadrage SOC-027). Les impôts courants et formalités d'EI de DOM-039, les tâches fiscales de DOM-011, les recours Urssaf d'un employeur société et les procédures d'entreprise en difficulté restent à découper. Aucun plugin, manifeste, script ou contenu éditeur n'est modifié par cette intégration.
