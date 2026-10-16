---
id: CLN-015
titre: "Soumettre une version de sortie à revue"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-001]
---

# CLN-015 — Soumettre une version de sortie à revue

## Objectif et résultat attendu

Une demande de revue identifie version/empreinte de sortie, auteur, destinataire prévu, questions et référent requis.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/supervisor-review-queue/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/supervisor-review-queue/references/review-queue.yaml` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/draft/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/client-letter/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/status/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/soumission-revue-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Cadre/processus CLN-001 ou équivalent, document/version, auteur/qualité, public/canal, questions/urgence et destinataire de revue.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Posséder contrat de demande et modèle de queue ; état mutable sous racine BASE-008, jamais references/review-queue.yaml installé. Geler contenu/version/hash ou référence stable, conserver réserves/dates et statut en attente. File formelle activée ou revue externe équivalente enregistrée, pas absence de queue=absence de revue. Identité déclarée distincte d’habilitation ; aucune notification, accord, libération d’envoi ou modification de fichier source depuis soumission.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Règles de revue/diffusion réelles et encadrement des actes selon rôles, contrat d’isolation/version ; aucune obligation ABA supposée.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Référence empaquetée reste modèle en lecture seule ; demande porte version exacte et ne certifie ni revue reçue ni autorisation externe.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : RV01 — Projet bailleur et deux réserves : demande de revue avec hash/version, destinataire prévu et référent.
- Cas limite : RV02 — Référent absent, document changé ou queue désactivée : en attente/à identifier, pas suppression de besoin de revue ou édition du paquet.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Décision de validation, envoi, dépôt et authentification IAM nouvelle.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

