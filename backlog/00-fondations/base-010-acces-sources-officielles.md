---
id: BASE-010
titre: "Rétablir la lecture des sources officielles sans souscription API"
statut: terminee
priorite: P0
nature: implementation
dependances: [BASE-005]
---

# BASE-010 — Rétablir la lecture des sources officielles sans souscription API

## Objectif

Poursuivre une recherche lorsque l'outil web rencontre un refus Légifrance
ou une page JavaScript EUR-Lex, avec une publication officielle alternative
et une preuve de lecture technique reproductible. Ajout demandé explicitement
par l'utilisateur pendant PILOTE-001.

## Périmètre

Outil de maintenance `scripts/legal_sources.py`, tests, procédure
`references/legal-source-access.md` et consignes du dépôt. Articles du Code du
travail via CDTN, documents français XHTML via CELEX/CELLAR, listes d'archives
et lecture XML ciblée dans les fonds DILA LEGI/KALI/CASS sans compte API.
Client PISTE facultatif, sans accès authentifié validé.

## Critères d'acceptation

- [x] Deux échecs réels aboutissent à un texte officiel lisible par une autre voie.
- [x] URL, erreurs, dates et empreintes sont conservées sans valider l'applicabilité.
- [x] Page de blocage, corps vide, mauvais article et métadonnées RDF ne sont pas des succès.
- [x] Aucun CAPTCHA résolu ; aucune clé stockée dans le dépôt.
- [x] Des XML LEGI/KALI/CASS sont récupérés sans souscription API.
- [x] La procédure distingue routes publiques opérationnelles et PISTE indisponible pour l'utilisateur.

## Vérification et bilan — 15 octobre 2026

[Procédure et limites](../../references/legal-source-access.md),
[résultats réseau](base-010-annexes/base-010-resultats-acces.json).
21 tests hors ligne réussis ; L2261-2, Rome I et trois documents XML DILA
obtenus en réseau par le script, avec trois listes d'archives.
Commandes CLI publiques rejouées avec sortie `0` ; argument d'article invalide
refusé avec sortie `2`. Syntaxe Python, JSON et `git diff --check` contrôlés.
PISTE : absence d'identifiants testée ; authentification et réponses réelles
non exécutées. L'utilisateur a créé un compte et une application mais signale
ne pas avoir le droit de souscrire à l'API ; aucune dépendance à cet accès.
Les consignes de maintenance imposent d'essayer la voie officielle appropriée
avant de conclure à une recherche empêchée. BASE-005 et ses copies `1.0.0`
restent identiques ; leur méthode permet déjà d'autres publications officielles.

## Hors périmètre

Disponibilité garantie de tous les éditeurs, toutes les API, corpus exhaustif,
résolution des droits PISTE, indexation complète des stocks DILA,
recherche historique automatique, validation juridique,
réécriture des skills hérités. Le script est un outil de maintenance du dépôt ;
son éventuel embarquement sera traité et vérifié dans le lot du plugin concerné.
