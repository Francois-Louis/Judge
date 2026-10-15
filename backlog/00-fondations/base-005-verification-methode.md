# BASE-005 — Vérification de la méthode de recherche

Relecture effectuée le **15 octobre 2026 (Europe/Paris)** sur la méthode
`1.0.0`, [source d'édition](../../references/research-citation-method.md).
Les cas ci-dessous sont fictifs et servent à contrôler les consignes et les
sorties attendues. Ils ne sont ni des consultations réalisées, ni des tests
d'exécution d'un skill. Les accès web réellement tentés sont relevés séparément.

## 1. Source inaccessible

**Entrée fictive.** Une personne invoque un article à partir d'un résumé ;
l'accès au texte officiel échoue, aucun contenu complet n'est fourni.

**Application.** Sections 3 à 5 : conserver le résumé comme piste, tracer
l'échec, laisser la consultation du texte vide et réserver la conclusion qui
dépend du passage manquant. Proposer une autre publication officielle ou
demander une copie dont la provenance sera identifiée.

**Sortie de contrôle.** « Le texte officiel n'a pas pu être lu. Le résumé ne
permet pas de confirmer la règle applicable. Il faut le passage complet et sa
version pour conclure sur votre demande. » La date de tentative ne serait
renseignée que lors d'une tentative réelle ; aucune citation ni consultation
fictive n'est produite dans ce cas.

**Résultat de relecture : conforme.** Le tableau des statuts distingue
`inaccessible`, `partiel` et `non-verifie`, et sépare l'accès de l'applicabilité.
Le relevé réel ci-dessous montre aussi la distinction entre un échec d'accès et
une consultation réussie par une autre URL.

## 2. Litige ancien

**Entrée fictive.** Contrat conclu en 2018, fait contesté en 2019, démarche
envisagée en 2026 ; seule une fiche pratique actuelle est disponible.

**Application.** Sections 1, 3 et 4 : distinguer les trois dates et la question
de fond de la démarche actuelle. Rechercher les versions pertinentes et leurs
transitions, puis la jurisprudence utile. La fiche ne prouve ni le droit de 2019,
ni l'absence de délai, ni la rétroactivité d'une réforme.

**Sortie de contrôle.** « La fiche actuelle ne suffit pas à établir la règle
pour les faits de 2019. Il faut le contrat, les événements datés et les textes
dans leurs versions pertinentes ; la possibilité d'agir aujourd'hui reste aussi
à vérifier. » Applicabilité : `a-etablir` ; aucune durée ni conclusion sur la
prescription ne sont déduites des seules années.

**Résultat de relecture : conforme.** La méthode requiert une chronologie et une
analyse des transitions ; elle interdit de remplacer le droit applicable aux
faits par la seule version en vigueur au jour de la recherche.

## 3. Demande transfrontalière

**Entrée fictive.** Particulier résidant en France, achat auprès d'un vendeur
établi en Allemagne, livraison prévue en France ; une clause désigne le droit
allemand et un tribunal allemand. Un résumé de directive, un projet de réforme
et une référence à la Cour EDH sont invoqués.

**Application.** Sections 1 à 5 : vérifier qualité des parties, contrat, dates
et rattachements ; séparer compétence, loi applicable et exécution. Le domaine
sectoriel recherche les instruments de conflit et protections utiles. La clause
n'est pas traitée comme décisive sans examen. Rechercher transposition et
invocabilité éventuelle de la directive ; classer le projet comme préparatoire.
La référence Cour EDH relève du Conseil de l'Europe et ne remplace pas une
analyse du droit de l'UE ou du droit allemand.

**Sortie de contrôle.** « Vos pays de résidence, d'établissement et de livraison
doivent être pris en compte. Les clauses et le résumé de directive ne suffisent
pas à déterminer vos droits ou le tribunal compétent. Le projet ne permet pas
de réclamer un droit déjà applicable. » Aucune règle sectorielle n'est inventée.

**Résultat de relecture : conforme.** Pas de déduction automatique du droit
français depuis la langue ou la résidence, pas de directive transformée sans
analyse en obligation entre particuliers, pas de confusion UE/CEDH/droit étranger.

## 4. Notification de date inconnue

**Entrée fictive.** Une décision porte une date, mais la personne ignore quand
et comment elle a été notifiée ; elle demande la date limite pour la contester.

**Application.** Section 6 : enregistrer la date portée sur le document comme
telle ; demander l'acte complet, le mode de notification et son justificatif.
Identifier le régime avant de retenir durée, déclencheur et exceptions. Garder
`echeance: a-determiner`, sans substituer la date de décision ou la date du jour.
Ne pas promettre qu'une demande de pièces suspend le délai.

**Sortie de contrôle.** « Je ne peux pas fixer une date limite fiable avec la
seule date de la décision. Il faut vérifier le régime du recours et les preuves
de notification. Réunissez ces pièces et contactez rapidement un professionnel
compétent ; un délai peut déjà courir. » Le contrôle humain est requis avant
de se fier au calcul d'un délai de recours ; aucune échéance certaine n'est créée.

**Résultat de relecture : conforme.** Nature, déclencheur, preuve, calcul,
exceptions, état de vérification et responsabilité sont exigés séparément.

## Accès officiels réellement effectués

Accès par l'outil de navigation le **15 octobre 2026**. Une date de tentative
est une trace d'opération, pas une date de consultation réussie. Les dates de
publication ou de collecte affichées par un moteur ne sont pas utilisées comme
dates de consultation. Aucun dossier personnel n'a été transmis.

| Cible | Résultat observé | Consultation du contenu utile / portée |
|---|---|---|
| [Légifrance, Cas d'usage](https://www.legifrance.gouv.fr/contenu/menu/cas-d-usage) | Ouverture refusée, HTTP 403 ; un extrait de moteur était visible | Non réalisée ; `inaccessible` pour la page complète, extrait seulement `partiel`. Aucune affirmation détaillée sur l'outil ChronoLégi n'en est tirée. |
| [Code civil, article 2](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419281) | Ouverture refusée, HTTP 403 | Non réalisée ; `inaccessible`. Aucun régime temporel particulier n'est tenu pour vérifié par cette tentative. |
| [TFUE, article 288, URL CELEX](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:12012E288) | Écran de contrôle nécessitant JavaScript | Non réalisée sur cette URL ; `inaccessible`. |
| [TFUE, article 288, URL ELI](https://eur-lex.europa.eu/eli/treaty/tfeu_2012/art_288/oj/fra) | Texte français complet de l'article accessible, CELEX 12012E288, JOUE C 326 du 26 octobre 2012 | Réalisée le 15 octobre 2026 ; `verifie` pour les catégories d'actes, repère S1 de la méthode. Ne valide aucune directive sectorielle. |
| [EUR-Lex, FAQ](https://eur-lex.europa.eu/content/help/faq/intro.html?locale=fr) | Écran de contrôle nécessitant JavaScript | Non réalisée ; `inaccessible`. Aucune conclusion sur la consolidation n'est présentée comme vérifiée grâce à cette FAQ. |
| [Conseil de l'Europe, Ne pas confondre](https://www.coe.int/fr/web/about-us/do-not-get-confused) | Rubriques institutionnelles lues | Réalisée le 15 octobre 2026 ; `verifie` pour la distinction des institutions, S2. Les autres chiffres et informations de la page ne sont pas repris ni certifiés. |
| [Cour EDH, Base de données HUDOC](https://www.echr.coe.int/fr/hudoc-database) | Présentation de la base lue | Réalisée le 15 octobre 2026 ; `verifie` pour la fonction de la base, S3. Aucun arrêt particulier consulté. |

## Embarquement et limites

La méthode contient sa version, sa date d'édition et son origine. Son corps est
autonome : aucune référence locale nécessaire vers le backlog, la racine ou un
autre plugin. Le chemin d'origine dans les métadonnées sert à l'édition ; le
chargement prévu depuis un skill utilise la copie locale dans le plugin.

Une copie temporaire a été préparée selon
`<plugin>/references/shared/research-citation-method.md` et lue depuis le chemin
relatif prévu pour `<plugin>/skills/<tache>/SKILL.md`, hors du checkout. Identité
des octets et résolution interne du chemin vérifiées ; aucun plugin opérationnel
n'a été synchronisé. Cette preuve porte sur le fichier et son chemin, pas sur
l'installation ou le comportement d'un plugin. La recette des artefacts réels
reste à BASE-006 et aux lots d'adaptation.

Le texte refuse toute garantie automatique de secret professionnel pour une
sortie générée. Les sources et raisonnements sectoriels restent à documenter
dans chaque plugin. Cette relecture ne valide aucun délai réel, aucune règle
sectorielle et aucun workflow juridique existant. Aucun test automatisé par
mots-clés n'est présenté comme validation juridique.
