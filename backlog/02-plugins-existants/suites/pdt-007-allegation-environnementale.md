---
id: PDT-007
titre: "Examiner une allégation environnementale précise"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-005]
---

# PDT-007 — Examiner une allégation environnementale précise

## Objectif et résultat attendu

Une petite entreprise reçoit une fiche d'examen d'une allégation environnementale de sa publicité France, les preuves manquantes et les options de suppression ou rédaction bornée.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/marketing-claims-review/SKILL.md (branche environnementale)`
- `product-legal/references/allegation-environnementale.md (à créer)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Allégation et contexte PDT-005 ou équivalent, captures/labels/mentions, produit/emballage/activité, public et canal, marché/date, étude et méthode, périmètre de cycle de vie, comparaison, compensation et organisme émetteur du label si invoqués.

## Travail attendu

Examiner une allégation et ses variantes de présentation sur un support, notamment « écoresponsable », « 100 % recyclable », « neutre en carbone ». Distinguer périmètres, effet réel, compensation et preuve ; une seule propriété de l'emballage ne prouve pas le produit entier. Rechercher textes et transitions applicables à la date de campagne, statut exact des initiatives UE et règles françaises pertinentes. Préparer une fiche citation/preuve/écart/question, puis reformulation uniquement si justifiée ou proposition de retrait. Ne pas substituer Green Guides, label privé ou guide ADEME à une obligation légale.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher Code de la consommation, dispositions françaises environnement/publicité/neutralité carbone et actes UE effectivement dans le champ, versions/transposition/application ; DGCCRF, ADEME et jurisprudence comme sources de portée distincte. Toute initiative dite Green Claims reste à qualifier adopté/proposé et applicable à la date considérée.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] La portée de l'étude est confrontée à produit/emballage/activité et au message global, visuels compris.
- [ ] Un bilan partiel ou une compensation ne devient pas preuve suffisante d'une neutralité globale.
- [ ] La fiche expose statut et date des textes réellement lus ; une réforme annoncée n'est pas appliquée par anticipation.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : E01 — « Emballage contenant X % de matière recyclée », justificatif daté portant sur cet emballage : examen ciblé sans avis sur tout le produit.
- Cas limite : E02 — « Carnet 100 % écoresponsable et neutre en carbone », feuille verte, preuve du seul carton et promesse de compensation : périmètres et justificatifs manquants, pas de conformité ni retouche magique.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-annexes/exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Analyse de cycle de vie réalisée par le skill, calcul d'empreinte, certification/label, revue ESG de l'entreprise et publication.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.

## Complément de besoins — 16 octobre 2026

Les points 76 à 87 de la [matrice marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md) précisent allégation générique, visuel vert, label privé, obligation présentée comme avantage, périmètre partiel et objectif futur sans plan. Rechercher le statut de transposition français et la disposition applicable de la directive 2024/825 ; ni application intégrale ni transposition inachevée ne sont admises depuis le texte utilisateur. Conserver aussi les règles françaises préexistantes, dont les mentions et la neutralité carbone selon champ. Recette attendue : campagne à une date proche d’une transition non vérifiée → état des textes et réserves, pas de date automatique.

Ces exigences et scénarios restent proposés, sans règle ou résultat métier validé par cette intégration.
