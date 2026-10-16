# DOM-008 — Vérification du complément des frictions transports

Relecture documentaire du **16 octobre 2026 (Europe/Paris)** par le rédacteur.
La [matrice](dom-008-frictions-utilisateurs.md) rattache les 128 points du
[texte reçu](../sources/transports-frictions-2026-10-16.txt) et ses sections
calendrier/méthode. Dix suites sont précisées et douze propositions ajoutées.

## Relecture du routage

Rapprochements du texte et des stories, sans invocation de skill. Les
scénarios métier restent à exécuter lors des lots d’implémentation.

| Cas relu | Pièces ou faits envisagés | Résultat documentaire |
|---|---|---|
| Train, correspondance et frais | TER puis TGV, panier unique, carte expirée, attente et taxi | TPT-004 qualifie les contrats/service avant assistance et indemnisation ; TPT-011 les frais du titre ; TPT-012 le PV. Pas de barème TGV automatique sur TER ni taxi garanti. |
| PV et médiation | Valideur défectueux, ticket payé, quittance ou avis majoré | TPT-012 distingue validation, paiement, stade et acte requis. TPT-013 garde le titre/service ; TPT-007 ne remplace pas le circuit PV. Recours pénal/public au fond reste à découper. |
| Dernier bus et abonnement | Service absent, facture de taxi, campagne de dédommagement | TPT-013 compare horaires et frais, puis critères datés de campagne ; aucune indemnisation du taxi déduite de la suppression. |
| Frais aériens et non-embarquement | Bagage cabine, enregistrement, faute de nom, retour annulé après no-show | TPT-014 garde conditions et frais ; TPT-022 isole taxes et redevances du tarif ; TPT-015 qualifie un refus involontaire. Aucun remboursement total ou clause nulle par défaut. |
| Vol avancé et remboursement imposé | Avis de changement, remboursement, nouveau billet et réponse météo | TPT-001/003 qualifient incident et arrivée finale ; distinguent alternatives, choix, causalité, assistance et indemnisation. |
| Bagage aérien | PIR seul, livraison tardive puis dommage constaté | TPT-005 distingue signalement, écrit, réception et régimes de retard/perte/dommage ; plafond distinct de somme automatiquement due. |
| Procédure aérienne récente | Réclamation fermée, médiateur inadéquat et action envisagée | TPT-007 exige vérification du texte et des transitions allégués en 2026 ; CTX-026 n’est pas un circuit de saisine par défaut. Aucune recevabilité ou interruption garantie. |
| Autocar et soute | Court segment d’un long service, arrêt changé et valise disparue | TPT-008 vérifie longueur du service, information et perturbation ; TPT-020 garde preuve de garde, inventaire et régime du bagage selon circonstances. |
| Ferry et véhicule | Tempête, hôtel, bon d’achat et véhicule rayé | TPT-009 sépare effets météo sur chaque obligation ; TPT-021 traite bien, constat et notification. Plainte perturbation, notification dommage et prescription restent distinctes. |
| Taxi et VTC | Forfait aéroport, refus de carte, prix dynamique et non-présentation | TPT-016 qualifie service, lieu, date et consentement ; réglementation taxi distincte du prix VTC. Faux conducteur : sécurité et DOM-002 ; aucune confrontation. |
| Covoiturage et accident | Supplément en espèces, dépose modifiée, activité professionnelle alléguée | TPT-017 garde contrat et acteurs sans régime autocar automatique. DOM-005/035 gardent couverture et dommage, sans assurance universelle promise. |
| Libre-service | Véhicule rendu, course ouverte, photo ambiguë et caution | TPT-018 distingue restitution/clôture, débit/préautorisation et preuve de dommage ; banque garde opération bancaire et assurance garantie. |
| Assistance et fauteuil | Demande tardive, ascenseur en panne et accompagnant imposé | TPT-019 vérifie mode par mode préavis, aide tardive, motifs et exceptions ; fauteuil distinct de bagage ordinaire. DOM-029 garde discrimination au fond. |
| Transport médical | VTC annoncé remboursable, prescription et refus CPAM | DOM-012 reçoit facturation médicale et recours à découper ; TPT-016 ne garantit ni conventionnement ni remboursement. |
| Images et blessure | Chute en station, témoins et caméra proche de l’effacement | DOM-035 garde dommage ; EXIST-003 doit découper accès/conservation hors travail. PRV-030 ne s’étend pas au réseau ; simple demande sans gel automatique. |
| Accord et recours | Bon déjà accepté, transaction et réclamation sans réponse | TPT-007 distingue offre commerciale et droits ; CTX-039 examine transaction civile. Aucun effet automatique sur délais ni signature exécutée. |

## Contrôles reproductibles

Le [contrôleur](dom-008-frictions-controles.py) vérifie numérotation source,
intégrité de copie si `--source` est fourni, couverture des 128 lignes,
frontmatters et dépendances, 22 propositions et tables de découpage,
douze nouveaux skills et références propriétaires, scénarios attendus,
liens locaux, colonnes, format, relais et absence de plugin transports créé.
Il ne vérifie ni le droit, ni les ancres Markdown, ni le résultat d’un skill.
Le [relevé daté](dom-008-frictions-resultats.json) conserve son exécution.

Contrôles exécutés avec succès dans la copie du lot : intégrité de la source
(SHA-256 `ee09d4b8d4c2e97a7e2eb22ca19e481ad618c8bd198d2cb61f378ea21fdf0cbb`),
128 lignes, 22 suites, douze nouveaux skills/références, liens et relais,
index généré, lecture des 80 JSON et portée des outils des cinq cookbooks.
Le contrôle des versions et `git diff --check` passent dans le checkout.
Le diff du lot est relu ; les autres travaux restent hors du commit.

```powershell
python -X utf8 backlog/03-nouveaux-domaines/dom-008-annexes/dom-008-frictions-controles.py
python -X utf8 backlog/etat.py --check
python scripts/check-version-bump.py
python scripts/lint-tool-scope.py
git diff --check
```

Les contrôles du cadrage initial attendent exactement dix suites ; leurs
scripts et relevés ne sont pas réécrits pour accepter cette extension.
Des travaux santé et véhicules évoluent simultanément dans le checkout :
ils restent hors du commit transports. L’index destiné au commit est généré
dans une copie de préparation contenant HEAD et les seuls fichiers du lot ;
l’index de travail continue de refléter les documents présents sur disque.

## Portée

Intégration documentaire, relecture et contrôles structurels du rédacteur ;
aucune source juridique externe consultée, règle ou date du texte utilisateur
validée, implémentation/exécution de skill, recette client, lecture indépendante
ou démarche externe. Les pistes officielles sont des recherches futures,
y compris la réforme procédurale aérienne alléguée. Les cadrages voisins
sans suites spécialisées restent des lacunes explicites dans la matrice.
