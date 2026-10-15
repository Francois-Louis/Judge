---
id: BASE-003
titre: "Fixer l'architecture des plugins par domaine"
statut: terminee
priorite: P0
nature: cadrage
dependances: []
---

# BASE-003 — Fixer l'architecture des plugins par domaine

## Objectif

Traduire le découpage demandé en règles d'organisation applicables story par story.

## Points de départ

- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [CLAUDE.md](../../CLAUDE.md)
- [employment-legal/](../../employment-legal/)
- [commercial-legal/](../../commercial-legal/)
- [litigation-legal/](../../litigation-legal/)
- [legal-clinic/](../../legal-clinic/)

## Travail attendu

- Cartographier les plugins existants et leurs responsabilités, sans les regrouper dans un plugin généraliste France/UE.
- Définir le contrat d'un plugin : manifeste, profil, documentation, skills par tâche et références métier. Agents, hooks et connecteurs ne sont ajoutés que pour un besoin identifié.
- Définir les frontières entre domaines proches : consommation/contrats, banque/assurance, logement/exécution, pénal/contentieux, travail/protection sociale.
- Étendre cette matrice aux domaines du quotidien : logement/travaux/achat/copropriété/urbanisme, famille/successions/protection des majeurs, protection sociale/retraite et travail privé/emploi public. Chaque domaine garde des tâches bornées et des interlocuteurs identifiables.
- Utiliser les [situations du quotidien](../usages-quotidiens.md) pour vérifier la couverture des particuliers, aidants, indépendants et petits exploitants. L'orientation vers les domaines ne doit pas devenir un plugin généraliste qui contient leurs raisonnements.
- Décider comment réutiliser les seules règles transverses de recherche et de citation tout en gardant chaque plugin installable seul ; pas de lien d'exécution cassé vers la racine du dépôt.

## Critères d'acceptation

- [x] Une matrice domaine → plugin → tâches indique existant, adaptation ou création.
- [x] Chaque tâche appartient à un plugin principal ; les interactions sont explicites.
- [x] Les noms des nouveaux plugins et skills sont marqués comme propositions jusqu'à leur cadrage.
- [x] Un exemple d'arborescence respecte le modèle de plugins existant et ne contient aucun plugin juridique fourre-tout.

## Vérification

Prendre trois demandes concrètes : contester un paiement, contester une saisie, revoir un contrat de travail. Vérifier que leur routage est clair sans charger tous les domaines.

## Hors périmètre

Créer les nouveaux plugins ou renommer massivement les plugins et commandes existants.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [dossier d'architecture](base-003-dossier-architecture.md), avec
  inventaire des 12 plugins internes et de leurs 150 skills, séparation du
  plugin éditeur et des cinq cookbooks, et matrice des 38 domaines proposés.
- Chaque tâche a un plugin principal, une sortie et un interlocuteur ; les
  frontières et questions complémentaires sont explicites, notamment pour
  logement/travaux/achat/copropriété/urbanisme, famille/successions/protection
  et travail privé/emploi public/prestations/retraite.
- Contrat minimal et arborescence proposés : manifeste, modèle de profil,
  documentation, skills bornés et références embarquées. Les nouveaux noms
  restent des propositions jusqu'à leur cadrage, sans création de plugins.
- Réutilisation retenue : méthode de recherche/citation versionnée à la racine
  pour l'édition, copie locale dans chaque plugin livré pour l'exécution.
  BASE-005 rédigera cette méthode ; BASE-006 formalisera le contrôle du paquet
  isolé ; BASE-004 décidera l'identité et les chemins des configurations.
- Vérifications : inventaire comparé aux manifestes et répertoires de skills,
  cohérence des noms proposés avec les 38 stories DOM, couverture des renvois
  des situations du quotidien, liens locaux et structure Markdown vérifiés.
  Les trois cas fictifs paiement/saisie/contrat de travail ont un routage
  explicite sans chargement de tous les domaines.
- Limites : relecture d'architecture, sans exécution de skill ni validation
  juridique ou installation isolée. Les écarts d'autonomie hérités restent
  à corriger dans les lots concernés. Aucun changement des plugins existants.

