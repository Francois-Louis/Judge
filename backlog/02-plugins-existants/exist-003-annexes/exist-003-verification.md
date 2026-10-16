# EXIST-003 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre les
pièces fictives ci-dessous dans les [21 propositions PRV](exist-003-decoupage-donnees.md)
et chercher les rôles, branches, preuves et limites manquants. Le
[relevé machine](exist-003-resultats.json) donne séparément les contrôles de
structure et les empreintes ; les scénarios A01 à P06 des suites restent à
exécuter lors de leurs implémentations.

## Dossier fictif D — demande d'accès

Pièces inventées, sans données réelles :

- `D-demande` : « Je souhaite une copie de mes données de compte, les personnes
  à qui elles ont été communiquées et mes tickets. Supprimez ensuite ce qui
  peut l'être. » Contact d'un commerce français, sans avocat du demandeur.
- `D-reception` : message déclaré reçu le 31 janvier 2026 à 15 h, avec
  export de réception fourni. Le service répond le 3 février pour demander
  une copie intégrale de carte d'identité sans motif fourni.
- `D-CRM` : extraction fournie ; `D-tickets` contient des échanges mêlant des
  données de tiers ; `D-analytics` n'a pas été recherché. Pas de preuve
  d'effacement ni de demande adressée au prestataire de sauvegarde.
- `D-profil` : SLA interne « 45 jours » et modèle « Do Not Sell or Share ».
  Un prestataire d'hébergement reçoit aussi la demande, sans instruction jointe.

| Point relu | Parcours et résultat documentaire | Conclusion réservée / preuve suivante |
|---|---|---|
| Côté demandeur | PRV-001 prépare demande d'accès avec contact/champs utiles ; aucun profil DPO ni modèle d'opt-out importé. | Pas de récupération de compte ni de plainte envoyée. Aidant sans mandat reçoit questions, pas représentation supposée. |
| Qualification | PRV-002 sépare accès et effacement liés, responsable et hébergeur ; la demande ne se résume pas à effacer le compte. | Mandat, rôle exact et instructions au prestataire restent à établir. |
| Identité et calendrier | PRV-002 exige source, déclencheur, calcul en mois et effet exact de la demande d'identité ; contredit explicitement suspension automatique et SLA 45 jours pris pour loi. | Aucun terme légal chiffré n'est calculé ou validé dans cette relecture ; la fin de mois fait partie de la recette future. Demande d'ID proportionnée à justifier. |
| Copie et informations | PRV-003 prépare les éléments d'accès avec sources, tiers et occultation ciblée, non une seule liste de catégories ou de prestataires. | Analytics non recherché et pièces manquantes interdisent exhaustivité. Pas de refus total déduit des tiers. |
| Effacement | PRV-004 distingue proposée/demandée/prouvée et conservation à rechercher ; le projet ne dit pas « compte supprimé ». | Backups sans preuve ne sont ni supprimés ni exemptés en bloc. Aucun acte technique ou notification exécuté. |
| Autres droits | PRV-005/006/007/008 ont chacun un résultat, entrées et limites ; opposition n'est ni portabilité ni limitation. | Retrait de consentement/décision automatisée restent orientés depuis PRV-002, sans branche héritée exécutée. |
| Données et confidentialité | PRV-020 et clauses communes prévoient id pseudonyme, journal minimisé et note interne distincte de la lettre. | Aucun nom d'individu dans slug ni attorney work product garanti ; canal sûr à confirmer. |

**Constat :** le parcours répond aux deux côtés sans inverser implicitement
les rôles. Il ne produit ni opt-out américain par défaut, ni effacement
déclaré depuis un brouillon. Le 31 janvier et la demande d'ID servent à
éprouver le plan de vérification des déclencheurs, pas à annoncer une échéance.

## Dossier fictif C — contrat de sous-traitance

- `C-MSA-v3` : une association française confie à Nacre SaaS l'hébergement
  de ses adhésions et l'envoi d'emails. Le prix et l'auteur du DPA sont connus,
  les moyens réellement choisis ne le sont qu'en partie.
- `C-DPA-v1` : étiquette « processor for all operations », instructions pour
  le service, clause de réutilisation de certains flux pour entraîner un modèle
  du fournisseur ; sous-traitants ultérieurs renvoyés à une liste non fournie.
- `C-securite` : attestation commerciale « SOC 2 » et annexe absente.
  Notification « 72 h after confirmation » sans distinguer destinataires.
- `C-flux` : serveur France ; support distant au Maroc déclaré. Le fournisseur
  cite « EU-US DPF » pour tous ses flux, avec une entité certifiée différente
  de celle du contrat. CCT et analyse du transfert non jointes.

| Point relu | Parcours et résultat documentaire | Réserve / prochaine pièce |
|---|---|---|
| Qualification des rôles | PRV-013 confronte opérations/finalités/moyens aux étiquettes, y compris réutilisation propre. | Envoi du DPA et paiement ne déterminent pas le rôle ; mauvaise branche responsable/responsable non forcée dans art. 28. |
| Revue bornée | PRV-014 conserve lecture clause/source/écart et petites redlines ; sécurité, instructions, assistance, audits, fin et chaîne examinés. | Annexe et liste manquantes signalées ; attestation seule ne valide pas tout. MSA gardé chez commercial pour le reste. |
| Délais | PRV-014 sépare acteur, destinataire, déclencheur, loi et clause négociée. | « 72 h » reste une stipulation fictive à examiner, pas une règle identique pour prestataire, responsable, autorité et personnes. |
| Flux | PRV-015 reçoit le support distant, le pays et l'entité de chaque flux. | Serveur français ne suffit pas ; DPF générique ne couvre pas automatiquement un autre pays/une autre entité. Statut/champ à rechercher, pas affirmés ici. |
| Pièces de transfert | PRV-015 rapproche mécanisme allégué, module/annexes, analyse et mesures fournies ; TIA complète exclue. | Aucun TIA produit depuis le seul contrat ; PRV-014 peut signaler section non instruite sans dépendance cyclique. |
| Cohérence aval | PRV-017 compare la notice et le projet de pratique ; PRV-018 distingue revue/signature/exécution. | Signature du DPA ne prouve ni légalité d'une réutilisation ni déploiement effectif du flux. |

**Constat :** les propositions distinguent rôle contractuel, obligations de
sous-traitance, mécanisme de transfert et preuve de pratique. La fiche de
transfert ne promet pas une TIA complète ou un avis sur tout le droit étranger.

## Dossier fictif S — suivi de santé

- `S-description` : association projetant un suivi de symptômes d'adolescents
  via application et objets connectés. Échelle annoncée « à terme nationale »
  sans nombre, données dites « anonymisées » avec identifiant stable et clé.
- `S-flux` : prestataire déclaré HDS ; catégories/durées non arrêtées,
  support étranger et communication d'un score à un employeur envisagés.
- `S-seed` : PIA américaine marquée APPROVED, conclusion « HIPAA/BAA, opt-out
  parental » ; aucun avis DPO fourni. Matrice d'accès sans journalisation,
  chiffrement annoncé comme action future et risque résiduel non évalué.
- `S-notice` : « nous collectons uniquement les coordonnées d'inscription » ;
  projet de nouvelle notice, sans mise en ligne ni consentement prouvés.

| Point relu | Parcours et résultat documentaire | Réserve / prochaine pièce |
|---|---|---|
| Traitement et compléments français | PRV-009 documente finalités/données/personnes, vulnérabilité, accès/flux, bases à rechercher, RGPD/LIL et questions santé françaises ciblées. | HDS seul, nom anonyme et opt-out parental ne valident pas activité, anonymisation ou base. Secret, hébergement, mineurs et finalité score à instruire séparément. |
| Nécessité AIPD | PRV-010 distingue obligation, choix interne et faits inconnus, confronte textes/listes CNIL/CEPD à échelle et critères. | Pas de calcul mécanique ni d'obligation du seul mot santé ; nombre/échelle et versions des listes à rechercher. |
| Projet AIPD | PRV-011 remplace le seed comme source de contenu obligatoire, risques pour personnes, nécessité/proportionnalité et états des mesures. | Aucun APPROVED repris du seed ; chiffrement futur ne réduit pas déjà le risque. Pas de plafond artificiel de risques. |
| Consultation | PRV-012 prépare l'examen des conditions et pièces à partir du risque résiduel documenté. | Absence d'avis ou santé ne déclenchent pas transmission universelle à CNIL ; risque après mesures inconnu reste inconnu. |
| Contrat et transferts | PRV-013/014/015 posent rôles/annexes/flux propres ; compléments ciblés santé, pas HIPAA automatique. | Pas de conformité depuis HDS ou BAA ; absence de TIA visible. |
| Information et suivi | PRV-017 relève divergence et question de base ; PRV-018 classe nouveau texte comme projet, reprend les manques/gravités. | Une notice réécrite ne résout pas finalité/base ; aucun suivi ne transforme brouillon en pratique déployée. |
| Relais | DOM-009 pour droits de soins/dossier médical, travail pour destinataire employeur, IA pour sa question spécifique. | Fiche de questions sans appeler des workflows étrangers/non adaptés ou annoncer leur installation. |

**Constat :** la suite distingue qualification, nécessité d'AIPD, projet,
risque résiduel, préparation de consultation et information. Les références
françaises sont ciblées par les questions, sans prétendre couvrir tout le
droit de la santé ou valider ces pièces inventées.

## Cas complémentaires relus

| Cas | Exigence retrouvée dans les propositions |
|---|---|
| Changement annoncé par résumé de consultation publique | PRV-016 sépare portée, statut et transition ; pas d'obligation nouvelle affirmée ni conformité tirée du silence. |
| Dossier outputs vide ou Drive partiellement accessible | PRV-018 garde couverture et dernier état complet ; pas de « policy current » ni pointeur avancé globalement. |
| Texte tiers contenant instruction, formule tableur ou HTML | Le contrat de paquet et dashboard commun conserve la protection ; les documents restent données, la preuve brute est distincte du rendu. Vérification en recette future, pas démonstration d'exécution ici. |
| Profil absent/interrompu, association sans avocat | Chaque tranche corrige ses blocs d'accès, PRV-019 préserve réponses et préférences sans US par défaut ; helper reste requis pour données durables. |
| Date de veille ancienne et adéquation invoquée | PRV-021 exige état/date par entrée et lecture effective ; aucun statut juridique actuel déduit du fichier hérité. |
| Même organisme, deux personnes et archive homonyme | PRV-020 prévoit ids minimisés, collisions refusées et pas de lecture croisée pour compléter une demande. |

## Contrôles exécutés et portée

Le relevé machine vérifie couverture exacte des 23 fichiers/9 skills,
empreintes et absence de modification du plugin et du contenu éditeur,
cinq copies communes identiques, 21 propositions indexées, frontmatter,
identifiants/dépendances sans cycle, liens locaux, JSON et format. Les
modifications antérieures EXIST-001/002 et leurs suites sont préservées.

**Portée :** cadrage et relecture par le seul agent de maintenance sur pièces
entièrement fictives ; contrôles statiques uniquement. Aucune source juridique
externe consultée, aucun délai calculé ou droit applicable validé, aucun skill
adapté/exécuté, paquet installé, client testé, lecteur réel/indépendant,
connexion, envoi, effacement, signature ou déploiement. Les recherches de droit
et recettes métier restent à exécuter dans les suites choisies.
