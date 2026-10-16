---
id: DOM-010
titre: "Cadrer un plugin de droit administratif"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-010 — Cadrer un plugin de droit administratif

## Objectif

Prévoir les demandes à l'administration et les recours dans un domaine distinct des contentieux civils.

Nom de plugin proposé : `administrative-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Administration, objet, demande ou décision, notification, délai et éventuel recours préalable.
- Tâches candidates : lecture de décision, demande d'accès aux documents, recours administratif et préparation d'un dossier.
- Identifier les régimes spéciaux et les frontières avec fiscalité et protection sociale ; leur présence n'autorise pas un délai générique.
- Les [actes d'urbanisme](dom-019-urbanisme-foncier.md), le [séjour/nationalité/asile](dom-028-sejour-nationalite-asile.md), les [décisions d'emploi public](dom-037-fonction-publique.md) et la [scolarité](dom-027-education-formation.md) sont orientés vers leurs cadrages métier. L'existence d'une administration ne suffit pas à choisir ce plugin général.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

CRPA, Code de justice administrative et textes sectoriels ; Service Public, Conseil d'État et CADA selon l'objet.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture d'une décision et de ses voies de recours, avec régime borné.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une décision notifiée avec voies de recours.
- Une demande restée sans réponse.
- Un refus d'accès à un document administratif.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Complément des frictions IA — 16 octobre 2026

Points 7–8, 28 et 49–50 de la [matrice IA](../02-plugins-existants/exist-005-frictions-utilisateurs.md) : découper la demande d'informations sur un traitement algorithmique fondant une décision individuelle, puis la lecture du refus de communication et les suites CADA/contentieuses. Recueillir décision, administration, notification/réception, règles/paramètres/sources demandés, réponse et preuve ; rechercher CRPA dont L311-3-1 et textes d'application, CJA et compétences/préalables CADA. Résultats séparés : brouillon d'accès et fiche de voie/calendrier, sans code source intégral promis ni demande d'explication réputée recours au fond. Les délais du tableau utilisateur ne sont pas des valeurs par défaut. Éducation, caisse, fiscalité et emploi public gardent le recours à leur décision. Cas attendus : demande d'explication encore en cours et recours distinct urgent ; refus de communication puis réponse administrative après CADA, avec chronologies séparées.

Ces exigences restent à découper ou préciser ; [portée et contrôles de l'intégration](../02-plugins-existants/exist-005-frictions-verification.md).

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.


## Complément issu des frictions police/pénal — 16 octobre 2026

La [matrice des 97 situations](dom-002-frictions-utilisateurs.md), notamment les points 74–75, 79, 97 et la section 7, ajoute les exigences de cadrage suivantes. DOM-010 reste proposé ; ces réponses au fond demandent encore des stories bornées, sans plugin créé ici.

- FPS : distinguer stationnement payant et contravention de stationnement interdit ; recueillir avis, auteur, lieu, dates d'envoi et de notification, paiement, majoration, recours déjà tenté et réponses. Prévoir lecture du FPS, brouillon de RAPO puis orientation ou préparation contentieuse dans des tâches distinctes, selon compétence et préalables vérifiés. Séparer effets sur paiement et recours : aucune suspension présumée ni délai tiré du tableau utilisateur.
- Permis : CRIM-023 identifie rétention et dépistage, CRIM-010 lit points et invalidation ; DOM-010 devra découper les recours contre suspension ou invalidation administrative. Recueillir décision complète, autorité, notification, mesures pénales parallèles, demandes et preuves ; sortie future : régime, acte attaqué, préalable, pièces, voie et urgence à vérifier. Aucun droit de conduire ni restitution automatique déduit du temps écoulé.
- Décision administrative incomprise : qualifier la nature et le secteur avant toute voie de recours. Fichier TAJ → CRIM-022 ; décision d'emploi public → DOM-037 ; ordonnance pénale → CRIM-006.

Scénarios de découpage **attendus, non exécutés** : FPS pris pour amende, RAPO déposé alors que le paiement reste une question distincte, FPS majoré après silence, avis de rétention suivi d'une décision préfectorale, invalidation confondue avec condamnation. Sources à rechercher : textes du stationnement payant et compétence juridictionnelle actuelle, Code de la route, CJA et textes de notification selon l'acte ; aucun régime spécial ramené au délai administratif de droit commun.

## Complément — formalités d'entreprise, 16 octobre 2026

Les points 88–90 et 96–97 de la [matrice formalités](../02-plugins-existants/exist-002-frictions-utilisateurs.md) ne créent pas un recours administratif universel. SOC-023 lit le dossier de société, DOM-039 celui de l'EI et ses décisions Urssaf, DOM-011 le contentieux fiscal. Qualifier auteur, nature et régime de l'acte avant de choisir voie, préalable ou juge : INPI opérateur, autorité validatrice et registre ne sont pas interchangeables. DOM-010 n'intervient qu'après cette qualification si une tâche administrative résiduelle est établie, à découper séparément. Un ticket d'assistance ne prouve ni dépôt de recours ni suspension. Portée : intégration documentaire décrite dans la matrice.

## Complément des frictions données personnelles — 16 octobre 2026

Le point 60 de la [matrice données personnelles](../02-plugins-existants/exist-003-frictions-utilisateurs.md) demande de préserver le calendrier propre d'une décision administrative pendant une demande RGPD. PRV-034 prépare la plainte CNIL ; recours contre une décision de l'autorité à qualifier et découper selon acte, compétence, notification et représentation, sans le confondre avec une réclamation adressée au responsable du traitement. Le seul statut public du responsable ne fixe pas toutes les voies de réparation. Scénario attendu : demande d'accès en cours et échéance de recours distincte ; aucun effet suspensif déduit. Portée et contrôles : voir la matrice.

## Complément du 16 octobre 2026 : régularité d'une décision administrative

Par décision de l'utilisateur ([décisions](../decisions-2026-10-16.md)), le futur
découpage prévoit une tâche de repérage prudent des points de régularité d'une
décision administrative : auteur et compétence apparente, motivation, procédure
contradictoire préalable annoncée, mention des voies et délais de recours,
notification. La sortie liste des points à soumettre à un avocat ou à un
juriste, avec l'urgence liée au délai de recours, sans conclure à
l'illégalité ; les décisions d'un domaine spécialisé (fiscalité, caisse,
urbanisme, séjour, emploi public) gardent leur propriétaire. Sources à
vérifier : Code des relations entre le public et l'administration, Code de
justice administrative et textes spéciaux.

## Complément des frictions contentieuses — 16 octobre 2026

Exigences issues des [125 frictions contentieuses](../02-plugins-existants/exist-006-frictions-utilisateurs.md), sans implémentation ni sélection de tranche.

Points 31 et 106–115, tableau §1 et checklist : découper en tâches bornées la lecture d’une décision implicite, le préalable obligatoire, le recours gracieux, le dossier de requête et sa preuve d’enregistrement, la demande indemnitaire préalable et son articulation avec l’annulation, l’urgence administrative et la lecture des communications/clôture. Recueillir demande initiale, objet, auteur, compétence, décisions, notifications/publications, dates et reçus, échanges et recours déjà formés. Prévoir comme sorties régime retenu, pièces manquantes, calendrier propre, démarche et interlocuteur ; aucune suspension présumée ni application universelle de la jurisprudence Czabaj citée par le guide.

La sécurité sociale garde DOM-012 et son ordre de juridiction qualifié ; fiscalité, séjour, urbanisme et emploi public gardent leurs domaines. Scénarios de découpage : silence avec régime inconnu ; recours gracieux avant demande indemnitaire ; requête sans décision jointe ; communication à régulariser et clôture imminente. Textes à rechercher : CRPA, CJA, régimes spéciaux et jurisprudence sur connaissance et délai raisonnable.

Les scénarios indiqués sont attendus, non exécutés. Sources/version, champ, déclencheur, exceptions et transitions restent à rechercher ; le texte fourni n’est pas une autorité juridique.
