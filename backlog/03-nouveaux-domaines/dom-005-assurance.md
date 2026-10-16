---
id: DOM-005
titre: "Cadrer un plugin d'assurance"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-005 — Cadrer un plugin d'assurance

## Objectif

Structurer la revue de couverture, les sinistres et les refus de garantie dans un plugin dédié.

Nom de plugin proposé : `insurance-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualités des parties, organisme, contrat, conditions générales/particulières, dates et type de risque.
- Tâches candidates : revue de garantie, préparation de déclaration, analyse de refus, contestation de chiffrage, résiliation et protection juridique.
- Ne pas confondre absence de garantie, exclusion, déchéance et nullité ; isoler les régimes auto, construction, santé et emprunteur.
- Séparer le litige de garantie de la responsabilité de l'intervenant : travaux en DOM-015, garage en DOM-023, soins en DOM-007 et dommage civil en DOM-035. Un dossier peut avoir plusieurs volets sans dupliquer la même analyse.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des assurances ou régimes de mutualité/prévoyance selon le contrat, textes spéciaux, ABE Infoservice et ACPR.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill d'analyse d'un refus de garantie à partir du contrat et du courrier de refus.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (scénarios rédigés, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un refus fondé sur une exclusion citée dans un courrier.
- Un sinistre avec conditions particulières manquantes.
- Un désaccord sur le montant d'une expertise.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-005-decoupage-assurance.md) : nom `insurance-legal`
  conservé (`judge-fr-eu-insurance-legal`) ; installation seule, sans profil,
  agent, hook, connecteur ni accès à un espace client ; garde-fous (quatre
  motifs de refus distingués, contrat applicable d'abord, garantie séparée de
  la responsabilité, aucun chiffrage refait, aucune déclaration inexacte) ;
  qualification commune (parties, organisme et régime, contrat, risque,
  dates, motif) ; frontières avec travaux, véhicules, santé, protection
  sociale, responsabilité, banque, consommation, voyages, successions,
  funéraire, copropriété, travail et pénal.
- 11 propositions INS-001 à INS-011 sous `suites/`, en quatre rangs.
  Première tranche : INS-001, analyse d'un refus de garantie à partir du
  contrat et du courrier, qui crée le paquet avec ce seul skill. Déclaration,
  expertise, lecture de garantie et médiation au rang 2 ; régimes emprunteur,
  santé, construction et vie isolés dans leurs propres stories.
- [Vérification documentaire](dom-005-verification.md) : les trois scénarios
  de la story et dix cas limites, sans délai, montant ni droit conclu.
- Ligne `insurance-legal` de la [matrice BASE-003](../00-fondations/base-003-dossier-architecture.md)
  précisée ; index du backlog mis à jour.
- [Contrôles statiques](dom-005-resultats.json), produits par
  [le contrôleur du lot](dom-005-controles.py), sur le modèle de DOM-001.

Point ouvert : l'offre d'indemnisation d'une victime d'accident de la
circulation n'est pas découpée ; son rattachement entre DOM-005 et DOM-035
reste à décider.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 11 propositions `suites/ins-*.md`, ligne de BASE-003 et
`backlog/README.md`. Le lot reste sous `backlog/`, sans entrée NOTICE.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.

## Décisions du 16 octobre 2026

Point ouvert levé ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : l'offre d'indemnisation d'une victime d'accident
de la circulation est rattachée à DOM-035.
