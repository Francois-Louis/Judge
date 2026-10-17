# CONSO-001 — Bilan de l'implémentation

17 octobre 2026 (Europe/Paris). Statut : `a-verifier`.

Le paquet `consumer-legal` `0.1.0` fournit un seul skill,
`non-delivery-claim`, pour préparer une réclamation au vendeur d'un bien
commandé à distance et non reçu. La sélection par l'utilisateur comprend
son inscription au marketplace. Le compte réel passe à 13 paquets/136 skills
avec BNK-001 en parallèle, plutôt que le compte anticipé dans l'ancien cadrage.

## Résultats séparés par couche BASE-006

| Couche | Résultat observé | Preuve et limite |
|---|---|---|
| Structure du paquet détaché | Aucun défaut bloquant ; contrôle statique `INCOMPLET`, trois `A_RELIRE`. | [Résultats techniques](resultats-paquet.json), inventaire SHA-256 des 13 fichiers ; vérificateur copié hors checkout. Les trois points de relecture sont détaillés ci-dessous. |
| Copies communes et licence | Réussi pour les six copies intégrales, dont BASE-005 `1.2.0`. | Empreintes source et embarquées identiques ; README, skill, références métier, helper, modèles et licence présents. |
| Schéma officiel | Réussi pour le paquet et le marketplace. | Claude Code `2.1.299`, binaire de l'application désigné par `--claude`. Avertissement attendu : le modèle CLAUDE.md racine n'est pas un contexte chargé. |
| Installation locale | Réussie dans la configuration jetable ; liste contenant uniquement ce plugin installé. | Commandes marketplace add/install/list conservées ; artefact local indiqué par le client, version `0.1.0`. Installation sans compte, sans invocation du skill. |
| Invocation et scénarios métier | **Non exécutés**, N01 à N13. | `auth status` : `loggedIn: false`, méthode `none`. Aucun identifiant, profil ou connecteur personnel importé. Aucune sortie de modèle simulée présentée comme une exécution. |
| Relecture des sources de maintenance | Passages et limites consignés ; huit lignes de relecture acceptées par le contrôleur BASE-014. | Chapitre livraison et repères civils lus par outil web connecté ; directive via CELLAR ; DGCCRF comme guide ; article liminaire et L221-15 inaccessibles ; L221-3 lu sur page historique. Les conclusions dépendantes restent réservées. |
| Relecture des sorties et raisonnement juridique | **Non exécutée**, faute de sorties du skill. | Les lectures de maintenance ne certifient pas la loi applicable, les versions futures ou les conclusions d'un dossier. |
| Compréhension par un lecteur sans formation juridique | **Non exécutée**. | Aucun participant réel ; les attentes des fixtures ne valent pas reformulation. |

Le vérificateur ne prouve pas l'absence d'accès au checkout dans un client
LLM. Les contrôles utilisent des répertoires, HOME/USERPROFILE, configuration
Claude et TEMP/TMP jetables sous le même compte Windows, sans sandbox système.
L'artefact ne change pas pendant les contrôles ; ce constat ne vaut pas
observation d'un parcours du skill. L'archive de test est supprimée après
inventaire ; ce chantier ne livre pas un lot LIV ni une installation personnelle.

## Relecture manuelle des trois signalements statiques

1. Le modèle commun de société mentionne cold-start-interview. Il est copié
   à l'identique pour BASE-008 ; le skill ne le charge pas, ne demande aucun
   profil et n'annonce pas de commande d'entretien disponible. Aucun skill
   d'entretien ajouté pour satisfaire artificiellement cette mention.
2. Le modèle de dashboard indique un chemin durable dynamique. Il est
   également embarqué sans être chargé par le parcours livré ; aucun
   dashboard ou export automatique n'est proposé.
3. La référence d'isolation décrit la racine durable du fork. Le skill la
   lit comme contrat, mais interdit l'accès au profil et le stockage dans
   cette tâche. Le helper est présent et identique, sans appel prévu.

Ces conclusions reposent sur la lecture des instructions ; leur respect
effectif devra être observé lors de l'invocation. Le contrôle reste
`INCOMPLET`, et n'est pas requalifié artificiellement en succès complet.
Le vérificateur commun a reçu en parallèle de BNK-001 une distinction entre
cette mention connue du modèle partagé et une vraie commande absente dans un
parcours ; son empreinte est conservée dans les résultats.

## Vérifications complémentaires

- `python scripts/test-base008-isolation.py` : [trace conservée](resultats-isolation.json),
  16 tests, 14 réussis et deux
  ignorés avec motif (jsonschema absent pour le test d'orchestration ; privilège
  Windows absent pour le lien symbolique réel). Les jonctions et liens durs
  sont testés. Contrôles hors ligne, aucun LLM exécuté.
- Validation de création du skill : frontmatter et nom acceptés par
  quick_validate.py du skill-creator, après retrait du champ optionnel Claude
  argument-hint non reconnu par ce contrôleur Codex.
- `python scripts/source_reviews.py consumer-legal --depuis 2026-10-17` :
  huit relectures, aucune erreur de forme ; le script ne prouve pas la lecture.
- Les 96 JSON suivis au moment du contrôle sont parseables. Les JSON de la
  présente annexe sont aussi relus lors de la revue finale.
- Contrôle des versions et diff exécuté avant commit ; les premiers fichiers
  du paquet ont été intégrés à un commit concurrent BASE-017 pendant le
  chantier. L'historique existant est conservé, les compléments CONSO-001 sont
  identifiés dans leur propre commit.

## Périmètre de la relecture des instructions

Qualification avant brouillon ; un fait par provenance/statut ; chronologie
des engagements et réceptions ; preuve de remise distincte du suivi ; délais,
résolution et remboursement séparés ; N03 sans brouillon consommateur ;
N04/N05 sans responsabilité ou faux affirmé ; N06 sans séquence automatique ;
N07 sans confusion entre option du panier et transporteur extérieur ; CONSO-019
et autres suites signalées comme proposées. Sans source utile lue, brouillon
factuel sans article, délai légal ou droit au remboursement affirmé.

USAGE-001 `1.0.0` est repris localement : entrée sans profil, une question
à la fois sans pièce, pièces limitées au besoin, engagements des deux parties,
prochaine action et destinataire. BASE-013 et BASE-016 sont portés par la méthode
`1.2.0` et le skill : phrase finale avec juriste d'association ou avocat,
renfort initial selon le contexte, aucune jurisprudence de mémoire. Cette
relecture documentaire ne coche pas les critères comportementaux de la story.

Pour terminer la recette : installer seul le paquet dans un environnement
authentifié de test autorisé, invoquer la commande sur les [fixtures](pieces-fictives.md),
conserver traces/sorties/erreurs, puis relire les conclusions et faire
reformuler par un lecteur réel. Aucun succès N01–N13 n'est revendiqué ici.
