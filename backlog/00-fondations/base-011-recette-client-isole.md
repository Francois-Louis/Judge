---
id: BASE-011
titre: "Exécuter la recette des paquets dans un client Claude isolé"
statut: proposee
priorite: P0
nature: validation
dependances: [BASE-006, BASE-008, BASE-012]
---

# BASE-011 — Exécuter la recette des paquets dans un client Claude isolé

## Objectif

Un même client jetable et authentifié exécute les recettes en attente de
BASE-008 et PILOTE-002 à PILOTE-004. Décision de l'utilisateur du 16 octobre
2026, prise après la [rétrospective du pilote](../01-pilote-travail/retrospective-pilote-travail.md)
(écart 1). Les stories concernées gardent leurs propres critères ; celle-ci
fournit l'environnement, les journaux et les observations.

## Périmètre

- Client : binaire `claude` embarqué par l'application desktop ou installation
  officielle, version consignée. L'utilisateur s'authentifie lui-même ; aucun
  identifiant ne transite par l'agent.
- Isolation : `CLAUDE_CONFIG_DIR`, `HOME` et `USERPROFILE` jetables (les chemins
  de profil suivent le home, pas `CLAUDE_CONFIG_DIR`), projet vide, marketplace
  locale jetable ne contenant que le paquet testé. Choisir et consigner le
  niveau atteint : compte Windows séparé (checkout et vrai profil illisibles) ou
  variables jetables seules (checkout encore lisible).
- Entrées : paquet identifié par son inventaire et ses empreintes, pièces
  fictives H01–H16, aucun connecteur ni jeton hérité.
- Lecteur : l'utilisateur, sans formation juridique déclarée. Ses
  reformulations sont recopiées telles quelles et marquées **participant non
  indépendant** (porteur du projet).

## Travail attendu

1. Préparer l'environnement et l'inventaire du paquet. Vérifier avant toute
   commande que le profil, les caches et les plugins d'origine sont absents.
2. Installer le seul plugin, consigner commande, chemin installé et liste des
   plugins chargés. Rejouer `check-plugin-package.py --schema --claude` sur le
   chemin installé.
3. BASE-008 : rejouer la recette authentifiée prévue par sa story.
4. PILOTE-003 : un scénario sans profil (H12) et un sans source (H11a puis H11b).
5. PILOTE-002 : scénarios prêts (H02–H16) ; H01 seulement si D02 est corrigé.
6. PILOTE-004 : étapes 1 à 4 de sa [recette](../01-pilote-travail/pilote-004-verification.md).
7. Faire reformuler les sorties par l'utilisateur sans aide (engagement,
   question, destinataire, réserve ; préférence mémorisée et emplacement).
8. Mettre à jour chaque story selon les résultats observés, sans clore une
   story dont un scénario a échoué ou n'a pas été exécuté.

## Critères d'acceptation

- [ ] Le niveau d'isolation atteint et ses limites sont consignés avant tout scénario.
- [ ] Le plugin est installé seul ; version du client, commande et plugins chargés sont journalisés.
- [ ] Chaque scénario exécuté conserve outils appelés, ressources lues, sorties et erreurs.
- [ ] Les reformulations de l'utilisateur sont recopiées et marquées non indépendantes.
- [ ] Le statut de BASE-008 et PILOTE-002 à 004 reflète les résultats observés.

## Vérification

La recette elle-même est la vérification : le dernier critère reste non coché
tant que les scénarios ne sont pas exécutés et rapportés.

## Hors périmètre

Liens symboliques réels de BASE-008 (privilège Windows), correction D02 du
nominal, lecteur indépendant, publication ou installation sur le compte réel.
