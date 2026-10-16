---
id: EXIST-009
titre: "Découper l'adaptation de la clinique juridique"
statut: terminee
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

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `legal-clinic`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire sur fixtures fictives par le rédacteur).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Suivre une échéance saisie avec notification inconnue et un accueil logement ; vérifier quelles références sont chargées et qui valide l'action.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-009-annexes/exist-009-inventaire-clinique.md) : 36 fichiers dont
  seize skills (quatorze invocables et deux alias dépréciés), modèles inline,
  bandes CA/IL, registres et dépendances de contenu ; décisions individuelles.
  Aucun agent ou cookbook propre livré.
- [Découpage CLN-001 à CLN-023](exist-009-annexes/exist-009-decoupage-clinique.md) : fichiers,
  résultats, entrées, recherches futures, exclusions et scénarios. Accueil,
  recherche, support d'analyse, mise en forme supervisée, dates, revue,
  journal et transmission ont des sorties distinctes.
- Chargement par code d'État, federal-always et copie IL audités : aucune
  bande américaine renommée France ; CLN-012 prévoit saisie incertaine sans
  calcul. Notification inconnue reste visible dans rapport/revue/transmission.
- Cadre réel et rôles à qualifier avant données réelles, pédagogie distincte
  de compétence et de validation, ABA non importé comme règle française.
  Modèle de file empaqueté en lecture seule, état utilisateur gardé et version
  de sortie revue à identifier. Conflits, données, urgences et relais explicités.
- [Relecture du cadrage](exist-009-annexes/exist-009-verification.md) : échéance saisie sans
  notification et accueil logement fictifs ; références attendues/non chargées
  et personnes chargées de vérifier/valider, sans exécution de skills.
- [Contrôles statiques et empreintes](exist-009-annexes/exist-009-resultats.json), rejouables
  avec le [contrôleur](exist-009-annexes/exist-009-controles.py). Clé HTML parasite du modèle
  deadlines, templates annoncés absents et clés pédagogiques divergentes
  constatés ; corrections assignées aux suites, non réalisées dans le plugin.
- PILOTE-003 terminé après BASE-011 : préalable satisfait, sans sélection
  d'extension ; limites H01 complet et lecteur indépendant consignées.
  Vingt-trois suites `proposee`, première tranche suggérée CLN-001.

Fichiers du lot : présente story, inventaire, découpage, vérification,
contrôleur, résultats JSON, vingt-trois propositions `suites/cln-*.md` et index
`backlog/README.md`. Modifications limitées à `backlog/`, sans entrée NOTICE
selon CLAUDE.md. Différences simultanées éventuelles ailleurs consignées sans
attribution ni modification par ce lot ; travaux antérieurs protégés.

**Portée :** cadrage et relecture par le seul agent de maintenance sur fixtures
fictives, contrôles statiques. Aucune source juridique externe consultée,
structure réelle juridiquement qualifiée, habilitation ou échéance réelle
validées. Aucune adaptation/exécution de skill, trace de chargement runtime,
installation, recette client, lecteur indépendant, donnée bénéficiaire,
connexion, notification, signature, dépôt, transmission, publication ou
déploiement. Plugin et contenus éditeur inchangés ; sources françaises,
versions, règles de structure, cadre professionnel/données et recettes restent
aux futures implémentations.

## Retrait du plugin — 16 octobre 2026

Le plugin `legal-clinic` a été retiré du marketplace et du dépôt sur décision
de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)).
Ce cadrage reste terminé et sert de trace ; ses vingt-trois suites CLN sont
`abandonnee`. Les liens du cadrage et de ses annexes vers `legal-clinic/`
désignent l'état du dépôt avant ce retrait (commit `e215a2b`).
