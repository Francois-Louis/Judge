---
id: HUB-003
titre: "Gérer les registres surveillés et leur cache"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002]
---

# HUB-003 — Gérer les registres surveillés et leur cache

## Objectif et résultat attendu

Un catalogue identifie registres surveillés, autorisation distincte et date/couverture du cache, avec ajout ou pause explicite.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/registry-browser/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/registry-browser/references/registries.yaml` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/references/registry-catalog.md` : à créer, propriétaire HUB-003.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Registres sélectionnés et politique active, index réellement accessible, version/récupération précédente et disponibilité réseau.

## Travail attendu

- Corriger le commentaire HTML initial de registries.yaml et séparer modèle de paquet, watchlist active et cache utilisateur.
- Définir la source canonique de watchlist, projections du profil, identifiants de dépôts et mise en pause sans perte du journal ; ajouter un registre ne modifie pas l’allowlist.
- Lister les métadonnées effectivement lues et manquantes, erreurs par registre et cache périmé ; sept jours est une durée technique déclarée, pas actualité juridique.
- Les trois registres autorisés dans le modèle et le seul registre surveillé par défaut sont des ensembles distincts ; nombre déclaré de skills et réputation ne sont pas des vérifications actuelles.

## Sources à rechercher lors de l'implémentation

Index et provenance des registres réellement consultés, politique locale ; ne pas promettre disponibilité, licences ou couverture FR/UE depuis une description héritée.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Mode hors ligne produit un résultat daté et borné, sans annoncer un sync réussi.
- [ ] Ajout/suppression de surveillance préserve les installations et les autorisations indépendantes.
- [ ] Les entrées adaptées chargent isolation, méthode partagée et références
  métier locales pertinentes. Les contrôles BASE-008/009 existants sont conservés.
- [ ] Les scénarios ci-dessous sont exécutés avec sorties et limites consignées ;
  les checks BASE-006 appropriés portent sur un paquet extrait.
- [ ] Les cinq copies partagées et helpers BASE-008 restent inchangés dans cette
  tâche de consommation de leurs contrats. Une limite du helper requiert un lot
  technique distinct, jamais une mutation directe pour le contourner.
- [ ] Documentation, version/NOTICE et champs communs du marketplace reflètent
  les seuls comportements effectivement livrés ; aucune suite proposée annoncée
  disponible, aucun contrôle statique présenté comme recette client.

## Vérification

- Cas normal : RG01 — Un index accessible et un cache ancien : actualiser seulement le registre réussi avec sa provenance.
- Cas limite : RG02 — Nouveau registre non autorisé ou inaccessible : état explicite, aucune confiance accordée ni remplacement par données inventées.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

