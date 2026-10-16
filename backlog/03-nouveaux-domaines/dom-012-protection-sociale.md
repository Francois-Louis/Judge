---
id: DOM-012
titre: "Cadrer un plugin de sécurité sociale et prestations"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-012 — Cadrer un plugin de sécurité sociale et prestations

## Objectif

Isoler les droits et recours contre les organismes sociaux des décisions de l'employeur.

Nom de plugin proposé : `social-security-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Organisme, prestation/cotisation, période, décision, motif, ressources déclarées et notification.
- Tâches candidates : lecture d'une décision, contestation d'indu, préparation d'un recours préalable et dossier de prestation.
- Séparer CAF, assurance maladie, France Travail et cotisations ; identifier compétences et procédures propres, sans inventer un recours commun.
- Les [retraites](dom-036-retraites.md) ont un cadrage dédié. Articuler les prestations et décisions liées au [handicap/autonomie](dom-025-handicap-autonomie.md) avec ce plugin, en désignant pour chaque demande un domaine principal.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code de la sécurité sociale, Code de l'action sociale et des familles et autres textes selon l'organisme ; sources officielles des caisses et jurisprudence.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture d'une notification d'indu pour un organisme et une prestation choisis.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une notification d'indu.
- Un refus de prise en charge.
- Une décision portant sur un droit à prestation ou un calcul.
- Une visite d'un contrôleur de la CAF, puis une demande de pièces.
- Une suspension de prestation après un contrôle, avec mention d'une fraude possible.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Compléments du 16 octobre 2026

Ajoutés par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)). Ces tâches candidates
s'ajoutent à celles ci-dessus ; elles restent à hiérarchiser par le cadrage.

- **Contrôle d'un organisme** (CAF, assurance maladie, France Travail,
  MSA selon le statut) : courrier ou visite de contrôle, entretien, demande
  de pièces, droit de communication auprès de tiers, rapport de contrôle.
  Préparer les pièces et les questions ; distinguer contrôle, décision,
  indu, suspension et pénalité administrative.
- **Suspicion de fraude** : pénalité administrative et volet pénal
  éventuel distingués ; plainte ou poursuite → DOM-002. Aucune présomption
  de fraude ni d'innocence.
- Les cotisations et contrôles URSSAF d'un indépendant relèvent de DOM-039 ;
  ceux d'un employeur restent à qualifier séparément.

Sources à prévoir en plus : Code de la sécurité sociale et textes propres à
chaque organisme sur le contrôle, le droit de communication et les
pénalités ; chartes de contrôle publiées par les organismes, à vérifier.

## Complément des frictions IA — 16 octobre 2026

Point 26 de la [matrice IA](../02-plugins-existants/exist-005-annexes/exist-005-frictions-utilisateurs.md) : prévoir des tâches distinctes de lecture d'un contrôle antifraude orienté par score et de contestation d'une décision sur les prestations. Recueillir organisme/prestation, contrôle ou décision, données contestées, demandes, notification et réception ; PRV-001/022/031 gardent les données et la demande relative à l'automatisation. Qualification IA vers IA-003/004 si faits utiles ; le seul score n'établit ni fraude de l'usager ni illégalité du contrôle. Sortie à cadrer : pièces, questions, voie préalable et calendrier propres au régime. Cas attendu : revenu erroné corrigé mais décision de caisse encore à contester, sans délai suspendu par la demande RGPD.

Ces exigences restent à découper ou préciser ; [portée et contrôles de l'intégration](../02-plugins-existants/exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Complément des frictions transports — 16 octobre 2026

Points 88, 115–116 de la [matrice transports](dom-008-annexes/dom-008-frictions-utilisateurs.md).

Distinguer conventionnement du taxi/VSL, prescription, accord préalable, facture et notification du refus CPAM. Découper une vérification de facturation médicale et un dossier de recours contre refus, avec sources Assurance maladie et textes de sécurité sociale aux faits ; les suites ne sont pas encore proposées.

Scénarios **attendus, non exécutés** : VTC présenté comme taxi conventionné puis remboursement refusé : qualifier le mode et le motif sans promettre prise en charge ; la course seule reste TPT-016.
