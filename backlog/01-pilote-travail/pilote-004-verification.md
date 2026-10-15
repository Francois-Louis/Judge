# PILOTE-004 — préférences candidat : implémentation et contrôles

15 octobre 2026, Europe/Paris. **Implémentation réalisée, story `a-verifier`.**
Les contrôles du helper sur données fictives passent ; le comportement d'un
modèle dans un client isolé et la compréhension par un lecteur réel restent
à observer. Aucune nouvelle règle de droit ni extension de TRAV-016.

## Modification livrée

Les branches candidat de `cold-start-interview` et `customize` chargent le
[contrat commun embarqué](../../employment-legal/references/candidate-preferences.md)
et se terminent explicitement avant les étapes professionnelles. Le modèle
de profil précise cette exception, y compris pour le profil société. Le retour
à `hiring-review` conserve les faits de conversation et respecte le format
demandé ; une demande actuelle prime sur la préférence enregistrée.

- `interview-required`, profil partiel, placeholders ou entretien en pause :
  qualification en conversation, aucune initialisation professionnelle imposée.
- « Pour cette réponse » : préférence de session. « Mémorise » : seul champ
  demandé dans le profil minimal, sans copier le modèle professionnel entier.
- Profil existant : contenu complet relu et remplacement avec empreinte ;
  réponses hors demande et langue préservées. Une préférence candidat absente
  est ajoutée sans réécrire les rubriques US ; celles-ci ne sont pas des règles
  françaises. Une ambiguïté de champ doit être levée avant l'écriture.
- Création exclusive ; refus si le fichier apparaît ou change entre-temps ;
  relecture après succès. Aucun profil société, dossier, registre ou sondage de
  connecteur nécessaire. Aucun accès persistant sans exécuteur Python.

Le helper BASE-008 et la méthode BASE-005 `1.0.0` restent identiques à leurs
sources du dépôt. La version `0.2.0` du lot PILOTE-002 en cours de recette est
conservée ; aucun paquet publié ou installé sur le compte utilisateur.

## Contrôles exécutés

Les [preuves JSON](pilote-004-controles.json) contiennent l'inventaire et les
empreintes du paquet copié hors du dépôt, les appels réels au helper livré,
leurs entrées/sorties, les contenus avant/après et les témoins. Les chemins
temporaires sont ceux de l'exécution, puis supprimés. Le projet et le vrai
dossier personnel ne sont pas rendus inaccessibles au processus : il s'agit
de fixtures jetables, **pas d'une isolation système ou d'un client installé**.

| Contrôle | Résultat observé |
|---|---|
| H12, couche stockage : profil absent | Lecture `interview-required`, contenu nul, un seul accès au profil du fork ; aucune création. Ne prouve pas l'explication de l'offre par un modèle. |
| Création « texte court », puis « tableau » | Seul profil candidat créé, profil société absent ; relectures exactes, seule préférence changée. |
| Profil partiel | Rôle, lieu/date, commentaire de pause et langue française conservés. |
| Ancien profil US du fork | Ajout de la préférence candidat, octets des rubriques précédentes conservés, état des dossiers inchangé. Ne prouve pas que le modèle ignore les règles US. |
| Placeholders professionnels | Valeurs et pause conservées ; seul format modifié. |
| Collision de création / empreinte périmée | Refus sans altération ; après relecture, changement conservant la nouvelle réponse. |
| Témoins et paquet | Profils d'origine, profil société lorsqu'il existe et dossier d'un autre salarié inchangés ; aucune trace d'accès à ces témoins ; aucun fichier du paquet modifié. |
| Suite PILOTE-004 | **7 tests réussis**, opérations de fixture explicitement choisies par le test, sans exécution de skill. |
| Régression BASE-008 | **14 réussis, 2 ignorés sur 16** : `jsonschema` absent et privilège Windows manquant pour le lien symbolique ; liens physiques et jonctions testés. |
| Contrôleur BASE-006 | **11 tests réussis**. |
| Structure du paquet détaché | **Code 2**, aucun `ECHEC`, **53 `A_RELIRE`**, 29 Markdown. Schéma non exécuté lors de ce contrôle ; [reprise](pilote-003-schema-cli.json) du même paquet : `SCHEMA OK`. Les chemins persistants/dynamiques et les références héritées restent à relire ; aucun succès global annoncé. |
| Validateur du skill-creator | Refuse le champ Claude `argument-hint` sur les trois skills concernés. Champ préexistant conservé pour le client cible ; YAML et liens contrôlés par BASE-006, sans prétendre à la validation officielle. |

Pour rejouer les opérations de stockage :

```powershell
python scripts/test-pilote004-preferences.py -v
```

L'option `--evidence <fichier.json>` produit un nouveau relevé des sept tests.
Le relevé conservé ici inclut aussi le contrôle séparé du paquet et la révision
de départ avec l'état de travail non commité. Pour les régressions :

```powershell
python scripts/test-base008-isolation.py
python scripts/test-check-plugin-package.py
```

## Recette encore nécessaire

Les schémas officiels passent en [reprise](pilote-003-schema-cli.json). L'installation, les commandes,
le retour effectif à la revue et l'absence d'appel à des connecteurs n'ont pas
été exécutés dans un client. Aucun lecteur non juriste réel n'a participé.
Les critères d'acceptation restent ouverts pour cette raison, malgré les
contrôles de stockage réussis.

Dans un client jetable authentifié, avec le seul paquet identifié par ses
empreintes et les pièces H12 de PILOTE-002, rendre le checkout, le vrai dossier
personnel et les caches d'origine inaccessibles. Conserver les outils appelés,
ressources lues, sorties et refus pour chaque étape :

1. Sans profil, demander l'explication de l'offre et « texte court pour cette
   réponse ». Attendre une lecture factuelle sans création persistante ; aucune
   promesse de conformité en l'absence de sources nécessaires.
2. Demander « mémorise texte court », puis `customize` : « modifie mon format
   enregistré en tableau ». Comparer intégralement avant/après ; seul le format
   doit changer. Reprendre la revue sans nouvel entretien professionnel.
3. Rejouer avec un profil partiel, des placeholders et un ancien profil US
   **dans le namespace du fork**, ainsi qu'un témoin dans un autre dossier.
   Le changement ne doit ni toucher le témoin ni appliquer les valeurs US.
   Tester aussi une langue déjà renseignée, un profil société absent et présent,
   et `--redo` / `--check-integrations` sans capacité précise demandée.
4. Retirer l'exécuteur Python du client cible : aucune lecture/écriture
   persistante par Read/Write ou un autre shell, aucune sauvegarde annoncée ;
   poursuite en conversation sur les pièces fournies. Ce scénario n'est pas
   couvert par le simple test du helper avec Python disponible.
5. Faire reformuler par un lecteur réel la préférence conservée, son emplacement
   et un point contractuel encore à vérifier. Recueillir les mots du participant
   et corriger si nécessaire, sans substituer une réponse attendue à sa réponse.

Exemple de bilan attendu, **non observé dans le client** : « Le format tableau
est mémorisé dans votre profil de lecture d'embauche, à [chemin retourné]. Vos
autres réponses sont conservées. Pour le contrat, l'annexe de rémunération
variable manque encore ; demandez-la au recruteur avant de conclure sur ce point. »
Le point restant à vérifier doit venir de la pièce réellement fournie.
