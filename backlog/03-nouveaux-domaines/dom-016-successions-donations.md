---
id: DOM-016
titre: "Cadrer un plugin successions et donations"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-016 — Cadrer un plugin successions et donations

## Objectif

Aider les héritiers et les donateurs à comprendre les pièces, les options et
les étapes d’une transmission patrimoniale. Nom de plugin proposé :
`inheritance-legal`. Aucun plugin n’est créé par cette story de cadrage.

## Tâches métier découpées

Le [découpage détaillé](dom-016-annexes/dom-016-decoupage-successions.md)
définit 25 stories SUC-001 à SUC-025 avec entrées, pièces, sortie, sources,
limites et deux scénarios chacune. Les [parcours en langage courant](dom-016-annexes/dom-016-parcours.md)
permettent de partir du récit ou d’un document :

- Courrier de notaire, actif/passif, demande d’option ou sommation,
  actes pouvant affecter l’option, formalités d’acceptation à concurrence de
  l’actif net, renonciation et descendants, créance et dette découverte : SUC-001 à 008.
- Frais bancaires, comptes oubliés, paiement des obsèques, fonctionnement
  des comptes après décès et preuve de qualité : SUC-009 à 013.
- Effets et documents, testament/donations omis, évaluations, comptes
  d’indivision, occupation, pouvoirs sur un bien, projet et contestation de
  partage : SUC-014 à 021.
- Logement du survivant, contrat de généalogiste, projet de donation et
  qualification d’un élément étranger : SUC-022 à 025.

## Qualification et frontières

Date du décès et preuve, liens familiaux, statut du couple et régime
matrimonial, résidence habituelle, pays et territoire, testament ou donations
connus, biens/dettes, qualité/capacité, pouvoirs et actes déjà signés ou
accomplis. Notification, réception et connaissance d’un fait sont distinguées.
Pour une donation entre vivants, ne pas exiger de décès.

Transmission et indivision successorale ici ; obsèques DOM-031, fiscalité
DOM-011, patrimoine du couple DOM-013, représentation d’un majeur DOM-026,
bail DOM-006 et mission/frais du notaire DOM-041. Le décompte bancaire
successoral reste ici ; paiement contesté et médiation bancaire restent
DOM-004. Assurance-vie et bénéficiaire → INS-011. La table de transmission
du découpage borne les questions, seules pièces utiles et résultats attendus.

## Sources prévues et lectures

Code civil, Code de procédure civile, Code monétaire et financier, textes
fiscaux pour leur articulation, instruments transfrontaliers pertinents et
information officielle DILA, Justice, DGFiP et Caisse des Dépôts.

Le [relevé des lectures](dom-016-annexes/dom-016-sources.md) distingue les
guides effectivement ouverts, des textes français restant à vérifier. Les
points de départ initiaux ont été lus :
[Règlement d’une succession](https://www.service-public.gouv.fr/particuliers/vosdroits/N171?lang=fr)
et [Indivision entre héritiers](https://www.service-public.gouv.fr/particuliers/vosdroits/F1296).
Ils orientent le cadrage ; textes, versions et transitions seront vérifiés
dans chaque implémentation. Aucun montant, délai ou majorité n’est établi ici.

## Première tranche proposée

[SUC-001](suites/suc-001-courrier-notaire.md) : décrypter un courrier de
règlement de succession et produire une fiche de pièces, points à éclaircir
et décisions à ne pas confondre. Aucun acte ou option préparés pour signature.

## Critères d’acceptation

- [x] Les tâches sont découpées en stories d’implémentation avec entrées, sortie, pièces, limites et scénarios : 25 propositions SUC, toutes `proposee`.
- [x] Un utilisateur peut partir de son problème sans connaître le code ou la qualification : 25 demandes courantes et parcours documentaires C01 à C50. *Vérification des contrats écrits par l’agent ; compréhension d’un participant réel non testée.*
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; contrat du futur paquet et frontières documentés. *Aucun paquet créé ni installation testée dans ce cadrage.*
- [x] Option, partage et déclaration fiscale sont distincts ; SUC-002/003/020 et frontière DOM-011 interdisent un partage définitif sur dossier incomplet.
- [x] Aucun tort de l’autre partie ni issue favorable présumés ; demandes documentaires et inconnues séparées des droits à établir.
- [x] Le préalable PILOTE-003 est lu : `terminee` après BASE-011. Aucune adaptation complète ni sélection automatique d’une SUC lancées.

## Compléments intégrés

La [table de couverture](dom-016-annexes/dom-016-decoupage-successions.md#couverture-des-compléments-reçus)
reprend les points 86–88 de la matrice DOM-004 et 33, 55–89, 99, 117,
120–122, 137 de la matrice DOM-031, sans modifier leurs relevés historiques.

- [x] Frais bancaires successoraux SUC-009, honoraires DOM-041 et fiscalité DOM-011 séparés ; assiette, tarif, produits et dates demandés.
- [x] Décompte global ou gratuité revendiquée : pièces et régime à vérifier, sans plafond ni gratuité affirmés sans texte lu. La décision constitutionnelle de juin 2026 alléguée reste non identifiée et non validée ; SUC-009 porte sa recherche exacte et ses effets temporels.
- [x] Recherche banque/FICOBA/Ciclade SUC-010, qualité et assurance-vie INS-011 distinctes, sans accès aux fonds promis.
- [x] Option/sommation SUC-003, actes SUC-004, acceptation protégée/inventaire SUC-005, renonciation/descendants SUC-006, créance SUC-007 et dette découverte SUC-008 découpées séparément.
- [x] Paiement des obsèques SUC-011, carte/procuration/compte joint SUC-012, petite succession SUC-013 et recherches/coffres SUC-010 prévus ; fonctionnement et propriété des fonds distingués avec SUC-002.
- [x] Inventaire/remise SUC-014, libéralités omises SUC-015, évaluations SUC-016, comptes SUC-017, occupation SUC-018, pouvoirs de vente SUC-019 et partage SUC-020/021 séparés ; aucun recel ou partage calculé.
- [x] Logement et volonté du survivant SUC-022 distincts du bail DOM-006 et du couple DOM-013 ; fiscalité et réclamation notariale chez leurs propriétaires.
- [x] Contrat de révélation du généalogiste SUC-023 : mission, mandat allégué, information et honoraires sans dette ou authenticité admises ; consentement général DOM-001 et infraction alléguée DOM-002.

## Scénarios de contrôle

Héritier invité à signer un document incompris (C01/C02), passif mal identifié
(C03/C04), désaccord d’occupation ou vente (C35 à C38). Compléments : sommation
et fiscalité (C05), vente d’objet avant connaissance du passif (C07), inventaire
manquant après déclaration (C09), compte joint (C23), généalogiste inconnu
(C45/C46), conjoint pressé de partir (C43), frais sans assiette/réforme alléguée
(C17/C18) et compte ancien sans transfert (C19).

La [vérification](dom-016-annexes/dom-016-verification.md) contrôle l’orientation,
les pièces et les résultats attendus dans les contrats écrits ; aucun de ces
dossiers n’est résolu pendant le cadrage.

## Hors périmètre

Créer un plugin vide, adapter toute la matière, choisir une option, calculer
un partage définitif, produire un acte à signer ou exécuter une démarche externe.

## Bilan d’exécution — 17 octobre 2026

25 suites proposées, contrat autonome, frontières, couverture des frictions,
lectures officielles et vérification documentaire livrés en annexes. SUC-001
reste la première tranche proposée. Famille SUC ajoutée au générateur et
index ETAT régénéré. Les [résultats techniques](dom-016-annexes/dom-016-resultats.json)
conservent les contrôles réellement exécutés.

**Portée :** voir la [portée de la vérification](dom-016-annexes/dom-016-verification.md#portée).
La relecture des livrables est prise en charge par l’utilisateur ; elle
n’est pas déclarée effectuée et ne maintient pas ce cadrage ouvert.
