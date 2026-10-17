# BNK-001 — Implémentation et vérification

> Ce bilan initial est conservé comme historique. La [reprise du 17 octobre](#reprise-des-tests-client--17-octobre-2026) ci-dessous donne le dernier état.

17 octobre 2026 (Europe/Paris). Paquet final banking-legal `0.1.1`, un seul
skill payment-dispute. Rédacteur et relecteur non indépendants. Aucun dossier
réel utilisé. L'implémentation est livrée ; la recette complète reste ouverte.

## Décisions et dépendances

La demande sélectionne BNK-001 et sa création de paquet. L'entrée marketplace
est ajoutée sans tri global ; auteur des nouveaux fichiers : Judge FR/UE
maintainers, licence Apache-2.0, attribution Anthropic pour les ressources
dérivées. Les copies BASE-008 et méthode sont identiques aux sources du dépôt.
La méthode actuelle BASE-005 `1.2.0` remplace la `1.0.0` du cadrage historique.
Le paquet est sans profil, agent, hook, connecteur ou stockage durable.

Pendant la tâche, le commit concurrent bee80d1 a enregistré et poussé la
première version BNK-001 et un autre nouveau paquet consumer-legal. L'historique
est conservé ; le commit final porte les corrections et preuves BNK-001. Les
tests globaux sont ajustés à l'inventaire effectivement publié : 13 paquets,
136 skills, dont 134 hérités. Aucun fichier métier consumer-legal n'est modifié
par cette tâche.

Ressources chargées par le parcours : isolation, méthode locale, qualification,
paiements, modèle de courrier conditionnel. Les pièces de la personne sont
des entrées explicites. Les sources officielles sont un accès externe optionnel
pour avancer sur les faits, nécessaire pour vérifier une règle. Les codes BNK
et DOM sont des orientations, pas des dépendances ni commandes installées.
Le helper et les deux modèles communs sont embarqués mais inactifs.

## Couches BASE-006

| Couche | Résultat et preuve | Limite |
|---|---|---|
| Structure détachée | Aucun défaut bloquant ; trois `A_RELIRE`, détaillés ci-dessous. Paquet copié hors checkout ; vérificateur copié séparément. Empreintes des ressources comparées. | Verdict script `INCOMPLET`, pas un feu vert automatique. |
| Schéma officiel | Réussi sur paquet détaché et marketplace ; CLI Claude Code `2.1.301`, binaire de l'extension VS Code trouvé hors PATH. | Avertissement attendu sur CLAUDE.md modèle ; cela ne prouve pas l'installation. |
| Contrôles automatisés | Suite BASE-008 : 16 tests, 14 réussis, 2 ignorés explicitement ; vérificateur : 14 tests réussis ; lint des cinq cookbooks et frontmatter du skill réussis. | jsonschema absent pour le test d'audit orchestrateur ; privilège de lien symbolique absent sous Windows. |
| Chargement et exécution client | Version `0.1.0` chargée par `--plugin-dir` depuis la copie détachée ; commande reconnue ; P01/P02/P03/P04/P06 produisent une réponse, sans source web ni profil. Flux, lectures, réponses et erreurs conservés dans executions. | Compte et HOME réels pour l'authentification ; pas de sandbox système ni installation en profil vierge. Trois plugins intégrés au client restent chargés. Version finale non réexécutée. |
| Recette juridique/d'usage | Relecture des cinq sorties contre les fixtures, ci-dessous ; accès aux sources documenté dans la référence paiements. | Sources nationales partiellement inaccessibles, règles réservées ; aucun régime de remboursement certifié. |
| Lecteur réel | Non exécuté. | La relecture du rédacteur ne valide pas la compréhension d'une personne sans formation juridique. |

Les [résultats statiques et empreintes finales](validation.json) conservent
les sorties du vérificateur, du schéma, de BASE-014, du frontmatter et du
contrôle de version, ainsi que l'empreinte de l'archive détachée finale.

Les trois signalements statiques sont relus : chemin dynamique de la frontière
de stockage, chemin dynamique du modèle de tableau de bord et mention de
cold-start-interview dans le modèle commun de profil d'entreprise. Ces modèles
restent inactifs dans ce skill sans profil. La copie identique est conservée.
Le vérificateur transforme uniquement cette dernière mention dans ce fichier
précis en relecture manuelle ; une commande absente dans un skill ou une autre
commande absente dans ce modèle reste une erreur. Un test couvre ces limites.

## Conditions des essais client

[Exécuteur](recette.py), [fixtures](fixtures.json),
[résultats bruts](executions/results.json) et [empreintes du paquet exécuté](executions/package.json).
Client `2.1.301`, modèle effectivement annoncé `claude-opus-5-5`.
Projet temporaire vide, paquet détaché, sources de réglages limitées au projet,
MCP strict (aucun serveur), outils disponibles Read/Glob/Grep/Skill ; Bash,
Write/Edit, Agent/Task et recherche web interdits. Variables héritées CLAUDE,
ANTHROPIC et MCP retirées ; aucune session persistée par l'option client.
Ce dispositif limite les outils du modèle mais ne rend pas le checkout/HOME
inaccessibles au processus. Ne pas l'appeler installation isolée.

Chaque flux jsonl contient init, plugin chargé, outils et sortie. Les cinq
sorties abouties lisent isolation, méthode, qualification et paiements ; P01,
P02, P04 et P06 lisent aussi le modèle. P03 ne le lit pas, cohérent avec
l'orientation commerciale. Aucun outil d'écriture, de shell ou de réseau
n'apparaît. P05 lit les références puis échoue ; P07–P12 échouent sans lecture.
Les erreurs du compte figurent dans la sortie, même quand stderr est vide :
« You've hit your session limit », réinitialisation annoncée à 11h40 Paris.
`subtype: success` ne vaut pas réussite : le code est 1 et `is_error` est vrai.

## Relecture des scénarios

| Cas et trace | Observation réelle | État |
|---|---|---|
| [P01](executions/P01.md), trois paiements inconnus | Opposition/signalement en tête ; branche non autorisée selon le récit ; trois lignes, total arithmétique 261 EUR distinct du dû ; brouillon complet ; sources non revérifiées signalées ; ni délai ni franchise chiffrés. | Sortie observée, critères principaux présents ; droit réservé. |
| [P02](executions/P02.md), faux conseiller | Urgence ; branche ouverte malgré validation ; demande du sens du message sans code ; orientation tromperie annoncée non disponible ; brouillon factuel. Mais affirme « c'est à la banque d'en apporter la preuve » sans source relue. | Défaut observé ; instruction corrigée en `0.1.1`, non réexécutée. |
| [P03](executions/P03.md), non-livraison | Oriente vers le vendeur ; chargeback contractuel sans promesse ; aucune opposition. Mais « ce n'est pas un paiement frauduleux » pourrait laisser croire qu'une escroquerie du vendeur est exclue. | Défaut de formulation corrigé en `0.1.1` ; non réexécuté. |
| [P04](executions/P04.md), code/refus/plainte/négligence | Branche ouverte ; demandes séparées de preuve du consentement, traitement technique, faute alléguée, fondement de la plainte et motif écrit ; aucune conclusion sur la négligence. | Sortie observée, critère principal présent, sans validation du fond juridique. |
| [P05](executions/P05.md), enquête | Références lues mais aucune réponse métier : limite de session. | Non validé ; scénario à rejouer. |
| [P06](executions/P06.md), débit après opposition/frais | Distingue autorisation et comptabilisation ; heures et justificatifs attribués sans prétendre les avoir vus ; frais 12 + 3 EUR séparés, remise en état conditionnelle ; pas de remboursement garanti. | Sortie observée, critère principal présent, droit réservé. |
| [P07](executions/P07.md), hors EEE | Limite de session, pas de réponse métier. | Non validé ; transfrontalier à rejouer. |
| P08–P12 | Limite de session : professionnel, données manquantes, modèle américain, prélèvement, actif numérique. | Non validés ; uniquement des fixtures et instructions à ce stade. |

Sans source : variante effectivement observée sur les cinq réponses, avec
réserves générales ; défaut de charge de preuve en P02 corrigé sans nouvelle
exécution. Le nominal avec recherche officielle active n'est pas validé.
Les deux corrections finales sont guidées par des sorties observées ; aucun
test de présence de mots ne se substitue à cette relecture.

## Sources et reste à vérifier

L133-23 et la section de champ L133-1 à L133-5 lus sur Légifrance ; informations
Banque de France, ABE et DGCCRF lues ; DSP2 articles 2, 64, 72–74 lus via la
voie Python officielle. L133-18/19/24 : refus web et Python consignés ; catalogue
DILA disponible mais pas de parcours complet du stock/deltas. Le tableau de
paiements distingue ces statuts et réserve les conclusions dépendantes.
Aucune décision lue, aucun contrat de réseau fourni, aucune recherche exhaustive
de versions futures ou de jurisprudence. Le contrôle BASE-014 recense neuf
lignes de relecture, sans transformer un échec d'accès en lecture.

Reste : rejouer les sept cas bloqués et les deux corrections, nominal avec
sources accessibles, installation réellement isolée sans autres plugins,
compréhension par participant réel et vérifications juridiques réservées.
La story reste `a-verifier`, sans certification globale ni lot LIV publié.

## Reprise des tests client — 17 octobre 2026

Sonde P01 en 0.1.1, puis P01–P03 en 0.1.2 intermédiaire. Les réserves de preuve et de téléservice sont améliorées. P03 appelle encore une correction livraison/remboursement et opposition ; formulation finale 0.1.3 non rejouée. P04–P12 sans nouveau résultat.

[Résultats de cette série](executions-reprise-2026-10-17/results.json),
[schéma/structure des copies initiales](executions-reprise-2026-10-17/checks.json),
[empreintes inchangées](executions-reprise-2026-10-17/integrity.json).
Les reprises et corrections conservent leurs propres journaux ;
une réponse finale ne signifie pas que le scénario est validé.

Détail des constats, limites et reprise : [bilan transversal](../../../recette-2026-10-17.md).
La compréhension par un lecteur reste non observée ; l'utilisateur
prend en charge sa relecture. Le blocage courant est le quota client
et les validations comportementales restantes.
