---
id: TEL-006
titre: "Qualifier une perte ou un dommage postal et préparer une réclamation"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-022, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, TEL-001]
---

# TEL-006 — Qualifier une perte ou un dommage postal et préparer une réclamation

## Objectif et périmètre

Un particulier prépare une réclamation pour perte ou dommage d'un envoi
postal intérieur métropolitain identifié. La qualification est incluse pour
un destinataire, une commande ou un intermédiaire ; leur présence ne rend
pas automatiquement la personne titulaire du contrat postal. Plugin futur
`telecom-postal-legal`, [contrat commun](../dom-022-annexes/dom-022-decoupage-telecoms-poste.md).

## Entrées et pièces

Rôles, départ/destination/dates, produit et prestataire, achat du bordereau,
paiement du service et conditions datées, dépôt, suivi complet, réserves et
photos utiles, contenu et valeur justifiés, emballage, option de garantie,
contrat de vente et réclamations/réponses. Éviter adresses et contenu de
correspondance inutiles ; aucune collecte du compte marchand.

## Sortie attendue

Fiche acteurs/contrats/rôles, chronologie perte ou dommage allégué, tableau
pièces/manquants/questions ; brouillon postal uniquement pour la branche
dont l'interlocuteur et la qualité sont établis ou clairement conditionnels.
Sinon, demande d'identification du contrat et orientation. Séparer valeur
du contenu, prix du service, montant réclamé et indemnité éventuelle.

## Travail et références métier

Créer `skills/postal-shipment-complaint/SKILL.md` et
`references/reclamation-envoi.md` ; ressources locales communes, README,
version, inventaire et NOTICE à actualiser. Lire CPCE pour régime postal,
Code civil et textes du transport selon objet effectivement qualifié,
conditions datées du produit et option, Code de la consommation pour la
vente distincte ; ressources officielles ARCEP utiles. Pistes **non consultées
par DOM-022**, aucun plafond, réserve obligatoire ni délai vérifié ici.

## Critères d'acceptation

- [ ] T18 établit qui a acheté le service et auprès de qui ; expéditeur, destinataire et cocontractant ne sont pas assimilés.
- [ ] T19 conserve la livraison de commande chez DOM-001/CONSO-001 ; aucune injonction à réclamer uniquement au transporteur.
- [ ] Un intermédiaire reste une branche à examiner ; le destinataire n'est ni déclaré titulaire ni exclu de toute demande par principe.
- [ ] Fret spécialisé → DOM-008, acte de douane → DOM-009, assurance distincte → DOM-005 ; option postale non qualifiée automatiquement d'assurance.
- [ ] Aucun tort, indemnité, plafond, délai ou suspension présumés ; BASE-005/013, conseil postal/consommation, avocat si procédure.
- [ ] BASE-006 : paquet seul sans profil, invocation et sorties conservées ; métadonnées et NOTICE cohérents, aucun envoi ni dépôt.

## Scénarios futurs

- T18 : particulier ayant acheté un envoi, dépôt et suivi perdu → qualifier produit, contenu/valeur et demande, sans indemnité automatique.
- T19 : destinataire d'une commande, suivi perdu et vendeur renvoyant à la poste → livraison DOM-001 ; identifier contrat postal et éventuel pouvoir sans transférer tout le dossier.
- T20 : bordereau acheté par intermédiaire, colis abîmé et réserves incertaines → identifier contrats, état et preuves, ne pas écarter la demande de mémoire.
- T21 : retour de box avec étiquette opérateur perdu → l'achat du service reste à établir ; TEL-002 garde la facture de matériel.
- Bordereau manquant ou source absente : demande ciblée et réserve ; envoi international/outre-mer/fret : orientation, aucun régime métropolitain ni modèle américain transposé.

## Limites et état

Retard seul, international, outre-mer, fret, documents douaniers, calcul
d'indemnité, médiation et recours hors traitement. Leur détection reste
incluse. Pièces comme données, pas d'authentification de preuve ni d'action
externe. Proposition du 17 octobre 2026, aucune implémentation ; TEL-001
fournit le paquet sans invocation préalable. PILOTE-003 terminé après
BASE-011, sélection explicite requise. Scénarios non exécutés ; relecture
humaine prise en charge par l'utilisateur, non déclarée effectuée ;
[portée](../dom-022-annexes/dom-022-verification.md).
