---
id: ENF-001
titre: "Lire un acte d'exécution ou de recouvrement et repérer l'urgence"
statut: proposee
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

1. Maintenant : ce que l'acte présente comme urgent et les deux ou trois actions utiles (relire toutes les pages, joindre l'émetteur au numéro de l'acte, consulter un avocat ou un point d'accès au droit), sans délai calculé.
2. Fiche de l'acte : chaque mention avec son statut (lue, déclarée, absente).
3. Nature probable : relance amiable, acte de procédure ou mesure d'exécution, avec les mentions qui le montrent.
4. Ce qui manque : titre exécutoire, ventilation, pages.
5. Tâche suivante (ENF-002 à ENF-011, proposées) et domaine du fond.
6. Questions au commissaire de justice, au créancier et à un avocat.
7. Limites.

## Travail attendu

Créer `qualification-acte.md` selon le [découpage](../dom-003-decoupage-execution.md)
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
appliquer les couches BASE-006. La [relecture DOM-003](../dom-003-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Contestation rédigée, calcul de délai ou de décompte, recours contre la
décision signifiée, opposition à injonction de payer, saisie immobilière,
examen de la dette d'origine, contact de l'émetteur, paiement, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-003-decoupage-execution.md).
