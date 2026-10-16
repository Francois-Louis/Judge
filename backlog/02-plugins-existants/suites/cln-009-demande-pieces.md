---
id: CLN-009
titre: "Préparer une demande routine de pièces à la personne"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-002]
---

# CLN-009 — Préparer une demande routine de pièces à la personne

## Objectif et résultat attendu

Un brouillon simple demande les seules pièces utiles à une personne accueillie, avec motif, canal et personne à contacter.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/client-letter/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/plain-language-letters/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/demande-pieces-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche d’accueil, liste de manques justifiés, destinataire/canal adapté, règles de structure, auteur/qualité et besoins de compréhension.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Limiter à demande administrative de pièces, pas conseil substantiel ni annonce d’acceptation du cas. Expliquer pourquoi chaque pièce est utile et possibilité de signaler absence, éviter données sensibles inutiles. Signature reflète qualité réelle, pas student-attorney. Alias plain-language-letters garde redirect cohérent. Préparer version et route de revue selon cadre, aucun envoi ou exemption depuis lighter-touch.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Règles internes accueil/données/accessibilité et encadrement auteur/diffusion selon cadre réel ; critères de pertinence des pièces fournis par référent/domaine.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Demande est compréhensible, minimale et non envoyée ; rôle exact et revue nécessaire sont visibles, pas signature d’avocat fictive.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : LE01 — Bail et courrier manquants : demande claire de pièces déjà identifiées et canal de réponse choisi.
- Cas limite : LE02 — Donnée sensible non nécessaire ou adresse partagée risquée : restreindre contenu et canal, sans collecte globale ou envoi.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Conseil, mauvaise nouvelle, admission, diagnostic et contact réel.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

