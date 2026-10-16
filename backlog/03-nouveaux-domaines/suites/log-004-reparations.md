---
id: LOG-004
titre: "Préparer une demande de réparation au bailleur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-004 — Préparer une demande de réparation au bailleur

## Objectif et résultat attendu

Pour une réparation identifiée, le locataire d'un logement privé vide,
résidence principale en France métropolitaine, prépare une demande au
bailleur en distinguant entretien, vétusté et cause inconnue.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/rental-repair-request/SKILL.md` — tâche (à créer)
- `housing-legal/references/reparations-locatives.md` — répartition et sources (à créer)
- `housing-legal/skills/rental-repair-request/references/demande-intervention.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale de LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Bail, désordre et date de constat, état des lieux et inventaire utile,
photos ciblées, entretien connu, diagnostic/devis éventuel et échanges.
Identifier qui a commandé les travaux et à qui la personne souhaite écrire.
Ne pas demander les images d'autres habitants ni un dossier technique entier.

## Sortie attendue

Faits prouvés/déclarés ; hypothèses d'entretien, vétusté ou autre cause à
vérifier ; pièces manquantes ; brouillon d'intervention au bailleur avec
demande de réponse et constat technique ; interlocuteur et limites.

## Travail attendu

Ne pas diagnostiquer depuis une photo ni attribuer automatiquement le coût.
Obligation du bailleur envers l'occupant ici ; recours contre le plombier
ou l'entreprise → DOM-015 sur devis/commande/réception distincts. Danger
immédiat allégué : priorité à la mise en sécurité et à un professionnel
approprié, sans conseil technique dangereux. Décence → LOG-005 ; assurance
→ DOM-005. Aucun arrêt de paiement ou travaux aux frais du bailleur promis.

## Références métier et sources à rechercher

Loi du 6 juillet 1989, Code civil, décret n° 87-712, vétusté, état des lieux
et preuve de la cause ; clauses applicables et ANIL/ADIL. Ouvrir versions,
champ et exceptions, sans présumer que la liste suffit à établir la cause.

## Critères d'acceptation

- [ ] R01 prépare une demande au bailleur sans trancher la cause technique.
- [ ] R02 sépare le contrat de travaux et l'obligation locative ; danger traité avant la revue ordinaire.
- [ ] Sans source, faits et questions seulement pour les obligations ; paquet seul et références locales vérifiés selon BASE-006.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si délai, acte ou enjeu irréversible (BASE-013).

## Vérification

- Cas normal : R01 — Chauffage en panne, entretien documenté, cause non diagnostiquée ; demande d'intervention sans coût imputé.
- Cas limite : R02 — Bailleur et entreprise se renvoient une fuite après travaux ; deux questions et interlocuteurs, sans responsabilité tranchée.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Autres régimes locatifs, expertise technique, recours travaux, indemnisation,
réduction de loyer décidée, saisine et envoi.
