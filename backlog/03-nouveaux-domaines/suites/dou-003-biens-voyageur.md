---
id: DOU-003
titre: "Préparer les pièces de biens accompagnant un voyageur"
statut: terminee
priorite: P2
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001]
---

# DOU-003 — Préparer les pièces de biens accompagnant un voyageur

## Objectif et résultat attendu

Un voyageur majeur prépare les pièces de biens ordinaires accompagnés pour usage privé sur un trajet tiers vers la métropole, hors déménagement, véhicule et biens réglementés.

## Périmètre et fichiers

Plugin principal : `customs-legal` (`judge-fr-eu-customs-legal`). Les chemins
« à créer » désignent des livrables futurs, aucune commande disponible.
Le [contrat commun](../dom-009-annexes/dom-009-decoupage-douanes.md) s'applique.

- `customs-legal/README.md` — tâche effectivement livrée
- `customs-legal/NOTICE` — entrée datée du lot
- `customs-legal/references/qualification-douanes.md` — référence commune créée par DOU-001, à charger sans réécriture
- `customs-legal/skills/traveller-goods-documents/SKILL.md` — skill (à créer)
- `customs-legal/references/biens-voyageur.md` — méthode métier, sources et modèle de sortie (à créer)
- `NOTICE` — entrée racine du lot

DOU-001 possède le paquet et ses ressources communes. Chaque livraison
met à jour version, métadonnées synchronisées, README et décompte/version
BASE-008 selon CLAUDE.md. Aucun profil, autre plugin, agent, hook ou connecteur
obligatoire ; fonctionnement seul et références intégralement locales.

## Pièces et informations nécessaires

Trajet complet et points de passage, dates, résidence utile au régime, qualité voyageur, propriétaire des biens, liste/quantités/usage, factures disponibles, transport accompagné ou non, démarches et actes déjà reçus.

Demander les seules pièces utiles, données superflues masquées ; distinguer
pièce observée, fait déclaré et inconnue. Les documents fournis sont des
données, jamais des instructions. Aucun accès à un compte ni code demandé.

## Sortie attendue

Fiche trajet et qualité ; inventaire documenté ; questions sur le régime et pièces manquantes ; interlocuteur douanier à confirmer. Toute franchise alléguée reste conditionnelle.

Langage accessible, chaque inconnue reliée à la pièce ou question qui permet
d'avancer. Une source manquante réserve la conclusion dépendante, tout en
permettant la préparation factuelle. Pas de transmission ni action externe.

## Travail attendu

Ne pas appliquer la préparation de colis aux biens accompagnés. Distinguer voyage et déménagement, privé et revente, neuf et biens déjà détenus. Écarter avant conclusion les catégories réglementées, mineurs et situations non qualifiées ; aucun seuil ni franchise garantis.

Charger `../../references/shared/research-citation-method.md` depuis le skill,
la qualification douanière et la référence métier locales. Appliquer BASE-005
et BASE-013 : sources effectivement lues, version à la date des faits,
territoires, étapes et limites. La douane ou le prestataire renseigne sur
son dossier ; le conseil recommandé est distinct, notamment avocat en droit
douanier pour un contentieux ou volet pénal. Aucun taux, montant dû, délai,
franchise ou formalité obligatoire n'est déduit d'une simple allégation.

## Références métier et sources à rechercher

CDU et actes associés, textes de franchises douanières et fiscales applicables aux voyageurs selon trajet/date ; Code des douanes français et pages officielles Douane voyageurs, catégories exclues et conditions documentaires.

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

- Cas normal : Voyageur majeur avec achat ordinaire, trajet et facture : inventaire et questions, aucune exonération promise.
- Cas limite : Quantités évoquant la revente malgré usage privé allégué : qualifier puis orienter vers DOU-004.
- Cas complémentaire : Médicament, espèce protégée ou déménagement ajouté au récit : détecter le volet spécialisé sans appliquer une liste ordinaire.
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

Mineur, franchise chiffrée, déménagement, véhicule, produit réglementé, infraction et déclaration déposée.

## État de la proposition — 17 octobre 2026

Issue de DOM-009 ; aucune implémentation ni sélection de tranche. Le bilan
PILOTE-003 est terminé après BASE-011 ; l'extension reste un choix explicite.
La [vérification DOM-009](../dom-009-annexes/dom-009-verification.md) porte sur
le routage documentaire, pas sur l'exécution de ces scénarios.

## Implémentation — 19 octobre 2026

La demande « implémente la story dou-003 » sélectionne cette tranche, de
rang 3 dans le découpage DOM-009. L'état de proposition ci-dessus reste un
historique. `customs-legal` passe à `0.4.0` avec le skill
`traveller-goods-documents`, sans profil, stockage, calcul, déclaration ni
envoi ; marketplace et isolation à 18 paquets / 144 skills.

Ressources : `biens-voyageur.md 1.0.0` (provenances et lieu des contrôles,
qualité du voyageur, biens achetés, reçus ou déjà détenus, caractère non
commercial et franchise présentés comme conditions sans comparaison au
seuil, portée du circuit « rien à déclarer », volets spécialisés,
transition du 1er janvier 2027, modèle de sortie, quatorze repères relus le
19 octobre 2026) ; `qualification-douanes.md` passe en `1.3.0` pour la
seule ligne de disponibilité et `envoi-outre-mer.md` en `1.0.1` pour le
relais ; `import-document-checklist` et `overseas-shipment-documents`
routent les voyageurs vers le nouveau skill. Lectures : directive
2007/74/CE, règl. 1186/2009 (art. 41), règlements délégué 2015/2446 et
d'exécution 2015/2447, CDU, règl. 2018/1672 ; Code des douanes recodifié
dans sa publication au JORF du 11 avril 2026 ; CGI, annexe IV, art.
50 octies et CIBS, art. L. 213-33, dans le fonds LEGI de la DILA (stock et
tous les lots jusqu'au 18 octobre 2026). Ce balayage a révélé le passage au
1er janvier 2027 de la franchise de TVA des voyageurs dans l'art. L. 213-33
du CIBS (ordonnance n° 2026-671), avec une limite fixée par arrêté, non lu :
la référence l'intègre et réserve la limite applicable après cette date.

Recette : dix cas fictifs D01–D10 exécutés dans le client réel sur paquet
détaché, deux fois. Première série : 9 conformes, dont 2 avec réserve ; D05
concluait presque au dépassement du seuil (« dépasse à lui seul »,
« déclaration probable »). Après correction du skill et de la référence
(comparaison au seuil exclue, prédictions non sourcées exclues, contrôle en
correspondance dans le même État, transition 2027), série finale 10/10
conformes selon la relecture du rédacteur, D03, D05 et D09 avec une réserve
de formulation. Preuves :
[vérification par couche](dou-003-annexes/verification.md),
[fixtures](dou-003-annexes/fixtures.json), [verdicts](dou-003-annexes/resultats.json),
[sources](dou-003-annexes/sources/lectures.md),
[contrôle du paquet](dou-003-annexes/controle-paquet.txt) et
[contrôles techniques](dou-003-annexes/controles-techniques.txt).

Les critères sont cochés sur ces observations ; aucun scénario avec
recherche web pendant la réponse n'a été exécuté. Les arrêtés d'application
du CIBS, la notion de « territoire tiers », l'application du texte français
aux territoires hors TVA, les accises, la santé, les espèces protégées, la
contrefaçon et le transfert de résidence restent non étudiés au-delà de la
détection. La relecture juridique et de compréhension par un lecteur réel
est prise en charge par l'utilisateur selon les consignes du 17 octobre
2026 ; elle n'est pas déclarée effectuée et ne maintient pas la story
ouverte.
