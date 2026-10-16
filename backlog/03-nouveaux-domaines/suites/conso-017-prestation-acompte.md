---
id: CONSO-017
titre: "Contester l’exécution d’un devis ou le sort d’une avance"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-017 — Contester l’exécution d’un devis ou le sort d’une avance

## Objectif et résultat attendu

Une personne face à une prestation ordinaire inexécutée, des suppléments non acceptés ou une avance retenue obtient une lecture ciblée du devis et un brouillon de réclamation au professionnel.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`), installé seul.
Les chemins « à créer » désignent des livrables futurs.

- `consumer-legal/skills/service-performance-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/prestations-avances.md` — grille, sources lues et modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche effectivement livrée
- `consumer-legal/.claude-plugin/plugin.json` — version du lot

`qualification-achat.md` (CONSO-001) est relu, pas réécrit. Aucun profil,
agent, hook, connecteur ni stockage durable ajouté.

## Pièces et informations nécessaires

Devis et preuve d’acceptation ; nature et lieu de la prestation ; versement et qualification indiquée (arrhes, acompte, autre) ; annulation, interventions, factures et échanges ; demande de travaux supplémentaires ; éléments de l’urgence alléguée.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente ni demander de code bancaire ou de mot de passe.

## Sortie attendue

Fiche des engagements et de l’exécution ; qualification conditionnelle du versement ; tableau des prestations commandées, réalisées et facturées ; justificatifs à demander ; brouillon avec demandes alternatives si les faits restent ouverts.

## Travail attendu

Distinguer accord sur le devis, simple estimation, arrhes et acompte, sans déduire leur qualification du seul libellé ni promettre restitution ou doublement. Examiner preuve de commande des suppléments, facturation de prestations absentes et portée d’une annulation. Un diagnostic alarmiste appelle un second avis technique, sans expertise du skill. Travaux et dépannage à domicile appartiennent à DOM-015, véhicules à DOM-023 ; sans plugin sectoriel livré, CONSO-014 applique seulement les règles générales et annonce les règles manquantes. Rétractation ou paiement hors établissement : CONSO-003 et CONSO-020 selon la question. La tâche reste bornée à une réclamation contractuelle.

Appliquer le contrat commun du [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md),
la méthode locale BASE-005 et le protocole d’orientation USAGE-001.

## Références métier et sources à rechercher

Code civil : formation, force obligatoire, preuve et inexécution ; Code de la consommation : information, avances et prestations ; règles des devis applicables à la prestation. Rechercher le régime précis avant d’utiliser les mots arrhes ou acompte comme conclusion.

Pistes non vérifiées ici : ouvrir et dater les sources à la date des faits.
Une page inaccessible ou un conflit entre guide et texte reste explicite.

## Critères d'acceptation
- [ ] PST01 produit tableau des engagements, qualification conditionnelle de l’avance et contestation des suppléments.
- [ ] PST02 identifie DOM-015 ou le repli CONSO-014, avec les exceptions d’urgence laissées à vérifier.
- [ ] Droit légal, promesse contractuelle et affirmation d’un interlocuteur sont distingués.
- [ ] Aucun délai, montant légal ou effet de démarche n’est affirmé sans source applicable lue.
- [ ] Le paquet détaché reste autonome ; seule la tâche livrée est annoncée, sans envoi.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : PST01 — Prestation photographique annulée, avance conservée et frais supplémentaires facturés sans accord : tableau et brouillon conditionnel.
- Cas limite : PST02 — Serrurier intervenu en urgence au domicile, devis contesté : DOM-015 ou CONSO-014 ; aucun droit sectoriel ni exception d’urgence inventés.
- Sans source accessible : produire les pièces et questions utiles, avec le point juridique réservé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Expertise technique, règlement d’un chantier, régime sectoriel, chiffrage d’indemnité, procédure judiciaire, envoi.

## Origine et état — 16 octobre 2026

Issue des [155 frictions utilisateur](../dom-001-annexes/dom-001-frictions-utilisateurs.md),
sans implémentation ni sélection. Préalable PILOTE-003 satisfait après BASE-011.
