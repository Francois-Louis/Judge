---
id: DOM-015
titre: "Cadrer un plugin construction et travaux"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-015 — Cadrer un plugin construction et travaux

## Objectif

Aider les particuliers à examiner un devis, documenter un chantier défaillant et préparer les démarches face à l'entreprise concernée.

Nom de plugin proposé : `construction-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Revoir un devis et les conditions de paiement avant signature.
- Documenter retard, abandon de chantier, prestation non réalisée ou facturation supplémentaire.
- Préparer une réception, des réserves ou une réclamation pour malfaçons selon le contrat et le stade des travaux.

## Qualification et frontières

Type de travaux et de contrat, qualité du client et des intervenants, devis/avenants, paiements, chronologie, réception alléguée, réserves, désordres et attestations d'assurance.

L'exécution et les défauts des travaux sont ici. Le permis relève de DOM-019, l'achat immobilier de DOM-017, la décision de copropriété de DOM-018 et l'analyse du refus de garantie du domaine assurance.

## Sources à prévoir et vérifier

Code civil, Code de la construction et de l'habitation, Code de la consommation selon le contrat, textes et jurisprudence propres aux garanties et responsabilités.

- [Garanties après réception — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F2958)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Revoir un devis de rénovation d'un particulier et identifier les clauses ou pièces manquantes avant signature.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] La qualification du contrat, du désordre et de la réception est prévue avant de proposer un régime de garantie ; aucune garantie n'est appliquée à tous les travaux.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un artisan demande un supplément sans avenant fourni.
- Un chantier reste inachevé après plusieurs acomptes.
- Une fuite apparaît après des travaux dont la réception est discutée.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Complément des frictions logement — 16 octobre 2026

Points 56, 123–124 ; relais 41–43, 49, 52–55 de la [matrice logement](dom-006-annexes/dom-006-frictions-utilisateurs.md).

Découper la revue de facture/devis/avenant, la conservation de preuve avant remise en état et la demande à l'entreprise responsable d'un désordre. Pièces : contrat, réception, photos originales, rapports, devis/factures et urgence. Sorties : rapprochement prestation/coût/accord et dossier contradictoire à préparer ; un devis ne prouve pas seul la nécessité ou l'imputabilité. Séparer mesures conservatoires et réparations définitives, sans retarder la sécurité. LOG-004/005 gardent la demande au bailleur ; DOM-018 la décision et les comptes de copropriété ; INS-017 l'assurance.

- [ ] Le futur découpage attribue à chaque tâche ses entrées, sortie, sources, limites et scénarios, y compris les voies urgentes distinctes.

Scénarios **attendus, non exécutés** : Fuite après travaux et devis élevé, remise en état prévue avant expertise : documenter état et sécurité, demander base contractuelle et préserver preuve sans attribuer automatiquement la responsabilité.
Les textes, versions, transitions, seuils et échéances seront vérifiés sur
sources officielles lors des implémentations. Ce complément ne termine pas
le cadrage, ne crée aucun plugin et n'exécute aucune démarche externe.
