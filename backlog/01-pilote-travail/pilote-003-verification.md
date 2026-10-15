# PILOTE-003 — bilan de recette du pilote

15 octobre 2026, Europe/Paris. **Résultat : recette incomplète, pas de
généralisation engagée.** PILOTE-002 et PILOTE-003 restent `a-verifier`.
La demande d'implémentation autorise ce bilan ; elle ne choisit pas un second
skill et ne vaut pas décision de publier le paquet.

## Constats confirmés

Le découpage fonctionne sur le plan documentaire : une tâche principale,
`hiring-review`, possède sa méthode et ses références dans le plugin
`judge-fr-eu-employment-legal` `0.2.0`. Le parcours candidat distingue faits,
sources, effet concret, question et destinataire ; il ne nécessite pas de
playbook d'entreprise. Les 19 autres skills et l'agent congés restent hérités.

Les [preuves techniques](pilote-003-controles.json) identifient la révision de
départ **et l'état de travail non commité**, chaque fichier du paquet, le ZIP
et leurs empreintes. L'artefact a été copié hors du checkout, sans autre plugin,
puis contrôlé depuis sa propre racine avec une copie séparée du vérificateur.
Les [scénarios relus](pilote-003-relecture.md) et les
[sources relues](pilote-003-sources-lues.json) sont des preuves distinctes.

| Couche réellement contrôlée | Résultat et preuve |
|---|---|
| Structure BASE-006 du paquet détaché | Code **2**, `STRUCTURE INCOMPLET`, 28 Markdown examinés, aucun `ECHEC`, **52 `A_RELIRE`**. Journal complet dans `structure`. Aucun succès général du paquet annoncé. |
| Méthode BASE-005 | Version `1.0.0`, copie embarquée identique octet pour octet à la source ; deux empreintes dans `method`. |
| Identité du lot | Version `0.2.0` ; nom/description/auteur identiques au marketplace, source `./employment-legal` ; syntaxe JSON contrôlée. |
| Helper livré, profil absent | Exécution réelle du Python embarqué avec `--home` fictif : `content: null`, `status: interview-required`, un seul événement de lecture du profil du fork. Le profil témoin d'origine n'est pas importé. |
| Helper livré, profil minimal | Création explicite puis relecture d'un profil fictif candidat. Un seul fichier créé ; témoins origine/autre dossier inchangés ; contenu du paquet inchangé. Ce test ne fait pas exécuter l'entretien par un modèle. |
| Fixtures du contrôleur BASE-006 | **11 tests réussis**, journal `regressions`. |
| Régression BASE-008 | **14 tests réussis sur 16, 2 ignorés** : `jsonschema` absent pour l'orchestrateur ; privilège Windows absent pour le lien symbolique réel. Jonctions et liens physiques effectivement testés. |
| Relecture des sources et sorties | Douze articles CDTN relus par accès réseau réel ; confrontation aux pièces et aux sorties PILOTE-002, puis application rédactionnelle des autres variantes. Pas de texte collectif ni de décision de non-concurrence ajouté aux sources vérifiées. |

La relecture des 52 signalements couvre quatre familles : données persistantes
du fork, chemins calculés de dossiers/registres, mention du profil personnel
comme accès interdit, orientation optionnelle de l'entretien vers le hub.
Les deux premières passent par le contrat du helper, sans prouver que le modèle
le respectera. Les deux dernières ne sont pas des ressources nécessaires à la
revue. Aucun signalement n'est masqué ni converti en succès de structure.

## Vérifications impossibles dans cette session

| Contrôle | Statut et cause constatée | Condition de reprise |
|---|---|---|
| Schéma officiel du plugin | **Exécuté en reprise le 15 octobre 2026** avec le binaire `claude` 2.1.299 embarqué par l'application desktop, sans installation : artefact exact (ZIP et 36 empreintes inchangés), contrôleur `--schema` code 2 avec `SCHEMA OK: code 0`, mêmes 52 `A_RELIRE` ; `claude plugin validate` passe avec le seul avertissement attendu sur `CLAUDE.md`. Voir le [schéma CLI](pilote-003-schema-cli.json). | Clos pour cet artefact. À rejouer sur tout nouvel artefact. |
| Schéma officiel du marketplace | **Exécuté en reprise** : fichier d'empreinte identique au lot, `claude plugin validate` code 0. | Clos pour ce fichier. |
| Installation du seul plugin | **Non exécutée**. Aucun client Claude disponible ; `docker info` échoue car le moteur Docker Desktop n'est pas joignable. | Environnement jetable avec client authentifié et accès au seul paquet et aux fixtures. Le Docker présent sur le PATH ne suffit pas. |
| Commande et scénarios réels | **Non exécutés**, H01–H16 compris, installation préalable indisponible. | Invocation de `/judge-fr-eu-employment-legal:hiring-review`, conservation des ressources lues, outils, sorties et erreurs. |
| Compréhension non juriste | **Non exécutée**, aucun participant réel. | Recueillir sans aide du rédacteur engagement, question, interlocuteur et réserve, corriger puis refaire lire si nécessaire. |

Ni les essais du helper ni une variable de dossier personnel de test ne
rendent le checkout et le profil réel inaccessibles. Aucune session client
n'a été lancée avec les identifiants ou les connecteurs du compte utilisateur.

## Effets indirects des composants livrés

| Composant relu dans le paquet | Constat et conséquence pour la recette |
|---|---|
| `CLAUDE.md` | Modèle de profil, pas contexte de projet automatiquement chargé à l'installation. La section PILOTE-002 donne priorité aux exceptions candidat ; plus bas restent profil société, en-têtes américains et attentes professionnelles. Un profil préexistant ne sera pas réécrit par une mise à jour du modèle. Tester ancien profil US, profil minimal et placeholders. |
| `cold-start-interview` | Branche candidat avant l'entretien hérité, aucune sauvegarde imposée. Après cette branche subsistent vérification de portée depuis le seul répertoire courant, handbook/mémos et profil société. La fin du chemin court n'ordonne pas explicitement d'arrêter cette lecture : ambiguïté à corriger par PILOTE-004 et à éprouver dans le client. |
| `customize` | Même branche ciblée, préservation des autres réponses demandée ; absence de transition terminale explicite avant le parcours professionnel. PILOTE-004 borne la modification d'une préférence sans traverser les autres sections. |
| Frontière de stockage `0.1.0` | Embarquée, identique au contrat BASE-008. Elle exige un entretien neuf si le profil manque ; le skill précise qu'il se déroule en conversation. Vérifier qu'`interview-required` ne devient pas une obligation de créer un profil professionnel. Aucun changement transverse fait ici. |
| `agents/leave-tracker.md` | Agent FMLA/USERRA/ADA, outils `Read`, `Write` et trois motifs MCP, **aucun outil d'exécution Python** déclaré. Il demande pourtant l'usage du helper pour les accès persistants : incompatibilité constatée, comportement réel non observé. Corriger dans TRAV-008 avant activation de cette tâche ; aucun ajout automatique de droits. |
| `skills/leave-tracker` et autres skills | Wrappers et descriptions hérités toujours découvrables. L'interdiction de les appeler dans `hiring-review` est explicite ; leur absence d'invocation réelle reste à observer, notamment sur « essai », « heures », « congés ». |
| `hooks/hooks.json` | `hooks: {}` : aucun hook ni script d'initialisation déclaré. Aucun déclenchement autonome déduit. |
| `.mcp.json` | Slack et Google Drive déclarés, catégories HRIS/documents/chat/email recommandées. Ces déclarations ne prouvent ni connexion ni absence de connexion automatique au chargement ; vérifier le client sans jeton. Aucun accès nécessaire à ces services pour lire les pièces fictives. |
| Horaire de l'agent | Le texte précise qu'il ne s'exécute pas seul et renvoie à une intégration séparée. Aucun planning n'a été créé. |

## Défauts, corrections et priorité

| ID | Défaut ou lacune constatée | Correction identifiée et résultat attendu | Condition avant extension |
|---|---|---|---|
| D01 | Installation, schémas et comportement non observés ; dépendance PILOTE-002 non close. | Poursuivre **PILOTE-002/PILOTE-003**, sans story de recette en doublon : compléter les journaux réels ci-dessous. | Bloquant pour conclure à la validation du pilote. |
| D02 | H01 est un extrait avec annexe, classification et textes collectifs absents ; aucun nominal complet. | **PILOTE-002** : ajouter un CDI fictif complet avec faits d'activité, classification et annexes cohérents ; authentifier/lire champ, textes collectifs et minima à la date retenue, puis exécuter H01. | Bloquant pour valider le nominal ; H04 ne le remplace pas. |
| D03 | Chemins courts de configuration suivis d'instructions professionnelles, sortie de branche ambiguë. | **PILOTE-004**, nouvelle story : modifier une préférence candidat sans charger ni créer le profil société ou des registres ; recette avec ancien profil et placeholders. | À corriger et vérifier avant réutilisation de ce setup dans un autre parcours. |
| D04 | Agent congés sans moyen déclaré d'exécuter son helper obligatoire ; contenu américain hérité. | **TRAV-008**, story existante précisée : choisir les capacités minimales compatibles avec le helper, tester l'échec sans exécuteur et le parcours adapté. | Bloquant pour activer le suivi congés, pas preuve d'échec de `hiring-review`. |
| D05 | Jurisprudence utile aux restrictions non lue ; durée/contrepartie/levée non analysées sur un cas complet. | **TRAV-017**, nouvelle tranche proposée depuis H02 : expliquer une clause de non-concurrence, sources et conséquences vérifiées ; réserve explicite jusque-là. | Pas de conclusion globale de validité sur cette clause. |
| D06 | H11b/H12 seulement préparés, aucun comportement après panne complète ; pas de pièce américaine littérale ni de public complémentaire dans les fixtures. | Relecture H11b/H12 consignée et pièces **H15/H16 ajoutées** ; reprise obligatoire dans le client de D01. | Lacune documentaire corrigée, recette dynamique toujours ouverte. |
| D07 | Pas de lecteur réel ; l'utilité et la compréhension ne sont pas mesurées. | **PILOTE-002/PILOTE-003** : consigner la reformulation réelle et les corrections, sans inventer de participant. | Bloquant pour les critères de compréhension. |

Les défauts documentaires peuvent être relus maintenant ; les comportements
suspectés ne sont pas présentés comme des erreurs déjà produites par le modèle.
La présence de fonctions héritées est un risque de périmètre, pas une preuve
qu'elles ont été appelées. Les corrections métier ne sont pas implémentées
par cette story de validation.

## Décisions d'architecture encore ouvertes

1. **Paquet mixte ou distribution limitée au pilote ?** Le paquet actuel
   conserve 20 skills et un agent ; seule la revue est adaptée. Avant une
   livraison, choisir explicitement le maintien avec limites visibles ou une
   distribution réduite et en éprouver les commandes. Aucune variante de
   packaging créée ici.
2. **Configuration minimale ou séparation des profils par parcours ?** La
   priorité locale suffit pour rédiger le pilote, mais son respect avec un
   ancien profil doit être observé. PILOTE-004 corrige le cas candidat ; la
   refonte générale reste TRAV-016, sans migration automatique.
3. **Accès officiel au runtime.** Les outils de maintenance BASE-010 ne sont
   pas embarqués. Choisir et éprouver les capacités de recherche du client,
   avec leurs voies officielles alternatives ; pas de souscription PISTE
   présumée ni de nouveau connecteur imposé.
4. **Prochaine tranche métier.** TRAV-001–TRAV-017 sont des propositions ;
   aucun ordre issu du seul nombre de sources n'est décidé. Toute extension
   attend la recette et une sélection explicite de l'utilisateur.

## Reprendre la vérification

Le JSON conserve les commandes exactes, chemins, codes et journaux. Pour
rejouer les seuls contrôles statiques, copier le plugin et le vérificateur
hors du dépôt, puis depuis la racine de l'artefact :

```powershell
python <outils>/check-plugin-package.py . --schema
```

Dans le dépôt, les contrôles de régression du lot sont :

```powershell
python scripts/test-check-plugin-package.py
python scripts/test-base008-isolation.py
```

Pour la recette client, conserver une nouvelle archive et son inventaire si
le paquet a changé. Rendre inaccessibles le checkout, le vrai dossier
personnel et les caches d'origine ; fournir seulement le plugin, un projet
vide, les pièces fictives et les outils explicitement autorisés. Consigner
version du client, authentification de test, commande d'installation locale,
chemin installé et liste des plugins chargés. Aucun mécanisme d'installation
n'a été essayé ici, donc aucune commande n'est annoncée comme testée.

Rejouer H12 sans profil, puis création volontaire d'un profil minimal et
modification d'une préférence ; observer toutes les lectures/écritures.
Rejouer H11a avec source alternative, puis H11b en empêchant toutes les voies
de recherche **dans la session cible** ; ne pas confondre panne d'une URL et
indisponibilité complète. Exécuter le nominal complété et H02–H16, confronter
chaque sortie aux pièces et aux sources effectivement lues. Recueillir enfin
la reformulation d'un participant réel. Reporter séparément tout échec,
scénario non exécuté ou source non vérifiée avant de statuer sur la clôture.

**Portée :** bilan de maintenance sur données fictives, relecture par le
rédacteur et tests locaux du contrôleur/helper ; aucune exécution de skill
installé, isolation système, relecture juridique indépendante ou mesure
utilisateur. La liste des contrôles impossibles ci-dessus fait foi. Rien
n'est publié, installé sur le compte utilisateur ou étendu à un autre domaine.
