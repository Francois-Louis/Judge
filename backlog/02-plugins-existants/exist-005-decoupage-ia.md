# EXIST-005 — Découpage de la gouvernance IA

Propositions du **16 octobre 2026**, fondées sur l'[inventaire des 23 fichiers](exist-005-inventaire-ia.md).
Les 20 suites IA restent `proposee` ; la [relecture documentaire](exist-005-verification.md)
porte sur trois dossiers fictifs, sans classification juridique définitive.

## Contrat commun et première tranche proposée

Toutes les suites dépendent d'EXIST-005, PILOTE-003, BASE-005 et BASE-006.
Le bilan PILOTE-003 est terminé après BASE-011 ; le préalable est satisfait,
sans sélection automatique d'une extension. Ses limites H01 complet et lecteur
indépendant demeurent consignées. Chaque lot applique BASE-003, BASE-008,
la méthode BASE-005 `1.0.0` embarquée et les couches de recette BASE-006.

**Première tranche proposée : IA-001**, inventaire factuel d'un assistant
rédactionnel interne pour une petite structure sans service juridique.
Entrée : description, outil/version et pièces disponibles ; sortie : fiche
identifiée, usages, acteurs déclarés, stade, preuves et inconnues. Aucun rôle
juridique, niveau de risque ni feu vert n'est déduit du simple enregistrement.
Cette fiche est utile sans profil professionnel complet, historique ou compte
connecté. Créer un profil durable absent reste soumis à l'entretien BASE-008 ;
une sortie ponctuelle peut rester dans la conversation.

Chaque tranche corrige les seuls blocs de setup, descriptions, routage et
sorties nécessaires à son résultat. IA-018/019/020 ne sont pas des préalables
à toute fiche manuelle : chacune embarque les références locales dont elle a
besoin et applique elle-même recherche et stockage. Les commandes techniques
existantes sont conservées, les modes visibles précisent leur portée et les
branches encore héritées ne sont pas présentées comme adaptées France/UE.

## Stories et dépendances métier

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [IA-001](suites/ia-001-inventaire-factuel.md) | Fiche factuelle d'un système et de ses versions/usages | Aucune |
| [IA-002](suites/ia-002-qualification-usage.md) | Qualification conditionnelle de l'objet, des acteurs et du champ | IA-001 |
| [IA-003](suites/ia-003-pratiques-interdites.md) | Examen ciblé d'une pratique potentiellement interdite | IA-002 |
| [IA-004](suites/ia-004-qualification-haut-risque.md) | Qualification haut risque d'un système/usage déterminé | IA-002 |
| [IA-005](suites/ia-005-transparence-usage.md) | Fiche de transparence pour une fonction et son public | IA-002 |
| [IA-006](suites/ia-006-qualification-modele-gpai.md) | Fiche distincte de modèle GPAI et rôle de l'acteur | IA-002 |
| [IA-007](suites/ia-007-obligations-deployeur.md) | Fiche d'obligations d'un déployeur pour un usage borné | IA-004 |
| [IA-008](suites/ia-008-dossier-fournisseur-systeme.md) | État des pièces d'un fournisseur de système potentiellement à haut risque | IA-004 |
| [IA-009](suites/ia-009-evaluation-interne.md) | Évaluation interne des impacts d'un usage | IA-002 |
| [IA-010](suites/ia-010-necessite-fria.md) | Décision motivée sur la nécessité d'une FRIA, ou faits manquants | IA-004 |
| [IA-011](suites/ia-011-projet-fria-service-public.md) | Projet FRIA d'un déployeur de service public déjà qualifié | IA-010 |
| [IA-012](suites/ia-012-cartographie-contrat-fournisseur.md) | Carte des engagements IA sur une chaîne fournisseur précise | Aucune |
| [IA-013](suites/ia-013-clauses-fournisseur.md) | Modifications ciblées d'un écart contractuel IA | IA-012 |
| [IA-014](suites/ia-014-politique-assistant-interne.md) | Projet de politique pour un assistant rédactionnel interne | Aucune |
| [IA-015](suites/ia-015-comparer-pratique-politique.md) | Écarts entre une pratique proposée et une politique déterminée | Aucune |
| [IA-016](suites/ia-016-revue-sorties-politique.md) | Rapport de dérive sur un corpus de sorties explicitement délimité | IA-015 |
| [IA-017](suites/ia-017-ecart-evolution-reglementaire.md) | Écart produit par un changement de texte pour un système/rôle | IA-002 |
| [IA-018](suites/ia-018-preferences-gouvernance.md) | Préférences volontaires et modification ciblée | Aucune |
| [IA-019](suites/ia-019-dossier-systeme.md) | Dossier isolé par organisme/système/version | Aucune |
| [IA-020](suites/ia-020-sources-calendrier.md) | Checklist d'actualité et relevé temporel traçable par disposition | Aucune |

Une dépendance métier désigne le contrat d'entrée réutilisé. Une fiche
équivalente fournie manuellement peut être consommée et ses manques sont
signalés ; aucun historique d'exécution ou plugin voisin n'est exigé.
IA-007/008/010 ne déduisent pas haut risque d'un mot RH : la qualification
IA-004 reste préalable à leurs conclusions. IA-003 et IA-005 sont à examiner
selon les fonctions, indépendamment de la seule qualification haut risque.
IA-006 concerne le modèle ; IA-008 le système. L'extension aux obligations
complètes du fournisseur de modèle ou aux autres opérateurs attend un cadrage
distinct, sans assimilation au rôle du fournisseur de système.

## Propriétaires des contrats de contenu

IA-001 possède la fiche d'inventaire : organisme, système/version, usage,
composants, propriétaire, stade et provenance. IA-002 possède la fiche de
qualification ; IA-003/004/005/006 ajoutent leurs analyses sourcées sans
écraser le fait d'origine. Un même système peut avoir plusieurs usages et
acteurs, et un composant partagé ne fusionne pas les dossiers des utilisateurs.
Le registre interne d'autorisations conserve sa propre décision, son auteur,
son périmètre et ses conditions ; il ne fournit pas une catégorie juridique.

IA-009 possède l'évaluation interne : dommage, hypothèse, mesure proposée,
preuve de réalisation et décision attribuée. IA-010 possède les critères
de nécessité FRIA ; IA-011 consomme leur résultat et porte son propre projet.
L'AIPD reste chez privacy, l'évaluation de conformité technique hors de ces
livrables. Aucune case AIA terminée ne clôt les autres évaluations.

IA-012 possède la carte contractuelle avec pièces/version/hiérarchie et
engagements par acteur ; IA-013 la proposition de modification. IA-014 possède
la politique bornée ; IA-015 le contrat d'écart, repris par IA-016 avec état
des pièces et couverture du balayage. IA-017 garde la source modificative et
la preuve de changement ; IA-020 possède relevé de recherche, actualité et
fiche temporelle. Les futures références n'ont qu'un propriétaire ; les autres
tranches les chargent localement plutôt que recopier des grilles inline.

## Faits déterminants, sources à rechercher et calendrier

Ces questions sont des exigences des futures implémentations, **pas des
qualifications ou dates vérifiées dans EXIST-005**.

| Axe | Faits et pièces à obtenir | Recherche future / traitement des manques |
|---|---|---|
| Objet | Fonctionnement, finalité prévue/effective, entrées/sorties, autonomie, versions, modèle seul ou système intégré | Définition et champ du règlement IA, exclusions éventuelles ; ne pas déduire IA du nom commercial. |
| Acteurs/rôles | Qui développe/fait développer, met sur le marché/met en service, sous quel nom, utilise, importe/distribue ; contrat, modifications et finalité changée | Définitions et règles de changement de rôle dans le texte actuel ; pas de rôle global de société, ni fine-tuning = fournisseur automatiquement. |
| Catégories | Fonction concrète, personnes, décision/effet, profilage éventuel, biométrie/émotions, produit et procédure sectorielle, modèle généraliste | Pratiques interdites, deux voies haut risque, conditions/exceptions, transparence et modèle GPAI traités séparément. Absence d'Annexe III ne signifie pas absence de haut risque ou d'autres obligations. |
| Territoire | Établissement des acteurs, pays de mise à disposition/service/utilisation, lieu d'utilisation des sorties, personnes affectées | Champ territorial et rattachements exacts ; ni siège français ni `eu_nexus: true` ni résidence UE ne suffisent à attribuer toutes les obligations. EEE à vérifier séparément. |
| Temps | Dates de marché/service, modifications et usage réel, date visée, versions des textes et dispositions transitoires | EUR-Lex : règlement IA, rectificatifs, modifications, actes délégués/d'exécution pertinents et JO ; chercher statut actuel des réformes alléguées. Distinguer adopté/publié/entré en vigueur/applicable, par disposition et acteur. Aucun calendrier global figé. |
| Autorités et guides | Activité, rôle, pays, domaine et problème précis | Identifier compétences françaises effectives dans les textes officiels et sites des autorités, CNIL pour ses sujets, Commission/Bureau IA pour leurs documents. Pas de CNIL présumée autorité unique, pas de guide/norme/code de pratique assimilé à un règlement ; vérifier adoption, version et portée. |
| Échéance | Nature de l'obligation, source et passage, événement déclencheur, preuve de date, régime transitoire, calcul et exceptions | IA-020 exige un calcul reproductible lorsqu'une échéance peut être établie ; sinon `a-determiner`. Distinguer délai légal, revue interne et date de lancement. |

Accès officiel suivant BASE-005 et BASE-010, y compris voies alternatives
EUR-Lex/CELLAR ou publications officielles françaises quand nécessaires.
Ne pas imposer d'abonnement API ni bloquer les autres travaux après un refus
d'accès ; réserver uniquement la conclusion dépendante, tracer la tentative
réelle et ne pas inventer de consultation.

## Relais ciblés et autonomie

Le plugin IA conserve la qualification IA et transmet une fiche autonome :
question exacte, usage/version, acteur, faits établis, pièces lues/manquantes,
dates/territoires et conclusion réservée. Privacy porte données/nécessité AIPD,
travail les effets RH, produit la revue de lancement ; PI et le domaine
sectoriel ne sont appelés que sur un fait discriminant. Les suites PRV/PDT et
les tâches RH encore héritées ne sont pas des capacités déjà disponibles.
Si le relais adapté manque, remettre cette fiche et les questions à instruire,
sans exécuter automatiquement le skill amont ou voisin.

Chaque futur paquet doit fournir seul ses modèles, méthode, sources métier et
messages de limite. La recette comprendra paquet détaché, client, résultat
métier et compréhension par lecteur non juriste. Aucune installation,
connexion, publication, programmation de veille ou adaptation métier n'est
réalisée par ce découpage.
