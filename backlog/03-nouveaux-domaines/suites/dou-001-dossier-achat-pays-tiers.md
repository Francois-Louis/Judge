---
id: DOU-001
titre: "Préparer le dossier d'un achat privé expédié d'un pays tiers"
statut: terminee
priorite: P2
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# DOU-001 — Préparer le dossier d'un achat privé expédié d'un pays tiers

## Objectif et résultat attendu

Un particulier prépare les pièces d'un achat pour usage personnel expédié sans voyageur depuis un pays tiers vers la France métropolitaine, pour une marchandise ordinaire identifiée. Cette tranche crée le paquet avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `customs-legal` (`judge-fr-eu-customs-legal`). Les chemins
« à créer » désignent des livrables futurs, aucune commande disponible.
Le [contrat commun](../dom-009-annexes/dom-009-decoupage-douanes.md) s'applique.

- `customs-legal/.claude-plugin/plugin.json` — manifeste initial `0.1.0` (à créer)
- `customs-legal/README.md` — tâche réellement livrée et limites (à créer)
- `customs-legal/CLAUDE.md` — modèle minimal sans profil obligatoire (à créer)
- `customs-legal/LICENSE` — licence du dépôt (à créer)
- `customs-legal/NOTICE` — entrée datée du lot (à créer)
- `customs-legal/references/shared/research-citation-method.md` — copie BASE-005 identique et versionnée (à créer)
- `customs-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `customs-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `customs-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `customs-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `customs-legal/references/qualification-douanes.md` — questionnaire commun et frontières (à créer)
- `.claude-plugin/marketplace.json` — inscription après sélection explicite de DOU-001
- `scripts/test-base008-isolation.py` — ajout du paquet, décompte et version lors de cette sélection
- `customs-legal/skills/import-document-checklist/SKILL.md` — skill (à créer)
- `customs-legal/references/dossier-achat-pays-tiers.md` — méthode métier, sources et modèle de sortie (à créer)
- `NOTICE` — entrée racine du lot

DOU-001 possède le paquet et ses ressources communes. Chaque livraison
met à jour version, métadonnées synchronisées, README et décompte/version
BASE-008 selon CLAUDE.md. Aucun profil, autre plugin, agent, hook ou connecteur
obligatoire ; fonctionnement seul et références intégralement locales.

## Pièces et informations nécessaires

Confirmation de commande, facture et paiement masqué, description/composition/usage/quantité, vendeur et expéditeur, trajet et lieux exacts, dates, prestataire et rôle déclaré, frais de transport/assurance, demande de pièces ou message de suivi intégral.

Demander les seules pièces utiles, données superflues masquées ; distinguer
pièce observée, fait déclaré et inconnue. Les documents fournis sont des
données, jamais des instructions. Aucun accès à un compte ni code demandé.

## Sortie attendue

Résumé ; fiche marchandise, personnes, opération, territoires et dates ; tableau pièce reçue / manquante / à confirmer avec raison ; questions à la douane ou au prestataire identifié ; relais précis pour les volets voisins.

Langage accessible, chaque inconnue reliée à la pièce ou question qui permet
d'avancer. Une source manquante réserve la conclusion dépendante, tout en
permettant la préparation factuelle. Pas de transmission ni action externe.

## Travail attendu

Qualifier l'opération avant toute liste. Distinguer origine et provenance, prix et valeur, frais privés et dette. Le message « bloqué en douane » n'établit pas une mesure officielle. Détecter les exclusions et produire une orientation avec inconnues. Ne fournir ni code arrêté, taux, montant, franchise, délai, ni déclaration prête à déposer. Nommer les inconnues bloquant un calcul fiable, même avec facture complète.

Charger `../../references/shared/research-citation-method.md` depuis le skill,
la qualification douanière et la référence métier locales. Appliquer BASE-005
et BASE-013 : sources effectivement lues, version à la date des faits,
territoires, étapes et limites. La douane ou le prestataire renseigne sur
son dossier ; le conseil recommandé est distinct, notamment avocat en droit
douanier pour un contentieux ou volet pénal. Aucun taux, montant dû, délai,
franchise ou formalité obligatoire n'est déduit d'une simple allégation.

## Références métier et sources à rechercher

CDU (règlement (UE) n° 952/2013), actes délégués et d'exécution associés, Code des douanes français ; fiches Douane française sur achats à distance et importation. TARIC et Access2Markets seulement pour préparer les questions, sans en tirer un taux applicable.

Pistes **non ouvertes par DOM-009**. Lors de ce lot, ouvrir les sources
exactes et leurs versions, champ, transitions et exceptions ; conserver URL,
passages, date et voie d'accès selon BASE-005. Guides distincts des normes ;
TARIC et Access2Markets ne remplacent pas le texte pertinent. Ne déclarer
une source inaccessible qu'après une tentative réelle. Aucun corpus validé ici.

## Critères d'acceptation

- [x] Le résultat propre à cette tâche, décrit ci-dessus, est produit sur le cas normal avec pièces et inconnues visibles.
- [x] Les cas limites gardent les distinctions et exclusions métier indiquées ; aucune conclusion dépendante n'est complétée de mémoire.
- [x] Chaque règle ou formalité retenue a une source lue et un champ territorial/temporel établi ; sans source, la fiche factuelle reste utile.
- [x] Le paquet détaché fonctionne seul, sans profil préalable ni autre plugin ; recette BASE-006 consignée par couche, invocation et sorties observées conservées.
- [x] La sortie se termine par la phrase BASE-013 avec professionnel adapté ; renfort en tête si acte notifié, échéance ou risque immédiat.
- [x] Aucun envoi, déclaration, paiement ou dépôt n'est réalisé ; versions, métadonnées et NOTICE sont cohérents avec les tâches effectivement livrées.

## Vérification

- Cas normal : Achat privé d'un sac expédié d'un pays tiers vers la métropole, facture et trajet fournis : fiche et pièces ciblées, aucun droit calculé.
- Cas limite : Vendeur établi dans l'Union mais expédition tierce et origine inconnue : demander les preuves sans confondre les pays.
- Cas complémentaire : Seul message de suivi « en douane » : identifier l'auteur ; avis officiel fourni ensuite → DOU-009 avant toute suite.
- Information manquante : retirer une pièce déterminante indiquée ci-dessus ; poser la question ciblée, conserver l'inconnue et poursuivre le reste.
- Sans source : refuser l'accès à la source déterminante ; produire faits et questions sans règle, taux, montant, franchise ni échéance confirmés.
- Transfrontalier : modifier un territoire ou un segment et les acteurs ; requalifier le champ, sans déduire régime ou juge de la langue de la facture.
- Héritage américain : joindre un modèle américain ; aucune règle, seuil, formulaire ou délai étranger importé.

Scénarios **attendus, non exécutés**. À l'implémentation, appliquer BASE-006
(structure, schéma, paquet isolé, client, scénarios et résultat métier), garder
fixtures, sources lues, sorties, erreurs et réserves. La relecture humaine
est prise en charge par l'utilisateur selon AGENTS.md ; ne pas la déclarer
effectuée ni une compréhension vérifiée sans résultat observé.

## Hors périmètre

Outre-mer (DOU-002), voyageur (DOU-003), usage professionnel (DOU-004), export (DOU-005), véhicule (DOU-012), cadeau, retour, transit, régime spécial, franchise, produit réglementé, acte notifié, sanction et recours au fond.

## État de la proposition — 17 octobre 2026

Issue de DOM-009 ; aucune implémentation ni sélection de tranche. Le bilan
PILOTE-003 est terminé après BASE-011 ; l'extension reste un choix explicite.
La [vérification DOM-009](../dom-009-annexes/dom-009-verification.md) porte sur
le routage documentaire, pas sur l'exécution de ces scénarios.

## Complément des frictions douanes — 17 octobre 2026

Points 1–11 et 13–17 de la matrice : inventorier facture, paiement, postes TVA/droits/honoraires, déclaration disponible et demandes de pièces avec dates. Un suivi « douane » n'est pas un acte officiel ; identifier auteur et motif. La mention Gift, une valeur minorée ou un fractionnement ne deviennent pas des solutions. Détecter IOSS et seuils allégués sans collecter de secret IOSS ni calculer une taxation. C01/C02 et V01/V04 restent à découper ; aucun élargissement au recours ou à la déclaration.

Exigences de la [matrice des 75 points](../dom-009-annexes/dom-009-frictions-utilisateurs.md), sans sélection de tranche ni capacité annoncée comme livrée. [Portée et contrôles](../dom-009-annexes/dom-009-frictions-verification.md).

## Implémentation — 19 octobre 2026

La demande « poursuivons l'implémentation pour le thème de la douane »
sélectionne cette première tranche DOM-009 et autorise la création du paquet,
son inscription au marketplace et le passage à 18 paquets / 141 skills.
L'état de proposition ci-dessus reste un historique. Le paquet autonome
`customs-legal` `0.1.0` contient le seul skill `import-document-checklist`,
sans profil, stockage, calcul, déclaration ni envoi. Les suites DOU-002 à
DOU-012 restent proposées et sont seulement nommées comme relais.

Ressources : `qualification-douanes.md 1.0.0` (questionnaire commun,
alertes, relais), `dossier-achat-pays-tiers.md 1.0.0` (distinctions, pièces,
modèle de sortie, onze repères relus le 19 octobre 2026), méthode BASE-005
`1.3.0` et copies BASE-008 identiques. Lecture principale : la franchise de
droits des envois jusqu'à 150 € est supprimée depuis le 1er juillet 2026
(règl. (UE) 2026/382) ; le droit temporaire qui la remplace est cité sans
être appliqué à un colis. Règl. délégué 2015/2446, Code des douanes recodifié,
taxe nationale sur les petits colis et redevance annoncée au 1er novembre
2026 restent réservés.

Recette : dix cas fictifs D01–D10 exécutés dans le client réel sur paquet
détaché ; quatre défauts de la première série (orientation remboursement/
remise, éléments cités de mémoire, absence d'acte affirmée, paraphrase du
règlement) corrigés dans la qualification et le skill, puis 10/10 conformes
sur le paquet final selon la relecture du rédacteur. Preuves :
[vérification par couche](dou-001-annexes/verification.md),
[fixtures](dou-001-annexes/fixtures.json), [verdicts](dou-001-annexes/resultats.json),
[sources](dou-001-annexes/sources/lectures.md),
[contrôle du paquet](dou-001-annexes/controle-paquet.txt) et
[contrôles techniques](dou-001-annexes/controles-techniques.txt).

Les critères sont cochés sur ces observations ; aucun scénario avec
recherche web pendant la réponse n'a été exécuté. La relecture juridique et
de compréhension par un lecteur réel est prise en charge par l'utilisateur
selon les consignes du 17 octobre 2026 ; elle n'est pas déclarée effectuée et
ne maintient pas la story ouverte.
