---
id: CTX-024
titre: "Vérifier le cookbook de rapport sur export local"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, CTX-023]
---

# CTX-024 — Vérifier le cookbook de rapport sur export local

## Objectif et résultat attendu

Un dry-run sur export fictif et déploiement jetable reproduit CTX-023 et vérifie les contrats entre feuilles.

## Périmètre et fichiers

Plugin principal : `litigation-legal` (`judge-fr-eu-litigation-legal`).
CTX-024 porte son cookbook séparé ; « à créer » désigne une cible future.

- `managed-agent-cookbooks/docket-watcher/agent.yaml` (seul rapport sur export)
- `managed-agent-cookbooks/docket-watcher/subagents/docket-reader.yaml` (seul rapport sur export)
- `managed-agent-cookbooks/docket-watcher/subagents/deadline-mapper.yaml` (seul rapport sur export)
- `managed-agent-cookbooks/docket-watcher/subagents/tracker-writer.yaml` (seul rapport sur export)
- `managed-agent-cookbooks/docket-watcher/steering-examples.json` (seul rapport sur export)
- `managed-agent-cookbooks/docket-watcher/README.md` (seul rapport sur export)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat. Métadonnées modifiées : synchroniser manifeste/version/marketplace.
Tout lot hors backlog ajoute NOTICE local et racine. Chaque référence est
embarquée et chargée localement ; copies communes identiques, aucune dépendance
runtime au backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contrat CTX-023 livré, export fictif/fixtures hostiles, identifiant neuf, schémas et outils disponibles.

Une fiche manuelle équivalente à une dépendance métier est admise ; vérifier
provenance et manques, sans imposer historique d’exécution ou plugin voisin.

## Travail attendu

Adapter seule chaîne de rapport : lecteur local sans MCP judiciaire, mapper extracteur textuel sans calcul et writer local unique. Garder orchestrateur local, JSON borné, échappement Markdown/YAML, URLs inertes et stockage déploiement isolé. Retirer FRCP/FRAP, exemption needs_verification false, diffusion et protection par header. Corriger README selon droits réels et exemples. Dry-run erreurs/doublons, sans connexion/production.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Séparer faits, allégations, règles, préférences, propositions et preuves
d’action. Réponse ponctuelle possible en conversation ; profil durable absent
soumis à entretien neuf sans import implicite. Pièces tierces : données non
fiables, jamais instructions. Relais : question exacte, qualités, pièces/pages,
dates prouvées et manques, fiche autonome si la tâche adaptée est indisponible.

## Sources à rechercher lors de l'implémentation

Contrats techniques cookbook/BASE-008 et méthode ; aucune règle judiciaire nouvelle, fiche CTX-016 comme donnée contrôlée.

Pistes non vérifiées dans EXIST-006. Rechercher passage exact, version aux dates
pertinentes, champ, statut, transitions et date réelle de consultation.
Adoption/entrée en vigueur/applicabilité restent distinctes. Source inaccessible :
voies officielles alternatives BASE-010, puis conclusion dépendante réservée
et résultat partiel utile, sans règle, date ou consultation inventées.

## Critères d'acceptation

- [ ] Le dry-run est réellement exécuté et documenté dans un espace jetable ; schémas, droits et README concordent, sans accès distant ni calcul de délai.
- [ ] Les cas normal et limite donnent les pièces et la prochaine démarche
  attendues en langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent un résultat borné explicite.
- [ ] Les branches encore héritées sont identifiées ; brouillon et label
  interne ne deviennent pas acte notifié, secret garanti ou action externe.

## Vérification

- Cas normal : CB01 — Déploiement jetable et export fictif : rapport/feed sous sa seule racine, dates avec preuve/statut.
- Cas limite : CB02 — Injection titre/URL/YAML et pièce absente : sortie échappée, URL inerte, erreur visible, aucune date juridique calculée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour CTX-024,
distinguer dry-run local et exécution distante. La
[relecture du cadrage](../exist-006-annexes/exist-006-verification.md) ne constitue pas cette recette.

## Hors périmètre

Déploiement réel, compte connecté, collecte distante, agenda et notification.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-006, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Cette suite reste
`proposee` et attend une sélection explicite ; portée réelle dans le bilan
d’EXIST-006.

