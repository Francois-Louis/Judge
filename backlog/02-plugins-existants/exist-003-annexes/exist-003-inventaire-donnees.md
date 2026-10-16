# EXIST-003 — Inventaire protection des données

Relevé du **16 octobre 2026** : **23 fichiers, dont 9 skills**, fichiers
cachés inclus, sans agent ni cookbook propre à ce plugin. Le
[relevé machine](exist-003-resultats.json) en donne les empreintes. Les
décisions ci-dessous portent sur les tâches héritées ; elles ne modifient
ni le paquet ni ses identifiants. Voir le [découpage PRV](exist-003-decoupage-donnees.md)
et la [relecture documentaire](exist-003-verification.md).

## Les neuf skills et leurs dépendances

Tous chargent `references/isolation.md`. Les accès durables passent par
`scripts/judge_store.py` sous `config/judge-fr-eu/privacy-legal/` ; le profil
du paquet est un modèle, distinct du profil effectif. Le seul fichier
partagé est `company-profile.md` à la racine de configuration du fork.
La méthode BASE-005 `1.0.0` est embarquée, sans chargement explicite dans
les neuf entrées héritées : chaque tranche adaptée devra la charger.

Les fichiers de sortie, historiques et modèles utilisateur cités dans ce
tableau sont des données futures ou fournies, pas des fichiers livrés.

| Fichier sous `privacy-legal/skills/` | Contenu et dépendances suivis | Décision individuelle et justification |
|---|---|---|
| `dsar-response/SKILL.md` | Profil DSAR/systèmes/SLA, dossier actif, demande et identité, parcours système manuel, exceptions, deux lettres, journal sans schéma ; ne recherche ni n'efface lui-même les données. | Conserver provenance, parcours par système et séparation notes/lettre. Réécrire qualification et calendrier (PRV-002), accès (PRV-003), effacement (PRV-004), rectification (PRV-005), portabilité (PRV-006), opposition (PRV-007), limitation (PRV-008). Retirer opt-out sale/share, 45 jours et deux lettres sous 3–5 jours comme défauts légaux français. Retirer exemption générale des backups et préférence pour sur-invoquer les exceptions. L'identité « pauses the clock (arguably) » contredit le modèle « does not pause » : exiger source et déclencheur. Un journaliste ou demandeur litigant ne perd pas ses droits par son statut. Le parcours particulier absent est créé séparément par PRV-001. |
| `dpa-review/SKILL.md` | Profil, deux playbooks, DPA/MSA/annexes, antécédents triage/PIA/revue, politique publiée ; neuf lignes de revue, redlines et note transferts. | Conserver lecture clause par clause, retouches précises et divergences sourcées. Réécrire qualification des rôles par opération (PRV-013), revue art. 28 à rechercher (PRV-014), transferts (PRV-015). Retirer client = responsable/prestataire = sous-traitant, SOC 2 = preuve suffisante, socle fédéral GLBA/HIPAA/FERPA/COPPA et 60 jours HITECH par défaut. Responsables conjoints ou autonomes ne sont pas forcés dans les deux playbooks. Distinguer notification sous-traitant → responsable, autorité et personnes. |
| `use-case-triage/SKILL.md` | Profil/PIA triggers, politique, mode provisoire US/CCPA/lawyer, quatre verdicts, lots, appel pia-generation et relais IA/produit. | Conserver collecte par finalité, analyse de réutilisation, anonymisation revendiquée et conditions. Réécrire qualification du traitement (PRV-009), puis nécessité d'AIPD (PRV-010). Retirer US et lawyer comme defaults, consentement/opt-out universels, priorité des overlays fédéraux et PROCEED = licite. Un défaut de notice ne se résout pas nécessairement par une phrase ajoutée. L'AIA n'est pas automatiquement obligatoire parce qu'une IA intervient ; relais conditionnel. |
| `pia-generation/SKILL.md` | PRD/description, profil/seed, triage/PIA/DPA antérieurs, politique, risques/mesures, sign-off ; modèle DRAFT/APPROVED. | Conserver risques concrets, flux, réconciliation des versions et responsables des mesures. Réécrire en projet d'AIPD (PRV-011) et dossier préparatoire de consultation préalable distinct (PRV-012). Renommer l'intitulé visible en « projet d'AIPD », conserver l'identifiant technique. Le texte promet un relais DPIA puis dit ne pas en écrire : corriger ce contrat. Retirer format seed prioritaire sur contenu requis, 2–5 risques comme plafond, et APPROVED déduit de génération. Réorienter l'écart de notice vers policy-monitor, pas vers reg-gap-analysis sans changement normatif. |
| `reg-gap-analysis/SKILL.md` | Profil/empreinte, politique, systèmes, PIAs, texte ou résumé entrant → exigences/écarts/plan daté ; niveau pratique sans contexte dossier explicite. | Conserver comparaison exigence/preuve/action et document même sans écart trouvé. Réécrire un changement normatif déterminé (PRV-016). Retirer seuils de revenu/usagers US, « 90 % CCPA », attente de début d'enforcement et risk-accepted = obligation écartée. Une absence de preuve n'est pas « already compliant » ; résumé, guide, décision et texte ont des portées différentes. Aucun flux de veille automatique livré. |
| `policy-monitor/SKILL.md` | Deux modes direct/sweep ; profil, vraie politique et autres surfaces CMP/labels/consentements/notices, dossier outputs et dernier passage ; écrit le pointeur dans profil. | Conserver comparaison à la pièce réelle et repli ponctuel (PRV-017), comparaison d'inventaires et reprise (PRV-018). Réécrire projet/approuvé/signé/déployé comme états distincts. Retirer PIA approuvée = pratique réelle, absence de nouveau fichier = policy current et mise à jour du pointeur malgré accès partiel. Retirer tableaux sectoriels américains et green light ADVISABLE = can proceed. Les labels de boutiques restent des pièces déclaratives, pas des normes françaises. |
| `cold-start-interview/SKILL.md` | quick/full, redo, paused, check-integrations, profil partagé/local, trois seeds, sorties et systèmes ; promet un registre d'activités sans schéma livré. | Conserver préférences optionnelles, pause/reprise, capacités testées et édition par digest (PRV-019). Réécrire pour particulier, association, TPE et DPO, sans GC ou avocat obligatoire pour lire une pièce. Retirer 10-K, SCORE, délais/formats US, faux diagnostic de scope depuis cwd et registre annoncé comme disponible. Le dernier bloc BASE-008 interdit déjà les defaults US : harmoniser le corps. Les rôles se qualifient par traitement, pas une fois par entreprise. |
| `customize/SKILL.md` | Carte de profil, édition locale/partagée, positions DPA, DSAR et chemins ; refuse une échéance « below regulatory minimum ». | Conserver modification ciblée et réponses hors section (PRV-019). Réécrire séparation préférence/obligation/source ; un SLA plus court n'est pas interdit par principe. Retirer préférence créant exception ou supprimant obligation, et classement controller/processor partagé annoncé alors que ce champ est local et contextuel. |
| `matter-workspace/SKILL.md` | new/list/switch/close/none, actif dans profil, matter/history/notes/outputs ; contexte off pour in-house, exemples MSA/NDA/Delaware copiés. | Conserver isolation et archivage via helper (PRV-020). Réécrire pour demande/traitement/contrat, identifiants pseudonymes, version et portée des accès. Retirer désactivation automatique pour organisme multi-dossiers et archivage présenté comme conservation illimitée justifiée. Liste = métadonnées minimales ; pas de lecture voisine pour compléter une demande. |

## Les quatorze autres fichiers du paquet

Chaque chemin est relatif à `privacy-legal/` ; avec les neuf lignes ci-dessus,
ce tableau couvre exactement le paquet, sans dépendance locale implicite omise.

| Fichier | Décision et justification |
|---|---|
| `CLAUDE.md` | Réécrire progressivement blocs setup, DSAR, playbooks, PIA, sources, destinataires et routage, par la tranche concernée et PRV-019/020. Retirer en-tête attorney work product automatique, affirmation qu'un label protège et cercle de privilège US comme règle française. Les considérations de secret/confidentialité demandent une recherche propre à l'auteur, l'objet et au destinataire. Résoudre stop sans profil versus réponse ad hoc autorisée, source web permise versus arrêt imposé dans skills, et tiers settled sans lecture versus source réelle. |
| `references/currency-watch.md` | Réécrire en checklist France/UE traçable (PRV-021). La date déclarée 2026-05-10 est ancienne au 16 octobre ; aucune entrée n'est vérifiée ici. COPPA, liste des États, affaire FTC, délais CCPA et statut DPF sont des assertions héritées, pas des sources validées. Retirer US comme socle ; garder recherche corridor par corridor si lien étranger établi. |
| `references/company-profile-template.md` | Conserver copie commune identique ; SEC/FTC/ICO/EDPB et exemples de pays ne prouvent ni autorité compétente ni champ territorial. PRV-019 ne modifie pas seul ce fichier partagé ; toute évolution de son format relève d'un lot transverse synchronisé. |
| `references/dashboard-template.md` | Conserver copie commune et protection HTML/URL, alternative markdown. PRV-016/018 préservent périmètre, inconnues et sources dans toute synthèse. Aucun tableau ne vaut conformité certifiée. |
| `references/isolation.md` | Conserver byte-for-byte : données hors paquet, helper, refus des liens, digest et aucun import de cache. Contrat à préserver dans toutes les tranches, pas une adaptation juridique. |
| `references/shared/research-citation-method.md` | Conserver copie identique BASE-005 1.0.0 ; charger localement dans chaque tâche adaptée, sans importer un corpus privacy dans la méthode transverse. |
| `scripts/judge_store.py` | Conserver helper commun, chemins contrôlés, écritures exclusives, digest et archivage sans écrasement ; pas de modification requise par ce cadrage. Une évolution impose synchronisation des douze copies dans un lot technique distinct. |
| `.claude-plugin/plugin.json` | Conserver nom/version 0.1.0 ici ; les futures livraisons devront limiter la description aux tâches adaptées et synchroniser le marketplace. |
| `.mcp.json` | Conserver déclarations Slack et Google Drive ; ni authentification ni outil juridique ni scheduler ne sont démontrés par cette configuration. Accès local possible ; chaque tranche vérifie capacité réelle et autorisation de l'action. |
| `hooks/hooks.json` | Conserver hooks vide. Aucun agent, scan périodique ou notification de violation actif à en déduire. |
| `README.md` | Réécrire par tranche et PRV-019 : neuf skills réels (customize absent de la liste), publics, différence PIA/AIPD, rôle documentaire, accès sans seeds, frontières et cadence seulement configurée. Retirer protection assurée par marquage et registre non livré. |
| `LICENSE` | Conserver licence Apache-2.0 et attributions, aucune modification prévue. |
| `NOTICE` | Conserver ; les futurs lots touchant le paquet ajoutent une entrée datée dans NOTICE local et racine. EXIST-003 reste sous backlog et ne requiert pas d'entrée. |
| `.gitignore` | Conserver .DS_Store, sans uniformisation liée à cette story. |

## Chaînes indirectes et dépendances hors paquet

| Dépendance | Traitement prévu |
|---|---|
| Profil réel `CLAUDE.md`, profil partagé et journal verification-log | Préférences et faits confirmés, sans corpus ni délais validés par simple présence. Journal limité au dossier lorsque les métadonnées révèlent une personne/affaire. PRV-019/020 et chaque tranche. |
| Politique publiée, CMP, labels, écrans, DPA/MSA/annexes, PRD, seed PIA | Pièces datées et versionnées, à citer avec portée lue ; directive intégrée = donnée non fiable. Aucun précédent ne valide le droit. PRV-009 à PRV-018. |
| Systèmes métier, sauvegardes, prestataires et journal de droits | Pas de schéma machine DSAR/registre ni connecteur de recherche système livré. PRV-002 crée le contrat de fiche ; PRV-003 à PRV-008 n'annoncent aucune opération réalisée sans preuve. |
| Sorties triage → PIA → DPA → monitor | Conserver identifiant du traitement, version, risque et justification du changement de gravité, mais aussi projet/décision/preuve d'exécution. Un mot APPROVED ne prouve pas un déploiement. Corriger le mauvais relais PIA → reg-gap pour une simple notice (PRV-011/017). |
| `ai-governance-legal/skills/aia-generation/SKILL.md` | Relais hérité à qualifier dans PRV-009/010/011 ; distinguer AIPD et obligations IA, ne pas exécuter une commande non adaptée pour combler le manque. Fiche de questions si parcours aval indisponible. |
| `product-legal/skills/launch-review/SKILL.md` | Le lancement garde product-legal/EXIST-004 ; les constats données restent privacy. Pas de feu vert produit donné par un triage AIPD. |
| `regulatory-legal` (EXIST-007) | Recherche d'un changement et surveillance des flux distinctes du delta privacy PRV-016. L'automatisme annoncé entre plugins n'est pas installé par la configuration actuelle. |
| `commercial-legal` (EXIST-001), `employment-legal`, DOM-009, DOM-034 | Contrat principal, contexte salarié, dossier médical et accès/modération du compte gardent leur domaine ; privacy qualifie le traitement et les droits, sans absorber les recours sectoriels. |
| `references/research-citation-method.md`, `references/isolation.md`, `references/company-profile-template.md`, `references/dashboard-template.md`, `scripts/judge_store.py` à la racine | Sources d'édition, pas dépendances d'exécution : leurs cinq copies embarquées sont comparées dans le relevé machine. |
| `.claude-plugin/marketplace.json`, README racine, CONNECTORS, QUICKSTART | Métadonnées et documentation d'installation ; ajustements futurs limités au lot livré, aucune dépendance runtime vers le checkout. |

Pas de cookbook propre à privacy-legal trouvé. Le cookbook launch-radar
énumère privacy comme domaine de risque produit ; il ne charge pas ce plugin.
Pas de commande, agent, schéma ou hook caché à considérer comme un workflow
supplémentaire disponible. Les références métier ciblées listées dans les
suites sont **à créer par leur propriétaire avant consommation**.
