---
id: EXIST-009
titre: "Découper l'adaptation de la clinique juridique"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-009 — Découper l'adaptation de la clinique juridique

## Objectif

Adapter l'accueil, la recherche et la supervision aux pratiques françaises sans conserver les présupposés de clinique américaine.

## Points de départ

- [legal-clinic/references/plausibility-bands/CA.md](../../legal-clinic/references/plausibility-bands/CA.md)
- [legal-clinic/references/plausibility-bands/IL.md](../../legal-clinic/references/plausibility-bands/IL.md)
- [legal-clinic/skills/deadlines/SKILL.md](../../legal-clinic/skills/deadlines/SKILL.md)
- [legal-clinic/skills/client-intake/SKILL.md](../../legal-clinic/skills/client-intake/SKILL.md)
- [legal-clinic/skills/research-start/SKILL.md](../../legal-clinic/skills/research-start/SKILL.md)
- [legal-clinic/deadlines.yaml](../../legal-clinic/deadlines.yaml)
- [legal-clinic/CLAUDE.md](../../legal-clinic/CLAUDE.md)

## Travail attendu

- Auditer les références Californie/Illinois et leur chargement automatique ; ne pas simplement les renommer France et conserver leurs fenêtres de délais.
- Séparer accueil, recherche, rédaction supervisée, registre des échéances et transmission de dossiers ; définir des stories distinctes.
- Qualifier le cadre réel de la clinique, les rôles et la supervision ; ne pas importer des obligations ABA comme règles françaises.
- Prévoir les domaines français d'accueil, la protection des données, les conflits et les urgences ; conserver les incertitudes visibles pour le superviseur.
- Sources à prévoir et à vérifier lors des futures implémentations : Sources françaises par matière, règles de la structure et encadrement professionnel applicable ; aucune bande américaine chargée par défaut dans un dossier français.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `legal-clinic`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Suivre une échéance saisie avec notification inconnue et un accueil logement ; vérifier quelles références sont chargées et qui valide l'action.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

