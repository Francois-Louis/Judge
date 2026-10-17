# Réclamation pour commande non livrée — CONSO-001

Version `0.1.1` — 17 octobre 2026 (Europe/Paris).

La commande `/judge-fr-eu-consumer-legal:non-delivery-claim` prépare une
réclamation au vendeur pour un bien acheté à distance et jamais reçu.
Elle s'adresse à une personne sans formation juridique, sans profil préalable.
Un récit suffit pour commencer ; les informations absentes restent inconnues.

Le résultat comprend un résumé, une fiche de commande avec la provenance de
chaque fait, une chronologie, les pièces utiles et un brouillon à relire.
La remise du colis, le transfert du risque, la demande de livraison, la fin
du contrat et le remboursement sont examinés séparément. Un suivi « livré »
contesté ne suffit pas à trancher le dossier.

Le paquet contient uniquement ce skill, sa [qualification commune](references/qualification-achat.md),
ses [repères de non-livraison](skills/non-delivery-claim/references/non-livraison.md),
la [méthode BASE-005 `1.3.0`](references/shared/research-citation-method.md) et
les ressources du [contrat BASE-008](references/isolation.md), copiées à
l'identique. Il fonctionne sans checkout ni autre plugin. L'accès aux sources
officielles est optionnel : sans lecture de la version utile au dossier, le
brouillon reste factuel et les règles sont réservées. Les lectures de
maintenance du 17 octobre 2026 ne valent pas vérification d'un futur dossier.

Aucun profil, entretien d'installation, agent, hook ou connecteur n'est
nécessaire. Le skill n'utilise pas de stockage durable ; le helper et les
modèles sont embarqués pour la conformité du paquet, sans être appelés.
Il n'envoie pas le courrier et n'engage aucune procédure.

Les achats pour l'activité professionnelle, ventes entre particuliers,
secteurs spécialisés et vendeurs étrangers donnent lieu à une orientation
explicite. Bien reçu cassé ou incomplet, rétractation, paiement bancaire,
remboursement déjà dû mais non reçu et indemnisation sont des tâches distinctes.
Les suites CONSO-002 à CONSO-021 restent proposées, sans commande disponible
dans ce paquet. Aucun autre domaine n'est appelé automatiquement.

Validation : paquet détaché et schémas contrôlés selon le bilan conservé dans
le backlog de maintenance CONSO-001 ; invocation du skill et compréhension
par un lecteur réel à vérifier. Une extraction ou une installation locale
ne constitue pas un test du raisonnement juridique.
