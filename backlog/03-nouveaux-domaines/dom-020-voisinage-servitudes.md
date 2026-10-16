---
id: DOM-020
titre: "Cadrer un plugin voisinage et servitudes"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-020 — Cadrer un plugin voisinage et servitudes

## Objectif

Aider à documenter les conflits de voisinage et à choisir une démarche proportionnée.

Nom de plugin proposé : `neighbourhood-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer une chronologie et les pièces de nuisances sonores, fumées ou autres troubles allégués.
- Lire une demande concernant arbres, clôture, mitoyenneté, limite ou passage.
- Préparer un échange écrit, une conciliation ou un dossier contentieux selon l'objet.

## Qualification et frontières

Qualité des occupants/propriétaires, localisation, titre, plan et éventuelle servitude, dates, récurrence, preuves obtenues et échanges.

Le conflit entre voisins est ici ; permis et décisions publiques vont en DOM-019, pollution en DOM-030 et règles propres à la copropriété en DOM-018.

## Sources à prévoir et vérifier

Code civil, textes nationaux et locaux pertinents, règles de preuve et de procédure, décisions utiles selon la situation.

- [Service Public](https://www.service-public.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Préparer une réclamation factuelle pour une nuisance répétée, en distinguant faits documentés et interprétations.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Les mesures techniques, les règles locales et les droits inscrits dans un titre sont prévus comme vérifications distinctes ; aucune action matérielle unilatérale n'est suggérée par défaut.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un voisin revendique un droit de passage.
- Une haie ou une clôture fait l'objet d'un désaccord.
- Des nuisances récurrentes sont alléguées sans preuve datée.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Complément des frictions logement — 16 octobre 2026

Points 73, 78–106 ; relais 92, 97, 111 de la [matrice logement](dom-006-annexes/dom-006-frictions-utilisateurs.md).

Découper nuisances (bruit, impact, odeurs et intimidation) ; bornage/limite/empiètement ; propriété et travaux des murs dont soutènement/abandon ; fondement/enclave/tracé d'un passage ; aggravation, réseaux et obstacles ; extinction ; accès temporaire de chantier ; plantations/branches/racines ; eaux naturelles/toiture ; vues et jours. Pour chaque tâche : titres complets et actes constitutifs, plans/PV contradictoires, dates, état des accès, mesures, règles locales, photos et constatations utiles. Sortie : faits/preuves/hypothèses, titre ou mesure à obtenir, question technique au géomètre-expert ou acousticien et brouillon proportionné. Le cadastre ne remplace pas un bornage et l'ancien usage ne suffit pas à établir un passage ; qualifier division, enclave, assiette, destination et droits de réseaux séparément. Examiner exceptions locales, ancienneté et règles applicables aux végétaux ou ouvertures, sans recopier distances du texte. Nuisances du locataire voisin : identifier auteur et bailleur informé ; tâche sur obligation envers tiers à découper avec DOM-006, hors réparation LOG-004. Ne pas proposer coupe, obstacle, déplacement de borne, entrée, suppression d'ouvrage ou représailles. DOM-019 garde permis et recours publics, DOM-018 règlement et décisions collectives ; éventuel volet pénal DOM-002 séparé.

- [ ] Le futur découpage attribue à chaque tâche ses entrées, sortie, sources, limites et scénarios, y compris les voies urgentes distinctes.

Le point 91 exige aussi une tâche sur l'entretien du passage : utilisateurs,
conventions, dégradations alléguées, devis et factures ; sortie comparant usage,
accord et répartition demandée, sans partage automatique des frais.

Scénarios **attendus, non exécutés** : Ancien passage sans titre, facture d'entretien, portail récent et conduites annoncées : examiner fondement, coûts et exercice séparément, sans reconnaître ni supprimer de droit. Arbre et écoulement après terrassement : demander mesures, contexte local et diagnostic d'origine, sans autoriser coupe ou drainage unilatéral.
Les textes, versions, transitions, seuils et échéances seront vérifiés sur
sources officielles lors des implémentations. Ce complément ne termine pas
le cadrage, ne crée aucun plugin et n'exécute aucune démarche externe.
