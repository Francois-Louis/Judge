# EXIST-005 — Vérification documentaire du cadrage IA

Relecture du **16 octobre 2026 (Europe/Paris)** par l'agent de maintenance,
sur les [20 propositions IA](exist-005-decoupage-ia.md). Les pièces ci-dessous
sont entièrement fictives. Le résultat est un contrôle des questions, des
propriétaires et des réserves prévus par le cadrage, pas une sortie de skill
exécuté ni une qualification juridique définitive. Les scénarios nommés des
suites restent des recettes futures. Les [résultats machine](exist-005-resultats.json)
consignent séparément contrôles statiques, commandes et empreintes.

## Dossier RH — outil de recrutement

Pièces inventées :

- `RH-projet-v2` : une PME française envisage un SaaS qui ordonne les CV et
  propose une présélection. Le recruteur peut modifier la liste ; fréquence
  réelle de contrôle et effet d'une exclusion non documentés.
- `RH-notice-v1` : « matching intelligent », option d'analyse de vidéo
  « sentiment/émotion » non décrite. Finalité exacte, profilage, données
  traitées et modèle sous-jacent inconnus.
- `RH-contrat` : fournisseur déclaré hors UE ; contrat, annexe amont et nom
  de mise à disposition incomplets. La PME annonce un paramétrage métier,
  sans preuve de fine-tuning ou de changement de finalité.
- `RH-profil` : ancien registre « outils internes approved », tier Standard.
  `RH-calendrier` : pilote prévu le 20 novembre 2026, date d'équipe ; le brief
  affirme que toutes les obligations sont reportées, sans texte joint.

| Question de cadrage | Parcours prévu / résultat de relecture | Faits et conclusion réservés |
|---|---|---|
| Quel objet, quelle version et quels usages ? | IA-001 distingue classement des CV et fonction vidéo, avec versions et pièces. IA-002 demande système/modèle, finalité, parties et lieux d'utilisation. | Un nom de produit, un siège français ou le mot interne ne déterminent pas rôle et champ. |
| Qui développe, commercialise, utilise et modifie ? | IA-002 demande contrats, nom/marque et changements réellement effectués, par acteur. | Achat SaaS ne suffit pas à conclure déployeur seul ; paramétrage ou fine-tuning ne suffit pas à conclure fournisseur. |
| Pratique interdite ou haut risque ? | IA-003 demande ce que fait la vidéo ; IA-004 demande effet sur sélection/profilage et examine les voies/conditions/exception pertinentes. | Aucun classement interdit/haut risque depuis mots émotion ou RH ; présence d'un recruteur ne prouve pas exemption. Pas de catégorie définitive sur ces pièces. |
| Quelles obligations, quand ? | IA-007 peut instruire le déployeur seulement après qualification, IA-008 le dossier fournisseur si ce rôle est établi. IA-020 recherche disposition/version/transitions. | 20 novembre est une date interne ; brief de report et watch list ne prouvent ni calendrier, ni exemption, ni délai légal. |
| Quelle évaluation et quels autres domaines ? | IA-009 documente dommages/tests/contrôle ; IA-010 vérifie nécessité FRIA sans la déduire de haut risque. Fiche vers privacy et travail avec finalité, décision et faits manquants. | Nécessité AIPD chez privacy ; information/consultation, discrimination et effets RH chez travail. Aucune de ces analyses exécutée, aucun recours à la revue d'embauche du pilote comme substitut. |

**Constat du cadrage :** les questions empêchent le registre approved et le
contrôle humain annoncé de devenir une autorisation. Les acteurs, la fonction
vidéo et les effets sur la décision restent à établir ; aucune catégorie ou
date d'obligation n'est arrêtée pour cet outil fictif.

## Dossier A — assistant rédactionnel interne

- `A-demande` : une association française de six personnes sans service
  juridique veut rédiger des comptes rendus et brouillons de courrier. Elle
  n'a ni profil du plugin, ni historique d'évaluations, ni connecteur.
- `A-usage` : l'utilisateur relit les brouillons avant diffusion. Des noms
  d'adhérents et pièces de dossiers pourraient être copiés ; flux effectifs,
  hébergement et suppression non renseignés.
- `A-offre-v1` : page du revendeur « nous n'entraînons pas sur vos données ».
  `A-AUP-v2` seule pièce contractuelle ; annexe, ToS incorporées, fournisseur
  modèle et conditions de conservation non fournis.
- `A-politique-v1` : « aucun dossier d'adhérent dans un outil externe ».
  `A-sortie` : ancienne AIA marquée APPROVED mais encore en brouillon ; mesure
  « suppression des données » seulement proposée, aucune preuve de réglage.

| Question de cadrage | Parcours prévu / résultat de relecture | Faits et conclusion réservés |
|---|---|---|
| Quel premier résultat sans configuration lourde ? | IA-001 prépare une fiche factuelle conversationnelle ; IA-018 reste volontaire. Aucun compte, GC ou seed obligatoire. | Tout accès durable respecte BASE-008 ; créer un profil absent nécessite entretien neuf, sans cache ni import. |
| Système ou modèle GPAI ? | IA-002 qualifie l'assistant ; IA-006 décrit séparément le modèle si la question est documentée. | L'usage d'une API généraliste ne classe pas tout le système gpai et ne donne pas à l'association le rôle de fournisseur de modèle. |
| Quels engagements d'entraînement/conservation ? | IA-012 cartographie documents, parties et promesse commerciale ; IA-013 ne rédige qu'un écart précis sur clauses fournies. | AUP seule ne décrit pas tous les engagements ; absence d'annexe ne prouve ni entraînement autorisé ni absence de protection. No training commercial n'établit pas la chaîne contractuelle. |
| Quels impacts et quelles preuves ? | IA-009 rapproche erreurs de rédaction, destinataires et contrôles proposés/prouvés. | Relecture annoncée et AIA brouillon ne prouvent pas réalisation des mesures ni approbation humaine attribuée. |
| Politique ou pratique à changer ? | IA-015 localise contradiction d'import envisagé avec politique ; IA-014 peut préparer un projet rédactionnel borné. | Ne pas réécrire silencieusement l'interdiction pour suivre l'usage. Politique ne remplace ni contrat, ni examen RGPD, ni formation effectivement réalisée. |
| Que transférer à privacy ? | Fiche autonome : finalité, catégories de données, personnes, flux, décisions, pièces non lues, questions de traitement/contrat/transfert. | AIPD non automatique depuis donnée personnelle ; relais PRV encore proposé, pas de plugin voisin supposé disponible ni de doublon d'analyse. |

**Constat du cadrage :** l'association peut obtenir des fiches et questions
concrètes sans service juridique constitué. Usage interne ne signifie ni
risque minimal, ni absence d'obligation ; aucune conformité ou catégorie
définitive n'est déduite de ces pièces fictives.

## Dossier S — service destiné au public

- `S-fiche-v1` : une structure propose un chatbot public « aide aux démarches ».
  Elle déclare travailler avec une collectivité, sans document de mission ni
  qualité juridique établie. Le service pourrait répondre à des questions
  générales ou recommander des décisions d'accès à une aide ; portée inconnue.
- `S-interface` : maquette sans mention IA visible ; preuve d'affichage et
  canal mobile absents. Public mineur ou vulnérable possible, non décrit.
- `S-stack` : intégrateur sous sa marque utilisant un modèle tiers ; contrat,
  version et rôle exact de chaque acteur non fournis.
- `S-docs` : une AIPD d'un ancien formulaire est invoquée, sans contenu. Une
  ancienne AIA est présentée comme « certificat FRIA ». Le brief parle d'un
  guide Commission obligatoire et d'un nouveau calendrier, sans publication.

| Question de cadrage | Parcours prévu / résultat de relecture | Faits et conclusion réservés |
|---|---|---|
| Information générale ou effet sur accès au service ? | IA-002 demande fonction, effet, publics et qualité des acteurs ; IA-004 examine critères et voies haut risque si pertinents. | Chatbot public ne détermine pas seul catégorie ; recommandation d'aide non décrite empêche de conclure. |
| Qui fournit le système, qui l'utilise, quel modèle ? | IA-002/006 séparent marque, intégration, mise à disposition, usage et modèle. IA-008 recense pièces si fournisseur système et champ établis. | Pas d'assimilation intégrateur/fournisseur modèle ni de certificat du modèle réputé couvrir le service. |
| Quelle transparence pour qui ? | IA-005 distingue interaction, marquage du fournisseur et information au public ; demande captures et preuve de diffusion. | Absence de mention dans maquette n'est pas constat de violation actuelle ; mention proposée ne prouve pas affichage conforme. |
| La FRIA est-elle nécessaire ? | IA-010 demande qualité/mission du déployeur, activité, catégorie et dates. IA-011 ne prépare le projet borné service public que si le besoin est établi. | Public visé, collectivité citée ou seul haut risque ne rendent pas FRIA universelle. AIA et AIPD ancienne ne sont pas substituts. Aucune décision sur nécessité ici. |
| Quelles interactions sectorielles ? | Produit reçoit lancement/version/canal ; privacy reçoit traitement/flux/décisions ; service public et secteur de l'aide reçoivent qualité, mission et effet précis. | Aucun dossier sectoriel complet ni décision d'octroi généré. En absence de tâche adaptée, remettre la fiche/questions sans appel d'un skill hérité. |
| Guide, autorité et calendrier ? | IA-020 identifie publication/statut, compétence française selon question et disposition temporelle ; IA-017 examine changement réellement lu. | Ni guide réputé contraignant, ni CNIL présumée autorité unique, ni report général depuis un brief. Aucun délai déterminé. |

**Constat du cadrage :** les propositions préparent les faits discriminants
avant de distinguer simple information, accès à un service et analyse FRIA.
Elles gardent l'évaluation interne, l'AIPD, la FRIA et la conformité technique
séparées ; aucune classification définitive du service fictif n'est retenue.

## Cas limites transverses relus

| Cas documentaire | Exigence prévue / résultat de relecture |
|---|---|
| Inventaire par société : un rôle pour trois systèmes | IA-001/002/006 séparent organisme, systèmes/usages et modèle ; rôle/qualification par acteur et objet, pas simple remplacement Builder par fournisseur. |
| Système hors liste d'usages mais intégré à un produit réglementé | IA-004 conserve voie produit, procédure et pièces sectorielles à rechercher ; pas de risque minimal par élimination. |
| Règle étrangère présentée comme plus stricte | IA-002 recherche champ propre, conflit et dates ; pas d'application automatique par règle du strictest regime. |
| Corpus vide, sortie brouillon, fichier illisible ou modification le même jour | IA-016 expose couverture et états, n'annonce pas politique à jour et n'avance pas le jalon au-delà des éléments effectivement revus. |
| Texte d'une pièce demandant de publier une note | Contenu tiers traité comme donnée dans les suites ; aucune exécution, envoi Slack ou modification d'autorisation depuis la pièce. |
| Profil interrompu, concurrent ou absent | IA-018 préserve sections et réponses, digest et entretien neuf pour création durable ; fiche ponctuelle ne nécessite pas de profil complet. |
| Deux organismes, deux versions, archive homonyme | IA-019 prévoit liste minimale, séparation des journaux, refus de collision et lecture croisée seulement sur demande ciblée autorisée. |
| Source officielle inaccessible et événement non daté | IA-020 et chaque tranche tracent alternatives BASE-010, réservent la conclusion et gardent échéance à déterminer ; aucun délai de notification inventé. |
| Une seule entrée d'actualité actualisée | IA-020 garde vérification par entrée, version et champ ; les autres lignes ne deviennent pas vérifiées par mise à jour d'une date globale. |
| Mesure proposée en AIA, résumée comme réalisée dans sweep | IA-009/016 conservent états et gravité amont ou justification du changement ; aucune rétrogradation silencieuse. |

## Contrôles exécutés et limites

Le relevé machine contrôle couverture exacte des 23 fichiers/10 skills,
20 propositions et leurs dépendances, unicité des références futures,
frontmatter, liens, format, index, copies communes et empreintes. Comparaison
à l'instantané de début de tâche : seules la story EXIST-005, ses livrables,
ses 20 suites et l'index backlog changent. Les travaux EXIST-001 à EXIST-004
déjà présents, les plugins, cookbooks et contenus éditeur sont préservés.
Les contrôles sont reproductibles par le script de vérification joint au lot ;
les assertions textuelles contrôlées ne sont pas des preuves de droit.

**Portée :** inventaire du checkout, relecture documentaire par son seul
rédacteur et contrôles statiques. Aucune recherche juridique externe,
classification définitive, obligation ou échéance validée, réécriture de
plugin, skill exécuté, installation/recette client, lecteur indépendant,
compte connecté, diffusion, dépôt, certification ou programmation de veille.
Les sources et scénarios d'implémentation restent à vérifier/exécuter dans
chaque suite sélectionnée. PILOTE-003 est terminé après BASE-011, sans choix
d'extension ; limites H01 complet et lecteur indépendant conservées.
