---
id: CLN-022
titre: "Modifier une préférence de clinique"
statut: abandonnee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006]
---

# CLN-022 — Modifier une préférence de clinique

## Objectif et résultat attendu

Une préférence ciblée et attribuée modifie présentation ou organisation sans requalifier rôle, validation ou dossiers antérieurs.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/customize/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/CLAUDE.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/preferences-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Demande ciblée, profil existant ou absence, rôle déclaré, cadre pertinent et version courante.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Préserver entretien neuf pour profil absent, digest et refus d’écrasement concurrent. Séparer préférence, règle de structure, fait et habilitation. Changement de pédagogie/contact ne libère ni diffusion ni consultation, ne transforme aucune date ou décision passée. Pas stage partagé inventé, import amont ou réécriture de toutes pièces. Aide ponctuelle fictive possible sans profil durable.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Contrat BASE-008, guide canonique et cadre réel pour seuls champs concernés ; pas de règle ABA ou juridique depuis préférence.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Modification reste ciblée/provenancée et ne lève aucune revue requise ; profil absent ou concurrent n’est pas écrasé.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : PR01 — Structure veut langage plus simple et remplace contact de suivi : changement ciblé avec effet expliqué.
- Cas limite : PR02 — Étudiant veut désactiver revue sans autorité, profil absent ou concurrent : demande non traitée comme habilitation, entretien/état à confirmer sans écrasement.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-annexes/exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Décision professionnelle, migration amont et modification globale des dossiers.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

## Abandon — 16 octobre 2026

Story abandonnée : le plugin `legal-clinic` a été retiré du marketplace et du
dépôt sur décision de l'utilisateur ([décisions du
16 octobre 2026](../../decisions-2026-10-16.md)). Aucune partie de cette story
n'a été implémentée. Le cadrage reste consultable ; le plugin hérité est
récupérable dans l'historique git si une clinique française est reprise un jour.
