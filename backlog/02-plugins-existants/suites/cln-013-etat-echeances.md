---
id: CLN-013
titre: "Présenter les échéances et dates à vérifier"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-012]
---

# CLN-013 — Présenter les échéances et dates à vérifier

## Objectif et résultat attendu

Un rapport local distingue dates établies, déclarées, à déterminer et jalons internes avec couverture et responsables de vérification.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/deadlines/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/status/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/etat-echeances-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Registre CLN-012 ou équivalent, périmètre autorisé, date de référence/fuseau explicites, états/provenances et filtres.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Ne pas calculer ni confirmer dates. Exposer inconnus en rubrique prioritaire de vérification et non-lus ; ne pas masquer car due_date nulle. Distinguer dépassement d’une date déclarée, échéance juridique validée dépassée et rappel interne. Lecture de bande CA/IL/federal interdite pour France ; aucune formule no-plausibility-band=problème à corriger par copie. Rapport ne prouve ni alerte remise ni absence d’urgence sur dossier sans date. Cadences 14/7/3/1 sont préférences de vue, pas délais de procédure.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Registre, preuves et méthode ; sources du délai uniquement dans fiche vérifiée par responsable compétent, aucun calcul clinique.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Notification inconnue reste visible et ne devient ni date sûre ni affaire standard ; aucune couleur ne certifie règle ou alerte envoyée.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : ER01 — Trois dates vérifiée/déclarée/inconnue : rubriques distinctes, provenance et personnes à vérifier.
- Cas limite : ER02 — Registre vide/partiel ou date de saisie dépassée sans notification : couverture et vérification urgente à instruire, pas overdue juridique certain.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Calcul, notification réelle, système de greffe et agenda.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

