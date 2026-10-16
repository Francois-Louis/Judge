# Données personnelles — Frictions utilisateur et réponses à prévoir

Demande du **16 octobre 2026** : « voici les frictions des utilisateurs auxquelles il faut pouvoir répondre ». Le [texte fourni](sources/donnees-personnelles-frictions-2026-10-16.txt) est archivé sans modification. La matrice reprend ses **60 points**, dans leur ordre, et ses sections pratiques.

**État : exigences de backlog.** PRV-001 et PRV-022 à PRV-034 décrivent les parcours du demandeur ; PRV-002 à PRV-008 gardent la réponse côté organisme. Les treize nouvelles propositions complètent le [découpage](exist-003-decoupage-donnees.md). Les secteurs encore au stade de cadrage restent à découper. Ce travail ne sélectionne pas de tranche d'implémentation.

## Statut du texte fourni

La date, les statistiques attribuées au rapport CNIL 2025, les sanctions évoquées et les règles du texte sont des assertions de la source utilisateur. Les favicons et mentions « +1 » ne donnent pas accès aux passages invoqués. Aucun chiffre ni règle de droit n'est validé par cette intégration documentaire. Les liens identifiables restent des pistes de recherche.

Avant implémentation, vérifier notamment la réforme du démarchage téléphonique annoncée au 11 août 2026 et ses exceptions, les cookies « pay or consent », les droits sur les données utilisées pour l'IA, les procédures de non-diffusion/occultation des registres, les décisions automatisées et les régimes d'accès sectoriels. Les durées de conservation, délais RGPD, délais médicaux et notifications de violation doivent être recherchés séparément : texte/version, champ, déclencheur, destinataire, transitions et preuve. Les recommandations CNIL ne deviennent pas des durées légales universelles.

## Répartition des tâches

- **Demandes du particulier** : PRV-001 pour l'accès ; PRV-022 pour la rectification ; PRV-023 pour l'opposition ou le retrait du consentement à une prospection déterminée ; PRV-024 pour l'effacement ; PRV-025 pour la limitation. Chaque parcours reste utilisable sans compte professionnel, connecteur ou exécution d'une autre story.
- **Comprendre les faits** : PRV-026 reconstitue une collecte/réutilisation ; PRV-027 documente un parcours de traceurs ; PRV-030 prépare les questions sur un dispositif de surveillance ; PRV-031 vise une décision présentée comme automatisée ; PRV-032 lit une notification de fuite du point de vue de la victime.
- **Publication et recours** : PRV-028 prépare le retrait auprès d'une source ; PRV-029 prépare une demande distincte de déréférencement ; PRV-033 compare une réponse à la demande initiale ; PRV-034 prépare les pièces d'une plainte CNIL. DOM-035 et EXIST-006 gardent dommage et procédure juridictionnelle ; DOM-002 garde la plainte pénale. Le recours contre une décision de l'autorité relève du régime à cadrer dans DOM-010.
- **Secteurs** : banque, assurance, logement, santé, emploi privé/public, plateformes et registres gardent le litige ou la procédure propre à leur domaine. Leur relais n'est pas une dépendance d'installation. Chaque fiche transmet seulement les faits, pièces, dates et questions utiles.

## Matrice des 60 points

Le premier propriétaire porte la tâche de données décrite ; le relais porte une demande distincte. Un cadrage attribué ne constitue pas une fonctionnalité disponible. Les noms courts PRV renvoient aux stories du tableau de découpage.

| N° | Friction | Propriétaire et relais | Résultat attendu |
|---|---|---|---|
| 1 | Case de consentement précochée | PRV-026 ; PRV-023 | Relever écran, état initial et choix ; demander la preuve et préparer l'opposition ou le retrait adapté. |
| 2 | Consentement noyé dans les CGV/CGU | PRV-026 ; PRV-023, contrat au domaine concerné | Distinguer acceptation du contrat et finalités commerciales, sans présumer que tout traitement exige un consentement. |
| 3 | Coordonnées de jeu-concours revendues | PRV-026 ; PRV-001 | Reconstituer organisateur, collecte, source et destinataires connus ; préparer les questions manquantes. |
| 4 | Partenaires non identifiés | PRV-001 ; PRV-026 | Cibler la demande d'informations sur les transmissions et les destinataires, sans inventer une liste. |
| 5 | Transmission en cascade | PRV-026 ; PRV-023 | Dresser une chaîne avec preuves/inconnues et une demande distincte pour chaque responsable identifié. |
| 6 | Démarchage après devis | PRV-026 ; PRV-023, DOM-001 si litige de consommation | Séparer exécution du devis et réutilisation commerciale ; vérifier le rôle du comparateur et du destinataire. |
| 7 | Adresse professionnelle utilisée pour toute prospection | PRV-026 ; PRV-023 | Qualifier destinataire, canal, objet et lien professionnel avant de choisir la règle à rechercher. |
| 8 | Ancien consentement étendu à de nouveaux usages | PRV-026 ; PRV-023 | Comparer finalités, versions et preuve du choix initial, puis demander le fondement du nouvel usage. |
| 9 | Prospection après désinscription | PRV-023 ; PRV-034 | Relier opposition, réception et messages postérieurs ; préparer la demande ou le dossier de plainte selon les faits. |
| 10 | Désinscription exigeant de nouvelles données | PRV-023 ; PRV-033 | Décrire l'obstacle et proposer un canal approprié ; vérifier la proportionnalité des informations demandées. |
| 11 | Réapparition dans les fichiers | PRV-023 ; PRV-026 | Identifier réimport/source ; distinguer effacement commercial et conservation minimale d'une opposition à vérifier. |
| 12 | Publicité présentée comme message de service | PRV-026 ; PRV-023 | Examiner contenu et contexte du message, en séparant les composantes de service et commerciales. |
| 13 | Refus des cookies dissimulé | PRV-027 ; PRV-034 | Comparer les parcours visibles et conserver les écrans successifs avant de qualifier le choix. |
| 14 | Traceurs déposés avant choix | PRV-027 | Dater l'observation et son contexte ; séparer observation technique fournie, déduction et point non vérifié. |
| 15 | Refus des traceurs ignoré | PRV-027 | Comparer état avant/après et choix prouvé ; indiquer ce que les pièces permettent réellement d'affirmer. |
| 16 | Traceurs publicitaires dits nécessaires | PRV-027 ; PRV-026 | Relever finalités et explication de l'exemption invoquée ; garder la qualification ouverte sans éléments suffisants. |
| 17 | Retrait du consentement introuvable | PRV-027 | Documenter l'accès aux réglages et le parcours de retrait ; préparer une demande ciblée au site. |
| 18 | Payer ou accepter le suivi | PRV-027 | Décrire alternatives, prix, accès et choix ; rechercher les critères applicables sans verdict automatique. |
| 19 | Traceurs tiers invisibles | PRV-026 ; PRV-027, PRV-001 | Identifier seulement les destinataires documentés et préparer l'accès aux informations manquantes. |
| 20 | Profil de navigation intersites | PRV-026 ; PRV-001/023 | Décrire sources et rapprochements allégués ; cibler accès et opposition sans promettre l'arrêt universel du suivi. |
| 21 | Compte obligatoire enrichissant le profil publicitaire | PRV-026 ; PRV-023, DOM-034 pour accès au service | Distinguer nécessité du compte et finalités secondaires ; proposer la demande propre à chaque traitement. |
| 22 | Permissions mobiles excessives | PRV-026 | Associer permission, fonctionnalité et finalité déclarée ; distinguer autorisation du système et base juridique. |
| 23 | Géolocalisation permanente | PRV-026 ; PRV-001/025 | Relever réglages, périodes, conservation et usages ; préparer accès ou limitation selon l'objectif. |
| 24 | Aspiration de données publiques | PRV-026 ; PRV-001/023/024 | Identifier source publique, réutilisateur et finalité ; ne pas déduire la libre réutilisation de la seule publicité. |
| 25 | Profilage par rapprochement de sources | PRV-001 ; PRV-026/031 | Demander les données déduites et informations pertinentes ; distinguer profilage et décision automatisée. |
| 26 | Données gardées après fermeture de compte | PRV-024 ; PRV-028 pour copies publiées | Distinguer fermeture, effacement, archives et copies tierces ; cibler les données et destinataires de chaque demande. |
| 27 | Suppression confondue avec déréférencement | PRV-028 et PRV-029, sorties séparées | Préparer une demande à la source et une autre au moteur, avec URL et effets recherchés distincts. |
| 28 | Anciennes informations préjudiciables republiées | PRV-028/029 ; DOM-043 si expression/presse | Conserver contexte, date et nouvelles URL ; rechercher les arbitrages de droits sans garantir un retrait. |
| 29 | Adresse personnelle diffusée dans un annuaire professionnel | DOM-039 pour EI, SOC-023/024 pour société ; PRV-028 pour copie privée | Identifier registre, acte, diffusion et annuaire ; préparer des demandes distinctes sans promettre la disparition des copies. |
| 30 | Contenus privés republiés | PRV-028 ; DOM-034, DOM-043, DOM-002 selon demande | Conserver URL/captures minimales et audience ; distinguer droits sur les données, image, plateforme et infraction alléguée. |
| 31 | Contenus personnels réutilisés pour entraîner une IA | PRV-026 ; PRV-001/024 selon droit, opposition hors prospection à découper ; EXIST-005 si gouvernance IA | Identifier responsable, finalité, provenance et droits à rechercher ; aucune interdiction générale ou suppression du modèle promise. |
| 32 | Notes de recrutement dissimulées | PRV-001 ; travail privé ou DOM-037 selon statut | Cibler données, appréciations et période ; examiner les droits des tiers sans exiger le dossier complet sans distinction. |
| 33 | CV refusé conservé indéfiniment | PRV-024 ; travail privé ou DOM-037 | Demander durée, dernier contact et finalités ; vérifier les références de conservation et leurs conditions. |
| 34 | Caméra contrôlant constamment le poste | PRV-030 ; travail privé/DOM-037 à découper | Fiche dispositif/finalité/périodes et demande de préservation ciblée ; recours professionnel séparé. |
| 35 | Enregistrements réutilisés pour évaluer le personnel | PRV-030 ; PRV-001 et domaine emploi | Comparer information, finalité réelle alléguée, accès et conservation ; ne pas déduire la licéité de l'information seule. |
| 36 | Géolocalisation hors temps de travail | PRV-030 ; domaine emploi | Identifier horaires, usage privé et désactivation ; préparer les questions de nécessité et proportionnalité. |
| 37 | Surveillance intrusive du télétravail | PRV-030 ; TRAV-012 pour charte, contestation à découper | Décrire dispositif et fréquence sur pièces ; séparer lecture de surveillance et rédaction d'une charte. |
| 38 | Dossier RH consulté sans nécessité | PRV-001/025 ; PRV-034, domaine emploi | Demander vérification des accès et restriction adaptée sans exiger automatiquement l'identité de tout agent. |
| 39 | Usage détourné de la messagerie professionnelle | PRV-030 ; domaine emploi | Recueillir charte, finalités et nature des échanges ; éviter toute collecte de conversations tierces inutiles. |
| 40 | Données erronées servant à une sanction | PRV-022/025 ; domaine emploi à découper | Tableau erreur/preuve/correction et limitation éventuelle ; repérer la contestation disciplinaire et son calendrier propre. |
| 41 | Crédit refusé sur score opaque | PRV-031 ; DOM-004 pour contestation du refus, à découper | Demander informations pertinentes et examen humain si applicable ; ne pas promettre l'octroi ni l'accès au code source. |
| 42 | Incident bancaire ancien ou erroné | BNK-010 ; PRV-022 pour données hors procédure spéciale | Identifier fichier, déclarant, dates et justificatifs ; garder la procédure de fichier et le score interne distincts. |
| 43 | Justificatifs financiers disproportionnés | PRV-026 ; domaine bancaire/assurance pour vérifications obligatoires | Rapprocher pièce, finalité et obligation invoquée ; examiner les masquages possibles sans gêner une vérification requise. |
| 44 | Dossier locatif trop intrusif ou conservé | DOM-006 à découper ; PRV-024/026 | Séparer liste de justificatifs autorisés, sécurisation et sort d'un dossier refusé. |
| 45 | Données médicales transmises sans justification | PRV-026 ; PRV-001/025, DOM-007 et DOM-005 | Identifier catégories, destinataires et justification alléguée ; limiter les pièces de santé partagées. |
| 46 | Consultation injustifiée du dossier patient | PRV-001/025/034 ; DOM-007 | Préparer demande au DPO de vérification des accès, faits et mesures ; distinguer soupçon et accès établi. |
| 47 | Dossier médical communiqué tardivement | DOM-007 à découper ; PRV-033 seulement pour volet RGPD distinct | Qualifier demandeur, informations et ancienneté ; rechercher le régime sectoriel avant tout calendrier. |
| 48 | Fuite minimisée | PRV-032 | Lire l'avis, distinguer données confirmées et inconnues ; préparer les questions et mesures adaptées à la victime. |
| 49 | Information de fuite tardive ou insuffisante | PRV-032 ; PRV-034 | Reconstituer dates connues et contenu ; distinguer obligations envers l'autorité et envers les personnes. |
| 50 | Documents sensibles transmis sans protection adaptée | PRV-032 si incident ; PRV-026 sinon | Décrire exposition, accès et destinataires ; proposer un canal sûr sans qualifier toute messagerie d'illicite. |
| 51 | Prestataire invoqué pour écarter la demande | PRV-032 ; PRV-026/033 | Identifier responsable, sous-traitant et contact utile ; éviter une réclamation dirigée seulement vers le prestataire technique. |
| 52 | Fraude utilisant les données divulguées | PRV-032 ; BNK-001 et CRIM-004 | Donner priorité aux canaux officiels du prestataire et aux preuves, puis séparer réclamation bancaire et plainte pénale. |
| 53 | Conservation excessive aggravant une fuite | PRV-032 puis PRV-024 | Distinguer mesures urgentes, préservation utile et effacement ciblé ; demander la justification des archives. |
| 54 | Réponse d'accès négative apparemment incomplète | PRV-033 ; PRV-001 | Comparer la demande, la réponse et les indices de traitements omis ; préparer une relance circonstanciée. |
| 55 | Compte client ou pièce d'identité systématiquement imposés | PRV-033 ; droit demandé PRV-001/022 à 025 | Décrire l'obstacle, le canal et le doute d'identité invoqué ; rechercher une vérification proportionnée. |
| 56 | Politique générale fournie comme réponse à l'accès | PRV-033 | Tableau des questions répondues/manquantes et brouillon demandant les données et informations personnelles pertinentes. |
| 57 | Obligation de tout supprimer ou de tout garder invoquée | PRV-024/025 ; PRV-033 | Ventiler finalités, conservation active/archives et motifs ; examiner une limitation sans promettre un effacement universel. |
| 58 | Export de portabilité présenté comme accès complet | PRV-001/033 | Distinguer périmètre de l'export et demande d'accès ; cibler les catégories absentes sans les présumer détenues. |
| 59 | Plainte CNIL prise pour une indemnisation | PRV-034 ; DOM-035 et EXIST-006 | Dossier de plainte distinct de dommage, causalité, chiffrage et voie juridictionnelle à qualifier. |
| 60 | Attente RGPD laissant expirer un autre recours | PRV-033/034 ; domaine de la décision, CTX-016 si procédure dans son champ | Deux calendriers indépendants avec sources et inconnues ; ne jamais déduire une suspension du seul dépôt RGPD. |

## Sections pratiques à reprendre dans les futures sorties

| Partie de la source | Exigence de sortie | Propriétaire |
|---|---|---|
| Plaintes et statistiques | Ne pas transformer une répartition sectorielle en fréquence d'infraction ou en preuve d'abus dans le dossier. | Toutes les tranches |
| Encadré démarchage téléphonique | Qualifier date, canal, nature commerciale, qualité du destinataire, contrat et exceptions avant de rechercher la règle applicable. Séparer opposition données et signalement commercial. | PRV-023/026 ; DOM-001 |
| Tableau des délais | Fiche avec règle sourcée, version, champ, événement et date prouvée, unité, échéance calculable ou manquante, éventuelle prolongation motivée ; distinguer obligation et recommandation. | Chaque tranche ; DOM-007 pour accès médical |
| Étape 1 : preuves | Préserver les pièces utiles avant effacement ; URL, captures, en-têtes, avis, réponse et preuve de réception. Demander la préservation d'images ciblées sans annoncer qu'elle est obtenue. | PRV-024/025/027/028/030/032 |
| Étape 2 : responsables | Fiche source → transmission → exploitation, en séparant acteurs établis et supposés ; demande différente par responsable et finalité. | PRV-026 ; chaque demande |
| Étape 3 : demande traçable | Brouillon limité au droit choisi, interlocuteur/canal à vérifier, pièces minimales, champs manquants et preuve d'envoi à conserver. | PRV-001/022 à 025/029/031 |
| Étape 4 : suivi | Comparer demande, réception, réponse et prolongation ; préparer une relance ou le dossier CNIL selon le calendrier vérifié. | PRV-033/034 |
| Étape 5 : conséquences | Fiche de relais pour décision professionnelle/bancaire, usurpation, dommage ou accès médical, avec échéances propres. | Secteur, DOM-002/035, EXIST-006 |
| Où agir ? | Vérifier canal officiel et champ : CNIL, SignalConso, 33700, Cybermalveillance, banque/Banque de France, registre/INSEE selon la question. FICOBA ne devient pas un accès bancaire effectué ni une preuve d'absence d'usurpation. | PRV-032/034 ; BNK-010, DOM-039 |
| Trois erreurs finales | Conserver avant suppression, examiner accès et limitation, traiter le dommage et les autres recours avec leurs calendriers. | Toutes les tranches concernées |

## Scénarios de recette à conserver

Scénarios et résultats **attendus**, à exécuter dans les lots d'implémentation :

1. Jeu-concours suivi de trois annonceurs : chaîne partielle et trois contacts distincts ; aucun destinataire inventé (3–5).
2. Opposition puis réimport d'une liste : messages datés, source à demander, conservation minimale de l'opposition à rechercher (9–11).
3. Appel commercial dont la date est proche de la réforme alléguée : branches datées et exceptions à rechercher (encadré).
4. Bannière avec captures, sans relevé technique : parcours documenté, aucun dépôt de traceur affirmé ; « payer ou consentir » examiné au cas par cas (13–18).
5. Adresse d'EI reprise par deux annuaires : demandes registre/copies privées séparées (29).
6. Texte personnel prétendument utilisé par une IA : provenance et responsable à identifier, absence de garantie de retrait du modèle (31).
7. Caméra dont les images peuvent disparaître : demande ciblée de préservation et accès, puis surveillance et contestation professionnelle distinctes (34–40).
8. Refus de crédit et fiche d'incident contestée : score/examen humain et procédure de fichier séparés, sans crédit promis (41–42).
9. Dossier médical mêlant accès et soupçon de consultation : deux objets, calendriers sectoriel/RGPD à vérifier, collecte minimale (46–47).
10. Fuite suivie d'un faux conseiller : canal officiel et mesures de protection en tête, dossiers données/banque/pénal distincts (48–53).
11. Export incomplet et demande d'identité : tableau des manques, justification d'identité et preuve de réception sans prolongation inventée (54–58).
12. Demande de dommages avec contestation proche : pièces CNIL et relais juridictionnel séparés, calendrier de fond conservé indépendamment de la demande RGPD (59–60).

## Portée et suivi

Intégration documentaire des besoins ; contrôles et limites dans le [relevé dédié](exist-003-frictions-verification.md). Les scénarios ci-dessus restent à exécuter. L'archive utilisateur n'est pas un corpus juridique validé ni une référence d'exécution des futurs plugins. Les preuves historiques d'EXIST-003 restent inchangées.
