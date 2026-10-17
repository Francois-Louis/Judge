# DOM-016 — Lectures et pistes officielles

Consultations du 17 octobre 2026 (Europe/Paris), agent de maintenance.
Objet : organiser les tâches et recherches futures ; aucun cas réel ni
montant, délai, majorité ou droit individuel déterminés. Les résumés ci-dessous
décrivent seulement l’usage documentaire retenu pour le cadrage.

| Repère et source exacte | Passage effectivement lu / usage | Vérification et applicabilité |
|---|---|---|
| S01 — DILA, [Règlement d’une succession](https://www.service-public.gouv.fr/particuliers/vosdroits/N171?lang=fr) ; voie outil web | Sommaire distinguant option, indivision, partage et questions de preuve. Sert au découpage SUC-001/003/013/020. | `partiel` : index d’information, textes liés non vérifiés. Applicabilité `a-etablir`, aucun dossier. |
| S02 — DILA, [Succession : indivision entre les héritiers](https://www.service-public.gouv.fr/particuliers/vosdroits/F1296), vérification affichée 16 avril 2026 ; voie outil web | Rubriques décisions, conventions, utilisation, fin d’indivision et références. Sert à séparer SUC-017/018/019/020/021 et prévoir textes territoriaux et réformes à vérifier. | `partiel` : fiche d’information lue, code, loi liée de 2026 et transitions non lus. Aucun pouvoir, majorité ou effet de cette loi adopté ; applicabilité `a-etablir`. |
| S03 — DILA, [Preuve de la qualité d’héritier](https://www.service-public.gouv.fr/particuliers/vosdroits/F12697), vérification affichée 1er janvier 2026 ; voie outil web | Attestation, pièces, finalités et acte de notoriété. SUC-013 distingue preuve de qualité, option et opération bancaire ; conditions à examiner au-delà du solde. | `partiel` : guide lu, textes et seuils historiques non contrôlés ; aucun montant repris comme règle. Applicabilité `a-etablir`. |
| S04 — DILA, [Option successorale](https://www.service-public.gouv.fr/particuliers/vosdroits/F1199), vérification affichée 3 avril 2025 ; voie outil web | Rubriques options, dette découverte, sommation, changement d’option et démarches. Sert à séparer SUC-003/004/005/006/008 et leurs échéances. | `partiel` : fiche lue, Code civil, procédure et versions non contrôlés. Aucune option ni durée conseillée ; applicabilité `a-etablir`. |
| S05 — DILA, [FICOBA](https://www.service-public.gouv.fr/particuliers/vosdroits/F2233), vérification affichée 21 juillet 2026 ; voie outil web | Contenu du fichier, absence de solde/opérations et rubrique personne décédée dont le demandeur est héritier. Sert au plan SUC-010, qualité et pièces avant accès. | `partiel` : fiche lue, textes primaires et voie à recontrôler à l’implémentation ; pas de recherche nominative effectuée ni accès garanti. Applicabilité `a-etablir`. |
| S06 — Caisse des Dépôts, [Découvrir Ciclade](https://ciclade.caissedesdepots.fr/decouvrir-ciclade) ; voie outil web, page d’accueil également ouverte | Présentation du service, produits, transfert préalable et résultats négatifs. Distinguer recherche auprès d’un détenteur et fonds transférés ; assurance-vie orientée INS-011. | `partiel` : information opérateur, sans textes, délais de transfert ou instruction individuelle vérifiés. Applicabilité `a-etablir` ; correspondance et restitution non promises. |
| S07 — Règlement (UE) n° 650/2012 du 4 juillet 2012, JOUE L 201 du 27 juillet 2012, p. 107 ; [publication officielle CELLAR](https://publications.europa.eu/resource/celex/32012R0650) | Article premier (champ et exclusions), articles 21/22 (rattachements et choix allégué), 83 (transitions). Sert uniquement à prévoir dans SUC-025 des contrôles distincts de loi, compétence et fiscalité. | `partiel` : publication initiale française récupérée et passages lus ; rectificatifs, consolidation et totalité du contexte non contrôlés. Applicabilité `a-etablir` ; aucun pays ou décès concret analysé. |

## Accès au règlement UE

L’[URL EUR-Lex tentée](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32012R0650)
affiche une restriction d’accès, sans texte exploitable. Le repli BASE-010 a
été exécuté avec `python -X utf8 scripts/legal_sources.py eu 32012R0650
--expect "Article premier"` : EUR-Lex HTTP 202 bloqué à
12:57:09 UTC ; CELLAR HTTP 200 à 12:57:10 UTC, XHTML français, 300350 octets.
URL finale :
[document DOC_1](https://publications.europa.eu/resource/cellar/727c6b77-86fc-4e68-a179-353873a434e3.0017.03/DOC_1).
Empreinte SHA-256 du corps :
`da6ca2bfe61fc8ddd43b1af9783ef9a8fff5393eef013ad1177011611d868e4b`.
La récupération ne certifie ni version consolidée ni applicabilité ; seuls
les passages nommés S07 sont déclarés lus.

## Points restant à rechercher dans les implémentations

- Textes français et versions applicables : tous restent `non-verifie` dans
  ce cadrage. Les codes et formalités du plan sont des pistes à ouvrir.
- Décision constitutionnelle de juin 2026 alléguée dans la matrice bancaire :
  aucune identité ni effet validés ici. SUC-009 devra retrouver la décision
  exacte et lire motifs, dispositif, publication et effets temporels, puis
  les textes bancaires applicables. L’allégation n’est pas une source de droit.
- Réformes de sortie d’indivision, seuils, plafonds et tarifs : aucun effet
  ou montant retenu ; vérifier les textes et dates propres à chaque opération.
- Les sources Justice, notices et formulaires propres aux formalités seront
  sélectionnés dans SUC-003/005/006 selon la qualité, l’acte et le territoire.
- Sources étrangères, conventions, traductions et instruments pertinents :
  à identifier selon les pays et actes, sans présomption liée à la langue.

Ces recherches futures appartiennent aux critères des suites proposées.
Elles ne sont ni déclarées passées ni nécessaires à une consultation de fond
dans ce cadrage, qui ne résout pas les scénarios. [Portée](dom-016-verification.md#portée).
