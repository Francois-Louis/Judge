# DOM-005 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-005-decoupage-assurance.md) et les
11 propositions INS, pour vérifier le routage et les informations à demander.
La story interdit de résoudre ces consultations : aucun délai, montant ou
droit n'est conclu. Le [relevé machine](dom-005-resultats.json) consigne
séparément les contrôles statiques.

## Dossier fictif E — refus fondé sur une exclusion citée

- `E-refus` : dégât des eaux dans une salle de bains ; « refus : exclusion
  pour défaut d'entretien, article 7.3 des conditions générales ».
- `E-cg` : conditions générales version 2019 fournies ; contrat souscrit en
  2022 ; conditions particulières non fournies.
- `E-recit` : fuite d'un joint, constatée par un plombier dont la facture
  est disponible ; un voisin du dessous a aussi subi des dégâts.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `insurance-legal`, INS-001. | Courrier complet. |
| Catégorie | Exclusion invoquée, distinguée d'une absence de garantie, d'une déchéance et d'une nullité. | Mentions et conditions de validité d'une exclusion : pistes L112-4 et L113-1 à lire, aucune conclusion. |
| Version | Version 2019 ne prouve pas la version en vigueur en 2022 ni à la date du sinistre. | Conditions générales et particulières applicables. |
| Faits | Facture du plombier et nature de la fuite rattachées à la question de l'entretien. | Ce que la clause entend par « défaut d'entretien ». |
| Voisin | Dommages du voisin : question de responsabilité civile, distincte (garantie RC de l'assuré ici, responsabilité DOM-035 ou DOM-018 selon l'immeuble). | — |
| Sortie | Brouillon de demande d'explication et de réexamen ; médiation (INS-005) ensuite. | — |

**Constat :** INS-001 suffit pour une réponse utile qui nomme la catégorie
invoquée sans la valider ni la rejeter.

## Dossier fictif C — sinistre avec conditions particulières manquantes

- `C-vol` : cambriolage ; plainte déposée, récépissé disponible.
- `C-pieces` : conditions générales seules ; conditions particulières perdues ;
  l'assureur demande des justificatifs de valeur.
- `C-recit` : « je crois avoir pris l'option objets de valeur ».

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâches | INS-004 pour lire la garantie ; INS-002 si la déclaration est à compléter ; INS-001 si un refus arrive. | Copie des conditions particulières à demander à l'assureur ou à l'intermédiaire. |
| Option déclarée | « Option objets de valeur » notée comme déclaration. | Garanties souscrites, plafonds, franchises, conditions de protection. |
| Verdict | Aucune réponse « couvert » sur les seules conditions générales. | — |
| Pièces | Récépissé de plainte, factures, photos, attestations de valeur. | Délai de déclaration propre au vol : texte et contrat à lire. |
| Voisins | Plainte : DOM-002, déjà faite. | — |

**Constat :** la pièce manquante est demandée avant toute lecture des
plafonds. Le cadrage ne dit pas si le vol est garanti.

## Dossier fictif X — désaccord sur le montant d'une expertise

- `X-rapport` : incendie de cuisine ; l'expert de l'assureur retient
  6 200 €, vétusté déduite.
- `X-devis` : deux devis de 10 900 € et 11 400 €.
- `X-contrat` : option « valeur à neuf » mentionnée dans les conditions
  particulières ; clause d'expertise contradictoire dans les conditions
  générales.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | INS-003. | Rapport complet poste par poste. |
| Comparaison | Tableau poste/expert/devis/clause ; vétusté et option « valeur à neuf » rapprochées. | Conditions de l'option (délai de reconstruction, plafond) à lire. |
| Options | Contre-expertise et expertise contradictoire à vérifier selon la clause ; honoraires d'expert à vérifier au contrat. | Aucun recours présenté comme acquis. |
| Montants | Recopiés ; aucun recalcul ; un devis n'est pas la valeur due. | — |
| Garantie | Poste écarté comme « non garanti » → INS-001. | — |

**Constat :** chiffrage et garantie sont séparés. Les montants sont des
données fictives recopiées ; aucun n'est déclaré dû.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| Refus de l'assurance emprunteur après un arrêt de travail | INS-008 ; crédit → DOM-004. |
| Mutuelle refusant des lunettes | INS-009 ; part de l'assurance maladie → DOM-012. |
| Fissures après travaux, dommages-ouvrage | INS-010 ; responsabilité des constructeurs → DOM-015. |
| « Garantie casse » vendue avec un téléphone, émise par un assureur | INS-001 ; même document émis par le vendeur → DOM-001. |
| Annulation de voyage | INS-001 pour l'assurance ; transporteur → DOM-008. |
| Victime blessée dans un accident de voiture, offre de l'assureur adverse | Point ouvert du découpage ; préjudice corporel → DOM-035. Tranché le 16 octobre 2026 : DOM-035. |
| Bénéficiaire d'une assurance-vie après un décès | INS-011 ; succession → DOM-016. |
| Assureur opposant une prescription | Question, sans calcul (INS-001, INS-005). |
| « Ajoutons l'ordinateur à la déclaration » | Refus d'aider une déclaration inexacte (INS-002). |
| Refus de l'assurance responsabilité civile professionnelle d'un artisan | INS-001 avec qualification professionnelle ; client → DOM-015. |

## Couverture des critères de la story

| Critère DOM-005 | Où il est traité |
|---|---|
| Plugin propre et frontières | Découpage, sections plugin, garde-fous et frontières ; ligne mise à jour dans la matrice BASE-003. |
| Tâches hiérarchisées, premier skill borné | Rangs 1 à 4 ; inclus et exclus d'INS-001. |
| Références, pièces, sortie, scénarios par story | Sections dédiées des 11 propositions, contrôlées par le relevé. |
| Installation seule, pas d'agent ni connecteur par principe | Contrat d'installation du découpage ; aucun accès à un espace client. |
| Implémentations non lancées | Aucun fichier sous `insurance-legal/` ; marketplace inchangé. |
| Distinctions demandées par la story | Absence de garantie, exclusion, déchéance et nullité séparées ; régimes auto, construction, santé et emprunteur isolés ; garantie séparée de la responsabilité des intervenants (DOM-015, DOM-023, DOM-007, DOM-035). |

## Complément — intégration des frictions assurance

La [matrice des 90 points](dom-005-frictions-utilisateurs.md) reprend le
texte utilisateur archivé. Le découpage courant comporte 21 propositions ;
les mentions des 11 propositions ci-dessus décrivent le cadrage initial.
INS-012 provient du complément bancaire ; INS-013 à INS-021 de ce complément.
Les anciennes modifications, notamment INS-008/INS-011, sont conservées.

Relecture documentaire par l'agent de maintenance, sans exécution métier :

| Situation du texte | Attribution relue | Réserve conservée |
|---|---|---|
| Pièces redemandées et quittance de solde avec paiement partiel | INS-013 | Complétude, nature du paiement et portée de la signature à établir. |
| Malus et hausse commerciale concomitants | INS-014 | Coefficient, responsabilité alléguée et tarif séparés ; aucun recalcul. |
| Livraison professionnelle avec voiture privée | INS-015 ; INS-019 pour la garantie | Questions initiales et usage réel, sans fausse déclaration intentionnelle déduite. |
| Appel commercial, consentement contesté et réforme alléguée | INS-016 | Texte, version, transition et preuve de consentement à rechercher. |
| Voisin, bailleur et syndic se renvoient la fuite | INS-017 | Gestionnaire à confirmer ; IRSI non tenue pour opposable universellement. |
| Sécheresse et arrêté pour une autre période | INS-018, INS-021 | Commune, phénomène, période, causalité et échéance non inventés. |
| Hébergement web ou stock artisanal dans un atelier partagé | INS-019 | Un risque ciblé, propriété et activité ; pas d'audit exhaustif ni de protection du particulier présumée. |
| Clause d'un souscripteur vivant ou recherche après décès | INS-020 / INS-011 | Pouvoir de modifier distinct du droit au capital ; acceptation à vérifier. |
| Frais ou perte sur unités de compte | BNK-011 | Orientation seule ; analyse au fond non couverte. |
| Constat auto imprécis, offre de cession ou offre corporelle | INS-002 / INS-003 / DOM-035 | Faits sans attribution de responsabilité ; restrictions de véhicule à vérifier ; corps à découper. |
| Réclamation simple, recommandé d'indemnisation et médiation | INS-005, INS-021 | Événements et preuves séparés ; aucune interruption ou suspension automatique. |

Les contrôles ajoutés vérifient numérotation 1 à 90, liens des propriétaires,
retour des suites concernées vers la matrice, neuf nouvelles suites reliées,
bornes placements/corps et empreinte SHA-256 du texte comparée à celle de la
pièce jointe. Le contrôleur conserve aussi dépendances, cohérence des 21
stories et du tableau, absence de plugin, liens, formats et index.
Le relevé JSON indique si la comparaison à l'instantané de début de tâche
a été exécutée ; les contrôles ne valident aucune règle du texte.

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles cités sont des pistes de recherche, pas des
règles vérifiées. Les montants figurant ci-dessus sont des données fictives
recopiées. Aucun délai établi, aucun skill créé ou exécuté, aucun paquet
installé, aucun lecteur réel ou indépendant, aucun envoi. Le préalable
PILOTE-003 est satisfait après BASE-011 ; aucune tranche n'est sélectionnée
par ce cadrage.
