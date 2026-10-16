---
id: DOM-003
titre: "Cadrer un plugin d'exécution et de recouvrement"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-003 — Cadrer un plugin d'exécution et de recouvrement

## Objectif

Isoler les actes des commissaires de justice, le recouvrement et l'exécution forcée du contentieux général.

Nom de plugin proposé : `enforcement-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualité de l'émetteur, titre de l'acte, mode et date de signification, créance et éventuel titre exécutoire.
- Tâches candidates : lecture d'acte, contrôle de décompte, recouvrement amiable, orientation face à une saisie ou une expulsion.
- Séparer saisies, mesures conservatoires et recouvrement ; articuler logement, dette bancaire et compétence du juge selon le régime vérifié.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des procédures civiles d'exécution, Code de procédure civile, Code civil, textes spéciaux et informations officielles de la profession.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture d'acte et de repérage des informations urgentes, sans promesse de suspension.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (scénarios rédigés, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une relance d'une société de recouvrement.
- Un acte signifié dont la date est contestée.
- Une mesure de saisie avec ventilation des frais absente.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-003-decoupage-execution.md) : nom `enforcement-legal`
  conservé (`judge-fr-eu-enforcement-legal`) ; installation seule, sans
  profil, agent, hook ni connecteur ; garde-fous (urgence d'abord, l'émetteur
  ne qualifie pas l'acte, authenticité, aucune promesse de suspension, fond
  laissé à son domaine) ; qualification commune (émetteur, titre de l'acte,
  titre exécutoire, remise et dates, décompte, situation de la personne) ;
  frontières avec contentieux, logement, banque, surendettement, créances
  publiques et sociales, contrats B2B, secteurs, pénal, successions,
  famille, administratif et travail.
- 11 propositions ENF-001 à ENF-011 sous `suites/`, en quatre rangs.
  Première tranche : ENF-001, lecture d'un acte et repérage de l'urgence, qui
  crée le paquet avec ce seul skill. Recouvrement amiable, décompte et saisie
  sur compte au rang 2.
- [Vérification documentaire](dom-003-verification.md) : les trois scénarios
  de la story et dix cas limites, sans délai, montant ni droit conclu.
- Ligne `enforcement-legal` de la [matrice BASE-003](../00-fondations/base-003-dossier-architecture.md)
  précisée ; index du backlog mis à jour.
- [Contrôles statiques](dom-003-resultats.json), produits par
  [le contrôleur du lot](dom-003-controles.py), sur le modèle de DOM-001.

Points ouverts : l'opposition d'un particulier à une injonction de payer n'a
pas de story propriétaire (rattachement proposé aux suites EXIST-006, à
décider) ; la saisie immobilière n'est pas découpée.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 11 propositions `suites/enf-*.md`, ligne de BASE-003 et
`backlog/README.md`. Le lot reste sous `backlog/`, sans entrée NOTICE.
Un lot EXIST-008 en cours d'écriture dans le même arbre est préservé et listé
à part dans le relevé ; l'en-tête de l'index compte les 265 stories présentes
au moment du contrôle, dont EXIST-007 terminée entre-temps.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.

## Décisions du 16 octobre 2026

Points ouverts levés ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : l'opposition à une injonction de payer est
rattachée à l'exécution (ENF-012) ; la saisie immobilière reçoit une story
d'orientation (ENF-013). Le domaine compte désormais 13 propositions.

## Intégration des frictions utilisateur — 16 octobre 2026

La [matrice des 47 points](dom-003-frictions-utilisateurs.md) conserve le [texte fourni](sources/commissaires-justice-frictions-2026-10-16.txt) comme expression du besoin. Elle complète dix suites et ajoute six propositions ENF-014 à ENF-019 : frais contestés, réclamation professionnelle, lecture de constat, invitation simplifiée de petites créances, devis de constat et dossier de contestation de saisie-attribution. Le domaine compte désormais 19 propositions, toutes non sélectionnées.

DOM-006 reçoit le besoin locatif et DOM-035 le besoin de dossier de responsabilité professionnelle, encore à découper. L'index, le découpage et les contrôles documentaires sont synchronisés. Les recours limités à une orientation restent explicitement signalés dans la matrice.

Fichiers de ce complément : matrice et source, six nouvelles suites, compléments ENF-001 à ENF-008, ENF-011 et ENF-012, DOM-006, DOM-035, présente story, découpage, vérification, contrôleur, relevé et index. Les modifications préexistantes, notamment le complément bancaire ENF-004, sont conservées.

**Portée de ce complément :** intégration documentaire, contrôles de structure et traçabilité ; aucune recherche juridique externe ni validation des affirmations du texte utilisateur, aucun skill ou plugin créé ou exécuté. Les scénarios restent attendus et non exécutés.

## Complément des frictions contentieuses — 16 octobre 2026

Exigences issues des [125 frictions contentieuses](../02-plugins-existants/exist-006-frictions-utilisateurs.md), sans implémentation ni sélection de tranche.

Points 83–95 : conserver ENF-003 pour décompte/paiements, ENF-004 pour compte/sommes protégées, ENF-008 pour délais, ENF-010 pour créancier muni d’un titre et ENF-019/020 pour contestation. Le besoin de vérifier mainlevée après règlement complet doit distinguer solde justifié, demande de levée et confirmation effective ; le paiement n’établit pas à lui seul la levée du blocage. Rechercher régime du titre et créances accessoires sans réutiliser mécaniquement la prescription de fond. Scénarios : justificatif de règlement complet et saisie encore visible ; intérêts ou frais discutés ; titre ancien avec événements d’exécution. CTX-041 porte la lecture d’ordonnance côté créancier avant signification ; ENF-012 garde l’opposition débiteur. Les recours spéciaux JEX restent à découper, sans leur appliquer CTX-036.

Les scénarios indiqués sont attendus, non exécutés. Sources/version, champ, déclencheur, exceptions et transitions restent à rechercher ; le texte fourni n’est pas une autorité juridique.
