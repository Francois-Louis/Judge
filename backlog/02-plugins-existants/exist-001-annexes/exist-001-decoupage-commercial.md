# EXIST-001 — Découpage des contrats commerciaux

Propositions du **16 octobre 2026**, issues de l'[inventaire complet](exist-001-inventaire-commercial.md).
EXIST-001 proposait 18 stories COM, sans adapter de skill. Depuis, COM-001 est
sélectionnée et son orientation est réécrite (`a-verifier`) ; les 22 autres
restent `proposee`. Voir son [bilan propre](../suites/com-001-annexes/com-001-verification.md).

## Condition de lancement et contrat commun

Toutes les suites dépendent d'EXIST-001, PILOTE-003, BASE-005 et BASE-006.
Le [bilan PILOTE-003](../../01-pilote-travail/pilote-003-bilan-pilote.md) est
`terminee` après la recette BASE-011 du 16 octobre 2026. Cela lève le préalable
de bilan, sans sélectionner une extension : H01 complet et lecteur réel restent
des limites de PILOTE-002. COM-001 a depuis été choisie explicitement ; son
résultat, ses sources et sa recette sont tracés séparément. Le présent cadrage
ne lance aucune autre COM.

Chaque story charge la méthode locale BASE-005, conserve l'isolation BASE-008,
et prévoit les couches de recette BASE-006 (structure, paquet détaché, client,
sortie métier, compréhension). Le protocole d'orientation USAGE-001 sert de
contrat de sortie accessible. Une proposition n'est pas une validation juridique.

La lecture d'un document doit rester possible sans profil de grande entreprise :
demander les seuls faits déterminants, sans inventer playbook, approbateur ni
droit applicable. Chaque tranche corrige les blocs de profil/setup qui
empêchent son parcours ; COM-013 porte leur personnalisation complète et
n'est pas un préalable cyclique à toutes les revues.

## Stories et dépendances métier

Les dépendances de ce tableau s'ajoutent au socle commun ci-dessus ; les
orientations vers d'autres domaines n'imposent pas leur installation.

| Story | Résultat borné et fichiers principaux | Dépendances métier |
|---|---|---|
| [COM-001](../suites/com-001-orientation-contrat.md) | Qualifier une demande et orienter un contrat ; `review` | Aucune |
| [COM-002](../suites/com-002-revue-prestation-b2b.md) | Revoir un contrat de prestation B2B français ; `vendor-agreement-review` | COM-001 |
| [COM-003](../suites/com-003-confidentialite-commerciale.md) | Expliquer et trier un engagement de confidentialité commercial ; `nda-review` | COM-001 |
| [COM-004](../suites/com-004-saas-transfrontalier.md) | Revoir une souscription SaaS B2B transfrontalière ; `saas-msa-review` | COM-002 |
| [COM-005](../suites/com-005-chaine-avenants.md) | Tracer une clause ou l'historique d'une chaîne d'avenants ; `amendment-history` | COM-001 |
| [COM-006](../suites/com-006-enregistrer-echeance.md) | Enregistrer une échéance et un calcul traçable ; tracker modes 1/3, YAML, handoffs des revues | COM-001 |
| [COM-007](../suites/com-007-rapport-renouvellements.md) | Produire le rapport d'échéances et fenêtres dépassées ; tracker modes 2/4, watcher | COM-006 |
| [COM-008](../suites/com-008-demande-arbitrage.md) | Préparer une demande d'arbitrage avec état exact ; `escalation-flagger` | COM-002 |
| [COM-009](../suites/com-009-synthese-accessible.md) | Expliquer une revue en une synthèse courte ; `stakeholder-summary` | COM-002, COM-008 |
| [COM-010](../suites/com-010-journal-ecarts.md) | Consigner le contexte d'écarts acceptés sur un accord signé ; `deal-debrief` | COM-002 |
| [COM-011](../suites/com-011-proposer-position.md) | Proposer une évolution commerciale à partir du journal ; `playbook-monitor` étapes 1–4 | COM-010 |
| [COM-012](../suites/com-012-decider-proposition.md) | Décider d'une proposition et appliquer le diff autorisé ; `review-proposals`, monitor étape 5 | COM-011 |
| [COM-013](../suites/com-013-preferences-commerciales.md) | Créer/modifier les préférences commerciales volontaires ; interview, customize, profil | Aucune |
| [COM-014](../suites/com-014-dossier-commercial.md) | Ouvrir/changer/archiver un dossier isolé ; `matter-workspace` | COM-013 |
| [COM-015](../suites/com-015-facture-b2b-impayee.md) | Reconstituer les pièces et le solde d'une facture B2B impayée ; nouveau skill proposé | COM-001 |
| [COM-016](../suites/com-016-frais-penalites.md) | Comparer des frais ou pénalités aux pièces d'un contrat B2B ; nouveau skill proposé | COM-002 |
| [COM-017](../suites/com-017-preparer-rupture.md) | Préparer les questions et pièces avant rupture d'une relation B2B ; nouveau skill proposé | COM-002, COM-005 |
| [COM-018](../suites/com-018-cookbook-renouvellements.md) | Adapter le cookbook de renouvellements au contrat de données local ; six fichiers du cookbook | COM-007, COM-008, COM-009 |
| [COM-019](../suites/com-019-demande-paiement-suspecte.md) | Lire une demande de paiement présentée comme une obligation administrative ; branche ou skill proposé | Aucune |
| [COM-020](../suites/com-020-abonnement-mandat-formalites.md) | Expliquer un abonnement ou mandat lié aux formalités d'entreprise ; branche ou skill proposé | Aucune |
| [COM-021](../suites/com-021-contrat-influence.md) | Lire un contrat de campagne d’influence | Aucune |
| [COM-022](../suites/com-022-rapprocher-prestation-marketing.md) | Rapprocher une prestation marketing et sa facturation | Aucune |
| [COM-023](../suites/com-023-sortie-agence-marketing.md) | Préparer la sortie d’une agence marketing | Aucune |

Le registre peut recevoir une clause fournie sans exiger une revue SaaS entière.
COM-004 peut produire une fiche d'échéance à reprendre manuellement tant que
COM-006 n'est pas adapté ; aucun appel silencieux au tracker hérité. Les
résultats de revue ne prétendent pas avoir produit une escalade ou une synthèse
encore indisponible. COM-018 adapte le chemin distant sans lancer de service,
sans publication et sans imposer le cookbook au plugin autonome.

## Points à revoir et pistes de sources

Ce tableau est un **plan de recherche non vérifié juridiquement**. Il
n'énonce ni validité de clause, ni taux, ni délai légal. Les futurs lots devront
lire les textes et décisions exacts, leur version à la date des faits, leur
champ et leurs transitions, puis documenter l'applicabilité selon BASE-005.
Aucune date de consultation de source externe n'est revendiquée par EXIST-001.

| Question | Pièces et qualification | Sources primaires à rechercher lors de l'implémentation | Porteur |
|---|---|---|---|
| Loi / juge / temps | Parties et établissements, lieu d'exécution, clauses, conclusion/effet/notification, territoire précis dont outre-mer ; clause choisie versus souhait du playbook | Code civil et Code de procédure civile ; Rome I et Bruxelles I bis selon leur champ ; décisions officielles françaises et CJUE utiles | COM-001/002/004/005/017 |
| Responsabilité / garanties | Assiette, dommages exclus, exceptions, cumul des plafonds, assurance, obligation réelle et conséquences ; achat et vente séparés | Code civil, Code de commerce et jurisprudence officielle sur limitations et obligations essentielles, selon la question | COM-002/004/016 |
| Résiliation / rupture | Durée déterminée ou indéterminée, inexécution, mises en demeure, préavis, ancienneté et dépendance de la relation ; non-renouvellement distinct | Code civil, Code de commerce, jurisprudence officielle sur résiliation et rupture des relations commerciales établies | COM-002/007/017 |
| Cession et sous-traitance de prestation | Parties exactes, agrément, chaîne de prestataires, paiement et objet ; ne pas confondre avec sous-traitance de données | Code civil ; loi relative à la sous-traitance si son champ est établi ; règles sectorielles le cas échéant | COM-002/005/017 |
| Preuve et opposabilité | Devis/commande/CGV acceptés, signature, courriels, versions incorporées, ordre de priorité et réception ; fichier final versus acte signé | Code civil, Code de commerce ; règlement eIDAS selon la question et la version ; décisions officielles | COM-002/005/006/015/016 |
| Imprévision / force majeure / prix | Événements, dates, clause d'exclusion ou d'allocation, index et formule ; préférence de prix distincte de la règle | Code civil, Code de commerce et jurisprudence utile, transitions pour les contrats anciens | COM-002/004/016/017 |
| Clauses déséquilibrées | Qualités réelles, contrat négocié/adhésion, soumission et faits ; ne pas assimiler toute concession à un déséquilibre juridique | Régimes pertinents du Code civil et du Code de commerce ; Code de la consommation seulement après qualification ; décisions officielles | COM-002/003/004/016 |
| Confidentialité / secret des affaires | Informations concernées, divulgateur/récepteur, mesures, exceptions, durée et pièces ; propriété et restrictions cachées | Code civil, Code de commerce ; directive sur le secret des affaires et transposition française, jurisprudence utile | COM-003 |
| Données / sortie SaaS / IA | Rôles réels, DPA complet et sa version, sous-traitants ultérieurs/transferts, accès-export-suppression, droits d'usage et politiques incorporées | RGPD, décisions et textes officiels pertinents ; CNIL/CEPD comme orientation à distinguer des textes ; règlement sur les données (Data Act), règlement IA selon champ et calendrier à établir | COM-004, complément privacy/IA sans délégation du résultat principal |
| Paiement / frais / pénalités | Facture, réception/exécution, échéance convenue, paiements/avoirs, montant/devise, clause et calcul | Code civil et Code de commerce ; règles UE sur retards de paiement et transposition à rechercher, sans taux/forfait importé du modèle | COM-015/016 |
| Secret professionnel et partage | Rôle réel des intervenants, auteur, finalité et destinataire ; marquage distinct de la protection effective | Textes français et jurisprudence applicables à la confidentialité des échanges concernés, sans transposition d'« attorney work product » | Chaque tranche pour ses sorties, profil COM-013 |

Les clauses fournies sont des pièces de la relation, pas une source normative.
Légifrance/JO, EUR-Lex/JOUE et décisions officielles sont les voies de recherche
prévues. Si l'accès web échoue, utiliser les voies documentées dans
[BASE-010](../../00-fondations/base-010-acces-sources-officielles.md) et le
[guide d'accès officiel](../../../references/legal-source-access.md), sans API
payante obligatoire ; tracer échecs, lectures réelles et conclusions réservées.

## Frontières et publics

- **Indépendant, artisan, TPE** : revue d'un devis/contrat de prestation en
  tant que client ou fournisseur (COM-002), facture client professionnel
  impayée (COM-015), frais/pénalités réclamés ou contestés (COM-016), préparation
  d'une rupture (COM-017). Sorties utilisables sans GC, CLM ou avocat attitré.
- **Consommation** : déterminer pour chaque acte la qualité des deux parties
  et son objet. Un artisan face à un particulier n'est pas un dossier B2B du
  seul fait de son statut. Orienter vers le futur `consumer-legal`
  ([DOM-001](../../03-nouveaux-domaines/dom-001-consommation.md)), ou le domaine
  sectoriel pertinent ; aucune commande future présentée comme installée.
  Ne pas exclure automatiquement une protection particulière d'un petit
  professionnel sans examiner les faits et le champ du texte.
- **Secteurs** : travaux, logement, agriculture, banque, assurance et télécoms
  gardent leur propriétaire BASE-003 ; le plugin commercial ne s'approprie
  pas tous les litiges ayant un contrat. Relation pouvant être salariée →
  qualification travail distincte, sans rédaction d'une prestation pour l'éluder.
- **Litige et exécution** : la comparaison des pièces B2B reste commerciale ;
  procédure civile/commerciale identifiée → `litigation-legal` à adapter
  (EXIST-006), saisie/titre/exécution → futur domaine
  [DOM-003](../../03-nouveaux-domaines/dom-003-commissaires-justice-execution.md).
  Aucun calcul de prescription/recours par le registre de renouvellement.

Le protocole ne renvoie pas la personne vers une commande indisponible : il
explique les pièces à réunir, la question précise et l'interlocuteur pertinent.
Les sorties attendues et limites ont été relues sur les cas de la
[vérification](exist-001-verification.md), sans exécuter de skill.

## Complément — demandes administratives trompeuses

Les [100 frictions sur les formalités](../exist-002-annexes/exist-002-frictions-utilisateurs.md) ajoutent COM-019 et COM-020, sans implémentation. Le total actuel est 20 stories, dont COM-001 `a-verifier` et 19 `proposee` ; les 18 COM d'EXIST-001 forment le lot historique. Ces nouveaux parcours n'exigent ni COM-002 ni un registre d'échéances pour lire ponctuellement un courrier.

COM-019 distingue demande privée, coût officiel et acte authentique ; COM-020 sépare formalité, abonnement et mandat. La rétractation B2B, la révocation d'un mandat et la résiliation ne sont pas interchangeables. COM-015 peut examiner les pièces d'une facture B2B ciblée ; il ne devient pas un validateur universel des mentions ni de la réforme électronique. Les obligations fiscales et leur calendrier restent chez DOM-011/039. Aucun routage vers ces parcours futurs ne doit être annoncé comme déjà disponible dans COM-001.

## Complément marketing — 16 octobre 2026

La [matrice des 140 frictions](../exist-004-annexes/exist-004-frictions-utilisateurs.md) ajoute COM-021 (contrat d’influence), COM-022 (rapprochement prestation/facture/mesures) et COM-023 (sortie d’agence, comptes et données). Ces parcours ne deviennent pas des revues B2C ; COM-002/016/017 gardent leurs contrats généraux, frais et rupture, COM-019 les demandes de paiement présentées comme obligatoires. Le tableau compte 23 COM : COM-001 reste `a-verifier`, les 22 autres `proposee`. Les relais PI, données et plateformes sont des fiches de questions autonomes, sans plugin voisin imposé.
