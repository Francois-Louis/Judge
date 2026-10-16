---
id: DOM-043
titre: "Cadrer un plugin médias et expression publique"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-043 — Cadrer un plugin médias et expression publique

## Objectif

Aider une personne atteinte par une publication, une personne mise en cause
pour un propos publié, un journaliste ou un créateur de contenu, et un petit
média ou site, à comprendre la situation, l'urgence et la démarche utile.
Ajouté le 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

Nom de plugin proposé : `media-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- **Personne atteinte** : documenter une publication (article, vidéo, message) avec date, auteur, support et preuve ; distinguer diffamation, injure, atteinte à la vie privée et à l'image, fausse information ; préparer une demande de retrait, de rectification ou un droit de réponse ; orienter vers le déréférencement.
- **Personne mise en cause** : lire une demande de retrait, un droit de réponse reçu, une mise en demeure ou une plainte pour un propos publié ; repérer l'urgence et les pièces ; préparer une réponse factuelle.
- **Journalistes et créateurs** : statut de journaliste et de pigiste, carte de presse, secret des sources ; créateur de contenu rémunéré et ses obligations de transparence.
- **Petits médias et sites** : obligations d'une publication ou d'un site (mentions légales, directeur de publication, droit de réponse à insérer, commentaires) et règles audiovisuelles selon le service.

## Qualification et frontières

Rôle de la personne (visée, auteur, éditeur, hébergeur, journaliste, créateur),
support et service, date de première publication, lieu de diffusion, propos
exacts et contexte, notoriété ou fonction publique de la personne visée,
démarches déjà engagées.

L'expression publique et le droit de la presse sont ici, avec leurs procédures
et délais propres, qui sont souvent très courts : l'urgence est traitée en
premier, sans délai calculé. Modération et suspension de compte par une
plateforme → DOM-034 ; données personnelles et déréférencement au titre du
RGPD → `privacy-legal` ; droit d'auteur sur un contenu → `ip-legal` ;
harcèlement, menaces et procédure pénale générale → DOM-002 ; contrat de
travail d'un journaliste salarié au quotidien → travail privé ; influence
commerciale d'une marque → `product-legal` (PDT-009) ; préjudice hors presse →
DOM-035.

## Sources à prévoir et vérifier

Loi du 29 juillet 1881 sur la liberté de la presse, Code civil (vie privée,
image), loi pour la confiance dans l'économie numérique, loi du 30 septembre
1986 relative à la liberté de communication, Code du travail (journalistes),
textes sur l'influence commerciale, règlement européen sur les services
numériques selon le service ; ARCOM, commission de la carte d'identité des
journalistes professionnels et jurisprudence comme sources à vérifier.

Les guides orientent le cadrage ; les textes et versions applicables seront
vérifiés lors de chaque implémentation, notamment les règles de prescription
et de procédure propres à la presse.

## Première tranche proposée

Documenter une publication qui atteint une personne et repérer la qualification
possible, l'urgence liée à la date de publication et la démarche utile
(retrait, droit de réponse, plainte), sans conclure sur l'infraction.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de la publication ou du courrier reçu sans connaître la qualification.
- [ ] L'urgence liée aux délais propres à la presse est signalée sans délai calculé ni qualification présumée.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières avec DOM-034, privacy, ip, DOM-002 et le travail évitent les doublons.
- [ ] La sortie respecte l'avertissement BASE-013, avec un avocat nommé quand une procédure de presse est envisagée.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un article local qui prête à un artisan des faits qu'il conteste, publié il y a plusieurs semaines.
- Une habitante qui reçoit une mise en demeure pour un avis négatif publié en ligne.
- Un photographe pigiste à qui un journal refuse le statut de journaliste.
- Une association qui lance un petit site d'information et ne sait pas qui est directeur de publication.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas
résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, rédiger un article, juger de la vérité d'une
information, conseiller une stratégie médiatique ou aider à publier un propos
illicite.
