# LIV-001 — Vérification du lot 001

Contrôles du **16 octobre 2026** sur l'artefact `judge-fr-eu-lot-001.zip`,
construit par [`scripts/build-lot.py`](../../../scripts/build-lot.py) et vérifié
par [le vérificateur du lot](liv-001-verifier-lot.py). Le [relevé machine](liv-001-resultats.json)
conserve commandes, sorties et empreintes.

## Choix du lot

| Candidat | Stories | Décision |
|---|---|---|
| `employment-legal` 0.2.1, `hiring-review` et parcours candidat | PILOTE-002, PILOTE-003, PILOTE-004 `terminee` ; recette client BASE-011 | **Livré** |
| `commercial-legal` 0.2.0, `review` (COM-001) | COM-001 `a-verifier` | Exclu : recette client et lecteur non exécutés |
| Dix autres plugins 0.1.0 | Isolation technique BASE-008 seulement | Exclus : aucune tâche juridique adaptée |
| CoCounsel, cookbooks | Contenu éditeur ; déploiements non recettés | Exclus |

Le plugin livré contient aussi ses 19 autres skills et l'agent hérités, non
adaptés : c'est le paquet recetté par BASE-011. Les notes de version et le
README du plugin les signalent comme tels.

## Identité et coexistence (BASE-004)

| Point | Observation pour ce lot |
|---|---|
| Noms | Marketplace `judge-fr-eu`, plugin `judge-fr-eu-employment-legal`, commandes qualifiées distinctes de l'original (BASE-011, scénarios B8). |
| Données | Racine `~/.claude/plugins/config/judge-fr-eu/employment-legal/` ; aucun chemin actif de l'origine dans le paquet (motif présent 8 fois dans la version amont de `hiring-review`, 0 dans le lot). |
| Installation | Configuration jetable : seul `judge-fr-eu` connu, source dossier local ; aucune récupération depuis GitHub ; aucun profil créé. |
| Mises à jour | Désactivées par environnement pendant le test ; l'utilisateur doit vérifier le réglage du marketplace (notes de version). |
| Limite BASE-008 | Critère 4 toujours ouvert. Le cycle du hub ne concerne pas ce lot. Le refus réel des liens symboliques par l'assistant de stockage n'est pas testé : création impossible sur ce poste (WinError 1314), test ignoré à nouveau. Jonctions et liens physiques refusés. |

## Métadonnées alignées

Version 0.2.1 : manifeste, entrée du marketplace, README et NOTICE du plugin
indiquent la recette client faite sur fixtures, le lecteur non indépendant et
le nominal H01 non exécuté. Les 34 autres fichiers du paquet sont identiques,
empreinte par empreinte, au paquet recetté par BASE-011 (révision `1265c5a`).
README et NOTICE racine, test BASE-008 (version attendue) mis à jour.

## Contrôles exécutés

| Contrôle | Résultat |
|---|---|
| Suites existantes avant modification | BASE-008 : 14 réussis, 2 ignorés (lien symbolique, orchestrateur) ; contrôleur BASE-006 : 13 réussis. |
| Construction | 42 fichiers ; sortie dans le checkout refusée ; source : arbre de travail à `e31ea94` plus 5 fichiers modifiés listés dans l'inventaire. |
| Archive et inventaire | Archive extraite dans un dossier neuf, identique à l'inventaire SHA-256. |
| Périmètre | Marketplace du lot à une entrée ; nom, description et auteur identiques au manifeste ; aucun autre plugin. |
| Contrôleur BASE-006 sur le paquet extrait | `SCHEMA OK` (CLI 2.1.299 embarquée) ; `STRUCTURE INCOMPLET` : état connu de relecture manuelle, sans erreur. |
| `claude plugin validate` | Marketplace du lot : réussi. Plugin : réussi avec l'avertissement attendu sur `CLAUDE.md`. |
| Installation jetable | `marketplace add`, `plugin install`, `plugin list` réussis ; version 0.2.1 activée ; copie installée identique au paquet extrait. |
| Suites après modification | Voir le bilan de la story. |

Empreinte de l'archive vérifiée : `9cadc4a11a5e0d1e43540f231ea5a3bd015e7e9485f6a34acf029465f6ee96e6`.
Elle change si le lot est reconstruit depuis un commit (voir ci-dessous).

## Reste à exécuter

**Invocation dans une session authentifiée.** Aucune commande du skill n'a
été invoquée sur l'artefact 0.2.1 : la connexion d'une configuration jetable
demande l'utilisateur. BASE-011 a exécuté H02 à H16 sur des fichiers de skill
identiques. Pour clore, dans une configuration jetable où l'utilisateur se
connecte lui-même :

```text
claude plugin marketplace add <dossier-extrait>\judge-fr-eu-lot-001
claude plugin install judge-fr-eu-employment-legal@judge-fr-eu --scope user
claude
> /judge-fr-eu-employment-legal:hiring-review
  (coller la pièce fictive H02 de PILOTE-002)
```

Consigner version du client, plugins chargés, ressources lues et sortie.

## Commandes de publication préparées — non exécutées

À n'exécuter qu'après décision de l'utilisateur. Toutes ciblent le fork
`Francois-Louis/Judge` ; aucune ne crée de PR. `gh` peut choisir par défaut le
dépôt parent d'un fork : `--repo` est donc toujours explicite.

```text
git remote -v                       # attendu : origin = git@github.com:Francois-Louis/Judge.git, aucun upstream
git add <fichiers du lot> && git commit
python scripts/build-lot.py --rev HEAD --lot judge-fr-eu-lot-001 --plugin employment-legal \
    --notes backlog/04-livraison/liv-001-annexes/liv-001-notes-version.md --out <dossier-hors-checkout>
python -X utf8 backlog/04-livraison/liv-001-annexes/liv-001-verifier-lot.py --zip <...>/judge-fr-eu-lot-001.zip \
    --work <dossier-neuf> --claude <claude.exe>
git tag -a judge-fr-eu-lot-001 HEAD -m "Judge FR/UE lot 001: employment-legal 0.2.1"
git push origin <branche> judge-fr-eu-lot-001
gh release create judge-fr-eu-lot-001 <...>/judge-fr-eu-lot-001.zip --repo Francois-Louis/Judge \
    --verify-tag --title "Judge FR/UE lot 001" --notes-file backlog/04-livraison/liv-001-annexes/liv-001-notes-version.md
```

Publier l'empreinte SHA-256 de l'archive avec la release. Ne pas utiliser
`gh pr create`, `gh repo sync` ni de remote vers l'origine.

## Portée

Contrôles techniques sur l'artefact dans une configuration client jetable,
sur le même compte Windows (checkout et profil réel lisibles, non lus). Aucune
session de modèle, aucun scénario exécuté sur 0.2.1, aucun lecteur
indépendant, aucune relecture juridique. Aucun commit, tag, push, release ni
changement distant.
