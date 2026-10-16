---
id: CONSO-018
titre: "Contester une décision de protection d’achat ou de vente d’une plateforme"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-018 — Contester une décision de protection d’achat ou de vente d’une plateforme

## Objectif et résultat attendu

Un acheteur ou un vendeur particulier obtient une fiche de la protection contractuelle proposée par la plateforme, les preuves à préserver et un brouillon de contestation interne ciblé.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`), installé seul.
Les chemins « à créer » désignent des livrables futurs.

- `consumer-legal/skills/platform-protection-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/protection-plateforme.md` — grille, sources lues et modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche effectivement livrée
- `consumer-legal/.claude-plugin/plugin.json` — version du lot

`qualification-achat.md` (CONSO-001) est relu, pas réécrit. Aucun profil,
agent, hook, connecteur ni stockage durable ajouté.

## Pièces et informations nécessaires

Conditions de protection dans la version acceptée ; annonce et échanges ; statut de paiement et remise ; notification de clôture et date de réception ; historique du dossier ; photos, poids et numéros de série disponibles.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente ni demander de code bancaire ou de mot de passe.

## Sortie attendue

Chronologie ; tableau règle contractuelle / fait / pièce / inconnue ; échéances internes séparées des délais légaux ; brouillon de réexamen ; démarches distinctes contre le vendeur, l’acheteur ou l’intermédiaire selon le contrat.

## Travail attendu

Distinguer plateforme vendeuse, intermédiaire et prestataire d’une protection. Traiter clôture automatique, confirmation de réception demandée trop tôt, retour d’un autre objet et colis prétendu vide. Ne jamais inventer une preuve, une signature ou une vidéo. Une transaction hors plateforme reçoit les limites de protection à vérifier. Ne pas confondre décision interne et extinction des recours civils. Le litige entre particuliers reste CONSO-011 ; modération et suppression de compte relèvent de DOM-034 ; fraude et paiement vont à CRIM-004, BNK-001 ou BNK-002. Aucun accès au compte ni dépôt de recours.

Appliquer le contrat commun du [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md),
la méthode locale BASE-005 et le protocole d’orientation USAGE-001.

## Références métier et sources à rechercher

Conditions contractuelles exactes de la protection, Code civil et Code de la consommation sur l’information des plateformes selon les parties. DSA et autres règles numériques seulement si une décision distincte relève de DOM-034.

Pistes non vérifiées ici : ouvrir et dater les sources à la date des faits.
Une page inaccessible ou un conflit entre guide et texte reste explicite.

## Critères d'acceptation
- [ ] MP01 distingue clôture de protection, dates internes et demande au vendeur, puis prépare le réexamen.
- [ ] MP02 rapproche identifiants disponibles et objet retourné, sans accusation ni échéance interne inventée.
- [ ] Droit légal, promesse contractuelle et affirmation d’un interlocuteur sont distingués.
- [ ] Aucun délai, montant légal ou effet de démarche n’est affirmé sans source applicable lue.
- [ ] Le paquet détaché reste autonome ; seule la tâche livrée est annoncée, sans envoi.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : MP01 — Achat jamais reçu, protection close automatiquement : produire une contestation interne sur les dates et garder la demande au vendeur distincte.
- Cas limite : MP02 — Vendeur particulier recevant un autre appareil en retour : comparer les numéros disponibles sans présumer la fraude ; délai interne inconnu réservé.
- Sans source accessible : produire les pièces et questions utiles, avec le point juridique réservé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Litige de modération, remboursement bancaire, décision sur la fraude, connexion au compte, dépôt ou envoi.

## Origine et état — 16 octobre 2026

Issue des [155 frictions utilisateur](../dom-001-annexes/dom-001-frictions-utilisateurs.md),
sans implémentation ni sélection. Préalable PILOTE-003 satisfait après BASE-011.
