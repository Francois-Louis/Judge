---
id: CLN-005
titre: "Préparer un plan de recherche français borné"
statut: abandonnee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-002]
---

# CLN-005 — Préparer un plan de recherche français borné

## Objectif et résultat attendu

Un plan sur une question donne faits déterminants, sources primaires à rechercher, versions/dates et questions restant à instruire.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/research-start/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/plan-recherche-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Question précise, faits/pièces/pays/dates, guide de structure ou équivalent, recherches déjà faites et objectif pédagogique.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Séparer piste et source effectivement lue, ne pas proposer numéro/article/arrêt inventé même verify. Précédent de clinique doit être versionné/autorisé, pas présumé actuel ou supérieur au texte. Remplacer requêtes Westlaw/USCIS/BIA par sources officielles France/UE du sujet, sans abonnement imposé. Guide manquant ou moins de dix seeds ne donne pas défaut juridique automatique ; pas analyse sectorielle depuis plan. Recherche échouée laisse réserve ciblée et autre voie officielle pertinente.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Méthode locale BASE-005/010, sources françaises de matière confiées au domaine et EUR-Lex si rattachement pertinent ; décisions primaires exactes seulement lorsqu’elles sont lues.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Chaque référence est piste ou lecture prouvée ; plan ne certifie ni droit applicable ni jurisprudence depuis citation vraisemblable.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : RE01 — Question logement bornée depuis courrier : axes/termes/pièces et sources officielles à consulter, pas conclusion de droit.
- Cas limite : RE02 — Source indisponible et ancien memo anonymisé : relever version/manques et alternative, sans texte ou consultation inventés.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Réponse juridique finale, corpus exhaustif et recherche payante obligatoire.

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
