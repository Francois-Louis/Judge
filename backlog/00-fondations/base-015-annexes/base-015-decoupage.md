# BASE-015 — Découpage

Stories issues du cadrage, toutes `proposee`. Aucune ne dépend de PISTE ;
aucune ne promet une recherche exhaustive.

| Story | Nature | Résultat borné | Dépend de |
|---|---|---|---|
| [BASE-016](../suites/base-016-methode-decisions-justice.md) | implémentation | Méthode `1.2.0` avec la section 10 proposée, synchronisée dans les onze paquets ; critère du modèle de story. | BASE-015 |
| [TRAV-062](../../01-pilote-travail/suites/trav-062-pistes-jurisprudence-embauche.md) | implémentation | Les deux décisions de `hiring-review-fr.md` lues et fichées ; adresse de l'arrêt de 2017 corrigée. | BASE-016, BASE-014 |
| [BASE-017](../suites/base-017-recette-jurisprudence-runtime.md) | validation | Cinq scénarios observés dans un client isolé sur `hiring-review`. | BASE-016, BASE-011, TRAV-062 |
| [BASE-018](../suites/base-018-lecture-decisions-dila.md) | implémentation | Lecture d'une décision par identifiant dans les fonds DILA, en maintenance ; fonds CAPP ajouté. | BASE-010 |

Ordre conseillé : BASE-016, puis TRAV-062, puis BASE-017. BASE-018 est
indépendante et sert la relecture BASE-014 quand Légifrance refuse l'outil.

Les domaines qui renvoient au « futur cadrage BASE-015 » (DOM-001, VEH-003)
appliqueront la section 10 une fois BASE-016 livrée ; leurs stories ne sont
pas modifiées ici. Les références métier de chaque domaine adaptent leurs
décisions lors de leur propre lot, avec la relecture BASE-014.
