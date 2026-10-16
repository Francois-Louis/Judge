---
id: CONSO-020
titre: "Contester un démarchage ou un contrat imposé sans consentement établi"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-020 — Contester un démarchage ou un contrat imposé sans consentement établi

## Objectif et résultat attendu

Une personne sollicitée au téléphone ou au domicile, ou recevant un produit non commandé, obtient une fiche du consentement contesté, les preuves utiles et un brouillon au professionnel.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`), installé seul.
Les chemins « à créer » désignent des livrables futurs.

- `consumer-legal/skills/solicitation-dispute/SKILL.md` — le skill (à créer)
- `consumer-legal/references/demarchage-consentement.md` — grille, sources lues et modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche effectivement livrée
- `consumer-legal/.claude-plugin/plugin.json` — version du lot

`qualification-achat.md` (CONSO-001) est relu, pas réécrit. Aucun profil,
agent, hook, connecteur ni stockage durable ajouté.

## Pièces et informations nécessaires

Date et canal ; numéro ou identité déclarée du démarcheur ; contrat en cours éventuel ; traces du consentement, offre et support durable ; signature, paiement, livraison ; récit de pression ; urgence alléguée et prestations demandées.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente ni demander de code bancaire ou de mot de passe.

## Sortie attendue

Chronologie et tableau des consentements, déclarations et preuves manquantes ; qualification conditionnelle du contrat ; brouillon de contestation et questions au professionnel ; orientations vers rétractation, signalement ou données selon la demande.

## Travail attendu

Examiner sollicitation téléphonique, vente sous pression, produit non sollicité et paiement anticipé hors établissement. La réforme annoncée dans le texte fourni reste une piste : vérifier publication, entrée en vigueur, transition, exceptions et dispositifs effectifs à la date des faits ; ne pas annoncer fin de Bloctel ou obligation universelle depuis le seul guide. Une relation contractuelle ne prouve pas le consentement à tout démarchage. Les règles de prospection et d’accès aux données relèvent de privacy ; rétractation de CONSO-003 ; signalement de CONSO-013 ; travaux de DOM-015 ou CONSO-014. Ne pas étendre une exception d’urgence à des prestations non demandées.

Appliquer le contrat commun du [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md),
la méthode locale BASE-005 et le protocole d’orientation USAGE-001.

## Références métier et sources à rechercher

Code de la consommation : démarchage téléphonique, contrats hors établissement, consentement, pratiques agressives et fournitures non sollicitées ; lois modificatives et dispositions transitoires. DGCCRF et CNIL pour distinguer canaux et demandes, sans avis global sur un traitement de données.

Pistes non vérifiées ici : ouvrir et dater les sources à la date des faits.
Une page inaccessible ou un conflit entre guide et texte reste explicite.

## Critères d'acceptation
- [ ] DEM01 distingue consentement à la sollicitation et au contrat, puis prépare contestation et demande de preuves.
- [ ] DEM02 sépare urgence et prestations supplémentaires et réserve les règles de transition et exceptions.
- [ ] Droit légal, promesse contractuelle et affirmation d’un interlocuteur sont distingués.
- [ ] Aucun délai, montant légal ou effet de démarche n’est affirmé sans source applicable lue.
- [ ] Le paquet détaché reste autonome ; seule la tâche livrée est annoncée, sans envoi.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : DEM01 — Appel commercial non souhaité puis contrat allégué par le vendeur : préparer contestation et demande de preuve de consentement.
- Cas limite : DEM02 — Intervention urgente au domicile avec prestations supplémentaires et paiement immédiat : qualifier chaque prestation et réserver les exceptions ; changement de régime entre deux dates à vérifier.
- Sans source accessible : produire les pièces et questions utiles, avec le point juridique réservé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Décision d’infraction, revue RGPD, plainte, règle sectorielle non lue, accès à une liste d’opposition, envoi.

## Origine et état — 16 octobre 2026

Issue des [155 frictions utilisateur](../dom-001-annexes/dom-001-frictions-utilisateurs.md),
sans implémentation ni sélection. Préalable PILOTE-003 satisfait après BASE-011.
