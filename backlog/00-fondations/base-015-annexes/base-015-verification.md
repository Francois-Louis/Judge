# BASE-015 — Vérification

Scénarios de la story exécutés le 17 octobre 2026 (Europe/Paris) par l'agent
de maintenance, avec les outils web d'une session ordinaire (WebFetch,
WebSearch). Journal : [tentatives S01 à S27](base-015-acces-session.json).

## Cas normal : arrêt de la Cour de cassation sur une clause de non-concurrence

| Étape | Observé |
|---|---|
| Site de la Cour de cassation | Page de décision et recherche Judilibre vides pour l'outil (S04, S05) : repli. |
| Recherche Légifrance par mots | 2 279 résultats, cinq premiers avec identifiants (S02). |
| Ouverture | Cass. soc., 24 janvier 2024, n° 22-20.926, ECLI:FR:CCASS:2024:SO00084, publié au bulletin, cassation partielle (S03). |
| Motifs | Paragraphe 5 de la réponse de la Cour : la violation de la clause prive le salarié de la contrepartie financière, même après la fin de la violation ; paragraphe 7 : application à l'espèce ; dispositif : cassation partielle et renvoi devant la cour d'appel de Douai autrement composée. Extraits littéraux courts restitués par l'outil. |

Fiche obtenue complète selon la proposition 10.2 : statut `verifie` pour ce
passage. Applicabilité à un dossier non évaluée : aucun dossier.

## Cas limite : aucun résultat sur les sites officiels

Recherche Légifrance « "clause de non-concurrence" "trottinette électrique
partagée" "dédit" » : « 0 texte trouvé » (S22). Réponse attendue selon la
proposition 10.5 :

> J'ai cherché une décision sur une clause de dédit liée à une trottinette
> partagée dans Légifrance le 17 octobre 2026 : aucun résultat. Cela ne
> prouve pas qu'il n'en existe pas. La validité de cette clause reste donc à
> confirmer ; pour avancer, lire les règles générales de la clause de
> non-concurrence déjà vérifiées et faire contrôler la clause par un avocat ou
> un juriste en droit du travail.

## Cas limite : seule une analyse doctrinale accessible

| Étape | Observé |
|---|---|
| Recherche web ouverte | Éditeurs privés, syndicat, réseau et blog d'avocats ; aucune publication officielle de décision de cour d'appel (S24). |
| Doctrine lue | Commentaire d'un avocat au barreau de Paris, publié le 23 décembre 2025, sur CA Bordeaux, ch. soc., 9 septembre 2025, n° 23/00380 ; analyse sans texte intégral ni lien officiel (S25). |
| Recherche de la décision | Légifrance par numéro : 0 résultat (S26) ; Judilibre illisible par l'outil (S05). |

Citation attendue : « Selon un commentaire d'un avocat au barreau de Paris
publié le 23 décembre 2025, la cour d'appel de Bordeaux aurait statué le
9 septembre 2025 (n° 23/00380) sur la renonciation à la clause en cas de
dispense de préavis ; je n'ai pas lu la décision. » Statut de la décision :
`non-verifie`.

Contre-exemple utile : l'arrêt Cass. soc., 17 décembre 2025, n° 24-13.585,
cité par la doctrine, est retrouvé sur Légifrance (S27). La conduite
« chercher la décision par son numéro » change donc le statut possible.

## Critères

| Critère | Résultat |
|---|---|
| Sources inventoriées avec un accès réellement testé et daté | [Inventaire](base-015-inventaire-acces.md) : neuf familles de sources, deux voies (outil web, HTTP direct par la [sonde](base-015-sonde.py), [relevé](base-015-acces-http.json)), échecs consignés. |
| Méthode de citation et conduite en cas d'échec écrites pour évolution de BASE-005 | [Proposition de section 10](base-015-methode-jurisprudence.md) : nature des sources, fiche, lecture des motifs, ordre de recherche, huit situations d'échec, formulations. |
| Découpage en stories bornées, sans PISTE | [Découpage](base-015-decoupage.md) : BASE-016, BASE-017, BASE-018, TRAV-062. |
| Aucune mémoire du modèle présentée comme décision lue | Règle 10.1 de la proposition et scénario 5 de BASE-017 ; vérifiée sur la rédaction de la proposition seulement. |

## Contrôles techniques

`python -X utf8 backlog/00-fondations/base-015-annexes/base-015-sonde.py`
(sortie 0, relevé enregistré), JSON valides, `python backlog/etat.py --check`
et `git diff --check`.

## Portée

Les scénarios ont été joués par l'agent de maintenance, pas par un skill
installé : aucun paquet ne porte encore la section 10, et le comportement
d'un skill pendant une réponse reste à observer (BASE-017). Les lectures par
WebFetch passent par le résumé d'un modèle, avec des extraits littéraux
courts ; elles ne sont pas une copie de la décision. Les accès valent pour
le 17 octobre 2026 et pour ces outils ; la voie HTTP directe a été testée
depuis le même poste. Aucune recherche jurisprudentielle exhaustive, aucune
analyse d'applicabilité à un dossier ; les décisions citées servent à tester
les voies, pas à établir une règle de droit.
