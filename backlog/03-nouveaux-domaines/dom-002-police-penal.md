---
id: DOM-002
titre: "Cadrer un plugin police et procédure pénale"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-002 — Cadrer un plugin police et procédure pénale

## Objectif

Créer des tâches distinctes pour l'identification d'une mesure policière, les droits, les plaintes et les contestations pénales.

Nom de plugin proposé : `criminal-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Statut de la personne, mesure exacte, autorité, dates/heures, âge et urgence ; ne pas confondre contrôle d'identité, audition libre et garde à vue.
- Tâches candidates : lecture d'une convocation, orientation pendant une mesure, préparation factuelle de plainte, lecture d'un avis d'amende.
- Séparer droits immédiats, qualification d'infraction et voies de recours ; éviter tout équivalent automatique de Miranda ou subpoena.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Codes pénal, de procédure pénale, de la sécurité intérieure et de la route selon les faits ; Justice, textes officiels et jurisprudence pertinente.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture et qualification d'une convocation, avant les régimes urgents plus complexes.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (scénarios rédigés, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une convocation sans qualification claire de l'audition.
- Une mesure en cours avec heure de début connue.
- Un avis d'amende déjà payé ou reçu tardivement.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-002-decoupage-penal.md) : nom `criminal-legal` conservé
  (`judge-fr-eu-criminal-legal`) ; installation seule, sans profil, stockage
  des faits pénaux, agent, hook ni connecteur ; garde-fous propres au domaine
  (urgence d'abord, aucun évitement de la justice, statut avant droits,
  aucune qualification présumée, recours à l'avocat) ; qualification commune
  distinguant contrôle, audition libre et garde à vue ; frontières avec
  contentieux, responsabilité, violences intrafamiliales, séjour, douanes,
  administratif, véhicules, exécution, numérique, consommation, banque,
  travail et santé.
- 12 propositions CRIM-001 à CRIM-012 sous `suites/`, en quatre rangs.
  Première tranche : CRIM-001, lecture d'une convocation par la police ou la
  gendarmerie, qui crée le paquet avec ce seul skill. Mesure en cours,
  amendes et plainte au rang 2.
- [Vérification documentaire](dom-002-verification.md) : les trois scénarios
  de la story et dix cas limites, sans durée, délai, montant ni droit conclu.
- Ligne `criminal-legal` de la [matrice BASE-003](../00-fondations/base-003-dossier-architecture.md)
  précisée ; index du backlog mis à jour.
- [Contrôles statiques](dom-002-resultats.json), produits par
  [le contrôleur du lot](dom-002-controles.py), sur le modèle de DOM-001.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 12 propositions `suites/crim-*.md`, ligne de BASE-003 et
`backlog/README.md`. Le lot reste sous `backlog/`, sans entrée NOTICE.
Un lot EXIST-007 en cours d'écriture dans le même arbre est préservé et listé
à part dans le relevé ; l'en-tête de l'index compte les 234 stories présentes
au moment du contrôle.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.

## Décisions du 16 octobre 2026

Voir les [décisions du 16 octobre 2026](../decisions-2026-10-16.md) : cinq propositions ajoutées, CRIM-013 (indemnisation des
victimes), CRIM-014 (exécution des peines), CRIM-015 (interpellation),
CRIM-016 (manifestations) et CRIM-017 (armes). La garde à vue reste CRIM-002.
Le domaine compte désormais 17 propositions.

## Intégration des frictions utilisateur — 16 octobre 2026

- [Matrice des 97 situations](dom-002-frictions-utilisateurs.md), avec [texte fourni archivé](sources/police-penal-frictions-2026-10-16.txt) et besoins des sections non numérotées ; aucun délai, chiffre ou droit du texte n'est validé par son archivage.
- CRIM-001 à CRIM-008, CRIM-010, CRIM-012, CRIM-015 et CRIM-016 complétées : pièces, sorties, frontières et scénarios attendus. CRIM-004 inclut un brouillon factuel au procureur en cas de dépôt bloqué ; CRIM-002 explicite l'audition libre en cours ; CRIM-006 lit aussi une composition pénale.
- Six propositions nouvelles, CRIM-018 à CRIM-023 : contrôle en cours, perquisition, conservation de preuves, signalement d'agent, TAJ, dépistage routier et rétention du permis. Le domaine compte désormais 23 propositions, toutes non implémentées et non sélectionnées.
- DOM-010 reçoit les exigences FPS et recours administratifs relatifs au permis ; son découpage reste à faire. Casier et TAJ, plainte et signalement, contrôle et audition restent distincts.
- Découpage, vérification, contrôleur, relevé et index actualisés. Le relevé contrôle la structure et la traçabilité, sans recherche juridique ni recette métier. Les travaux préexistants sont comparés à l'instantané de début de cette intégration.
