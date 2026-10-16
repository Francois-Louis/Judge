# Judge FR/UE — lot 001

Lot préparé le **16 octobre 2026** (LIV-001). Il contient **un seul plugin** :
`judge-fr-eu-employment-legal` version **0.2.1**. Les onze autres plugins du
dépôt, le plugin éditeur CoCounsel et les cookbooks ne sont pas livrés.

## Ce qui est adapté

Une seule tâche est réécrite pour la France : `hiring-review`. Elle aide un
candidat à lire une offre ou un contrat de travail salarié du secteur privé :
engagements des deux parties, sources et versions, conséquences concrètes,
questions à poser au recruteur. Le CDI en métropole est le cas nominal ; le CDD
ordinaire reçoit des contrôles limités. Emploi public, contrats spéciaux,
outre-mer et travail transfrontalier reçoivent une orientation explicite.

Le parcours candidat de `cold-start-interview` et `customize` permet de
mémoriser volontairement une préférence de présentation, sans profil
d'entreprise.

Commandes :

```text
/judge-fr-eu-employment-legal:hiring-review
/judge-fr-eu-employment-legal:cold-start-interview
/judge-fr-eu-employment-legal:customize
```

## Ce qui n'est pas adapté

Les autres commandes du même plugin (rupture, classification, congés,
enquêtes, politiques, handbook, expansion, paie), l'agent `leave-tracker`,
les hooks et les connecteurs déclarés sont **hérités de Claude for Legal et
non adaptés** à la France ou à l'Union européenne. Ils restent présents dans
le paquet testé ; ne pas les utiliser comme s'ils l'étaient.

## État de validation

- Recette dans un client Claude Code isolé (BASE-011), sur pièces fictives :
  scénarios H02 à H16, sans profil, sans source accessible et préférences
  candidat, réussis techniquement.
- Le lecteur était le porteur du projet, **non indépendant**. Aucun essai
  avec une personne extérieure, aucune relecture juridique indépendante.
- Le scénario nominal complet H01 n'a pas été exécuté (défaut D02 ouvert).
- Écarts consignés pendant la recette : une instruction injectée dans une
  pièce est ignorée mais pas signalée ; une règle citée « de mémoire » quand
  aucune source n'est accessible, avec réserve.
- La version 0.2.1 ne change que le manifeste, le README et la NOTICE du
  plugin ; les instructions des skills et les références sont identiques à
  celles de la recette.

Ce lot ne constitue ni une certification de conformité ni un avis juridique.

## Installer

Prérequis : Claude Code, Python 3.12 ou ultérieur pour l'assistant de
stockage embarqué.

1. Vérifier l'empreinte de l'archive avec celle publiée avec le lot, puis
   l'extraire dans un dossier relu.
2. Ajouter le marketplace du lot et installer le plugin :

```text
claude plugin marketplace add <chemin-absolu-vers-judge-fr-eu-lot-001>
claude plugin install judge-fr-eu-employment-legal@judge-fr-eu --scope user
```

3. Dans `/plugin`, onglet Marketplaces, vérifier que la mise à jour
   automatique de `judge-fr-eu` est désactivée.

Le marketplace du lot s'appelle `judge-fr-eu`, comme celui du dépôt complet :
n'ajouter que l'un des deux. Le plugin d'origine `employment-legal` de Claude
for Legal peut rester installé ; les commandes qualifiées sont distinctes et
aucune configuration de l'origine n'est lue.

## Données

Aucun profil n'est créé par défaut. Une préférence mémorisée est écrite sous
`~/.claude/plugins/config/judge-fr-eu/employment-legal/`, hors du paquet ; une
mise à jour ou une désinstallation du plugin ne la supprime pas.

## Licence et provenance

Dérivé de Claude for Legal, Copyright 2026 Anthropic PBC, sous licence Apache
2.0 : voir `LICENSE`. Les fichiers modifiés par le fork sont listés dans
`NOTICE` et `employment-legal/NOTICE`. Fork maintenu par Judge FR/UE
maintainers (github.com/Francois-Louis/Judge), sans affiliation ni
approbation revendiquée d'Anthropic. `lot-inventory.json` donne la révision
source et l'empreinte SHA-256 de chaque fichier.
