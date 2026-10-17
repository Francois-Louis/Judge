# Décisions de l'utilisateur — 17 octobre 2026

## Relecture et clôture des stories

L'utilisateur relit lui-même tous les livrables. Les stories ouvertes
uniquement pour attendre une relecture peuvent être clôturées. Cette règle
est mémorisée dans [AGENTS.md](../AGENTS.md) et [CLAUDE.md](../CLAUDE.md) et
s'applique aussi aux prochaines stories.

La prise en charge inclut la relecture humaine, juridique, indépendante et
par un lecteur non juriste. Elle ne constitue pas une preuve de relecture
effectuée ni de compréhension observée. Les résultats et limites des
recettes restent consignés ; les défauts connus et tests non exécutés
restent à traiter.

| Story | Application de la décision |
|---|---|
| [TRAV-001](01-pilote-travail/suites/trav-001-qualification-relation.md) | `terminee` : seule restait la reformulation par un lecteur non juriste. Relecture prise en charge par l'utilisateur, compréhension non observée. |
| COM-001, CONSO-001, CRIM-001, ENF-001, BNK-001, INS-001, FUN-001 | Restent `a-verifier` : invocations ou scénarios client non exécutés, bloqués ou corrections non réexécutées, en plus de la relecture. |
| BASE-008 | Reste `en-cours` : cycle du hub et liens symboliques réels encore à recetter. |
| BASE-017 | Reste `en-cours` : défauts observés et rejeu S2 à S4 attendu dans BASE-019 ; maintien ouvert déjà décidé par l'utilisateur. |

Le tableau [ETAT.md](ETAT.md) est régénéré après la clôture de TRAV-001.
