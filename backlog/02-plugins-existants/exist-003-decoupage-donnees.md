# EXIST-003 — Découpage protection des données

Propositions du **16 octobre 2026**, issues de l'[inventaire complet](exist-003-inventaire-donnees.md).
Les 21 stories PRV restent `proposee` ; aucune commande du plugin n'est
adaptée par ce cadrage. La [relecture](exist-003-verification.md) confronte
les parcours à des demandes et pièces fictives.

## Contrat commun et lancement

Toutes les suites dépendent d'EXIST-003, PILOTE-003, BASE-005 et BASE-006.
Le bilan PILOTE-003 est terminé après BASE-011 ; le préalable est satisfait,
sans sélectionner de suite. Ses limites H01 complet et lecteur indépendant
restent consignées. Chaque lot applique BASE-003, la méthode locale BASE-005
`1.0.0`, l'isolation BASE-008 et les couches de recette BASE-006.

La sortie suit USAGE-001 : ce qu'on sait, ce qui manque, ce que signifie
le document ou la demande, les pièces et la prochaine action. Une personne,
une association ou une TPE sans service juridique et sans connecteur doit
pouvoir préparer un dossier utile. Le profil complet PRV-019 et le gestionnaire
PRV-020 ne sont pas des préalables : chaque tranche corrige ses propres blocs
setup/routage et accepte une lecture ponctuelle. Sans fait déterminant, garder
les branches conditionnelles ; sans source, réserver la seule conclusion dépendante.

Les identifiants techniques existants sont conservés. « Projet d'AIPD »
remplace l'intitulé visible de pia-generation, sans migration de commande.
PRV-001 crée une tâche pour le particulier, sans inverser implicitement
le rôle de dsar-response. Les modes non adaptés restent explicitement hors
périmètre ; aucun appel à une branche héritée ne les rend disponibles.

## Stories et dépendances métier

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [PRV-001](suites/prv-001-preparer-demande-acces.md) | Préparer une demande d'accès pour un particulier | Aucune |
| [PRV-002](suites/prv-002-qualifier-demande-droits.md) | Qualifier une demande de droits et son calendrier côté organisme | Aucune |
| [PRV-003](suites/prv-003-projet-reponse-acces.md) | Préparer la réponse à une demande d'accès | PRV-002 |
| [PRV-004](suites/prv-004-projet-reponse-effacement.md) | Préparer la réponse à une demande d'effacement | PRV-002 |
| [PRV-005](suites/prv-005-projet-reponse-rectification.md) | Préparer la réponse à une demande de rectification | PRV-002 |
| [PRV-006](suites/prv-006-projet-reponse-portabilite.md) | Préparer la réponse à une demande de portabilité | PRV-002 |
| [PRV-007](suites/prv-007-projet-reponse-opposition.md) | Préparer la réponse à une opposition au traitement | PRV-002 |
| [PRV-008](suites/prv-008-projet-reponse-limitation.md) | Préparer la réponse à une demande de limitation | PRV-002 |
| [PRV-009](suites/prv-009-qualifier-traitement.md) | Établir la fiche de qualification d'un traitement | Aucune |
| [PRV-010](suites/prv-010-necessite-aipd.md) | Motiver la nécessité ou non d'une AIPD | PRV-009 |
| [PRV-011](suites/prv-011-projet-aipd.md) | Préparer un projet d'AIPD sur un traitement qualifié | PRV-010 |
| [PRV-012](suites/prv-012-dossier-consultation-prealable.md) | Préparer les pièces d'une éventuelle consultation préalable CNIL | PRV-011 |
| [PRV-013](suites/prv-013-qualifier-roles-contrat.md) | Qualifier les rôles sur les opérations d'un contrat | Aucune |
| [PRV-014](suites/prv-014-revue-sous-traitance.md) | Revoir un accord de sous-traitance et ses annexes | PRV-013 |
| [PRV-015](suites/prv-015-qualifier-transfert.md) | Qualifier un flux hors EEE et ses justificatifs | PRV-013 |
| [PRV-016](suites/prv-016-ecarts-changement-normatif.md) | Comparer un changement normatif privacy à des pratiques documentées | Aucune |
| [PRV-017](suites/prv-017-ecart-notice-pratique.md) | Comparer une pratique à ses supports d'information | Aucune |
| [PRV-018](suites/prv-018-rapport-derive-documentaire.md) | Produire un rapport de dérive sur un corpus de sorties délimité | PRV-017 |
| [PRV-019](suites/prv-019-preferences-donnees.md) | Créer ou ajuster des préférences privacy volontaires | Aucune |
| [PRV-020](suites/prv-020-dossier-donnees.md) | Isoler et archiver un dossier de protection des données | Aucune |
| [PRV-021](suites/prv-021-checklist-actualite.md) | Remplacer la veille héritée par une checklist France/UE traçable | Aucune |

PRV-002 possède la référence `references/exercice-droits.md` et le contrat
versionné de fiche/journal (demande, rôle, dates et preuves, systèmes, états).
PRV-003 à PRV-008 possèdent leurs références de droit précises, sans réécrire
le calendrier commun. PRV-009 possède la fiche traitement, PRV-010 le test AIPD,
PRV-011 les risques/mesures et PRV-013 la qualification contractuelle des rôles.
Un instantané manuel avec ces champs peut être fourni : pas de fichier
persistant obligatoire. Aucun schéma absent n'est chargé à l'exécution.

PRV-014 conserve une section transfert « à instruire » si PRV-015 n'est
pas disponible ; il ne prononce pas conformité complète. PRV-011 signale les
limites d'un flux non instruit. PRV-018 n'est pas un registre général de
conformité : il suit seulement la couverture des pièces et leur dérive.
Les références à créer ne sont pas une bibliothèque à rédiger en avance.

## Plan de recherche ciblé pour les futures implémentations

Les lignes suivantes sont des **questions et sources à vérifier**, pas des
règles ni des délais validés par ce cadrage. Rechercher le passage exact,
sa version à la date des faits, les transitions et son champ ; distinguer
texte, décision, lignes directrices et outil pratique. EUR-Lex/JOUE,
Légifrance/JO, CNIL, CEPD et CURIA/juridictions officielles sont les entrées
prévues, avec les voies BASE-010 si l'accès direct échoue.

| Sujet | Faits/pièces et recherches attendues | Propriétaire |
|---|---|---|
| Champ et acteurs | Établissements, personnes, territoire précis dont outre-mer si pertinent, activité privée/publique, finalités/moyens réels ; RGPD et loi Informatique et Libertés (LIL), décret d'application, doctrine CNIL/CEPD et jurisprudence. Ni localisation du serveur ni langue ni profil ne suffisent. | PRV-002/009/013 |
| Exercice des droits | RGPD, LIL, lignes directrices CNIL/CEPD et arrêts utiles sur copie, destinataires, tiers, motifs d'exception et modalités ; demande directe/mandataire/mineur, identité proportionnée et canal sûr. | PRV-001 à PRV-008 |
| Calendriers | Délai propre au droit/régime, réception attestée, événement de départ, unité, calcul de mois, jours de fin, éventuelle information/extension, effet exact d'une demande d'identité et preuve ; SLA et objectif interne distincts. Ne pas transformer 1 mois en 30 jours ou suspendre sans source. | PRV-002 puis chaque réponse ; PRV-021 indexe les vérifications |
| Qualification du traitement | Finalité par finalité, base à rechercher, minimisation, source, durée, destinataires, sécurité, registre et DPO selon conditions ; pas d'exemption automatique petite association/TPE. | PRV-009 |
| Données sensibles et secteurs | Santé, génétique, biométrie, infractions, NIR, vulnérabilité/mineurs : catégories et régimes distincts ; RGPD/LIL, dispositions françaises ciblées. Pour santé : Code de la santé publique, secret, hébergement et référentiels CNIL pertinents selon activité ; HDS ne suffit pas à conclure. Pour emploi/éducation/banque : textes sectoriels seulement après qualification. | PRV-009/010/011/013/014 |
| Nécessité et contenu AIPD | RGPD, listes CNIL d'obligation/exemption dans leur version/champ, critères CEPD, jurisprudence utile ; méthode CNIL comme outil distinct du texte. Décrire nécessité/proportionnalité, risques pour les personnes, mesures vérifiées/prévues, avis DPO et participation lorsque pertinente. | PRV-010/011 |
| Risque résiduel et consultation | RGPD et procédure CNIL, responsable compétent, avis, pièces, risque restant malgré mesures ; ne pas confondre transmission systématique d'AIPD, consultation et autorisation de tout traitement. Calendrier propre à l'autorité recherché séparément. | PRV-012 |
| Rôles et sous-traitance | RGPD et lignes directrices CEPD/CNIL : responsable, sous-traitant, sous-traitant ultérieur, responsables conjoints ou autonomes ; contenu contractuel et réalité, instructions, assistance, sécurité, audits, fin du contrat et délais selon destinataire. | PRV-013/014 |
| Transferts | Pays, exportateur/importateur, rôle, accès distant, flux ultérieur, opérations et garanties ; RGPD, décisions Commission et CCT/modules applicables à rechercher sur EUR-Lex, orientations CEPD et arrêts CJUE. Statut de toute adéquation/DPF à relire ; TIA absent = point ouvert. Un hébergement UE ne prouve pas absence de transfert. | PRV-015 |
| Information, traceurs et prospection | RGPD/LIL, règles françaises et européennes pertinentes, CNIL, jurisprudence ; collecte directe/indirecte, version notice, preuve des choix. Distinguer information, consentement, opposition, traceurs et communication commerciale. Une notice ne rend pas un traitement licite à elle seule. | PRV-007/009/017/018 |
| Changement normatif et statut | Texte original/modificatif, date d'application/transitions, portée d'une sanction ou ligne directrice, preuve de pratique ; ne pas attendre une date d'enforcement étrangère ni traiter une amende théorique comme dommage certain. | PRV-016/021 |
| Confidentialité et destinataires | Auteur, qualité, contexte, secret applicable et destinataire réel ; textes et jurisprudence France/UE à rechercher. Aucun attorney work product ou protection automatique par label. Minimiser toute copie de demande/PIA santé dans les logs, tableaux et relais. | Chaque tranche, PRV-019/020 pour le profil |

## Frontières et exclusions

Privacy reste propriétaire des droits relatifs aux données et de la
qualification du traitement. L'accès au dossier médical et les recours de
soins se coordonnent avec DOM-009 ; une demande RGPD n'est pas assimilée
à toute procédure d'accès sectorielle. L'accès au compte, sa suspension et
la modération gardent DOM-034. L'exercice de droits d'un salarié ne résout
pas un litige de rupture. Commercial porte le contrat principal ; corporate
la diligence d'opération ; IA et produit leurs analyses respectives.

La fiche PRV-002 qualifie aussi demandes combinées, retrait de consentement,
décision automatisée et droits propres LIL (dont contexte de décès à
rechercher). Seuls les parcours bornés ci-dessus sont promis : pour un droit
non encore adapté, produire questions/pièces/interlocuteur, sans importer
un opt-out US ni exécuter une branche héritée. Une violation suspectée donne
lieu à collecte minimale des faits et orientation urgente adaptée ; aucune
notification, effacement, accès à un SI, plainte CNIL, recours, signature,
transmission ou publication n'est implémenté par ces propositions.

Le test des traceurs, l'audit technique, la TIA complète, un registre art. 30
complet et un programme sectoriel entier restent à découper avant mise en
œuvre. Aucun abonnement juridique ni scheduler n'est un prérequis de lecture.
