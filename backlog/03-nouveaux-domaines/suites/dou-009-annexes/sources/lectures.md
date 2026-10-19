# DOU-009 — Journal de recherche de maintenance

19 octobre 2026 (Europe/Paris). Sources de l'Union, Journal officiel de la
République française (fonds JORF de la DILA) et page du Sénat. Les résultats
de moteur ont servi à trouver le numéro de l'ordonnance et l'état du projet
de ratification ; ils ne sont pas retenus comme textes lus. Aucune décision
de justice lue ou citée. [Traces techniques](attempts.json) : URL, statut
HTTP, horodatage et empreinte SHA-256 de chaque reproduction obtenue.

| Source | Voie | Observation et suite |
|---|---|---|
| CDU, règl. (UE) n° 952/2013, consolidé au 12.12.2022 | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 200. | Art. 22, 29, 42 à 46, 48, 101 à 103, 108 et 198 lus : droit d'être entendu, décisions sans demande, sanctions, recours non suspensif et sursis, contrôles, notification et prescription de la dette, délai de paiement, mesures sur les marchandises. |
| Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026 | `legal_sources.py eu` : EUR-Lex 202, CELLAR refusé par la borne de 8 Mio du script (`ValueError`). Téléchargement direct de la même ressource CELLAR (200, 29,6 Mo). | Art. 8 (30 jours ; 24 heures pour certaines marchandises non déclarées), 9 et 10 (exceptions) lus. La réserve DOU-001 sur ce règlement est levée pour ces seuls articles ; les définitions d'envoi postal et de valeur intrinsèque n'ont pas été relues. |
| Règl. (UE) n° 608/2013 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200, texte initial. | Art. 17 (notification de la retenue) et 23 (10 jours ouvrables, 3 pour les denrées périssables ; silence pouvant valoir accord à la destruction) lus. Consolidations éventuelles non recherchées. |
| Ordonnance n° 2026-265 et décret n° 2026-266 du 8 avril 2026 (Code des douanes recodifié) | Archive JORF du 11 avril 2026 (200), lue en flux sans extraction ; l'archive du 10 avril au soir ne contient pas le texte. Légifrance non tenté : refus des requêtes scriptées constaté par BASE-010/BASE-018. | Entrée en vigueur au 1er mai 2026 (art. 11 de l'ordonnance ; décret de même date). Articles lus : voir `lecture-acte-douanier.md` (L. 311-1 à L. 311-9, L. 322-1 et 322-2, L. 323-1, L. 323-6 à 323-8, L. 331-1 à 331-8, L. 332-1 à 332-5, L. 421-1, L. 431-1 à L. 433-1, L. 441-1, L. 442-1 et 442-2, L. 443-3, L. 444-1, L. 444-6, L. 611-1, L. 613-1 à 613-4 ; R. 323-2, D. 323-3, R. 331-1, R. 331-2). Version publiée, non consolidée ; R. 331-1 se lit « l'autorité compétente et le directeur régional des douanes ». |
| Sénat, projet de loi n° 836 (2025-2026) | Outil web, page mise à jour le 2 juillet 2026. | Ratification déposée le 1er juillet 2026, procédure accélérée, commission des finances ; aucun vote ni promulgation affiché. Corrections annoncées à surveiller. |

Aucune clé PISTE utilisée ni demandée. Les numéros de l'ancien Code des
douanes (avant le 1er mai 2026) ne sont pas repris dans la référence : un
acte antérieur demande la version applicable à sa date. Les lectures sont
intégrées à `lecture-acte-douanier.md 1.0.0` ; elles ne certifient pas le
droit applicable à un acte réel. À reprendre en priorité : version consolidée
du code après ratification, régime du droit d'être entendu pour les
impositions autres que les droits à l'importation, et consolidations du
règlement 608/2013.
