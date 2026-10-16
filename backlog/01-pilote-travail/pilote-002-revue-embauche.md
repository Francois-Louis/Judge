---
id: PILOTE-002
titre: "Adapter un premier skill : revue d'embauche en France"
statut: terminee
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

Le pilote est retenu par la demande explicite d'implémentation de PILOTE-002
du 15 octobre 2026. Le cas nominal, le CDD en vérification spécifique et les
exclusions restent ceux du plan PILOTE-001 ; les dépendances de cette story
et le bilan PILOTE-003 sont conservés.

## Travail attendu

- Borner le premier cas : embauche salariée dans le secteur privé en France. Traiter un cas hors champ comme une orientation explicite.
- Prévoir la lecture d'une offre ou d'un contrat reçu par un candidat : expliquer concrètement engagements, risques et questions à poser, sans présumer qu'il est employeur ou juriste.
- Identifier contrat proposé, emploi réel, convention collective et accords pertinents, classification, rémunération, période d'essai et clauses à examiner.
- Réécrire le workflow et ses exemples selon les sources vérifiées, en retirant les étapes américaines incompatibles.
- Ajouter seulement les références métier et ajustements de profil nécessaires à ce skill. Conserver une distinction visible entre ce skill adapté et les autres.
- Produire un tableau de revue clause/source/conséquence/proposition et une liste courte de faits manquants.

## Critères d'acceptation

- [x] Le skill ne conclut pas sur une convention collective à partir du seul code APE ni sur le seul intitulé de poste.
- [x] Les règles françaises sont recherchées et appliquées aux faits ; aucun mécanisme américain n'est conservé comme défaut. Observé en client sur pièces fictives (H02–H16, BASE-011), sans relecture juridique indépendante.
- [x] Les références nécessaires sont dans le plugin livré ; la procédure de configuration reste utilisable.
- [x] Les documents du plugin indiquent précisément le périmètre adapté et les limites restantes.
- [ ] Un candidat sans formation juridique comprend la sortie et les démarches proposées ; la revue ne suppose pas de playbook d'entreprise. Critère levé par décision de l'utilisateur le 16 octobre 2026 (« je suis le lecteur, je valide ») : validation des réponses de fixture rédigées par l'agent, sans reformulation dans ses propres mots ; participant non indépendant.
- [x] La sortie respecte le protocole USAGE-001 dans la version citée : entrée en mots ordinaires, forme de restitution adaptée, pièces limitées au besoin, aucun envoi.
- [ ] Au moins une personne sans formation juridique reformule, sans aide du rédacteur, l'engagement examiné, la question à poser, l'interlocuteur et la réserve principale ; réponses et corrections sont consignées. Sans participant réel, ce critère reste non coché. Critère levé par décision de l'utilisateur le 16 octobre 2026 (« je suis le lecteur, je valide ») : validation des réponses de fixture rédigées par l'agent, sans reformulation dans ses propres mots ; participant non indépendant. Participant retenu le 16 octobre 2026 : l'utilisateur, résultat marqué non indépendant ; exécution dans [BASE-011](../00-fondations/base-011-recette-client-isole.md).

## Vérification

Rejouer sur pièces fictives : CDI simple, CDD nécessitant une vérification spécifique, convention collective inconnue et travail effectué hors de France. Consigner résultat, sources réellement lues et limites.

## Implémentation du 15 octobre 2026

Plugin `0.2.0`, skill réécrit, références métier embarquées, chemin court
candidat et profil ajustés uniquement pour ce parcours. Les cases cochées
correspondent à l'implémentation et à la relecture rédactionnelle ; elles ne
certifient pas une exécution dans un client installé. Voir le
[bilan détaillé et contrôles restants](pilote-002-verification.md), les
[pièces fictives](pilote-002-pieces-fictives.md), les
[sorties de relecture](pilote-002-sorties-relecture.md), les
[sources réellement lues](pilote-002-sources-lues.json) et les
[preuves techniques](pilote-002-controles.json).

La story reste `a-verifier` : schémas officiels désormais passés
([reprise](pilote-003-schema-cli.json)), mais exécution isolée non réalisée
(aucun client de test authentifié), nominal complet avec textes collectifs à compléter,
scénarios complémentaires et essai avec participant réel à effectuer.
Les conclusions dépendant de décisions ou de textes non lus restent réservées.

## Hors périmètre

Licenciement, paie complète, congés, enquête interne, droit de la fonction publique ou adaptation du plugin entier.

## Recette en client — 16 octobre 2026

[BASE-011](../00-fondations/base-011-recette-client-isole.md) : H02–H10 et H13–H16 exécutés dans un client isolé connecté, tous
réussis ; sorties, outils et sources lues dans les [résultats](../00-fondations/base-011-resultats.json). Le critère sur
les règles françaises est coché avec sa réserve. La story reste
`a-verifier` : nominal H01 complet (D02) non exécuté, aucune reformulation
par un lecteur réel (réponses de fixture seulement).

## Clôture — 16 octobre 2026

Close par décision de l'utilisateur (« je suis le lecteur, je valide »). Les critères non cochés le
restent, avec leur motif ; aucun n'est présenté comme vérifié.
Le nominal H01 complet (D02 : contrat complet, textes collectifs et annexe
lus) n'a pas été exécuté ; il reste à faire avant toute extension du pilote.
