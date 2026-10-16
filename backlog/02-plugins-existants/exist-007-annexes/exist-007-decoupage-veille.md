# EXIST-007 — Découpage de la veille réglementaire

Propositions du **16 octobre 2026**, fondées sur l’[inventaire exhaustif](exist-007-inventaire-veille.md).
Les 21 VEI restent `proposee`. La [relecture](exist-007-verification.md) porte
sur publication JORF, directive et consultation fictives, sans obligation réelle
qualifiée. Les [sondages de sources](exist-007-sources.json) sont techniques.

## Contrat commun et première tranche proposée

Chaque suite dépend d’EXIST-007, PILOTE-003, BASE-005 et BASE-006. Le bilan
PILOTE-003 est terminé après BASE-011 : préalable satisfait, sans sélection
automatique d’une extension. Les limites H01 complet et lecteur indépendant
du pilote restent consignées.

**Première tranche proposée : VEI-001**, qualification d’une publication fournie
par une petite structure, association ou personne sans profil professionnel.
Entrée : document et objectif ; sortie : auteur, identifiant/version, nature
de l’événement, dates textuelles, statut de lecture, pièces manquantes et
question suivante. Ni collecte exhaustive ni obligation applicable n’en
résultent. Cette tranche fonctionne sans bibliothèque, registre ou compte.

Une dépendance métier désigne le contrat d’entrée : une fiche équivalente
manuelle peut être consommée en signalant ses manques. Les stories de
préférences/dossier ne bloquent pas la lecture conversationnelle ponctuelle.
Chaque tranche corrige ses seuls blocs de profil, routage et annonces et
charge méthode BASE-005 1.0.0 et références locales autonomes ; stockage durable
via helper BASE-008, profil absent créé seulement après entretien neuf.

VEI-019 et **VEI-020 sont postérieures à l’adaptation des tâches manuelles**.
Le cookbook fait l’objet d’une story distincte après agent et manuel ; aucun
catalogue, compte, hook vide ou YAML de planning ne constitue une automation
installée. Les sondages de maintenance ne sont pas un collecteur embarqué.

## Stories et dépendances métier

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [VEI-001](../suites/vei-001-qualifier-publication.md) | Qualifier une publication fournie | Aucune |
| [VEI-002](../suites/vei-002-capacite-source.md) | Vérifier la capacité d’une source de veille | Aucune |
| [VEI-003](../suites/vei-003-collecter-rss.md) | Collecter manuellement un flux RSS français | VEI-002 |
| [VEI-004](../suites/vei-004-preuve-modification.md) | Établir la preuve d’une modification de texte | VEI-001 |
| [VEI-005](../suites/vei-005-chronologie-texte.md) | Établir la chronologie d’un texte | VEI-001 |
| [VEI-006](../suites/vei-006-suivi-transposition.md) | Documenter la transposition française d’une directive | VEI-001, VEI-005 |
| [VEI-007](../suites/vei-007-applicabilite-ciblee.md) | Qualifier le champ d’un changement pour une activité | VEI-001, VEI-005 |
| [VEI-008](../suites/vei-008-ecart-politique.md) | Comparer un changement qualifié à une politique | VEI-004, VEI-007 |
| [VEI-009](../suites/vei-009-projet-politique.md) | Proposer une modification ciblée de politique | VEI-008 |
| [VEI-010](../suites/vei-010-enregistrer-ecart.md) | Enregistrer un écart documentaire qualifié | VEI-008 |
| [VEI-011](../suites/vei-011-etat-ecarts.md) | Présenter l’état des écarts suivis | VEI-010 |
| [VEI-012](../suites/vei-012-decision-ecart.md) | Consigner une décision de suivi d’écart | VEI-010 |
| [VEI-013](../suites/vei-013-qualifier-consultation.md) | Qualifier une consultation d’autorité | VEI-001 |
| [VEI-014](../suites/vei-014-decision-consultation.md) | Suivre une décision de participation à consultation | VEI-013 |
| [VEI-015](../suites/vei-015-projet-contribution.md) | Préparer un projet de contribution à consultation | VEI-013 |
| [VEI-016](../suites/vei-016-digest-manuel.md) | Préparer une synthèse de veille à la demande | VEI-001 |
| [VEI-017](../suites/vei-017-preferences-veille.md) | Gérer des préférences de veille volontaires | Aucune |
| [VEI-018](../suites/vei-018-dossier-veille.md) | Isoler un dossier de veille ou consultation | Aucune |
| [VEI-019](../suites/vei-019-agent-synthese-locale.md) | Adapter l’agent à une synthèse locale bornée | VEI-003, VEI-016 |
| [VEI-020](../suites/vei-020-cookbook-veille.md) | Vérifier le cookbook après adaptation manuelle | VEI-019 |
| [VEI-021](../suites/vei-021-veille-references-plugins.md) | Signaler les textes modifiés touchant les références d'un plugin livré | BASE-014 |

## Contrats de contenu et responsabilités

| Chaîne | Contrat possédé et limites |
|---|---|
| Sources et collecte | VEI-002 possède fiche source : autorité/pays/secteur, URL de découverte, endpoint, méthode/format, auth nécessaire/testée, limites et observation. VEI-003 possède lot de collecte : fenêtre demandée/effective, éléments, erreurs, doublons et curseur par source. Aucune source silencieuse ne devient disponible ou exhaustive. |
| Événement et versions | VEI-001 possède nature et provenance : identifiant, langue, auteur, source d’origine, URL/corps/version/empreinte, publication déclarée et récupération. VEI-004 possède relation entre versions et relevé des différences ; conserver original, intermédiaires, rectificatif et acte modificatif sans remplacement silencieux. |
| Temps et transposition | VEI-005 possède événement temporel par disposition, source/passages, statut, conditions et preuve de déclencheur ; VEI-006 relation directive/disposition/pays/mesure nationale. Échéance de transposition, mesure notifiée, texte publié et couverture établie sont distincts. |
| Applicabilité et écart | VEI-007 possède fiche acteur/activité/champ/temps/critères/preuves ; VEI-008 compare une politique lue/versionnée à une exigence qualifiée. Un index vide n’établit pas absence de politique ; absence d’écart textuel ne prouve pas pratiques conformes. Le domaine métier conserve l’analyse substantielle de son régime. |
| Proposition et suivi | VEI-009 possède proposition minimale et justification, sans modifier la source. VEI-010 possède entrée du registre des écarts ; VEI-011 rapport ; VEI-012 décision attribuée avec résiduel/réexamen. Acceptation interne du risque ou clôture de tâche ne change pas obligation ni état d’exécution. |
| Consultation | VEI-013 possède fiche avis/objet/version/questions/public/modalités/clôture ; VEI-014 registre intention/décision/préparation/dépôt prouvé ; VEI-015 brouillon distinct. Consultation n’est ni exigence de conformité ni réponse à un contrôle individuel. |
| Sorties et espaces | VEI-016 possède digest avec nature/statut/pertinence et couverture ; VEI-017 préférences volontaires ; VEI-018 espace par organisme/texte/activité/consultation. VEI-019 et VEI-020 réutilisent ces contrats après recette des tâches manuelles, sans élargir conclusions ou droits. |

Les champs date unique `effective`, `due` et booléen `status_verified` hérités
ne suffisent pas. Chaque événement conserve nature, texte/disposition/version,
pays/acteur, date ou inconnue, source/passage, condition/déclencheur et preuve,
méthode de calcul si applicable, vérification et auteur de décision. Jalon
interne, clôture de consultation et délai juridique ne partagent pas une
couleur « overdue » indifférenciée.

## Événements à distinguer

Les attentes ci-dessous sont celles des futures implémentations, **pas des
règles ou calendriers juridiquement vérifiés dans EXIST-007**.

| Entrée | Événement conservé | Vérification et suite possible |
|---|---|---|
| Texte identifié au JORF | Publication d’un acte dans une édition et version déterminées | Texte complet, annexes, portée et dispositions finales/transitoires à lire. Entrée en vigueur et application par disposition restent événements propres VEI-005 ; VEI-007 vérifie rôle/activité. Aucun final rule US ou gap automatique. |
| Directive au JOUE | Publication/type d’acte, pays et dispositions/échéances à instruire | VEI-005 garde temporalité ; VEI-006 recherche mesures françaises pertinentes et leur couverture. Une mesure déclarée ou un délai dépassé ne tranche ni transposition complète ni obligation d’un acteur privé. Aucune transposition présumée du règlement. |
| Consultation d’autorité | Ouverture/invitation portant sur objet et version identifiés | VEI-013 lit avis, questions, participants, clôture/heure/fuseau, modalités et publication des réponses. VEI-014 décision distincte ; VEI-015 brouillon si demandé. Aucun délai de conformité ni dépôt depuis décision de participer. |
| Guide, communiqué, discours ou résumé | Information/position de son auteur, avec statut réel à rechercher | Retrouver texte ou décision primaire avant effets juridiques ; document officiel ne signifie pas acte normatif. Un communiqué et l’acte annoncé ne fusionnent pas en une preuve unique. |
| Rectificatif, modification ou consolidation | Relation à un acte et version, avec passages changés si disponibles | VEI-004 garde avant/après et relation officielle ; différence d’empreinte seule peut être éditoriale. Consolidation, traduction et publication initiale ne sont pas interchangeables. |
| Demande individuelle d’une autorité | Acte entrant à qualifier, distinct d’une consultation publique | Auteur/qualité/destinataire, procédure/stade, pièces et réception à obtenir ; relais administratif, contentieux ou secteur selon acte. Aucun brouillon de contribution publique ni délai NPRM plaqué. |

## Sources, capacités et méthode de recherche future

La matrice technique de l’[inventaire](exist-007-inventaire-veille.md) et le
[relevé des 59 lignes](exist-007-sources.json) distinguent déclarations,
documentation officielle indexée, accès HTTP et format parsé. Les deux flux
CNIL testés sont des candidats bornés ; répertoire DILA JORF, accueil EUR-Lex,
aide SOAP/RSS et page EDPB ne sont pas des endpoints RSS validés par leur seule
URL. Aucun compte authentifié n’a été testé.

Chaque future fiche source précise identité de l’émetteur, territoire/secteur,
primaire ou secondaire, objet couvert et exclusions, endpoint/format/parsing,
pagination/fenêtre/rétention, authentification/droits, tentative horodatée,
réponse/redirection, preuve et prochaine vérification. Retrait ou changement
d’endpoint ferme la couverture active tout en préservant archives et origine.
RSS découvert, endpoint répondant et flux complet sont trois constats distincts.

Sources primaires à lire lors des lots : JORF/Légifrance et textes consolidés
avec relation à la publication ; EUR-Lex/JOUE et dispositions/rectificatifs/
actes modificatifs ; autorité française ou européenne choisie selon secteur,
avis et modalités exactes d’une consultation. UK, Conseil de l’Europe et sources
US restent des périmètres étrangers explicites, pas des membres d’une catégorie
UE indifférenciée. Rechercher statut, version, champ et transitions aux dates
utiles ; guides, projets, actes adoptés, publications et obligations applicables
ne sont pas fusionnés.

BASE-010 fournit des voies de maintenance sans souscription obligatoire :
DILA pour lots publics, CELLAR pour identifiant exact, documents fournis en
solution manuelle. Ni script du checkout ni index juridique global livré
dans le paquet ne sont présumés. Après refus HTTP/202 vide/challenge, essayer
voie officielle pertinente puis réserver la conclusion dépendante, sans
inventer consultation, date ou règle ; poursuivre les éléments indépendants.

## Frontières et disponibilité

Le réglementaire garde provenance/événements/suivi et écart documentaire ciblé.
Privacy traite traitement et AIPD, IA qualification et obligations propres,
produit lancement/allégations, travail effets RH et secteurs leurs règles.
Le relais reçoit question exacte, acteur/activité, textes/versions/passages,
dates établies, pièces lues/manquantes et conclusion réservée. Les suites
PRV/IA/PDT/CTX encore proposées ne sont pas des services installés ; si le
relais adapté manque, cette fiche reste utile sans appel automatique.

Recours contre décision, contrôle individuel, sanction ou réponse à enquête
ne relèvent pas du seul mot « réglementaire » ; qualifier acte et propriétaire
administratif/contentieux/secteur. Publication ou consultation ne devient pas
contentieux. Confidentialité et destination se recherchent selon auteur,
qualité, mission, destinataires et procédure : aucun header work product ou
marque de confidentialité ne garantit protection ou publication restreinte.

Aucune connexion, modification de politique approuvée, abonnement, souscription,
notification, soumission à consultation, calendrier, publication ou déploiement
n’est réalisé par ce découpage.

