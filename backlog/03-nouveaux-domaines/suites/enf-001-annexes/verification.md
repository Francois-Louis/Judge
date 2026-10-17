# ENF-001 — Implémentation et vérification

> Ce bilan initial est conservé comme historique. La [reprise du 17 octobre](#reprise-des-tests-client--17-octobre-2026) ci-dessous donne le dernier état.

17 octobre 2026 (Europe/Paris). enforcement-legal `0.1.0`, un seul skill
enforcement-act-reading. Aucun dossier réel utilisé. Relecture du rédacteur,
sans revue juridique indépendante ni test avec un lecteur réel.

## Périmètre et décisions

La demande sélectionne ENF-001, son paquet et son intégration au marketplace,
sans tri global des entrées. Auteur des nouveaux contenus : Judge FR/UE
maintainers ; licence Apache-2.0, attribution Anthropic pour les ressources
communes dérivées. La méthode actuelle BASE-005 `1.2.0` remplace la version
`1.0.0` du cadrage. Les six copies communes sont comparées octet pour octet.

Ressources du parcours : isolation, méthode locale, qualification-acte et
lecture-acte avec modèle de fiche. Les pièces de la personne sont des entrées
explicites ; les sources officielles sont un accès externe nécessaire pour
une règle vérifiée, facultatif pour la fiche factuelle. Aucun profil ni
stockage durable. Helper et modèles communs inactifs. Les orientations ENF/DOM
ne sont ni des commandes livrées ni des dépendances d'installation.

Des créations concurrentes criminal-legal et funeral-legal sont apparues après
le début de la tâche. Elles sont préservées et exclues du périmètre ENF-001.
La première suite globale a rencontré l'entrée criminal-legal encore sans
adaptation de son inventaire (15 paquets pour 14 attendus et interview absente).
Le contrôleur prépare donc une copie de maintenance hors checkout avec le
marketplace de HEAD et l'entrée ENF-001 ; la preuve liste exactement les
paquets couverts. Ce contrôle borné ne valide pas les travaux concurrents.

## Couches BASE-006

| Couche | Résultat et preuve | Limite |
|---|---|---|
| Structure du paquet détaché | Aucun défaut bloquant ; trois signalements manuels, conservés dans validation.json. | Verdict statique `INCOMPLET`, pas un feu vert automatique. |
| Schéma officiel | Réussi sur paquet détaché et marketplace borné ; CLI `2.1.301` trouvée dans l'extension VS Code. | Avertissement attendu : CLAUDE.md est un modèle ; conseil non bloquant sur la ligne d'installation du README. |
| Contrôles d'intégration | Six copies identiques, frontmatter valide, BASE-014 (six relevés), lint des cinq cookbooks et contrôle de version réussis ; BASE-008 sur le contenu préparé pour ENF-001 : 16 tests, 14 réussis, 2 ignorés. JSON ajoutés parseables et diff sans erreur d'espacement. | jsonschema absent pour l'audit orchestrateur ; privilège Windows absent pour le lien symbolique. Les autres tests de liens et de jonctions réussissent. |
| Chargement client | Plugin `0.1.0` et commande canonique listés dans l'événement init d'A01. | Chargement par `--plugin-dir`, pas installation en profil vierge ; trois plugins intégrés au client restent chargés. |
| Exécution métier | Bloquée par `usage_limit_reached` / HTTP 429 avant toute lecture du skill ou sortie métier d'A01. | Aucun scénario d'acceptation réussi ; A02–A08 et R01–R05 non exécutés. |
| Relecture juridique et d'usage | Instructions et sources relues par le rédacteur ; grille ci-dessous. | Aucune sortie métier à évaluer, aucun test de compréhension par un participant. |
| Installation réellement isolée | Non exécutée. | HOME et authentification réels restent accessibles au processus ; aucune sandbox système revendiquée. |

Les trois signalements statiques concernent les chemins dynamiques de
stockage et de tableau de bord, et la mention de cold-start-interview dans le
modèle commun d'entreprise. Ce skill ne charge aucun profil ou modèle commun,
ne stocke rien et n'invoque pas cette commande. Les copies identiques sont
conservées ; cette relecture manuelle ne valide pas un parcours de stockage.

## Sources et temporalité

Les passages et statuts exacts se trouvent dans la table Relecture de
lecture-acte.md. Tentatives Légifrance pour CPCE L111-2/L111-3 et versions
actuelles CPC empêchées (403 ou aucun contenu utile). Voies alternatives lues :
fiches DILA F35106/F1780 et pages historiques CPC 653–657 et 514–514-3.
La version historique de 653 indique elle-même une fin au 1er septembre 2025 :
elle ne sert pas de règle actuelle. Les versions 2026 restent réservées.
Aucun accès PISTE, extraction LEGI ou jurisprudence métier prétendument validé.

Annuaire officiel : accueil en timeout, fiche témoin accessible et lue ;
cela ne certifie ni un SMS ni l'identité d'un émetteur fictif. Aucune coordonnée
de cet office n'est proposée comme destinataire de la personne. Les lectures
de maintenance ne sont pas reprises comme consultations futures d'un dossier.

## Fixtures et relecture des instructions

[Fixtures](fixtures.json), [exécuteur client](recette.py),
[résultats](executions/results.json), [flux A01](executions/A01.jsonl),
[message de limite A01](executions/A01.md),
[empreintes du paquet présenté au client](executions/package.json).

Projet temporaire vide, paquet détaché, aucun profil préalable ni serveur MCP,
réglages limités au projet ; outils Read/Glob/Grep/Skill. Outils de mutation,
shell, agents et web interdits ; variables CLAUDE/ANTHROPIC/MCP retirées,
option sans persistance de session. Ces restrictions d'outils ne rendent pas
le checkout ou HOME inaccessibles. Aucun outil de lecture du modèle n'a été
exécuté avant le rejet de quota ; le nom de commande reconnu n'atteste donc
pas la lecture des quatre ressources ou la qualité de la réponse.

| Fixture | Décision demandée dans les instructions, relue statiquement | Exécution |
|---|---|---|
| A01 | Relance probablement amiable, menace rapportée, pas de saisie déduite, titre non mentionné distinct d'inexistant | Bloquée, aucune sortie métier |
| A02 | Dates de l'acte, avis, retrait et découverte distinctes ; aucun délai redémarré ou calculé | Non exécutée |
| A03 | Ventilation/paiement à documenter, ENF-003 et ENF-004 proposées, pas de solde dû calculé | Non exécutée |
| A04 | Canal officiel indépendant avant lien/paiement, identité non vérifiée sans accès | Non exécutée |
| A05 | Qualification par mentions et non en-tête ; absence de titre mentionné n'exclut pas mesure conservatoire | Non exécutée |
| A06 | Appel/exécution provisoire à examiner avec avocat, aucun arrêt garanti | Non exécutée |
| A07 | Page manquante/coquille relevée, pas de nullité annoncée | Non exécutée |
| A08 | Réclamation professionnelle distincte du recours ; urgence et checklist conservées | Non exécutée |
| R01 | Assignation orientée contentieux, pas mesure d'exécution | Non exécutée |
| R02 | Injonction signifiée : urgence et opposition ENF-012 proposée, sans rédaction | Non exécutée |
| R03 | Expulsion et pluralité de dettes, ENF-005/DOM-024 ; refus de soustraire l'argent | Non exécutée |
| R04 | Sans pièce : titre/date d'abord, succession DOM-016 avant dette personnelle | Non exécutée |
| R05 | Acte public, lecture ici, contestation au domaine du fond sans voie civile par défaut | Non exécutée |

Toutes les fixtures sont préparées sans web pour éprouver le mode dégradé,
qui reste à exécuter. La version nominale avec source applicable relue reste
également à recetter. Ne pas transformer cette grille d'attendus en résultats.

## Reprise

Relancer recette.py après disponibilité du client dans un workspace neuf,
conserver lectures, sorties et erreurs des treize cas, puis comparer les
réponses aux critères et corriger si nécessaire. Compléter les versions
officielles utiles, recetter une installation avec HOME/checkout inaccessibles
et faire relire la réponse par une personne sans formation juridique.
L'implémentation est livrée ; la story reste `a-verifier`.

## Reprise des tests client — 17 octobre 2026

Treize scénarios préparés, sans nouvelle invocation : arrêt global après le refus de quota observé sur CRIM-001. Les anciennes preuves sont conservées et les cas sont marqués not-run-quota, pas réussis.

[Résultats de cette série](executions-reprise-2026-10-17/results.json),
[schéma/structure des copies initiales](executions-reprise-2026-10-17/checks.json),
[empreintes inchangées](executions-reprise-2026-10-17/integrity.json).
Les reprises et corrections conservent leurs propres journaux ;
une réponse finale ne signifie pas que le scénario est validé.

Détail des constats, limites et reprise : [bilan transversal](../../../recette-2026-10-17.md).
La compréhension par un lecteur reste non observée ; l'utilisateur
prend en charge sa relecture. Le blocage courant est le quota client
et les validations comportementales restantes.
