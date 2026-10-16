---
id: DOM-006
titre: "Cadrer un plugin logement locatif et habitat"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-006 — Cadrer un plugin logement locatif et habitat

## Objectif

Aider locataires, occupants et petits bailleurs à comprendre le bail, les sommes réclamées et les démarches concernant l'habitation.

Nom de plugin proposé : `housing-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Location vide/meublée, résidence principale ou autre, parc privé/social, qualité de l'occupant et localisation.
- Tâches candidates : revue de bail, dépôt de garantie, réparations/décence, charges récupérables, congé et demande au bailleur.
- Distinguer les obligations du bailleur envers l'occupant et le litige avec une entreprise de travaux ; les responsabilités et interlocuteurs diffèrent.
- Prévoir les frontières avec [construction et travaux](dom-015-construction-travaux.md), [achat immobilier](dom-017-transactions-immobilieres.md), [copropriété](dom-018-copropriete.md), [urbanisme](dom-019-urbanisme-foncier.md) et [voisinage](dom-020-voisinage-servitudes.md). L'acte d'exécution ou d'expulsion reste en DOM-003.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code civil, textes locatifs et de copropriété, Code de la construction et de l'habitation, textes locaux pertinents, ANIL/ADIL.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de contestation d'une retenue sur dépôt de garantie, avec régime locatif borné.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites (relecture documentaire du rédacteur).
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (attendus, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un dépôt de garantie retenu après l'état des lieux.
- Un congé reçu pour un bail meublé.
- Une régularisation de charges locatives sans justificatifs fournis.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Besoin issu des frictions des commissaires de justice

Points 35–36 de la [matrice utilisateur](dom-003-annexes/dom-003-frictions-utilisateurs.md) : au futur découpage, prévoir une tâche bornée sur l'arriéré locatif et les conditions d'une demande de délais ou de suspension de clause résolutoire. Recueillir bail et régime, commandement et signification, décompte et paiements, état du procès, reprise du loyer courant, ressources, charges et aides sollicitées. La sortie attendue explique les conditions à vérifier, les pièces et l'interlocuteur ; la préparation d'une demande judiciaire doit recevoir sa propre story.

Scénarios **attendus, non exécutés** : commandement assimilé à une expulsion immédiate ; locataire ayant repris le loyer courant et souhaitant demander un étalement. Vérifier les textes locatifs, leurs dispositions transitoires et les conditions du pouvoir du juge, sans reprendre les durées du texte fourni. ENF-005 garde la lecture des actes et de l'expulsion ; aucune tâche logement n'est livrée par ce complément.

## Complément des frictions données personnelles — 16 octobre 2026

Le point 44 de la [matrice données personnelles](../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md) demande de découper le contrôle d'un dossier locatif : bail, candidat/garant, liste de justificatifs autorisés et version applicable, finalité et conservation après refus. PRV-026 qualifie la collecte, PRV-024 prépare l'effacement ciblé. Scénario attendu : pièces intrusives et candidature refusée conservée, avec contrôle de liste et demande de données distincts. Aucun dossier entier sensible à collecter par défaut ; portée et contrôles dans la matrice.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-006-annexes/dom-006-decoupage-logement.md) : nom `housing-legal`
  conservé, identifiant futur `judge-fr-eu-housing-legal` ; qualification
  bail/usage/parc/parties/localisation/dates ; frontières et installation seule,
  références locales, sans agent, connecteur, hook ni profil requis.
- Onze propositions LOG-001 à LOG-011, une tâche par skill, en quatre rangs.
  LOG-001 crée le paquet avec la seule contestation de retenues après une
  location privée vide de résidence principale en France métropolitaine.
  Meublé, social et autres régimes restent hors de cette première tranche.
- Réparation au bailleur et recours contre l'entreprise distincts ; charges,
  revue du bail, décence et deux congés séparés. LOG-008/009/010 découpent
  décompte, conditions de délais/suspension de clause et préparation judiciaire.
  LOG-011 contrôle les justificatifs de candidature avec relais PRV-026/024.
- [Vérification documentaire](dom-006-annexes/dom-006-verification.md) : trois
  scénarios de la story, compléments exécution/données et cas de frontière.
  [Relevé statique](dom-006-annexes/dom-006-resultats.json) produit par le
  [contrôleur](dom-006-annexes/dom-006-controles.py).
- Matrice BASE-003, relais ENF-005 et matrice données précisés ; famille LOG
  ajoutée au générateur de l'état du backlog et index régénéré.

PILOTE-003 a été relu : terminé après BASE-011, avec limites de PILOTE-002
toujours explicites. Aucune suite n'est sélectionnée par ce cadrage.

Fichiers du lot : présente story, quatre annexes (découpage, vérification,
contrôleur, relevé), onze suites `suites/log-*.md`, ligne BASE-003, relais
ENF-005, ligne 44 de la matrice données, `backlog/etat.py` et `backlog/ETAT.md`.
Tout reste dans `backlog/` ; aucune entrée NOTICE requise.

**Portée :** relecture documentaire du seul rédacteur sur pièces fictives
et contrôles statiques ; aucun plugin créé, skill exécuté, paquet installé,
lecteur réel ou indépendant, source juridique ouverte, délai ou montant établi,
envoi ou saisine. Voir la vérification pour les réserves et scénarios attendus.
