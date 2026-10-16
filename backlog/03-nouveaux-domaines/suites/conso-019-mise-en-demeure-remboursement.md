---
id: CONSO-019
titre: "Préparer une mise en demeure et suivre un remboursement contesté"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-019 — Préparer une mise en demeure et suivre un remboursement contesté

## Objectif et résultat attendu

Après une réclamation infructueuse ou un remboursement promis mais absent, une personne obtient une chronologie, un état des sommes et un brouillon de mise en demeure adapté à la demande déjà qualifiée.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`), installé seul.
Les chemins « à créer » désignent des livrables futurs.

- `consumer-legal/skills/claim-escalation/SKILL.md` — le skill (à créer)
- `consumer-legal/references/mise-en-demeure-remboursement.md` — grille, sources lues et modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche effectivement livrée
- `consumer-legal/.claude-plugin/plugin.json` — version du lot

`qualification-achat.md` (CONSO-001) est relu, pas réécrit. Aucun profil,
agent, hook, connecteur ni stockage durable ajouté.

## Pièces et informations nécessaires

Commande, fondement déjà identifié ou à confirmer ; réclamation et preuve de réception ; réponse ou silence ; notification de rétractation ou résolution et retour éventuel ; sommes payées, promises et reçues ; offre d’avoir ou de transaction ; démarches parallèles.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente ni demander de code bancaire ou de mot de passe.

## Sortie attendue

Fiche des faits et du fondement réservé ou confirmé ; rapprochement des sommes avec justificatifs ; brouillon de mise en demeure, destinataire et preuve de réception à conserver ; tableau des suites, effets et échéances à vérifier.

## Travail attendu

Accepter un dossier fourni manuellement sans exiger l’exécution d’un autre skill. Ne pas requalifier automatiquement un retard en résolution : revenir à CONSO-001 pour la livraison, CONSO-002 pour le défaut, CONSO-003 pour la rétractation, CONSO-017 pour la prestation. Distinguer délai de réponse proposé et délai légal, notification et réception, remboursement dû et avoir volontaire. Examiner portée d’une transaction ou renonciation avant acceptation, sans la recommander automatiquement. Aucun calcul de majoration sans texte, assiette, dates et conditions lus. Médiation : CONSO-006 ; conciliation, tentative amiable obligatoire et voie judiciaire : orientation EXIST-006 ; banque et plainte restent distinctes. Ne présumer aucun effet suspensif ou interruptif d’une relance, d’un signalement ou d’une mise en demeure.

Appliquer le contrat commun du [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md),
la méthode locale BASE-005 et le protocole d’orientation USAGE-001.

## Références métier et sources à rechercher

Code civil : mise en demeure, inexécution, résolution, prescription et transaction ; Code de la consommation : remboursement et majorations selon le fondement ; règles de procédure civile et information officielle pour identifier le relais, sans rédiger d’acte de procédure.

Pistes non vérifiées ici : ouvrir et dater les sources à la date des faits.
Une page inaccessible ou un conflit entre guide et texte reste explicite.

## Critères d'acceptation
- [ ] MD01 produit chronologie, rapprochement des sommes et brouillon lié au fondement déjà documenté.
- [ ] MD02 relève montant, renonciation et réception inconnue, sans accepter la transaction ni calculer une échéance.
- [ ] Droit légal, promesse contractuelle et affirmation d’un interlocuteur sont distingués.
- [ ] Aucun délai, montant légal ou effet de démarche n’est affirmé sans source applicable lue.
- [ ] Le paquet détaché reste autonome ; seule la tâche livrée est annoncée, sans envoi.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : MD01 — Commande résolue après démarche documentée, remboursement toujours absent : état des sommes et brouillon selon les sources lues.
- Cas limite : MD02 — Avoir partiel assorti d’une renonciation générale et date de réception inconnue : relever la portée, réserver l’échéance et orienter vers un avis adapté avant choix.
- Sans source accessible : produire les pièces et questions utiles, avec le point juridique réservé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Acte judiciaire, décision de prescription, transaction acceptée à la place de l’utilisateur, calcul sans sources, envoi.

## Origine et état — 16 octobre 2026

Issue des [155 frictions utilisateur](../dom-001-annexes/dom-001-frictions-utilisateurs.md),
sans implémentation ni sélection. Préalable PILOTE-003 satisfait après BASE-011.
