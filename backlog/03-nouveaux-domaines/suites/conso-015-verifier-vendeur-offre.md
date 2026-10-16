---
id: CONSO-015
titre: "Vérifier le vendeur et les informations d’une offre avant achat"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-015 — Vérifier le vendeur et les informations d’une offre avant achat

## Objectif et résultat attendu

Avant de payer, une personne obtient une fiche de vérification du vendeur, du rôle de la plateforme et des informations manquantes dans l’offre. Une identité plausible ou un avis favorable ne devient jamais une certification de fiabilité.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`), installé seul.
Les chemins « à créer » désignent des livrables futurs.

- `consumer-legal/skills/purchase-offer-check/SKILL.md` — le skill (à créer)
- `consumer-legal/references/verification-offre.md` — grille, sources lues et modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche effectivement livrée
- `consumer-legal/.claude-plugin/plugin.json` — version du lot

`qualification-achat.md` (CONSO-001) est relu, pas réécrit. Aucun profil,
agent, hook, connecteur ni stockage durable ajouté.

## Pièces et informations nécessaires

URL et captures datées ; annonce, mentions légales, identité et pays déclarés ; numéro d’immatriculation éventuel ; bénéficiaire du paiement ; prix total, stock, délai et modalités de retour ; avis ou labels contestés.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente ni demander de code bancaire ou de mot de passe.

## Sortie attendue

Fiche des identités concordantes ou divergentes, avec provenance ; tableau offre / justificatif / inconnue ; questions au vendeur ; pièces à archiver ; recommandation conditionnelle sur les vérifications restant à faire avant paiement.

## Travail attendu

Comparer enseigne, vendeur contractuel, registre officiel et bénéficiaire sans assimiler domaine .fr et établissement français. Examiner clone, identité usurpée, dropshipping, faux particulier, avis, labels, origine et publicité d’influence. Signaler un marquage ou un partenariat à vérifier, sans attester authenticité, qualité ou fraude. Une offre personnalisée ou fabriquée à la commande renvoie aussi à CONSO-003 pour la rétractation. Prévoir une checklist avant paiement ; aucun accès automatique ni achat. Les demandes de renseignement ne sont pas envoyées.

Appliquer le contrat commun du [découpage](../dom-001-decoupage-consommation.md),
la méthode locale BASE-005 et le protocole d’orientation USAGE-001.

## Références métier et sources à rechercher

Code de la consommation : information précontractuelle, plateformes, avis et pratiques commerciales ; Annuaire des entreprises et registres pertinents ; DGCCRF sur labels, origine et influence commerciale. Vérifier la portée de chaque registre et marquage.

Pistes non vérifiées ici : ouvrir et dater les sources à la date des faits.
Une page inaccessible ou un conflit entre guide et texte reste explicite.

## Critères d'acceptation
- [ ] O01 produit une fiche vendeur / registre / bénéficiaire et les questions sur les retours et délais.
- [ ] O02 conserve les identités discordantes et l’incertitude d’accès, sans certification de fiabilité.
- [ ] Droit légal, promesse contractuelle et affirmation d’un interlocuteur sont distingués.
- [ ] Aucun délai, montant légal ou effet de démarche n’est affirmé sans source applicable lue.
- [ ] Le paquet détaché reste autonome ; seule la tâche livrée est annoncée, sans envoi.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : O01 — Boutique affichant un drapeau français, mais vendeur tiers étranger et retour non local : comparer les identités et demander le coût du retour.
- Cas limite : O02 — SIREN réel copié sur un clone et avis flatteurs : conserver la divergence sans déclarer le site fiable ; registre ou accès indisponible explicitement signalé.
- Sans source accessible : produire les pièces et questions utiles, avec le point juridique réservé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Certification d’un vendeur ou d’un produit, enquête exhaustive, achat, revue publicitaire pour un professionnel (PDT), plainte pénale.

## Origine et état — 16 octobre 2026

Issue des [155 frictions utilisateur](../dom-001-frictions-utilisateurs.md),
sans implémentation ni sélection. Préalable PILOTE-003 satisfait après BASE-011.
