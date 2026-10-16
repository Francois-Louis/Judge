# EXIST-004 — Inventaire produits et publicité

Relevé du **16 octobre 2026** : **23 fichiers, dont 7 skills et 1 agent**,
fichiers cachés inclus, et **6 fichiers** du cookbook `launch-radar` hors
paquet. Le [relevé machine](exist-004-resultats.json) conserve leurs empreintes.
Les décisions portent sur le contenu hérité, sans modification du plugin.
Voir le [découpage PDT](exist-004-decoupage-produits.md) et la
[relecture documentaire](exist-004-verification.md).

## Les sept skills

Toutes les entrées chargent `references/isolation.md`. Profil effectif et
dossiers vivent sous `config/judge-fr-eu/product-legal/`, via
`scripts/judge_store.py` ; `company-profile.md` est le seul fichier partagé
du fork. La méthode BASE-005 `1.0.0` est embarquée, mais les sept skills ne
la chargent pas explicitement. Chaque tranche adaptée devra le faire.
Les PRD, tickets, copies, preuves et sorties évoqués sont des entrées ou
données utilisateur, pas des fichiers déjà livrés.

| Fichier sous `product-legal/skills/` | Contenu et dépendances | Décision individuelle et justification |
|---|---|---|
| `launch-review/SKILL.md` | Profil/calibration, PRD/design, ticket et commentaires, plan marketing ; grille inline à huit catégories, overlays sectoriels, note interne et résumé tracker ; relais privacy/IA/PI. | Conserver provenance, lecture des pièces, actions avec responsable et synthèse distincte. Réécrire qualification préalable (PDT-001), préparation d'un lancement borné (PDT-002), rôle de service numérique (PDT-010) et collecte sécurité produit (PDT-011). Retirer calibration qui décourage une AIPD au motif « PIA, ships in 1–2 days », socle FTC/COPPA/GLBA/HIPAA/FedRAMP et renvois automatiques AIA/PIA. Retirer Clear to ship, SAFE TO POST garanti et publication au tracker dès connexion. Marché constant ne suffit pas à sauter un contrôle ; une UI peut modifier consentement, prix ou accessibilité. |
| `feature-risk-assessment/SKILL.md` | Dossier, profil, constat amont ; scénarios, victimes, probabilité/gravité, mesures, précédent, options et recommandation ; appelle AIA, PIA et vendor-ai-review. | Conserver risque concret, options et décision attribuée. Réécrire comparaison avant/après (PDT-003), puis analyse d'un seul risque produit (PDT-004), avec dispatch explicite. Retirer 2–5 risques comme plafond, recherche réglementaire seulement en présence d'attention d'un régulateur, dommage ramené à amende/class action et double dossier PIA/AIA obligatoire. Renommer les intitulés visibles des deux modes, conserver l'identifiant technique. |
| `marketing-claims-review/SKILL.md` | Copie texte, profil Marketing claims, données de justification ; taxonomie puffery/factual/comparative/implied/absolute, tableau de revue et réécriture ; overlays avis/influence/essai gratuit. | Conserver citation exacte, portée de la preuve et propositions courtes. Réécrire extraction/contextualisation (PDT-005), faits (PDT-006), environnement (PDT-007), comparaison (PDT-008), avis/influence (PDT-009). Retirer exclusion préalable de la puffery et synonymes « typically », « first », « legacy » présentés comme réparation suffisante ; une allégation vague ou implicite doit rester visible. Retirer Ready to ship et sources FTC/NAD par défaut. Étendre l'entrée aux visuels, labels, liens et mentions fournis ; si non lisibles, signaler la couverture manquante. Essai/renouvellement renvoie à consommation, sans CGV complètes ici. |
| `is-this-a-problem/SKILL.md` | Question PM/Slack, calibration, pièges logo/prix/opt-in/data/IA, dossier et destinataire ; verdict en une minute puis arbre de décision. | Conserver réponse courte et question déterminante (PDT-012). Réécrire en orientation motivée, sans feu vert par simple correspondance. Retirer « analytics covered by policy = fine », PIA en une journée et formalité AIA depuis mot-clé. Logo peut appeler PI/contrat/publicité selon usage ; prix consommateur ne devient pas contrat B2B. Pas de délai de réponse promis au détriment des faits/sources. |
| `cold-start-interview/SKILL.md` | quick/full, redo/pause/check-integrations ; profils partagé/local, dix anciennes revues ou tickets, framework/calibration, tracker/Drive/Slack ; annonce archive et marketing claims log. | Conserver préférences volontaires, reprise, capacités réellement testées et validation des faits extraits (PDT-013). Réécrire pour artisan, association, TPE ou équipe sans GC ni historique. Retirer dix revues obligatoires, SCORE/10-K et vocabulaire VC comme présupposés, faux diagnostic de portée depuis cwd, normes déduites du passé et journal annoncé sans schéma. Harmoniser corps et bloc BASE-008 qui interdit déjà les defaults US. Un profil complet n'est pas requis pour préparer une fiche ponctuelle. |
| `customize/SKILL.md` | Carte des sections, positions marketing, calibration/escalades, chemins et intégrations ; écrit profil local ou partagé. | Conserver changement ciblé, réponses voisines et digest (PDT-013). Réécrire distinction préférence/obligation/preuve ; supprimer une catégorie interne ne supprime pas le contrôle applicable. Le stade de société annoncé partagé n'est pas un champ du modèle commun ; ne pas inventer un schéma. Aucun seuil interne ne rend une allégation prouvée. |
| `matter-workspace/SKILL.md` | new/list/switch/close/none, profil actif, matter/history/notes/outputs et archive ; modèles MSA/NDA/Delaware copiés. | Conserver séparation des dossiers et archivage contrôlé (PDT-014). Réécrire pour lancement/version/campagne, y compris plusieurs produits chez un même organisme ; retirer désactivation in-house systématique. Retirer secret garanti par en-tête et conservation illimitée justifiée par archivage. Related matters n'autorise pas la lecture croisée ; minimiser la liste et refuser les collisions d'archives. |

## Les seize autres fichiers du paquet

Les chemins de ce tableau sont relatifs à `product-legal/`. Avec les sept
entrées ci-dessus, ils couvrent exactement les 23 fichiers du paquet.

| Fichier | Décision et justification |
|---|---|
| `agents/launch-watcher.md` | Conserver radar comme repérage, sans revue complète ni changement de statut (PDT-015). Réécrire filtres et inconnues : titre, absence de mot-clé ou sign-off ancien ne prouvent rien sur la version courante. Retirer COPPA/HIPAA par défaut, PIA likely required depuis mot-clé, all-clear sans couverture. Outils Read/Write et motifs MCP sans exécution Python déclarée : résoudre l'accès au helper avant activation, sans contournement. Aucun scheduler livré ; le texte précise l'invocation séparée malgré « runs daily ». |
| `skills/launch-review/references/seven-category-framework.md` | Réécrire avec PDT-002 ; conserver le chemin historique, renommer l'intitulé visible en grille de préparation bornée. Le nom dit seven, le titre et le corps eight ; maintenir une seule grille métier référencée plutôt que deux copies divergentes. Retirer auto-skip réglementaire depuis marché inchangé et DPA requis pour tout tiers. Ajouter qualification, critères d'inclusion, inconnues et relais avec limite de couverture. |
| `CLAUDE.md` | Modèle de profil, pas contexte chargé à l'installation. Réécrire par tranche les sorties, destinataires, framework, calibration et routage ; PDT-013/014 pour la configuration/dossiers. Retirer attorney work product automatique, affirmation « header protects », renonciation systématique pour clients et protection « meaningful everywhere ». Secret/confidentialité à rechercher selon auteur, qualité, objet et destinataire. Résoudre STOP sans profil versus réponse ad hoc permise, et settled sans lecture versus provenance réelle. Retirer framework US comme substitut français même assorti de caveats. |
| `references/currency-watch.md` | Remplacer la liste par une checklist de recherche datée par entrée (PDT-017). Date déclarée 2026-05-10, antérieure au relevé ; COPPA, sanctions DSA, Section 230, FTC et calendrier AI Act/Digital Omnibus sont des assertions héritées, aucune vérifiée ici. Ne pas promouvoir une proposition de réforme ou sanction isolée en règle applicable. Une mise à jour partielle ne rafraîchit pas tout le fichier. |
| `references/company-profile-template.md` | Conserver copie commune identique ; FTC/SEC/EDPB et exemples de pays sont des exemples non vérifiés. Le rôle vendeur/fabricant/plateforme dépend de l'activité, pas seulement de la société. PDT-013 ne change pas seul ce format commun ; évolution éventuelle dans un lot transverse synchronisé. |
| `references/dashboard-template.md` | Conserver copie commune, protection HTML/URL et alternative Markdown. PDT-002/015 préservent périmètre, inconnues et états de preuve dans les synthèses. Un compteur vert ne signifie pas conformité. |
| `references/isolation.md` | Conserver octet pour octet : helper obligatoire, pas de cache/import, refus des liens, création exclusive et digest. Les futures tranches adaptent leurs accès et outils à ce contrat. |
| `references/shared/research-citation-method.md` | Conserver copie BASE-005 1.0.0 identique et charger depuis le paquet dans chaque tâche adaptée. Les références produit/publicité restent locales au domaine. |
| `scripts/judge_store.py` | Conserver helper commun sans changement. Une évolution technique demande synchronisation des douze copies ; l'absence d'outil permettant son usage dans l'agent est un point de PDT-015/016, pas une raison de le contourner. |
| `.claude-plugin/plugin.json` | Conserver nom/version 0.1.0 dans ce cadrage. Les prochaines livraisons décrivent seulement la tranche adaptée, avec marketplace synchronisé si modifié. |
| `.mcp.json` | Conserver Slack, Google Drive, Linear, Atlassian et Asana déclarés. Ne prouve ni connexion, ni outil juridique, ni scheduler ; pas de connecteur obligatoire pour une lecture locale. Tester capacité et périmètre avant usage. |
| `hooks/hooks.json` | Conserver hooks vide ; ne déclenche aucun radar. |
| `README.md` | Réécrire par tranche : sept skills réels (customize absent du tableau), publics, couverture bornée, sources officielles sans abonnement imposé, frontières et cadence à configurer. Corriger protection assurée par marquage, calibration érigée en critère unique et automatisation annoncée active. |
| `LICENSE` | Conserver Apache-2.0 et attributions. |
| `NOTICE` | Conserver ici ; futur lot hors backlog ajoute entrée datée locale et racine. |
| `.gitignore` | Conserver sans uniformisation. |

## Cookbook lié : six fichiers hors paquet

PDT-016 dépend de la tranche radar PDT-015, sans lui faire dépendre un skill
manuel. Aucun déploiement, compte MCP ou permission réseau n'est créé ici.

| Fichier sous `managed-agent-cookbooks/launch-radar/` | Décision individuelle |
|---|---|
| `agent.yaml` | Conserver orchestrateur local et délégation aux feuilles ; réécrire append/framing et contrat du profil effectif. Pas de corpus juridique ni feu vert en headless. |
| `subagents/tracker-reader.yaml` | Conserver lecture des seuls trackers et données non fiables. Corriger schéma ASCII qui exclut titres français, date seulement regex et limite 200 qui abandonne des tickets sans métadonnées de couverture ; documenter permissions réelles (toolsets activés par défaut ne garantissent pas lecture seule). Préserver URL brute et signalement d'hôte inattendu, sans normalisation silencieuse. |
| `subagents/risk-classifier.yaml` | Conserver classifications de routage. Retirer « list is trusted » : schéma valide n'efface pas les directives du texte libre. Corriger calibration « plugin CLAUDE.md » ambiguë, skip UI/copy et horizon/dates/délai interne confondus avec échéance légale. maxItems 8 face à 12 domaines exige règle explicite de couverture. |
| `subagents/memo-writer.yaml` | Conserver seul détenteur Write, rendu protégé et diff daté. Résoudre demande de liens cliquables versus URL inerte, handoff_request absent du schéma classificateur, en-tête US et accès profil/sortie via helper sans outil d'exécution déclaré. Diff limité au même périmètre ; disparition d'un ticket ne signifie ni annulation ni résolution. |
| `steering-examples.json` | Réécrire cas français avec horizon/périmètre explicites, export tronqué et injection ; ne pas promettre exécution du skill complet depuis simple triage headless. |
| `README.md` | Réécrire tableau de droits qui attribue MCP à l'orchestrateur pourtant local, lecture du modèle comme profil, horizon quotidien/30 jours versus hebdo/6 semaines, sortie ./out versus racine de déploiement BASE-008. Conserver configuration explicite de scheduler et recette avant activation. |

## Dépendances indirectes à traiter

| Chaîne ou entrée | Traitement prévu et propriétaire |
|---|---|
| Profil partagé/local, seeds et calibration | Préférences et décisions passées distinctes du droit et des faits du nouveau produit ; seeds facultatifs, datés, périmètre lu. PDT-013 et chaque tranche. |
| PRD/design → ticket → commentaires → pièces liées | Version et source par constat, liens non lus signalés, contenu tiers traité comme données. PDT-001/002/003/015 ; le tracker n'est pas une preuve de mise en œuvre. |
| Grille inline → référence séparée → profil | PDT-002 possède la grille, avec renvoi local ; le profil ne peut enlever un contrôle applicable. PDT-001 qualifie en amont. |
| Copie → image/label/renvoi → justificatif | PDT-005 possède inventaire et contrat d'allégation ; PDT-006/007/008/009 possèdent examens ciblés. Claims log annoncé sans schéma devient tableau versionné proposé, sans registre global obligatoire. |
| Constat → risque → mesures → résumé tracker/Slack/dashboard | Séparer proposé/décidé/réalisé/prouvé ; gravité amont conservée ou changement justifié. Synthèse minimisée selon destinataire, aucune mention SAFE garantie. PDT-002/004/014/015. |
| Données → `privacy-legal` | Qualification du traitement PRV-009, nécessité AIPD PRV-010, projet PRV-011, notice PRV-017 et contrat PRV-013/014 : propositions non disponibles par simple relais. Fiche manuelle suffisante ; pas d'appel automatique à `use-case-triage`/`pia-generation` hérités. |
| IA → `ai-governance-legal` | `use-case-triage`, `aia-generation`, `vendor-ai-review` à cadrer dans EXIST-005. Repérer fonction/rôle/public, ne pas imposer AIA depuis mot « AI » ; conserver question non instruite si tâche adaptée absente. |
| Contrat/PI/secteur | Commercial pour contrat B2B, IP pour marque/OSS/licence, domaine sectoriel pour son analyse ; produit conserve ses engagements de lancement. Pas d'exécution automatique d'une commande héritée. |
| Achat/plateforme côté utilisateur | DOM-001 garde CGV B2C/réclamation ; DOM-034 garde suspension/modération. PDT-010 traite le rôle de l'opérateur qui prépare un service, sans doublon de contestation ni plugin fantôme. |
| Déploiement cookbook | `scripts/deploy-managed-agent.sh`, `scripts/cookbook_paths.py`, `scripts/validate.py`, `scripts/lint-tool-scope.py`, `scripts/orchestrate.py`, `scripts/test-cookbooks.sh` et contrats de `managed-agent-cookbooks/README.md` : lire avant PDT-016 ; changements transverses éventuels dans un lot distinct. Ne pas inférer d'une validation de schéma que le runtime confine les outils. |

Les futures références métier sont énumérées dans les stories, explicitement
« à créer ». Aucune dépendance vers la racine du checkout ou un autre plugin
ne sera requise dans le paquet installé. La recherche juridique et la recette
métier restent celles des futures tranches ; la portée du présent relevé
est donnée dans la [vérification](exist-004-verification.md).
