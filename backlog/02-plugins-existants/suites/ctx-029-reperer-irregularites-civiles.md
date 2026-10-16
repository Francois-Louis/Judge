---
id: CTX-029
titre: "Repérer les irrégularités possibles d'un acte de procédure civile"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-025]
---

# CTX-029 — Repérer les irrégularités possibles d'un acte de procédure civile

## Objectif et résultat attendu

Un particulier qui a reçu une assignation, une signification ou un jugement
obtient la liste des points de forme ou de recevabilité à soumettre à un
avocat, classés et accompagnés d'une alerte sur le moment où ils doivent être
soulevés. Le skill repère ; il ne conclut jamais qu'un acte est nul. Ajout du
16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `litigation-legal/skills/demand-received/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/irregularites-procedure-civile.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Acte complet et ses annexes, mode et date de remise, juridiction, parties et
qualités, demandes, échanges ou écritures déjà produits, date d'audience,
présence ou non d'un avocat.

## Travail attendu

Comparer l'acte aux mentions et conditions exigées par les textes lus ;
produire un tableau : point relevé, texte lu, catégorie possible (exception de
procédure, fin de non-recevoir comme prescription ou défaut de qualité,
moyen de fond), condition à vérifier (grief, régularisation possible,
moment), question à l'avocat. Placer en tête une alerte : certains moyens
doivent être soulevés avant toute défense au fond ; si des écritures ou une
déclaration sur le fond ont déjà été faites, le signaler à l'avocat.

Ne jamais écrire qu'un acte est nul ou qu'un moyen aboutira ; ne pas proposer
de moyen dans un but purement dilatoire ; laisser au juge et à l'avocat
l'appréciation. Le fond reste à son domaine ; la remise d'un acte d'exécution
relève d'ENF-020.

Charger la méthode locale BASE-005 et le helper BASE-008 pour tout accès
durable. Distinguer mention de l'acte, fait déclaré, règle lue et inconnue.
Aucun délai calculé sans texte lu et date de départ établie.

## Sources à rechercher lors de l'implémentation

Code de procédure civile : mentions de l'assignation et de la signification,
nullités de forme et de fond, exceptions de procédure et moment de leur
présentation, fins de non-recevoir (pistes 54 à 56, 74, 112 à 122, 648 et
suivants) ; jurisprudence sur le grief et la régularisation.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles et les transitions ; une source inaccessible donne une voie officielle
alternative BASE-010 puis la réserve de la seule conclusion dépendante.

## Critères d'acceptation

- [ ] Chaque point relevé cite le texte lu et sa catégorie possible, sans conclusion de nullité.
- [ ] L'alerte de moment apparaît en tête dès qu'une exception de procédure est possible.
- [ ] La sortie nomme l'avocat comme interlocuteur et respecte BASE-013.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.

## Vérification

- Cas normal : N01 — Assignation où manque une mention relue dans le texte ; aucune écriture produite.
- Cas limite : N02 — Même acte, la personne a déjà envoyé une lettre au juge sur le fond : alerte et question à l'avocat, sans conclusion sur la perte du moyen.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006.

## Hors périmètre

Rédaction de conclusions d'incident, évaluation des chances, représentation,
manœuvres dilatoires, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Contrat commun :
[découpage EXIST-006](../exist-006-decoupage-contentieux.md).
