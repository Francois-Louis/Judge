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

## Complément des frictions santé — 16 octobre 2026

Points 5, 45, 64–66, 107–122, 134 et 142–147 et sections 12–15 de la
[matrice santé](dom-007-annexes/dom-007-frictions-utilisateurs.md).
Le cadrage reste `proposee` ; ces tâches restent à découper, sans recours commun.

| Tâche candidate | Entrées et résultat borné | Cas de contrôle attendu |
|---|---|---|
| Remboursement, feuille papier et droits | Facture, décompte, transmission/réception, affiliation, médecin traitant et période ; demande de correction ou motif de décision, sans remboursement recalculé | Feuille papier égarée et base inattendue : séparer preuve d'envoi, parcours et montant de pièce |
| ALD, tiers payant et forfaits | Prescription, lien déclaré avec ALD, droits et facture ; questions sur base, exonération et circuit, distinctes des dépassements | ALD présentée comme tout remboursé et chambre facturée : part caisse séparée de SAN-011/014 |
| Indu et compensation | Notification, période, décompte et réception ; lecture du motif puis recours propre à l'organisme | Somme retenue sans détail : demander décompte sans remplacer le recours formel |
| Arrêt et indemnités journalières | Arrêt/prolongation, dates, envoi, attestation de salaire, décomptes et subrogation ; pièces manquantes et décision à qualifier | IJ versées à employeur mais paie discordante : caisse ici, obligation/paie de l'employeur au cadrage travail |
| Recours administratif de caisse | Décision et réception, régime, objet, voies mentionnées ; projet de recours préalable à borner puis calendrier propre | Réclamation simple sans saisine CRA : identifier acte requis ; silence et délai judiciaire à rechercher |
| Recours médical de caisse | Décision médicale, contrôle, consolidation/taux annoncé et notification ; voie CMRA à vérifier selon champ | IJ suspendues ou consolidation contestée : ne pas choisir CRA sur le seul mot remboursement |
| Transport sanitaire pris en charge | Prescription/date, mode, distance, ALD, accord préalable/réception, partage et facture ; conditions puis décision à contester | Prescription après trajet, refus de partage et absence de réponse : trois conditions à vérifier, aucun accord ou remboursement automatique |

Sources à ouvrir : Code de la sécurité sociale et textes d'application,
conventions/nomenclatures utiles, décisions et informations officielles
Assurance maladie ; règles de CRA/CMRA, tribunal et médiation selon régime.
Les règles 2026, montants des forfaits et durées d'arrêt du texte utilisateur
sont des assertions à vérifier, avec transitions/exceptions ; aucun délai de
médiation suspendu sans texte et événement établis. Notifications, accusés,
réception et calendrier du silence sont des pièces essentielles. Aucune
plainte ordinale, demande RGPD ou réclamation informelle ne reçoit d'effet
conservatoire automatique. Complémentaire privée → INS-009 ; facture du
soignant → SAN-011/014 ; traitement et continuité → SAN-013/016.

Scénarios **attendus, non exécutés** ; [portée et contrôles](dom-007-annexes/dom-007-frictions-verification.md).

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 105, 113–117 et D07–D08 de la [matrice](dom-031-annexes/dom-031-frictions-utilisateurs.md). Tâches candidates à découper ; aucune nouvelle capacité livrée.

- [ ] Découper le capital décès par régime : statut du défunt, organisme, qualité/priorité, événement, demande et preuve de réception ; distinguer délai de priorité et délai ordinaire, sans importer les délais de la CPAM à une prévoyance privée.
- [ ] Découper aides décès France Travail et CAF/MSA, notamment décès d’enfant : entrées propres, qualité, demande et décision ; sortie : pièces, organisme et calendrier sourcé. Congés vers le domaine emploi, garantie collective privée vers INS-009.
- [ ] Prévoir origine professionnelle du décès et créances de prestations encore dues : décision de reconnaissance, bénéficiaire et nature des sommes ; distinguer rentes/frais/prestations et responsabilité civile DOM-035. Réversion et ASPA d’un régime de retraite vers DOM-036 ; autre régime de récupération à qualifier.

Scénarios supplémentaires **attendus, non exécutés** : demande CPAM tardive pour priorité mais pas nécessairement pour le droit ordinaire ; conjoint d’un allocataire France Travail ; décès d’enfant et aides multiples ; décès avec reconnaissance professionnelle en cours.

Sources à ouvrir lors de l’implémentation : CSS, textes France Travail/CAF/MSA et régime AT/MP, sources des organismes ; conditions et échéances propres, sans prestation commune inventée.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](dom-031-annexes/dom-031-frictions-verification.md).

## Complément emploi, minima sociaux et aides — 16 octobre 2026

Ajouté par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)).
Ces tâches candidates restent à hiérarchiser. Chaque prestation a son
organisme, son texte, son recours préalable et son juge : ils sont recherchés
séparément, sans transposer la commission de recours amiable de la sécurité
sociale ni un autre recours par analogie.

| Régime | Tâches candidates | Cas de contrôle attendu |
|---|---|---|
| Inscription et suivi à France Travail | Lire un refus d'inscription, un avertissement, une sanction, une radiation de la liste ou une décision liée au contrat d'engagement ; recueillir convocation, motif, réponse donnée et notification | Radiation après une convocation non reçue : établir l'envoi et la réception avant la voie de recours |
| Allocation chômage (assurance chômage) | Lire un refus, un calcul, une date de début ou un trop-perçu ; préparer pièces et questions sur la fin de contrat, les attestations et les périodes déclarées | Trop-perçu réclamé après une reprise d'activité déclarée en retard : période, décompte et demande d'explication, sans calcul refait |
| Allocation de solidarité spécifique | Lire un refus ou une fin de droit ; identifier le texte et l'autorité qui décide | Fin de droits présentée comme définitive sans motif détaillé |
| RSA | Lire une décision d'ouverture, de suspension, de réduction ou de fin, ou un indu ; distinguer le département qui décide de la CAF ou de la MSA qui instruit et verse ; qualifier les obligations d'accompagnement | RSA suspendu pour non-respect allégué du contrat d'engagement : pièces, motif et recours préalable propres au RSA |
| Prime d'activité | Lire un refus, un recalcul ou un indu après déclaration trimestrielle ; rapprocher ressources déclarées et période | Indu après une déclaration trimestrielle erronée corrigée ensuite |
| Aides de France Travail à la création ou reprise d'entreprise | Lire une décision sur l'aide en capital, le maintien de l'allocation pendant l'activité ou une autre aide ; recueillir dates de création et d'inscription, demande et réponse | Aide en capital refusée pour une demande jugée tardive : dates établies, aucune échéance donnée sans texte |

Qualifier pour chaque demande le statut de la personne (demandeur d'emploi,
allocataire, bénéficiaire du RSA, indépendant), l'organisme qui décide, celui
qui verse, la décision, sa notification et sa réception. Les obligations et
sanctions issues de la loi pour le plein emploi de 2023 sont à vérifier dans
leur version applicable à la date des faits. Le cumul des allocations avec une
activité indépendante se décide ici ; DOM-039 garde l'activité, ses
déclarations et l'ACRE. L'attestation que doit remettre l'employeur reste
TRAV-021. Les intermittents du spectacle relèvent d'abord de DOM-042. Une
pension militaire d'invalidité relève de DOM-044.

Le cadrage dira si l'emploi et les minima sociaux justifient un plugin
distinct de `social-security-legal`. Le découpage par régime reste exigé dans
les deux cas.

Sources à prévoir : Code du travail et règlement d'assurance chômage pour
l'allocation chômage et l'inscription ; Code de l'action sociale et des
familles pour le RSA ; Code de la sécurité sociale pour la prime d'activité ;
textes et informations officielles de France Travail, de l'Unédic, de la CAF,
de la MSA et des départements. Les juridictions compétentes sont à vérifier
pour chaque régime.

Scénarios **attendus, non exécutés**.

## Complément des frictions travail — 16 octobre 2026

La [fiche de relais](dom-012-annexes/dom-012-frictions-travail.md), issue des
[182 frictions travail](../01-pilote-travail/pilote-001-annexes/pilote-001-frictions-utilisateurs.md),
précise les tâches candidates de déclaration/instruction/reconnaissance AT/MP,
consolidation, incapacité, faute inexcusable, invalidité et indemnisation choisie,
y compris chômage après départ/CSP. Ces tâches restent à découper ; la première
tranche de lecture d’un indu reste inchangée. TRAV-040 garde le signalement à
l’employeur, TRAV-041/042 les visites et effets professionnels. Délais et voies
sociales propres à l’acte ne sont pas remplacés par la procédure prud’homale.
Scénarios et limites : voir la fiche et la vérification travail liée.

## Complément des frictions allocations et aides sociales — 16 octobre 2026

Le [guide intégral](sources/aides-sociales-frictions-2026-10-16.txt) et la
[matrice des 185 points](dom-012-annexes/dom-012-frictions-utilisateurs.md)
précisent les exigences d'entrée, résultats, frontières et sources futures.
Les codes locaux de tâches ne sont ni des stories ni des commandes livrées.
DOM-012 reste `proposee`, sans sélection de tranche ; le premier indu reste
à borner à un organisme et une prestation. L'éventuelle séparation d'un
plugin emploi/minima sociaux demeure une question du cadrage.

- [ ] Décliner FT01–FT07 : ouverture/calcul/début ARE, reliquat/option/rechargement, actualisation, engagement, avertissement et sanction, en actes séparés. Attestation employeur vers TRAV-021, rupture/CSP contractuels vers TRAV-049/050.
- [ ] Décliner RS01/02 et PA01 par prestation : foyer, résidence, ressources, période, préremplissage et correction, puis accompagnement/sanction RSA ; payeur et décideur distincts. Aucune fenêtre de ressources ou obligation d'activité commune imposée.
- [ ] Séparer CR02–CR05/07 : questions ARCE/maintien ARE, versements/reprise, cumul indépendant, demande IPR et ATI. ACRE/cotisations CR01 chez DOM-039 ; fiscalité personnelle chez DOM-011 ; aide publique à la création CR06 proposée chez DOM-010, à confirmer.
- [ ] Décliner LG01/02, FD01–FD03 et JF01/02 : logement, fin de droits ASS/RSA, rémunération/frais de formation, mobilité/garde, CEJ et prestations familiales. Compte bailleur chez DOM-006, contrat de formation chez DOM-027, fixation de pension chez DOM-013.
- [ ] Séparer SA01–SA04 : IJ, C2S, paiement caisse distinct de reconnaissance handicap DOM-025, secours locaux/FSL avec règlement territorial et nature prêt/subvention.
- [ ] Séparer IN01–IN05 et CT01/02 : lecture d'indu, prescription, contestation, remise/échéancier/retenues, contrainte, contrôle et pénalité. Dette, sanction, erreur et fraude ne se déduisent pas les unes des autres. Position sur dette demandée avant tout brouillon de remise ; ses effets restent à vérifier selon régime.
- [ ] Décliner RC01/02 : voies préalables, silence, juridiction, médiation éventuelle obligatoire et urgence propres à chaque décision. Aucune CRA, juridiction ou durée commune aux décisions CAF, France Travail ou département. Procédures spécialisées à découper avec DOM-010/EXIST-006 selon attribution.

Scénarios supplémentaires **attendus, non exécutés** : ancienne ARE reprise
alors qu'une option est envisagée ; correction d'un net social mais indu non
contesté ; micro-entreprise et SASU sans rémunération traitées selon leurs
pièces propres ; RSA suspendu avec référents multiples ; AAH reconnue mais
paiement refusé ; APL reçue par le bailleur sans imputation ; dette incertaine
avec formulaire de remise ; contrainte pendant médiation et ressources vitales
interrompues. Les tableaux annexés couvrent aussi trois prescriptions, neuf
objets de recours, douze repères de calendrier et dix réflexes.

Sources futures : textes d'assurance chômage/Code du travail, CASF, CSS,
CCH et textes d'application propres à chaque régime, Unédic/France Travail,
CAF/MSA, Assurance maladie, départements et règlements d'aides identifiés.
Les réformes, montants, taux et délais du guide ne sont pas validés ici.
[Contrôles et portée](dom-012-annexes/dom-012-frictions-verification.md).
