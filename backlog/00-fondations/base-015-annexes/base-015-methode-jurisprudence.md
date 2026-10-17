# BASE-015 — Méthode proposée pour les décisions de justice

Texte rédigé pour l'évolution de la méthode BASE-005 (`1.1.0` → `1.2.0`).
Il **n'est pas livré** : [BASE-016](../suites/base-016-methode-decisions-justice.md)
l'intègre à `references/research-citation-method.md` et synchronise les onze
copies. D'ici là, les paquets gardent la version `1.1.0`, dont les sections 3
à 5 s'appliquent déjà aux décisions.

Les voies citées ont été testées le 17 octobre 2026
([inventaire](base-015-inventaire-acces.md)). Elles peuvent changer : un
échec d'une voie n'est pas une preuve d'absence.

## Insertion proposée

Ajouter une **section 10** « Rechercher, lire et citer une décision de
justice », après la section 9, pour ne pas renuméroter la section 8 que
citent le modèle de story et les skills adaptés. Les sections 3 à 5 renvoient
vers elle d'une phrase. Le texte suivant est la proposition.

---

## 10. Rechercher, lire et citer une décision de justice

Une décision n'est citée comme jurisprudence que si elle a été **ouverte et
lue** pendant la réponse, ou si une référence embarquée la porte avec une
relecture datée ; dans ce second cas, la citer avec cette date. Tout le reste
est une piste.

### 10.1 Nature de ce qui a été lu

| Ce qui a été lu | Exemples | Ce qu'il permet |
|---|---|---|
| **Décision lue** | Texte intégral sur Légifrance, sur le site de la juridiction, HUDOC, CELLAR | Fonder la proposition, après lecture des motifs et du dispositif. |
| **Résumé officiel** | Analyse, titrage ou sommaire de Légifrance ; fiche, note explicative ou lettre de chambre de la juridiction ; analyses du Conseil d'État | Orienter et repérer la portée annoncée. La décision reste `partiel` tant que ses motifs ne sont pas lus. |
| **Communiqué** | Communiqué de presse de la juridiction | Signaler une décision et son importance ; même statut que le résumé. |
| **Conclusions ou avis** | Rapporteur public, avocat général, conclusions devant la CJUE | Éclairer le raisonnement ; ne disent pas ce que la juridiction a jugé. |
| **Doctrine** | Article, commentaire, blog d'avocat, éditeur privé, fiche d'un syndicat | Citée comme doctrine (auteur, qualité, date, support). La décision commentée reste `non-verifie`. |
| **Résultat de moteur** | Liste ou synthèse d'une recherche web | Trouver un numéro ou une adresse. Jamais une lecture. |
| **Mémoire du modèle** | Référence ou solution rappelée sans document | Rien. Ne pas l'énoncer comme une solution jugée. |

Une référence rappelée de mémoire peut seulement guider une recherche. Si elle
est montrée à la personne, elle porte « de mémoire, non vérifiée, peut être
inexacte » et ne s'accompagne d'aucune formule du type « la Cour a jugé ». Ne
jamais compléter de mémoire un numéro, une date, un ECLI ou une citation.

### 10.2 Fiche d'une décision

| Champ | Contenu |
|---|---|
| Juridiction et formation | Par exemple « Cour de cassation, chambre sociale », « Conseil d'État, juge des référés ». |
| Date | Date de la décision (prononcé ou lecture), pas celle de la publication. |
| Numéro | Pourvoi, requête, affaire ou numéro de rôle, tel qu'affiché. |
| ECLI | S'il est affiché dans la source ; ne jamais le construire. Sinon « ECLI non affiché ». |
| Publication | Bulletin, Lebon ou tables, inédit, ou mention absente. |
| Accès | Adresse effectivement ouverte, voie (outil), date réelle de consultation, langue. |
| Passages lus | Numéros de paragraphes ou considérants des motifs utiles et dispositif ; extrait littéral court. |
| Statut | `verifie`, `partiel`, `inaccessible` ou `non-verifie` (section 4), pour ce passage et cette question. |
| Portée et applicabilité | Faits comparables ou non, solution de principe ou d'espèce, texte interprété et sa version, évolutions connues ou non recherchées. |

### 10.3 Lire les motifs

1. Identifier la décision dans la page même : juridiction, date, numéro. Un
   titre de résultat de recherche ne suffit pas.
2. Lire, dans cet ordre utile : faits et procédure nécessaires, question
   posée, **réponse de la juridiction** (motifs) et **dispositif**. Ne pas
   attribuer à la juridiction un argument du moyen, de l'arrêt attaqué, des
   conclusions ou d'une partie.
3. Distinguer la règle énoncée, son application aux faits et la solution
   d'espèce. Une cassation sur un manque de base légale ou un rejet fondé sur
   le pouvoir souverain des juges du fond ne pose pas la même règle qu'un
   attendu de principe.
4. Pour une page longue, poursuivre la lecture jusqu'au dispositif (lecture
   par tranches). Un dispositif non atteint laisse la décision `partiel`.
5. Avec un outil qui résume la page, demander la restitution littérale des
   paragraphes déterminants, du dispositif et de l'identité. La décision est
   `verifie` pour le passage seulement si ces trois éléments viennent de la
   page de la décision ; sinon `partiel`.

Une décision lue ne prouve ni l'état actuel de la jurisprudence, ni
l'exhaustivité de la recherche. Le dire quand la réponse en dépend.

### 10.4 Où chercher pendant une réponse

Recherche **ciblée** : seulement pour une conclusion qui dépend d'une
décision. Au plus trois recherches et trois décisions ouvertes par question ;
au-delà, réserver la conclusion et indiquer la voie suivante. Ordre :

1. Les décisions des références embarquées du plugin, avec leur date de
   relecture : ouvrir leur adresse si un outil web est disponible.
2. **Légifrance**, par numéro puis par mots : fonds JURI (Cour de cassation,
   sélection des juges du fond) et CETAT (juridiction administrative).
3. Le site de la juridiction pour une décision dont l'adresse est connue :
   Conseil d'État (ArianeWeb), Conseil constitutionnel, HUDOC (adresse de
   conversion du document), CELLAR pour la CJUE.
4. Une recherche web **restreinte aux domaines officiels** pour retrouver un
   numéro ou une adresse ; puis ouvrir la décision.
5. En dernier, la doctrine, citée comme telle.

Ne pas construire une adresse ou un identifiant à la main : un échec sur une
adresse devinée ne prouve rien. Un zéro résultat sur Légifrance ne prouve pas
l'absence de décision : seule une sélection des décisions des juridictions du
fond y est diffusée.

Voies observées le 17 octobre 2026 avec l'outil web d'une session :

| Source | Adresse | Observation |
|---|---|---|
| Légifrance, recherche judiciaire | `https://www.legifrance.gouv.fr/search/juri?tab_selection=juri&searchField=ALL&query=<numéro ou mots>&page=1&init=true` | Résultats avec identifiant JURITEXT. |
| Légifrance, décision judiciaire | `https://www.legifrance.gouv.fr/juri/id/<JURITEXT…>` | Texte intégral et analyse. |
| Légifrance, recherche administrative | `https://www.legifrance.gouv.fr/search/cetat?tab_selection=cetat&searchField=ALL&query=<…>&page=1&init=true` | Résultats avec identifiant CETATEXT. |
| Légifrance, décision administrative | `https://www.legifrance.gouv.fr/ceta/id/<CETATEXT…>` | Texte intégral, analyse, mention Lebon. |
| Conseil d'État | `https://www.conseil-etat.fr/fr/arianeweb/CE/decision/<AAAA-MM-JJ>/<numéro>` | Lisible si l'adresse vient d'une recherche. |
| Conseil constitutionnel | `https://www.conseil-constitutionnel.fr/decision/<année>/<numéro>.htm` | Lisible ; la recherche du site ignore la requête. |
| Cour EDH | `https://hudoc.echr.coe.int/app/conversion/docx/html/body?library=ECHR&id=<001-…>` | Lisible ; la page HUDOC ordinaire est vide. |
| CJUE | manifestation CELLAR connue | CURIA et EUR-Lex illisibles ; voir 10.5. |
| Cour de cassation (Judilibre) | — | Pages vides pour l'outil ; passer par Légifrance. |

### 10.5 Conduite quand la recherche n'aboutit pas

| Situation | Conduite |
|---|---|
| **Recherche vide** | Dire où et comment la recherche a été faite (source, termes ou numéro, date). Rappeler qu'un résultat vide ne prouve pas l'absence de jurisprudence. Réserver la seule conclusion qui dépend d'une décision ; donner la règle écrite lue, la piste (notion, question à poser) et la voie de recherche ; poursuivre le reste de la réponse. |
| **Décision identifiée mais illisible** | Fiche au statut `inaccessible` avec l'obstacle observé. Essayer une autre publication officielle (Légifrance ou site de la juridiction). Sinon proposer à la personne de l'ouvrir dans son navigateur ou de la fournir, ou au professionnel nommé de la vérifier. Ne pas restituer son contenu de mémoire. |
| **Seulement un résumé officiel ou un communiqué** | Le citer comme tel, avec la décision au statut `partiel` ; conclusion présentée comme conditionnelle. |
| **Seulement de la doctrine** | « Selon [auteur, qualité], dans [support] du [date], [juridiction] aurait jugé… ; je n'ai pas lu la décision. » Chercher ensuite la décision par son numéro sur Légifrance ; si elle reste introuvable, réserver. |
| **Jurisprudence divergente** | Exposer les décisions lues avec juridiction, formation, date et publication. Distinguer Cour de cassation et juges du fond, chambres différentes, formations solennelles, publié et inédit. Une décision plus récente n'efface pas automatiquement les autres. Ne pas choisir en silence : conclusion conditionnelle et risque expliqué. |
| **Décision ancienne et texte plus récent** | Vérifier quel texte et quelle version la décision interprétait, et quelle version s'applique aux faits (section 3). Si le texte a changé, signaler que la décision peut ne plus être pertinente et chercher une décision postérieure ; pour des faits anciens, elle peut rester pertinente. Ne pas présumer l'un ou l'autre. |
| **Décision non définitive, revirement, décision d'une cour suprême ou européenne** | Signaler un recours connu ou non recherché, une inconstitutionnalité à effet différé, une interprétation de la CJUE ou un constat de la Cour EDH qui peut modifier la portée ; ne pas en tirer un effet sur le dossier sans le vérifier. |
| **Aucun outil web** | Citer seulement les décisions des références embarquées, avec leur date de relecture, comme pistes non relues pendant la réponse. Ne citer aucune autre décision. Réserver la conclusion et indiquer la vérification à faire. |

Formulations utilisables (les crochets sont à renseigner) :

> J'ai cherché une décision sur [question] dans [source] le [date] avec
> [termes / numéro] : [aucun résultat / résultat illisible]. Cela ne prouve
> pas qu'il n'en existe pas. [Conclusion] reste donc à confirmer ; pour
> avancer, [voie de recherche ou professionnel].

> Je n'ai trouvé qu'un commentaire de [auteur, qualité] du [date], qui
> rapporte que [juridiction] aurait jugé [solution]. Je n'ai pas lu la
> décision elle-même.

---

## Partage entre l'exécution et la maintenance

| Pendant la réponse d'un skill | En maintenance du dépôt |
|---|---|
| Recherche ciblée par l'outil web de la session, dans l'ordre 10.4, bornée à la question. | Outils `scripts/legal_sources.py` (BASE-010) : CELLAR, archives DILA ; [BASE-018](../suites/base-018-lecture-decisions-dila.md) pour lire une décision des fonds de jurisprudence DILA. |
| Aucun script du dépôt, aucun accès Bash, aucun connecteur requis. | Relecture datée des décisions citées par les références embarquées, bloquante pour un lot (BASE-014). |
| Sans outil web : références embarquées comme pistes, avec date de relecture. | Les décisions de principe utiles à une tâche sont relues et embarquées dans la référence métier avec une adresse officielle lisible, pour éviter une recherche à l'exécution. |
| Aucun stockage persistant de décisions récupérées. | Veille des décisions nouvelles touchant une référence livrée (VEI-021). |
| Pas de promesse d'exhaustivité. | Pas d'index complet des fonds DILA (hors périmètre). |

Options écartées pour l'exécution : embarquer `legal_sources.py` dans les
paquets (dépendance Python et Bash, hôtes et limites à maintenir dans onze
paquets, sans gain pour Légifrance qui refuse le client direct) ; API
Judilibre et Légifrance (souscription PISTE indisponible) ; index local des
fonds DILA (hors périmètre de la story).
