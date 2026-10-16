---
id: FUN-008
titre: "Organiser les démarches et pièces des premiers jours après un décès"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-001]
---

# FUN-008 — Organiser les démarches et pièces des premiers jours après un décès

## Objectif et résultat attendu

Un proche qui vient d'apprendre un décès obtient une liste ordonnée des
démarches des premiers jours (constat, déclaration, choix d'un opérateur,
autorisations, cérémonie), les pièces à réunir et l'interlocuteur de chaque
étape, présentée comme une liste à vérifier et non comme un calendrier
juridique.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/after-death-first-steps/SKILL.md` — le skill (à créer)
- `funeral-legal/references/premieres-demarches.md` — étapes, pièces, interlocuteurs, sources lues (à créer)
- `funeral-legal/references/qualification-funeraire.md` — relue, créée par FUN-001
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Lieu du décès : domicile, établissement de santé ou médico-social, voie publique ; date déclarée.
- Démarches déjà faites : certificat, déclaration, contact d'un opérateur.
- Volontés connues ; contrat obsèques connu ; obstacle signalé par un médecin ou les autorités.
- Personne qui organise et proches à informer, sans données de santé du défunt.

## Sortie attendue

1. En tête : ce qui est à faire en premier et ce qui peut attendre.
2. Liste ordonnée : étape, interlocuteur, pièce, statut (fait, à faire, à vérifier).
3. Délais signalés comme existants et à vérifier, jamais chiffrés sans source lue.
4. Points de décision à ne pas précipiter : signature d'un devis (FUN-001), désaccord (FUN-003).
5. Suites : obstacle médico-légal ou enquête → DOM-002 ; succession → DOM-016 ; comptes et contrats → DOM-016, DOM-005.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `premieres-demarches.md` et l'appliquer : chaque étape est sourcée ou
marquée « à vérifier » ; aucun délai d'inhumation ou de crémation n'est
donné sans texte lu. Le skill n'effectue aucune démarche et ne recommande
aucun opérateur. Il rappelle qu'il est possible de comparer des devis, sans
pression ni jugement.

## Références métier et sources à rechercher

Code civil, déclaration et acte de décès (pistes 78 et suivants) ; CGCT,
certificat de décès (piste L2223-42), opérations consécutives au décès et
autorisations d'inhumation ou de crémation (pistes R2213-1-1 et suivants,
R2213-31 et suivants) ; soins de conservation (pistes R2213-2-1 et
suivants) ; information officielle Service Public.

## Critères d'acceptation

- [ ] M01 produit une liste ordonnée avec interlocuteurs et pièces, délais signalés sans chiffre non sourcé.
- [ ] M02 place l'obstacle médico-légal en tête et oriente vers DOM-002 sans conclure.
- [ ] La sortie se comprend dans un moment de deuil, sans jargon.
- [ ] La sortie se termine par la phrase BASE-013 nommant la mairie ou le notaire comme interlocuteurs de démarche et un avocat en cas de difficulté.

## Vérification

- Cas normal : M01 — Décès à domicile d'une personne âgée, aucun contrat obsèques connu.
- Cas limite : M02 — Décès sur la voie publique, la famille informée qu'un obstacle médico-légal empêche les obsèques.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Démarches successorales, bancaires et sociales au fond, élément étranger,
réalisation d'une démarche, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 8, 15, 21, 23–32, 37–38, 98 et checklist R01–R19 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FM01 — Qualifier domicile/hôpital/EHPAD/voie publique et distinguer certificat médical, déclaration et acte d’état civil : qui agit, auprès de qui, pièce, coût allégué et preuve. Ne pas généraliser un délai entre ces lieux.
- [ ] FM02 — Distinguer conservation au domicile, chambre mortuaire et chambre funéraire, initiateur du transfert, mise en bière, autorisations et périodes facturées ; relayer une facture litigieuse vers FUN-002.
- [ ] FM03 — Séparer transport avant mise en bière, inhumation/crémation et exhumation ultérieure ; établir décès, autorisation judiciaire, territoire, dérogation et preuve avant un délai. Un obstacle médico-légal passe en tête sans enquête ni autopsie conseillée.
- [ ] FM04 — Proposer une checklist avec fait/à faire/à vérifier, responsable, pièce et interlocuteur, et signaler les objets parallèles : volontés/contrat, comptes, assurances, logement, aides, emploi et succession. Ne pas reporter une urgence de capital ou de recours derrière le seul ordre « premiers mois ».

Scénarios supplémentaires **attendus, non exécutés** : décès à domicile et délai allégué non confirmé ; transfert d’un EHPAD demandé par son directeur ; obstacle levé mais date d’autorisation absente ; proches demandant toutes les démarches et une priorité CPAM imminente.

Sources à ouvrir lors de l’implémentation : Code civil état civil, textes CGCT et santé sur constat/certificat/chambres/transports/obsèques ; sources officielles par lieu, territoire, obstacle et exception. Recherche des contrats et délais sociaux chez leurs propriétaires.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
