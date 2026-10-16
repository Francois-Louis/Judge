---
id: ETU-001
titre: "Qualifier la consigne et le cadre d’un exercice"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006]
---

# ETU-001 — Qualifier la consigne et le cadre d’un exercice

## Objectif et résultat attendu

Une fiche de contexte distingue exercice, entraînement ou travail évalué, corpus, date de référence et aide autorisée avant de choisir une tâche.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/irac-practice/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/case-brief/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/legal-writing/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/bar-prep-questions/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/session/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/CLAUDE.md` : adaptation ciblée à cette tâche.
- `law-student/references/exercise-context.md` : à créer, propriétaire ETU-001.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Consigne exacte, cursus/matière, documents disponibles, travail de l’apprenant et règles de l’établissement relatives aux aides. Les informations déjà fournies sont réutilisées avec leur provenance.

## Travail attendu

- Séparer cas pratique, fiche d’arrêt, commentaire, dissertation, note de synthèse, oral et révisions ; CRFPA est un contexte d’examen à préciser, pas une méthode de réponse universelle.
- Demander seulement ce qui change l’aide possible ; si consigne inconnue, proposer une méthode générale limitée et ne pas attribuer de règles à l’établissement.
- Respecter les restrictions d’aide sur les travaux évalués ; ne pas produire un devoir à remettre ou camoufler l’usage de l’outil. Une préférence pédagogique ne lève pas ces contraintes.
- Charger isolation et méthode locales ainsi que le contexte dans chaque entrée adaptée ; ne pas compter sur le seul profil, qui est un modèle de configuration.

## Sources à rechercher lors de l'implémentation

Consignes et politique d’aide effectivement fournies par l’établissement ; méthode BASE-005, sans inventer une règle nationale uniforme.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] La sortie indique explicitement l’exercice et les inconnues, sans déduire un examen français de JD/1L/UBE.
- [ ] Une demande de devoir interdit conserve une aide méthodologique autorisée ou un exercice fictif distinct, sans réponse au sujet évalué.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : Q01 — Consigne de cas pratique, entraînement autorisé et brouillon : branche cas pratique, question guidée et critères de la consigne.
- Cas limite : Q02 — « Fais mon commentaire, IA interdite » : aucune rédaction substitutive ; expliquer la limite issue de la consigne, proposer une méthode ou un autre exercice.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

