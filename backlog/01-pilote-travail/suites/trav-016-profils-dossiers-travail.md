---
id: TRAV-016
titre: "Compléter les profils et dossiers des parcours travail adaptés"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-016 — Compléter les profils et dossiers des parcours travail adaptés

## Objectif

Après le pilote, un salarié, employeur ou praticien veut modifier son contexte ou séparer ses dossiers sans réintroduire les anciens défauts.

Résultat : Configuration compatible conservant les réponses et dossiers isolés ; disponibilité des parcours explicite.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : cold-start-interview ; customize ; matter-workspace ; CLAUDE.md.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Profil existant/absent, rôle réel, dossiers et habilitations, périmètres réellement adaptés.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Revoir états US/at-will/exempt/privilege, quick start et modèles MSA/LoL ; distinguer entreprise publique et statut du contrat ; isoler dossiers salariés/enquêtes même en interne, sans toucher les autres distributions.

Sources primaires à rechercher : Méthode BASE-005, règles de confidentialité et protection des données à rechercher selon l'usage ; un profil ne prouve aucune règle sectorielle.
Ces pistes sont **non vérifiées pour cette story**. Lire les dispositions,
versions et transitions applicables lors de l'implémentation ; conserver
le relevé des accès et réserves BASE-005. Utiliser les voies officielles
alternatives de BASE-010 si une page web échoue, sans confondre lecture et validation.

Charger la méthode locale versionnée et embarquer les références utiles.
Conserver la frontière de stockage BASE-008 ; nommer les accès externes
nécessaires/optionnels et prévoir la sortie utile si la recherche reste empêchée.

## Critères d'acceptation

- [ ] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous.
- [ ] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie.
- [ ] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement.
- [ ] Sources et données sont traçables ; le paquet isolé ne requiert aucun fichier voisin du dépôt.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche.
- [ ] Le périmètre adapté et le reste non adapté sont explicitement distingués.

## Vérification

- Cas normal : Profil candidat issu du pilote : modifier un fait sans effacer les autres réponses.
- Limite : Ancien profil US, pause ou dossier d'un autre salarié : conserver l'historique, inconnues explicites et refus des lectures non autorisées.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Migration automatique depuis une autre distribution, adaptation juridique des commandes restantes et politique complète de conservation.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
