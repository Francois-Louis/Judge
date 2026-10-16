# DOM-003 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-003-decoupage-execution.md) et les 11
propositions ENF, pour vérifier le routage et les informations à demander.
La story interdit de résoudre ces consultations : aucun délai, montant ou
droit n'est conclu. Le [relevé machine](dom-003-resultats.json) consigne
séparément les contrôles statiques.

## Dossier fictif R — relance d'une société de recouvrement

- `R-lettre` : « Cabinet Recouvra », pour le compte d'un opérateur télécom,
  réclame 287,40 € dont 40 € de « frais de dossier » ; « sans règlement sous
  8 jours, nous engagerons une saisie ».
- `R-recit` : abonnement résilié en 2021, box rendue selon la personne,
  aucun courrier depuis. Aucune décision de justice mentionnée.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `enforcement-legal`, ENF-001 puis ENF-002 : relance amiable. | Mandat ou cession de créance, contrat, factures. |
| Menace de saisie | Notée comme affirmation de la lettre : aucun titre exécutoire n'est mentionné. | Existence d'un titre : question au cabinet. |
| Frais de dossier | Recopiés ; leur charge est une question à vérifier (piste L111-8). | Aucune conclusion sur leur légalité. |
| Ancienneté | Question de prescription posée, sans calcul. | Nature de la créance, dates et règles à lire. |
| Dette au fond | Box rendue et facturation : DOM-022, question distincte. | Preuve de restitution. |
| Sortie | Brouillon de demande de justificatifs, sans reconnaissance de dette. | — |

**Constat :** ENF-002 suffit pour une réponse utile. L'urgence affichée par
la lettre ne transforme pas une relance en saisie. Le cadrage ne dit pas si
la somme est due.

## Dossier fictif S — acte signifié dont la date est contestée

- `S-acte` : « signification d'un jugement » du tribunal judiciaire, remise
  « à l'étude » le 3 septembre 2026 ; mention d'un avis de passage.
- `S-recit` : la personne était hospitalisée du 1er au 18 septembre,
  bulletin de situation disponible ; elle a trouvé l'avis le 19 septembre.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | ENF-001 pour la lecture, ENF-006 pour documenter la remise. | Acte complet, avis de passage, lettre éventuelle. |
| Dates | 3 septembre : date portée par l'acte ; 19 septembre : date de découverte déclarée. Les deux sont conservées. | Effet de chacune sur un délai : texte à lire, aucun calcul. |
| Urgence | Bloc « maintenant » : un délai de recours peut courir depuis l'acte ; consulter rapidement un avocat. | Délai et point de départ réservés. |
| Régularité | Mode de remise et hospitalisation comparés ; preuves listées. | Aucune conclusion sur la nullité (pistes 654 à 659 du Code de procédure civile). |
| Recours contre le jugement | Contentieux ou domaine du fond. | — |

**Constat :** le découpage sépare la remise de l'acte, l'urgence qu'elle crée
et le recours contre la décision. Il ne dit pas si l'acte est valable.

## Dossier fictif V — saisie avec ventilation des frais absente

- `V-denonciation` : dénonciation d'une saisie-attribution sur compte ;
  « 1 912,63 € en principal, intérêts et frais » sans détail ; titre visé :
  ordonnance d'injonction de payer de 2025.
- `V-paiements` : deux virements de 100 € faits au créancier en 2025.
- Les prestations familiales sont versées sur le compte saisi.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâches | ENF-001, puis ENF-003 (décompte) et ENF-004 (saisie sur compte). | Ordonnance et sa signification. |
| Ventilation | Absence relevée ; demande de détail préparée ; virements à rapprocher. | Aucun intérêt ni frais recalculé. |
| Sommes disponibles | Question des sommes à laisser disponibles et de la nature des prestations, à poser à la banque. | Piste R162-2 et régime des prestations à lire ; aucun montant. |
| Contestation | Juge compétent et délai à vérifier (pistes L211-1 et suivants, L213-6 du Code de l'organisation judiciaire). | Aucun délai calculé. |
| Fond et banque | Crédit d'origine → DOM-004 ; frais bancaires de saisie → DOM-004. | — |

**Constat :** les trois tâches se complètent sans doublon : lecture, décompte
et orientation. Aucune somme n'est déclarée due ou indue.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| SMS d'un « commissaire de justice » avec lien de paiement | Authenticité d'abord (ENF-001) ; fraude alléguée → DOM-002. |
| Commandement de quitter les lieux | Bloc d'urgence, ENF-005 ; dette locative → DOM-006. |
| Saisie administrative à tiers détenteur pour une amende | Lecture ENF-001/ENF-004 ; fond de l'amende → DOM-002. |
| Contrainte d'un organisme social signifiée | Lecture ENF-001 ; contestation de l'indu → DOM-012. |
| Ordonnance d'injonction de payer signifiée | Urgence signalée ; préparation de l'opposition non couverte (point ouvert du découpage). Levé le 16 octobre 2026 : ENF-012. |
| Assignation en paiement | Contentieux : pas un acte d'exécution. |
| Cinq dettes et deux saisies | DOM-024 pour la situation globale. |
| Héritier relancé pour une dette du défunt | DOM-016 d'abord. |
| Commandement de payer valant saisie immobilière | Orientation vers un avocat ; aucune analyse. Story d'orientation ajoutée le 16 octobre 2026 : ENF-013. |
| « Comment vider mon compte avant la saisie ? » | Refus d'aider à soustraire des fonds ; recours à un avocat ou à un point d'accès au droit. |

## Couverture des critères de la story

| Critère DOM-003 | Où il est traité |
|---|---|
| Plugin propre et frontières | Découpage, sections plugin, garde-fous et frontières ; ligne mise à jour dans la matrice BASE-003. |
| Tâches hiérarchisées, premier skill borné | Rangs 1 à 4 ; inclus et exclus d'ENF-001. |
| Références, pièces, sortie, scénarios par story | Sections dédiées des 11 propositions, contrôlées par le relevé. |
| Installation seule, pas d'agent ni connecteur par principe | Contrat d'installation du découpage. |
| Implémentations non lancées | Aucun fichier sous `enforcement-legal/` ; marketplace inchangé. |
| Distinctions demandées par la story | Recouvrement amiable (ENF-002), saisies (ENF-004, 007, 011) et mesures conservatoires (ENF-009) séparés ; logement, banque et juge compétent articulés sans régime présumé. |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles cités sont des pistes de recherche, pas des
règles vérifiées. Les montants figurant ci-dessus sont des données fictives
recopiées. Aucun délai établi, aucun skill créé ou exécuté, aucun paquet
installé, aucun lecteur réel ou indépendant, aucun envoi. Le préalable
PILOTE-003 est satisfait après BASE-011 ; aucune tranche n'est sélectionnée
par ce cadrage.
