# EXIST-002 — Découpage sociétés et opérations

Propositions du **16 octobre 2026**, issues de l'[inventaire complet](exist-002-inventaire-societes.md).
Les 27 stories SOC restent `proposee` : les 26 propositions d'implémentation et le cadrage SOC-027 définissent fichiers, entrées,
résultat, sources à vérifier, exclusions et scénarios. Les cas relus et la
portée des vérifications sont dans la [vérification](exist-002-verification.md).

## Lancement et contrat commun

Toutes les suites d'implémentation dépendent d'EXIST-002, PILOTE-003, BASE-005 et BASE-006.
Le cadrage SOC-027 dépend d'EXIST-002, BASE-003 et BASE-005 ; sa sortie est un découpage.
Le [bilan PILOTE-003](../01-pilote-travail/pilote-003-bilan-pilote.md) est
`terminee` après BASE-011 le 16 octobre 2026. Ce préalable est satisfait ;
H01 complet et lecture indépendante restent des limites consignées dans le
pilote. Le cadrage ne sélectionne aucune extension métier.

Chaque tranche applique l'architecture BASE-003, charge la méthode locale
BASE-005 `1.0.0`, préserve BASE-008 et suit la recette BASE-006 : structure,
paquet détaché, client, résultat métier et compréhension. USAGE-001 fournit
le contrat de sortie accessible : expliquer acte/obligation, inconnues,
pièces et prochaine démarche, sans imposer une équipe juridique à la personne.

SOC-019 porte la personnalisation complète, SOC-020 le contexte d'opération,
SOC-021 le cycle de dossier. Ils ne sont pas préalables à toute lecture :
chaque tranche corrige ses seuls blocs de profil/routage nécessaires. Les
données permanentes sont hors paquet via helper ; les pièces fournies peuvent
être lues ponctuellement sans créer profil ou registre. Aucune lecture de
dossier voisin pour combler une lacune.

Un schéma « à créer » est créé par son lot propriétaire avant utilisation
par un lot dépendant ; un handoff aval indisponible reste une fiche manuelle,
pas un appel au skill hérité. La première tranche crée un parcours autonome
sur sa tâche, sans prétendre adapter toutes les branches du skill.

## Stories et dépendances métier

Les dépendances du tableau s'ajoutent au socle commun. Les orientations vers
d'autres domaines n'imposent pas leur installation.

| Story | Résultat borné | Dépendances métier |
|---|---|---|
| [SOC-001](suites/soc-001-qualifier-decision-sociale.md) | Qualifier l'organe et la modalité d'une décision sociale | Aucune |
| [SOC-002](suites/soc-002-projet-autorisation-bancaire.md) | Préparer un projet d'autorisation bancaire SAS ou SARL | SOC-001 |
| [SOC-003](suites/soc-003-projet-proces-verbal.md) | Préparer le procès-verbal d'une décision sociale documentée | SOC-001 |
| [SOC-004](suites/soc-004-initialiser-formalites.md) | Créer le registre des formalités identifiées d'une société | Aucune |
| [SOC-005](suites/soc-005-preuves-formalites.md) | Rapprocher une preuve de formalité du registre | SOC-004 |
| [SOC-006](suites/soc-006-rapport-formalites.md) | Présenter les échéances et inconnues des formalités suivies | SOC-004, SOC-005 |
| [SOC-007](suites/soc-007-audit-pieces-societes.md) | Repérer les pièces manquantes d'un dossier de société | Aucune |
| [SOC-008](suites/soc-008-grille-diligence.md) | Extraire une grille de diligence traçable sur des contrats | Aucune |
| [SOC-009](suites/soc-009-constats-acquisition.md) | Extraire les constats documentaires d'une acquisition de titres | Aucune |
| [SOC-010](suites/soc-010-annexe-contrats.md) | Préparer une annexe de contrats selon l'accord d'acquisition | SOC-008, SOC-009 |
| [SOC-011](suites/soc-011-construire-checklist-operation.md) | Construire la liste sourcée des conditions et livrables d'une acquisition | Aucune |
| [SOC-012](suites/soc-012-suivi-checklist-operation.md) | Rapprocher les mises à jour et rapporter les points ouverts d'une acquisition | SOC-011, SOC-009 |
| [SOC-013](suites/soc-013-synthese-operation.md) | Expliquer les constats et décisions ouvertes d'une acquisition | SOC-009 |
| [SOC-014](suites/soc-014-plan-post-acquisition.md) | Initialiser le plan des engagements après acquisition | Aucune |
| [SOC-015](suites/soc-015-accords-contrats-operation.md) | Qualifier et suivre les accords tiers sur les contrats d'une opération | SOC-014 |
| [SOC-016](suites/soc-016-rapport-post-acquisition.md) | Mettre à jour et expliquer le suivi des engagements post-acquisition | SOC-014 |
| [SOC-017](suites/soc-017-controle-export-ia.md) | Préparer et contrôler un export d'extraction d'un outil tiers | SOC-008 |
| [SOC-018](suites/soc-018-rapport-nouveautes-vdr.md) | Comparer deux inventaires de data room et préparer le rapport des nouveautés | Aucune |
| [SOC-019](suites/soc-019-preferences-societes.md) | Personnaliser les préférences sociétés sans imposer un profil de grande entreprise | Aucune |
| [SOC-020](suites/soc-020-contexte-operation.md) | Créer le contexte isolé d'une acquisition | Aucune |
| [SOC-021](suites/soc-021-dossier-societes.md) | Isoler et archiver un dossier sociétés ou opération | SOC-020 |
| [SOC-022](suites/soc-022-cookbook-diligence.md) | Adapter le cookbook de grille aux données de diligence traçables | SOC-008, SOC-018 |
| [SOC-023](suites/soc-023-lire-dossier-formalite.md) | Lire le stade et les blocages d'un dossier de formalité de société | Aucune |
| [SOC-024](suites/soc-024-qualifier-modification.md) | Qualifier une modification de société et ses pièces manquantes | Aucune |
| [SOC-025](suites/soc-025-pieces-depot-comptes.md) | Rapprocher les pièces d'un dépôt de comptes et d'une demande de confidentialité | Aucune |
| [SOC-026](suites/soc-026-qualifier-fermeture-solvable.md) | Préparer les questions d'une fermeture volontaire de société | Aucune |
| [SOC-027](suites/soc-027-cadrage-entreprises-difficulte.md) | Découper l'aide aux entreprises en difficulté et ses frontières — cadrage | Aucune |

Répartition des modes et fichiers :

- décisions sociales : SOC-001 qualification, SOC-002 rédaction d'une seule
  autorisation bancaire, SOC-003 PV documenté. Les autres actes restent à
  découper avant rédaction ; pas de « tout consentement courant » implicite.
- entity-compliance : SOC-004 init/schéma, SOC-005 update/import/sweep,
  SOC-006 report/export, SOC-007 audit documentaire sans présumer conformité.
- opération : SOC-009 constats, SOC-010 annexe, SOC-011 construction de
  checklist, SOC-012 rapprochement et rapport, SOC-013 synthèse.
- integration-management : SOC-014 init/plan, SOC-015 lecture et mise à jour
  des accords/contrats, SOC-016 mise à jour des engagements et rapport/export.
  SOC-016 peut lire un instantané SOC-015 adapté ou afficher section non couverte ;
  aucun statut d'accord écrit indépendamment par deux modes.
- corpus : SOC-008 grille native et trois références, SOC-017 export d'outil
  tiers, SOC-018 comparaison d'inventaires, SOC-022 adaptation distante.
  Le plugin reste autonome sans le cookbook ; le cookbook n'est pas déployé.

## Qualification avant modèle

La séquence française à implémenter commence par identité/formes et acte,
pièces à leur date, compétence/pouvoirs, modalités autorisées, informations
et participants requis, puis projet et preuve de décision. La modalité
écrite, l'unanimité ou la présence d'un modèle ancien ne la remplacent pas.

SOC-001 doit distinguer ce qui vient du texte applicable, des statuts,
d'un pacte, d'une délégation, d'une décision antérieure ou d'une préférence.
Un pacte manquant n'est ni réputé inexistant ni substitué aux statuts.
Un doute déterminant réserve le projet dépendant tout en produisant une
liste concrète des pièces/questions.

SAS et SARL reçoivent des branches distinctes ; aucun « board » présumé.
Organe social, associé signataire et tiers cocontractant ne se confondent
pas. Une société étrangère garde son identité et son droit à rechercher ;
la présence de sa mère en France ne lui attribue pas les formalités françaises.

## Plan de recherche — à vérifier lors des implémentations

Ce tableau ne donne ni règle applicable, ni délai, ni majorité légale. Aucune
source juridique externe n'a été consultée par EXIST-002. Les futurs lots
devront rechercher les passages exacts, leur champ, version à la date des
faits et transitions, tracer l'accès et motiver l'applicabilité selon BASE-005.
Les statuts et contrats fournis sont des pièces, distinctes des sources normatives.

| Question | Pièces et faits déterminants | Sources primaires à rechercher | Lots |
|---|---|---|---|
| Compétence et décision | Forme, acte, territoire, statuts et modifications, pactes, associés/droits, pouvoirs, conflits, dates | Code civil, Code de commerce, textes d'application et jurisprudence officielle sur SAS/SARL et l'acte concerné ; ne pas importer DGCL/unanimité de board | SOC-001/002/003/009/011 |
| PV et preuve | Convocation/réception, présence/pouvoirs, votes réels, annexes, signature et conservation | Codes et textes d'application propres à forme/acte ; Code civil et eIDAS si preuve électronique, dans leur champ/version | SOC-002/003/005 |
| Formalités françaises | Événement, exercice, date de décision, identité, destinataire, mandat et reçus | Code de commerce, textes d'application, publications officielles INPI/Guichet unique et registres compétents RNE/RCS/BODACC selon question ; distinguer procédure expliquée et texte | SOC-004/005/006/007 |
| Diligence et information | Titres/actifs, côtés, statuts/pactes/registre titres, PA/annexes, contrats et corpus exclu | Code civil et Code de commerce, jurisprudence officielle ; règles propres aux titres, restrictions et garanties selon structure | SOC-008/009/010/013 |
| Conditions et autorisations | Acquisition réelle, entreprises/activités/pays, critères de contrôle et conditions PA | Codes/textes France/UE, Autorité de la concurrence/Commission, DG Trésor et autorité sectorielle selon question ; textes normatifs et guides séparés | SOC-009/011/012 |
| Cession et contrôle | Structure de l'opération, loi du contrat, définition de contrôle, clause/avenants, accord conditionnel et garant | Code civil/Code de commerce, jurisprudence et instruments de conflit utiles ; droit étranger recherché séparément. Ni clause silencieuse ni cession de titres n'établissent transfert de contrat | SOC-008/009/010/015 |
| Engagements postérieurs | Accord signé ou projet, preuve de réalisation, clauses et dates propres, garantie/séquestre/earn-out | Accord comme source contractuelle ; Code civil/Code de commerce et textes de formalités selon événement ; pas de délai contentieux universel déduit de survival | SOC-014/015/016 |
| Filiale étrangère | Forme/pays, statuts locaux, pouvoirs, registres, activité et pièce réellement transférée | Publication officielle locale et conseil compétent selon question ; instruments UE/internationaux seulement si champ établi ; aucune formalité US importée | SOC-004/007/009/011/014/015 |
| Confidentialité et circulation | Auteur/rôle, objet du document, destinataires et accès réels | Textes et jurisprudence applicables au secret/confidentialité de ces échanges, sans héritage automatique attorney work product | Chaque tranche pour sa sortie ; SOC-019 pour profil |

Prévoir Légifrance/JO, EUR-Lex/JOUE et décisions officielles. En cas d'accès
difficile, suivre les [voies officielles BASE-010](../../references/legal-source-access.md)
et tracer échecs/lectures exactes ; un connecteur payant n'est pas obligatoire.

## Colonnes et contrats de données à conserver

SOC-008 réexamine les 21 colonnes de la référence actuelle, sans supprimer
la traçabilité : parties, nature, effet, durée, reconduction, résiliation,
préavis, contrôle, cession, exclusivité, plafond, indemnisation, loi, litiges,
MFN/prix, minimums, PI, confidentialité, assurances, audit et notifications.
Les ajouts sectoriels US sont retirés des valeurs par défaut ; tout ajout
français exige qualification et source. Ajouter identités, versions/avenants,
juridictions distinctes et état de lecture/vérification.

Contrats à versionner dans leurs lots : cellule (SOC-008), constat (SOC-009),
checklist (SOC-011), formalité (SOC-004), engagement/accord (SOC-014/015),
inventaire (SOC-018), contexte deal/dossier (SOC-020/021). Préserver citations,
localisations, identité de source et états ; sortie neutralisée pour tableur
distincte de la preuve brute. Les fixtures doivent couvrir citation mismatch,
illisible, version remplacée, données contradictoires et reprise partielle.

## Frontières et exclusions

Les contrats B2B courants gardent commercial-legal/EXIST-001. Dans une
opération, corporate porte structure, acte social, diligence et suivi ; la
revue spécialisée travail, PI, données, fiscalité DOM-011 ou réglementation
forme une question complémentaire nommée, pas un domaine entier absorbé.
Un litige identifié relève de son domaine et éventuellement litigation,
sans transformer la checklist en registre de recours.

Les premiers actes sont SAS/SARL ; SA, cotées, capital/financement, fusion,
dissolution et procédure collective ne sont pas implémentés par ces projets. SOC-026 prépare seulement la qualification d'une fermeture ; SOC-027 doit encore découper les difficultés d'entreprise.
Le module Public Company hérité n'a aucun skill : SOC-019 retire ses promesses
US et signale l'absence d'adaptation, sans inventer de workflow AMF/UE.
Aucun identifiant technique ou contenu éditeur n'est modifié ici.

## Complément — formalités des entreprises

La [matrice des 100 frictions](exist-002-frictions-utilisateurs.md) conserve le texte fourni et distingue besoins attribués et tâches encore à découper. SOC-023 à SOC-026 sont quatre propositions d'implémentation ; SOC-027 est un cadrage et ne dépend que d'EXIST-002, BASE-003 et BASE-005. Les autres lots gardent le socle commun et leur recette. Aucun nouveau parcours n'est livré.

SOC-023 lit un dossier sans registre ; SOC-024 qualifie un événement sans rédiger tous les actes ; SOC-025 rapproche les pièces d'un exercice sans tenir les comptes ; SOC-026 qualifie une fermeture envisagée sans conduire la liquidation. Les preuves et échéances peuvent être reportées dans SOC-004/005/006 une fois ces modes adaptés, ou dans une fiche manuelle. Pas de dépendance imposant un registre à toute lecture.

SASU/EURL doivent être reconnues comme formes unipersonnelles dans les branches SAS/SARL, avec leurs pièces et modalités à vérifier ; leur présence ne permet pas d'inventer une assemblée. La création, les changements et la cessation d'EI restent DOM-039. Le droit fiscal est séparé entre DOM-039 (activité courante de l'indépendant) et DOM-011 (sociétés, contrôle et contentieux fiscal). Les difficultés structurelles et leurs frontières restent à cadrer dans SOC-027.
