---
id: DOU-013
titre: "Établir le calendrier d'une déclaration d'exportation déposée à l'avance"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001]
---

# DOU-013 — Établir le calendrier d'une déclaration d'exportation déposée à l'avance

## Objectif et résultat attendu

Une personne habilitée à déposer les déclarations d'exportation de son
entreprise demande combien de temps à l'avance elle peut déclarer un envoi
« sans que ce soit gênant ». Le résultat est une fiche chronologique sourcée
d'une seule déclaration d'exportation : dépôt, présentation des marchandises,
acceptation, mainlevée, sortie effective, preuve de sortie, et les seuils qui
font tomber, invalider ou rectifier la déclaration, avec le type de
déclaration adapté à un dépôt anticipé.

## Origine

Question reçue le 19 octobre 2026 d'une collègue de l'utilisateur, qui dépose
des déclarations « EXA » pour une entreprise de coutellerie : « Combien de temps
à l'avance puis-je le faire sans que ce soit gênant ? ». Le parcours K05 et les
points 34, 38 et 39 de la [matrice des frictions](../dom-009-annexes/dom-009-frictions-utilisateurs.md)
posent la même question de chronologie export.

## Périmètre et fichiers

Plugin principal : `customs-legal` (`judge-fr-eu-customs-legal`). Les chemins
« à créer » désignent des livrables futurs, aucune commande disponible.
Le [contrat commun](../dom-009-annexes/dom-009-decoupage-douanes.md) s'applique.

- `customs-legal/README.md` — tâche effectivement livrée
- `customs-legal/NOTICE` — entrée datée du lot
- `customs-legal/references/qualification-douanes.md` — référence commune créée par DOU-001, à charger sans réécriture
- `customs-legal/skills/export-declaration-timeline/SKILL.md` — skill (à créer)
- `customs-legal/references/calendrier-declaration-export.md` — méthode, sources et modèle de sortie (à créer)
- `NOTICE` — entrée racine du lot

Cas pris en charge : une exportation définitive de marchandises de l'Union
depuis la France métropolitaine, déclaration standard déposée par
l'exportateur ou son représentant dans le système export français en
vigueur, mode de transport et bureau de sortie connus ou à demander.

## Pièces et informations nécessaires

Type de déclaration réellement saisi (« EX » et type complémentaire A, D ou
autre), date et heure prévues de dépôt, date à laquelle les marchandises seront
prêtes et présentées ou mises à disposition au bureau d'exportation, lieu de
présentation (bureau, lieu agréé, procédure de domiciliation éventuelle),
mode de transport et bureau de sortie, statut du déclarant (salarié de
l'exportateur, représentant direct ou indirect), autorisations de
simplification éventuelles, état de la déclaration (déposée, acceptée,
mainlevée, sortie) et messages reçus.

Ne demander ni identifiants ni accès au portail douanier. L'habilitation
annoncée par la personne est un fait déclaré, pas une autorisation vérifiée.

## Sortie attendue

Frise datée : dépôt → présentation → acceptation → éventuel contrôle →
mainlevée → présentation au bureau de sortie → confirmation de sortie →
preuve d'exportation pour la TVA. Pour chaque étape : règle lue, délai ou
condition, effet d'un dépassement, action ou question utile. Encadré « dépôt
anticipé » : type de déclaration à utiliser, durée maximale entre dépôt et
présentation, conséquence d'une absence de présentation, modifications
possibles avant acceptation. Encadré « après mainlevée » : sortie non
confirmée, relance, justification alternative de sortie, invalidation,
rectification. Questions au service des douanes ou au conseiller en
dédouanement du bureau concerné.

Langage accessible ; distinguer règle de l'Union, mise en œuvre nationale du
système export et pratique d'un bureau. Pas de dépôt, de message ni de
modification de déclaration réalisés par l'outil.

## Travail attendu

- Lire et citer l'article 171 du code des douanes de l'Union (dépôt avant la
  présentation attendue ; 30 jours) et les articles 172 à 174 (acceptation
  après présentation, rectification, invalidation), en version applicable.
- Rechercher dans les actes délégués et d'exécution (règlements (UE)
  2015/2446 et 2015/2447) les règles d'exportation et de sortie :
  traitement de la déclaration déposée avant présentation, délais de la
  déclaration préalable à la sortie selon le mode de transport, recherche
  de sortie non confirmée, invalidation d'une déclaration d'exportation
  après mainlevée sans sortie (piste : 150 jours), preuves alternatives.
- Rechercher la liste de codes du type de déclaration complémentaire (piste :
  A pour une déclaration standard, D pour la même déclaration déposée selon
  l'article 171) et la notice française du système export (Delta IE ou
  successeur) qui en fixe l'usage et la confirmation ultérieure.
- Distinguer « gênant » au sens juridique (déclaration réputée non déposée,
  rejet, invalidation, données inexactes à rectifier, contrôle sur une
  marchandise absente) et au sens pratique du bureau ; ne pas transformer une
  pratique locale en règle.
- Relier la preuve de sortie à l'exonération de TVA à l'exportation sans
  absorber la question fiscale (V04).

Charger `../../references/shared/research-citation-method.md` depuis le skill,
la qualification douanière et la référence métier locales. Appliquer BASE-005
et BASE-013.

## Références métier et sources à rechercher

Règlement (UE) n° 952/2013 (CDU), art. 171 à 174, 263, 267 et 269 ; règlement
délégué (UE) 2015/2446 et règlement d'exécution (UE) 2015/2447, dispositions
export/sortie et annexe B (type de déclaration complémentaire) ; Code des
douanes français et BOD/notices de la DGDDI sur le système export ; guide
utilisateur export de la douane française. Les guides d'autres États membres
(Irlande, Suède) et les portails privés sont des pistes de vocabulaire, jamais
la règle française.

Lu le 19 octobre 2026 lors du découpage, sans valider l'implémentation :
article 171 du CDU, reproduction française actuelle via
`scripts/legal_sources.py eu 32013R0952` (« Si les marchandises ne sont pas
présentées dans les 30 jours suivant le dépôt de la déclaration en douane, la
déclaration en douane est réputée ne pas avoir été déposée »). Les règlements
2015/2446 et 2015/2447 n'ont pas pu être lus par cette voie (défi EUR-Lex,
CELLAR en erreur de transport) ; leur contenu reste une piste.

## Critères d'acceptation

- [ ] Sur une déclaration déposée avant que les couteaux soient prêts, la sortie donne le type de déclaration adapté, la durée maximale avant présentation et l'effet d'un dépassement, chacun relié à la source lue.
- [ ] La différence entre déclaration standard présentée et déclaration déposée avant présentation est expliquée sans présumer le code réellement saisi.
- [ ] Le cas d'une sortie non confirmée après mainlevée produit la chronologie de relance, preuves alternatives et invalidation possible, sans délai repris d'un guide non vérifié.
- [ ] Règle de l'Union, mise en œuvre nationale et pratique du bureau sont séparées ; aucune pratique locale présentée comme obligation.
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 consignée par couche, invocation et sorties observées conservées.
- [ ] La sortie se termine par la phrase BASE-013 avec professionnel adapté (service des douanes, conseiller en dédouanement, représentant en douane) ; renfort en tête si une déclaration est déjà réputée non déposée ou invalidée.
- [ ] Aucune déclaration n'est déposée, modifiée ou confirmée par l'outil ; versions, métadonnées et NOTICE sont cohérents.

## Vérification

- Cas normal : déclaration prévue douze jours avant que les marchandises soient prêtes : type de dépôt anticipé, délai, étapes et questions.
- Cas limite : marchandises prêtes 35 jours après le dépôt : déclaration réputée non déposée à expliquer, nouvelle déclaration à envisager.
- Cas complémentaire : déclaration de type A déposée alors que les colis ne sont pas au lieu de présentation et sélectionnée pour contrôle : risque et question au bureau, sans conclusion sur une sanction.
- Sortie non confirmée : mainlevée il y a quatre mois, aucun message de sortie : relance, preuves alternatives, invalidation à rechercher.
- Information manquante : type de déclaration inconnu ; poser la question, conserver la chronologie générale.
- Sans source : refuser l'accès au règlement délégué ; produire la frise avec l'article 171 seul et réserver les étapes dépendantes.
- Héritage américain : joindre une procédure EEI/AES américaine ; aucun délai ni formulaire américain importé.

Scénarios **attendus, non exécutés**. À l'implémentation, appliquer BASE-006 et
conserver fixtures, sources lues, sorties, erreurs et réserves. La relecture
humaine est prise en charge par l'utilisateur selon CLAUDE.md ; ne pas la
déclarer effectuée ni une compréhension vérifiée sans résultat observé.

## Hors périmètre

Déclaration simplifiée et inscription dans les écritures du déclarant au fond,
transit, réexportation, exportation temporaire, preuve fiscale certifiée (V04),
restrictions produit et destination (DOU-014, DOU-015), formalités du pays
destinataire, statut ou responsabilité du représentant (C11).
