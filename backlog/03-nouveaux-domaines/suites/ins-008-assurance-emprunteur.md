---
id: INS-008
titre: "Faire valoir ou changer une assurance emprunteur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-008 — Faire valoir ou changer une assurance emprunteur

## Objectif et résultat attendu

Un emprunteur obtient la lecture d'un refus de prise en charge de ses
échéances, ou prépare un changement d'assurance emprunteur, avec les
conditions à vérifier.

## Périmètre et fichiers

- `insurance-legal/skills/borrower-insurance/SKILL.md` — le skill (à créer)
- `insurance-legal/references/assurance-emprunteur.md` — garanties, changement, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Notice ou contrat d'assurance ; offre de prêt ; questionnaire de santé
signé ; refus ; arrêt de travail ou invalidité déclarés.

## Sortie attendue

Lecture du refus ou des conditions de changement ; questions ; brouillon ;
limites. Les données de santé ne sont demandées que si elles sont
nécessaires, et ne sont pas conservées.

## Travail attendu

Crédit et échéances → DOM-004. Fausse déclaration alléguée : faits à
établir, aucune conclusion ; ne jamais aider à omettre une information au
questionnaire.

## Références métier et sources à rechercher

Code des assurances et Code de la consommation, assurance emprunteur et
changement de contrat ; convention AERAS comme information.

## Critères d'acceptation

- [ ] B01 lit le refus sans conclure sur la fausse déclaration.
- [ ] B02 prépare le changement sans omission conseillée au questionnaire.

## Vérification

- Cas normal : B01 — Refus de prise en charge après un arrêt de travail, motif « affection antérieure ».
- Cas limite : B02 — « Je change d'assurance, dois-je mentionner mon traitement ? »

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Renégociation du prêt, souscription, envoi.

## Complément issu des frictions bancaires

Points 56–58 et 64 de la [matrice utilisateur](../dom-004-frictions-utilisateurs.md).
Recueillir garanties exigées, contrat proposé en délégation, tableau d'équivalence,
motifs du refus de substitution, réception des demandes et changements annoncés
de taux, frais ou conditions du prêt. Pour la couverture : exclusions, carence,
franchise, quotité et critères d'indemnisation, sans collecte de santé superflue.

- [ ] B03 — Refus d'assurance externe : comparer garanties exigées, proposées et motifs ; préparer la demande de réexamen avec textes lus.
- [ ] B04 — Frais ou modification du prêt à cause de la substitution : documenter les conditions avant/après et préparer la question au prêteur, distincte de la garantie ; crédit → BNK-005.
- [ ] B05 — Risque que la personne croyait couvert : expliquer les clauses applicables et les pièces manquantes sans garantie d'indemnisation.

Scénarios B03–B05 **attendus, non exécutés** : refus sans garantie manquante
identifiée, frais d'avenant liés à une assurance externe, incapacité définie
différemment du risque attendu. Sources à ouvrir : libre choix, substitution,
motivation, conditions du crédit et garanties selon les dates des contrats.

## Complément issu des frictions assurance

Points 13 et 60–65 de la [matrice](../dom-005-frictions-utilisateurs.md).

- [ ] B06 — Quotités : distinguer assuré, part de prêt, risque garanti et prestation annoncée ; aucun calcul de prise en charge.
- [ ] B07 — Perte d'emploi : relever statut et cause de cessation, exclusions, carence et franchise ; ne pas présumer qu'une rupture conventionnelle ou un indépendant est couvert.
- [ ] B08 — Substitution : frise ancien/nouveau contrat, acceptation du prêteur, date d'effet, carences et franchises ; ne pas confondre équivalence annoncée et continuité effective.
- [ ] B09 — Questionnaire de santé : vérifier d'abord champ du crédit, montant cumulé par assuré, âge et terme ; ne demander les réponses médicales que si la tâche le nécessite.
- [ ] B10 — Réponse inexacte : conserver question exacte, réponse et preuve du rôle de l'intermédiaire ; intention et sanction non déduites de la seule discordance.

Scénarios B06–B10 **attendus, non exécutés** : quotités distinctes entre coemprunteurs, perte d'emploi non couverte, arrêt traversant la substitution, crédits cumulés et questionnaire réclamé, intermédiaire ayant rempli une réponse. Rechercher l'accord CCSF allégué du 26 mai 2026, son champ et son effet ; aucune règle tirée d'un communiqué seul. L'existence d'un questionnaire signé n'est pas un préalable systématique. Sources et droit dans le temps à vérifier.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
