# DOM-006 — Vérification du complément des frictions logement

Relecture documentaire du **16 octobre 2026 (Europe/Paris)**, par le rédacteur.
La [matrice](dom-006-frictions-utilisateurs.md) rattache les 126 points du
[texte utilisateur](../sources/logement-frictions-2026-10-16.txt) et ses sections
non numérotées aux propriétaires du backlog. Douze nouvelles suites sont
proposées ; les onze suites initiales et les cadrages voisins sont complétés.

## Relecture du routage

Ces cas sont des rapprochements documentaires effectués sur le texte et les
stories, sans invocation de skill. Les résultats indiquent le routage et les
distinctions présents dans les documents ; les scénarios métier des stories
restent à exécuter à l'implémentation.

| Cas relu | Pièces ou faits envisagés | Résultat de la relecture |
|---|---|---|
| Entrée puis retenue | État générique, photos, absence d'exemplaire puis devis de peinture | LOG-012 demande copie/complément ; LOG-001 compare vétusté, coût et imputabilité ; LOG-023 garde le retard, sans étendre le calcul de LOG-001. |
| Encadrement et hausse annuelle | Bail, complément et mauvaise série d'indice, source locale manquante | LOG-013 sépare les encadrements et réserve le barème local ; LOG-014 traite clause/indice/DPE. Ni la revue LOG-003 ni l'un des calculs ne valide le loyer entier. |
| Vide et meublé | Contrat meublé sans inventaire, supplément de charges et départ envisagé | LOG-021 qualifie ; LOG-022 examine forfait ; LOG-020 prépare départ ordinaire. Les tranches vides ne sont pas étendues au meublé ; autres régimes restent à découper. |
| Surface | Mesurage du logement loué puis acte de vente d'un lot | LOG-015 garde surface habitable, mention absente et demande datée ; DOM-017 garde Carrez et action de vente, sans échange des délais. |
| Congé et solidarité | Congé reçu pour reprise, protection invoquée, départ d'un colocataire | LOG-017/006 selon vide/meublé ; LOG-018 sépare départ, notification et remplacement dans sa borne vide. Cautionnement locatif au fond reste à découper. |
| Acte et audience | Commandement, paiement repris et accord annoncé avant audience | ENF-001 lit l'acte, LOG-008 rapproche dette, LOG-009 conditions, LOG-010 demande identifiée ; ENF-005 garde l'expulsion. Aucun accord annoncé ne fait disparaître l'audience dans les exigences. |
| Eau et travaux | Facture élevée, fuite et renvoi bailleur/syndic/assureur | DOM-021 qualifie l'abonné et le plafonnement ; LOG-002 la récupération ; LOG-004 la demande au bailleur ; DOM-018 l'équipement commun ; INS-017 cause/dommages/assurance. Aucune convention d'assurance déclarée universelle. |
| AG et caméra | Vote favorable, PV non notifié, caméra de palier | DOM-018 doit découper accès, comptes et recours d'AG séparés. EXIST-003 doit découper le traitement d'images hors travail ; PRV-030 ne couvre pas ce besoin. |
| Passage et entretien | Usage ancien sans titre, conduites annoncées et facture d'entretien | DOM-020 doit distinguer titre/enclave, réseaux, usage et partage des frais (point 91) ; aucune acquisition ni répartition automatique, aucun obstacle conseillé. |
| Permis et achat | Affichage partiel, recours déjà déposé, véranda ancienne et achat en cours | DOM-019 garde recevabilité et notifications propres au recours public ; DOM-017 les documents de vente ; DOM-020 les droits privés. Ni cadastre, permis ni ancienneté ne remplacent les pièces manquantes. |
| Prescription et accord | Lettre, négociation, reconnaissance de dette ou transaction proposées | CTX-030 pour l'action civile dans son champ ; CTX-039 pour la portée transactionnelle ; domaine métier pour forclusion et acte requis. Le simple envoi ou l'amiable ne reçoit aucun effet automatique. |

## Contrôles reproductibles

Le [contrôleur du complément](dom-006-frictions-controles.py) vérifie la copie
du texte si `--source` est fourni, l'ordre et l'unicité des 126 numéros, les
colonnes de la matrice, les liens locaux, les frontmatters et dépendances du
backlog, les 23 propositions LOG, les douze propriétaires de fichiers futurs,
leurs scénarios, les relais et l'absence de plugin logement créé. Il ne
contrôle pas le sens juridique des textes ni les fragments d'ancre Markdown.
Le [relevé daté](dom-006-frictions-resultats.json) conserve les résultats.

Contrôles exécutés avec succès : intégrité de la source jointe (SHA-256
`8c3e4f11161855042888f70f895de6c0c7a325f83a71503f135005ce3a6ef03a`),
matrice, métadonnées/dépendances, suites, liens/relais, absence de plugin,
index du backlog, contrôle des versions, lint de portée des outils des cinq
cookbooks et lecture des 87 fichiers JSON du checkout. Le diff est relu pour
ne retenir que le lot logement. Une copie de préparation contenant HEAD et
les seuls fichiers logement permet de régénérer l'index destiné au commit
sans les ajouts funéraires concurrents ; le relevé précise ce contexte.

```powershell
python -X utf8 backlog/03-nouveaux-domaines/dom-006-annexes/dom-006-frictions-controles.py
python -X utf8 backlog/etat.py --check
python scripts/check-version-bump.py
git diff --check
```

Les contrôles du lot initial DOM-006 attendent exactement onze suites et
leurs anciens chemins de lot. Ils ne sont pas adaptés ni leurs résultats
réécrits pour leur faire accepter ce complément.

## Portée

Intégration documentaire et contrôles structurels du rédacteur ; aucun texte
officiel consulté, montant ou délai validé, skill implémenté/exécuté, paquet
installé, client testé, lecteur indépendant ou résultat métier réel vérifié.
Les durées, seuils et barèmes du texte utilisateur restent des besoins de
recherche ; les renvois aux cadrages non découpés restent des lacunes
explicites. Aucune notification, signature, action matérielle, saisine ou
transmission exécutée. Les modifications funéraires observées en parallèle
sont hors du lot logement et doivent rester hors de son commit.
