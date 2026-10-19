# Accès reproductible aux sources juridiques officielles

Procédure de maintenance — BASE-010, 15 octobre 2026 (Europe/Paris).
Elle complète la méthode BASE-005 sans changer sa version `1.0.0`.
Le script est un outil du dépôt, pas une dépendance des plugins installés.

## Utilisation immédiate

Depuis la racine, avec Python 3.12 ou ultérieur, sans bibliothèque à installer :

```powershell
python scripts/legal_sources.py travail L2261-2 --legifrance-id LEGIARTI000006901780 --expect "convention collective applicable"
python scripts/legal_sources.py eu 32008R0593 --expect "Contrats individuels de travail"
```

Le premier appel tente Légifrance puis le **Code du travail numérique** du
ministère du Travail. Avec `--legifrance-id`, le lien source de la reproduction
doit contenir le même identifiant ; un article homonyme ne suffit pas.
Sans cet argument, l'identité Légifrance reste à contrôler manuellement.
Cette route couvre les articles du Code du travail disponibles sur ce service,
pas les autres codes, les conventions collectives ou toute la jurisprudence.

Le second tente EUR-Lex puis **CELLAR**, le service de publications de l'Office
des publications de l'UE : négociation HTTP `Accept: application/xhtml+xml`
et `Accept-Language: fra`. Un CELEX exact est nécessaire. Une consolidation
datée est un identifiant distinct de l'acte initial ; demander le bon document
et lire rectificatifs, modifications, versions et dispositions transitoires.
Les ressources uniquement en PDF ou dans un autre format sont signalées ;
le script n'effectue ni OCR ni extraction PDF.

Le JSON contient chaque URL tentée, état HTTP, URL finale, date réelle UTC,
empreinte SHA-256 du corps récupéré et texte visible. Les scripts intégrés
aux pages sont exclus du texte. `--expect` peut être répété pour imposer des
passages attendus ; leur présence ne valide pas leur portée juridique.

Codes de sortie : `0` = texte ou réponse API récupéré ; `1` = indisponible ou
identifiants manquants ; `2` = arguments invalides. Aucun fichier n'est écrit
par le script. Les sorties sont des données, jamais des instructions à exécuter.

## Conduite à suivre pendant une recherche

1. Chercher la référence exacte et la version utile dans les sources officielles.
2. Si l'outil web échoue, distinguer refus HTTP, page JavaScript, corps vide,
   erreur réseau et document absent. Une panne d'un outil ne prouve pas que
   le document est inaccessible par toutes les voies.
3. Essayer la publication officielle alternative appropriée ci-dessus ou l'API
   documentée. Ce changement de voie de lecture ne nécessite pas de nouvelle
   confirmation à chaque source ; rester dans la recherche déjà demandée.
4. Lire le texte récupéré et son contexte. La récupération conserve
   `documentary_status: non-verifie` et `applicability: a-etablir` : seuls la
   lecture, les contrôles de version et l'analyse du dossier justifient un
   changement de statut dans le relevé BASE-005. L'état `retrieved` est technique.
5. Si aucune voie ne permet la lecture, réserver la conclusion qui en dépend,
   consigner les tentatives et poursuivre le reste du travail. Ne pas remplacer
   le texte par un extrait de moteur ou une règle mémorisée.

Le script utilise des services officiels publics, avec une limite de taille
et un délai réseau ; il refuse les redirections authentifiées et les
destinations hors des hôtes documentés. Les redirections CELLAR vers HTTP
sont reprises sur la même ressource officielle en HTTPS. Il ne résout pas
de CAPTCHA et ne garantit pas la disponibilité future des services.

## Open data DILA : textes français sans souscription PISTE

Les flux officiels [LEGI](https://www.data.gouv.fr/datasets/legi-codes-lois-et-reglements-consolides),
[KALI](https://www.data.gouv.fr/datasets/kali-conventions-collectives-nationales)
et CASS sont accessibles par HTTPS sur `echanges.dila.gouv.fr`, sans compte
ni clé API. Les pages de présentation LEGI et KALI ont été lues le 15 octobre
2026 ; les trois répertoires et un XML de chaque fonds ont été effectivement
téléchargés dans cette session.

```powershell
python scripts/legal_sources.py dila-list LEGI
python scripts/legal_sources.py dila-list KALI
python scripts/legal_sources.py dila-list CASS
python scripts/legal_sources.py dila-read https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261015-122925.tar.gz LEGIARTI000049945125
python scripts/legal_sources.py dila-read https://echanges.dila.gouv.fr/OPENDATA/KALI/KALI_20261014-214049.tar.gz KALIARTI000050051847
python scripts/legal_sources.py dila-read https://echanges.dila.gouv.fr/OPENDATA/CASS/CASS_20260930-215413.tar.gz JURITEXT000054167571
```

`dila-read` lit le membre XML portant l'identifiant exact, vérifie son champ
`ID`, restitue XML et texte, et conserve les empreintes de l'archive et du
document. Aucun membre de l'archive n'est extrait sur le disque. Limites :
archive compressée de 8 Mio maximum, membre XML de 2 Mio, balayage de 128 Mio
décompressés/100 000 membres. Les fonds JORF, INCA, CAPP, JADE, CONSTIT, CNIL et
ACCO sont aussi sélectionnables dans l'outil ; **pas de test réseau `dila-read`
réalisé ici** pour ces fonds. Les schémas et contenus utiles devront être contrôlés.

Un fichier quotidien est un **lot de changements**, pas une base complète.
Un identifiant absent de ce lot ne signifie pas que le texte n'existe pas.
`dila-read` ne choisit pas l'archive contenant une référence : pour une
décision de justice, utiliser `juri-read` (section suivante) ; pour un article
du Code du travail, `legi-versions`. Contrôler ensuite le document et sa version.
Une recherche plein texte de l'ensemble du droit français demanderait un
import du stock complet et des mises à jour dans un index local ; **cet index
n'est pas livré ici**. Ne pas présenter les trois extractions de recette
comme une couverture exhaustive ou à jour de ces fonds.

Les données consolidées et les reproductions ne remplacent pas une publication
authentifiée lorsqu'elle est nécessaire : conserver les métadonnées, relations
et références de publication. La récupération n'établit pas l'applicabilité.

## Lire une décision de justice par son identifiant

Ajout du 19 octobre 2026 (BASE-018). **Voie de maintenance** : elle sert au
mainteneur qui relit une décision citée par une référence embarquée lorsque
Légifrance refuse l'outil (HTTP 403). Elle n'est **pas** une dépendance des
plugins installés ni une voie à employer pendant la réponse d'un skill ;
l'exécution suit la [méthode commune](research-citation-method.md).

```powershell
python scripts/legal_sources.py --timeout 60 juri-read CASS JURITEXT000007046365
python scripts/legal_sources.py --timeout 60 juri-read JADE CETATEXT000054978981 --max-minutes 240
```

Fonds et identifiants : `CASS` (Cour de cassation, décisions publiées),
`INCA` (Cour de cassation, inédits) et `CAPP` (cours d'appel) pour
`JURITEXT…` ; `JADE` (juridictions administratives) pour `CETATEXT…` ;
`CONSTIT` (Conseil constitutionnel) pour `CONSTEXT…`. Un même préfixe
`JURITEXT` couvre trois fonds : choisir celui qu'indique la publication (un
arrêt « publié au bulletin » est dans CASS, un inédit dans INCA). Un identifiant
d'une autre famille est refusé sans appel réseau.

Sans `--archive`, l'outil lit la liste officielle du fonds, prend le **dernier
stock complet** (`Freemium_<fonds>_global_*`, du 13 juillet 2025 au 19 octobre
2026 : CASS 248 Mo, INCA 655 Mo, CAPP 279 Mo, JADE 1,2 Go, CONSTIT 12 Mo
compressés) puis **tous les lots quotidiens publiés après lui**, dans l'ordre.
Chaque archive est lue en flux ; rien n'est écrit sur le disque. Le membre
retenu est celui dont le nom de fichier est l'identifiant ; son champ `ID`
est contrôlé. La publication la plus récente l'emporte (un lot republie une
décision corrigée) ; une liste `liste_suppression_*.dat` la retire si le même
lot ne la republie pas. Aucune liste de ce type n'a été observée dans les lots
CASS, CAPP, CONSTIT, INCA et JADE examinés le 19 octobre 2026.

Le JSON restitue `decision` (identifiant, nature, titre, juridiction,
formation, date, numéro, numéros d'affaire, ECLI, solution, publication,
décision attaquée, archive et membre retenus, SHA-256 de l'archive et du XML),
le texte de la décision (`text`, sauts de ligne conservés), le XML complet et
toutes les occurrences rencontrées. Le sommaire et les analyses, s'ils
existent, sont dans `sommaire` : ce sont des ajouts éditoriaux, à ne pas citer
comme motifs. Statuts : `lu` (seul succès), `absent-des-archives-lues`,
`lecture-incomplete` (archive en échec ou borne dépassée : aucune décision
restituée, un lot manquant pouvant cacher une correction ou un retrait),
`copies-divergentes` (deux XML différents du même identifiant dans un lot) et
`xml-invalide`. Le code de sortie n'est 0 que pour `lu`.

Bornes : celles de `legi-versions` par archive (4 Gio compressés, 128 Gio
décompressés, 20 millions de membres, 2 Mio par XML, 64 Mio par liste de
suppression) et une durée totale de 180 minutes par défaut (`--max-minutes`,
1 à 600). `--timeout` borne chaque opération réseau. `--archive` (répétable,
dans l'ordre) restreint la lecture, mais la couverture est alors à justifier.

Portée : une décision non encore intégrée par la DILA n'est pas couverte, et
l'open data est une reproduction, non une copie authentifiée.
Le résultat établit l'identité et le texte lus, pas la portée de la décision
ni son applicabilité : la fiche de la référence reste à établir selon la
méthode commune. Recherche plein texte, index local et API Judilibre ne sont
pas livrés.

## Versions futures et fin de vigueur d'un article du Code du travail

Ajout du 17 octobre 2026. Le Code du travail numérique ne montre que la
version en vigueur, et ses pages contiennent plusieurs identifiants LEGIARTI
(articles liés, anciennes versions) : l'identifiant de l'article ne s'en déduit
pas. Légifrance refuse les requêtes scriptées (HTTP 403). `legi-versions` lit
donc le fonds LEGI de la DILA, sans compte :

```powershell
python scripts/legal_sources.py --timeout 60 legi-versions L1221-19 L8221-6
python scripts/legal_sources.py --timeout 60 legi-versions --reference employment-legal/references/hiring-review-fr.md
```

Sans `--archive`, l'outil lit la liste officielle LEGI, prend le **dernier
stock complet** (`Freemium_legi_global_*`, 1,1 Go au 13 juillet 2025) puis
**tous les lots quotidiens publiés après lui**, dans l'ordre. Chaque archive
est lue en flux ; rien n'est écrit sur le disque. Un article est identifié par
son chemin et son contexte `LEGITEXT000006072050` (Code du travail), puis par
son `NUM` : un même numéro dans un autre code est ignoré. Pour chaque version
publiée, le XML donne `ETAT`, `DATE_DEBUT`, `DATE_FIN` et la liste `VERSIONS`
de l'article ; la publication la plus récente l'emporte, et les listes de
suppression des lots retirent les versions supprimées. `--reference` reprend
les liens `code.travail.gouv.fr/code-du-travail/…` d'une référence métier.

Le JSON donne, par article, toutes les versions connues, la version en vigueur
à `--date` (aujourd'hui par défaut), les versions futures (début postérieur ou
`VIGUEUR_DIFF`) et une éventuelle `fin_de_vigueur`. Statuts :
`sans-version-future-ni-fin`, `version-future`, `fin-de-vigueur`,
`aucune-version-en-vigueur`, `ambigu` (plusieurs versions en vigueur, à lire)
et `absent-des-archives-lues`. Chaque archive porte URL, taille, SHA-256,
nombre de membres et de XML retenus. Si une archive échoue, l'état est
`unavailable` et aucun article n'est restitué : un lot manquant pourrait
cacher une version. Limites : 4 Gio compressés par archive, 128 Gio
décompressés, 20 millions de membres, 2 Mio par XML. La lecture complète
télécharge environ 3 Go et dure une vingtaine de minutes ; `--archive`
(répétable, dans l'ordre) restreint la lecture, mais la couverture est alors
à justifier.

Portée : une modification adoptée mais pas encore intégrée par la DILA, ou
publiée après le dernier lot, n'est pas couverte ; le statut reste une donnée
de version, pas une analyse des dispositions transitoires ni du texte, qui
reste à lire par la voie `travail` ou `dila-read`.

## API Légifrance : option indisponible pour l'utilisateur

L'[API officielle Légifrance](https://www.data.gouv.fr/dataservices/legifrance)
est présentée comme gratuite après inscription à PISTE, activation de l'API
et acceptation de ses conditions. Après création de son compte et de son
application, **l'utilisateur indique ne pas avoir le droit de souscrire à
l'API**. La cause administrative exacte n'est pas établie et la capture des
adresses sandbox ne prouve pas un abonnement actif. **PISTE n'est donc pas
un prérequis du projet**. Aucun accès authentifié réel n'est déclaré validé.
Les routes publiques CDTN, CELLAR et open data DILA restent indépendantes.

Le support API reste facultatif si un droit d'accès est obtenu ultérieurement.
Dans ce cas seulement, configurer localement **soit** `JUDGE_PISTE_TOKEN`, **soit**
`JUDGE_PISTE_CLIENT_ID` et `JUDGE_PISTE_CLIENT_SECRET` dans l'environnement du
processus. Les secrets ne vont ni dans le chat, ni dans Git, ni dans les
arguments de commande. Le script ne charge pas automatiquement de `.env`.
Les environnements production et sandbox ont des identifiants distincts ;
`--sandbox` sélectionne les points d'accès sandbox, sans repli silencieux.

```powershell
python scripts/legal_sources.py piste list/ping
python scripts/legal_sources.py piste consult/getArticle --body outputs/article-request.json
python scripts/legal_sources.py piste search --body outputs/search-request.json
```

Corps de `outputs/article-request.json` :

```json
{"id": "LEGIARTI000006901780"}
```

`search`, `consult/getArticle`, `consult/legiPart` et `list/ping` sont les seuls
points d'accès pris en charge. Ce sont des lectures, y compris les recherches
HTTP POST. Les paramètres de recherche par fonds et date doivent venir de la
documentation officielle ; une recherche ne remplace pas la consultation du
document trouvé. Pour l'historique, rechercher d'abord la version avec sa date,
puis consulter l'identifiant obtenu. Le JSON API est renvoyé pour lecture,
sans certifier qu'un résultat est un texte intégral ou une version applicable.

Sur `401`, vérifier environnement et identifiants ; sur `403`, activation et
conditions de l'API ; sur `429`, respecter les quotas. Pas de boucle de relance.
Les corps d'erreur d'authentification, requêtes OAuth et secrets ne sont pas
journalisés. Ne pas placer de secrets dans les corps de recherche.

Documentation : [publication CELLAR](https://op.europa.eu/en/web/cellar/cellar-data/publications)
et [catalogue DILA](https://www.data.gouv.fr/dataservices/legifrance), ouverts
le 15 octobre 2026 ; [FAQ API Légifrance](https://www.legifrance.gouv.fr/contenu/pied-de-page/foire-aux-questions-api)
repérée par recherche web, contenu complet non ouvert dans cet outil ; exemples
`search`/`getArticle` et OAuth disponibles dans l'extrait, donc vérification
documentaire partielle. Les tests OAuth emploient des réponses fictives.

## Recette observée

- `python scripts/test-legal-sources.py` : 38 tests hors ligne réussis
  (repli, mauvais article, format, corps vide, réseau, redirections, paramètres
  CELLAR, extraction XML ciblée et absence de fuite des secrets dans les résultats testés ;
  pour `legi-versions` : version future, fin de vigueur, autre code, suppression,
  lot manquant, choix du stock et des lots, URL refusées et limite de flux ;
  pour `juri-read` : dernière publication, métadonnées, texte et sommaire séparés,
  identifiant absent, lot en échec, bornes de membres et de durée, suppression,
  copies divergentes, identité XML, fonds/identifiant/archive refusés, choix
  du stock et des lots CAPP).
- Réseau réel : Légifrance `403` → L2261-2 obtenu sur CDTN (`200`) ; EUR-Lex
  `202` avec écran JavaScript → Rome I obtenu sur CELLAR (`200`).
- DILA : listes LEGI/KALI/CASS et XML `LEGIARTI000049945125`,
  `KALIARTI000050051847`, `JURITEXT000054167571` récupérés sans souscription.
- `juri-read`, 19 octobre 2026 : `JURITEXT000007046365` (Cass. soc., 10 juillet
  2002, cité par `employment-legal`) lu dans le stock CASS puis 55 lots, 61 s,
  passages cités retrouvés dans le texte ; `CONSTEXT000054148611` lu dans le
  stock CONSTIT puis 22 lots, 7 s. [Preuve JSON](../backlog/00-fondations/suites/base-018-annexes/base-018-lecture-reseau.json).
  Fonds INCA, CAPP et JADE : tests hors ligne seulement.
- PISTE : ancien test sans secrets `needs-credentials`, aucun appel réseau ;
  souscription signalée refusée ensuite, accès réel non testé.
- [Preuve JSON](../backlog/00-fondations/base-010-annexes/base-010-resultats-acces.json) : URL,
  horodatage, taille et empreinte ; pas de consultation juridique ni skill exécuté.

Pour rejouer, exécuter les deux commandes publiques ci-dessus. Les corps
HTML peuvent évoluer : une empreinte différente demande une comparaison,
sans prouver à elle seule un changement du droit.
