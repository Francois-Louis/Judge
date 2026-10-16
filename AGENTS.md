# Instructions pour les agents

Ces consignes s'appliquent à tout le dépôt. Lire aussi le fichier
`CLAUDE.md` à la racine pour les conventions et les validations.

## Git : terminer par un commit et un push

- Travailler directement sur `main`, sans branche de travail ni pull request,
  sauf demande explicite contraire de l'utilisateur.
- Pour toute tâche qui modifie le dépôt, vérifier le diff et exécuter les
  contrôles pertinents, puis terminer par un `git commit` et un
  `git push origin main`. Cette consigne autorise ces actions sans redemander
  confirmation à chaque tâche.
- Inclure uniquement les changements de la tâche dans le commit. Préserver
  les modifications préexistantes et ne pas les embarquer sans instruction.
- Si le commit ou le push échoue, signaler le blocage et ce qui reste à faire.
  Ne pas forcer le push ni écraser l'historique distant.
