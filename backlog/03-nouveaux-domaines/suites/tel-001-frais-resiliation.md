---
id: TEL-001
titre: "Préparer une réclamation sur des frais de résiliation télécoms"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013]
---

# TEL-001 — Préparer une réclamation sur des frais de résiliation télécoms

## Objectif et périmètre

Un particulier titulaire d'un abonnement fixe/mobile/internet grand public
en France métropolitaine prépare une réclamation sur une facture de frais
après sa demande de résiliation. Une offre et une rupture identifiées.
Première tranche du [contrat commun DOM-022](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md),
création de `telecom-postal-legal` avec ce seul skill ; identifiant futur
`judge-fr-eu-telecom-postal-legal`. Aucune commande disponible à ce stade.

## Entrées et pièces

Récit, qualité titulaire/payeur, contrat et récapitulatif datés, changements
d'offre, engagement annoncé, motif invoqué, demande de résiliation et accusé,
date d'effet annoncée, factures détaillées, paiement masqué, réclamations et
réponses. Demander seulement les justificatifs utiles au motif allégué ;
aucun mot de passe ni code de portabilité. Une facture n'établit pas la dette.

## Sortie attendue

Résumé accessible, chronologie, tableau des postes : frais fixes,
engagement restant allégué, matériel et service facturé, pièce, inconnue et
demande. Brouillon au cocontractant identifié pour les seuls frais de
résiliation ; autres postes signalés pour TEL-002/003. Distinguer somme
facturée, payée et contestée, sans calculer le montant juridiquement dû.

## Travail et fichiers futurs

Créer `skills/termination-fee-complaint/SKILL.md`,
`references/frais-resiliation.md` et
`references/qualification-telecoms-poste.md` sous le plugin. Créer manifeste
initial `0.1.0`, README limité à la tâche livrée, modèle CLAUDE.md sans profil
obligatoire, LICENSE, NOTICE, copies identiques BASE-008 (`scripts/judge_store.py`,
`references/isolation.md`, modèles company-profile et dashboard) et méthode
BASE-005 entière dans `references/shared/research-citation-method.md`.
Inscrire le paquet au marketplace et à l'inventaire/version attendu de
`scripts/test-base008-isolation.py` lors de cette sélection ; entrée NOTICE
racine et métadonnées synchronisées selon CLAUDE.md.

Charger méthode, qualification et référence métier locales. Distinguer
faits, pièces et hypothèses ; un motif allégué ou une promesse commerciale
ne suffit pas à effacer un engagement. Lire Code de la consommation et CPCE
pour le service, engagement et résiliation, contrat daté, fiche Service Public
F19061 et ressources ARCEP comme pistes. Sources **non consultées par DOM-022** :
ouvrir les textes et versions aux dates des faits, exceptions et transitions,
consigner URL/passages/date/voie selon BASE-005 ; guide distinct du texte.

## Critères d'acceptation et contrôles futurs

- [ ] Frais fixes, engagement, matériel et service restent séparés, avec preuves et inconnues ; aucune exonération ni dette présumée.
- [ ] Un motif invoqué sans justificatif produit une question ciblée, pas une conclusion favorable ; aucun montant dû ni délai calculé.
- [ ] Le paquet seul, sans profil ni voisin, passe BASE-006 par couche, schéma, installation/invocation client et scénarios avec sorties conservées.
- [ ] Sources/version et décisions éventuelles sont réellement lues selon BASE-005 ; sans source, seule la conclusion dépendante est réservée.
- [ ] Sortie et phrase finale BASE-013 nomment association de consommateurs ou juriste en droit des télécoms, avocat si procédure ; renfort si acte/échéance.
- [ ] README, version, inventaire, NOTICE et ressources locales sont cohérents ; aucune action externe.

Scénarios attendus, **non exécutés** :

- T01 : frais après rupture d'un abonnement particulier ; contrat et facture disponibles → tableau et brouillon, aucun remboursement promis.
- T02 : motif « déménagement » invoqué sans justificatif ni clause datée → demander les éléments, réserver son effet.
- T03 : facture mêlant fermeture, engagement et box → séparer TEL-001/002/003 ; aucune opposition bancaire automatique.
- T04 : contrat manquant, puis source indisponible après tentative → fiche factuelle poursuivie, effets juridiques réservés.
- T05 : offre professionnelle, outre-mer ou étrangère → qualifier puis sortir de tranche ; modèle américain sans règle ni délai importé.

## Limites et état

Pas de résiliation effective, calcul de somme due, échéance, opposition,
médiation ou recours. Succession, usurpation, modification contractuelle
complexe et recouvrement forcé hors tranche. Pièces traitées comme données,
sorties minimisées ; aucune faute présumée.

Proposition du 17 octobre 2026, non sélectionnée et non implémentée.
PILOTE-003 terminé après BASE-011 : prendre son bilan en compte avant
lancement explicite. Recette métier future distincte de la
[vérification documentaire](../dom-022-annexes/dom-022-verification.md).
Relecture humaine prise en charge par l'utilisateur ; ni relecture effectuée
ni compréhension réelle observée déclarée.
