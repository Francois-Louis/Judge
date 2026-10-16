---
id: TRAV-004
titre: "Lire les pièces d'un licenciement individuel pour motif personnel"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-004 — Lire les pièces d'un licenciement individuel pour motif personnel

## Objectif

Un salarié privé reçoit une convocation ou lettre et veut comprendre le motif annoncé et les pièces utiles.

Résultat : Chronologie, points de procédure/motif à vérifier, pièces et interlocuteurs, sans décision de validité ni échéance certaine non établie.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : termination-review.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Actes complets, preuves des dates, contrat, ancienneté déclarée, statut protecteur éventuel, accords et chronologie.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Remplacer go/no-go employeur, WARN, COBRA, OWBPA et release par qualification du mode, protections et procédure propre ; supprimer le renvoi FLSA.

Sources primaires à rechercher : Code du travail, textes conventionnels et jurisprudence officielle du motif/procédure choisi ; règles de computation si un délai est abordé.
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

- Cas normal : Lettre et convocation datées : distinguer griefs déclarés et preuves.
- Limite : Salarié protégé ou notification sans preuve : orientation ciblée et urgence potentielle, pas de délai par défaut.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Licenciement économique, inaptitude, rupture conventionnelle, décision disciplinaire et chiffrage exhaustif.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.

## Complément des frictions travail — 16 octobre 2026

**Notification, assistance et motifs.** Points 3.12, 9.08 et 10.08–12 : conserver annonce orale, présentation/remise de convocation, entretien, assistance, lettre, précision des motifs et réception. Distinguer insuffisance et faute, qualification grave et préavis ; aucune règle de trois avertissements. Cas ajouté : annonce orale suivie d’une lettre imprécise, dates de présentation et réception divergentes : contradiction conservée et demande de précision à examiner en urgence. TRAV-044 garde sanctions hors licenciement ; TRAV-046 la rupture protégée et ses actes administratifs ; TRAV-051 les sommes. Pas de calcul global d’indemnisation ni de verdict de validité.

Rattachement complet : [matrice des frictions](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md).
Les critères restent non cochés. Pour ces ajouts, appliquer BASE-013 : phrase
finale nommant le professionnel compétent et renfort en tête si urgence ou
procédure ; sources, paquet détaché, client et compréhension à vérifier selon
BASE-005/006. Portée de l’intégration et lectures préliminaires :
[vérification](../pilote-001-annexes/pilote-001-frictions-verification.md).
