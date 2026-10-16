---
id: CTX-004
titre: "Rédiger un projet de mise en demeure de paiement B2B"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-003]
---

# CTX-004 — Rédiger un projet de mise en demeure de paiement B2B

## Objectif et résultat attendu

Un projet versionné de lettre réclame un solde documenté avec checklist de signature et notification.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `litigation-legal/skills/demand-draft/SKILL.md` (blocs nécessaires à cette tranche)
- `litigation-legal/demand-letters/_README.md` (blocs nécessaires à cette tranche)
- `litigation-legal/references/projet-paiement-b2b.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche CTX-003 ou équivalente, pièces/version, destinataire, représentant, clause et mode de notification, dates et montants vérifiés.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Réécrire seulement squelette paiement, chaque fait/montant lié à sa pièce. Distinguer assertion de droits et offre transactionnelle. Vérifier forme/effets, signature et notification dans le régime retenu. Retirer FRE 408, without prejudice protecteur, accord and satisfaction, sanctions de spoliation et poursuite certaine. Marquer réserves ; produire docx seulement si outil effectif avec solution textuelle. Brouillon/envoi/réception gardent états distincts.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Code civil et dispositions commerciales applicables ; clause, représentation/signature et règles professionnelles si auteur avocat.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Le projet distingue signature, envoi et réception ; aucune mention ne garantit confidentialité ou effet juridique et aucun docx inexistant n’est annoncé.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : D01 — Solde B2B documenté et clause fournie : projet factuel, annexes, destinataire et checklist, sans menace non étayée.
- Cas limite : D02 — Signataire incertain et demande d’ajouter without prejudice : question précise et effets réservés, pas de délai 14 jours par défaut.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Autres squelettes, transaction, acte d’exécution et envoi.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

