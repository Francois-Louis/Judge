---
id: PILOTE-002
titre: "Adapter un premier skill : revue d'embauche en France"
statut: proposee
priorite: P1
nature: implementation
dependances: [PILOTE-001, BASE-004, BASE-006, USAGE-002]
---

# PILOTE-002 — Adapter un premier skill : revue d'embauche en France

## Objectif

Livrer une première adaptation verticale et relisible de `employment-legal:hiring-review`.

## Points de départ

- [Inventaire et dépendances PILOTE-001](pilote-001-releve-inventaire.md).
- [Sections à reprendre et scénarios de contrôle](pilote-001-plan-hiring-review.md).
- [Comparaison USAGE-002 et premier lot proposé](../05-usages-quotidiens/usage-002-comparaison-priorites.md).
- [Protocole d'orientation USAGE-001, version 1.0.0](../05-usages-quotidiens/usage-001-protocole-orientation.md) : formes de restitution, pièces limitées, absence d'envoi sans autorisation.
- [employment-legal/skills/hiring-review/SKILL.md](../../employment-legal/skills/hiring-review/SKILL.md)
- [employment-legal/CLAUDE.md](../../employment-legal/CLAUDE.md)
- [employment-legal/README.md](../../employment-legal/README.md)
- [employment-legal/.claude-plugin/plugin.json](../../employment-legal/.claude-plugin/plugin.json)

USAGE-002 propose de conserver ce pilote ; son choix reste à arrêter. Ce
classement n'engage pas l'implémentation. Le cas nominal, le CDD en vérification
spécifique et les exclusions restent ceux du plan PILOTE-001 ; les dépendances
de cette story et le bilan PILOTE-003 sont conservés.

## Travail attendu

- Borner le premier cas : embauche salariée dans le secteur privé en France. Traiter un cas hors champ comme une orientation explicite.
- Prévoir la lecture d'une offre ou d'un contrat reçu par un candidat : expliquer concrètement engagements, risques et questions à poser, sans présumer qu'il est employeur ou juriste.
- Identifier contrat proposé, emploi réel, convention collective et accords pertinents, classification, rémunération, période d'essai et clauses à examiner.
- Réécrire le workflow et ses exemples selon les sources vérifiées, en retirant les étapes américaines incompatibles.
- Ajouter seulement les références métier et ajustements de profil nécessaires à ce skill. Conserver une distinction visible entre ce skill adapté et les autres.
- Produire un tableau de revue clause/source/conséquence/proposition et une liste courte de faits manquants.

## Critères d'acceptation

- [ ] Le skill ne conclut pas sur une convention collective à partir du seul code APE ni sur le seul intitulé de poste.
- [ ] Les règles françaises sont recherchées et appliquées aux faits ; aucun mécanisme américain n'est conservé comme défaut.
- [ ] Les références nécessaires sont dans le plugin livré ; la procédure de configuration reste utilisable.
- [ ] Les documents du plugin indiquent précisément le périmètre adapté et les limites restantes.
- [ ] Un candidat sans formation juridique comprend la sortie et les démarches proposées ; la revue ne suppose pas de playbook d'entreprise.
- [ ] La sortie respecte le protocole USAGE-001 dans la version citée : entrée en mots ordinaires, forme de restitution adaptée, pièces limitées au besoin, aucun envoi.
- [ ] Au moins une personne sans formation juridique reformule, sans aide du rédacteur, l'engagement examiné, la question à poser, l'interlocuteur et la réserve principale ; réponses et corrections sont consignées. Sans participant réel, ce critère reste non coché.

## Vérification

Rejouer sur pièces fictives : CDI simple, CDD nécessitant une vérification spécifique, convention collective inconnue et travail effectué hors de France. Consigner résultat, sources réellement lues et limites.

## Hors périmètre

Licenciement, paie complète, congés, enquête interne, droit de la fonction publique ou adaptation du plugin entier.
