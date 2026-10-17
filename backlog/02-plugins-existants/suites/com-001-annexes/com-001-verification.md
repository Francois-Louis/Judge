# COM-001 — Bilan de l'orientation contractuelle

> Ce bilan initial est conservé comme historique. La [reprise du 17 octobre](#reprise-des-tests-client--17-octobre-2026) ci-dessous donne le dernier état.

16 octobre 2026, Europe/Paris. Story [COM-001](../com-001-orientation-contrat.md),
plugin principal `judge-fr-eu-commercial-legal` **0.2.0**, skill canonique `review`.
État : **implémenté, à vérifier**. Le résultat est borné à l'orientation ; les
branches COM-002 à COM-018 restent proposées/non adaptées selon leur nature.

## Changements livrés

Titres puis substance utile, rôles des deux parties pour l'acte, domaine
principal, achat/vente, pièces et questions décisives. Loi applicable, juge et
préférence de négociation séparés. Construction/B2C, secteur, emploi possible,
contentieux identifié et exécution ont leur frontière propre. Les branches
prestation, NDA, SaaS, avenants, échéance, paiement et rupture annoncent leur état
réel et ne lancent aucun skill hérité non adapté, même avec un profil complet.

L'exception au setup concerne uniquement cette orientation. Profil absent,
placeholders ou helper indisponible ne déclenchent pas d'interview/import ;
les entrées explicites permettent une préparation dans la conversation.
Tout accès durable conserve les contrôles du helper. Aucune donnée utilisateur
dans le paquet, action externe, rappel ou garantie de secret déduite du récit.

## Ressources et portée des accès

| Ressource | Classe / comportement |
|---|---|
| `review`, référence `orientation-commerciale.md` 1.0.0 | Embarquées ; procédure et états des branches. |
| Méthode BASE-005 1.0.0 | Copie locale entière, identique à la source racine ; aucune modification des copies communes. |
| Frontière de stockage et `judge_store.py` | Embarqués, identiques à leurs sources racine ; helper requis pour les seuls accès durables. |
| Modèle `CLAUDE.md` | Embarqué ; exception d'orientation explicite, exemples hérités jamais traités comme réponses. |
| Profil commercial/partagé, dossier | Données utilisateur facultatives, via helper uniquement ; aucune lecture réelle de profil personnel dans ce lot. Aucun dossier requis. |
| Documents/récit | Entrées explicites ; lecture ciblée, couverture et provenance à annoncer. |
| Drive/SharePoint/Box/CLM, DocuSign/Slack | Optionnels ; configuration MCP héritée ne prouve pas connexion. Aucun appel dans cette recette. |
| Publications officielles | Facultatives pour commencer l'orientation factuelle ; nécessaires avant toute conclusion de droit dépendante. Échecs et versions tracés. |
| Autres plugins, cookbook | Simple orientation avec disponibilité réelle ; aucun chargement, installation de domaine complémentaire ou déploiement. |

## Sources effectivement recherchées et lues

- Rome I : [trace brute de récupération](source-rome-i.json).
  EUR-Lex `202`/écran JavaScript, puis CELLAR `200` XHTML français, consolidation
  CELEX `02008R0593-20080724`. Lecture du champ, choix/absence de choix,
  consommation/travail, lois de police et art. 28 rectifié/29. La consolidation
  intègre le repère C1 ; aucun rectificatif séparé n'a été ouvert. Applicabilité
  aux futurs dossiers conditionnelle, exhaustivité des évolutions non certifiée.
- Bruxelles I bis : [trace brute](source-bruxelles-i-bis.json).
  EUR-Lex `202`/écran JavaScript, puis CELLAR `200` XHTML français, CELEX
  `02012R1215-20150226`. Lecture art. 1, 4, 6, 17–19, 25, 66 et 81 : champs et
  date procédurale distincts de la date du contrat. Même réserve de version et
  d'applicabilité. Les annexes graphiques récupérées n'ont pas été analysées.
- Article liminaire du Code de la consommation `LEGIARTI000049464063` et
  L221-3 `LEGIARTI000032226882` : outil web, liens Légifrance directs et datés
  tentés le 16/10/2026 ; erreurs d'accès puis **403** sur les liens sans date.
  **Contenu non lu**, version/applicabilité à établir. Les résultats de moteur
  ne sont pas des consultations. Aucun accès PISTE, abonnement ni extraction
  DILA de ces articles effectué. Les conclusions dépendantes sont réservées,
  notamment définition juridique définitive et protection du petit professionnel.

Les JSON UE restent des traces de transport avec `documentary_status:
non-verifie` : les contrôles de lecture distincts sont décrits dans la
référence livrée, sans réécrire les résultats bruts comme une certification.
La recette ne revendique aucune règle française inaccessible comme vérifiée.

## Résultats par couche BASE-006 1.2.0

| Couche | Résultat réellement observé | Limite |
|---|---|---|
| Structure du paquet détaché | **Incomplet, code 2** ; 22 Markdown, aucun `ECHEC`, 42 `A_RELIRE`. Références locales présentes ; méthode/frontière/helper identiques, inventaire SHA-256 conservé. | Les 42 points concernent surtout chemins de profil, données dynamiques et appels croisés des branches héritées ; pas un succès global du paquet. |
| Schéma officiel du paquet | **Réussi**, Claude Code 2.1.299. Avertissement attendu : le modèle `CLAUDE.md` n'est pas du contexte projet chargé automatiquement. | Le schéma ne prouve ni lecture des références ni qualité de sortie. |
| Schéma marketplace | **Réussi** ; nom, description et auteur commerciaux identiques au manifeste du plugin. | Aucune publication effectuée. |
| Installation locale | **Réussie** dans configuration jetable, marketplace locale contenant seulement le paquet commercial ; `plugin list` annonce 0.2.0 activé depuis sa source détachée. | Variables jetables sous le même compte Windows, pas une isolation OS ; ne pas présenter ce résultat comme recette d'exécution isolée complète. |
| Exécution du skill / ressources réellement chargées par le client | **Non exécutée** : `auth status` annonce `loggedIn: false`. Aucun compte/configuration personnel importé. | Aucun scénario n'est déclaré réussi en client, y compris sans profil/source. |
| Isolation de stockage | Helper détaché : profil absent reste `interview-required`, aucune création/import ; traversée refusée, sentinelle d'origine préservée ; paquet inchangé. BASE-008 : **14 tests réussis, 2 ignorés**, aucun échec au dernier passage. | Ignorés : `jsonschema` absent pour un test d'orchestrateur, privilège Windows insuffisant pour symlink ; jonctions et hardlinks testés. |
| Contrôleur / cohérence | **13 tests du contrôleur réussis** ; lint des cinq cookbooks réussi (aucun cookbook modifié). JSON parseables, diff sans erreur d'espace. | Aucun de ces contrôles n'est juridique. |
| Validation skill-creator | Validateur Codex tenté : refuse `argument-hint`, champ existant du format Claude. | Outil incompatible sur ce champ ; pas de faux succès ni retrait d'un champ valide pour le client cible. Frontmatter couvert par contrôleur du dépôt et schéma cible. |
| Relecture métier et USAGE-001 1.0.0 | [Neuf applications manuelles](sorties-relecture.md) sur [pièces fictives](pieces-fictives.md), ressources de rédaction nommées. | Relecture par le rédacteur, pas exécution du skill ni avis juridique indépendant. |
| Compréhension par une personne sans formation juridique | **Non exécutée**, aucun participant réel. | Faire reformuler la prochaine action, son destinataire, les pièces et la réserve après une sortie réelle. |

Le premier passage BASE-008 avait signalé l'absence de la notation littérale
de chargement de la frontière dans le nouveau skill ; corrigée avant le dernier
passage. Le premier lint a échoué sur l'encodage du terminal Windows ; relancé
avec `PYTHONIOENCODING=utf-8`, réussi. Les résultats finaux ne masquent pas ces
corrections. L'ancienne fixture de version BASE-008 est étendue au commercial
0.2.0 sans relâcher le contrôle des autres versions.

## Rejouer et terminer la recette

Depuis la racine du dépôt (fournir le chemin de sa CLI si elle n'est pas au PATH) :

```powershell
python backlog/02-plugins-existants/suites/com-001-annexes/controles.py --claude <chemin-claude.exe>
python scripts/test-base008-isolation.py
python scripts/test-check-plugin-package.py
```

Le [relevé machine](resultats-paquet.json) donne commandes,
sorties, révision de départ, empreinte de l'archive jetable et empreintes de
tous les fichiers du paquet.
`controles.py` retourne 2 tant que la structure demande relecture ou que le
schéma n'est pas validé ; il ne lance jamais le modèle. L'authentification est
inspectée seulement dans son environnement jetable, puis cet environnement
est supprimé. Les sorties métier conservées sont des relectures, pas les
sorties de ce script.

Pour clôturer, authentifier volontairement un client de test avec les limites
d'isolation explicites, appeler `/judge-fr-eu-commercial-legal:review` sur C01 à
C09, conserver messages/outils/ressources et relire les sorties ; rejouer sans
profil et sans source. Faire reformuler à un lecteur réel. Toute conclusion
dépendant de F1/F2 nécessite la source exacte/version applicable. Pas de
lancement automatique de COM-002 ou d'élargissement à l'issue de ces contrôles.

## Reprise des tests client — 17 octobre 2026

C01–C07, C09 et C08-A/B : dix sorties ; C04 rejoué après une première correction. Les constats sur les règles de mémoire, la dette et le NDA ont conduit à commercial-legal 0.2.4. La formulation finale reste à rejouer.

[Résultats de cette série](executions-reprise-2026-10-17/results.json),
[schéma/structure des copies initiales](executions-reprise-2026-10-17/checks.json),
[empreintes inchangées](executions-reprise-2026-10-17/integrity.json).
Les reprises et corrections conservent leurs propres journaux ;
une réponse finale ne signifie pas que le scénario est validé.

Détail des constats, limites et reprise : [bilan transversal](../../../recette-2026-10-17.md).
La compréhension par un lecteur reste non observée ; l'utilisateur
prend en charge sa relecture. Le blocage courant est le quota client
et les validations comportementales restantes.
