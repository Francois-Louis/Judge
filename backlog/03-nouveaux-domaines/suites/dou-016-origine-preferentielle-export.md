---
id: DOU-016
titre: "Préparer l'attestation d'origine préférentielle d'une vente à l'export"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001, DOU-007]
---

# DOU-016 — Préparer l'attestation d'origine préférentielle d'une vente à l'export

## Objectif et résultat attendu

Un exportateur français veut que son client d'un pays tiers bénéficie d'un
droit réduit ou nul grâce à un accord commercial de l'Union. Le résultat est
une fiche accord × produit × envoi : accord applicable à la date de l'envoi
(ou absence d'accord), preuve d'origine requise et son auteur, enregistrement
REX ou statut d'exportateur nécessaire, règle d'origine du produit à
satisfaire, pièces de fabrication à conserver, et brouillon de mention à
reporter sur la facture lorsque toutes les conditions sont sourcées.

## Origine

Demande de l'utilisateur du 19 octobre 2026. Les destinations citées relèvent
de situations différentes à vérifier : accords en vigueur (Canada, Mexique,
Chili, Afrique du Sud, Tunisie), accord appliqué à titre provisoire avec le
Mercosur depuis le 1er mai 2026 selon des sources secondaires, accord avec
l'Australie conclu le 24 mars 2026 mais pas encore en vigueur selon des
sources secondaires, absence d'accord avec les États-Unis, préférences
unilatérales du Cambodge sans effet pour les exportations de l'Union. Reprend
K04, C19 et les points 28 à 31 de la
[matrice des frictions](../dom-009-annexes/dom-009-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `customs-legal`. Fichiers futurs :
`customs-legal/skills/export-origin-statement/SKILL.md` et
`customs-legal/references/origine-preferentielle-export.md` avec un tableau
des accords datés (à créer). Charge la référence de DOU-007 lorsqu'elle existe,
sans la réécrire ; sinon réserve le dossier de fabrication. Contrat commun
DOM-009 applicable.

## Pièces et informations nécessaires

Pays de destination et date d'expédition, classement tarifaire retenu
(DOU-006), nomenclature des composants (lame, manche, ressort, vis, étui) avec
origine et déclarations fournisseurs, opérations réalisées en France, valeur
des composants non originaires, valeur de l'envoi, numéro REX ou statut
d'exportateur agréé annoncé, Incoterm et importateur.

## Sortie attendue

Tableau : accord / statut et date d'application / règle de liste du chapitre
ou de la position / test satisfait, non satisfait ou inconnu / preuve requise
(EUR.1, EUR-MED, déclaration ou attestation d'origine, REX) / seuil propre à
l'accord / pièces à conserver et durée. Brouillon de mention uniquement si
accord, règle et statut d'exportateur sont sourcés. Rappel que « Made in
France » n'est ni origine préférentielle ni preuve.

## Travail attendu

- Lire au Journal officiel de l'Union le texte de chaque accord de la
  tranche (protocole ou chapitre origine, règles de liste, formule de
  l'attestation, seuils), sa date d'application et ses dispositions
  transitoires. Vérifier sur source officielle le statut Mercosur et Australie.
- Lire la convention PEM révisée et son application avec la Tunisie.
- Lire les règles REX (règlement d'exécution (UE) 2015/2447) et la procédure
  française d'enregistrement.
- Ne proposer aucune mention d'origine improvisée ; ne présumer aucun accord
  pour un pays non vérifié.

Méthode BASE-005 locale, BASE-013 et BASE-014 (date de relecture par accord).

## Critères d'acceptation

- [ ] Pour un couteau à lame d'acier importé et manche français vers le Canada, la règle de liste est lue et le résultat reste conditionnel tant que l'origine des composants manque.
- [ ] Pour les États-Unis et le Cambodge, la fiche indique l'absence de préférence pour une exportation de l'Union, avec source.
- [ ] Le seuil au-delà duquel un enregistrement REX est requis n'est donné que pour l'accord dont le texte a été lu.
- [ ] La sortie se termine par la phrase BASE-013 (service des douanes, conseiller en origine, commissionnaire) ; aucun avantage tarifaire garanti.
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 consignée.

## Vérification

- Cas normal : envoi B2B vers le Chili avec nomenclature complète.
- Cas limite : envoi vers le Brésil pendant l'application provisoire : statut et date vérifiés.
- Cas complémentaire : envoi vers l'Australie avant entrée en vigueur : aucune préférence.
- Information manquante : déclaration fournisseur de la lame absente.
- Sans source : protocole d'origine inaccessible ; aucune mention proposée.
- Héritage américain : certificat USMCA fourni ; non transposé.

Scénarios **attendus, non exécutés**. La relecture humaine est prise en charge
par l'utilisateur selon CLAUDE.md.

## Hors périmètre

Renseignement contraignant d'origine (C19), origine non préférentielle et
marquage d'origine à destination (DOU-014 pour les couteaux aux États-Unis),
calcul des droits (C26), contrôle a posteriori de l'origine.
