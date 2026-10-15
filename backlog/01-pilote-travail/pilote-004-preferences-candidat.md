---
id: PILOTE-004
titre: "Modifier une préférence candidat sans initialisation professionnelle"
statut: a-verifier
priorite: P1
nature: implementation
dependances: [PILOTE-002, BASE-006, BASE-008]
---

# PILOTE-004 — Modifier une préférence candidat sans initialisation professionnelle

## Objectif

Un candidat qui veut conserver un format de lecture ou le modifier obtient
un profil minimal préservant ses réponses, sans passer par l'entretien
d'un service juridique d'entreprise. Correction D03 du
[bilan PILOTE-003](pilote-003-verification.md), dans le périmètre du pilote.
Cette proposition n'autorise pas la refonte des autres parcours de TRAV-016.

## Périmètre

`employment-legal`, branche candidat de `cold-start-interview`, `customize`,
modèle `CLAUDE.md` et retour à `hiring-review`. Entrées : préférence demandée,
réponses confirmées et profil existant/absent, y compris un ancien profil US.
Résultat : seule la préférence explicitement demandée est conservée/modifiée ;
la simple lecture sans sauvegarde reste possible.

## Travail attendu

- Rendre explicite la fin des branches candidat, sans poursuite vers le
  profil société, handbook, mémos de rupture ou tests de connecteurs non demandés.
- Concilier le statut `interview-required` du helper avec l'entretien en
  conversation ; un profil absent ou un placeholder professionnel ne doit
  pas imposer de sauvegarde pour expliquer l'offre.
- Ne pas charger les exemples juridiques américains d'un ancien profil comme
  règles françaises. Conserver les autres réponses ; remplacement seulement
  avec empreinte relue, création exclusive si le profil est absent.
- Garder le helper et la méthode BASE-005 embarqués. Aucune nouvelle règle de
  droit substantiel n'est prévue ; toute règle ajoutée demande ses sources
  primaires et versions selon BASE-005.

## Critères d'acceptation

- [ ] Sans profil, une offre reçue peut être expliquée sans création persistante.
- [ ] Une préférence volontairement mémorisée crée seulement le profil du fork ; pas de profil société ni registre.
- [ ] Modifier le format sur un profil partiel ou US conserve les réponses hors demande et n'applique aucun défaut US.
- [ ] Le parcours termine la branche candidat sans exécuter l'entretien professionnel ni sonder un connecteur non demandé.
- [ ] Lectures/écritures du helper et retour à la revue sont observés dans un client isolé ; le paquet n'exige aucun fichier du dépôt.
- [ ] Un lecteur non juriste peut expliquer ce qui a été mémorisé, l'emplacement et ce qui reste à vérifier sur son contrat.

## Vérification

H12, puis préférence « texte court », puis changement vers « tableau » sur
le profil créé ; comparer toutes les données avant/après. Rejouer avec ancien
profil US, placeholders et dossier d'un autre salarié contenant un témoin.
Conserver accès, sorties et absence de modification des témoins. Rejouer sans
exécuteur Python : aucune lecture persistante en contournement du helper.
Vérifier l'offre sans profil sans interpréter ce test comme validation juridique.

## Hors périmètre

Migration de profils d'une autre distribution, adaptation des congés/enquêtes,
refonte de tous les profils, nouveau connecteur, publication ou envoi.

## Bilan d'exécution

Implémentation réalisée le 15 octobre 2026 à la demande de l'utilisateur :
contrat candidat embarqué commun aux trois skills, branches terminales,
profil minimal volontaire, préservation des autres réponses et reprise de la
revue selon le format demandé. Helper et méthode BASE-005 inchangés, aucune
nouvelle règle de droit. Sept tests du helper sur paquet détaché réussis ;
régressions BASE-006/BASE-008 exécutées. Voir le
[bilan de vérification](pilote-004-verification.md) et les
[accès et contenus observés](pilote-004-controles.json).

La story reste `a-verifier` : CLI Claude absente, aucune invocation dans un
client isolé ni lecture avec un participant réel. Les cases ci-dessus ne sont
pas cochées sur la seule base des consignes ou des tests du helper. La recette
sans exécuteur et le retour effectif à la revue restent à observer. Aucune
extension aux autres parcours ni publication réalisée.
