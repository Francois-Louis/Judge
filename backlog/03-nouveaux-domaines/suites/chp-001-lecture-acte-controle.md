---
id: CHP-001
titre: "Lire un acte reçu après un contrôle de chasse ou de pêche"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013]
---

# CHP-001 — Lire un acte reçu après un contrôle de chasse ou de pêche

## Objectif et périmètre

Un pratiquant comprend ce que le document lui reproche, le stade affiché,
les pièces manquantes et à qui poser ses questions. Première tranche
proposée de `hunting-fishing-legal` ; contrat commun et frontières dans le
[découpage DOM-040](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).
Un seul résultat : une fiche de lecture, sans recours formel.

## Entrées et pièces

Acte lisible recto verso, annexes, enveloppe ou preuve de réception ; à
défaut récit marqué comme déclaré. Lieu, date et pratique, auteur et qualité
affichée, destinataire, mentions reprochées, textes cités, documents détenus
au contrôle et démarches déjà accomplies. Recueillir les mesures éventuelles
(saisie, convocation, suspension) sans présumer la nature pénale de tout acte.

## Sortie attendue

1. Urgence observée en tête, avocat nommé pour le pénal, sans délai calculé.
2. Fiche : nature affichée, auteur, faits allégués, stade établi ou incertain,
   dates et montants recopiés avec leur provenance.
3. Tableau : mention de l'acte, pièce disponible, règle à rechercher,
   question réservée ; aucune infraction ni nullité conclue par défaut.
4. Liste limitée des pièces à demander et brouillon de demande de copie ou
   d'explication, adressé au service identifié, sans argument de contestation.
5. Relais précis : procédure pénale → DOM-002 ; arme → CRIM-017 ; décision
   administrative → DOM-010 ; règle de pratique à éclaircir → CHP-002/003/004.
6. Phrase finale BASE-013 : information et préparation ne remplacent pas
   l'avis d'un avocat dans ce dossier pénal, ou du professionnel adapté si
   l'acte est administratif. L'autorité n'est pas présentée comme conseil.

## Travail et fichiers futurs

Créer `skills/outdoor-control-notice-review/SKILL.md`,
`references/lecture-acte-controle.md`,
`references/qualification-chasse-peche.md` et un modèle local de fiche.
Créer avec ce skill le paquet proposé `judge-fr-eu-hunting-fishing-legal` :
manifeste, README, modèle de profil facultatif, LICENSE/NOTICE et copies
BASE-005/008 décrites au contrat ; déclarer l'entrée marketplace et ajuster
les contrôles d'inventaire/versions au lot choisi. Aucun connecteur ni agent.

Charger les références locales ; rechercher les codes et la règle exacte
visés dans l'acte selon pratique, territoire et date. Source locale absente :
demander ou retrouver l'arrêté et réserver l'appréciation de l'allégation,
en poursuivant la fiche. Ne jamais conseiller de payer, consigner, attendre,
ignorer ou contester sans traitement procédural distinct chez DOM-002.

## Critères d'acceptation

- [ ] C01 et C03 produisent une fiche exploitable à partir du seul document, sans vocabulaire juridique fourni par la personne.
- [ ] C03 réserve la taille applicable faute de règle locale ; C09 ne transforme pas un récit en procès-verbal.
- [ ] Allégation, pièces, stade et inconnues sont séparés ; une validation manquante ne prouve pas à elle seule l'infraction.
- [ ] Renfort, phrase BASE-013, frontières et absence de démarche externe sont observés ; toute jurisprudence citée est lue selon BASE-005 section 10.
- [ ] Paquet seul contrôlé avec BASE-006/008, sources effectivement lues tracées selon BASE-014, version et schémas vérifiés ; scénarios en client conservés.

## Vérification prévue

- C01 : avis après contrôle de chasse, validation annuelle présentée comme
  expirée → mentions et dates recopiées, pièces de validation demandées,
  aucune culpabilité affirmée ni recours rédigé.
- C03 : pêcheur verbalisé pour taille d'une prise, arrêté absent → lieu,
  date et espèce alléguée relevés, règle réservée, avocat pour la procédure.
- C09 : seulement un contrôle raconté oralement, puis mention d'une arme
  retenue → acte demandé, mesure orientée CRIM-017/DOM-002 sans attendre
  une revue ordinaire, aucune instruction sur l'arme.

## Hors périmètre et état

Contestations, calcul de délai ou d'amende, défense pénale, conseils de
pratique et d'équipement. Proposition issue de DOM-040 ; scénarios futurs,
sans implémentation. [Portée](../dom-040-annexes/dom-040-verification.md#portée).
