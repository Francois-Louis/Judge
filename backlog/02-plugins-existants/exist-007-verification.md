# EXIST-007 — Vérification du cadrage de veille

Relecture par l’agent de maintenance, **16 octobre 2026**. Objets relus :
[inventaire](exist-007-inventaire-veille.md), [découpage](exist-007-decoupage-veille.md)
et vingt suites proposées. Les fixtures ci-dessous sont **fictives** : aucun
texte juridique réel de ces scénarios n’a été recherché ni qualifié et aucun
skill n’a été exécuté. La portée générale est regroupée dans le
[bilan de la story](exist-007-veille-reglementaire.md).

## V01 — Publication au JORF

**Fixture textuelle :** « Arrêté fictif A, publié au JORF le 2 octobre 2026.
L’article 1 s’applique à compter du 1er janvier 2027 ; l’article 2 à compter
du 1er juillet 2027. » L’annexe mentionnée manque. Une association demande
« qu’est-ce que cela change pour nous ? » sans décrire son activité.

**Résultat attendu dans les futures recettes :** VEI-001 identifie publication,
auteur, référence, version et annexe manquante. VEI-005 garde publication et
deux événements d’application rattachés à leurs dispositions ; une entrée en
vigueur reste à rechercher, sans la remplacer par l’une des dates. VEI-007
demande activité, rôle, territoire, dates et critères pertinents avant champ
ou obligation. VEI-008 ne crée aucun écart sans politique/texte complet et
exigence qualifiée. Aucun Federal Register, final rule, date effective unique
ou gap automatique ne résulte du mot JORF.

**Observation de relecture :** VEI-001 Q01, VEI-005 T01/T02 et VEI-007 A01/A02
portent ces conditions et manques. VEI-008 E02 couvre document absent et
comparaison impossible. Le contrat conserve nature de l’événement, version,
source/passages et statut temporel. **Conforme au cadrage**, pas un résultat
juridique produit par le plugin.

## V02 — Directive à transposer

**Fixture textuelle :** « Directive fictive D, publiée au JOUE. Disposition X :
les États membres mettent en vigueur les mesures de transposition au plus
tard le 30 juin 2027. » Une fiche de portail annonce une mesure française M,
sans son texte ; aucune correspondance précise à X n’est fournie.

**Résultat attendu :** VEI-001 identifie type d’acte et provenance ; VEI-005
conserve échéance de transposition distincte de publication/entrée en vigueur/
application. VEI-006 recherche texte national exact/version, relation avec X,
date et couverture, distingue mesure déclarée/notifiée, publiée, lue et portée
établie. Absence de résultat ou fiche isolée ne prouve ni défaut ni transposition
complète. VEI-007 réserve toute obligation de l’acteur privé et, si nécessaire,
prépare relais sectoriel avec question exacte. Aucun décret français imaginé,
booléen « transposé » ou échéance interne de conformité n’est créé.

**Observation de relecture :** VEI-006 D01/D02 nomment les pièces et limites,
VEI-005 exige source/version et événement, VEI-007 accepte fiche équivalente
mais non conclusion dépourvue de preuve. La directive reste distincte d’un
règlement et d’une mesure nationale. **Conforme au cadrage**, sans analyse
réelle de transposition ou d’effet direct.

## V03 — Consultation d’autorité

**Fixture textuelle :** « Autorité Z : consultation publique sur un projet
de guide, questions 1 à 5. Contributions avant le 15 novembre 2026 à 17 h,
heure de Paris ; modalités dans l’annexe. » L’annexe précise publication
possible des réponses, mais le régime de confidentialité reste incomplet.
Une petite association envisage de répondre aux questions 2 et 4.

**Résultat attendu :** VEI-013 identifie consultation, auteur, projet/version,
public et modalités, source de la date/heure/fuseau et points à vérifier sur
publication/confidentialité ou prolongation. La clôture de participation n’est
pas une date d’application ou de mise en conformité. VEI-014 garde intention,
décision attribuée, projet préparé et dépôt avec accusé distincts. VEI-015
prépare seulement les questions choisies sur faits fournis, sans statistiques,
mandat ou consensus inventés. Pas de NPRM, gap-tracker de conformité, avocat
obligatoire pour noter une intention, dépôt ni Slack automatique.

**Observation de relecture :** VEI-013 CO01/CO02 distingue avis public et
demande individuelle, VEI-014 CD01/CD02 intention et dépôt prouvé, VEI-015
CC01/CC02 le brouillon et les faits non disponibles. La confidentialité
est une question à instruire, pas une propriété du header. **Conforme au
cadrage**, sans contribution préparée pour un avis réel ni soumission.

## Différences d’événements et limites complémentaires

| Variante fictive | Disposition du cadrage constatée à la relecture |
|---|---|
| La même page change de bandeau, sans ancien texte sauvegardé | VEI-004 ne déduit pas réforme de l’empreinte ; version antérieure manque et comparaison réservée. |
| Consultation « material » selon critère interne | VEI-013 garde nature consultation ; aucune obligation nouvelle dans VEI-010 ; VEI-016 classe pertinence distincte. |
| Politique exclue du corpus ou bibliothèque non indexée | VEI-008 garde non examiné/inconnu, ne dit pas politique absente. |
| Politique approuvée, mesure opérationnelle inconnue | VEI-009 garde proposition ; VEI-012 ne transforme pas approbation ou risque accepté en conformité. |
| Source échouée, entrée tardive et date identique à dernier curseur | VEI-003 garde erreur/fenêtre/doublons ; VEI-016 ne produit pas all-clear ; curseur par source et couverture lue. |
| Courrier individuel de contrôle envoyé par autorité | VEI-013 ne traite pas cela en consultation publique, fiche autonome pour secteur/administratif/contentieux selon acte. |
| Source inaccessible, profil absent ou domaine voisin non adapté | Résultat ponctuel utile, alternative officielle puis réserve ciblée, fiche de relais sans appel à un plugin supposé livré. |

## Vérifications techniques effectivement exécutées

Sept sondages publics sont conservés dans [sources.json](exist-007-sources.json),
avec URL/horodatage/taille/empreinte et format. Les endpoints CNIL anglais du
catalogue et français renvoient chacun HTTP 200, racine RSS et dix items.
Le répertoire DILA JORF renvoie HTML avec liens d’archives, sans téléchargement
de ces archives. La page EDPB renvoie HTML, avec redirection et aucun lien
RSS/Atom détecté par le sondage limité. Les trois URL EUR-Lex renvoient HTTP
202 vide en accès Python ; les ouvertures web des aides affichent challenge JS.

Les résultats indexés de la documentation officielle
[webservice EUR-Lex](https://eur-lex.europa.eu/content/help/data-reuse/webservice.html?locale=en)
et [alertes RSS](https://eur-lex.europa.eu/content/help/my-eurlex/my-rss-feeds.html?locale=en)
ont été lus : SOAP/XML après inscription/autorisation et création d’alertes
personnalisées connecté. Ce statut documentaire est distinct d’une page ouverte
complètement et d’un compte authentifié testé. Aucun accès SOAP, création
d’alerte ou abonnement n’a été réalisé. Le sondage ne certifie pas les autres
assertions héritées de retrait/panne/authentification du catalogue.

Commandes réellement exécutées :

```text
python -X utf8 backlog/02-plugins-existants/exist-007-sondages.py
python -X utf8 backlog/02-plugins-existants/exist-007-controles.py --baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-007-resultats.json
```

Le [contrôleur documentaire](exist-007-controles.py) conserve les
[résultats](exist-007-resultats.json) : 26 fichiers/9 skills et six fichiers
de cookbook couverts exactement, vingt suites et cibles futures, liens/index,
frontmatters/dépendances, copies communes, inventaire des 59 lignes et format
des sondages. Il observe aussi le défaut du modèle comment-tracker : commentaire
HTML chargé comme clé parasite et entrée CMT-001 fictive dans liste active,
correction future VEI-014. Le défaut n’est pas corrigé dans le plugin ici.

Comparaison à l’instantané de début de tâche : empreintes du plugin, cookbook
et travaux antérieurs protégées ; différences simultanées éventuelles ailleurs
consignées sans attribution. JSON, lint des droits cookbook et espaces sont
contrôlés. Pas de validation de schéma plugin/client ni recette métier par ces
contrôles documentaires, puisque les paquets sont inchangés.
