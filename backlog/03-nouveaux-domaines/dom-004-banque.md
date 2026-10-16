---
id: DOM-004
titre: "Cadrer un plugin bancaire"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-004 — Cadrer un plugin bancaire

## Objectif

Organiser les tâches bancaires indépendamment de l'assurance et de la consommation générale.

Nom de plugin proposé : `banking-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Statut du client, prestataire, pays, contrat, opération et dates ; distinguer compte, paiement, crédit et investissement.
- Tâches candidates : contestation de paiement, réclamation bancaire, lecture d'une offre de crédit, frais/clôture de compte et incidents.
- Séparer paiement non autorisé, virement effectué sous tromperie et litige commercial ; prévoir les frontières avec surendettement et AMF.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code monétaire et financier, Code de la consommation selon le produit, textes UE applicables, Banque de France, ABE Infoservice, ACPR et AMF selon le sujet.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de qualification d'une contestation de paiement et de préparation de la réclamation.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (scénarios rédigés, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un paiement par carte contesté.
- Un virement validé après une usurpation d'identité.
- Une réclamation sur des frais de compte professionnel.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-004-decoupage-banque.md) : nom `banking-legal` conservé
  (`judge-fr-eu-banking-legal`) et nom de skill `payment-dispute` confirmé ;
  installation seule, sans profil, agent, hook, connecteur ni accès à un
  compte ; garde-fous (urgence d'abord, jamais de code ni d'identifiant
  complet, trois qualifications séparées, aucune conclusion sur la
  négligence, aucun conseil d'investissement) ; qualification commune
  distinguant compte, paiement, crédit et placement ; frontières avec
  consommation, assurance, surendettement, exécution, pénal, données,
  numérique, sociétés, immobilier et successions.
- 11 propositions BNK-001 à BNK-011 sous `suites/`, en quatre rangs.
  Première tranche : BNK-001, qualification d'un paiement contesté et
  réclamation, qui crée le paquet avec ce seul skill. Tromperie, frais et
  médiation au rang 2.
- [Vérification documentaire](dom-004-verification.md) : les trois scénarios
  de la story et dix cas limites, sans délai, montant ni droit conclu.
- Matrice [BASE-003](../00-fondations/base-003-dossier-architecture.md) :
  ligne `banking-legal`, confirmation de `payment-dispute` et règle sur
  l'investissement précisées ; index du backlog mis à jour.
- [Contrôles statiques](dom-004-resultats.json), produits par
  [le contrôleur du lot](dom-004-controles.py), sur le modèle de DOM-001.

Points ouverts : placements et actifs numériques sans domaine propriétaire
(orientation seule par BNK-011, cadrage dédié à décider) ; caution d'un prêt
non découpée.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 11 propositions `suites/bnk-*.md`, matrice BASE-003 et
`backlog/README.md`. Le lot reste sous `backlog/`, sans entrée NOTICE.
Un lot EXIST-009 écrit pendant la tâche dans le même arbre est préservé et
listé à part dans le relevé ; l'en-tête de l'index compte les 324 stories
présentes au moment du contrôle, dont EXIST-008 et EXIST-009 terminées.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles et actes cités sont des pistes. Aucun plugin créé, skill exécuté,
paquet installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est
satisfait après BASE-011 ; aucune tranche n'est sélectionnée.

## Décisions du 16 octobre 2026

Points ouverts levés ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : placements et actifs numériques en orientation
seule (BNK-011), sans nouveau domaine ; caution d'un prêt découpée dans
BNK-012. Le domaine compte alors 12 propositions.

## Intégration des frictions utilisateur — 16 octobre 2026

La [matrice des 99 points](dom-004-frictions-utilisateurs.md) rattache chaque
friction à sa tâche et à un résultat attendu. BNK-001 à BNK-012 sont précisées ;
sept propositions BNK-013 à BNK-019 complètent mobilité, blocage, erreur de
virement, carte indisponible, comptes inactifs et services professionnels.
Le domaine compte désormais 19 propositions, toutes `proposee`.

Rachat d'assurance-vie : INS-012 ; assurance emprunteur et capital décès :
INS-008/INS-011 ; saisie : ENF-004 ; frais et comptes successoraux : DOM-016 ;
situation d'endettement globale : DOM-024. Les tâches de ces cadrages restent
à découper. Placements et PEA restent en orientation seule, selon la décision
antérieure. Les montants, délais et événements juridiques du texte fourni ne
sont pas validés par cette intégration. Aucune première tranche n'est lancée.

## Complément des frictions données personnelles — 16 octobre 2026

Points 41–43 et 52 de la [matrice données personnelles](../02-plugins-existants/exist-003-frictions-utilisateurs.md) : PRV-031 porte la demande relative à une décision présentée comme automatisée ; contestation du refus de crédit au particulier encore à découper ici. BNK-005 lit une offre, BNK-006 un prélèvement, BNK-018 un refus professionnel : aucun ne couvre ce refus au particulier. BNK-010 garde le fichier Banque de France ; PRV-022 la rectification hors procédure spéciale. Fraude après fuite → BNK-001 et PRV-032, plainte pénale → CRIM-004. Scénario attendu : score opaque et incident contesté, avec objets, destinataires et calendriers séparés, sans crédit promis. Portée et contrôles : voir la matrice.
