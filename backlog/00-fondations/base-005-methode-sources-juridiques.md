---
id: BASE-005
titre: "Définir la méthode de recherche et de vérification France/UE"
statut: terminee
priorite: P0
nature: cadrage
dependances: [BASE-003]
---

# BASE-005 — Définir la méthode de recherche et de vérification France/UE

## Objectif

Fixer les règles communes de recherche sans centraliser les raisonnements de tous les domaines.

## Points de départ

- [references/](../../references/)
- [privacy-legal/references/currency-watch.md](../../privacy-legal/references/currency-watch.md)
- [regulatory-legal/skills/reg-feed-watcher/references/source-catalog.md](../../regulatory-legal/skills/reg-feed-watcher/references/source-catalog.md)
- [legal-clinic/skills/deadlines/SKILL.md](../../legal-clinic/skills/deadlines/SKILL.md)

## Travail attendu

- Définir qualification territoriale, date des faits, qualité des parties et articulation France/UE ; distinguer UE, CEDH et autres droits étrangers.
- Définir citation et traçabilité : texte ou décision exacts, version applicable, lien, date réelle de consultation et statut de vérification.
- Définir le traitement d'une source inaccessible, d'une réforme non encore applicable et d'une règle non vérifiée.
- Définir les informations minimales pour un délai : nature, événement déclencheur, preuve de date, calcul, exceptions et contrôle humain adapté.
- Confier les sources et raisonnements sectoriels aux références du plugin concerné.

## Critères d'acceptation

- [x] La méthode n'affirme pas qu'un document généré bénéficie automatiquement du secret professionnel.
- [x] Elle ne transforme pas une directive, un projet de réforme ou une fiche pratique en règle directement applicable sans analyse.
- [x] Une recherche impossible produit une limite explicite, pas une source ou une date de consultation inventée.
- [x] La méthode peut être embarquée dans un plugin autonome selon la solution retenue en BASE-003.

## Vérification

Éprouver la méthode sur une source inaccessible, un litige ancien, une demande transfrontalière et une date de notification inconnue. Ce sont des scénarios de contrôle, pas des consultations déjà réalisées.

## Hors périmètre

Constituer un corpus exhaustif des codes ou figer des barèmes et délais pour tous les domaines.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [méthode commune de recherche et de citation](../../references/research-citation-method.md),
  version `1.0.0`, avec qualification territoriale, temporelle et personnelle,
  articulation France/UE, distinction CEDH et autres droits étrangers.
- Citation et relevé de sources : document et passage exacts, version, lien,
  dates réelles de tentative/consultation, statut documentaire et applicabilité
  motivée séparément. Traitement des sources inaccessibles, règles non vérifiées,
  réformes futures, directives et documents d'information défini explicitement.
- Fiche minimale de délai : nature, fondement, déclencheur, preuve de date,
  calcul reproductible, exceptions et contrôle humain adapté. Notification
  inconnue : échéance à déterminer, sans substitution d'une date ni durée par défaut.
- [Compte rendu de vérification](base-005-verification-methode.md) : relecture
  des quatre scénarios fictifs demandés et relevé des accès officiels réellement
  effectués, y compris refus 403 et écrans JavaScript. Les limites sont conservées.
- Embarquement conforme au contrat BASE-003 : copie ordinaire intégrale sous
  `references/shared/research-citation-method.md`, version et provenance incluses,
  sources métier locales. Copie temporaire isolée comparée à l'identique et chemin
  depuis un skill vérifié ; liens locaux et format des documents contrôlés.
- Limites : aucun plugin existant adapté ou synchronisé, aucune installation,
  aucun skill exécuté, aucune consultation sectorielle ni échéance réelle validée.
  La recette des paquets réels reste à BASE-006 et aux lots concernés. Aucune
  garantie automatique de secret professionnel n'est attribuée aux documents générés.

