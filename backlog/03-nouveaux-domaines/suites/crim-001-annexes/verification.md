# CRIM-001 — Bilan de recette du 17 octobre 2026

> Ce bilan initial est conservé comme historique. La [reprise du 17 octobre](#reprise-des-tests-client--17-octobre-2026) ci-dessous donne le dernier état.

Périmètre : `criminal-legal` `0.1.0`, seul skill `summons-reading`, personne
majeure convoquée en France par la police ou la gendarmerie. Statut de la
story : `a-verifier`. Aucun succès comportemental C01–C10 n'est revendiqué.

## Résultats par couche BASE-006

| Couche | Résultat observé | Preuve et limite |
|---|---|---|
| Structure détachée | Aucun défaut statique ; contrôle `INCOMPLET`, trois points à relire | [Trace, inventaire et empreintes](resultats-paquet.json), 9 Markdown ; relecture des trois points ci-dessous. |
| Schéma officiel du paquet | Réussi, code 0 ; avertissement attendu sur le modèle CLAUDE.md | Claude Code `2.1.299`, binaire embarqué trouvé sous AppData/Roaming/Claude/claude-code, hors PATH. Même trace. |
| Schéma marketplace | Réussi, code 0 | Même trace ; manifeste et marketplace concordent sur nom, description et auteur. |
| Installation locale seule | Réussie dans une configuration jetable ; seul criminal-legal listé et activé | Ajout d'un marketplace local limité au paquet, installation, liste : commandes et sorties conservées. Aucune installation personnelle modifiée. |
| Exécution des scénarios | Non exécutée | `auth status` : `loggedIn: false`, `authMethod: none`. Aucune authentification importée ou effectuée. C01–C10 gardent une sortie et des ressources lues absentes, explicitement signalées ; aucune simulation de réponse. |
| Relecture juridique des sorties | Non exécutée | Aucune sortie de skill disponible ; relecture documentaire des instructions et des sources seulement, pas de validation par un professionnel indépendant. |
| Compréhension par une personne sans formation juridique | Non exécutée | Aucun participant réel ; la rédaction accessible et le protocole USAGE-001 ne remplacent pas ce contrôle. |

Le contrôleur [controles.py](controles.py) copie le paquet et le vérificateur
hors du checkout, compare les six copies communes, inventorie les fichiers
et vérifie qu'ils ne changent pas pendant les contrôles. L'archive est jetable,
son empreinte et l'inventaire sont conservés. HOME, USERPROFILE, configuration
Claude et TEMP/TMP sont jetables **sous le même compte Windows** : aucune
sandbox système ne rend le checkout ou le profil réel inaccessibles. Une
installation locale réussie n'établit donc pas l'isolation forte de BASE-006
ni l'exécution du parcours. L'option `--run-fixtures` est demandée dans la
recette conservée ; elle ne lance pas de LLM sans client de test authentifié.

## Trois points de structure relus

1. Le modèle commun de société mentionne cold-start-interview absent. La copie
   est identique pour BASE-008 ; le skill ne la charge pas et interdit profil,
   entretien et helper de stockage. Aucun faux skill ajouté.
2. Le modèle de dashboard décrit un chemin durable dynamique. Il n'est pas
   chargé par le parcours ; aucun export ou dashboard automatique.
3. Le contrat d'isolation décrit la racine durable du fork. Il est lu comme
   frontière, sans accès au profil ni stockage pénal pour cette tâche.

Ces conclusions portent sur les instructions ; leur respect réel reste à
observer. Le résultat statique reste `INCOMPLET`.

## Contrôles complémentaires

- [Tests BASE-008](resultats-isolation.json) : 16 tests, 14 réussis et deux
  ignorés avec motif : jsonschema absent pour l'orchestration, privilège Windows
  absent pour créer un lien symbolique réel. Jonctions et liens durs testés.
  Le test inclut le nouveau paquet et son unique commande, les copies communes,
  les manifestes et le fonctionnement du helper embarqué sur des données
  fictives ; cela ne signifie pas que le skill appelle ce helper.
- Ces tests tournent sur une extraction de `main` à la révision
  `33b27db421251f81b3c1f8fa29f9451450e7a448`, augmentée des seuls changements
  CRIM-001 (14 paquets / 137 skills). ENF-001 et FUN-001 modifient simultanément
  l'espace partagé ; leurs changements non commités sont préservés et exclus
  du périmètre de cette preuve. Leurs validations restent distinctes.
  Une seconde [preuve d'intégration](resultats-integration.json) reprend les
  contrôles après le commit ENF-001, avec 15 paquets / 138 skills ; FUN-001
  reste exclue tant qu'elle n'est pas commitée.
- `python scripts/source_reviews.py criminal-legal --depuis 2026-10-17` :
  sept lignes de relecture, aucune erreur de forme. Cela ne prouve pas la
  lecture ni l'applicabilité ; le relevé de la référence les distingue.
- Les JSON suivis et ceux de CRIM-001 ont été parsés ; `git diff --check` et
  le contrôle de version sont exécutés avant commit. Nouveau paquet : `0.1.0`.
- Les copies de BASE-005 **1.2.0**, BASE-008 et LICENSE sont identiques par
  SHA-256. La version 1.0.0 visée par le cadrage a été remplacée par la version
  commune courante, sans modifier les autres paquets.

## Sources effectivement lues et limites

Le relevé métier embarqué sépare les textes, les fiches et leur applicabilité.
Les [captures UE](sources/32012L0013.json),
[accès à l'avocat](sources/32013L0048.json) et
[interprétation](sources/32010L0064.json) gardent chaque tentative EUR-Lex
(challenge 202), la route CELLAR française réussie, la date et les empreintes.
Le statut technique `non-verifie` émis par l'outil est conservé : la
qualification documentaire des passages lus se trouve dans le relevé métier.
Publication initiale seulement ; consolidation, modifications et transposition
utile au dossier non vérifiées. Aucun effet direct présumé.

Les [tentatives françaises et fiches lues](sources/acces-francais.json)
documentent le refus HTTP 403 sur CPP 61-1 et 78, par web et Python. Les voies
datées et la section liée par Service-Public ont également échoué via le web.
Les deux articles restent réservés : aucun extrait de moteur ni souvenir du
modèle n'est traité comme lecture. Les deux fiches Service-Public ont été
lues le 17 octobre 2026 comme informations générales, jamais comme texte
normatif. Aucun accès PISTE, compte, connecteur ou index LEGI complet requis.

## Relecture des instructions et suite de la recette

Les [fixtures](fixtures.json) portent C01–C04, puis la dégradation sans source,
le mineur, l'audition commencée, les violences avec canal surveillé, la
préfecture et la pièce incomplète avec interprète/protection juridique.
Chaque attente est un critère à relire sur une sortie réelle, pas un oracle
qui fabriquerait la réponse ni un test textuel certifiant le comportement.

Relecture documentaire : qualité inconnue conservée ; authenticité avant
l'exploitation d'un message douteux ; actes de juridiction et mineurs limités
à la fiche et l'avocat ; pas de préparation des déclarations ni d'évitement ;
aucune preuve modifiée ; priorité au canal sûr ; se présenter, répondre et
quitter distincts ; droits réservés faute de statut/source ; phrase finale
avec avocat en droit pénal et renfort initial de procédure selon BASE-005.
USAGE-001 `1.0.0` est repris localement : entrée ordinaire, pièces utiles,
questions progressives, action/destinataire et aucun envoi automatique.

Pour achever la recette, utiliser un client de test authentifié dans un
environnement isolé autorisé, conserver appels, ressources lues, sorties et
erreurs pour C01–C10, relire les conclusions et les textes pertinents, puis
faire reformuler les prochaines démarches à un participant réel. Aucun
nouveau plugin ni profil n'est nécessaire pour accomplir cette tâche.

## Reprise des tests client — 17 octobre 2026

C01–C07 ont produit une sortie. C08 est refusé par le quota ; C09–C10 non lancés. Les formulations sur mineur, accompagnement parental, obligation de présentation et régularité sont précisées dans criminal-legal 0.1.2 ; rejeu final non exécuté.

[Résultats de cette série](executions-reprise-2026-10-17/results.json),
[schéma/structure des copies initiales](executions-reprise-2026-10-17/checks.json),
[empreintes inchangées](executions-reprise-2026-10-17/integrity.json).
Les reprises et corrections conservent leurs propres journaux ;
une réponse finale ne signifie pas que le scénario est validé.

Détail des constats, limites et reprise : [bilan transversal](../../../recette-2026-10-17.md).
La compréhension par un lecteur reste non observée ; l'utilisateur
prend en charge sa relecture. Le blocage courant est le quota client
et les validations comportementales restantes.
