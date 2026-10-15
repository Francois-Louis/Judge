---
id: EXIST-007
titre: "Découper l'adaptation de la veille réglementaire"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-007 — Découper l'adaptation de la veille réglementaire

## Objectif

Remplacer le centrage sur les autorités américaines par des sources et événements normatifs français et européens.

## Points de départ

- [regulatory-legal/skills/reg-feed-watcher/SKILL.md](../../regulatory-legal/skills/reg-feed-watcher/SKILL.md)
- [regulatory-legal/skills/reg-feed-watcher/references/source-catalog.md](../../regulatory-legal/skills/reg-feed-watcher/references/source-catalog.md)
- [regulatory-legal/skills/policy-diff/SKILL.md](../../regulatory-legal/skills/policy-diff/SKILL.md)
- [regulatory-legal/skills/policy-redraft/SKILL.md](../../regulatory-legal/skills/policy-redraft/SKILL.md)
- [regulatory-legal/agents/reg-change-monitor.md](../../regulatory-legal/agents/reg-change-monitor.md)

## Travail attendu

- Inventorier les sources, formats, authentifications et capacités réellement disponibles ; une URL de page ne vaut pas flux RSS fonctionnel.
- Séparer collecte, qualification d'un texte, analyse d'écart, rédaction de politique et réponse à une consultation.
- Définir le suivi publication/entrée en vigueur/application/transposition et la preuve d'une modification ; préserver les sources et versions antérieures.
- Traiter les cookbooks automatisés dans une story distincte après adaptation des tâches manuelles.
- Sources à prévoir et à vérifier lors des futures implémentations : Légifrance/JORF, EUR-Lex/JOUE et autorités françaises ou européennes choisies selon le secteur ; disponibilité technique à vérifier.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `regulatory-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer une publication au JORF, une directive à transposer et une consultation d'autorité ; elles doivent produire des événements distincts.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

