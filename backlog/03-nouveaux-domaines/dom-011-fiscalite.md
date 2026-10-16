---
id: DOM-011
titre: "Cadrer un plugin de fiscalité"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-011 — Cadrer un plugin de fiscalité

## Objectif

Distinguer l'assistance déclarative, le contrôle et la réclamation fiscale.

Nom de plugin proposé : `tax-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Impôt, période, contribuable, résidence, déclaration, acte reçu et stade de la procédure.
- Tâches candidates : lecture d'avis, préparation de réclamation, lecture de proposition de rectification, constitution de pièces.
- Séparer assiette, contrôle, recouvrement, pénalités et demande gracieuse ; prévoir les conventions et régimes particuliers sans tout traiter d'emblée.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code général des impôts, Livre des procédures fiscales, textes UE ou conventions pertinents, impots.gouv.fr et BOFiP avec portée à vérifier.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture et de qualification d'un document fiscal précisément identifié.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une erreur alléguée sur un avis d'impôt.
- Une proposition de rectification.
- Une demande de délai de paiement.
- Une demande de justifications reçue d'un service des impôts, sans proposition de rectification.
- Un avis de vérification de comptabilité adressé à un artisan.
- Un avis de paiement majoré du comptable public, suivi d'une saisie administrative.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Compléments du 16 octobre 2026

Ajoutés par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)). Ces tâches candidates
s'ajoutent à celles ci-dessus ; elles restent à hiérarchiser par le cadrage.

- **Contrôle fiscal**, phase par phase : demande de renseignements ou de
  justifications, contrôle sur pièces, avis d'examen de la situation fiscale
  personnelle, avis de vérification de comptabilité ; puis proposition de
  rectification, réponse et recours internes. Garanties du contribuable
  contrôlé à lire dans les textes et documents officiels applicables.
- **Vérification de comptabilité d'une entreprise ou d'un indépendant** :
  la procédure fiscale est ici ; les cotisations sociales de l'indépendant
  restent à DOM-039, la relation avec l'expert-comptable à DOM-041.
- **Comptable public** : avis de paiement, majorations, délais de paiement
  et remise gracieuse. L'acte de saisie administrative est lu par ENF-001
  et ENF-004 ; son bien-fondé fiscal reste ici.
- **Fraude alléguée** : volet pénal → DOM-002, sans qualification présumée.

Sources à prévoir en plus : Livre des procédures fiscales (procédures de
contrôle, garanties, recouvrement), documents officiels remis au contribuable
contrôlé, à identifier dans leur version.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

