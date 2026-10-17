---
id: ANM-003
titre: "Vérifier une facture de pension professionnelle pour un chien"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, ANM-001]
---

# ANM-003 — Vérifier une facture de pension professionnelle pour un chien

## Objectif et résultat attendu

Une personne qui conteste un supplément rapproche réservation, contrat,
séjour et facture d'une pension professionnelle en France pour son chien.
Elle obtient les lignes expliquées et un brouillon de demande de justificatifs.

## Périmètre et fichiers

Plugin principal : futur `animal-legal` (`judge-fr-eu-animal-legal`).
Pension professionnelle rémunérée, chien de compagnie, particulier client ;
facturation d'un séjour identifié, hors dommage et diagnostic.

- `animal-legal/skills/dog-boarding-invoice-review/SKILL.md` (à créer).
- `animal-legal/references/facture-pension-chien.md` (à créer).
- `animal-legal/references/qualification-animal.md` — créé par ANM-001, à relire.
- `animal-legal/README.md`, `animal-legal/NOTICE`, `NOTICE` — tâche et traçabilité.
- `animal-legal/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py` — version et métadonnées synchronisées.

Charger méthode locale BASE-005 et socle ANM-001 ; appliquer le contrat du
[découpage](../dom-033-annexes/dom-033-decoupage-animaux.md).

## Pièces et informations nécessaires

Réservation/devis, conditions acceptées et leur date, tarifs, entrée/sortie
prévues et réelles, facture détaillée, paiements, options autorisées, échanges
sur dépassement de séjour ou frais vétérinaires ; seule la pièce de soins
utile au poste contesté, sans dossier vétérinaire complet.

## Sortie attendue

Tableau poste / base contractuelle / quantité / tarif / paiement / justificatif
manquant ; calcul arithmétique reproductible à partir des seules données
fournies, sans somme juridiquement due présumée ; obligations du client et
de la pension, points contestés et brouillon à la pension.

## Travail attendu

Séparer jours/nuitées, prestations incluses, options et frais engagés pour
l'animal. Ne pas inventer le mode de comptage ni considérer une facture comme
preuve de consentement. Si données insuffisantes, donner les inconnues avant
tout total. Examiner aussi retard de reprise et instruction du client.
Une blessure ou disparition ouvre une autre tâche, pas une déduction de remise.

## Références métier et sources à rechercher

Code rural et de la pêche maritime pour activité de garde et détention ;
Code civil pour contrat/preuve ; Code de la consommation selon prestation et
parties, information tarifaire et réclamation. Guides du ministère de
l'Agriculture et de la DGCCRF comme orientation. Textes, versions, exceptions,
transitions et décisions non ouverts dans DOM-033 : lecture BASE-005 et
relecture des sources BASE-014 lors du lot.

## Critères d'acceptation

- [ ] Chaque poste est rattaché à une pièce ou laissé à justifier ; une prestation contestée n'est pas déclarée fictive.
- [ ] Calculs documentés et sommes demandées sont distingués des sommes dues ; engagements et retards du client sont examinés.
- [ ] Le résultat explique en mots courants quoi demander à la pension, sans promesse de remise ni conseil de non-paiement automatique.
- [ ] Le paquet reste autonome sans profil/connecteur ; BASE-006 couvre nominal, limite et absence de source.
- [ ] Phrase finale BASE-013 avec avocat ou juriste compétent, renfort si procédure, échéance ou restitution menacée.
- [ ] Les décisions et textes cités sont tracés selon BASE-005, sans règle mémorisée ni diagnostic.

## Vérification

- Cas normal : facture avec deux promenades supplémentaires, conditions et échanges disponibles : vérifier autorisation et base, préparer la question au professionnel.
- Cas limite : sortie le matin facturée comme une journée entière sans condition fournie : mode de comptage réservé, aucun trop-perçu conclu.
- Cas limite : soins facturés après malaise : autorisation, facture et urgence déclarée distinguées ; pas d'appréciation vétérinaire ni faute présumée.
- Sans source : comparaison pièces/facture et calcul documenté seulement, obligation juridique réservée.

Scénarios **attendus, non exécutés** ; à exécuter selon BASE-006 et USAGE-001
`1.0.0`, avec sortie et ressources conservées. Relecture par l'utilisateur ;
aucune compréhension déclarée sans observation. Aucune tranche sélectionnée.

## Hors périmètre

Garde privée ANM-004, responsabilité pour blessure/disparition en pension
(future tranche), garantie d'assurance DOM-005, recouvrement forcé ou envoi.
