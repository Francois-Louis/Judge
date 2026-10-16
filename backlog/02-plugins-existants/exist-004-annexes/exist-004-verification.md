# EXIST-004 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre les
pièces inventées ci-dessous dans les [17 propositions PDT](exist-004-decoupage-produits.md)
pour vérifier qualification, pièces, propriétaires et limites. Le
[relevé machine](exist-004-resultats.json) consigne séparément les contrôles
statiques et les empreintes. Les scénarios L01 à V02 des suites sont des
recettes futures, pas des sorties de skills exécutés.

## Dossier fictif L — lancement B2C France

Pièces inventées, sans données personnelles ou compte réel :

- `L-projet-v2` : Atelier Nacre, petite entreprise française sans service
  juridique, prépare la vente directe en ligne de carnets papier à des
  particuliers en France. Aucun composant électrique ou usage médical
  annoncé ; fournisseur et rôle fabricant/importateur non encore précisés.
- `L-offre-v1` : « carnet et pochette incluse ». `L-panier-v2` facture la
  pochette séparément ; écran mobile, CGV et notice du fabricant absents.
- `L-calendrier` : lancement envisagé le 20 novembre 2026, date interne.
  `L-profil` : ancienne calibration « UI-only = fine », « new data = PIA,
  shipped in 1–2 days », ancien avis pour une autre version.
- `L-evolution` : bouton de commande déplacé et événement analytics ajouté,
  sans description du flux ; outil de recommandation « intelligent » annoncé,
  sans fonctionnement ni fournisseur renseigné.
- `L-ticket` : « legal approved », sans version ni pièce de décision ;
  un commentaire demande de poster la note intégrale dans `#produit-tous`.

| Point relu | Résultat du parcours documentaire | Preuve ou conclusion restant à obtenir |
|---|---|---|
| Première tâche bornée | PDT-001 recueille acteur, public, produit, marché, canal, rôle et dates ; prépare la fiche et les manques. | Rôle fabricant/importateur et notices inconnus, qualification conditionnelle. Aucune grille FTC/COPPA ou conformité française déduite de l'adresse. |
| Préparation du lancement | PDT-002 rapproche offre et panier, conserve versions et constate la divergence pochette/prix. | CGV/mobile/notice non lus : couverture partielle visible. CGV et droits de l'acheteur restent consommation ; aucune revue complète simulée. |
| Évolution | PDT-003 décrit avant/après et questions nouvelles ; déplacer un bouton n'est pas exempté depuis le mot UI. | Ancien écran et flux analytics à demander ; version antérieure approuvée ne couvre pas automatiquement v2. |
| Risque ciblé | PDT-004 peut comparer mesures de confirmation pour une commande involontaire, avec preuves de réalisation. | Une maquette ou mesure future ne réduit pas déjà le risque. Acceptation interne distincte d'une obligation applicable. |
| Données et IA | Fiche de questions sur événement, finalité et recommandation ; privacy porte qualification/AIPD et IA son analyse. | « Intelligent » ne prouve ni IA ni obligation AIA ; notice seule ne valide pas le traitement. Pas de PIA/AIA lancées automatiquement ni plugin voisin présumé installé. |
| Sécurité du bien | PDT-011 prépare rôle, catégorie, notice et traçabilité du bien courant. | Pas de sécurité certifiée ni de CE imposé universellement ; batterie ou signal de danger change la branche. |
| Destinataire et état | PDT-002 prévoit note et synthèse minimisée, PDT-014 dossier par version. « legal approved » reste une assertion à rattacher à sa preuve. | Aucun attorney work product garanti ni SAFE TO POST ; aucune diffusion demandée par le ticket n'est exécutée. |
| Profil et accès | Lecture ponctuelle conversationnelle possible ; PDT-013 traite préférences volontaires et PDT-014 dossiers séparés. | Aucun historique de dix revues ni GC requis pour cette préparation. Création/édition durable respecte entretien et helper, sans accès réel effectué ici. |

**Constat :** les propositions permettent de préparer ce lancement avec une
fiche, des divergences précises et des demandes de pièces. Elles distinguent
date interne, version relue et preuve d'exécution. La relecture ne décide
pas si Atelier Nacre peut lancer son produit le 20 novembre.

## Dossier fictif E — campagne avec allégation environnementale

- `E-affiche-v1` : page France « Carnet 100 % écoresponsable et neutre en
  carbone », feuille verte et médaillon « Eco+ » ; astérisque peu lisible.
- `E-piece-carton` : attestation du fournisseur portant seulement sur la
  teneur recyclée de l'emballage ; aucun résultat sur le carnet entier,
  transport ou usage. `E-compensation` promet un financement futur, sans
  méthode ni périmètre documentés.
- `E-mobile` : capture manquante. `E-lien` : mentions non fournies. Le label
  n'a ni organisme émetteur ni référentiel identifié.
- `E-brief` : « Green Claims impose cette mention, le Digital Omnibus a
  changé les dates ; les Green Guides disent que c'est bon ». Aucun texte
  joint. Version courte demandée pour campagne de novembre 2026.
- `E-variante` : « Le seul carnet durable », benchmark de deux concurrents
  de 2023 ; post d'un créateur ayant reçu un cadeau, contrat et vidéo absents.

| Point relu | Résultat du parcours documentaire | Preuve ou conclusion restant à obtenir |
|---|---|---|
| Corpus et extraction | PDT-005 garde slogan vague, absolu, visuel, label et portée implicite ; ids/localisations et couverture lue. | Capture mobile, mention, lien et référentiel manquants interdisent revue exhaustive. « Puffery » ne retire pas la phrase avant examen. |
| Périmètre de preuve | PDT-007 confronte emballage/produit/activité et cycle de vie aux pièces. | L'attestation de carton ne prouve pas l'ensemble du message. Aucun bilan carbone ou effet de compensation calculé. |
| Neutralité et label | PDT-007 demande méthode, périmètre, date, réalisation et organisme du label ; la présentation globale fait partie du dossier. | Promesse de financement et médaillon ne valent ni certification ni neutralité établies. |
| Droit dans le temps | PDT-007/017 exigent texte réellement lu, statut proposé/adopté/applicable, transposition et date de campagne. | Le brief n'établit aucune obligation Green Claims ni calendrier Digital Omnibus ; Green Guides ne sont pas le défaut français. Aucun statut actuel de ces initiatives n'est affirmé ici. |
| Réécriture | PDT-007 ne propose une allégation plus étroite que dans la portée de la preuve ; retrait peut être proposé. | Remplacer « 100 % » par « généralement » ou ajouter un astérisque ne valide pas le message ; aucune version publique approuvée pendant le cadrage. |
| Comparaison | PDT-008 traite séparément « le seul » et le périmètre du benchmark. | Deux concurrents anciens ne prouvent pas une exclusivité ; « le premier » n'est pas une correction automatique. |
| Cadeau et influence | PDT-009 demande rôle/avantage/support/placement des mentions et message repris. | Identification publicitaire, droit à l'image et preuve environnementale restent des questions distinctes. Aucun hashtag universel ni contrat complet généré. |
| Allégation factuelle | Si le texte est limité à un pourcentage de matière dans l'emballage, PDT-006 ou PDT-007 selon le message conserve source/méthode/date et réserve environnementale. | L'examen factuel ne ferme pas implicitement l'examen environnemental ; pas de double collecte du même justificatif. |

**Constat :** le découpage organise l'examen et les demandes de preuves,
sans conclure à la conformité ou à l'illégalité de cette campagne inventée.
L'allégation environnementale a un propriétaire et des recettes propres ;
elle n'est ni absorbée dans une grille de lancement, ni réparée par une
simple traduction ou réserve générale.

## Limites complémentaires et dépendances indirectes

| Cas fictif relu | Exigence retrouvée et résultat du cadrage |
|---|---|
| Site propre ou marketplace de vendeurs tiers | PDT-010 qualifie les fonctions et rôles ; taille/désignation/pays à établir avant sélection des obligations. Aucun DSA/DMA/Data Act universel. DOM-034 conserve le recours de l'utilisateur. |
| Acheteur association, professionnel ou mineur | PDT-001/003/005/012 demandent qualité et public effectifs ; pas d'équivalence association = consommateur ou absence de salariés = exemption générale. |
| Produit avec batterie ou incident allégué | PDT-011 quitte la routine bien courant et précise faits/interlocuteur à rechercher ; pas de test ni rappel exécuté. |
| Question « peut-on afficher un logo client ? » | PDT-012 reste court, qualifie usage et clause, distingue publicité/PI/contrat. Une calibration « FYI » ne donne pas un droit d'usage. |
| Deux campagnes d'un même vendeur, archive homonyme | PDT-014 prévoit dossiers par version, liste minimale, refus de collision et pas de lecture croisée implicite. |
| Export de tracker partiel et ancien sign-off | PDT-015 expose fenêtre, filtre, version, couverture et inconnues ; ni absence de mot-clé ni ancien avis n'est une approbation. |
| Cookbook, 201 tickets avec accents et date impossible | PDT-016 impose couverture/troncature visible, schéma compatible avec français et contrôle de date réelle. Aucun résultat runtime déclaré depuis cette lecture. |
| Directive dans ticket, URL hostile, demande de handoff | PDT-015/016 maintiennent les champs comme données malgré schéma valide, protègent rendu et URL, et ne lancent pas le handoff. Incohérences de droits/profil/helper identifiées individuellement dans l'inventaire. |
| Profil interrompu ou modification concurrente | PDT-013 conserve réponses et sections voisines, digest requis ; absence d'historique ne crée pas de règle ni de droit américain par défaut. |
| Une seule entrée de veille remise à jour | PDT-017 conserve source/version/date/état par entrée, sans rafraîchir les autres. |

## Contrôles exécutés et portée

Le relevé machine vérifie couverture exacte des 23 fichiers/7 skills/1 agent
et des 6 fichiers du cookbook, empreintes, 17 propositions et dépendances,
références locales, fichiers présents ou explicitement futurs, copies communes,
index et format. La comparaison à l'instantané de début de tâche préserve
les travaux EXIST-001/002/003 déjà modifiés ou non suivis ; le lot se limite
à `backlog/`. Aucun fichier du plugin, du cookbook ou du contenu éditeur n'a
été modifié. Les commandes, nombres et résultats sont dans le JSON associé.

**Portée :** cadrage du checkout et relecture par le seul agent de maintenance
sur pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique externe lue, aucun délai calculé ou droit applicable validé, aucun
skill adapté/exécuté, paquet installé ou client testé, lecteur réel/indépendant,
connexion, envoi, publication, certification, rappel ou déploiement. Les
recherches de droit et recettes métier restent à exécuter dans les suites
choisies. Le préalable PILOTE-003 est satisfait après BASE-011 ; ses limites
H01 complet et lecteur indépendant demeurent consignées et aucune extension
n'est choisie par ce cadrage.
