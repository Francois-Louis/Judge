# Banque et paiements — BNK-001

Version `0.1.0`. Une seule tâche est livrée :
`/judge-fr-eu-banking-legal:payment-dispute` qualifie un paiement contesté
et prépare le brouillon d'une réclamation au prestataire pour une opération
non autorisée sur un compte personnel. Public : particulier sans formation
juridique ; cas nominal : services de paiement en France, pays des deux
prestataires et devise à qualifier.

Commencer par exemple par « trois paiements inconnus sur mon relevé, ma carte
est toujours avec moi ». Fournir les seules lignes utiles, dates, montants,
libellés et échanges masqués. Aucun code, mot de passe, identifiant de
connexion, numéro complet de compte ou de carte n'est demandé.

La réponse commence par les actions urgentes auprès du prestataire via ses
canaux officiels. Elle distingue les faits déclarés, les pièces et les inconnues,
explique la branche retenue, liste les pièces utiles et produit un brouillon
à relire. Une validation dans l'application ou un code saisi sous tromperie
laisse le consentement à éclaircir. La négligence alléguée n'est jamais tranchée.

Le paquet fonctionne seul, sans profil préalable, agent, hook, connecteur,
accès à un compte bancaire ou stockage durable. Il embarque la méthode
BASE-005 `1.2.0` et les copies BASE-008 identiques aux sources du dépôt.
Une recherche officielle est utile pour vérifier la règle à la date des faits ;
sans source effectivement lue, le résultat reste factuel et les règles sont
réservées. Les lectures de maintenance ne valent pas vérification d'un dossier.

Les opérations sous tromperie, litiges avec le vendeur, comptes professionnels,
prélèvements, chèques, crédits et actifs numériques reçoivent une qualification
et une orientation. BNK-002/003/004/006/011 et DOM-001/002 sont des suites ou
domaines proposés, sans commande disponible dans ce paquet. La rétrofacturation
(chargeback) relève des conditions privées du réseau à demander au prestataire ;
elle n'est pas un remboursement légal automatique.

Aucune opposition, plainte, signature ou transmission n'est effectuée. Aucun
calcul de délai, de franchise ou de pénalités ; aucun remboursement garanti,
conseil d'investissement ou conclusion sur la négligence.

Validation : structure du paquet détaché et schéma officiel contrôlés en
maintenance ; voir le bilan BNK-001 dans le backlog du projet pour les traces,
les scénarios exécutés et les limites. Une copie détachée ne prouve pas une
installation isolée et une relecture du rédacteur ne vaut pas test utilisateur.
