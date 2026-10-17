---
id: DOM-009
titre: "Cadrer un plugin douanes et import-export"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-009 — Cadrer un plugin douanes et import-export

## Objectif

Organiser les tâches douanières autour de la marchandise, du territoire et de l'opération.

Nom de plugin proposé : `customs-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Particulier/professionnel, voyageur/vente/importation commerciale, territoires douanier et fiscal, origine, provenance, valeur et usage.
- Tâches candidates : préparation documentaire, qualification d'une importation, lecture d'un contrôle ou avis, demande de remboursement/remise.
- Séparer classement/origine/valeur, formalités, dette et sanction ; expliciter les inconnues qui empêchent un taux ou un montant fiable.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des douanes français et de l'Union, actes associés, Douane française, TARIC et Access2Markets selon le besoin.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de préparation documentaire d'une opération bornée, sans calcul de droits sans données vérifiées.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un achat expédié depuis un pays tiers.
- Un envoi vers un territoire ultramarin.
- Un avis de contrôle ou de perception déjà notifié.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Complément des frictions véhicules — 16 octobre 2026

Points 45 et 191. Prévoir la qualification documentaire de l'importation d'un véhicule de particulier, en distinguant achat dans l'Union et provenance d'un pays tiers, territoires douanier/fiscal, origine, provenance, résidence, usage et éventuel transfert de résidence. Recueillir factures, documents étrangers et douaniers, trajet, vendeur/mandataire et date ; sortie attendue : pièces manquantes et questions à la douane, sans taux ni droit calculé. Le document douanier ne remplace ni quitus fiscal DOM-011 ni immatriculation DOM-010 ; VEH-019 garde l'engagement contractuel de remise. Cas à découper : achat UE pris à tort pour import tiers ; véhicule tiers sans justificatif de dédouanement ; demande de franchise alléguée. Lire sources officielles et textes selon opération, sans transformer le guide en liste universelle de formalités.

Exigences de la [matrice des 195 points](dom-023-annexes/dom-023-frictions-utilisateurs.md), à découper sans sélection de tranche. Sources et scénarios métier non vérifiés ; [portée de l’intégration](dom-023-annexes/dom-023-frictions-verification.md).

## Bilan d'exécution — 17 octobre 2026

- [Découpage douanes](dom-009-annexes/dom-009-decoupage-douanes.md) : nom
  `customs-legal` conservé, identifiant futur `judge-fr-eu-customs-legal` ;
  qualification marchandise, qualités, opération, usage, territoires douanier
  et fiscal, origine, provenance, valeur, acteurs, dates et acte reçu.
- Douze propositions DOU-001 à DOU-012 sous `suites/`, avec un skill, ses
  entrées, sortie, références à ouvrir et scénarios propres à chaque tâche.
  Classement, origine, valeur, formalités, dette et sanction sont séparés ;
  remboursement et remise ont chacun leur story.
- Première tranche DOU-001 : dossier d'un achat privé ordinaire expédié d'un
  pays tiers vers la métropole, sans calcul ni déclaration. Outre-mer,
  voyageur, professionnel, véhicule et acte notifié sortent de cette tranche.
- DOU-012 reprend les points véhicules 45 et 191 : achat UE, provenance
  tierce et franchise alléguée ; quitus DOM-011, immatriculation DOM-010,
  engagement contractuel VEH-019 et historique VEH-007 restent distincts.
- [Vérification documentaire](dom-009-annexes/dom-009-verification.md) :
  trois dossiers demandés, trois variantes véhicules et cas limites relus
  par le rédacteur ; [relevé des contrôles](dom-009-annexes/dom-009-resultats.json)
  structurels distinct de la validation juridique ou de l'exécution de skill.
- Ligne douanes de la matrice BASE-003, situation S-17 et liens véhicules
  précisés ; famille DOU ajoutée au générateur, index ETAT régénéré.

Fichiers du lot : présente story, découpage, vérification, relevé JSON,
douze propositions `suites/dou-*.md`, ligne douanes BASE-003, situation S-17,
liens de la matrice véhicules et de VEH-019, `backlog/etat.py` et
`backlog/ETAT.md`. Lot limité à `backlog/`, sans entrée NOTICE ni changement
de version de plugin.

**Portée :** cadrage documentaire, aucun plugin créé ni inscrit au
marketplace, aucun skill implémenté ou exécuté, aucune installation ni
démarche externe. Les sources sont des pistes non ouvertes et non une
vérification du droit actuel ; aucun délai, taux ou montant validé.
PILOTE-003 est terminé après BASE-011, sans sélection automatique d'une
tranche ; toutes les suites restent `proposee`.

La relecture humaine est prise en charge par l'utilisateur conformément à
AGENTS.md du 17 octobre 2026. Elle n'est pas déclarée effectuée ; la
compréhension par un lecteur réel n'a pas été observée. La story est close
sur ses livrables et contrôles de cadrage, sans attendre cette relecture.

## Complément des 75 frictions douanes — 17 octobre 2026

- [Source intégrale](sources/douanes-frictions-2026-10-16.txt) conservée à
  l'octet près, avec ses quinze lignes de calendrier, dix réflexes et cinq
  dossiers coutellerie. Sa mention de vérification juridique n'est pas une
  validation par le dépôt.
- [Matrice des besoins](dom-009-annexes/dom-009-frictions-utilisateurs.md) :
  75 points reliés aux douze propositions existantes, aux voisins et à
  26 tâches douanières candidates C01–C26 plus quatre tâches voisines V01–V04,
  toutes à découper. Entrées, résultat et scénario futur par candidat.
- Distinctions renforcées : lecture de frais, rectification/invalidation,
  retour en l'état/SAV/perfectionnement/temporaire/transit, représentation,
  observations/contestation/suite judiciaire/sursis/garanties, retenue PI,
  RTC/RCO, EMEBI et restrictions produit/pays/matière.
- Neuf propositions DOU précisées dans leur périmètre ; DOU-001 reste une
  préparation documentaire sans calcul. Frontières fiscales, contrats,
  poste/fret, assurance, banque, pénal, contentieux, produits, PI et matières
  précisées dans les cadrages concernés.
- [Vérification du complément](dom-009-annexes/dom-009-frictions-verification.md) :
  couverture et cohérence documentaires, distinctes d'une recherche juridique
  ou de l'exécution de skills. Les relevés du cadrage initial sont historiques.

Lot limité à `backlog/` : source, matrice, rapport, présente story et
découpage, neuf suites DOU, IND-027, treize cadrages voisins et index ETAT.
Pas de changement de plugin, version ou NOTICE. DOM-009 reste close sur son
cadrage ; les suites restent proposées et les candidats non implémentés.
Sources, nouveautés 2026, délais et coordonnées du guide restent à vérifier
aux dates des faits ; aucune règle adoptée ni tranche sélectionnée. La
relecture humaine reste prise en charge par l'utilisateur, sans résultat
de compréhension observé.
