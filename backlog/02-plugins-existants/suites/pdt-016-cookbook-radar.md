---
id: PDT-016
titre: "Adapter la variante headless du radar de lancements"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-015]
---

# PDT-016 — Adapter la variante headless du radar de lancements

## Objectif et résultat attendu

Un cookbook contrôlable produit le même rapport de routage borné depuis fixtures françaises, dans une racine de déploiement isolée, sans se présenter comme service actif.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `managed-agent-cookbooks/launch-radar/agent.yaml`
- `managed-agent-cookbooks/launch-radar/subagents/tracker-reader.yaml`
- `managed-agent-cookbooks/launch-radar/subagents/risk-classifier.yaml`
- `managed-agent-cookbooks/launch-radar/subagents/memo-writer.yaml`
- `managed-agent-cookbooks/launch-radar/steering-examples.json`
- `managed-agent-cookbooks/launch-radar/README.md`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Contrat radar PDT-015, manifestes et schémas, configuration effective de déploiement, horizon et export/fixtures de tracker ; capacités MCP réelles à constater séparément des déclarations.

## Travail attendu

Conserver orchestrateur local et Write dans la feuille prévue. Corriger documentation des droits, profil modèle/effectif, horizon/cadence et racine BASE-008. Porter couverture/pagination/erreurs et troncature 200 dans un contrat vérifiable ; titres français acceptés, dates réelles validées, domaines sans perte silencieuse. Les champs conformes au schéma restent données non fiables. Préserver protections de rendu et URL inerte, résoudre contradiction liens, handoff_request absent du schéma et accès helper sans outil d'exécution. Conserver diff sur même périmètre et signaler changement de fenêtre plutôt que disparition résolue. Aucun appel automatique de revue amont ni extension transverse des permissions sans lot motivé.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Lire contrats de managed-agent-cookbooks/README.md, scripts de lancement, validation, lint et orchestrate.py avant de fixer les changements. Sources légales restent celles des tranches manuelles si invoquées ; le radar n'est pas un moteur juridique. Un succès de schéma n'établit pas confinement ni connexion réelle.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Fixtures françaises nominales, accents, date invalide, 201 tickets, domaine multiple et accès incomplet donnent rapport et couverture honnêtes.
- [ ] Orchestrateur et classificateur n'acquièrent ni réseau ni Write par dérive ; les toolsets des lecteurs sont examinés contre les capacités réelles.
- [ ] Rendu d'un texte injecté ou URL hostile, re-scan de périmètre différent et handoff ne déclenchent aucune action externe.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : R03 — Fixtures de six lancements français : dry-run/lint valides, sorties isolées et orientations cohérentes avec PDT-015.
- Cas limite : R04 — 201 tickets, accents, date impossible, instruction injectée et champ handoff : contrôle explicite sans abandon silencieux ni exécution du handoff.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-annexes/exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Déploiement distant, accès aux comptes réels, configuration de scheduler, nouvelle infrastructure transverse et publication d'un rapport.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
