# DOU-001 — Journal de recherche de maintenance

19 octobre 2026 (Europe/Paris). Sources de l'Union et pages françaises
officielles. Les résultats de moteur ont servi à trouver les adresses ; ils
ne sont pas retenus comme textes lus. Aucune décision de justice lue ou citée.
[Traces techniques](eu-attempts.json) : URL, statut HTTP, horodatage et
empreinte SHA-256 de chaque reproduction officielle obtenue.

| Source | Voie | Observation et suite |
|---|---|---|
| CDU, règl. (UE) n° 952/2013 | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 200 pour le texte initial et la consolidation du 12.12.2022 ; consolidation 17.01.2025 inexistante (404). SPARQL CELLAR pour les consolidations et actes modificatifs. | Art. 4, 5, 18, 56, 59-61, 70, 77, 172 lus dans la consolidation. Aucun acte modificatif listé après le règl. (UE) 2022/2399. Liste de l'art. 4 mentionnant encore le Royaume-Uni : effet du retrait non tranché, réservé. |
| Règl. (CE) n° 1186/2009 | CELLAR 200, consolidation du 01.07.2026. | Chapitre V supprimé (mention ►M1 règl. 2026/382) ; art. 25-27 lus, hors tranche. |
| Règl. (UE) 2026/382 | CELLAR 200, texte intégral publié au JO L du 18.2.2026. | Art. 1 à 4 et considérants lus : suppression, droit de 3 EUR par article du 1.7.2026 au 1.7.2028 pour IOSS ou envoi postal, tarif commun ailleurs (considérant 6), évaluations mensuelles dès le 1.10.2026. |
| Directive 2006/112/CE | CELLAR 200, consolidation du 14.04.2025 (dernière listée). | Art. 5-7, 30, 60-61, 85-87, 143 § 1 c bis, 369 sexvicies à septvicies ter lus. Transposition française non lue. |
| Règl. délégué (UE) 2015/2446 | Consolidations 01.07.2026 et 25.02.2025 : EUR-Lex 202 puis erreur de transport CELLAR (`ValueError`). | Inaccessible : définitions d'envoi postal et de valeur intrinsèque réservées. |
| Règl. d'exécution (UE) 2026/1200 | CELLAR 200. | Intitulé et considérants 1-4 lus ; dispositif non exploité. |
| Douane, fiche droit de 3 € | Outil web, page mise à jour le 10/07/2026. | Lecture du guide : ligne d'article de même position tarifaire, exclusions B2B et C2C ≤ 45 €, hiérarchie des redevables, non-remboursement hors art. 116 CDU. Guide, pas la règle. |
| Douane, questions-réponses droit de 3 € | Outil web, mise à jour 10/07/2026. | Base de TVA selon le régime ; remboursement limité. Plusieurs questions non traitées par la page (cadeaux, fractionnement). |
| Douane, actualité recodification | Outil web, page du 1er mai 2026. | Entrée en vigueur des trois parties au 1er mai 2026, « à droit constant », tables de concordance sur Légifrance ; numéros de l'ordonnance non donnés. Articles du nouveau code non lus. |
| Ministère de l'Économie, communiqué n° 850 | Outil web, 30 juin 2026. | Taxe petits colis du 1er mars 2026 suspendue au 1er juillet ; redevance européenne de frais de gestion annoncée au 1er novembre 2026. Aucun texte juridique cité ni lu. |
| info.gouv.fr, petits colis | Outil web. | HTTP 403, non lue. |

Aucune clé PISTE utilisée ni demandée. Les lectures sont datées et
intégrées à `dossier-achat-pays-tiers.md 1.0.0` ; elles ne certifient pas le
droit applicable à un envoi futur. Les recherches à reprendre en priorité :
définition d'envoi postal (U5), texte de la taxe nationale et de sa
suspension, texte de la redevance annoncée au 1er novembre 2026, et articles
du Code des douanes recodifié utiles aux tâches suivantes.
