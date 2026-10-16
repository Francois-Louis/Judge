# Rétrospective de l'epic 05-usages-quotidiens

Établie le **15 octobre 2026 (Europe/Paris)** sur USAGE-001 et USAGE-002,
après relecture des six livrables, de la matrice des situations et des
documents qu'ils modifient (README, BASE-003, PILOTE-002, NOTICE), puis
nouvelle exécution des contrôles documentaires. Les corrections qui ne
demandaient aucune décision sont tracées dans
[USAGE-003](usage-003-corrections-retrospective.md).

## Bilan

Les deux stories de cadrage sont terminées et leurs livrables sont cohérents
avec BASE-003. L'epic ne produit aucun point d'entrée exécutable, ce qui était
son périmètre. Son principal livrable, le protocole d'orientation, n'est
cependant encore utilisé par aucune story en aval (écart 2).

| Story | Statut | Point ouvert |
|---|---|---|
| USAGE-001 | terminee | Contrôle de compréhension avec un utilisateur réel non exécuté |
| USAGE-002 | terminee | **Choix du pilote à arrêter** par l'utilisateur ; rangs 2 à 5 à réexaminer à PILOTE-003 |

Contrôles rejoués sur les six fichiers de l'epic, la matrice, le README du
backlog, PILOTE-002 et le dossier BASE-003 : 232 liens locaux résolus, aucune
cible absente ; tableaux de largeur cohérente, UTF-8, fin de ligne finale,
aucun espace de fin de ligne ; 81 stories à identifiants distincts (12
terminées, une en cours, 68 proposées) ; 42 lignes dans la matrice, chacune
avec un seul cadrage principal ; `git diff --check` sans erreur.

## Ce qui a bien marché

- Séparation orientation / métier : la matrice ne garde que domaine principal,
  frontière et question discriminante ; règles, délais et sources restent aux
  domaines. Aucun plugin généraliste n'a été créé.
- Protocole concret : questions ordinaires posées une ou deux à la fois, six
  formes de restitution, urgences traitées d'abord, examen des engagements des
  deux parties, minimisation des pièces et aucun envoi sans autorisation.
- Les croisements difficiles sont traités explicitement : achat et paiement,
  relance et acte d'exécution, aidant sans mandat, petit exploitant avec trois
  interlocuteurs, montant jamais utilisé comme seuil de routage.
- USAGE-002 sépare utilité potentielle et capacité de livraison, n'invente
  aucune statistique et reconnaît que T1 profite peu au retraité et seulement
  sous condition au petit exploitant.
- Discipline de preuve maintenue : récits fictifs, absence d'utilisateur réel
  et de source externe consultée signalés dans chaque relevé.

## Écarts constatés

1. **Aucun commit, une seconde fois.** L'epic n'existe que dans le worktree,
   entremêlé avec PILOTE-001 et BASE-010 dans les mêmes fichiers (README,
   NOTICE, PILOTE-002, CLAUDE.md). C'est l'écart 1 de la rétrospective des
   fondations : la leçon n'a pas été reportée dans la façon de travailler.
2. **Protocole sans consommateur.** Ni PILOTE-002, ni le plan PILOTE-001, ni la
   [recette BASE-006](../../references/package-validation.md) ne renvoient au
   protocole USAGE-001. PILOTE-002 cite seulement la comparaison USAGE-002. Rien
   n'oblige donc le premier skill adapté à reprendre les formes de restitution,
   la minimisation des pièces ou le contrôle de reformulation.
3. **Protocole non versionné.** BASE-003 impose d'embarquer dans chaque plugin
   les références utiles à l'exécution, et la méthode BASE-005 porte une
   version (`1.0.0`). Le protocole, destiné à être repris par les futurs points
   d'entrée, n'a ni version ni copie embarquée prévue : les copies risquent de
   diverger.
4. **Critères cochés sur une relecture faite par l'auteur.** « Des mots
   ordinaires suffisent » et « sans jargon non expliqué » sont cochés à partir
   de restitutions écrites par l'auteur du protocole et relues par lui. Les
   limites le disent, mais la case cochée laisse croire à davantage. La même
   réserve vaut pour les quinze croisements d'USAGE-002.
5. **Comparaison fermée dès le départ.** Les cinq tâches comparées étaient
   imposées par le texte de la story et reprennent les premières tranches déjà
   écrites dans PILOTE-002, DOM-006, DOM-015 et DOM-016 ; seule T2 s'écarte de
   DOM-022. T1 arrive en tête parce qu'elle est la mieux documentée, et elle est
   la mieux documentée parce qu'elle était déjà le pilote proposé. Le
   raisonnement tient, mais le critère qui a réellement décidé (capacité de
   livraison, non utilité) n'apparaît pas en une phrase dans le README.
6. **Densité des livrables.** Pour un epic consacré à l'accessibilité,
   environ 8 650 mots dans six fichiers et environ 190 tournures négatives ou
   restrictives (« ne … pas », « sans », « aucun »). Les mêmes réserves (pas
   d'utilisateur réel, pas de skill exécuté, pilote non arrêté) sont répétées
   dans le bilan, la comparaison, le relevé, le README, PILOTE-002 et NOTICE.
   La relecture s'en trouve alourdie et le contenu de fond dilué.
7. **Situations sans identifiant stable.** Les 42 lignes de la matrice n'ont
   pas d'identifiant ; USAGE-002 a dû créer des numéros locaux T1 à T5 qu'il
   déclare non réutilisables. Les futures stories ne pourront pas citer une
   situation de façon fiable.
8. Points mineurs :
   - NOTICE recense les nouveaux fichiers du backlog story par story, dans un
     ordre non chronologique (USAGE-002, USAGE-001, BASE-008, PILOTE-001/BASE-010,
     BASE-009). Ce recensement va au-delà des fichiers modifiés et grossit à
     chaque story.
   - Dans PILOTE-002, une ligne vide coupe la liste « Points de départ » en deux.
   - Le relevé USAGE-001 indique « 11 terminées, 69 proposées » : exact à sa
     date, désormais 12 et 68.

## Suites

| Action | Traitement |
|---|---|
| Écart 1 : commits séparés (PILOTE-001/BASE-010, epic 05, corrections), sans push | Réalisé dans USAGE-003, branche `usages-quotidiens/usage-001-003` |
| Écart 2 : renvoi au protocole depuis PILOTE-002 et la checklist d'un skill BASE-006 | Corrigé dans USAGE-003 ; recette en version 1.1.0 |
| Écart 3 : version du protocole et règle de reprise | Corrigé dans USAGE-003 : version 1.0.0, exigences reprises par chaque skill avec la version citée, sans copie intégrale |
| Écart 4 : critères vérifiés sur papier | Mention ajoutée dans USAGE-001 ; critère d'essai réel ajouté à PILOTE-002 |
| Écart 5 : critère déterminant du classement | Phrase ajoutée au README |
| Écart 6 : densité des réserves | Règle « Portée » ajoutée au [modèle de story](../story-template.md) ; les livrables existants ne sont pas réécrits |
| Écart 7 : identifiants des situations | Corrigé : `S-01` à `S-42`, T1 à T5 rattachés |
| Points mineurs | Liste PILOTE-002 réunifiée, décompte daté, lignes vides finales retirées |
| Choix du pilote | **Décision de l'utilisateur**, avant tout développement de PILOTE-002 |
| Essai de compréhension réel | Critère de PILOTE-002, non coché sans participant |
| NOTICE | Décidé le 16 octobre 2026 : seuls les fichiers hors `backlog/` sont recensés ; listes existantes nettoyées |
