# Lire une convocation — CRIM-001

Version `0.1.1` — 17 octobre 2026. Pour une personne majeure convoquée en
France par la police ou la gendarmerie, ou un proche qui l'aide à lire le
document. Un seul skill est livré : `summons-reading`.

Installation depuis le marketplace Judge :

```text
/plugin install judge-fr-eu-criminal-legal --marketplace Francois-Louis/Judge
```

Commande : `/judge-fr-eu-criminal-legal:summons-reading`, suivie du document
ou de sa description. Sans document, commencer par la date de convocation.
Masquer les identifiants inutiles ; aucune pièce personnelle n'est nécessaire
pour essayer le skill sur un exemple fictif.

La sortie commence par les prochaines actions utiles, puis donne une fiche
des mentions lues, déclarées ou absentes, les inconnues, les questions au
service et à un avocat, les pièces demandées et les droits à vérifier pour
le seul statut établi. « Pour affaire vous concernant » ne permet pas de
conclure que la personne est témoin ou suspecte. Un message douteux est
vérifié par un canal officiel indépendant avant toute suite.

Aucun profil, entretien initial, connecteur ou autre plugin requis. Aucun
agent, hook ni serveur MCP. Pas de contact du service, envoi, dépôt ou
préparation des déclarations. Le dossier n'est pas conservé durablement par
ce parcours ; cette consigne ne garantit pas l'absence de conservation par
le client ou le service qui l'héberge. Les modèles et le helper de stockage
communs sont embarqués pour le contrat BASE-008 et ne sont pas utilisés.

Le [skill](skills/summons-reading/SKILL.md) charge la
[qualification pénale](references/qualification-penale.md), les
[repères et sources datées](skills/summons-reading/references/convocation.md),
la [méthode BASE-005 `1.3.0`](references/shared/research-citation-method.md)
et le [contrat BASE-008](references/isolation.md), tous locaux au paquet.
Les articles 61-1 et 78 n'ont pas pu être lus lors de cette préparation :
leurs conclusions sont réservées. Les fiches Service-Public lues restent
des informations générales, distinctes des textes. Les directives ont été
lues dans leur publication initiale via CELLAR ; leur applicabilité et la
transposition utile au dossier restent à établir.

Mineur, mesure déjà commencée, citation devant un tribunal ou autre acte de
juridiction : fiche minimale et orientation vers un avocat. Les tâches
CRIM-002, CRIM-006 et CRIM-011 sont proposées, absentes de ce paquet.
Les violences intrafamiliales demandent d'abord une orientation de protection
et un canal sûr ; DOM-038 est un cadrage proposé, pas une commande installée.

Structure, schéma, installation, exécution des scénarios et lecture par une
personne sans formation juridique sont des validations distinctes. Voir le
bilan de recette CRIM-001 conservé avec la story dans le dépôt ; ce paquet
ne revendique pas une validation juridique ou utilisateur complète.
