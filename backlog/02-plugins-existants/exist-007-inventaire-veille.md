# EXIST-007 — Inventaire de la veille réglementaire

Relevé du **16 octobre 2026** : **26 fichiers dont 9 skills**, fichiers cachés
inclus, et **6 fichiers de cookbook associé**. Le catalogue comporte **59 lignes
de sources**, dont dix lignes de rappel dans la section sans flux ; ce décompte
n'est pas celui de 59 services distincts disponibles.

Les [sources et sondages](exist-007-sources.json) conservent chaque ligne,
section, URL/méthode, format, authentification, couverture et notes **déclarés**,
sa décision et son statut ; les [empreintes](exist-007-resultats.json) contrôlent
le périmètre. Le [découpage VEI-001 à VEI-020](exist-007-decoupage-veille.md)
décrit les suites, sans modifier les contenus hérités.

## Les neuf skills

Chemins relatifs à `regulatory-legal/skills/`. Les neuf entrées chargent
`references/isolation.md`. Profils, trackers, politique et sorties utilisateur
sont distincts des modèles livrés dans le paquet. Chaque future tranche charge
méthode BASE-005 locale et références métier, sans dépendance au checkout.

| Fichier | Contenu et dépendances | Décision individuelle motivée |
|---|---|---|
| `reg-feed-watcher/SKILL.md` | Profil/watchlist/seuil, catalogue local, Federal Register/RSS/MCP/paste, classement, date effective/commentaire, trackers, curseur et digest fichier. | Conserver entrée manuelle et provenance, réécrire VEI-001 qualification, VEI-003 collecte RSS bornée, VEI-005 temps, VEI-013 consultation et VEI-016 digest. Retirer Federal Register toujours actif ou repli vide, final rule = matériel/obligation, source riche remplaçant primaire, avance globale du curseur après échec et all-clear sans couverture. Un résumé fourni n'est pas le texte normatif. Seuil de lecture interne ne prouve pas applicabilité. |
| `policy-diff/SKILL.md` | Profil/index, texte/summary, statut du rule, grille requirement/effective, rapprochement policies, diff, no-match, pre-rule ANPR/RFI et relais gap-surfacer. | VEI-004 possède preuve de modification, VEI-007 champ/applicabilité ciblés et VEI-008 écart documentaire. Conserver citations et exclusions visibles ; vérifier statut à chaque analyse et non seulement après 12 mois/30 jours ou règle politiquement sensible. Retirer NPRM traité comme exigence, bibliothèque vide = toutes politiques manquantes, exclusion = absence et no-gap = conformité. Texte antérieur/postérieur et activité réelle requis avant obligation nouvelle affirmée. |
| `policy-redraft/SKILL.md` | Gap, texte actuel approuvé, règle, statut, redline minimale, modèle memo, nouveau fichier, critères de clôture et severity floor. | Conserver un écart/une politique/proposition séparée, VEI-009. Réécrire exemple COPPA/dates US, fichier cwd et renvois Federal Register, garanties de protection par header et vérification depuis connecteur seulement connecté. Version approuvée déclarée et version effectivement lue distinctes. Préserver gravité ou expliquer révision ; ne pas conclure conformité après texte approuvé sans preuve de pratique. |
| `gap-surfacer/SKILL.md` | Référence `user-invocable:false`, framework pour gaps/comments, schéma inline riche, ingest, statuts, watch/comment-decision, Slack et rappels. | Conserver référence interne, VEI-010 ingestion, VEI-011 rapport et VEI-012 décision de suivi. Réconcilier schéma inline/modèles et échéances juridiques/internes/de revue. Retirer notifications on-by-default, disparition des risk-accepted du risque visible et clos = conformité. Le texte dit ne pas lire comment-tracker : garder ce registre distinct ; ne pas dupliquer consultation en compliance gap. Aucun envoi réel dans ces tranches. |
| `gaps/SKILL.md` | Façade vers gap-surfacer, gap-tracker, close/accept et rapport par âge/matérialité. | Conserver point d'entrée mince qui charge la référence locale, VEI-011/012. Distinguer clôture de tâche, preuve d'exécution et conclusion juridique ; choix interne d'accepter un risque ne légalise pas une pratique. État/échéance inconnus ne deviennent ni overdue ni compliant. |
| `comments/SKILL.md` | comment-tracker, décisions filing/not-filing/waived/filed, délai/compte à rebours, Slack DM/rappels et gate non-lawyer, cadre partagé. | Réécrire VEI-013 qualification d'une consultation, VEI-014 décision/suivi ; nom technique conservé, intitulé visible futur « Suivi des consultations ». Retirer NPRM universel, avocat requis pour simplement consigner intention, décision filing = dépôt et conséquences déclarées identiques de toute participation. Ne pas confondre consultation publique, demande d'information individuelle d'autorité et procédure de contrôle. VEI-015 seul crée un brouillon de contribution borné, jamais déposé. |
| `cold-start-interview/SKILL.md` | Entretien quick/full, profil commun/local, outils déclarés, watchlist, index, seuils, cadence, trackers et modèles inline. | Conserver préférences explicites, reprise et helper, VEI-017. Ajouter petite structure/association/particulier ; retirer profil professionnel nécessaire pour qualifier un document, Federal Register toujours disponible, seuil/cadence par défaut présentés comme couverture et header protecteur. Collecte, analyse, abonnement et authentification restent distincts ; ne configurer que capacités nécessaires. |
| `customize/SKILL.md` | Carte profil/sections, source/seuil/index/cadence, company profile, écriture ciblée et effets annoncés. | Conserver mise à jour ciblée VEI-017 ; retirer promesses « ajout autorité = sweep prochain », « skip reste searchable » sans archive ni collecteur, stage partagé inventé et régulateur qu'on ne pourrait jamais retirer. Retrait de watchlist conserve historique sourcé et fin de couverture visible ; préférence ne change ni droit ni preuve. |
| `matter-workspace/SKILL.md` | new/list/switch/close/none, actif profil, matter/history/notes/outputs, overrides, archives et cross-matter. | Conserver cloisonnement VEI-018, y compris organisme avec plusieurs usages et sans cabinet. Réécrire exemples MSA/NDA/Delaware et types de dossiers par texte/version/activité/consultation. Résoudre ambiguïté slug réutilisable/refusé, archive distincte d'effacement et header protecteur. Related matters ne donne pas droit aux pièces ; liste de métadonnées minimale, aucun déplacement hors racine. |

## Les dix-sept autres fichiers du plugin

Chemins relatifs à `regulatory-legal/`. Ces dix-sept lignes et les neuf skills
couvrent exactement les 26 fichiers du paquet.

| Fichier | Décision individuelle motivée |
|---|---|
| `skills/reg-feed-watcher/references/source-catalog.md` | Réécrire VEI-002 : 15 lignes US fédérales, 11 États US, 10 UE/UK, 3 internationales, 10 secondaires et 10 rappels sans flux. Retirer « URLs verified May 2026 » comme preuve actuelle et starter packs US par défaut. Distinguer page d'accueil, catalogue, endpoint RSS/Atom, API, archives XML et email. URL CNIL observée ne certifie pas tous contenus/versions ; UK et Conseil de l'Europe distincts d'UE. Détails exhaustifs dans sources.json, aucune ligne supprimée de l'inventaire. |
| `skills/gap-surfacer/references/gap-tracker.yaml` | Modèle `gaps: []`, exemple US et schéma moins riche que l'inline. VEI-010 possède alignement des champs source/version, activité, statut, couverture et types de dates ; ne pas inventer tracker utilisateur depuis modèle ou fermer sur risque accepté. |
| `skills/gap-surfacer/references/comment-tracker.yaml` | **Commentaire HTML initial chargé comme clé YAML parasite** ; exemple CMT-001 et dates figées encore actifs dans la liste. VEI-014 remplace par commentaire YAML et liste vide, schéma/exemple séparés ; vérifie les vrais consommateurs comments et watcher. Aucune consultation fictive livrée comme dossier réel. |
| `CLAUDE.md` | Modèle avec setup STOP, profil, seuils, index, flux, sortie et frontières. Corriger par tranche ; VEI-017 possède préférences, VEI-018 dossiers. Retirer Federal Register gratuit donc toujours disponible, keeper header qui protège, waiver général France/UE, profil avocat comme condition de lecture ponctuelle. Garder citations, fidélité et données tierces non fiables. |
| `README.md` | Annonces de collecte, tracking, politique et calendrier. Distinguer neuf skills réels dont customize omis au tableau, huit invocables et gap-surfacer référence ; pas de connecteur CourtListener/paid feed dans .mcp.json. Réécrire au fil des tranches, aucun domaine France/UE ou automation déclaré livré par ce cadrage. |
| `agents/reg-change-monitor.md` | Profil, watcher, policy-diff automatique sur toujours matériel, post digest, fréquence et droits WebFetch/Slack wildcard. VEI-019 adapte seulement un rapport local après tâches manuelles ; retirer lancement automatique du diff, post, calendrier implicite et all-clear. La gravité de veille n'est pas une obligation applicable. |
| `.mcp.json` | Deux déclarations : Slack et Google Drive. Conserver sans activer ; authentification/droits non testés. Catégorie email ne livre aucun Gmail/Outlook ; pas de paid-feed, CourtListener, scheduler ou index documentaire déjà créé. Lecture manuelle/conversation suffit à la première tranche. |
| `.claude-plugin/plugin.json` | Conserver identité/version 0.1.0 pendant cadrage. Annonces futures limitées aux tranches livrées, version et marketplace synchronisés. |
| `hooks/hooks.json` | Objet hooks vide, conserver : aucun job de veille ni notification réellement branchés. |
| `references/shared/research-citation-method.md` | Conserver copie BASE-005 1.0.0 identique et charger explicitement depuis chaque tranche adaptée. Une étiquette source ne prouve ni lecture ni applicabilité. |
| `references/isolation.md` | Conserver contrat BASE-008 identique, pas d'accès direct hors helper ou import amont. Réponse ponctuelle sans profil dans le futur contrat ; profil durable absent soumis à entretien neuf. |
| `scripts/judge_store.py` | Conserver copie commune identique ; toute évolution transverse exige synchronisation des douze paquets. Aucun curseur, archive ou tracker sous chemin non gardé. |
| `references/company-profile-template.md` | Conserver copie commune ; pays/activité déclarés ne prouvent champ d'un texte ou statut d'opérateur. Pas de société obligatoire pour lire une consultation. |
| `references/dashboard-template.md` | Conserver copie commune/échappement ; VEI-011/016 affichent couverture et dates qualifiées, aucun compteur/coloris ne vaut conformité. |
| `LICENSE` | Conserver Apache-2.0 et attributions. |
| `NOTICE` | Conserver ici ; entrée locale et racine lors de chaque futur lot hors backlog. |
| `.gitignore` | Conserver sans uniformisation ni ajout de données utilisateur dans le paquet. |

## Les six fichiers du cookbook associé

Chemins relatifs à `managed-agent-cookbooks/reg-monitor/`. VEI-020 est une
story distincte après adaptation manuelle et VEI-019, sans déploiement réel.

| Fichier | Décision individuelle motivée |
|---|---|
| `agent.yaml` | Conserver orchestrateur local, feuilles séparées et racine BASE-008. Réécrire imports/append/contrat selon tâches livrées. gdrive déclaré n'est pas accordé via outil MCP dans l'orchestrateur ; handoff Slack ne désigne aucun worker livré. Aucune collecte ou diffusion distante supposée fonctionnelle. |
| `subagents/feed-reader.yaml` | Conserver schéma borné, données non fiables, egress et refus privé ; réécrire allowlist réelle pour seul RSS français retenu. Liste actuelle *.europa.eu n'autorise ni cnil.fr ni legifrance.gouv.fr. Corriger « URL reçue du MCP » alors que feuille sans MCP et « omettre champ requis » incompatible avec schéma required. Erreur explicite plutôt qu'élément tronqué silencieusement. |
| `subagents/materiality-filter.yaml` | Conserver calcul sur JSON sans réseau/écriture ; réécrire matérialité interne versus nature/statut/qualification juridique. Ne pas perdre source, versions et événements de consultation ; les patterns ASCII sur agency/source doivent accepter les noms français sans déformer identité. |
| `subagents/digest-writer.yaml` | Conserver seul écrivain, échappement et URLs inertes ; retirer work product présumé, all-clear et handoff présumé exécutable. Propager couverture, manques et types temporels ; ne pas charger policy-diff/gap-surfacer pour transformer formatage en analyse nouvelle. |
| `steering-examples.json` | Réécrire exemples FINRA et date figée en fixtures JORF/directive/consultation et erreurs techniques ; aucune règle ou date de conformité déduite du texte d'exemple. |
| `README.md` | Corriger tableau gdrive/orchestrateur selon outils effectifs, Slack worker absent et import-agent contradictoire. Décrire une seule chaîne bornée, dry-run et erreurs, sans déploiement, abonnement ou programmation livrés. |

## Sources, formats et capacités réellement observées

Les [sept sondages HTTP](exist-007-sources.json) portent URL tentée/finale,
horodatage UTC réel, état, taille, empreinte, format et absence de credentials.
Rejouables avec [exist-007-sondages.py](exist-007-sondages.py). Il s'agit de
sondages techniques ponctuels, pas d'une lecture normative ou d'une certification
de disponibilité future. Aucune souscription ou configuration modifiée.

| Source/méthode | Déclaration et observation du 16 octobre 2026 | Décision |
|---|---|---|
| CNIL anglais du catalogue et candidat français | Les deux endpoints `/en/rss.xml` et `/fr/rss.xml` répondent HTTP 200, `application/rss+xml`, racine rss, dix items chacun, sans compte fourni. Le navigateur web refuse le format RSS ; le parseur HTTP/XML réussit. | Candidats pour VEI-003, sans garantir couverture de toutes décisions/versions ni identité linguistique depuis le seul chemin. |
| JORF DILA | [Répertoire officiel](https://echanges.dila.gouv.fr/OPENDATA/JORF/) HTML 200, liens tar.gz présents ; aucune archive téléchargée ici. | Piste de collecte d'archives à adapter séparément si choisie ; ni RSS fonctionnel ni recherche exhaustive de JORF. Première tranche accepte document fourni. |
| EUR-Lex accueil, aide RSS et webservice | HTTP direct : 202 vide sur les trois URL. Outil web : challenge JavaScript sur les aides ; contenu officiel indexé lu par recherche. | Aucun RSS EUR-Lex personnel ni SOAP authentifié exécuté. La [documentation webservice](https://eur-lex.europa.eu/content/help/data-reuse/webservice.html?locale=en) distingue SOAP/XML après inscription/autorisation et téléchargement de fichiers via CELLAR ; les [alertes RSS personnalisées](https://eur-lex.europa.eu/content/help/my-eurlex/my-rss-feeds.html?locale=en) demandent compte connecté. Vérifier les endpoints exacts avant configuration. |
| EDPB URL « News » du catalogue | HTML 200, redirection vers `/news_en`, aucun lien RSS/Atom détecté par le sondage limité. | Une page HTML lue ne valide pas deux flux annoncés ; endpoints précis et pagination à vérifier, sans conclure absence de RSS sur tout le site. |
| Autres sources UE/UK/internationales et secondaires | Formats, auth, retraits ou pannes sont des assertions héritées inventoriées ligne par ligne, non testées ici. | Choisir secteur/pays ; autorité, communiqué, guide, décision et texte normatif distincts. UK/CoE hors UE à qualifier ; résumé secondaire reste piste. |
| API PISTE / CELLAR / outils BASE-010 | Accès et limites consignés dans [BASE-010](../../references/legal-source-access.md), pas retestés dans ce lot ; outil du dépôt absent du paquet installé. Souscription PISTE indisponible signalée dans BASE-010. | Aucun besoin d'abonnement imposé ; une future tranche embarque ses accès requis et peut accepter texte fourni. CELLAR pour un identifiant exact n'est pas une veille exhaustive. |
| Email, portail de consultation, bibliothèque, scheduler, Slack/Drive | Catégories/URL ne prouvent ni compte, consentement, worker, index ni abonnement. Aucun accès authentifié testé. | Brouillons locaux et collecte manuelle d'abord ; actions externes et automation hors cadrage. |

## Chaînes de contenu et frontières

| Chaîne | Propriétaire et invariants futurs |
|---|---|
| Source → collecte → événement → version | VEI-002 capacités, VEI-003 collecte d'un RSS, VEI-001 événement manuel, VEI-004 versions. Préserver endpoint, URL canonique, identifiant, corps/version, langue, date de récupération et source initiale même après enrichissement. Une empreinte différente ne prouve pas modification du droit. |
| Événement → temps → transposition → applicabilité | VEI-005 fiche temporelle, VEI-006 directive/pays/mesure nationale, VEI-007 activité/acteur/obligation. Publication, adoption, entrée en vigueur, application différée, transposition, rectificatif et consultation restent événements distincts. |
| Obligation → politique → proposition → exécution | VEI-008 écart documentaire, VEI-009 redraft, VEI-010 registre, VEI-012 décision de suivi. Pas de politique absente déduite d'index vide ; texte conforme ne prouve pas pratique conforme. |
| Consultation → décision → contribution | VEI-013 fiche de consultation, VEI-014 décision attribuée et preuve de dépôt séparée, VEI-015 brouillon. Ne pas traiter invitation comme obligation ou contrôle d'autorité ; contribution non envoyée. |
| Synthèse et automatisation | VEI-016 digest manuel ; VEI-019 agent local après tâches manuelles ; VEI-020 cookbook distinct après ces adaptations. Aucun calendrier, abonnement, message ou déploiement automatique dans ces propositions. |
| Relais métier | Privacy, produit, IA, travail ou secteur analysent leur régime précis ; réglementaire garde collecte/provenance et écart documentaire borné. Litige d'une décision/contrôle individuel → contentieux/administratif/secteur selon acte, pas consultation publique. Fiche autonome si relais adapté absent. |

Les références futures sont marquées « à créer » dans chaque suite. Les pistes
de sources primaires sont des travaux futurs, pas des autorités, délais ou
obligations validés par cet inventaire.
