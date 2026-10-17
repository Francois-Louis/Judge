<!-- Modified by Judge FR/UE for PILOTE-002 (2026-10-15): scope and setup of French hiring pilot. -->
<!-- Modified by Judge FR/UE for LIV-001 (2026-10-16): version 0.2.1, validation status and lot installation. -->
<!-- Modified by Judge FR/UE for TRAV-001 (2026-10-17): version 0.3.0, worker-classification adapted. -->
<!-- Modified by Judge FR/UE for BASE-013 (2026-10-17): version 0.3.1, closing scope sentence. -->
<!-- Modified by Judge FR/UE for BASE-014 (2026-10-17): version 0.3.2, source review dates. -->
<!-- Modified by Judge FR/UE for BASE-014 follow-up (2026-10-17): version 0.3.3, LEGI version review. -->
<!-- Modified by Judge FR/UE for TRAV-062 (2026-10-17): version 0.3.5, court decisions read in hiring-review-fr.md 1.1.0. -->

# Judge FR/UE — revue d'embauche et qualification d'une relation

Version du plugin **0.3.5**. Deux tâches sont réécrites pour la France.
Chaque note se termine par une phrase courte : elle aide à comprendre et à
préparer, sans remplacer l'avis d'un avocat ou d'un juriste en droit du
travail ; un renfort ouvre la note si une signature ou une réponse presse
(BASE-013, méthode BASE-005 1.1.0). Depuis la méthode 1.2.0 (BASE-016), une
décision de justice n'est citée qu'après lecture de ses motifs ; sinon elle
reste une piste et la conclusion qui en dépend est réservée. Les repères
d'embauche 1.1.0 (TRAV-062) portent quatre arrêts de la chambre sociale lus
sur Légifrance, avec leur fiche : non-concurrence et offre/promesse.
`worker-classification` est décrit [plus bas](#qualifier-une-relation-avant-quelle-commence).
`hiring-review` porte sur l'embauche
salariée du privé en France : lire une offre ou un contrat reçu, comprendre
les engagements et préparer les questions au recruteur. CDI métropolitain
comme cas nominal ; CDD ordinaire avec contrôles spécifiques limités.
La recette en client isolé a été exécutée sur pièces fictives (BASE-011,
16 octobre 2026) ; le lecteur était le porteur du projet, non indépendant,
et le scénario nominal complet H01 n'a pas été exécuté. Aucune relecture
juridique indépendante. Ce paquet n'est pas une certification de conformité.

## Commencer avec un contrat reçu

Depuis le lot livré (LIV-001), après extraction de l'archive dans un
dossier relu, ajouter le marketplace par son chemin absolu :

```text
claude plugin marketplace add <chemin-absolu-vers-judge-fr-eu-lot-001>
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

Indiquer que le besoin est la lecture d'une offre en France. « En texte court
pour cette réponse » reste dans la conversation ; « mémorise texte court »
crée seulement cette préférence, puis `customize` peut la passer à « tableau ».
Les autres réponses restent inchangées, y compris avec un ancien profil US ou
des champs professionnels vides. Aucun profil société, registre ou test de
connecteur n'est nécessaire. Le profil
reste sous `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md`,
hors du paquet remplaçable. Un profil minimal n'active pas les autres parcours.
Le résultat indique la valeur mémorisée et son emplacement avant de revenir
à la revue. Sans exécuteur Python, la lecture des pièces fournies continue en
conversation et la préférence n'est pas enregistrée. Voir le
[parcours candidat](references/candidate-preferences.md) (PILOTE-004) ; sa
recette client a été exécutée sur fixtures (BASE-011) ; aucun lecteur
indépendant.

La restitution explique les engagements des deux parties, puis rapproche
clause/pièce, source et version, conséquence concrète, proposition ou question
avec son destinataire. Elle rend les faits manquants prioritaires et une
prochaine étape. Un texte court ou une liste peut remplacer le tableau selon
le besoin. Les montants bruts, versements fixes et variables sont distingués.
Aucun feu vert à signer, acceptation, envoi, suivi ou inscription à un registre.

## Qualifier une relation avant qu'elle commence

`/judge-fr-eu-employment-legal:worker-classification` (TRAV-001) aide un futur
donneur d'ordre, un futur prestataire ou un candidat à qui l'on propose un
statut d'indépendant, **avant tout début d'exécution**. Décrire la mission :
tâches, qui décide des horaires et méthodes, outils, prix, durée, lieux et
dates, intermédiaire éventuel (agence, portage, plateforme).

La note relie chaque fait aux critères lus : subordination (ordres, contrôle,
sanction, service organisé), présomption attachée à l'immatriculation, objet
du contrat (prestation ou mise à disposition de personnel). Elle signale les
risques sans chiffrage, les pièces à demander et l'interlocuteur. **Elle ne
choisit pas le statut.** Une relation déjà commencée reçoit une orientation
distincte, sans analyse rétrospective. Emploi public, territoires non couverts,
travail transfrontalier, plateformes et métiers à présomption de salariat
sont orientés. Repères embarqués : [qualification d'une relation 1.1.0](references/worker-classification-fr.md).
Hors champ : contrat complet, audit du passé, cotisations et impôts chiffrés.
Exécuté le 17 octobre 2026 sur trois pièces fictives dans un client réel non
isolé ; aucun lecteur non juriste ni relecture juridique indépendante.

## Sources et prérequis réels

- Python 3.12 ou ultérieur pour le helper de stockage, avant tout accès aux
  profils ou sorties persistantes ; voir [la frontière de stockage](references/isolation.md).
- Les références nécessaires sont embarquées : [méthode BASE-005 1.2.0](references/shared/research-citation-method.md),
  [repères d'embauche France 1.1.0](references/hiring-review-fr.md) et
  [qualification d'une relation 1.1.0](references/worker-classification-fr.md).
  Le parcours reprend USAGE-001 1.0.0 dans ses propres instructions.
  Chaque source de ces repères porte sa date et son issue de relecture
  avant livraison (colonne « Relecture », BASE-014) ; dernière relecture
  le 17 octobre 2026, versions recherchées dans le fonds LEGI de la DILA :
  L8222-2 a une version future (au plus tard le 26 décembre 2026), intégrée
  aux repères de qualification 1.1.0 ; aucune autre version future ni fin.
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

Les commandes de rupture, congés, enquêtes,
politiques, handbook, expansion et questions de paie restent dans le paquet
hérité. L'agent `leave-tracker`, les hooks et les connecteurs déclarés ne sont
pas validés par ce pilote. La configuration professionnelle historique reste
présente pour ces parcours, avec ses limites. Ne pas les appeler pour
compléter les tâches adaptées ni présenter leur installation comme une adaptation.

Les seuls changements à `cold-start-interview`, `customize` et au modèle de
profil servent le chemin court d'embauche. Le pilote ne garantit aucun secret
professionnel du seul fait d'un en-tête. L'explication et la préparation d'un
brouillon sont accessibles sans consultation préalable ; les questions hors
champ ou non résolues peuvent être préparées pour un professionnel compétent.

Fork indépendant de Claude for Legal / Anthropic, maintenu par Judge FR/UE
sur [Francois-Louis/Judge](https://github.com/Francois-Louis/Judge), sans
revendication d'affiliation. Voir [licence](LICENSE) et [modifications](NOTICE).
