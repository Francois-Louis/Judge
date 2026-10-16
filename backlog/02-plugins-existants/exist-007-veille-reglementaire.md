---
id: EXIST-007
titre: "Découper l'adaptation de la veille réglementaire"
statut: terminee
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

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `regulatory-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire sur fixtures fictives par le rédacteur).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer une publication au JORF, une directive à transposer et une consultation d'autorité ; elles doivent produire des événements distincts.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-007-inventaire-veille.md) : 26 fichiers dont neuf
  skills (huit invocables et une référence), modèles inline, catalogues,
  trackers, agent, profils et dépendances ; six fichiers du cookbook associé.
  Chaque tâche/fichier reçoit une décision motivée.
- [Sources et sondages](exist-007-sources.json) : 59 lignes héritées avec URL,
  format, authentification et capacités déclarés, dont dix rappels de sources
  sans flux. Sept sondages publics horodatés : RSS CNIL parsés, répertoire
  JORF DILA et page EDPB HTML, trois réponses EUR-Lex 202 vides. Documentation
  officielle EUR-Lex lue via contenu indexé, ouvertures directes web avec
  challenge ; aucun accès authentifié configuré ou testé.
- [Découpage VEI-001 à VEI-020](exist-007-decoupage-veille.md) : collecte,
  qualification, versions, temporalité/transposition, champ, écart, rédaction
  et consultation séparés. Conservation des versions et preuves de changement,
  dates par événement/disposition. Première tranche proposée VEI-001 sur texte
  fourni ; agent et cookbook distinct VEI-020 attendent les tâches manuelles.
- [Relecture du cadrage](exist-007-verification.md) : publication JORF,
  directive à transposer et consultation d'autorité fictives produisent des
  événements attendus distincts ; aucune obligation réelle ou date validée.
- [Contrôles statiques et empreintes](exist-007-resultats.json), rejouables
  avec le [contrôleur](exist-007-controles.py) ; sondages rejouables avec
  [leur script](exist-007-sondages.py). Le modèle comment-tracker charge une
  clé HTML parasite et un exemple actif : correction assignée à VEI-014.
- PILOTE-003 terminé après BASE-011 : préalable satisfait, sans sélection
  d'extension ; limites H01 complet et lecteur indépendant consignées.
  Les vingt suites restent `proposee`.

Fichiers du lot : présente story, inventaire, découpage, vérification,
sources JSON/script de sondage, résultats JSON/contrôleur, vingt propositions
`suites/vei-*.md` et index `backlog/README.md`. Lot limité à `backlog/`, sans
entrée NOTICE selon CLAUDE.md. Travaux antérieurs comparés à l'instantané ;
différences simultanées éventuelles ailleurs rapportées sans attribution.

**Portée :** cadrage et relecture par le seul agent de maintenance sur fixtures
fictives, contrôles statiques et sondages techniques publics bornés. Aucune
lecture normative de scénario, obligation, applicabilité ou échéance réelle
validée ; aucune adaptation/exécution de skill, installation, recette client,
lecteur indépendant, connexion authentifiée, abonnement, envoi, dépôt,
publication, programmation ou déploiement. Plugin, cookbook et contenus
éditeur inchangés. Disponibilité observée ponctuelle, sans garantie future
ou couverture exhaustive ; recherches juridiques et recette restent aux suites.

