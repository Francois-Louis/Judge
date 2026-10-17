# BASE-015 — Inventaire des sources de jurisprudence et accès testés

Tentatives du **17 octobre 2026** (Europe/Paris), sans compte ni clé API.
Deux voies sont testées, celles dont dispose une session qui exécute un skill :

- **WebFetch / WebSearch**, outils web ordinaires de la session :
  [journal](base-015-acces-session.json), tentatives S01 à S27 ;
- **HTTP direct par Python** (voie Bash, ou outil de maintenance) :
  [sonde](base-015-sonde.py) et son [relevé](base-015-acces-http.json), avec
  état HTTP, adresse finale, taille, empreinte et marqueurs attendus.

Un accès réussi est une observation de transport à une date donnée ; il ne
vaut ni lecture juridique, ni garantie de disponibilité future. WebFetch
restitue la réponse d'un modèle sur la page, avec des citations littérales
courtes (environ 125 caractères observés) et une lecture par tranches de
100 000 caractères.

## Résultat par source

| Source | Contenu | WebFetch / WebSearch | HTTP direct | Usage pendant une réponse |
|---|---|---|---|---|
| **Légifrance JURI** (Cour de cassation, sélection de cours d'appel et de juridictions du fond) | Texte intégral, analyse (titrage, résumé) pour les arrêts publiés, identifiant JURITEXT, ECLI souvent affiché | Recherche par mots et par numéro : résultats avec identifiants (S02, S23, S27) ; zéro résultat affiché comme tel (S22, S26) ; décisions lues avec motifs et dispositif (S01, S03) | HTTP 403 sur la décision et la recherche | **Voie principale** pour la Cour de cassation. |
| **Légifrance CETAT** (Conseil d'État, cours administratives d'appel, sélection de tribunaux administratifs) | Texte intégral, analyse, mentions Lebon, ECLI | Recherche et décision lues (S10, S11) | HTTP 403 | Voie principale pour la juridiction administrative. |
| **Cour de cassation, courdecassation.fr / Judilibre** | Décisions de la Cour et, depuis leur ouverture, des cours d'appel ; communiqués, notes explicatives | Page de décision et recherche vides (S04, S05) | HTTP 200, corps sans texte (JavaScript) | **Inaccessible** en lecture : se replier sur Légifrance. L'API Judilibre passe par PISTE, exclue. |
| **Conseil d'État, ArianeWeb** | Décisions, conclusions, analyses | Décision lue (S08) ; adresses construites à la main en 404 (S06, S09) | HTTP 200, texte présent | Lecture d'une décision dont l'adresse vient d'une recherche ; pas de recherche directe validée. |
| **Conseil constitutionnel** | Décisions DC, QPC, commentaires | Décision lue (S13) ; la recherche ignore la requête (S14) | HTTP 200, texte présent | Lecture d'une décision par son numéro ; recherche par Légifrance ou recherche web restreinte. |
| **CJUE : CURIA, EUR-Lex** | Arrêts, conclusions, ordonnances | CURIA redirigé vers une page vide (S15) ; EUR-Lex vide (S16) | CURIA 200 vide ; EUR-Lex 202 (écran JavaScript) | **Inaccessible** par la session. |
| **CJUE : CELLAR** (Office des publications) | Même document par CELEX | Notice RDF trop volumineuse (S17) ; manifestation française lue par tranches si son adresse est connue (S18) | HTTP 200 XHTML avec `Accept` et `Accept-Language: fra` | Lecture partielle à l'exécution ; voie fiable en maintenance (`legal_sources.py eu <CELEX>`). |
| **Cour EDH : HUDOC** | Arrêts et décisions, versions linguistiques par identifiant | Page vide (S19) ; point de conversion lu jusqu'au dispositif (S20) | HTTP 403 sur la page, la conversion et la requête | Lecture par l'adresse de conversion d'un identifiant `001-…` déjà connu. |
| **Données ouvertes DILA** (CASS, INCA, CAPP, JADE, CONSTIT) | Lots XML quotidiens et stocks complets | Non testé (archives binaires) | Listes HTTP 200 ; derniers lots CASS 30/09/2026, INCA et JADE 16/10/2026, CONSTIT 05/10/2026 | **Maintenance** seulement ; CAPP absent de `legal_sources.py`. |
| **Données ouvertes de la justice administrative** | Décisions des juridictions administratives | Non testé | HTTP 200, page de présentation | Maintenance ; pas d'usage pendant une réponse. |
| **Recherche web** (WebSearch) | Liens et synthèse d'un moteur | Liens officiels réels (S07, S21), doctrine et éditeurs privés (S24) | — | **Piste** pour trouver un numéro ou une adresse ; la synthèse n'est jamais une lecture. |
| **Doctrine, blogs, éditeurs privés** | Commentaires, analyses | Article d'avocat lu (S25) | — | Citée comme doctrine, avec auteur et date ; ne remplace pas la décision. |

## Constats

1. **La voie dépend de l'outil.** Légifrance et HUDOC refusent le client HTTP
   direct (403) mais répondent à WebFetch le même jour ; le Conseil d'État et
   le Conseil constitutionnel répondent aux deux ; CURIA, EUR-Lex et le site de
   la Cour de cassation ne donnent rien de lisible. Le refus Légifrance de la
   recette BASE-011 (H11a) était un refus de permission de l'outil dans le
   scénario, pas un 403 : une session peut aussi perdre l'accès par
   configuration.
2. **Un identifiant ne se devine pas.** Les adresses construites sans
   référence vérifiée (S06, S09, S12) échouent ; l'échec ne prouve rien sur la
   décision. Toute adresse lue vient d'une recherche, d'une référence embarquée
   relue ou d'une pièce.
3. **Une recherche peut mentir par omission.** La recherche du Conseil
   constitutionnel ignore la requête (S14) ; un zéro résultat de Légifrance
   (S22, S26) ne prouve pas l'absence de décision : Légifrance ne diffuse
   qu'une sélection des décisions des juridictions du fond.
4. **La synthèse d'un moteur n'est pas une lecture.** S07 et S21 mêlent moyens,
   motifs et régimes voisins ; seules les adresses sont réutilisables.
5. **Lecture longue.** Une décision de plus de 100 000 caractères demande une
   lecture suivie (offset) pour atteindre le dispositif (S18, S20).
6. **Écart dans une référence livrée.** L'arrêt Cass. soc., 21 septembre 2017,
   n° 16-20.103, noté inaccessible dans `employment-legal/references/hiring-review-fr.md`
   (0.3.2), est retrouvé sur Légifrance (JURITEXT000035616989, S23). Correction
   confiée à [TRAV-062](../../01-pilote-travail/suites/trav-062-pistes-jurisprudence-embauche.md).

## Sources non testées

Juridictions financières, tribunaux des conflits, Tribunal de l'UE (même voie
que la CJUE), bases sectorielles (CNIL, autorités de régulation), décisions
étrangères. Le domaine propriétaire documente ses bases propres, conformément
à la section 3 de la méthode BASE-005.
