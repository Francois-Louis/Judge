---
id: CTX-003
titre: "Préparer une demande de paiement contractuelle B2B"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006]
---

# CTX-003 — Préparer une demande de paiement contractuelle B2B

## Objectif et résultat attendu

Une fiche documente une obligation de paiement B2B et les pièces nécessaires au projet.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/demand-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/demand-letters/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/intake-paiement-b2b.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contrat/devis accepté, facture, prestation/livraison, exigibilité alléguée, paiements/avoirs, parties, territoire/loi, échanges et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Borner à une obligation contractuelle française B2B ; exclure difficultés collectives, dette consommateur, emploi et titres exécutoires. Identifier montant/devise/fondement et preuves contraires. Demander destinataire, pouvoir du signataire, clause de notification et preuve utile. Retirer valeurs 7/14/30 jours et protection par mention par défaut. Une fiche manuelle équivalente suffit pour CTX-004, sans matérialité minimale.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Code civil, dispositions commerciales applicables au paiement selon opération/parties, clause réelle et textes de notification.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Chaque montant et exigibilité renvoie à une pièce ; aucun délai uniforme, intérêt ou pénalité n’est ajouté sans fondement vérifié.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : I01 — TPE avec facture et acompte : tableau facture/paiement/avoir, objectif et manques pour un solde.
- Cas limite : I02 — Contrat étranger ou dette consommateur : qualifier écart de champ et préparer relais au lieu du modèle français B2B.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Lettre, transaction et calcul général de toutes créances.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

