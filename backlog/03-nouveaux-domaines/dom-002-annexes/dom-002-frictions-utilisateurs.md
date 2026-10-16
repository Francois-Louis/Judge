# Police et procédure pénale — Frictions utilisateur et réponses à prévoir

Demande du **16 octobre 2026** : « voici les frictions des utilisateurs auxquelles il faut pouvoir répondre ». Le [texte fourni](../sources/police-penal-frictions-2026-10-16.txt) est conservé intégralement comme expression du besoin. Ses 97 situations numérotées sont reliées ci-dessous aux tâches et résultats attendus.

**État : exigences de backlog.** Les 23 stories CRIM restent proposées ; aucune capacité livrée n'est déduite de cette matrice. DOM-010 reste un cadrage proposé : les réponses administratives au fond restent à découper. Aucun plugin ni skill n'est créé et aucune première tranche n'est sélectionnée.

## Lecture du texte fourni

La mention « état du droit : 16 octobre 2026 » appartient au document utilisateur. Les statistiques, rapports, délais, droits et décisions évoqués ne sont pas vérifiés ici. Les favicons et mentions « +1 » n'identifient pas des passages sources. Les liens du document sont archivés comme pistes, sans corpus juridique validé.

Les futures implémentations devront ouvrir les textes et leurs versions applicables, les pages officielles et les décisions pertinentes selon BASE-005. Points sensibles : régimes territoriaux, pouvoirs municipaux et privés, consentement aux fouilles, statut témoin/suspect, accès à l'avocat, PV et copies, usage de la force, règles de preuve, TAJ, prélèvements et expertise routière, effets d'un paiement, notification et computation de chaque délai. Aucune durée du texte ni échéance de son aide-mémoire n'est utilisée comme constante.

## Changements de découpage

- Préciser les convocations, auditions libres en cours et gardes à vue ; refus de plainte, suivi, amendes, actes de poursuite, récits de contrôle et manifestations restent chez leur propriétaire.
- Ajouter CRIM-018 à CRIM-023 : contrôle en cours, domicile, conservation des preuves, signalement d'agent, fichier TAJ, contrôle routier et rétention du permis.
- CRIM-008 garde le récit après contrôle ; CRIM-018 traite l'orientation immédiate. CRIM-002 garde audition et garde à vue. Le passage d'une mesure à l'autre est explicite.
- CRIM-020 prépare les demandes de conservation, CRIM-021 les signalements ; la plainte pénale relève de CRIM-004. Chaque démarche a son objectif et ses effets à vérifier.
- Le TAJ relève de CRIM-022 ; le casier reste CRIM-012. Un classement ne vaut pas preuve d'effacement.
- FPS, recours contre suspension/invalidation du permis et autres décisions administratives restent à DOM-010 ; CRIM lit seulement les pièces utiles au routage. Aucun recours administratif au fond livré ou promis par cette intégration.

## Matrice des 97 situations

Les propriétaires secondaires traitent une question distincte ; leur présence ne crée aucune dépendance d'installation. Contrôle en cours et récit ultérieur sont deux moments différents. Chaque résultat est une exigence future soumise à la lecture des sources.

| N° | Friction | Propriétaire et relais | Résultat attendu |
|---|---|---|---|
| 1 | « Ce n'est pas notre secteur. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Vérifier réception hors secteur et préparer la voie au procureur si blocage. |
| 2 | « Il faut prendre rendez-vous. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Documenter rendez-vous proposé, accès effectif et refus allégué. |
| 3 | « Ce n'est pas assez grave. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Consigner le motif de gravité et rechercher l'obligation de réception. |
| 4 | « Sans certificat médical, on ne peut rien faire. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Préparer les faits avec certificat absent ou à venir, sans bloquer le dossier. |
| 5 | « On ne connaît pas l'auteur. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Préparer une plainte contre X sans inventer un auteur. |
| 6 | « Ça sera classé sans suite. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Distinguer réception de plainte et décision future du parquet. |
| 7 | « Faites plutôt une main courante. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Identifier plainte ou main courante réellement enregistrée et leurs effets à vérifier. |
| 8 | « Revenez avec davantage de preuves. » | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Inventorier pièces disponibles et futures sans exiger de preuve immédiate. |
| 9 | Tes déclarations sont résumées incorrectement. | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Comparer récit et PV, demander correction ou mention du désaccord. |
| 10 | On refuse de te remettre un document. | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Demander récépissé et copie du PV de plainte selon le texte lu. |
| 11 | On te dit que les faits sont trop anciens. | [CRIM-004](../suites/crim-004-preparer-plainte.md) | Consigner faits anciens sans conclure à la prescription ni refuser leur préparation. |
| 12 | Ta plainte ne reçoit aucune suite apparente. | [CRIM-007](../suites/crim-007-suivre-plainte.md) | Préparer une demande de suivi avec référence et preuve du dépôt. |
| 13 | Contrôle sans explication | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Demander motif et fondement sans déduire l'illégalité du silence de l'agent. |
| 14 | Contrôle fondé sur l'apparence ou l'origine | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md), [DOM-029](../dom-029-discriminations.md) | Documenter indices et témoins ; question de discrimination distincte vers DOM-029. |
| 15 | On exige obligatoirement ta carte d'identité | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Vérifier moyens de justifier l'identité et obligations documentaires propres au statut. |
| 16 | Tu n'as aucun document | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Identifier contrôle et vérification sans infraction présumée du défaut de document. |
| 17 | Vérification d'identité prolongée | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Relever début, territoire et mesure avant toute règle de durée. |
| 18 | On veut t'interroger sur une autre affaire pendant la vérification | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md), [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Détecter le changement de statut ou de mesure et orienter vers CRIM-002. |
| 19 | On te photographie ou prend tes empreintes | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Rechercher cadre, autorisation et pièces pour photographie ou empreintes. |
| 20 | Un policier municipal annonce un contrôle d'identité général | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Distinguer pouvoirs municipaux et nationaux, relevé et contrôle. |
| 21 | On te tutoie, menace ou humilie | [CRIM-008](../suites/crim-008-controle-subi.md), [CRIM-021](../suites/crim-021-signaler-agent.md) | Consigner termes et circonstances puis préparer le canal adapté. |
| 22 | Contrôles répétés et ciblés | [CRIM-008](../suites/crim-008-controle-subi.md), [CRIM-021](../suites/crim-021-signaler-agent.md), [DOM-029](../dom-029-discriminations.md) | Tenir une chronologie des contrôles et indices comparables sans discrimination présumée. |
| 23 | « Ouvrez votre coffre, s'il vous plaît. » | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Distinguer consentement sollicité et mesure imposée sur fondement à vérifier. |
| 24 | Fouille systématique après un contrôle d'identité | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Ne déduire aucun pouvoir général de fouille du seul contrôle d'identité. |
| 25 | Palpation assimilée à une fouille | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Qualifier palpation extérieure et fouille corporelle sans les confondre. |
| 26 | Fouille d'un sac sans consentement | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Vérifier cadre et consentement pour le sac sans réponse universelle. |
| 27 | Contrôle d'accès à un événement | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Distinguer refus de consentement et conséquence sur l'accès à l'événement. |
| 28 | Fouille à nu présentée comme systématique | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Rechercher nécessité, cadre et dignité pour une fouille à nu alléguée. |
| 29 | « Laissez-nous entrer pour jeter un œil. » | [CRIM-019](../suites/crim-019-perquisition-domicile.md) | Identifier invitation à entrer et mesure de perquisition annoncée. |
| 30 | Perquisition en enquête préliminaire | [CRIM-019](../suites/crim-019-perquisition-domicile.md) | Vérifier cadre préliminaire, assentiment ou autorisation et exceptions. |
| 31 | Saisie de matériel | [CRIM-019](../suites/crim-019-perquisition-domicile.md), [CRIM-015](../suites/crim-015-interpellation.md) | Lister objets, inventaire, scellés et références manquantes. |
| 32 | « Passez simplement répondre à quelques questions. » | [CRIM-001](../suites/crim-001-lire-convocation.md), [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Identifier qualité et faits annoncés sans conseiller d'ignorer une convocation. |
| 33 | On te présente l'audition libre comme une formalité sans conséquence | [CRIM-001](../suites/crim-001-lire-convocation.md), [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Expliquer l'enjeu procédural à vérifier sans qualifier l'audition de formalité. |
| 34 | On te fait parler sans t'indiquer clairement les faits reprochés | [CRIM-001](../suites/crim-001-lire-convocation.md), [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Rechercher notification des faits et statut au moment des déclarations. |
| 35 | « Vous n'avez pas besoin d'avocat. » | [CRIM-001](../suites/crim-001-lire-convocation.md), [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Vérifier accès à l'avocat selon statut et infraction annoncée. |
| 36 | « Si vous n'avez rien à vous reprocher, répondez. » | [CRIM-001](../suites/crim-001-lire-convocation.md), [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Distinguer identité et déclarations sur les faits, droit au silence selon statut. |
| 37 | On te laisse croire que tu ne peux pas partir | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Vérifier caractère libre ou changement de mesure avant toute possibilité de départ. |
| 38 | Le procès-verbal ne reflète pas tes réponses | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Préparer relecture, rectification et trace du désaccord sur le PV. |
| 39 | On te refuse une copie du PV d'audition libre | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Distinguer règles de copie du PV d'audition et du PV de plainte. |
| 40 | Les policiers minimisent la nécessité d'un avocat | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Préparer une demande explicite d'avocat et les modalités vérifiées. |
| 41 | Tu ne sais pas pourquoi tu es retenu | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Identifier faits, motif de placement et notification des droits disponibles. |
| 42 | Tu es fatigué, malade ou blessé | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Prioriser médecin et transmission utile des besoins de santé. |
| 43 | On exige que tu répondes à toutes les questions | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Vérifier droit au silence et identité sans conseiller de réponse au fond. |
| 44 | On t'invite à renoncer à ton avocat | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Distinguer assistance et renonciation sans promettre une sortie accélérée. |
| 45 | Les enquêteurs rapportent tes propos de manière inexacte | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Relever propos contestés, correction demandée et question à l'avocat. |
| 46 | Tu subis des menaces, humiliations ou pressions | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Prioriser avocat et santé puis conservation factuelle des pressions alléguées. |
| 47 | Tes proches ne sont pas informés | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Vérifier personne à prévenir, demande, restrictions et trace. |
| 48 | Menottage systématique sans justification | [CRIM-002](../suites/crim-002-mesure-en-cours.md) | Documenter risque allégué, contexte et durée du menottage sans nullité présumée. |
| 49 | Usage disproportionné de la force | [CRIM-020](../suites/crim-020-preserver-preuves.md), [CRIM-004](../suites/crim-004-preparer-plainte.md), [CRIM-021](../suites/crim-021-signaler-agent.md) | Prioriser soins, constat et preuves sans qualification définitive des violences. |
| 50 | Coups après maîtrise ou menottage | [CRIM-020](../suites/crim-020-preserver-preuves.md), [CRIM-004](../suites/crim-004-preparer-plainte.md), [CRIM-021](../suites/crim-021-signaler-agent.md) | Reconstituer chronologie avant et après maîtrise avec témoins et images. |
| 51 | Usage contestable de lacrymogène, taser ou LBD | [CRIM-020](../suites/crim-020-preserver-preuves.md), [CRIM-004](../suites/crim-004-preparer-plainte.md), [CRIM-021](../suites/crim-021-signaler-agent.md) | Décrire arme alléguée, distance, contexte, avertissements et blessures sans expertise inventée. |
| 52 | Agent sans identification apparente | [CRIM-021](../suites/crim-021-signaler-agent.md), [CRIM-020](../suites/crim-020-preserver-preuves.md) | Consigner identifiants visibles et exceptions à rechercher sans chercher l'identité privée. |
| 53 | Le policier refuse de donner son nom | [CRIM-021](../suites/crim-021-signaler-agent.md), [CRIM-020](../suites/crim-020-preserver-preuves.md) | Distinguer nom civil, identification professionnelle et unité. |
| 54 | Tutoiement et propos dégradants | [CRIM-021](../suites/crim-021-signaler-agent.md), [CRIM-020](../suites/crim-020-preserver-preuves.md) | Reproduire propos exacts et préparer un signalement factuel. |
| 55 | On t'interdit de filmer une intervention publique | [CRIM-020](../suites/crim-020-preserver-preuves.md) | Distinguer captation, gêne et diffusion avec règles à lire. |
| 56 | Un agent veut supprimer ta vidéo | [CRIM-020](../suites/crim-020-preserver-preuves.md) | Préserver l'original et distinguer demande d'effacement et saisie judiciaire. |
| 57 | Les versions divergent après une intervention | [CRIM-020](../suites/crim-020-preserver-preuves.md) | Tableau des versions, pièces contemporaines et témoins sans départager arbitrairement. |
| 58 | Les enregistrements des caméras-piétons risquent de disparaître | [CRIM-020](../suites/crim-020-preserver-preuves.md) | Préparer demande urgente de conservation distincte d'une demande d'accès. |
| 59 | « Payez, ce sera réglé. » | [CRIM-003](../suites/crim-003-lire-avis-amende.md), [CRIM-005](../suites/crim-005-contester-amende.md) | Vérifier effet d'un paiement au stade établi avant le choix d'une démarche. |
| 60 | Tu contestes mais verses le montant comme paiement | [CRIM-003](../suites/crim-003-lire-avis-amende.md), [CRIM-005](../suites/crim-005-contester-amende.md) | Identifier justificatif de consignation ou de paiement et leurs effets distincts. |
| 61 | Tu signes un procès-verbal | [CRIM-003](../suites/crim-003-lire-avis-amende.md), [CRIM-005](../suites/crim-005-contester-amende.md) | Vérifier effet de signature ou refus sans annulation automatique du PV. |
| 62 | Tu reçois une contravention sans avoir été arrêté | [CRIM-003](../suites/crim-003-lire-avis-amende.md), [CRIM-005](../suites/crim-005-contester-amende.md) | Identifier constatation sans interception et régime de l'avis. |
| 63 | « C'est votre parole contre celle du policier. » | [CRIM-005](../suites/crim-005-contester-amende.md) | Vérifier force probante du PV, régularité et preuves contraires admissibles. |
| 64 | Un radar t'attribue une infraction contestée | [CRIM-005](../suites/crim-005-contester-amende.md) | Séparer demande de cliché et contestation sans suspension présumée. |
| 65 | Tu n'étais pas le conducteur | [CRIM-005](../suites/crim-005-contester-amende.md) | Qualifier responsabilité du titulaire et conducteur réel sans désignation fictive. |
| 66 | Tu vends un véhicule puis reçois ses amendes | [CRIM-005](../suites/crim-005-contester-amende.md) | Rapprocher cession, enregistrement et date d'infraction. |
| 67 | Tu ne reçois jamais le premier avis | [CRIM-003](../suites/crim-003-lire-avis-amende.md), [CRIM-005](../suites/crim-005-contester-amende.md) | Reconstituer envois, réceptions et adresse utile sans irrégularité automatique. |
| 68 | Tu demandes une remise gracieuse au lieu de contester | [CRIM-003](../suites/crim-003-lire-avis-amende.md), [CRIM-005](../suites/crim-005-contester-amende.md) | Séparer remise financière et contestation de l'infraction. |
| 69 | Le dépistage d'alcool est positif | [CRIM-023](../suites/crim-023-controle-routier.md) | Distinguer dépistage alcool et vérification probante. |
| 70 | Tu contestes le résultat d'alcoolémie | [CRIM-023](../suites/crim-023-controle-routier.md) | Vérifier second contrôle, moment, demande et trace dans la procédure. |
| 71 | Dépistage positif aux stupéfiants | [CRIM-023](../suites/crim-023-controle-routier.md) | Identifier prélèvement et possibilité d'expertise selon le stade sans conseil de refus. |
| 72 | Tu attends trop longtemps pour la contre-expertise stupéfiants | [CRIM-023](../suites/crim-023-controle-routier.md) | Rechercher notification, réserve et conditions de demande sans délai repris du texte. |
| 73 | On retient ton permis | [CRIM-023](../suites/crim-023-controle-routier.md) | Lire avis et heure de rétention, puis décisions ultérieures connues. |
| 74 | Tu confonds rétention et suspension | [CRIM-023](../suites/crim-023-controle-routier.md), [DOM-010](../dom-010-administratif.md) | Séparer rétention, suspension administrative, peine judiciaire et points. |
| 75 | Tu penses récupérer automatiquement ton permis après 72 heures | [CRIM-023](../suites/crim-023-controle-routier.md), [DOM-010](../dom-010-administratif.md) | Vérifier suite et restitution sans autorisation de conduire déduite du temps écoulé. |
| 76 | Relevé d'identité pour une contravention | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Qualifier relevé municipal et cadre de la contravention. |
| 77 | Un agent veut procéder à une vérification d'identité au commissariat municipal | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Identifier service et autorité compétente pour une vérification d'identité. |
| 78 | Fouille de sac ou de véhicule | [CRIM-018](../suites/crim-018-controle-en-cours.md), [CRIM-008](../suites/crim-008-controle-subi.md) | Vérifier pouvoirs et contexte de fouille propres à l'agent municipal. |
| 79 | Verbalisation pour stationnement | [CRIM-005](../suites/crim-005-contester-amende.md), [DOM-010](../dom-010-administratif.md) | Rapprocher lieu, horaires, signalisation et arrêté ; FPS à DOM-010. |
| 80 | Usage de caméras-piétons | [CRIM-020](../suites/crim-020-preserver-preuves.md) | Identifier corps, détenteur supposé et demande de conservation des images. |
| 81 | Comportement abusif d'un agent municipal | [CRIM-021](../suites/crim-021-signaler-agent.md) | Préparer canal municipal et Défenseur des droits à vérifier, plainte séparée. |
| 82 | Usage d'armes de force intermédiaire | [CRIM-016](../suites/crim-016-manifestation.md) | Documenter nécessité et proportionnalité à examiner sans jugement sur la force. |
| 83 | Dispersion d'un attroupement | [CRIM-016](../suites/crim-016-manifestation.md) | Relever sommations perçues, contexte et exceptions à rechercher. |
| 84 | Encerclement ou « nasse » | [CRIM-016](../suites/crim-016-manifestation.md) | Décrire durée, danger annoncé, sorties possibles et jurisprudence à rechercher. |
| 85 | Interpellation au sein d'une foule | [CRIM-016](../suites/crim-016-manifestation.md), [CRIM-015](../suites/crim-015-interpellation.md) | Séparer présence dans la foule et faits individuels allégués. |
| 86 | Agents difficilement identifiables | [CRIM-020](../suites/crim-020-preserver-preuves.md), [CRIM-016](../suites/crim-016-manifestation.md) | Documenter unités, positions, véhicules et identification visible. |
| 87 | Images de manifestations contestées | [CRIM-020](../suites/crim-020-preserver-preuves.md), [CRIM-016](../suites/crim-016-manifestation.md) | Préserver séquences complètes, contexte et originaux. |
| 88 | Une plainte est classée sans suite | [CRIM-007](../suites/crim-007-suivre-plainte.md) | Lire motif du classement sans le confondre avec un jugement sur la vérité des faits. |
| 89 | La plainte n'avance pas depuis plusieurs mois | [CRIM-007](../suites/crim-007-suivre-plainte.md) | Vérifier conditions de suite et préalable de plainte avec un avocat, sans délai générique. |
| 90 | Tu n'obtiens pas d'information sur l'enquête | [CRIM-007](../suites/crim-007-suivre-plainte.md) | Préparer demande de suivi au service ou au parquet sans droit d'accès présumé. |
| 91 | Une procédure te met en cause sans condamnation | [CRIM-022](../suites/crim-022-fichier-taj.md) | Distinguer TAJ et casier sans effacement présumé après classement. |
| 92 | Tu découvres une inscription erronée au TAJ | [CRIM-022](../suites/crim-022-fichier-taj.md) | Qualifier accès, rectification ou effacement et préparer la demande adaptée. |
| 93 | La demande d'effacement du TAJ est rejetée | [CRIM-022](../suites/crim-022-fichier-taj.md) | Lire refus ou silence, réception et voie de recours à vérifier sans requête contentieuse. |
| 94 | On te propose une composition pénale | [CRIM-006](../suites/crim-006-lire-acte-poursuite.md) | Lire composition, stade et consentement sollicité ; questions à l'avocat avant choix. |
| 95 | Tu reçois une ordonnance pénale sans audience préalable | [CRIM-006](../suites/crim-006-lire-acte-poursuite.md) | Identifier ordonnance, matière et notification ; opposition à vérifier sans délai calculé. |
| 96 | Une version des faits retenue dans le dossier est contestée | [CRIM-006](../suites/crim-006-lire-acte-poursuite.md), [CRIM-020](../suites/crim-020-preserver-preuves.md) | Rapprocher mentions contestées, récit déclaré et pièces à préserver pour l'avocat. |
| 97 | Tu reçois une décision administrative ou judiciaire incompréhensible | [CRIM-006](../suites/crim-006-lire-acte-poursuite.md), [DOM-010](../dom-010-administratif.md) | Identifier nature, autorité et notification ; administratif à DOM-010, pénal à CRIM-006. |

## Besoins transversaux hors numérotation

| Partie du texte | Propriétaire | Exigence future |
|---|---|---|
| Section 1 — chiffres et rapports | DOM-002 | Contexte déclaré du besoin ; ne pas transformer une enquête déclarative en taux d'illégalité, ni embarquer des chiffres non vérifiés. |
| Section 7 — paiement, contestation et FPS | CRIM-003, CRIM-005 ; DOM-010 pour FPS | Identifier régime, paiement et consignation ; séparer RAPO, paiement, majoration et contentieux du stationnement payant, sans suspension présumée. |
| Section 11 — plainte contre un agent | CRIM-004, CRIM-020, CRIM-021 | Préparer faits, preuves et démarches distinctes selon corps ; signalement, plainte et recours ne se remplacent pas. |
| Section 12 — délais et aide-mémoire | Chaque propriétaire de démarche | Relever acte, régime, point de départ, notification, preuve, exception et source ; réserver toute échéance incertaine, ne pas calculer depuis un délai générique. |
| Section 13 — intervention en cours | CRIM-018, CRIM-002, CRIM-019, CRIM-023 selon mesure | Bloc bref de sécurité et de questions, statut avant droits, avocat si mise en cause, aucune consigne de résistance physique. |
| Section 13 — après les faits et blessures | CRIM-015, CRIM-020, CRIM-004 | Prioriser soins, constats et conservation ; chronologie et originaux, sans altération ni diagnostic. |
| Section 13 — outrage ou rébellion allégués | CRIM-015, CRIM-006 | Avocat ; séparer mention de procédure, déclaration et preuve, sans défense au fond ni version inventée. |

## Réception et échéances

Chaque sortie distingue date du fait, début d'une mesure, émission, envoi, remise, réception déclarée et notification prouvée. Une pièce manquante reste inconnue. Le tableau des délais du texte fourni n'autorise ni durée universelle de conservation des images, ni délai standard pour une procédure pénale, administrative ou spéciale. Prescription, suspension, interruption et effet d'une demande doivent être recherchés séparément. Les stories qui excluent le calcul ou le recours rédigé gardent ces limites et préparent les questions à un avocat.

## Vérification de cette intégration

Le [contrôleur DOM-002](dom-002-controles.py) vérifie structure, dépendances, couverture 1–97, liens des propriétaires et présence des livrables futurs, sans exécuter les skills. La [relecture documentaire](dom-002-verification.md) décrit des parcours fictifs. Ni ces contrôles ni le [relevé](dom-002-resultats.json) ne valident le droit ou la capacité d'un produit à répondre.
