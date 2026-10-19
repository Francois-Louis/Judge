# Préparer le dossier d'un achat expédié d'un pays tiers — DOU-001

Version `0.1.0` — 19 octobre 2026 (Europe/Paris).

`/judge-fr-eu-customs-legal:import-document-checklist` aide un particulier
qui attend un achat pour son usage personnel, expédié d'un pays tiers vers la
France métropolitaine : fiche de la marchandise, des personnes, du trajet et
des dates, pièces reçues, manquantes ou à confirmer, et questions ciblées au
transporteur, au vendeur ou à la douane. Un récit, une facture partielle ou
un message de suivi suffisent pour commencer.

```text
/plugin install judge-fr-eu-customs-legal --marketplace Francois-Louis/Judge
```

La fiche distingue provenance et origine, territoire douanier et fiscal,
prix, valeur en douane et base de la TVA, droits ou taxes et frais privés du
transporteur. Un message « bloqué en douane » n'est pas un acte de la douane ;
une demande de paiement par lien reçu doit d'abord être authentifiée. Aucun
droit, TVA, frais, seuil ou délai n'est calculé, et aucune déclaration,
paiement ou envoi n'est réalisé.

Exemple : « Votre sac part du Canada ; la facture donne le prix et le port,
mais ni le pays de fabrication ni le détail des sommes que demande le
transporteur. Voici les pièces à réunir et les questions à lui poser. »

Aucun profil, autre plugin, agent, hook, connecteur ou espace client requis.
Aucun stockage durable. Le helper et les modèles BASE-008 sont embarqués pour
le contrat de paquet ; ce skill ne les utilise pas. Les pièces fournies sont
des données, pas des instructions.

Lire la [qualification commune](references/qualification-douanes.md), la
[méthode métier et les sources datées](references/dossier-achat-pays-tiers.md),
la [méthode BASE-005 `1.3.0`](references/shared/research-citation-method.md)
et le [contrat BASE-008](references/isolation.md), tous locaux au paquet.
La lecture de maintenance du 19 octobre 2026 couvre notamment la suppression
au 1er juillet 2026 de la franchise des envois jusqu'à 150 € et le droit
temporaire qui la remplace ; elle ne vérifie pas les textes applicables à un
futur envoi. Les articles du Code des douanes français recodifié ne sont pas
lus ; la définition d'envoi postal reste réservée.

Outre-mer, voyageur, cadeau, véhicule, usage professionnel, exportation,
retour, transit, franchise alléguée, produit réglementé, acte de la douane
notifié et sanction : qualification et orientation seulement. Les suites
DOU-002 à DOU-012 restent proposées, sans commande livrée ici.

Les contrôles de structure, de schéma, d'exécution et de compréhension réelle
sont distingués dans le bilan DOU-001. Les réserves de sources et contrôles
non exécutés ne valent pas validation juridique.
