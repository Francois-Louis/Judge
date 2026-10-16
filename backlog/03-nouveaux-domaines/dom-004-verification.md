# DOM-004 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-004-decoupage-banque.md) et les 11
propositions BNK, pour vérifier le routage et les informations à demander.
La story interdit de résoudre ces consultations : aucun délai, montant ou
droit n'est conclu. Le [relevé machine](dom-004-resultats.json) consigne
séparément les contrôles statiques.

## Dossier fictif K — paiement par carte contesté

- `K-releve` : trois paiements en ligne le 4 octobre 2026 vers un site
  étranger, libellés inconnus ; carte toujours en possession de la personne.
- `K-recit` : aucun code reçu selon la personne ; découverte le 9 octobre ;
  pas encore d'opposition. Un des trois libellés ressemble à un abonnement
  souscrit l'an dernier.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `banking-legal`, BNK-001 (`payment-dispute`). | Relevé complet, numéros masqués. |
| Urgence | Opposition et signalement par les canaux officiels en tête. | Aucune opposition faite par le plugin. |
| Branches | Deux paiements : non autorisés selon la déclaration. Le troisième : branche ouverte, possible abonnement oublié, donc litige commercial (DOM-001) ou prélèvement récurrent. | Contrat de l'abonnement, historique. |
| Réclamation | Brouillon pour les opérations non autorisées ; aucun délai de signalement ni franchise affirmés. | Pistes L133-18, L133-19, L133-24 à lire. |
| Suites | Médiation (BNK-004) si refus ; plainte (DOM-002) en tâche distincte. | — |

**Constat :** la qualification opération par opération évite de traiter un
abonnement oublié comme une fraude. Le cadrage ne dit pas si la banque doit
rembourser.

## Dossier fictif U — virement validé après une usurpation d'identité

- `U-appel` : appel du « service fraude » affichant le numéro de l'agence ;
  l'interlocuteur connaît les dernières opérations et demande de « sécuriser
  l'épargne ».
- `U-validation` : la personne valide dans l'application un virement de
  4 800 € vers un compte « de sécurité » ; message de la banque affichant le
  nom du bénéficiaire, non lu selon la personne.
- `U-suite` : appel à la vraie agence deux heures plus tard.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | BNK-001 qualifie (opération validée sous tromperie, branche ouverte), puis BNK-002. | Captures de l'application et du message. |
| Urgence | Demande de rappel des fonds à poser immédiatement ; signalement ; plainte (DOM-002). | Aucune promesse de récupération. |
| Autorisation | Ni autorisée ni non autorisée par principe : faits listés (numéro usurpé, informations connues, validation, message affiché). | Jurisprudence récente sur le « faux conseiller » à lire. |
| Vérification du bénéficiaire | Question posée sur ce que la banque a affiché. | Date d'application du règlement (UE) 2024/886 à vérifier. |
| Négligence | Question, jamais conclusion. | — |

**Constat :** le découpage sépare l'opération non autorisée de l'opération
validée sous tromperie et prévoit pour celle-ci un dossier propre, sans
trancher la question débattue. Le montant est une donnée fictive recopiée.

## Dossier fictif F — frais d'un compte professionnel

- `F-releves` : compte professionnel d'une menuisière en entreprise
  individuelle ; commissions d'intervention et frais de lettre d'information
  sur trois mois.
- `F-grille` : conditions tarifaires « professionnels » de l'année
  précédente ; version en vigueur non fournie.
- `F-recit` : « pour les particuliers c'est plafonné, pourquoi pas moi ? ».

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | BNK-003, compte professionnel. | Grille en vigueur à la date des frais. |
| Statut | Compte professionnel : les repères du particulier ne sont pas appliqués. La question de la personne reçoit une réponse sourcée ou réservée. | Pistes L312-1-1, L312-1-3 et règles propres aux professionnels à lire. |
| Comparaison | Tableau frais/ligne tarifaire/déclencheur ; écart signalé seulement si la grille applicable est lue. | Convention de compte professionnelle. |
| Escalade | BNK-004 laisse ouverte la recevabilité de la médiation pour une professionnelle. | Piste L316-1 à lire. |
| Voisins | Pouvoirs bancaires d'une société → SOC-002 ; ici entreprise individuelle, sans objet. | — |

**Constat :** le statut professionnel change les repères sans exclure la
réclamation. Aucun plafond ni écart n'est affirmé.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| Commande payée par carte jamais livrée | BNK-001 litige commercial → DOM-001 ; rétrofacturation présentée comme règle privée à demander. |
| Prélèvement d'un abonnement résilié | BNK-006 pour la banque, domaine du contrat pour le créancier. |
| Crédit en magasin pour une cuisine non livrée | BNK-005 pour le crédit, DOM-001 pour la vente. |
| Refus de l'assurance emprunteur | DOM-005. |
| Saisie sur compte et frais de la banque | Saisie → DOM-003 ; frais → BNK-003. |
| Cinq crédits en retard | DOM-024 pour la situation globale. |
| Plateforme de cryptoactifs bloquant les retraits | BNK-011, fraude → BNK-002 et DOM-002 ; aucun conseil d'investissement. |
| Comptes d'un parent décédé bloqués | DOM-016. |
| « Mon conseiller me demande mon code pour annuler la fraude » | Arrêt immédiat : aucun conseiller légitime ne le demande ; signalement par les canaux officiels. |
| Fuite de données de la banque | Privacy pour les données ; conséquences sur le compte ici. |

## Couverture des critères de la story

| Critère DOM-004 | Où il est traité |
|---|---|
| Plugin propre et frontières | Découpage, sections plugin, garde-fous et frontières ; ligne mise à jour dans la matrice BASE-003. |
| Tâches hiérarchisées, premier skill borné | Rangs 1 à 4 ; inclus et exclus de BNK-001, nom `payment-dispute` confirmé. |
| Références, pièces, sortie, scénarios par story | Sections dédiées des 11 propositions, contrôlées par le relevé. |
| Installation seule, pas d'agent ni connecteur par principe | Contrat d'installation du découpage ; aucun accès à un compte en ligne. |
| Implémentations non lancées | Aucun fichier sous `banking-legal/` ; marketplace inchangé. |
| Distinctions demandées par la story | Compte, paiement, crédit et investissement séparés ; paiement non autorisé, tromperie et litige commercial dans des branches distinctes ; frontières surendettement (DOM-024) et AMF (BNK-011, point ouvert). |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles et actes cités sont des pistes de recherche, pas
des règles vérifiées. Les montants figurant ci-dessus sont des données
fictives recopiées. Aucun délai établi, aucun skill créé ou exécuté, aucun
paquet installé, aucun lecteur réel ou indépendant, aucun envoi. Le
préalable PILOTE-003 est satisfait après BASE-011 ; aucune tranche n'est
sélectionnée par ce cadrage.
