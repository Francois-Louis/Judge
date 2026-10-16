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

## Complément des frictions IA — 16 octobre 2026

Points 30–31, 35 et 48 de la [matrice IA](../02-plugins-existants/exist-005-frictions-utilisateurs.md) : prévoir lecture de la décision de plateforme, demande de retrait d'un contenu synthétique ou usurpé, puis contestation de modération, avec rôle et champ du service à vérifier. IA-005 garde la transparence, PRV-028/029 données et déréférencement, DOM-043 expression/image, DOM-002 la plainte pénale. URL, date, identifiants et preuve minimale avant retrait, sans rediffusion d'un contenu intime. Une boucle de tickets n'est pas un recours au fond ; pas de droit universel à un humain ou retrait garanti. Cas attendus : compte bloqué avec réponses répétées ; faux contenu intime et copies multiples avec urgence de procédure, sans attendre une date future alléguée.

Ces exigences restent à découper ou préciser ; [portée et contrôles de l'intégration](../02-plugins-existants/exist-005-frictions-verification.md).

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.


## Complément des frictions données personnelles — 16 octobre 2026

Points 21 et 26–31 de la [matrice données personnelles](../02-plugins-existants/exist-003-frictions-utilisateurs.md) : distinguer récupération/fermeture de compte et modération (ici, à découper) de l'effacement PRV-024, retrait source PRV-028 et déréférencement PRV-029. Conserver URL, date et preuve avant demande ; qualifier plateforme, éditeur et réutilisateur. Scénario attendu : compte fermé, contenu encore publié et résultat moteur persistant, avec trois objets et destinataires distincts. Les demandes de données ne promettent pas la restauration du compte ; presse → DOM-043, infraction alléguée → DOM-002. Portée et contrôles : voir la matrice.
