<!-- Modified by Judge FR/UE for PILOTE-002 (2026-10-15): scope and setup of French hiring pilot. -->

# Judge FR/UE — revue d'embauche

Version du plugin **0.2.0**. Seul `hiring-review` est réécrit pour l'embauche
salariée du privé en France : lire une offre ou un contrat reçu, comprendre
les engagements et préparer les questions au recruteur. CDI métropolitain
comme cas nominal ; CDD ordinaire avec contrôles spécifiques limités.
La recette dans un client isolé et l'essai avec un participant non juriste
restent à réaliser. Ce paquet n'est pas une certification de conformité.

## Commencer avec un contrat reçu

```text
/plugin install judge-fr-eu-employment-legal@judge-fr-eu --scope user
/judge-fr-eu-employment-legal:hiring-review
```

Présenter le contrat, un extrait ou une description en mots courants, avec
les lieux de travail, dates et fonctions connus. Masquer les identifiants et
coordonnées inutiles. Aucun profil d'entreprise, handbook ou playbook requis.
Un bref entretien dans la conversation permet de démarrer sans profil ; les
inconnues restent visibles. Pas de profil persistant créé par défaut.

Pour conserver volontairement des préférences, utiliser le chemin court :

```text
/judge-fr-eu-employment-legal:cold-start-interview
/judge-fr-eu-employment-legal:customize
```

Indiquer que le besoin est la lecture d'une offre en France. La configuration
courte renseigne seulement les faits utiles et le format souhaité. Le profil
reste sous `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md`,
hors du paquet remplaçable. Un profil minimal n'active pas les autres parcours.

La restitution explique les engagements des deux parties, puis rapproche
clause/pièce, source et version, conséquence concrète, proposition ou question
avec son destinataire. Elle rend les faits manquants prioritaires et une
prochaine étape. Un texte court ou une liste peut remplacer le tableau selon
le besoin. Les montants bruts, versements fixes et variables sont distingués.
Aucun feu vert à signer, acceptation, envoi, suivi ou inscription à un registre.

## Sources et prérequis réels

- Python 3.12 ou ultérieur pour le helper de stockage, avant tout accès aux
  profils ou sorties persistantes ; voir [la frontière de stockage](references/isolation.md).
- Les références nécessaires sont embarquées : [méthode BASE-005 1.0.0](references/shared/research-citation-method.md)
  et [repères d'embauche France 1.0.0](references/hiring-review-fr.md).
  Le parcours reprend USAGE-001 1.0.0 dans ses propres instructions.
- Lecture de sources officielles par les outils disponibles dans la session,
  sans connecteur spécifique ni abonnement API obligatoire. Leur disponibilité
  doit être observée. Si une source manque, la conclusion concernée reste
  réservée ; les pièces et questions peuvent être expliquées.
- Aucune convention collective n'est certifiée ici. L'activité réelle,
  le champ, les textes et accords applicables demandent vérification. L'APE
  seul et l'intitulé du poste ne permettent pas de conclure.

Le contrôle CDD initial couvre recours/motif, terme ou durée minimale,
mentions, essai et transmission. Il ne valide pas durée maximale,
renouvellements/successions, carence, indemnités ou rupture. Non-concurrence,
forfait et autres clauses sensibles exigent leurs textes et décisions utiles.
Les sources non lues et les limites sont signalées dans les repères métier.
Emploi public, contrats spéciaux, particulier employeur, outre-mer à qualifier
et travail transfrontalier reçoivent une orientation explicite.

## Reste du paquet : hérité et non adapté à la France/UE

Les commandes de rupture, classification d'indépendants, congés, enquêtes,
politiques, handbook, expansion et questions de paie restent dans le paquet
hérité. L'agent `leave-tracker`, les hooks et les connecteurs déclarés ne sont
pas validés par ce pilote. La configuration professionnelle historique reste
présente pour ces parcours, avec ses limites. Ne pas les appeler pour
compléter la revue adaptée ni présenter leur installation comme une adaptation.

Les seuls changements à `cold-start-interview`, `customize` et au modèle de
profil servent le chemin court d'embauche. Le pilote ne garantit aucun secret
professionnel du seul fait d'un en-tête. L'explication et la préparation d'un
brouillon sont accessibles sans consultation préalable ; les questions hors
champ ou non résolues peuvent être préparées pour un professionnel compétent.

Fork indépendant de Claude for Legal / Anthropic, maintenu par Judge FR/UE
sur [Francois-Louis/Judge](https://github.com/Francois-Louis/Judge), sans
revendication d'affiliation. Voir [licence](LICENSE) et [modifications](NOTICE).
