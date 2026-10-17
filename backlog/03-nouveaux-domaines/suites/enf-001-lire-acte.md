---
id: ENF-001
titre: "Lire un acte d'exécution ou de recouvrement et repérer l'urgence"
statut: a-verifier
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# ENF-001 — Lire un acte d'exécution ou de recouvrement et repérer l'urgence

## Objectif et résultat attendu

Une personne qui reçoit un courrier ou un acte lié à une dette comprend ce
qu'est le document, ce qui est urgent, ce qui manque et à qui s'adresser,
sans promesse de suspension. Cette tranche crée le paquet `enforcement-legal`
avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `enforcement-legal` (`judge-fr-eu-enforcement-legal`).
Les chemins « à créer » sont des livrables futurs.

- `enforcement-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0` (à créer)
- `enforcement-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `enforcement-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `enforcement-legal/NOTICE` — entrée datée du lot (à créer)
- `enforcement-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `enforcement-legal/references/shared/research-citation-method.md` — copie BASE-005 `1.0.0` identique (à créer)
- `enforcement-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `enforcement-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `enforcement-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `enforcement-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `enforcement-legal/references/qualification-acte.md` — qualification commune et garde-fous (à créer)
- `enforcement-legal/skills/enforcement-act-reading/SKILL.md` — le skill (à créer)
- `enforcement-legal/skills/enforcement-act-reading/references/lecture-acte.md` — types d'actes, mentions, sources lues, modèle de fiche (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Acte ou courrier complet, toutes pages, y compris le décompte et les annexes.
- Émetteur, signataire, coordonnées ; créancier pour le compte duquel il agit.
- Titre de l'acte et titre exécutoire visé (décision, date, juridiction).
- Mode de remise indiqué, date portée par l'acte, avis de passage, date de découverte déclarée.
- Montants indiqués et paiements déjà faits.
- Autres dettes, procédure de surendettement, mesure de protection, qualité d'héritier.

Sans pièce, le skill travaille sur la description, marquée comme déclarée, et
demande d'abord le titre du document et sa date.

## Sortie attendue

1. Maintenant : ce que l'acte présente comme urgent et les deux ou trois actions utiles (relire toutes les pages, joindre l'émetteur par des coordonnées officielles vérifiées, consulter un avocat ou un point d'accès au droit), sans délai calculé.
2. Fiche de l'acte : chaque mention avec son statut (lue, déclarée, absente).
3. Nature probable : relance amiable, acte de procédure ou mesure d'exécution, avec les mentions qui le montrent.
4. Ce qui manque : titre exécutoire, ventilation, pages.
5. Tâche suivante (ENF-002 à ENF-019, proposées) et domaine du fond.
6. Questions au commissaire de justice, au créancier et à un avocat.
7. Limites.

## Travail attendu

Créer `qualification-acte.md` selon le [découpage](../dom-003-annexes/dom-003-decoupage-execution.md)
et l'appliquer :

- demande de paiement par SMS, lien ou virement urgent → authenticité vérifiée par un canal officiel d'abord ;
- assignation ou convocation à une audience → orientation contentieux, pas d'acte d'exécution ;
- ordonnance d'injonction de payer signifiée → urgence signalée, préparation de l'opposition par ENF-012 (proposée) ;
- commandement de quitter les lieux → bloc d'urgence et ENF-005 ;
- plusieurs dettes ou saisies → orientation DOM-024 ;
- dette d'un défunt → DOM-016 d'abord ;
- acte d'un comptable public ou d'un organisme social → lecture ici, contestation au domaine du fond.

Charger la méthode locale BASE-005 et citer les sources réellement lues dans
`lecture-acte.md`. Ne jamais conseiller de soustraire un bien ou de vider un
compte pour échapper à une saisie.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, titres exécutoires (pistes L111-2,
L111-3) ; Code de procédure civile, signification (pistes 653 et suivants) ;
annuaire officiel de la profession pour l'authenticité, à identifier.

## Critères d'acceptation

- [ ] A01 qualifie une relance sans titre comme amiable, sans annoncer de saisie.
- [ ] A02 distingue date portée par l'acte et date déclarée, signale l'urgence sans calculer de délai.
- [ ] A03 relève l'absence de ventilation et renvoie vers ENF-003 et ENF-004.
- [ ] A04 traite d'abord l'authenticité d'une demande par SMS.
- [ ] Aucune promesse de suspension ; la sortie se comprend sans formation juridique ; le paquet détaché fonctionne seul.

## Vérification

- Cas normal : A01 — Lettre d'une société de recouvrement pour un ancien abonnement, menace de « saisie sous 8 jours ».
- Cas limite : A02 — Signification d'un jugement remise « à l'étude », avis de passage trouvé tardivement.
- Cas limite : A03 — Dénonciation d'une saisie sur compte, total sans détail.
- Cas limite : A04 — SMS « commissaire de justice » avec lien de paiement.
- Sans source lue : fiche et questions, règle réservée.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-003](../dom-003-annexes/dom-003-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Contestation rédigée, calcul de délai ou de décompte, recours contre la
décision signifiée, opposition à injonction de payer, saisie immobilière,
examen de la dette d'origine, contact de l'émetteur, paiement, envoi.

## Complément issu des frictions des commissaires de justice

Points 1–2, 11, 15–18 et 45 de la [matrice utilisateur](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

- [ ] A05 — Mise en demeure et jugement : qualifier par les mentions, pas par le seul papier à en-tête ; absence de titre mentionné ne prouve pas l'absence de tout titre ni de possibilité de mesure conservatoire.
- [ ] A06 — Jugement signifié et appel envisagé : relever voies de recours, exécution provisoire mentionnée, juridiction et mode de remise ; orienter vers un avocat sans calcul ni promesse d'arrêt de l'exécution.
- [ ] A07 — Page manquante ou mention apparemment erronée : relever précisément l'absence et demander la pièce ; ne pas annoncer la nullité pour une coquille.
- [ ] A08 — Réclamation au cabinet ou à une chambre en cours : distinguer cette démarche du recours adapté et garder son urgence ; inclure la liste de contrôle identité officielle, type d'acte, dates, titre, décompte, paiements et pièces conservées.

Scénarios A05–A08 **attendus, non exécutés** : lettre menaçante sans titre ; jugement avec exécution provisoire et appel envisagé ; acte incomplet ; attente d'une réponse amiable pendant une mesure. Sources à rechercher : effets de la signification, voies de recours et exécution provisoire selon la décision. Prescription de la créance, durée d'exécution du titre et forclusion restent des qualifications distinctes, sans calcul dans ENF-001.

## Livraison et vérification — 17 octobre 2026

La demande d'implémentation sélectionne ENF-001 et la création du paquet,
y compris l'entrée marketplace et l'ajustement de l'inventaire BASE-008.
`enforcement-legal` `0.1.0` livre uniquement enforcement-act-reading. Les
fichiers annoncés « à créer » ci-dessus sont maintenant livrés. La méthode
BASE-005 actuelle `1.2.0` remplace la `1.0.0` du cadrage, à l'identique.
Pas de profil, agent, hook, connecteur, stockage durable ou autre skill créé.

L'implémentation couvre les gardes A01–A08 et les frontières DOM-003. Les
cases d'acceptation restent ouvertes : elles ne valent pas réussite de
scénarios non exécutés. Le client reconnaît le paquet détaché et la commande,
mais sa limite de session bloque A01 avant toute lecture du skill et réponse
métier. A02–A08 et les cinq autres fixtures restent non exécutées. Le scénario
sans source normative relue est préparé, pas validé en exécution.

Le [bilan par couche BASE-006](enf-001-annexes/verification.md), les
[13 fixtures](enf-001-annexes/fixtures.json), l'[exécuteur](enf-001-annexes/recette.py),
les [traces client](enf-001-annexes/executions/results.json) et les
[contrôles et empreintes](enf-001-annexes/validation.json) distinguent les
résultats statiques, le schéma, la limite client et la recette restant à faire.
Les accès et réserves des sources sont consignés dans lecture-acte.md livré.
Une installation en environnement réellement isolé et une lecture par une
personne sans formation juridique restent à recetter. Statut `a-verifier`.
