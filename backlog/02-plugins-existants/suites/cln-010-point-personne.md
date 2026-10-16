---
id: CLN-010
titre: "Préparer un point à la personne accueillie"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-002]
---

# CLN-010 — Préparer un point à la personne accueillie

## Objectif et résultat attendu

Un projet de point accessible expose faits de suivi établis, actions à confirmer et prochaines questions sans consultation nouvelle.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/status/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/plain-language-letters/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/point-personne-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Dossier/pièces/journal autorisés, destinataire/canal, décisions et dates qualifiées, cadre et périmètre communicable.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Distinguer fait déclaré/prouvé, action prévue/réalisée et état de revue. Ne pas annoncer nous avons déposé/accepté depuis brouillon ou absence de journal. Questions de fond/mauvaise nouvelle sont soumises au référent compétent sans cacher automatiquement faits importants. Retirer signature student-attorney et mise en forme tribunal. Revue d’une version/destinataire avant usage ; projet n’est pas contact loggé comme fait.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Pièces de suivi, règles de structure/données/diffusion, analyse sectorielle fournie si une explication substantielle est requise.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Point ne crée aucun dépôt, acte, admission ou conseil nouveau ; pièces et incertitudes à communiquer sont identifiées pour revue.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : ST01 — Deux pièces reçues et réponse attendue : projet simple distinguant fait établi et prochaine action.
- Cas limite : ST02 — Issue défavorable alléguée sans décision ou canal partagé : réserver contenu, référent/canal à confirmer, pas faux rassurement.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Envoi, consultation nouvelle, acte à juridiction et suppression des incertitudes.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

