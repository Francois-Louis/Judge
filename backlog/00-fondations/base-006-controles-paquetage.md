---
id: BASE-006
titre: "Définir les contrôles d'une adaptation de skill"
statut: terminee
priorite: P0
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# BASE-006 — Définir les contrôles d'une adaptation de skill

## Objectif

Savoir vérifier une petite adaptation avant d'en multiplier le nombre.

## Points de départ

- [scripts/](../../scripts/)
- [CLAUDE.md](../../CLAUDE.md)
- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [.github/workflows/cla.yaml](https://github.com/Francois-Louis/Judge/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/.github/workflows/cla.yaml) — supprimé par BASE-007 ; version auditée au commit `4a6c651`
- [scripts/lint-tool-scope.py](../../scripts/lint-tool-scope.py)

## Travail attendu

- Séparer contrôles de structure (manifestes, frontmatter, commandes, références embarquées) et contrôles du comportement juridique.
- Prévoir une installation isolée d'un seul plugin : pas de dépendance implicite au dépôt entier, ni au profil ou aux connecteurs de l'origine.
- Définir une grille de scénarios : cas nominal, information déterminante manquante, source indisponible, situation transfrontalière et héritage américain trompeur.
- Inclure les [situations du quotidien](../usages-quotidiens.md) et un utilisateur sans formation juridique : compréhension des sommes, obligations, interlocuteurs et actions possibles.
- Décider quels contrôles méritent un script et lesquels demandent une relecture ; ne pas créer de tests qui vérifient seulement des mots-clés.

## Critères d'acceptation

- [x] Une checklist de validation est utilisable pour un skill puis pour un plugin.
- [x] La validation du schéma et l'exécution réelle sont distinguées ; un outil absent n'est pas annoncé comme ayant réussi.
- [x] Les dépendances de paquetage sont vérifiées depuis l'artefact installé.
- [x] Les futurs workflows CI prévus restent limités aux besoins du fork, sans publication ni PR automatique vers l'origine.

## Vérification

Préparer une référence volontairement absente d'un paquet et un nom de commande inexistant. Les contrôles retenus doivent les détecter.

## Hors périmètre

Ajouter d'emblée une CI complète, déployer des agents ou exécuter tous les scénarios juridiques du dépôt.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [recette de validation](../../references/package-validation.md),
  version `1.0.0`, avec checklists skill puis plugin, procédure d'installation
  isolée et fiche de preuve. Structure, schéma, installation/exécution réelle,
  relecture juridique et compréhension par l'utilisateur ont des résultats séparés.
- Grille : cas nominal, information déterminante manquante, source indisponible,
  situation transfrontalière et héritage américain trompeur. Fixtures d'usage
  prévues pour le particulier sans formation juridique, l'aidant, l'indépendant
  et le petit exploitant ; sommes, obligations, interlocuteurs et démarches
  sont évalués par relecture et reformulation, sans assertions de mots-clés.
- [Contrôleur de paquet](../../scripts/check-plugin-package.py) : un seul
  artefact en argument, sans recherche dans le checkout ni accès au profil ;
  contrôles bornés JSON/frontmatter, références locales, commandes et copie
  embarquée de BASE-005. Chemins dynamiques et commandes interplugins signalés
  pour relecture. Schéma officiel seulement sur demande et si l'outil est présent.
- [Fixtures de vérification](../../scripts/test-check-plugin-package.py) :
  paquet temporaire hors du dépôt avec la vraie copie intégrale de BASE-005 ;
  référence retirée du paquet alors qu'une copie source existe ailleurs, et
  commande inventée détectées. Vérification complémentaire des chemins hors
  paquet, frontmatter invalide, points d'entrée, profils et statuts d'outil absent.
  Les 11 tests passent. Un lancement réel du contrôleur depuis la racine d'un
  artefact temporaire confirme `STRUCTURE OK` et le code `2` avec `--schema`
  (CLI absente), puis le code `1` avec les deux défauts injectés simultanément.
  Liens locaux et format des documents du lot vérifiés.
- Future CI limitée aux besoins du fork et aux preuves du lot ; aucune CI,
  publication, PR vers l'origine ni modification du workflow CLA ajoutée.
- Limites : preuves structurelles sur artefacts factices, pas d'installation
  réelle dans un client ni d'exécution d'un skill. CLI `claude` absente ici :
  schéma officiel non exécuté. Aucun scénario juridique ni contrôle utilisateur
  présenté comme exécuté. La recette réelle du pilote reste à PILOTE-003 ;
  aucun plugin existant adapté ou certifié par ce cadrage.

