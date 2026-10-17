<!-- Added by Judge FR/UE for COM-001, 2026-10-16. Modified for BASE-013, 2026-10-17. -->

# Orientation d'une demande contractuelle — 1.1.0

Référence métier locale de `review`, France/UE. Reprend USAGE-001 `1.0.0`
(15 octobre 2026) et les frontières BASE-003 sans dépendre du backlog à
l'exécution. Charger [la méthode locale BASE-005](shared/research-citation-method.md).
Cette orientation ne réalise ni revue des clauses ni procédure.

## Décider à partir des faits

Recueillir progressivement objectif, qualité/rôle des **deux** parties pour
l'acte, usage réel, engagements et exécution, pays/territoires précis,
établissements, conclusion/effet/notification, loi et juge indiqués. Métier
habituel, langue, devise et titre ne suffisent pas. Sans pièce, une déclaration
attribuée et une question ciblée permettent de commencer. « Non fourni » ne
signifie pas « absent du contrat ».

| Situation réelle | Domaine principal et limite | Préparation utile / interlocuteur |
|---|---|---|
| Prestation courante entre professionnels pour leur activité | Commercial ; achat si la personne reçoit la prestation, vente si elle la fournit. Qualification juridique conditionnelle si faits/sources manquent. | Contrat/devis/commande, CGV acceptées et versions, engagements et paiements des deux parties ; cocontractant pour les pièces, conseil en contrats pour la revue. |
| Particulier achetant pour un usage privé, sans secteur spécial | Consommation ; futur `consumer-legal` proposé, non disponible ici. | Commande, usage, conditions et échanges utiles ; vendeur ou conseil en consommation. |
| Artisan facturant un particulier pour des travaux dans son logement | Construction/travaux avec question de consommation ; futur `construction-legal` proposé, non disponible. Le statut de l'artisan ne rend pas l'acte B2B. | Devis accepté, descriptif, factures, acomptes, réception/réserves selon la demande ; client/entrepreneur pour les faits, conseil en construction pour le droit. |
| Logement, bail rural, crédit/paiement bancaire, assurance ou abonnement télécom | Domaine sectoriel : logement, agriculture, banque, assurance, télécoms ; domaines proposés, aucune commande annoncée. | Bail/décompte, acte bancaire, police/refus ou contrat opérateur selon la question ; bailleur, banque, assureur ou opérateur, puis conseil du secteur. |
| « Prestation » avec travail dirigé, horaires imposés ou contrôle réel | Emploi possible à qualifier ; ne pas rédiger une prestation pour contourner la question. | Conditions réelles, instructions et contrat ; conseil en droit du travail. `employment-legal` existe, mais sa revue d'embauche privée en France est un pilote borné, pas une requalification validée ; installation à vérifier. |
| Désaccord, facture ou relance sans procédure identifiée | Le domaine du contrat conserve le fond ; le désaccord seul ne déclenche pas le contentieux. | Contrat, facture, exécution, paiements/avoirs et échanges ; cocontractant ou conseil du fond. |
| Assignation, décision ou procédure civile/commerciale identifiée | Tâche procédurale distincte ; `litigation-legal` existe mais reste hérité à adapter. | Acte complet, preuve de notification et dates, juridiction ; conseil chargé de la procédure rapidement si date annoncée. |
| Titre, saisie ou acte d'exécution allégué | Exécution, futur `enforcement-legal` proposé ; conserver le fond chez son domaine. Un commissaire de justice peut aussi émettre une simple relance : qualifier l'acte. | Acte, titre mentionné, décompte et notification ; émetteur/commissaire de justice ou conseil compétent pour identifier l'acte et la suite. Aucun acte exécuté ici. |
| Convocation par la police ou la gendarmerie, plainte ou poursuite pénale liée au contrat | Pénal, futur `criminal-legal` proposé, non disponible ; le volet contractuel reste une question distincte. | Convocation complète, qualité annoncée et date ; renfort en tête ; avocat à contacter rapidement, éventuellement pénaliste. L'officier de police judiciaire renseigne sur la convocation : c'est une autorité, pas un conseil. |
| Frais, honoraires ou acte d'un notaire, avocat, commissaire de justice ou expert-comptable | Professionnels du droit et du chiffre, futur `professional-services-legal` proposé ; le fond du dossier garde son domaine. | Décompte ou facture, convention, acte et échanges ; le professionnel concerné pour le détail, puis l'instance de sa profession ou un médiateur à identifier. Avocat seulement en cas de procédure ou de contestation de la validité de l'acte. |

Ne pas exclure automatiquement toute protection particulière d'un petit
professionnel. Selon les faits, demander objet par rapport à l'activité,
effectif et circonstances de conclusion, puis vérifier le texte précis (piste
L221-3 ci-dessous). Usage mixte, personne morale hors activité et objet incertain
restent à établir, sans B2B par défaut.

Un DPA (accord sur les données personnelles), un SLA (niveau de service) ou
une annexe IA ne change pas automatiquement le domaine principal. Identifier
le complément et ses pièces : rôles/traitements pour les données, mesures et
exclusions pour le service. Aucune revue de ces annexes réputée effectuée,
aucun dossier envoyé à un autre plugin ou service.

La dernière colonne fournit l'interlocuteur de la fiche, selon la section 8 de
la méthode BASE-005 `1.2.0` : « conseil » désigne un avocat ou un juriste du
domaine nommé ; l'émetteur d'un acte, le cocontractant ou une autorité
renseignent sans être le conseil de la personne.

## Tâches et disponibilité — état livré au 16 octobre 2026

Une future adaptation met à jour sa ligne après vérification du bilan. La
présence d'un fichier ne prouve pas son adaptation. Aucun appel automatique.

| Besoin / pièces de repérage | Tâche visée et état réel | Sortie possible maintenant |
|---|---|---|
| Qualifier un contrat ou un récit | `review` — orientation COM-001 réécrite ; validation client/utilisateur distincte de la structure. | Fiche d'orientation et questions utiles. |
| Prestation B2B ; contrat, devis, CGV | `vendor-agreement-review` — hérité non adapté, COM-002 proposé. | Achat/vente et pièces pour une future revue. |
| Engagement principal de confidentialité ; informations, divulgateur/récepteur | `nda-review` — hérité non adapté, COM-003 proposé. Une clause confidentielle d'un MSA ne suffit pas. | Qui donne/reçoit quelles informations, obligations supplémentaires à examiner ; aucun feu vert par couleur. |
| SaaS/abonnement ; commande, récurrence, SLA, DPA, politiques incorporées | `saas-msa-review` — hérité non adapté, COM-004 proposé ; sa dépendance à la revue générale reste non adaptée. | Abonnement et pièces identifiés ; aucun lancement de surcouche/tracker. |
| Avenant/historique ; base et chaîne signée | `amendment-history` — hérité non adapté, COM-005 proposé. | Inventaire des dates et versions ; pas de clause applicable déduite du nom de fichier. |
| Échéance/reconduction ; durée, notification, preuve | `renewal-tracker` — hérité non adapté, COM-006/007 proposés ; agent/cookbook non adaptés (COM-018). | Date déclarée et clauses à vérifier ; aucune inscription/alerte active ni calcul de délai légal. |
| Facture impayée / frais ou pénalités | COM-015/016 — tâches proposées, aucun nouveau skill livré. | Facture, exécution, paiements/avoirs, clause, montant/devise et contestation ; pas de pénalité/prescription inventée. |
| Rupture d'une relation | COM-017 — tâche proposée, aucun nouveau skill livré. | Contrats/avenants, ancienneté, commandes, notifications et objectif ; aucun préavis universel ni courrier envoyé. |

Escalade, synthèse, journal et préférences complètes restent hérités
(COM-008 à COM-014). Ne pas les appeler pour terminer l'orientation. Sans
branche adaptée : « Je peux préparer les faits et les pièces pour cette revue ;
cette tâche n'est pas encore adaptée dans ce paquet. » Préciser la question au
cocontractant/professionnel, sans installation ni avocat attitré obligatoire.

## Loi applicable, juge et souhait : trois champs

- **Clause observée** : fichier/passage de loi choisie, juridiction ou arbitrage ;
  distinguer projet, accord signé et annexe manquante.
- **Hypothèse juridique** : établir séparément loi applicable et compétence,
  avec champs matériel, personnel, territorial et temporel. Rome I traite la loi
  des obligations contractuelles en situation de conflit ; Bruxelles I bis la
  compétence et la circulation des décisions civiles et commerciales. Aucun ne
  s'applique à tout contrat au seul motif qu'il est français. Vérifier règles
  internes/internationales utiles, exclusions, régimes protecteurs et territoires,
  notamment outre-mer. Une clause ne prouve pas sa validité. [R1, R2]
- **Préférence déclarée** : « je souhaite négocier le droit français » reste
  un souhait, même au profil. Aucun pays, tribunal, seuil ou approbateur par
  défaut ; les exemples du modèle ne sont pas des réponses.

## Sources de cadrage et limites

Lectures de maintenance du **16 octobre 2026 (Europe/Paris)**. Ces repères ne
vérifient pas un futur dossier : recontrôler version et applicabilité avant
chaque conclusion déterminante. Les consolidations sont documentaires ;
publication, modifications et transitions restent à contrôler selon le cas.
Légifrance/JO et EUR-Lex/JOUE sont les voies publiques, sans abonnement PISTE
requis. En cas d'échec EUR-Lex, CELLAR de l'Office des publications est une
alternative officielle. DILA propose des archives XML publiques, mais un lot
quotidien ne constitue pas un corpus complet. Sans texte accessible, tracer
l'obstacle réel et réserver la conclusion ; ne pas inventer un accès alternatif.

| Repère / nature | Accès, version, passage et état documentaire | Applicabilité |
|---|---|---|
| R1 — Règlement (CE) n° 593/2008 du 17 juin 2008, Rome I, JO L 177 du 4 juillet 2008, p. 6 ; texte normatif UE | [Consolidation française CELEX 02008R0593-20080724](https://publications.europa.eu/resource/celex/02008R0593-20080724), CELLAR après écran JavaScript EUR-Lex. Art. 1–4, 6, 8–9, 28–29 et rectificatif C1 indiqué : lus le 16/10/2026 ; `verifie` pour ces passages/version, pas pour toutes les évolutions. | `conditionnelle` : conflit, matière, territoires, parties et dates à vérifier. Choix et absence de choix distincts ; consommation/travail et règles impératives demandent un examen propre. Art. 28 rectifié : contrats conclus à compter du 17/12/2009 ; art. 29 distingue entrée en vigueur/application. Contrat antérieur : régime à rechercher. |
| R2 — Règlement (UE) n° 1215/2012 du 12 décembre 2012, Bruxelles I bis, JO L 351 du 20 décembre 2012, p. 1 ; texte normatif UE | [Consolidation française CELEX 02012R1215-20150226](https://publications.europa.eu/resource/celex/02012R1215-20150226), CELLAR après écran JavaScript EUR-Lex. Art. 1, 4, 6, 17–19, 25, 66, 81 : lus le 16/10/2026 ; `verifie` pour ces passages/version seulement. | `conditionnelle` : matière, domiciles, juridiction, régimes spéciaux et date procédurale à vérifier. Art. 66 : régime à partir du 10/01/2015, maintien prévu pour certaines décisions antérieures. Art. 81 distingue application/entrée en vigueur. La date du contrat ne suffit pas. |
| F1 — Code de la consommation, article liminaire, 1°–3° ; piste normative française LEGIARTI000049464063 | [Légifrance tenté](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049464063) le 16/10/2026 : 403, contenu non lu ; `inaccessible`. Aucune consultation réussie/version applicable certifiée. | `a-etablir` : qualité de chaque partie pour l'acte ; vérifier définition/version à la date des faits. Aucun statut juridique définitif déduit du métier. |
| F2 — Code de la consommation, L221-3 ; piste normative française LEGIARTI000032226882 | [Légifrance tenté](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882) le 16/10/2026 : 403, contenu non lu ; `inaccessible`. Aucune reproduction officielle alternative lue dans ce lot. | `a-etablir` : conditions/exclusions à rechercher avant d'écarter/accorder une protection au petit professionnel ; aucune durée de rétractation ni protection affirmée ici. |

Conserver pièces lues, passages, tentatives/consultations réelles et raisons
des réserves. Un récit peut justifier une **orientation factuelle conditionnelle**
même lorsque F1/F2 reste inaccessible. Aucune règle étrangère de remplacement.
