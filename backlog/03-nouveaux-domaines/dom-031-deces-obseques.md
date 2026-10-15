---
id: DOM-031
titre: "Cadrer un plugin décès et prestations funéraires"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-031 — Cadrer un plugin décès et prestations funéraires

## Objectif

Aider les proches à lire des devis et contrats et à organiser les démarches au moment d'un décès.

Nom de plugin proposé : `funeral-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Comparer un devis funéraire aux prestations demandées et documents contractuels.
- Préparer une réclamation sur une prestation, un financement ou une facture.
- Distinguer volonté du défunt, pouvoir de décision, concession et questions de prise en charge.

## Qualification et frontières

Qualité et souhaits des personnes, volontés connues, urgence, devis/contrats, signataire, facture et intervenants.

Les prestations et décisions funéraires sont ici ; le règlement de la succession reste en DOM-016 et la garantie d'un contrat d'assurance en DOM-005.

## Sources à prévoir et vérifier

Code général des collectivités territoriales pour le funéraire, Code civil, Code de la consommation et textes sectoriels ; informations officielles des collectivités et de la DGCCRF.

- [DGCCRF](https://www.economie.gouv.fr/dgccrf)
- [Service Public — frais d'obsèques](https://www.service-public.gouv.fr/particuliers/vosdroits/F17059?lang=fr)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un devis funéraire et préparer les demandes d'explication avant engagement, avec un besoin limité et explicite.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage distingue signataire du contrat, personne habilitée à décider et personne éventuellement tenue au paiement ; aucune réponse unique n'est déduite du seul lien familial.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Des prestations apparaissent sans avoir été demandées.
- Plusieurs proches sont en désaccord sur une décision.
- Un opérateur réclame un paiement et les signataires ne sont pas identifiés.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

