---
id: EXIST-010
titre: "Découper l'adaptation des méthodes et examens juridiques"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-010 — Découper l'adaptation des méthodes et examens juridiques

## Objectif

Adapter les tâches pédagogiques aux cursus et exercices français demandés.

## Points de départ

- [law-student/skills/irac-practice/SKILL.md](../../law-student/skills/irac-practice/SKILL.md)
- [law-student/skills/case-brief/SKILL.md](../../law-student/skills/case-brief/SKILL.md)
- [law-student/skills/bar-prep-questions/SKILL.md](../../law-student/skills/bar-prep-questions/SKILL.md)
- [law-student/skills/outline-builder/SKILL.md](../../law-student/skills/outline-builder/SKILL.md)
- [law-student/skills/exam-forecast/SKILL.md](../../law-student/skills/exam-forecast/SKILL.md)
- [law-student/CLAUDE.md](../../law-student/CLAUDE.md)

## Travail attendu

- Distinguer cas pratique, fiche/commentaire d'arrêt, dissertation, note de synthèse et préparation au CRFPA selon l'exercice réel.
- Définir l'évolution des noms IRAC et bar prep sans supposer une équivalence avec un examen américain ; prévoir la compatibilité des commandes seulement si utile.
- Conserver l'accompagnement pédagogique et les règles d'intégrité ; adapter critères et exercices à la consigne de l'établissement.
- Séparer méthode, plan de révision et actualisation du droit ; ne pas promettre une prédiction fiable des sujets d'examen.
- Sources à prévoir et à vérifier lors des futures implémentations : Consignes de cours et d'examen, décisions et textes français/UE ; sources officielles actuelles pour les épreuves et calendriers.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `law-student`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Comparer les consignes d'un cas pratique et d'un commentaire d'arrêt avec un extrait de décision française ; les attendus doivent différer.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-010-inventaire-formation.md) : 26 fichiers,
  treize skills et leurs dépendances de contenu/stockage ; décisions de
  conservation, réécriture, renommage visible et retrait justifiées par entrée.
  Aucun agent ou cookbook propre, pas d’état étudiant livré.
- [Découpage ETU-001 à ETU-021](exist-010-decoupage-formation.md) : vingt-et-une
  suites bornées avec fichiers, entrées, résultats, sources futures et scénarios.
  Méthode et retour sur brouillon distincts pour les exercices concernés ;
  cas pratique, fiche/commentaire, dissertation et synthèse non interchangeables.
- Noms IRAC/bar prep traités comme chemins hérités, pas équivalences françaises ;
  CRFPA qualifié par session/épreuve/consigne et sources officielles à vérifier.
  Aucun alias fictif, nouveau skill ou calendrier français livré dans ce lot.
- Intégrité et aide selon consigne, révisions et données séparées d’une
  actualisation ponctuelle du droit. Analyse descriptive d’annales sans
  promesse de prédiction, retrait des poids prévu aussi chez les consommateurs.
- [Relecture comparative](exist-010-verification.md) : consignes fictives
  de cas pratique et commentaire avec [extrait réel traçable](exist-010-support-verification.json)
  d’une décision française lu depuis une reproduction DILA locale de BASE-010.
  Attendus différents et limites d’extrait explicités, pas corrigé de fond.
- [Contrôles statiques et empreintes](exist-010-resultats.json), rejouables
  avec le [contrôleur](exist-010-controles.py) ; couverture et dépendances,
  liens, sources de contenu, copies partagées et protection des travaux antérieurs.
- PILOTE-003 terminé après BASE-011 : préalable satisfait, sans sélection
  d’extension ; limites H01 complet et lecteur indépendant consignées.
  Toutes les suites restent `proposee`, première tranche suggérée ETU-001.

Fichiers du lot : présente story, inventaire, découpage, vérification,
contrôleur, support et résultats JSON, vingt-et-une propositions `suites/etu-*.md`
et index `backlog/README.md`. Modifications limitées à `backlog/`, sans entrée
NOTICE selon CLAUDE.md. Différences simultanées éventuelles hors lot consignées
sans attribution ; plugin, contenus éditeur et travaux antérieurs préservés.

**Portée :** cadrage et relecture par le seul agent de maintenance ; pas
adaptation ou exécution de skill. Provenance et fidélité d’un extrait lues
localement, sans nouvelle recherche externe ni validation de portée/applicabilité
juridique ou de droit actuel. Pas de copie d’étudiant réelle corrigée, note,
prévision de sujet, règlement ou calendrier d’examen validés, permission d’aide
institutionnelle établie, donnée d’apprenant collectée, connexion, rappel,
installation, recette client, lecteur indépendant, publication ou déploiement.
Ces résultats distincts restent aux futures implémentations sélectionnées.
