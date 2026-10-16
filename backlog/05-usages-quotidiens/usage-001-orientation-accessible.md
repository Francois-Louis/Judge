---
id: USAGE-001
titre: "Définir une orientation accessible à partir d'un problème concret"
statut: terminee
priorite: P0
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# USAGE-001 — Définir une orientation accessible à partir d'un problème concret

## Objectif

Permettre à une personne de demander de l'aide sans connaître son code, son
tribunal ou le nom d'un plugin. Cette story définit le routage et les attentes
de restitution ; elle ne crée pas un plugin généraliste France/UE.

## Points de départ

- [Situations du quotidien](../usages-quotidiens.md).
- [Architecture par domaine](../00-fondations/base-003-architecture-domaines.md).
- [Modèle de story](../story-template.md).

## Travail attendu

- Partir du récit et du document reçu, puis identifier qualité de la personne,
  acte, date et objectif. Ne pas imposer un questionnaire de cabinet à une
  personne venue comprendre une facture.
- Définir un domaine principal et, si nécessaire, des volets complémentaires
  avec leur question précise. Pour un paiement contesté après un achat, séparer
  la demande au vendeur de celle au prestataire de paiement.
- Prévoir une sortie compréhensible : ce que le document demande, ce qui reste
  incertain, pièces utiles, éventuelle urgence, interlocuteur et action possible.
- Prévoir des formes utilisables : explication courte, tableau d'une facture,
  liste de pièces, chronologie, brouillon de courrier et questions à un professionnel.
- Prévoir particuliers, salariés, retraités, aidants, indépendants, artisans,
  adhérents d'association et petits exploitants. Le profil d'avocat ou de
  directeur juridique ne doit pas être nécessaire pour obtenir une orientation.
- Traiter langue, accessibilité, manque de pièces et difficulté numérique
  comme des besoins à prendre en compte, sans demander de données superflues.

## Critères d'acceptation

- [x] Les situations de la matrice ont un domaine principal identifiable et des frontières explicites.
- [x] Des mots ordinaires suffisent à commencer ; le nom du code ou de la procédure n'est pas une entrée obligatoire. *Vérifié sur cas fictifs par le rédacteur ; essai réel reporté à PILOTE-002.*
- [x] Les sorties expliquent les options et leur utilité sans jargon non expliqué. *Vérifié sur cas fictifs par le rédacteur ; essai réel reporté à PILOTE-002.*
- [x] La collecte et la diffusion de pièces sont limitées au besoin ; aucun envoi n'est fait sans autorisation adaptée.
- [x] Un conflit n'est pas qualifié d'abus du seul fait que l'utilisateur le conteste ; la demande et les obligations des deux parties sont examinées.
- [x] Les règles d'orientation restent séparées des raisonnements métier et ne dupliquent pas tous les domaines.

## Vérification

Éprouver le routage avec « on me réclame 800 € », « je ne comprends pas ce
courrier » et « mon artisan ne revient plus ». Ajouter les seuls faits qui
permettent de distinguer dette, facture, décision et travaux, puis vérifier que
la personne comprend la prochaine étape. Le montant est un exemple fictif,
pas un seuil juridique.

## Hors périmètre

Construire une application, créer un assistant juridique universel ou résoudre
toutes les demandes de la matrice dans cette story.

## Bilan d'exécution — 15 octobre 2026

- Support retenu : [protocole documentaire](usage-001-annexes/usage-001-protocole-orientation.md)
  dans le backlog et [index des 42 situations](../usages-quotidiens.md) enrichi
  avec domaine principal et frontière. La correspondance vers les plugins
  reste celle de BASE-003 ; les noms proposés ne deviennent pas disponibles.
- Le protocole définit l'accueil progressif sans profil de cabinet, le domaine
  principal par tâche, les compléments bornés, les six formes de restitution,
  les besoins d'accessibilité et les limites de collecte, stockage et envoi.
  Il demande d'examiner les engagements des deux parties et la provenance des
  faits, sans présumer un abus ni une issue favorable.
- [Relecture sur cas fictifs](usage-001-annexes/usage-001-verification.md) : les trois récits
  demandés et leurs variantes distinguent facture, dette, décision et travaux.
  Le cas achat/paiement sépare vendeur et prestataire de paiement ; les limites
  aidant, retraite, agriculture, statut public, langue et manque de pièces
  sont explicitées. Chaque sortie rend identifiables action, interlocuteur et
  incertitude ; aucune transmission n'est effectuée.
- Contrôles structurels : couverture des 42 lignes et des 38 domaines DOM,
  cohérence avec BASE-003, liens locaux, tableaux Markdown, statuts et espaces
  de fin de ligne vérifiés. Le résultat technique détaillé figure dans le
  relevé de vérification.
- Limites : cadrage relu sur papier, sans utilisateur réel, moteur de routage,
  exécution de skill ni installation isolée. Aucune règle métier ou source
  juridique nouvelle n'est validée. BASE-005 reste la méthode applicable aux
  futures analyses ; BASE-006 encadre leur recette. Le protocole définit le
  contrôle de compréhension à réaliser avec les utilisateurs des futurs lots.
- Suite : USAGE-002 compare et priorise les petites tâches ; aucun second
  pilote ni changement de priorité n'est déclenché par cette story.
