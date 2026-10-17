# DOM-021 — Sources du cadrage et recherches futures

Lectures du **17 octobre 2026 (Europe/Paris)** par outil de lecture web.
Les lectures ci-dessous servent au découpage ; elles ne constituent pas
un corpus juridique vérifié pour les futurs dossiers. La
[portée du bilan DOM-021](../dom-021-energie-eau.md#bilan-dexécution--17-octobre-2026)
s'applique.

| Référence et nature | Lecture / voie observée | Usage et limite |
|---|---|---|
| [Médiateur national de l'énergie — Les litiges](https://www.energie-mediateur.fr/les-litiges/) ; information institutionnelle | Page ouverte et lue, outil web ; présentation des litiges et orientation vers les conseils. | Repère d'interlocuteur énergie ; ne valide ni compétence sur un dossier, ni recevabilité, ni extension à l'eau. |
| [Service Public — Impayés F20055](https://www.service-public.gouv.fr/particuliers/vosdroits/F20055) ; guide | Page ouverte et lue, outil web ; présentation et sections gaz/électricité, champ logement indiqué. | Justifie de prévoir trois branches d'urgence ; les procédures et protections restent à vérifier dans les textes aux dates utiles. Aucun calendrier repris ici. |
| [Service Public — Surconsommation d'eau F389](https://www.service-public.gouv.fr/particuliers/vosdroits/F389) ; guide | Page ouverte et lue, outil web ; rubriques information, fuite/absence de fuite, compteur et recours. Date de vérification affichée : 9 octobre 2026. | Pièces et branches de UTI-004 ; aucun seuil ni droit au plafonnement validé par cette lecture seule. |
| [CGCT, R. 2224-20-1, version datée issue de la recherche](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000026418286/2026-05-10) ; norme recherchée | Ouverture refusée HTTP 403 ; même refus sur [URL sans date](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000026418286/). Texte non lu. | Statut `inaccessible` pour ces voies ; extrait de moteur non traité comme lecture, version applicable non établie. |
| [CGCT, L. 2224-12-4, lien fourni par F389](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041410387) ; norme recherchée | Clic depuis F389, refus HTTP 403 ; texte non lu. | Statut `inaccessible` pour cette voie ; conditions, champ et versions restent à établir. |

Les échecs n'ont pas arrêté le cadrage : les lectures officielles disponibles
permettent de préparer les tâches et pièces, sans certifier les normes.
Aucune absence de droit ou de source n'est déduite des 403. La prochaine
implémentation reprend les accès officiels et, si nécessaire, les voies
DILA décrites dans le contrat d'accès ; PISTE n'est pas requis.
Ne pas importer les moyens d'accès du dépôt comme dépendance d'exécution.

## Programme de recherche par tâche

| Stories | Sources exactes à ouvrir au lot | Question à vérifier |
|---|---|---|
| UTI-001/002 | Code de la consommation (fourniture énergie/factures), Code de l'énergie, textes de présentation des factures, contrat et grilles ; documentation du gestionnaire pour conversion du gaz. | Périodes, index, conversion, régularisation, imputation ; limites et exceptions, pas de durée de mémoire. |
| UTI-003 | CGCT eau/assainissement, présentation des factures, règlement et délibérations tarifaires du service. | Auteur de chaque ligne, période, unité et tarif applicables. |
| UTI-004 | CGCT L. 2224-12-4, R. 2224-20-1 et dispositions associées d'assainissement ; textes modificatifs, règlement local. | Abonné, information/réception, référence de consommation, fuite et exclusions, attestation, compteur, demande/réponse et effets sur les sommes. |
| UTI-005/006/007 | Code de la consommation (souscription, information, modification et fin des contrats d'énergie), Code de l'énergie ; offre, avis et procédure officielle correspondant à l'événement. | Accord allégué, prix/mensualité, changement, clôture et solde ; dates et champs propres à l'événement. |
| UTI-008/009/010 | CGCT, règles de consommation selon la relation, règlement et décisions tarifaires locales, contrat/demandes. | Ouverture, modification ou clôture de l'eau ; pas de délai d'énergie transposé. |
| UTI-011/012 | Code de l'action sociale et des familles, textes réglementaires d'impayés et protections, Code de l'énergie/consommation, documents de l'opérateur. | Gaz/électricité séparés, résidence et situation, mesure, chronologie, protections légales distinctes d'engagements commerciaux. |
| UTI-013 | Textes de continuité de l'eau et CGCT, règlement ; décisions de justice uniquement si nécessaires et lues. | Auteur/motif/logement, dette distincte de protection sur la fourniture, restriction distincte de suspension. |
| UTI-014 | Textes sectoriels, documentation du gestionnaire, règlement et avis de l'autorité technique/sanitaire selon le service. | Identifier le motif et l'interlocuteur sans diagnostic ni compensation présumée. |

Pour chaque source future : titre et nature, article/passage lu, URL
effective, date et voie, statut de lecture, version à la date des faits,
champ territorial, transitions et exceptions. Un guide est un repère ; le
contrat et le règlement local ne remplacent pas les normes applicables.
La méthode BASE-005 versionnée sera embarquée dans le paquet.
