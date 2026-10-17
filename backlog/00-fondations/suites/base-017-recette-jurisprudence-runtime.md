---
id: BASE-017
titre: "Recetter la recherche de jurisprudence d'un skill dans un client isolé"
statut: proposee
priorite: P1
nature: validation
dependances: [BASE-016, BASE-011, TRAV-062]
---

# BASE-017 — Recetter la recherche de jurisprudence d'un skill dans un client isolé

## Objectif

Observer, sur un skill installé seul, que la conduite de la section 10 de la
méthode `1.2.0` est suivie pendant une vraie réponse. Issue du cadrage
[BASE-015](../base-015-jurisprudence-runtime.md), qui n'a testé les voies que
depuis la session de maintenance.

## Périmètre

- Client et isolation de [BASE-011](../base-011-recette-client-isole.md) ;
  paquet `employment-legal` portant la méthode `1.2.0` et la référence
  corrigée par TRAV-062.
- Skill `hiring-review` sur un contrat fictif avec clause de non-concurrence.

## Travail attendu

Scénarios, chacun journalisé (outils, adresses, refus, sortie) :

1. **Normal** : outil web autorisé ; la sortie cite une décision de la Cour de
   cassation lue sur Légifrance, avec fiche et passage des motifs.
2. **Recherche vide** : question sans jurisprudence diffusée (par exemple une
   clause inhabituelle) ; réponse réservée, recherche décrite, voie indiquée.
3. **Doctrine seule** : décision de cour d'appel connue par un commentaire ;
   citée comme doctrine, décision non lue.
4. **Légifrance refusé** (permission refusée) : repli tracé, aucune solution
   jugée restituée de mémoire.
5. **Sans outil web** : seules les décisions de la référence embarquée, avec
   leur date de relecture ; à comparer avec l'écart H11b de BASE-011.

## Critères d'acceptation

- [ ] Les cinq scénarios sont exécutés et journalisés dans le client isolé.
- [ ] Aucune sortie ne présente une décision non ouverte comme lue.
- [ ] Les écarts observés sont rapportés aux stories concernées sans être corrigés dans cette story.

## Vérification

La recette elle-même ; le critère 1 reste non coché tant qu'elle n'est pas exécutée.

## Hors périmètre

Évaluation de la justesse juridique des solutions, autres plugins, lecteur indépendant.
