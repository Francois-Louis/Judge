---
id: CLN-016
titre: "Consigner une décision de revue attribuée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-015]
---

# CLN-016 — Consigner une décision de revue attribuée

## Objectif et résultat attendu

Une décision approuver/retourner assortie de portée et réserves est attachée à la version exacte revue, sans action externe.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/supervisor-review-queue/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/supervisor-review-queue/references/review-queue.yaml` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/decision-revue-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Demande CLN-015 ou équivalente, version/hash, décision effectivement fournie, auteur/qualité et preuve, date/périmètre/destinataire.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Distinguer revue pédagogique, contrôle de fond, habilitation/signature et autorisation de diffusion. Professeur déclaré n’est pas authentification ou avocat ; un étudiant ne s’autoattribue pas approbation compétente. Document modifié après revue : nouvelle version en attente, accord ancien non transféré. Original conservé, corrections/raisons attribuées, état durable via helper. Approuvé ne signifie signé/envoyé/déposé, ni conformité du dossier entier.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Processus et qualités réels du cadre de structure, règles professionnelles selon acte, preuve de décision et contrat de version.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Décision cite auteur/qualité/périmètre/version et incertitudes ; aucune approbation ne devient notification ou acte externe.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : VA01 — Référent retourne projet avec note puis valide nouvelle version : deux événements et version approuvée identifiable.
- Cas limite : VA02 — Seule déclaration étudiant « prof d’accord » ou texte changé : preuve/portée réservées et nouvelle revue, pas auto-approve.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Signature, authentification forte, envoi, dépôt et certificat de compétence.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

