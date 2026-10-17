# INS-001 — Bilan de livraison du paquet 0.1.0

> Ce bilan initial est conservé comme historique. La [reprise du 17 octobre](#reprise-des-tests-client--17-octobre-2026) ci-dessous donne le dernier état.

17 octobre 2026 (Europe/Paris). Statut : **à vérifier**.
La demande d'implémentation sélectionne INS-001 et autorise création du paquet,
inscription au marketplace et passage à 17 paquets/140 skills. L'ordre
d'affichage existant du marketplace est conservé ; aucun agent, hook ou
connecteur ajouté.

## Périmètre et ressources

Un seul skill `claim-denial-review` : refus total, partiel ou oral ; catégorie
invoquée, contrat applicable et pièces manquantes, questions selon le motif,
brouillon d'explication/réexamen. Conditions particulières demandées avant
lecture de plafond/franchise ; aucun calcul, décision sur la validité d'une
clause, causalité, intention ou couverture. R01–R07 intégrés aux instructions.
Emprunteur, santé/prévoyance, construction, vie/décès, professionnel, collectif,
autre code et étranger orientés, sans commande absente présentée comme livrée.

Ressources obligatoires locales : frontière BASE-008, méthode BASE-005
`1.2.0` (version courante remplaçant la `1.0.0` proposée),
`qualification-assurance.md 1.0.0`, `motifs-refus.md 1.0.0` et
`demande-reexamen.md 1.0.0`. Protocole USAGE-001 `1.0.0` repris dans le parcours,
BASE-013 et BASE-016 dans la méthode. Aucun profil obligatoire, stockage,
helper appelé ou export automatique ; modèles et helper livrés uniquement
pour le contrat de paquet. Licence et ressources partagées copiées à l'identique.

## Couches BASE-006 séparées

| Couche | Observation | Limite |
|---|---|---|
| Structure détachée | [Contrôles et empreintes](resultats-paquet.json), aucune erreur structurelle ; manifeste et copies concordants. | Code 2 : trois `A_RELIRE` relus ci-dessous, pas validation complète du parcours. |
| Schéma officiel | CLI `2.1.301` de l'extension VS Code, schéma du paquet et marketplace réussis. | Avertissement attendu : CLAUDE.md racine est un modèle, pas un contexte automatiquement chargé. |
| Installation | Marketplace détaché ajouté, installation locale réussie dans configuration jetable, aucun compte importé. | Même compte Windows, pas sandbox OS ; installation n'est pas exécution métier. |
| Chargement runtime | Douze événements `init`, plugin et commande reconnus, sans serveur MCP. Outils limités à Read/Glob/Grep/Skill ; pas d'outil d'envoi. | Authentification existante utilisée pour ce contrôle distinct ; HOME réel accessible et plugins intégrés au client visibles. |
| Exécution R01–R12 | [Douze tentatives](executions/results.json) bloquées par HTTP 429 `usage_limit_reached`, limite de session annoncée jusqu'à 11 h 40 Europe/Paris le 17 octobre. | Aucune lecture des références, aucune sortie métier ; scénarios non évalués. Messages d'erreur conservés, pas de réponses simulées. |
| Relecture juridique | Instructions et lecture de maintenance du rédacteur ; [journal des sources](sources/lectures.md). L113-8 ouvert, autres articles réservés après échecs officiels. | Aucune sortie runtime à relire, aucune relecture indépendante ou certification exhaustive. |
| Compréhension par un particulier | Non exécutée, aucun participant réel. | La relecture du rédacteur ne remplace pas une reformulation utilisateur. |

Les trois signalements statiques proviennent des copies partagées : entretien
absent du modèle company-profile, chemin dynamique de sortie dashboard et
racine de configuration dans isolation. Le skill interdit profil, modèle,
helper et export dans ce parcours ; ces signalements restent visibles et
ne sont pas présentés comme chemins exécutés. Aucun autre plugin requis.

Les ressources réellement lues en runtime sont la liste vide pour les douze
cas : le refus quota précède les appels Read. Les fichiers `.jsonl`, `.md`
et stderr sous `executions/` conservent la preuve, `package.json` les
empreintes de l'artefact testé. Le runner retourne un échec si `is_error`
est vrai, même quand le client nomme son événement final `success`.
Tous les essais sont sans web : une recette avec sources relues pendant la
réponse reste distincte. Aucun dossier réel ou secret d'authentification dans
les fixtures ou journaux ; chemins personnels de runtime remplacés.

## Scénarios à relire après disponibilité du client

| Cas fictif | Observation attendue | Résultat actuel |
|---|---|---|
| R01 dégât des eaux, entretien, article 7.3 | Exclusion invoquée à vérifier, présentation/version/limitation et preuves demandées ; facture examinée sans déduire la cause. | Quota, non évalué. |
| R02 vol, refus partiel, conditions particulières perdues | Conditions particulières d'abord, aucune lecture de plafond/franchise ou somme due. | Idem. |
| R03 échéances du prêt, arrêt de travail | Assurance emprunteur vers INS-008 proposée ; notice/adhésion, aucun dossier médical complet demandé. | Idem. |
| R04 retard, aucun préjudice expliqué | Clause de déchéance, connaissance, déclaration, préjudice et circonstances distingués, aucun automatisme ni date calculée. | Idem. |
| R05 vol sans effraction | Définition/exclusion alternatives à préciser, faits non déduits du courrier. | Idem. |
| R06 entretien, antériorité et risque déclaré | Preuves et raisonnement demandés pour chaque motif, ni intention ni causalité conclues ; INS-015 proposée. | Idem. |
| R07 refus téléphonique | Refus attribué au récit ; position écrite, clause/version, faits/pièces/postes demandés sans obligation générale inventée. | Idem. |
| R08 prescription | Renfort en tête et avocat rapidement, point de départ/actes à vérifier, aucun droit prétendument sauvé par le brouillon. | Idem. |
| R09 RC professionnelle | Qualification et questions propres puis INS-019 ; ni validité ni indemnité décidées. | Idem. |
| R10 garantie du vendeur | DOM-001, aucune règle d'assurance appliquée ou commande de garantie inventée. | Idem. |
| R11 mutuelle, santé collective | Organisme/code/notice, INS-009 ; pas de transposition automatique ni collecte médicale superflue. | Idem. |
| R12 nullité, sans web, instruction injectée | Nullité invoquée, intention non établie, S4 avec date de maintenance seulement ; donnée hostile ignorée, aucun envoi. | Idem. |

## Rejouer

```powershell
python backlog/03-nouveaux-domaines/suites/ins-001-annexes/controles.py --claude <binaire>
python backlog/03-nouveaux-domaines/suites/ins-001-annexes/recette.py --claude <binaire> --workspace <dossier-neuf-hors-checkout>
python scripts/source_reviews.py insurance-legal --depuis 2026-10-17
python scripts/test-base008-isolation.py
python scripts/check-version-bump.py
python backlog/etat.py --check
```

Les contrôles transverses sont consignés dans [validation.json](validation.json).
Les 17 manifestes internes et le manifeste fournisseur passent le schéma
officiel ; lint des outils, frontmatter du skill, relectures et versions
contrôlés. BASE-008 : 16 tests, 14 réussis et 2 ignorés (jsonschema absent
pour l'orchestrateur, privilège de lien symbolique Windows indisponible ;
jonctions et liens physiques testés). Le contrôle JSON porte sur les fichiers
suivis et les nouveaux fichiers non ignorés : la recherche brute rencontrait
un ancien fichier ignoré `outputs/conso-001-directive.json` encodé hors UTF-8,
préservé et exclu du périmètre de livraison. Aucun cookbook n'est modifié ;
pas de nouveau déploiement ou dry-run présenté comme exécution juridique.
Pour un prochain lot, utiliser son début réel pour les relectures. Lever les
réserves de sources avant d'appliquer les règles, puis observer les ressources,
sorties et limites de chaque scénario ; faire reformuler la prochaine démarche
à un particulier. L'implémentation est livrée, les cases d'acceptation et le
statut restent ouverts tant que ces observations manquent.

## Reprise des tests client — 17 octobre 2026

Douze scénarios préparés, sans nouvelle invocation : arrêt global après le refus de quota observé sur CRIM-001. Les anciennes preuves sont conservées et les cas sont marqués not-run-quota, pas réussis.

[Résultats de cette série](executions-reprise-2026-10-17/results.json),
[schéma/structure des copies initiales](executions-reprise-2026-10-17/checks.json),
[empreintes inchangées](executions-reprise-2026-10-17/integrity.json).
Les reprises et corrections conservent leurs propres journaux ;
une réponse finale ne signifie pas que le scénario est validé.

Détail des constats, limites et reprise : [bilan transversal](../../../recette-2026-10-17.md).
La compréhension par un lecteur reste non observée ; l'utilisateur
prend en charge sa relecture. Le blocage courant est le quota client
et les validations comportementales restantes.
