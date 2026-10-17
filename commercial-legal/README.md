<!-- Modified by Judge FR/UE for COM-001, 2026-10-16, and BASE-013, 2026-10-17. -->

# Contrats commerciaux — Judge FR/UE 0.2.1

`review` qualifie une demande sur un contrat ou un récit en France/UE et
prépare la suite : domaine principal, rôle achat/vente, tâche visée, pièces
utiles et questions décisives. **COM-001 adapte cette orientation seulement.**
Les revues juridiques complètes, agents et registres hérités restent non adaptés.
La validation en client et avec un lecteur réel est documentée séparément dans
le bilan de la story ; une validation de structure ne prouve pas leur exécution.

## Commencer sans profil

```text
/judge-fr-eu-commercial-legal:review contrat.pdf
```

Ou raconter la situation : « Je suis artisan et j'achète une prestation de
maintenance pour mon activité ; que faut-il vérifier ? » Aucun profil de grande
entreprise, playbook, abonnement ou connecteur n'est nécessaire. L'orientation
s'appuie sur les pièces et pose une ou deux questions à la fois. Elle distingue
ce qui est établi de ce qui manque, loi applicable, juge et souhaits de négociation.

Le même artisan facturant des travaux à un particulier sera orienté vers
construction/travaux avec sa question de consommation. Ces domaines futurs ne
sont pas présentés comme des plugins disponibles. Les faits et pièces utiles
restent fournis, y compris sans profil ou source juridique accessible.

## Périmètre livré

| Entrée / composant existant | État France/UE |
|---|---|
| `/judge-fr-eu-commercial-legal:review` | Orientation COM-001 réécrite ; aucune revue aval automatique. |
| `vendor-agreement-review`, `nda-review`, `saas-msa-review` | Hérités non adaptés ; COM-002/003/004 proposés. |
| `/judge-fr-eu-commercial-legal:amendment-history` | Hérité non adapté ; COM-005 proposé. |
| `/judge-fr-eu-commercial-legal:renewal-tracker`, agent `renewal-watcher` | Hérités non adaptés ; COM-006/007 proposés, cookbook COM-018 proposé. Aucun rappel actif annoncé. |
| `/judge-fr-eu-commercial-legal:escalation-flagger`, `stakeholder-summary` | Hérités non adaptés ; COM-008/009 proposés. |
| Agents `deal-debrief`, `playbook-monitor`, `/judge-fr-eu-commercial-legal:review-proposals` | Hérités non adaptés ; COM-010/011/012 proposés. |
| `/judge-fr-eu-commercial-legal:cold-start-interview`, `/judge-fr-eu-commercial-legal:customize`, `/judge-fr-eu-commercial-legal:matter-workspace` | Personnalisation/dossiers hérités à adapter (COM-013/014) ; aucun préalable pour l'orientation ponctuelle. |
| Paiement, pénalités, préparation de rupture | COM-015/016/017 proposés ; aucun nouveau skill livré. |

Les noms techniques sont conservés. Leur présence ne certifie pas leur
adaptation. Même avec `confirm_routing: false`, `review` ne lance aucune branche
non adaptée. La fiche n'est ni une revue complète ni un feu vert pour signer.
Elle se termine par une phrase courte qui nomme l'interlocuteur compétent pour
la branche retenue (notaire pour ses frais, avocat en pénal…) et s'ouvre sur
un renfort en cas de délai, de procédure ou de convocation (BASE-013, 0.2.1).

## Pièces, sources et accès optionnels

Fichier fourni, texte collé ou récit suffisent. Drive, SharePoint, Box et CLM
peuvent fournir les documents si l'accès existe ; sinon, fournir l'extrait utile
ou une retranscription. Les connecteurs configurés dans `.mcp.json` (Ironclad,
DocuSign, Slack, Google Drive) restent optionnels ; leur configuration ne prouve
pas leur connexion. Aucun envoi, signature, inscription de registre, lancement
d'agent ou déploiement ne découle de la demande d'orientation.

Lire les [règles d'orientation et états des branches](references/orientation-commerciale.md)
et la [méthode de recherche/citation embarquée](references/shared/research-citation-method.md).
Les sources officielles sont recherchées selon les faits ; sans lecture de la
source/version utile, la conclusion juridique dépendante reste réservée.
Aucun abonnement PISTE ni connecteur américain de recherche n'est requis.

## Installation et données

```text
/plugin install judge-fr-eu-commercial-legal@judge-fr-eu --scope user
```

Le modèle `CLAUDE.md` livré est un modèle, jamais le profil utilisateur.
Les préférences facultatives existantes se lisent sous
`~/.claude/plugins/config/judge-fr-eu/commercial-legal/CLAUDE.md`, uniquement via
le helper embarqué. Profil absent/incomplet : l'orientation continue sans import
ni création. Sortie dans la conversation ; conservation seulement si demandée,
dans l'espace isolé validé via le helper. Aucune donnée durable dans le paquet.
Voir la [frontière de stockage](references/isolation.md).

Fork indépendant maintenu par Judge FR/UE, dérivé de Claude for Legal /
Anthropic sans affiliation revendiquée. [Licence](LICENSE) et [modifications](NOTICE).
