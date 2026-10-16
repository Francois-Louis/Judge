# DOM-031 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-031-decoupage-funeraire.md) et les
12 propositions FUN, pour vérifier l'orientation, les pièces à demander et le
résultat attendu. La story interdit de résoudre ces dossiers : aucun délai,
plafond, montant ou droit n'est conclu. Le [relevé machine](dom-031-resultats.json)
consigne séparément les contrôles statiques.

## Dossier fictif P — prestations apparues sans avoir été demandées

- `P-recit` : « On avait demandé une inhumation simple. Sur la facture, il y
  a des soins de conservation et un maître de cérémonie. Personne ne les a
  demandés. »
- `P-pieces` : devis signé par la fille du défunt, sans soins de
  conservation ni maître de cérémonie ; facture comportant ces deux lignes
  en plus ; courriel de l'opérateur évoquant « l'accord donné sur place » ;
  acompte payé par la fille.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `funeral-legal`, FUN-002 ; FUN-001 seulement si la question se pose avant engagement. | — |
| Point d'entrée | Phrase courante « on nous facture des soins que personne n'a demandés » reconnue sans vocabulaire juridique. | — |
| Trois qualités | Signataire du devis : la fille (signature). Personne qui décide : à établir. Personne tenue au paiement : à établir ; l'acompte ne la désigne pas. | Volontés connues ; autres proches. |
| Commande | Deux lignes sans commande écrite retrouvée ; « accord donné sur place » allégué par l'opérateur, noté comme inconnu, ni retenu ni écarté. | Bon de commande complémentaire ou trace écrite côté opérateur ; auteur de l'accord allégué. |
| Tableau | Lignes du devis et de la facture rapprochées ; montants recopiés ; écart présenté comme différence. | — |
| Règles | Forme de la commande et information préalable réservées. | Textes FUN-001 et FUN-002 à lire. |
| Sortie | Tableau, brouillon de demande de justification ou de rectification, sans remboursement annoncé. | — |
| Avertissement | Phrase BASE-013 nommant une association de consommateurs puis le médiateur du secteur. | — |

**Constat :** FUN-002 suffit ; l'opérateur n'est pas présumé abusif, la
prestation n'est pas présumée inutile, l'accord allégué n'est ni transformé
en commande ni écarté.

## Dossier fictif D — proches en désaccord sur une décision

- `D-recit` : « Ma sœur a déjà demandé une crémation aux pompes funèbres.
  Papa m'avait toujours dit qu'il voulait être enterré avec maman. Les
  pompes funèbres ne veulent rien faire tant qu'on n'est pas d'accord. »
- `D-pieces` : aucun écrit du défunt retrouvé ; titre de concession au nom
  de la mère ; devis de crémation non signé ; message de l'opérateur
  suspendant l'organisation ; corps en chambre funéraire.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | FUN-003 en premier ; FUN-007 pour la concession ; FUN-001 pour le devis ensuite. | — |
| Urgence | Corps en attente et organisation suspendue : renfort en tête, avocat à joindre sans attendre ; aucun délai chiffré. | Délais applicables, textes à lire. |
| Volontés | Inhumation : volonté rapportée par le fils, aucun écrit. Crémation : position de la sœur, fondement à préciser. Aucune volonté supposée. | Écrits éventuels, témoins, contrat obsèques. |
| Qui décide | Non désigné : ni l'aîné, ni la première à avoir contacté l'opérateur, ni le titulaire du lien le plus proche n'est présumé décider. | Règle à lire ; désignation éventuelle par le défunt. |
| Concession | Inhumation près de la mère : question au titre (FUN-007), sans droit affirmé. | Titre complet, bénéficiaires désignés. |
| Saisine du juge | Orientation vers un avocat ; aucune story de procédure (point ouvert du découpage). | — |
| Sortie | Tableau des volontés et positions, questions, pièces, interlocuteur ; aucune recommandation de choix. | — |

**Constat :** la sortie organise sans trancher ; aucun proche n'est présumé
de mauvaise foi ; l'urgence est en tête sans délai inventé.

## Dossier fictif R — paiement réclamé, signataires non identifiés

- `R-recit` : « Les pompes funèbres m'envoient une relance pour payer les
  obsèques de mon oncle. Je n'ai rien signé, j'étais juste là le jour du
  rendez-vous avec mes cousins. »
- `R-pieces` : relance nominative avec une échéance ; bon de commande dont
  la signature est illisible et sans nom ; facture adressée « à la famille » ;
  défunt sans enfant, notaire non saisi.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | FUN-004 ; FUN-005 pour les financements ; FUN-002 si le contenu de la facture est discuté. | — |
| Stade | Relance amiable avec échéance alléguée : renfort en tête ; aucun acte de commissaire de justice. | Nature exacte de la relance. |
| Trois qualités | Signataire : inconnu, la présence au rendez-vous ne vaut pas signature. Personne qui décide : sans objet pour la demande. Personne tenue au paiement : à établir, ni le lien de neveu ni la relance nominative ne la fondent. | Copie lisible du bon de commande, identité du signataire selon l'opérateur. |
| Financements | Fonds du défunt → DOM-016 ; contrat obsèques ou capital éventuels → DOM-005 ; aucune prise en charge promise. | Existence de comptes ou de contrats. |
| Succession | Notaire non saisi : orientation DOM-016, sans qualité d'héritier affirmée. | — |
| Sortie | Brouillon demandant la copie des pièces signées et le décompte, sans reconnaissance ni refus de dette. | — |
| Suites | Relance de recouvrement → DOM-003 (ENF-002) ; injonction de payer → DOM-003 (ENF-012). | — |

**Constat :** signataire, personne qui décide et personne tenue au paiement
restent trois questions distinctes ; aucune réponse n'est déduite du lien
familial ; l'opérateur n'est pas présumé abusif ni la personne dispensée de
payer.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| Devis à signer le soir même, corps à l'hôpital | FUN-001 ; renfort en tête sur ce qui doit être décidé maintenant, sans pression ni délai inventé. |
| Contrat obsèques et opérateur réclamant un supplément | FUN-006 ; capital non versé → DOM-005 (INS-011). |
| Facture payée sur le compte du défunt, banque demandant des pièces | DOM-016 pour les comptes ; FUN-002 seulement pour la facture. |
| Capital décès d'un organisme social | DOM-012 ; FUN-005 nomme la piste. |
| Défunt sans ressources ni proches connus | FUN-005 ; commune comme interlocuteur à vérifier ; aucune prise en charge promise. |
| Enfants sollicités alors que la succession est vide | Point ouvert du découpage (DOM-013, DOM-016) ; FUN-005 nomme la question. |
| Décès à l'étranger, rapatriement envisagé | Point ouvert du découpage ; aucune story. |
| Obstacle médico-légal bloquant les obsèques | FUN-008 en tête ; enquête → DOM-002. |
| Défunt sous tutelle, contrat obsèques payé par le tuteur | Pouvoirs → DOM-026 ; prestations → FUN-006. |
| Erreur de gravure sur la tombe | FUN-010. |
| Mairie annonçant la reprise d'une concession | FUN-007 ; recours contre la décision → DOM-010. |
| Un enfant garde l'urne chez lui contre l'avis des autres | FUN-011, puis FUN-003 ; avocat en cas de blocage. |
| Personne voulant écrire ses volontés et léguer sa maison | FUN-009 pour les volontés ; DOM-016 pour le legs. |
| Démarchage d'un opérateur à l'hôpital juste après le décès | FUN-001 ; fait déclaré, sans qualification ; signalement → CONSO-013 si une pratique commerciale est visée. |
| Litige funéraire pendant que funeral-legal n'est pas livré | CONSO-014 : règles générales, règles sectorielles annoncées comme non examinées. |
| Crémation d'un animal de compagnie | DOM-033 ; rien ici. |

## Couverture des critères de la story

| Critère DOM-031 | Où il est traité |
|---|---|
| Stories avec entrées, sortie, pièces, limites et scénarios | Sections dédiées des 12 propositions, contrôlées par le relevé. |
| Partir du problème sans connaître le code | Table des points d'entrée du découpage ; dossiers P, D et R. |
| Références métier, autonomie de paquetage, frontières | Contrat d'installation, références possédées par FUN-001, FUN-003, FUN-005 et FUN-007 ; table des frontières ; ligne de la matrice BASE-003. |
| Signataire, personne qui décide, personne tenue au paiement | Section dédiée du découpage ; fiche des trois qualités dans FUN-001 ; critères de FUN-001, FUN-003, FUN-004, FUN-005 ; dossiers D et R. |
| Pas de présomption contre l'autre partie, pas de promesse | Garde-fous ; critères de toutes les propositions ; constats P, D et R. |
| Implémentations après PILOTE-003, aucune adaptation lancée | PILOTE-003 terminée ; aucun fichier sous `funeral-legal/` ; marketplace inchangé. |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles et textes cités sont des pistes de recherche
issues de la connaissance de l'agent, pas des règles vérifiées. Aucun délai,
plafond ou montant établi, aucun skill créé ou exécuté, aucun paquet
installé, aucun lecteur réel ou indépendant, aucun envoi. Le préalable
PILOTE-003 est satisfait après BASE-011 ; aucune tranche n'est sélectionnée
par ce cadrage.
