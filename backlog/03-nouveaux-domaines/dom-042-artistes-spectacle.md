---
id: DOM-042
titre: "Cadrer un plugin artistes-auteurs et intermittents du spectacle"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-042 — Cadrer un plugin artistes-auteurs et intermittents du spectacle

## Objectif

Aider un artiste-auteur ou un intermittent du spectacle à comprendre son
statut, ses cotisations, son imposition, ses contrats d'engagement et son
indemnisation, et à préparer une démarche auprès de l'organisme concerné.
Ajouté le 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

Nom de plugin proposé : `arts-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Artiste-auteur : lire un appel ou une régularisation de cotisations, comprendre le précompte par le diffuseur et l'affiliation, préparer une demande de correction.
- Artiste-auteur : identifier le régime d'imposition des revenus artistiques à vérifier, sans calcul.
- Intermittent : lire un contrat d'engagement (contrat à durée déterminée d'usage, guichet unique pour les employeurs occasionnels), une fiche de paie et les congés spectacles.
- Intermittent : lire une décision ou un courrier de France Travail sur l'indemnisation au titre des annexes propres au spectacle et préparer la réponse.

## Qualification et frontières

Statut réel (artiste-auteur, artiste interprète salarié, technicien, cumul
des deux, micro-entrepreneur), activité, diffuseurs et employeurs, contrats,
heures ou cachets, revenus déclarés, organismes et courriers reçus.

Le statut et ses démarches sont ici. Droits sur les œuvres, contrats d'édition
ou de production, gestion collective et droit moral → `ip-legal` (PI-026 à
PI-029) ; relation de travail ordinaire et rupture → travail privé ; autres
prestations de la CAF et minima sociaux → DOM-012 ; impôts du foyer hors
revenus artistiques → DOM-011 ; activité exercée en micro-entreprise →
DOM-039 ; retraite → DOM-036 ; acte de saisie → DOM-003.

## Sources à prévoir et vérifier

Code de la sécurité sociale (artistes-auteurs), Code du travail (artistes du
spectacle, contrats d'usage), règlement d'assurance chômage et ses annexes
propres au spectacle, Code général des impôts ; URSSAF, France Travail,
caisse des congés spectacles et guichet unique comme sources d'information.

Les guides orientent le cadrage ; les textes et versions applicables seront
vérifiés lors de chaque implémentation, les règles d'indemnisation évoluant
par accords successifs.

## Première tranche proposée

Lire un courrier de France Travail adressé à un intermittent du spectacle et
repérer décision, période, heures retenues, pièces et voie de réponse.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son courrier ou de son contrat sans connaître son régime.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières avec `ip-legal`, le travail privé, DOM-012 et DOM-039 évitent les doublons.
- [ ] Aucun seuil d'heures, taux, cotisation ou montant affirmé sans texte lu et date établie.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une illustratrice qui reçoit une régularisation de cotisations sur ses droits d'auteur.
- Un technicien du spectacle dont des cachets n'ont pas été pris en compte par France Travail.
- Un musicien à la fois artiste-auteur pour ses compositions et salarié intermittent pour ses concerts.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas
résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, gérer la paie d'un employeur du spectacle, faire les
déclarations à la place de la personne ou traiter les droits sur les œuvres.
