# DOM-012 — Relais issus des frictions travail

Complément du 16 octobre 2026 à la [story de cadrage](../dom-012-protection-sociale.md),
issu de la [matrice travail](../../01-pilote-travail/pilote-001-annexes/pilote-001-frictions-utilisateurs.md).
Ces tâches candidates restent à découper et hiérarchiser ; la première tranche
proposée de DOM-012 (lecture d'un indu choisi) reste inchangée.

| Points du guide travail | Tâche sociale à découper | Entrées et sortie à prévoir | Frontière et cas limite attendu |
|---|---|---|---|
| 1 ; 7.01–08 | Préparer une déclaration initiale d'accident au régime compétent, puis une réponse pendant l'instruction | Événement, lieu/heure, témoins, certificat initial, déclaration/version contestée, réserves, demandes, dates/réceptions ; dossier et brouillon adaptés au stade | CPAM/MSA et qualité du demandeur vérifiées ; carence employeur et déclaration directe distinctes. TRAV-040 garde signalement et version factuelle. Réserves patronales ne sont pas la décision de caisse ; pas de reconnaissance garantie ni règle AT transposée sans examen à l'accident de trajet. |
| Titre 7 ; 7.17 | Préparer un dossier de reconnaissance de maladie professionnelle pour une maladie identifiée | Certificat et diagnostic établis par médecin, expositions/postes, périodes, tableau ou voie invoquée et notification ; pièces et voie à vérifier | Ne pas déduire du seul antécédent une absence de lien au travail ; ne produire aucun diagnostic. Un événement soudain et une maladie liée à exposition ne suivent pas un dossier unique par défaut. |
| 7.06 ; refus éventuel après instruction | Lire une décision de reconnaissance ou de refus AT/MP et préparer le recours propre | Décision intégrale, motifs, voies, réception, instruction et pièces autorisées ; fiche de contestation factuelle et calendrier à vérifier | Instruction, refus administratif et question médicale distingués ; identifier organe de recours et juridiction selon l'acte, sans circuit CRA/CMRA universel. Une contestation patronale n'est pas présumée être le refus définitif reçu par le salarié. |
| 7.10–11 | Lire une notification de consolidation ou de taux d'incapacité permanente, en tâches séparées | Notification, date prouvée, avis et séquelles documentées par médecin ; explication de la décision et dossier pour conseil/recours compétent | Consolidation distincte de guérison ; pas de taux ni d'indemnité déterminés par le plugin. Réception incertaine : urgence et pièces manquantes, aucune date de recours par défaut. |
| 7.12 | Préparer les pièces d'une demande liée à la faute inexcusable de l'employeur | Risque, connaissance alléguée, alertes, prévention, événement, reconnaissance et dates utiles ; chronologie et pièces pour l'avocat compétent | Preuve du danger, absence de mesures, compétence et prescription à rechercher ; ni faute ni réparation forfaitaire présumées. Volet pénal distinct DOM-002, effets contractuels dans travail. |
| 7.21 ; 7.09/17 selon la décision | Lire une notification d'invalidité ou d'indemnisation choisie | Organisme, statut, prestation, notification et réception, pièces minimales ; motifs et questions pour le recours adapté | Invalidité sociale distincte de l'avis d'inaptitude professionnelle TRAV-042 ; maintien de salaire employeur distinct des IJ et décisions de caisse. Pas de dossier médical complet systématique. |
| 10.03/20 ; 12 | Lire une décision d'indemnisation chômage après départ ou CSP | Acte de rupture, dossier CSP, France Travail, décision, périodes et réception ; explication et dossier de correction/contestation à découper | TRAV-049/050 gardent effets contractuels et choix ; prestations et différé ne sont pas garantis par l'appellation du départ. Choisir le régime applicable avant calcul ou recours. |

Pour chaque future suite : une tâche, un acte ou résultat, un propriétaire,
une source/version effectivement lue, la date déclenchante et sa preuve,
l'unité de décompte, exceptions/transitions, l'acte requis et son destinataire.
Séparer déclaration, instruction, notification, recours préalable, contentieux
social et prescription de réparation. Réclamation employeur, demande RGPD et
négociation ne reçoivent aucun effet suspensif ou interruptif automatique.

Sources futures : Code de la sécurité sociale, Code du travail selon l'objet,
textes des régimes, Assurance maladie/MSA, Unédic/France Travail et jurisprudence
officielle. Ces pistes restent à lire ; les nombres et affirmations du guide
ne sont pas validés. Le plugin proposé `social-security-legal` devra embarquer
ses références et la méthode locale BASE-005, sans requérir `employment-legal`
installé. Un relais indisponible reçoit une fiche manuelle et un interlocuteur
compétent, jamais un appel à un skill inexistant.

Scénarios ci-dessus **attendus, non exécutés**. Portée documentaire et contrôles :
[vérification travail](../../01-pilote-travail/pilote-001-annexes/pilote-001-frictions-verification.md).
