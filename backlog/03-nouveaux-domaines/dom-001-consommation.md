---
id: DOM-001
titre: "Cadrer un plugin de droit de la consommation"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-001 — Cadrer un plugin de droit de la consommation

## Objectif

Donner aux litiges de consommation leur propre plugin, distinct des contrats commerciaux B2B.

Nom de plugin proposé : `consumer-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualité des parties, canal de vente, territoire, rôle des plateformes et pièces nécessaires.
- Tâches candidates : revue de CGV B2C, rétractation, garanties, inexécution, réclamation et médiation.
- Frontières avec banque, assurance, voyages et données ; éviter un second plugin qui reproduit toutes leurs procédures.
- Répartir les litiges sectoriels avec [travaux](dom-015-construction-travaux.md), [énergie/eau](dom-021-energie-eau.md), [télécoms/poste](dom-022-telecoms-poste.md), [véhicules](dom-023-vehicules-garages.md), [prestations funéraires](dom-031-deces-obseques.md) et [services numériques](dom-034-numerique-plateformes.md). Les règles générales utiles peuvent être réutilisées, sans créer deux traitements concurrents du même dossier.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code de la consommation, Code civil, textes UE applicables, DGCCRF et CEC France pour l'orientation transfrontalière.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de réclamation pour non-livraison, à borner après cadrage.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (scénarios rédigés, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une commande en ligne jamais livrée.
- Un produit défectueux et une garantie commerciale invoquée.
- Un achat professionnel présenté à tort comme achat de consommateur.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-001-decoupage-consommation.md) : nom `consumer-legal`
  conservé (`judge-fr-eu-consumer-legal`) ; contrat d'installation seule,
  sans profil, agent, hook ni connecteur ; qualification commune (parties,
  objet, canal, territoire, plateformes, pièces) ; frontières avec banque,
  assurance, voyages, données, contrats B2B, produits, contentieux et les six
  secteurs nommés par la story. Un secteur garde son litige, même quand son
  plugin n'est pas disponible.
- 13 propositions CONSO-001 à CONSO-013 sous `suites/`, en quatre rangs.
  Première tranche : CONSO-001, réclamation pour une commande non livrée,
  qui crée le paquet avec ce seul skill. Inclus, exclus et sortie précisés.
- [Vérification documentaire](dom-001-verification.md) : les trois scénarios
  de la story et neuf cas limites, sans délai, montant ni droit conclu.
- Ligne `consumer-legal` de la [matrice BASE-003](../00-fondations/base-003-dossier-architecture.md)
  précisée ; index du backlog mis à jour.
- [Contrôles statiques](dom-001-resultats.json), produits par
  [le contrôleur du lot](dom-001-controles.py) : frontmatter et dépendances,
  sections des propositions, propriétaires uniques des fichiers futurs,
  liens, format, index, absence de paquet `consumer-legal`, périmètre
  comparé à l'instantané de début de tâche.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 13 propositions `suites/conso-*.md`, ligne de BASE-003 et
`backlog/README.md`. Le lot reste sous `backlog/`, sans entrée NOTICE.
Un lot EXIST-006 écrit en parallèle dans le même arbre est préservé et listé
à part dans le relevé ; l'en-tête de l'index est recalé sur les 222 stories
présentes au moment du contrôle.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.

## Décisions du 16 octobre 2026

Voir les [décisions du 16 octobre 2026](../decisions-2026-10-16.md) : achats entre particuliers maintenus (CONSO-011) ; sans plugin
du secteur disponible, consumer traite le litige avec les règles générales et
signale les règles sectorielles manquantes, d'où CONSO-014. La phrase du
bilan « un secteur garde son litige, même quand son plugin n'est pas
disponible » est remplacée par cette règle.

## Intégration des frictions utilisateur — 16 octobre 2026

Le [guide fourni](sources/consommation-frictions-2026-10-16.txt) est archivé
intégralement comme expression du besoin, avec son empreinte contrôlée.
La [matrice des 155 situations](dom-001-frictions-utilisateurs.md) relie chaque
friction à un propriétaire, des preuves et un résultat attendu. Les sections
non numérotées ajoutent checklist, calendrier et distinction des organismes.

Les 14 suites existantes sont complétées par des critères et scénarios ; six
propositions CONSO-015 à CONSO-020 portent vérification du vendeur et de l’offre,
prix et frais, prestation et avance, protection de plateforme, mise en demeure
et remboursement, démarchage et consentement. Le [découpage](dom-001-decoupage-consommation.md)
compte désormais 20 propositions, toujours sans sélection d’implémentation.
CONSO-011 traite aussi la position du vendeur particulier ; CONSO-012 garde
la réponse d’une TPE. Les frontières banque, assurance, pénal, procédure,
données et secteurs restent explicites, avec le repli CONSO-014 déjà décidé.

La [relecture](dom-001-verification.md) éprouve le routage documentaire sur des
cas fictifs. Le [contrôleur](dom-001-controles.py) et son
[relevé](dom-001-resultats.json) vérifient structure, dépendances, couverture,
liens, fichiers futurs et texte archivé. Les travaux préexistants hors lot
sont comparés à l’instantané de début d’intégration, sans réécriture de leurs
fichiers. L’index partagé est ajusté aux nombres réels de stories.

**Portée du complément :** exigences de backlog seulement ; statistiques,
délais, réformes et conflit de sources allégué dans le guide restent à
vérifier selon BASE-005. Aucune recherche juridique, consultation résolue,
création de plugin ou skill, exécution métier, lecteur réel, envoi ou dépôt.
Les contrôles documentaires ne valident ni le droit ni la capacité du produit
à répondre aux situations. DOM-001 reste un cadrage terminé ; ses suites
restent proposées.
