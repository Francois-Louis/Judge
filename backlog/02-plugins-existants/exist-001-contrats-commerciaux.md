---
id: EXIST-001
titre: "Découper l'adaptation des contrats commerciaux"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-001 — Découper l'adaptation des contrats commerciaux

## Objectif

Conserver les workflows de revue, négociation et suivi en les replaçant dans les contrats français B2B et leur éventuelle dimension européenne.

## Points de départ

- [commercial-legal/skills/review/SKILL.md](../../commercial-legal/skills/review/SKILL.md)
- [commercial-legal/skills/vendor-agreement-review/SKILL.md](../../commercial-legal/skills/vendor-agreement-review/SKILL.md)
- [commercial-legal/skills/nda-review/SKILL.md](../../commercial-legal/skills/nda-review/SKILL.md)
- [commercial-legal/skills/saas-msa-review/SKILL.md](../../commercial-legal/skills/saas-msa-review/SKILL.md)
- [commercial-legal/skills/renewal-tracker/SKILL.md](../../commercial-legal/skills/renewal-tracker/SKILL.md)

## Travail attendu

- Séparer revue de contrat, confidentialité, SaaS, avenants et échéances de renouvellement ; proposer une story par tâche.
- Identifier les points à revoir : responsabilité, résiliation, cession, preuve, imprévision, clauses déséquilibrées, données et sous-traitance selon l'objet.
- Distinguer B2B et consommation ; orienter les demandes de consommateurs vers leur futur plugin sans dupliquer toute la matière.
- Prévoir aussi le point de vue des indépendants, artisans et TPE : facture client impayée, contrat de prestation, frais ou pénalités contestés, rupture de relation. Ne pas limiter les sorties aux juristes d'une grande entreprise.
- Sources à prévoir et à vérifier lors des futures implémentations : Code civil, Code de commerce, droit UE pertinent et clauses effectivement fournies ; ne pas transformer un playbook commercial en règle de droit.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `commercial-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer le découpage sur un contrat fournisseur français et un SaaS transfrontalier ; distinguer les hypothèses de droit applicable des préférences de négociation.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

