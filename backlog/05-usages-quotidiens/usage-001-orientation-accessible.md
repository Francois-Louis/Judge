---
id: USAGE-001
titre: "Définir une orientation accessible à partir d'un problème concret"
statut: proposee
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

- [ ] Les situations de la matrice ont un domaine principal identifiable et des frontières explicites.
- [ ] Des mots ordinaires suffisent à commencer ; le nom du code ou de la procédure n'est pas une entrée obligatoire.
- [ ] Les sorties expliquent les options et leur utilité sans jargon non expliqué.
- [ ] La collecte et la diffusion de pièces sont limitées au besoin ; aucun envoi n'est fait sans autorisation adaptée.
- [ ] Un conflit n'est pas qualifié d'abus du seul fait que l'utilisateur le conteste ; la demande et les obligations des deux parties sont examinées.
- [ ] Les règles d'orientation restent séparées des raisonnements métier et ne dupliquent pas tous les domaines.

## Vérification

Éprouver le routage avec « on me réclame 800 € », « je ne comprends pas ce
courrier » et « mon artisan ne revient plus ». Ajouter les seuls faits qui
permettent de distinguer dette, facture, décision et travaux, puis vérifier que
la personne comprend la prochaine étape. Le montant est un exemple fictif,
pas un seuil juridique.

## Hors périmètre

Construire une application, créer un assistant juridique universel ou résoudre
toutes les demandes de la matrice dans cette story.
