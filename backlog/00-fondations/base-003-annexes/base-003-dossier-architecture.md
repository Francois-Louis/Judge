# BASE-003 — Architecture des plugins par domaine

Cadrage établi le **15 octobre 2026 (Europe/Paris)** à partir des manifestes,
des répertoires de skills et du backlog local. Il fixe les règles à appliquer
aux prochaines stories ; il ne certifie pas l'adaptation France/UE des plugins
existants et ne crée aucun nouveau plugin.

## Décision d'organisation

Un plugin porte un domaine identifiable. Un skill porte une tâche bornée,
avec ses entrées, son résultat, ses exclusions et ses références métier.
Le territoire et la date d'application sont qualifiés dans chaque tâche ;
ils ne justifient pas un plugin juridique généraliste France/UE.

Chaque tâche a **un seul plugin principal**. Un dossier peut contenir plusieurs
demandes : la réclamation au vendeur et la contestation du paiement à la banque
sont deux tâches. Un complément confié à un autre domaine doit désigner une
question précise, sans transférer tout le dossier ni charger tous les plugins.
Une référence à un autre domaine n'est pas une dépendance d'installation.

L'orientation prévue par [USAGE-001](../../05-usages-quotidiens/usage-001-orientation-accessible.md)
utilise le récit, le document, la qualité des parties et l'objectif. Elle
retourne un domaine principal, les seules questions complémentaires utiles et
la disponibilité réelle de la tâche. Elle garde un index de routage, sans
héberger les raisonnements, corpus, modèles de recours ou délais des domaines.
Son support est le [protocole documentaire USAGE-001](../../05-usages-quotidiens/usage-001-annexes/usage-001-protocole-orientation.md)
et l'index enrichi des situations du quotidien ; aucun plugin d'orientation
n'est créé. Ce cadrage n'ajoute pas de point d'entrée exécutable.

## Inventaire existant et adaptations

Inventaire local : **12 plugins internes, 150 skills**, tous en version `1.0.2`,
inscrits dans le [marketplace](../../../.claude-plugin/marketplace.json).
Les noms de skills ci-dessous sont les répertoires actuels, pas des commandes
françaises nouvellement livrées. « Existant → adaptation » décrit une cible de
travail, sans annoncer que son comportement juridique est déjà adapté.
Les skills de configuration et de gestion de dossier restent dans leur plugin.

| Domaine / plugin principal | État / suivi | Tâches existantes représentatives | Frontière et interlocuteur |
|---|---|---|---|
| Contrats professionnels — `commercial-legal` (12 skills) | Existant → adaptation, EXIST-001 | `vendor-agreement-review`, `nda-review`, `saas-msa-review`, `renewal-tracker` : revue et suivi d'un contrat B2B | Client/fournisseur professionnel ; achats de consommation → DOM-001 ou domaine sectoriel, exécution d'un titre → DOM-003. |
| Sociétés et opérations — `corporate-legal` (13) | Existant → adaptation, EXIST-002 | `tabular-review`, `board-minutes`, `closing-checklist`, `entity-compliance` | Organes sociaux, conseil de l'opération ; contrats courants → commercial, fiscalité → DOM-011. |
| Données personnelles — `privacy-legal` (9) | Existant → adaptation, EXIST-003 | `dsar-response`, `dpa-review`, `pia-generation` ; l'exercice d'un droit par un particulier reste à découper | Responsable du traitement / délégué à la protection des données ; accès au compte et modération → DOM-034. |
| Produits et publicité — `product-legal` (7) | Existant → adaptation, EXIST-004 | `launch-review`, `marketing-claims-review`, `feature-risk-assessment` | Équipe produit/marketing ; réclamation individuelle à un vendeur → DOM-001 ou secteur, données → privacy. |
| Gouvernance IA — `ai-governance-legal` (10) | Existant → adaptation, EXIST-005 | `use-case-triage`, `aia-generation`, `vendor-ai-review` | Responsable d'un usage IA ; traitement de données → privacy, clause PI → ip, sans dupliquer leur analyse. |
| Contentieux — `litigation-legal` (19) | Existant → adaptation, EXIST-006 | `chronology`, `claim-chart`, `brief-section-drafter`, `demand-intake` | Conseil chargé d'un contentieux civil/commercial ; pénal → DOM-002, acte d'exécution → DOM-003. Une demande sectorielle conserve son propriétaire. |
| Veille réglementaire — `regulatory-legal` (9) | Existant → adaptation, EXIST-007 | `reg-feed-watcher`, `policy-diff`, `gap-surfacer` | Responsable conformité ; veille et écarts, pas recours contre toute décision administrative (DOM-010 ou secteur). |
| Propriété intellectuelle — `ip-legal` (12) | Existant → adaptation, EXIST-008 | `clearance`, `ip-clause-review`, `oss-review`, `takedown` | Titulaire de droits / conseil PI ; compte suspendu → DOM-034, procédure contentieuse distincte → litigation. |
| Clinique — `legal-clinic` (16), **retiré le 16 octobre 2026** | Plugin supprimé sur décision de l'utilisateur ; EXIST-009 conservé comme trace, suites CLN abandonnées | `client-intake`, `supervisor-review-queue`, `semester-handoff`, `plain-language-letters` | Étudiant et superviseur : accueil, supervision, continuité ; l'analyse d'un bail ou d'une saisie appartient au domaine concerné. |
| Formation juridique — `law-student` (13) | Existant → adaptation, EXIST-010 | `case-brief`, `irac-practice`, `socratic-drill`, `study-plan` | Apprenant/enseignant ; entraînement, pas traitement du litige de l'apprenant avec son école (DOM-027). |
| Gestion des skills — `legal-builder-hub` (10) | Existant → adaptation, EXIST-011 | `registry-browser`, `skill-installer`, `skills-qa`, `auto-updater` | Utilisateur/mainteneur ; installation et contrôle technique, sans moteur de raisonnement juridique ni dépendance obligatoire pour les autres plugins. |
| Travail privé — `employment-legal` (20) | Existant → adaptation, PILOTE-001 à PILOTE-003 | `hiring-review`, `termination-review`, `wage-hour-qa`, `leave-tracker` | Candidat/salarié/employeur privé ; emploi public → DOM-037, décision d'une caisse → DOM-012, retraite → DOM-036. |

Le plugin éditeur [CoCounsel](../../../external_plugins/cocounsel-legal/README.md)
est une entrée distincte du marketplace (`cocounsel-legal`, recherche via son
service). Il n'est ni un domaine France/UE adapté, ni une dépendance commune ;
son contenu reste maintenu par l'éditeur.

Les cinq [cookbooks](../../../managed-agent-cookbooks/README.md) (`diligence-grid`,
`docket-watcher`, `launch-radar`, `reg-monitor`, `renewal-watcher`) sont des
recettes de déploiement séparées, pas cinq plugins supplémentaires. Leur
existence ne justifie pas l'ajout d'un agent à chaque domaine.

## Matrice des nouveaux domaines et des tâches

**Toutes les lignes ci-dessous sont des créations proposées.** Les noms de
plugins sont repris des stories DOM et restent des **propositions jusqu'au
cadrage correspondant**. Les tâches sont des candidates à découper : elles ne
sont pas des skills disponibles et ne rendent pas leurs domaines livrables.
Les références métier appartiendront au plugin de la ligne. Chaque tâche
indiquée dans la colonne « Tâche → résultat » a ce plugin comme propriétaire.
Les interlocuteurs indiquent à qui préparer une demande ; leur compétence
exacte sera vérifiée pour le régime choisi lors de l'implémentation.

| Domaine / suivi | Plugin principal proposé | Tâche bornée → résultat candidat | Interlocuteur ; interaction explicite |
|---|---|---|---|
| Consommation — [DOM-001](../../03-nouveaux-domaines/dom-001-consommation.md), [découpage](../../03-nouveaux-domaines/dom-001-annexes/dom-001-decoupage-consommation.md) | `consumer-legal`, nom conservé par le cadrage | Réclamation pour commande non livrée → pièces et brouillon au vendeur (CONSO-001) | Vendeur professionnel ; paiement/crédit → DOM-004, assurance vendue avec le bien → DOM-005, voyage → DOM-008, données → privacy, achat pour l'activité → commercial, envoi confié par l'usager → DOM-022, douane → DOM-009, vendeur particulier → tâche civile CONSO-011. Les secteurs spécialisés gardent leurs litiges. |
| Police et pénal — [DOM-002](../../03-nouveaux-domaines/dom-002-police-penal.md), [découpage](../../03-nouveaux-domaines/dom-002-annexes/dom-002-decoupage-penal.md) | `criminal-legal`, nom conservé par le cadrage | Lire une convocation → mesure, statut et points urgents à vérifier (CRIM-001) | Autorité émettrice/conseil pénal ; réparation civile distincte → DOM-035 ou secteur, parcours de protection → DOM-038, retenue pour le droit au séjour → DOM-028, retenue douanière → DOM-009, police administrative → DOM-010, saisie pour une amende → DOM-003, demande de pièces civile → litigation. |
| Recouvrement et exécution — [DOM-003](../../03-nouveaux-domaines/dom-003-commissaires-justice-execution.md), [découpage](../../03-nouveaux-domaines/dom-003-annexes/dom-003-decoupage-execution.md) | `enforcement-legal`, nom conservé par le cadrage | Lire un acte de recouvrement ou d'exécution → acte, dates, urgence et questions (ENF-001) ; décompte et saisie sur compte en suites | Émetteur/commissaire de justice, conseil ou juridiction à identifier ; dette locative → DOM-006, crédit et frais bancaires → DOM-004, situation globale → DOM-024, impôt/amende/indu au fond → DOM-011/DOM-002/DOM-012, procédure pour obtenir un titre → litigation. |
| Banque — [DOM-004](../../03-nouveaux-domaines/dom-004-banque.md), [découpage](../../03-nouveaux-domaines/dom-004-annexes/dom-004-decoupage-banque.md) | `banking-legal`, nom conservé par le cadrage | Qualifier un paiement contesté → réclamation documentée (BNK-001, `payment-dispute`) ; lire une offre de crédit → questions ciblées | Prestataire de paiement/prêteur ; garantie d'assurance → DOM-005, difficulté globale → DOM-024, litige avec le vendeur → DOM-001, saisie sur compte → DOM-003, plainte → DOM-002 ; placements orientés seulement. |
| Assurance — [DOM-005](../../03-nouveaux-domaines/dom-005-assurance.md), [découpage](../../03-nouveaux-domaines/dom-005-annexes/dom-005-decoupage-assurance.md) | `insurance-legal`, nom conservé par le cadrage | Lire un refus de garantie → comparaison contrat/motifs/pièces (INS-001) | Assureur, mutuelle ou institution de prévoyance ; crédit → DOM-004, responsabilité du dommage → secteur ou DOM-035, responsabilité des constructeurs → DOM-015, prestations de caisse → DOM-012, garantie commerciale d'un vendeur → DOM-001, succession → DOM-016. |
| Logement locatif — [DOM-006](../../03-nouveaux-domaines/dom-006-logement.md), [découpage](../../03-nouveaux-domaines/dom-006-annexes/dom-006-decoupage-logement.md) | `housing-legal`, nom conservé par le cadrage | Retenue sur dépôt d'une location privée vide → tableau et brouillon au bailleur (LOG-001) ; charges, bail, réparations/décence, congés, dette et candidature en suites LOG-002 à LOG-011 | Bailleur/agence ; conseil ADIL ou avocat ; acte/expulsion → DOM-003, entreprise de travaux → DOM-015, achat → DOM-017, copropriétaire → DOM-018, autorisation publique → DOM-019, nuisance directe → DOM-020, données → PRV-026/024. |
| Santé — [DOM-007](../../03-nouveaux-domaines/dom-007-sante.md), [découpage](../../03-nouveaux-domaines/dom-007-annexes/dom-007-decoupage-sante.md) | `health-legal`, nom conservé par le cadrage | Préparer la demande d'accès au dossier médical d'un patient majeur pour lui-même → qualification, pièces et brouillon (SAN-001) | Établissement/professionnel de santé ; remboursement et décision de caisse → DOM-012, complémentaire santé → DOM-005, chiffrage du préjudice corporel → DOM-035, étendue d'une mesure → DOM-026, droits RGPD et traces d'accès → privacy, plainte → DOM-002. Explication, sanction ordinale, signalement à l'ARS et indemnisation sont des tâches distinctes ; soins sans consentement gardés par health. |
| Transports et voyages — [DOM-008](../../03-nouveaux-domaines/dom-008-transports.md), [découpage](../../03-nouveaux-domaines/dom-008-annexes/dom-008-decoupage-transports.md) | `transport-legal`, nom conservé par le cadrage | Vol direct annulé hors forfait → qualification, demandes distinctes, pièces et brouillon (TPT-001) | Mode, trajet, dates, transporteur effectif/vendeur, réservation unique ou contrats distincts, passager/fret qualifiés ; correspondances, train, bagage, forfait et fret séparés. Assurance → DOM-005 ; achat/réparation véhicule → DOM-023, poste → DOM-022, livraison de vente → DOM-001, douane → DOM-009 ; aucun régime aérien sur train ou fret. |
| Douanes — [DOM-009](../../03-nouveaux-domaines/dom-009-douanes.md) | `customs-legal` | Qualifier un colis bloqué → acte et dossier documentaire | Douane/transporteur selon l'acte ; obligation du vendeur → DOM-001, impôt hors douane → DOM-011. |
| Administratif — [DOM-010](../../03-nouveaux-domaines/dom-010-administratif.md) | `administrative-legal` | Lire une décision administrative sans domaine spécial identifié → motifs et voies à vérifier | Administration émettrice ; urbanisme → DOM-019, séjour → DOM-028, emploi public → DOM-037. |
| Fiscalité — [DOM-011](../../03-nouveaux-domaines/dom-011-fiscalite.md) | `tax-legal` | Lire un document fiscal identifié → impôt, période et stade | Service fiscal ; transmission successorale → DOM-016, acte d'exécution distinct → DOM-003 après qualification du régime. |
| Protection sociale — [DOM-012](../../03-nouveaux-domaines/dom-012-protection-sociale.md) | `social-security-legal` | Lire une notification d'indu pour une prestation choisie → motifs, période et pièces | Caisse/organisme émetteur, dont MSA selon statut ; retraite → DOM-036, reconnaissance du handicap → DOM-025. |
| Famille et couple — [DOM-013](../../03-nouveaux-domaines/dom-013-famille-patrimoine.md) | `family-legal` | Lire une décision familiale → obligations et points à éclaircir | Conseil/notaire ou juridiction identifiée ; succession → DOM-016, besoin de protection contre des violences → DOM-038. |
| Agriculture et rural — [DOM-014](../../03-nouveaux-domaines/dom-014-agriculture-rural.md) | `agricultural-legal` | Lire une demande de fermage → montants et pièces à vérifier pour un bail borné | Bailleur/preneur ; caisse MSA → DOM-012, salarié agricole → employment, succession → DOM-016. |
| Construction et travaux — [DOM-015](../../03-nouveaux-domaines/dom-015-construction-travaux.md) | `construction-legal` | Revoir un devis de rénovation ; documenter un chantier inachevé → engagements, paiements et réclamation | Artisan/entrepreneur ; permis → DOM-019, vote de travaux → DOM-018, refus d'assurance → DOM-005. |
| Successions et donations — [DOM-016](../../03-nouveaux-domaines/dom-016-successions-donations.md) | `inheritance-legal` | Décrypter un courrier de succession → pièces et questions au notaire | Notaire/cohéritiers ; obsèques → DOM-031, fiscalité → DOM-011, pouvoirs d'un majeur protégé → DOM-026. |
| Achat et vente immobilière — [DOM-017](../../03-nouveaux-domaines/dom-017-transactions-immobilieres.md) | `real-estate-legal` | Lire un avant-contrat de logement ancien → engagements et pièces manquantes | Notaire/vendeur ; prêt → DOM-004, travaux → DOM-015, bail → DOM-006. |
| Copropriété — [DOM-018](../../03-nouveaux-domaines/dom-018-copropriete.md) | `co-ownership-legal` | Décrypter un appel de charges ou une décision de travaux → justificatifs et objet de contestation | Syndic/syndicat ; charges réclamées au locataire → DOM-006, malfaçons → DOM-015. |
| Urbanisme et foncier — [DOM-019](../../03-nouveaux-domaines/dom-019-urbanisme-foncier.md) | `planning-legal` | Lire un refus d'autorisation → motifs et documents locaux à vérifier | Service instructeur/mairie ; servitude privée → DOM-020, pollution → DOM-030. |
| Voisinage et servitudes — [DOM-020](../../03-nouveaux-domaines/dom-020-voisinage-servitudes.md) | `neighbourhood-legal` | Documenter une nuisance ou un passage contesté → chronologie, titres et réclamation | Voisin/conseil ; autorisation publique → DOM-019, pollution → DOM-030. |
| Énergie et eau — [DOM-021](../../03-nouveaux-domaines/dom-021-energie-eau.md) | `utilities-legal` | Lire une régularisation d'électricité → période, index et demande de justification | Fournisseur/gestionnaire ; charges du bailleur → DOM-006, travaux énergétiques → DOM-015. |
| Télécoms et poste — [DOM-022](../../03-nouveaux-domaines/dom-022-telecoms-poste.md) | `telecom-postal-legal` | Contester des frais de résiliation ou de matériel restitué → comparaison contrat/facture/preuve | Opérateur ; non-livraison due par le vendeur → DOM-001, modération de plateforme → DOM-034. |
| Véhicules et garages — [DOM-023](../../03-nouveaux-domaines/dom-023-vehicules-garages.md), [découpage](../../03-nouveaux-domaines/dom-023-annexes/dom-023-decoupage-vehicules.md) | `vehicle-legal`, nom conservé par le cadrage | Comparer une facture de garage au devis et aux accords retrouvés → tableau des écarts et brouillon de demande (VEH-001) ; gardiennage, réparation défaillante, occasion, location, véhicule neuf, expertise amiable et garantie constructeur en suites VEH-002 à VEH-012 | Garage/vendeur/loueur/constructeur ; association de consommateurs, médiateur du secteur, expert automobile pour la seule question technique ; infraction, amende et permis → DOM-002, garantie auto et expertise d'assurance → DOM-005, accident corporel → DOM-035, crédit, paiement et préautorisation → DOM-004, saisie du véhicule → DOM-003, immatriculation et fourrière → DOM-010, véhicule professionnel → commercial. Vente entre particuliers, vente professionnelle, location et réparation sont des régimes distincts ; vente d'un véhicule entre particuliers ici sous réserve d'arbitrage (CONSO-011). |
| Dettes et surendettement — [DOM-024](../../03-nouveaux-domaines/dom-024-dettes-surendettement.md) | `debt-relief-legal` | Lire une notification et organiser plusieurs dettes → stade, pièces et tableau de situation | Organisme du dossier/créanciers ; saisie → DOM-003, bien-fondé du crédit → DOM-004. Difficultés professionnelles à qualifier séparément. |
| Handicap et autonomie — [DOM-025](../../03-nouveaux-domaines/dom-025-handicap-autonomie.md) | `disability-legal` | Lire une notification de reconnaissance/accompagnement → dossier de questions et pièces | Organisme décisionnaire, MDPH selon le cas ; calcul par une caisse → DOM-012, école → DOM-027. |
| Protection des majeurs — [DOM-026](../../03-nouveaux-domaines/dom-026-protection-majeurs.md) | `adult-protection-legal` | Lire décision ou mandat pour un acte choisi → pouvoirs et vérifications | Personne concernée/représentant, professionnel ou juge identifié ; soins → DOM-007, succession → DOM-016. |
| Éducation et formation — [DOM-027](../../03-nouveaux-domaines/dom-027-education-formation.md) | `education-legal` | Lire une décision d'établissement → demande motivée dans un régime borné | Établissement ; apprentissage salarié → employment, handicap → DOM-025, aides → DOM-012. |
| Séjour, nationalité, asile — [DOM-028](../../03-nouveaux-domaines/dom-028-sejour-nationalite-asile.md) | `immigration-legal` | Lire une demande de pièces pour un titre choisi → liste de réponses à préparer | Autorité émettrice/conseil ; emploi → employment ou DOM-037, famille → DOM-013. Urgences en tâches distinctes. |
| Discriminations — [DOM-029](../../03-nouveaux-domaines/dom-029-discriminations.md) | `equality-legal` | Structurer un refus d'accès à un service → faits, critère allégué et pièces | Auteur du refus/organisme compétent à identifier ; contestation du bail, de la rupture ou de la décision scolaire pilotée par son domaine. |
| Environnement — [DOM-030](../../03-nouveaux-domaines/dom-030-environnement-pollutions.md) | `environmental-legal` | Structurer un signalement de pollution observée → faits sans causalité présumée | Autorité compétente selon activité/lieu ; voisinage privé → DOM-020, exploitation agricole → DOM-014. |
| Décès et obsèques — [DOM-031](../../03-nouveaux-domaines/dom-031-deces-obseques.md), [découpage](../../03-nouveaux-domaines/dom-031-annexes/dom-031-decoupage-funeraire.md) | `funeral-legal`, nom conservé par le cadrage | Lire un devis funéraire avant engagement → postes demandés ou proposés, mentions et brouillon de demande d'explication (FUN-001) ; facture et prestations non demandées, désaccord entre proches, demande de paiement, financements, contrat obsèques, concession, premières démarches, marbrerie, cendres, volontés anticipées et exhumation en suites FUN-002 à FUN-012 | Opérateur funéraire/signataire ; association de consommateurs, médiateur du secteur, notaire pour la succession, avocat en cas de désaccord ou de procédure ; succession, frais funéraires comme passif et comptes du défunt → DOM-016, contrat obsèques comme assurance et capital → DOM-005, capital décès d'un organisme → DOM-012, pouvoirs d'un majeur protégé → DOM-026, obstacle médico-légal et atteinte alléguée → DOM-002, recouvrement → DOM-003. Signataire, personne qui décide et personne tenue au paiement sont qualifiés séparément, jamais par le seul lien familial. |
| Associations — [DOM-032](../../03-nouveaux-domaines/dom-032-associations-adherents.md) | `association-legal` | Lire une exclusion et les statuts → demande d'explication | Organe associatif ; service vendu → DOM-001 ou secteur, salarié → employment, accident → DOM-035 ou secteur. |
| Animaux — [DOM-033](../../03-nouveaux-domaines/dom-033-animaux.md) | `animal-legal` | Lire acquisition, garde ou pension pour une espèce choisie → obligations et pièces | Cédant/gardien ; élevage professionnel → DOM-014, voisinage → DOM-020, pénal → DOM-002. |
| Numérique et plateformes — [DOM-034](../../03-nouveaux-domaines/dom-034-numerique-plateformes.md) | `digital-rights-legal` | Lire une suspension de compte → contestation interne ; documenter une usurpation → questions distinctes | Plateforme ; données → privacy, droit d'auteur → ip, achat → DOM-001, paiement → DOM-004, infraction alléguée → DOM-002. |
| Responsabilité civile — [DOM-035](../../03-nouveaux-domaines/dom-035-responsabilite-dommages.md) | `civil-liability-legal` | Organiser un dommage matériel sans domaine spécial identifié → faits, pièces et chiffrage | Auteur allégué/conseil ; dommage médical, construction, circulation ou infraction d'abord orientés au secteur ; garantie → DOM-005. |
| Retraites — [DOM-036](../../03-nouveaux-domaines/dom-036-retraites.md) | `pension-legal` | Préparer une correction de période de carrière → demande sur pièces pour un régime | Régime de retraite concerné ; litige employeur → employment ou DOM-037, autres prestations → DOM-012. |
| Fonction publique — [DOM-037](../../03-nouveaux-domaines/dom-037-fonction-publique.md) | `public-employment-legal` | Lire une décision individuelle de carrière/rémunération → motifs et questions pour un statut choisi | Employeur public/service RH ; emploi privé → employment, pension → DOM-036, caisse → DOM-012. |
| Violences intrafamiliales — [DOM-038](../../03-nouveaux-domaines/dom-038-violences-intrafamiliales.md) | `domestic-violence-legal` | Préparer un parcours de protection → canal sûr et pièces strictement utiles | Interlocuteur de protection adapté à la situation ; qualification pénale → DOM-002, séparation → DOM-013, logement → DOM-006, soins → DOM-007. |
| Micro-entreprise — [DOM-039](../../03-nouveaux-domaines/dom-039-micro-entreprise.md) | `self-employed-legal` | Lire un courrier de l'URSSAF → période, montants recopiés, stade et pièces | URSSAF/administration fiscale ; impôts du foyer → DOM-011, CAF → DOM-012, retraite → DOM-036, client professionnel → commercial, acte de saisie → DOM-003. |
| Chasse et pêche — [DOM-040](../../03-nouveaux-domaines/dom-040-chasse-peche.md) | `hunting-fishing-legal` | Lire un procès-verbal de chasse ou de pêche → infraction alléguée, stade et pièces | Agent verbalisateur/fédération ; arme → CRIM-017, procédure pénale → DOM-002, exploitation agricole → DOM-014, espèces et pollution → DOM-030, assurance → DOM-005. |
| Professionnels du droit et du chiffre — [DOM-041](../../03-nouveaux-domaines/dom-041-professionnels-du-droit.md) | `professional-services-legal` | Lire un décompte de frais de notaire → émoluments, débours, taxes et questions | Notaire/avocat/commissaire de justice/expert-comptable, instance ou médiateur à identifier ; fond du dossier → son domaine, frais d'un acte de saisie → ENF-003, faute pénale → DOM-002. |
| Artistes et spectacle — [DOM-042](../../03-nouveaux-domaines/dom-042-artistes-spectacle.md) | `arts-legal` | Lire un courrier de France Travail à un intermittent → décision, période, heures et pièces | URSSAF/France Travail/caisse des congés spectacles ; droits sur les œuvres → ip, travail ordinaire → employment, CAF → DOM-012, micro-entreprise → DOM-039. |
| Médias et expression publique — [DOM-043](../../03-nouveaux-domaines/dom-043-medias-expression.md) | `media-legal` | Documenter une publication qui atteint une personne → qualification possible, urgence et démarche | Auteur/éditeur/hébergeur, avocat pour une procédure de presse ; modération de plateforme → DOM-034, RGPD et déréférencement → privacy, droit d'auteur → ip, harcèlement → DOM-002, journaliste salarié → employment. |

Les cadrages EXIST/DOM précisent ensuite les tâches supplémentaires et les
stories d'implémentation. Leurs implémentations attendent le bilan PILOTE-003,
selon le [backlog](../../README.md) ; BASE-003 ne change pas cette condition.

## Règles de frontière à appliquer story par story

| Croisement | Règle de propriété de la tâche et complément autorisé |
|---|---|
| Consommation / contrats / secteurs | Qualifier les parties et l'objet : contrat B2B courant → commercial ; achat de consommation sans secteur spécial → consumer ; rénovation, énergie, véhicule, voyage, etc. → secteur. Le secteur embarque les règles de consommation utiles à sa tâche, sans imposer l'installation de consumer. Tant que le plugin du secteur n'est pas disponible, consumer traite la demande avec les règles générales et signale les règles sectorielles non examinées (CONSO-014, décision du 16 octobre 2026) ; ensuite il oriente. Une revue de CGV B2C reste candidate chez consumer. |
| Banque / assurance | Opération de paiement, compte ou crédit → banking ; couverture ou refus de garantie, y compris assurance emprunteur → insurance. Un prêt et son assurance donnent deux questions, deux sorties et deux interlocuteurs. L'investissement n'est pas traité par DOM-004, qui ne prévoit qu'une orientation (BNK-011) ; aucun cadrage dédié, par décision du 16 octobre 2026. |
| Logement / exécution | Décompte du bail, dépôt et obligation du bailleur → housing ; lecture et contestation d'un acte d'exécution, saisie ou expulsion → enforcement. La présence d'un commissaire de justice ne suffit pas : qualifier l'acte. Le fond locatif reste chez housing ; l'urgence d'un acte est traitée d'abord. |
| Pénal / contentieux | Mesure policière, convocation et procédure pénale → criminal ; chronologie, pièces et rédaction dans un contentieux civil/commercial identifié → litigation. Une même affaire peut donner un volet pénal et un volet civil distincts. Ni subpoena, ni deposition, ni privilège américains ne sont des équivalents présumés. |
| Contentieux / domaines | Un désaccord ou un courrier de réclamation ne bascule pas automatiquement chez litigation. La contestation d'une saisie reste chez enforcement, le litige de travail chez employment ou public-employment. Une tâche générique de chronologie ou de préparation de pièces peut être confiée à litigation sur question bornée, sans lui transférer le raisonnement sectoriel. |
| Logement / travaux / achat / copropriété / urbanisme | Bail et charges locatives → housing ; contrat et défauts des travaux → construction ; acte d'achat/vente → real-estate ; décision collective et charges du copropriétaire → co-ownership ; autorisation publique → planning ; droit privé de passage/nuisance → neighbourhood. L'adresse commune ne fusionne pas les tâches. |
| Famille / succession / protection | Couple et parentalité → family ; transmission et indivision successorale → inheritance ; pouvoirs d'assistance/représentation pour un acte → adult-protection ; reconnaissance/accompagnement de l'autonomie → disability. Le besoin de protection face aux violences est coordonné par domestic-violence, avec volets pénal, familial ou logement distincts. |
| Travail / protection sociale / retraite / public | Relation d'emploi privé → employment ; décision de prestation/indu par une caisse → social-security ; carrière pour pension et liquidation → pension ; emploi public après qualification du statut → public-employment. L'employeur public ne suffit pas à qualifier le contrat. Le statut agricole ne transfère ni paie ni décision MSA à agricultural. |
| Administratif / secteurs | La présence d'une autorité publique ne déplace pas toute demande vers administrative. Les décisions fiscales, scolaires, sociales, d'urbanisme, de séjour ou de carrière publique restent dans leur secteur. Administrative porte une tâche administrative précisément bornée hors secteur identifié. |
| Clinique / orientation / domaines | L'accueil et la supervision restent à la clinique, l'orientation reste un index, l'analyse métier reste au domaine. Une personne peut demander une explication de facture sans installer la clinique ni remplir un profil de cabinet. |

Pour toute interaction, la story indique le plugin principal, la question
confiée au complément, les seuls faits/pièces nécessaires et le résultat attendu.
Si le complément n'est pas installé ou pas adapté, produire une orientation
et signaler cette limite. Ne pas appeler une commande absente, installer un
plugin ou transmettre des pièces automatiquement pour poursuivre.

## Contrat minimal d'un plugin adapté ou créé

| Élément | Contrat à vérifier dans sa story de livraison |
|---|---|
| `.claude-plugin/plugin.json` | Nom canonique, version, description et auteur ; pour un plugin interne, nom/description/auteur cohérents avec le marketplace. Un domaine proposé n'y est inscrit que lorsqu'un lot réel est prêt. |
| `CLAUDE.md` | Modèle de profil livré, pas contexte automatiquement chargé. Chaque skill explique comment lire/créer la configuration utilisateur persistante, hors cache remplacé par une mise à jour. Aucun fait personnel dans le modèle. L'identité et les chemins du fork seront décidés dans BASE-004. |
| `README.md` | Tâches réellement disponibles, public, territoire et limites par skill ; installation seule, configuration, exemples de sortie et intégrations facultatives. Distinguer précisément adapté, hérité et proposé. |
| `skills/<nom>/SKILL.md` | Frontmatter avec `description`, nom canonique cohérent avec les commandes citées ; déclencheur, entrées, exclusions, workflow, sortie et références locales. Un skill métier correspond à une tâche bornée. Les utilitaires existants ne sont pas renommés en masse. |
| Références métier | Dans `references/` du plugin ou `skills/<nom>/references/` ; sources, versions, pièces, modèles et raisonnements propres à la tâche. Un renvoi documentaire vers le backlog ne remplace pas une référence nécessaire à l'exécution. |
| Profil utilisateur | Informations minimales adaptées au public réel : candidat, particulier, aidant, indépendant ou organisation. Un profil d'entreprise partagé peut être facultatif ; aucune installation d'un autre plugin ni profil de l'origine n'est requis. La procédure autonome embarque ses modèles nécessaires. |
| Agents, hooks, `.mcp.json` | Facultatifs, ajoutés seulement si une tâche identifiée en a besoin, avec capacités et effets documentés. Sans intégration, préciser la solution sur fichiers/pièces fournis ou la limite effective. Pas de stubs ajoutés par principe. |

Exemple d'arborescence **proposé**, sans création de ces fichiers dans BASE-003 :

```text
banking-legal/                         # nom proposé, DOM-004
  .claude-plugin/
    plugin.json
  CLAUDE.md                           # modèle de profil, données hors paquet
  README.md                           # périmètre réellement livré
  references/
    shared/
      research-citation-method.md     # copie embarquée, version identifiée
    payment-sources.md                # références métier bancaires
  skills/
    payment-dispute/                  # nom de skill proposé, non disponible
      SKILL.md
      references/
        complaint-outline.md
```

Le nom `payment-dispute` est confirmé par DOM-004 pour BNK-001 ; les autres
noms de cet exemple restent illustratifs. Depuis ce `SKILL.md`, les références communes et bancaires
sont accessibles dans le paquet via `../../references/…`, et le modèle de
réclamation via `references/complaint-outline.md`. Aucun `../../../references/`
vers la racine du dépôt, lien symbolique externe ou téléchargement depuis le
checkout n'est nécessaire.

## Réutilisation transverse et autonomie

**Décision : une méthode source versionnée, des copies embarquées à la
préparation des lots.** BASE-005 rédigera la méthode dans
`references/research-citation-method.md` à la racine (chemin proposé, non créé
ici). Chaque plugin livré en embarquera une copie ordinaire sous
`references/shared/research-citation-method.md`. Les skills liront cette copie.
La racine sert à l'édition et à la synchronisation par les mainteneurs, jamais
à l'exécution du plugin installé.

Le contenu partagé se limite à la qualification territoriale/temporelle pour
la recherche, à la vérification des sources, à leur citation et à la conduite
à tenir si elles sont inaccessibles ou incertaines. Sources sectorielles,
qualification des actes, délais propres, calculs, argumentaires et modèles
métier restent dans le domaine, même quand plusieurs domaines utilisent un
même code. Cette séparation fixe le contenant ; BASE-005 fixera le contenu.

Lors d'une évolution de méthode, sa version et son origine sont inscrites
dans le document ; le lot indique quels plugins ont été synchronisés et
vérifiés. Les copies d'une même version doivent être identiques. Pas de
synchronisation à l'exécution ni de mise à jour automatique : une nouvelle
version est intégrée et relue avec le prochain lot concerné. Un écart de version
est explicite, pas masqué par un lien vers un fichier externe.

Une tâche sectorielle qui utilise des règles de consommation les documente
localement dans ses références métier. Elle ne dépend pas d'un service
juridique commun ni du chargement du plugin consumer. Les duplications utiles
sont suivies lors de l'évolution des domaines ; elles ne deviennent pas une
bibliothèque de raisonnements de tous les domaines à la racine.

Contrôle à formaliser dans [BASE-006](../base-006-controles-paquetage.md) : extraire
un seul paquet dans un dossier isolé, rendre le checkout et les autres plugins
indisponibles, suivre toutes les références nécessaires depuis le skill et
initialiser un profil vierge avec les seuls modèles embarqués. Vérifier aussi
le fonctionnement sans connecteur, ou la limite annoncée s'il est indispensable.
Un simple lien Markdown valide dans le dépôt ne prouve pas cette autonomie.

Les modèles partagés actuellement dans [references/](../../../references/) ne
sont pas embarqués automatiquement. Les renvois hérités qui les supposent
disponibles et les chemins de profil de l'origine restent des écarts à corriger
dans les lots BASE-004, BASE-006 et les adaptations concernées. BASE-003 ne
présente pas le parc actuel comme déjà conforme à ce contrat.

## Vérification du routage sur trois demandes

Relecture d'architecture sur cas fictifs, sans exécuter les skills, déterminer
de délai, trancher un droit au remboursement ou résoudre une consultation.

| Demande et faits discriminants | Plugin / tâche principale | Sortie et interlocuteur | Complément chargé seulement si nécessaire | Résultat du contrôle |
|---|---|---|---|---|
| « Je conteste ce paiement » : obtenir opération, prestataire, pays, dates, validation alléguée et objet recherché. Cas choisi : débit par carte contesté auprès de la banque. | `banking-legal` / qualification du paiement et réclamation, création proposée DOM-004 | Opération identifiée, pièces manquantes et réclamation à la banque/prestataire | Commande non livrée : tâche vendeur chez consumer ; assurance invoquée : question de garantie chez insurance ; faits pénaux allégués : volet criminal. Aucun complément requis pour la seule qualification bancaire. | Propriétaire unique identifié ; paiement non autorisé, virement validé sous tromperie et litige vendeur restent distincts. Tâche non encore disponible. |
| « Je conteste une saisie » : obtenir copie de l'acte, émetteur, nature, notification prouvée, titre allégué et décompte. Cas choisi : acte de saisie bancaire. | `enforcement-legal` / lecture d'acte et préparation des questions de contestation, création proposée DOM-003 | Fiche d'acte, dates établies/incertaines et interlocuteur procédural à identifier | Bien-fondé d'un crédit : banking ; dette locative : housing ; difficultés globales : debt-relief. La banque qui bloque le compte ne devient pas propriétaire de la contestation de l'acte. | Propriétaire unique identifié ; pas de chargement automatique de litigation et pas de suspension promise. Tâche non encore disponible. |
| « Je veux revoir ce contrat de travail » : obtenir contrat/offre, lieu de travail, statut, emploi réel et objectif. Cas choisi : candidat à un emploi salarié privé en France. | `employment-legal:hiring-review`, existant à adapter par PILOTE-002 | Revue clause/source/conséquence/proposition, engagements expliqués et questions au recruteur | Statut public à qualifier : orientation DOM-037 ; décision de caisse distincte : DOM-012 ; pension distincte : DOM-036. Aucun complément pour la seule revue privée. | Nom existant vérifié dans le dépôt ; son adaptation France pour le candidat reste à réaliser. Pas de chargement de tous les domaines sociaux. |

Ces scénarios valident le choix des propriétaires et les critères de passage ;
ils ne valent ni installation isolée ni validation du comportement juridique.

## Couverture des situations du quotidien

La [matrice des usages](../../usages-quotidiens.md) est confrontée aux propriétaires
ci-dessus : toutes ses entrées renvoient soit à un DOM-001 à DOM-043, soit au
travail privé, aux contrats B2B ou aux données personnelles. Chaque renvoi a
donc un plugin principal et une tâche candidate ; aucune entrée n'exige un
plugin généraliste. Les tâches additionnelles restent à prioriser, notamment
dans USAGE-002 ; couverture d'architecture ne signifie pas couverture livrée.

| Public / contrôle concret | Routage retenu et résultat utile | Vérification de frontière |
|---|---|---|
| Particulier : facture de garage, dépôt locatif, courrier du notaire | vehicle → comparaison aux travaux autorisés ; housing → décompte ; inheritance → questions au notaire | Ni commercial pour tout contrat, ni litigation pour toute contestation. |
| Aidant : décision de protection puis accès au dossier médical | adult-protection → pouvoirs pour l'acte ; health → demande d'accès distincte | La qualité d'aidant ne présume pas un pouvoir de représentation ; disability n'absorbe pas ces tâches. |
| Indépendant/artisan : client professionnel impayé | commercial → contrat et réclamation ; enforcement seulement pour l'acte d'exécution distinct | Si le client est un consommateur, qualifier le contrat sectoriel/B2C ; le statut professionnel du demandeur seul ne rend pas le dossier B2B. |
| Petit exploitant : fermage et notification MSA | agricultural → bail et décompte ; social-security → notification de prestation distincte | La pension agricole relève de pension ; un contrat de salarié agricole relève de employment. |
| Retraité/agent public : carrière manquante et décision employeur | pension → correction auprès du régime ; public-employment → décision d'emploi | Pas de fusion de la retraite, de la relation d'emploi et des autres prestations. |

Les sorties restent celles attendues dans les usages : expliquer le document,
les sommes et obligations, distinguer faits et incertitudes, préparer les pièces
et identifier une prochaine étape compréhensible. Les urgences de sécurité ou
de procédure passent avant la revue ordinaire, sans inventer de régime commun
à tous les actes.
