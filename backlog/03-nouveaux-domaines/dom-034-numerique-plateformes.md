---
id: DOM-034
titre: "Cadrer un plugin numérique et plateformes du quotidien"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-034 — Cadrer un plugin numérique et plateformes du quotidien

## Objectif

Aider les utilisateurs à comprendre une suspension de compte, une décision de modération ou un litige avec un service numérique.

Nom de plugin proposé : `digital-rights-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire une notification de suspension, de retrait ou de restriction et préparer une contestation.
- Organiser une demande sur une publication ou une usurpation d'identité en ligne.
- Qualifier le rôle d'une plateforme dans un litige et identifier le bon interlocuteur.

## Qualification et frontières

Service, rôle, pays, qualité d'utilisateur/professionnel, compte, décision, notification, contenu, conditions et mécanismes internes disponibles.

Les décisions et responsabilités du service numérique sont ici ; accès/effacement des données restent dans privacy-legal, droit d'auteur dans ip-legal, achat non livré en DOM-001, débit en DOM-004 et harcèlement pénal en DOM-002.

## Sources à prévoir et vérifier

Textes français et UE applicables aux services numériques, Code civil, consommation selon le contrat, CNIL/ARCOM et autorités désignées selon le champ.

- [ARCOM](https://www.arcom.fr/)
- [Commission — stratégie numérique](https://digital-strategy.ec.europa.eu/fr)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une notification de suspension et préparer une contestation interne pour un type de service choisi.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage vérifie rôle et champ des obligations ; il ne promet pas une restauration de compte ou un retrait et ne traite pas toute plateforme comme un hébergeur identique.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un compte est fermé avec un motif peu clair.
- Une identité est utilisée pour ouvrir un faux profil.
- Une plateforme et un vendeur se renvoient la responsabilité d'une commande.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

