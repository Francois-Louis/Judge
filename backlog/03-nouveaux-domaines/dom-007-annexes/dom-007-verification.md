# DOM-007 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-007-decoupage-sante.md) et les 12
propositions SAN, pour vérifier le routage et les informations à demander.
La story interdit de résoudre ces consultations : aucun délai, montant ou
droit n'est conclu. Le [relevé machine](dom-007-resultats.json) consigne
séparément les contrôles statiques.

## Dossier fictif P — demande de dossier médical par le patient

- `P-recit` : patiente majeure, opérée d'une hernie dans une clinique il y a
  plusieurs années ; elle veut le compte rendu opératoire et les résultats
  d'examens pour un nouveau chirurgien.
- `P-pieces` : courrier de sortie avec le nom de la clinique ; pièce
  d'identité disponible ; aucune demande antérieure.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `health-legal`, SAN-001. | — |
| Qualité | Patiente majeure agissant pour elle-même ; aucune mesure de protection déclarée. | — |
| Structure | Clinique : statut privé déclaré, à confirmer ; la voie de contestation éventuelle en dépend (SAN-004). | Adresse du service des relations avec les usagers ou de la direction. |
| Informations visées | Compte rendu opératoire et résultats, période du séjour ; ancienneté notée car elle peut changer les modalités. | Modalités et délai : pistes L1111-7 et R1111-1 et suivants, à lire ; rien n'est affirmé. |
| Sortie | Fiche, pièces à joindre, brouillon de demande ; frais éventuels de copie réservés. | — |
| Avertissement | Phrase BASE-013 nommant l'établissement puis une association d'usagers. | — |

**Constat :** SAN-001 suffit pour une demande utile ; aucun délai n'est
promis à la patiente.

## Dossier fictif Q — demande d'un proche dont le pouvoir reste à vérifier

- `Q-recit` : un fils s'occupe de son père, vivant, hospitalisé et
  « désorienté » ; il veut le dossier pour comprendre le traitement.
- `Q-pieces` : aucune décision de protection ni mandat ; le père n'a pas été
  interrogé.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | SAN-001 détecte un tiers et oriente vers SAN-002. | — |
| Qualité | Proche aidant : qualité déclarée, sans pouvoir établi. Aucune demande n'est rédigée en son nom. | Existence d'une mesure, d'un mandat, d'une désignation comme personne de confiance. |
| Alternatives | Demande par le père lui-même, avec aide ; questions à l'équipe soignante dans le cadre que le père accepte, à vérifier. | Ce que la personne de confiance peut recevoir : texte à lire. |
| Mesure | Si une mesure est demandée ou existe : DOM-026 pour son étendue. | — |
| Sortie | Questions et pièces ; pas de brouillon de demande d'accès. | — |

**Constat :** la qualité est vérifiée avant toute demande ; être aidant ne
vaut pas pouvoir. SAN-002 porte la question, DOM-026 seulement l'étendue
d'une mesure.

## Dossier fictif R — réclamation cherchant sanction et indemnisation

- `R-recit` : « Mon fils a été mal opéré de l'appendicite à l'hôpital, je
  veux que le chirurgien soit sanctionné et être indemnisée. »
- `R-pieces` : bulletin d'hospitalisation dans un centre hospitalier public ;
  aucune pièce médicale ; enfant mineur.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | SAN-005 identifie trois objets : explication, sanction, indemnisation. | — |
| Qualité | Parent d'un mineur ; SAN-002 pour l'accès au dossier si nécessaire. | Autorité parentale, à établir. |
| Explication | Réclamation à l'établissement (SAN-005), faits datés, sans terme de faute. | Circuit interne et commission des usagers : pistes à lire. |
| Sanction | Plainte ordinale (SAN-007) ; praticien hospitalier public : règles particulières à vérifier. | Statut du chirurgien. |
| Indemnisation | SAN-006 : voies amiable, commission, juge administratif à examiner pour un établissement public ; dossier médical d'abord. | Échéance : question signalée en tête, sans date. |
| Chiffrage | DOM-035 si un chiffrage du préjudice est demandé. | — |
| Sortie | Trois sorties distinctes ; aucune lettre unique présentée comme suffisante. | — |

**Constat :** sanction et indemnisation ne sont pas fusionnées ; aucune
faute n'est retenue.

## Dossier fictif T — copie du dossier et soupçon de consultation

Scénario du complément des frictions données personnelles (points 45–47).

- `T-recit` : une infirmière, patiente de l'hôpital où elle travaille,
  attend la copie de son dossier ; elle pense qu'un collègue l'a consulté.
- `T-pieces` : demande envoyée sans accusé de réception ; aucune réponse.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Objet 1 — copie | SAN-004 : chronologie ; réception non prouvée, délai réservé ; brouillon de relance. | Date de réception, ancienneté des informations, statut de l'hôpital. |
| Objet 2 — accès soupçonné | PRV-001 ou PRV-025 : demande au délégué à la protection des données de vérifier les accès, sans promettre l'identité de tous les agents ; PRV-034 si une plainte est envisagée. | Faits à l'origine du soupçon, distingués d'un accès établi. |
| Calendriers | Deux calendriers distincts, aucun calendrier RGPD appliqué à la copie du dossier. | Textes propres à chaque objet. |
| Travail | Relation de travail avec l'hôpital : orientation employment ou DOM-037 selon le statut, si une sanction interne est envisagée. | Statut de l'employeur. |
| Signalement | SAN-008 possible si un dysfonctionnement est décrit. | — |

**Constat :** deux objets, deux propriétaires et deux calendriers ; aucune
donnée de santé superflue n'est demandée.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| Refus de remboursement d'une consultation par la caisse | DOM-012 ; facture du soignant comme pièce seulement (SAN-011). |
| Mutuelle refusant des lunettes | INS-009 ; achat chez l'opticien → DOM-001 pour la vente. |
| Hospitalisation sous contrainte annoncée par un proche | SAN-010, renfort en tête, avocat ; aucun jugement sur l'état de santé. |
| Petite-fille voulant le dossier de sa grand-mère décédée | SAN-003 ; qualité d'ayant droit et objectif à établir ; succession → DOM-016. |
| Fille aidante d'une mère sous curatelle | SAN-002 ; étendue de la mesure → DOM-026. |
| Dossier de médecine du travail demandé par un salarié | Point ouvert du découpage ; aptitude → employment. |
| Plainte contre une résidence pour personnes âgées | Point ouvert du découpage, partage avec DOM-025 non décidé. |
| Dépassement d'honoraires sans devis | SAN-011 ; remboursement → DOM-012. |
| Douleur thoracique en cours, question sur ses droits | Secours en tête ; aucune démarche écrite d'abord. |
| Faux naturopathe se présentant comme médecin | SAN-007 pour un titre usurpé, DOM-002 pour l'infraction alléguée ; publicité → product-legal. |
| Victime de violences demandant son dossier pour une plainte | SAN-001 ; parcours de protection → DOM-038, plainte → DOM-002. |

## Couverture des critères de la story

| Critère DOM-007 | Où il est traité |
|---|---|
| Plugin propre et frontières | Découpage, sections plugin, garde-fous et frontières ; ligne mise à jour dans la matrice BASE-003. |
| Tâches hiérarchisées, premier skill borné | Rangs 1 à 4 ; inclus et exclus de SAN-001. |
| Références, pièces, sortie, scénarios par story | Sections dédiées des 12 propositions, contrôlées par le relevé. |
| Installation seule, pas d'agent ni connecteur par principe | Contrat d'installation du découpage ; aucun accès à un espace numérique de santé. |
| Implémentations non lancées | Aucun fichier sous `health-legal/` ; marketplace inchangé. |
| Distinctions demandées par la story | Établissement et commission des usagers (SAN-005), ARS (SAN-008), ordre (SAN-007), assurance (DOM-005), commissions et ONIAM, juge (SAN-006) ; soins sans consentement (SAN-010) et remboursement par une caisse (DOM-012) séparés. |
| Complément des frictions données personnelles | Points 45–47 rattachés dans le découpage ; dossier fictif T. |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles cités sont des pistes de recherche issues de la
connaissance de l'agent, pas des règles vérifiées. Aucun délai, seuil ou
montant établi, aucun skill créé ou exécuté, aucun paquet installé, aucun
lecteur réel ou indépendant, aucun envoi. Le préalable PILOTE-003 est
satisfait après BASE-011 ; aucune tranche n'est sélectionnée par ce
cadrage.
