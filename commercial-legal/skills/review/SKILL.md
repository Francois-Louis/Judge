---
name: review
description: >
  Qualifier une demande sur un contrat ou un récit en France/UE : domaine
  principal, rôle achat/vente, tâche utile, pièces et questions décisives.
  Utiliser pour « relis ce contrat », un NDA, une souscription SaaS, un avenant,
  une échéance ou une demande de paiement/rupture. Orientation sans profil
  obligatoire ; les revues héritées non adaptées ne sont pas exécutées.
argument-hint: '[fichier | lien documentaire | texte ou récit]'
---

<!-- Modified by Judge FR/UE for COM-001, 2026-10-16, BASE-013, BASE-016 and BASE-019, 2026-10-17. -->

# /review — Comprendre la demande et choisir la suite

Produire une **fiche d'orientation**, pas une revue juridique complète.
Appliquer USAGE-001 `1.0.0`, repris dans la référence locale. Accepter un récit,
une photo lisible, un extrait ou un contrat sans profil professionnel,
abonnement ni connecteur obligatoire.

## Ressources et accès

Charger d'abord `${CLAUDE_PLUGIN_ROOT}/references/isolation.md`,
[la frontière de stockage](../../references/isolation.md), puis
[la méthode BASE-005 `1.3.0`](../../references/shared/research-citation-method.md) et
[l'orientation commerciale](../../references/orientation-commerciale.md).
Sous un cookbook, résoudre ces fichiers dans sa copie embarquée du plugin ;
aucun checkout ni autre plugin requis. Une référence indispensable absente est
un défaut de paquet à signaler, pas une lecture accomplie.

Le profil est **facultatif pour cette orientation**. Si des préférences
enregistrées sont utiles, utiliser uniquement le helper embarqué
`${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py` pour lire le profil commercial
puis, si nécessaire, les faits du profil partagé. Un profil absent
(`interview-required`), incomplet ou avec placeholders ne bloque pas la lecture
ponctuelle : ignorer les valeurs non renseignées et continuer sur les pièces et
réponses de la personne. Ce statut ne lance pas l'interview. Aucune recherche
ailleurs, import, création de profil ou écriture de registre/dossier n'en
découle. Si le helper manque ou refuse l'accès, arrêter cet accès durable et
continuer sur les entrées explicites. Les règles d'isolation restent applicables.

Drive, SharePoint ou Box peuvent fournir une pièce ; un CLM peut fournir le
contrat et ses versions. Ces accès sont **optionnels**, à constater. Si un lien
est illisible ou un accès manque, demander le fichier, l'extrait utile ou sa
retranscription et donner l'orientation conditionnelle possible sur le récit.
Ne pas explorer d'autres dossiers. DocuSign et Slack ne sont pas requis.
Sans accès aux sources officielles, réserver les conclusions de droit.
Une réserve finale ne permet pas d'énoncer auparavant une règle « de mémoire »
ou sous la rubrique « hypothèses ». Sans texte relu, garder une question à
vérifier : par exemple, « les horaires et le contrôle décrits au §7 justifient
une analyse en droit du travail ; la qualification reste à vérifier ». Ne pas
énoncer le test juridique de qualification ni l'effet d'une clause de mémoire.
Cette limite vaut dès l'introduction. Pour une facture contestée, dire
« solde arithmétique apparent, à rapprocher des pièces » ; jamais « le client
doit sans doute » avant d'avoir vérifié la créance. Pour un NDA, demander à
qui les clauses imposent des obligations sans présumer la partie protégée,
leur validité, leur caractère inhabituel ou leur effet favorable. Deux parties
françaises ne suffisent pas à exclure une question de loi applicable : relever
les rattachements manquants et réserver cette question.

## Parcours

1. **Comprendre l'objectif et l'urgence.** Lire les entrées avant de questionner.
   Distinguer expliquer, préparer une revue, suivre une échéance, demander un
   paiement ou préparer une rupture. Relever acte, convocation ou intervention
   datée et sa provenance ; aucun calcul de délai légal par défaut. Une tâche
   procédurale urgente peut passer avant le fond.
2. **Titres, puis substance utile.** Relever titre principal, annexes, avenants,
   commandes et documents incorporés. Lire ensuite parties, objet réel,
   engagements de chacun, prix/paiement, dates/durée, loi et juge, ainsi que les
   passages nécessaires pour lever les ambiguïtés. Pas de limite arbitraire
   aux deux premières pages. Un titre MSA, une clause confidentielle ou le mot
   « consultant » ne décide pas du régime. Indiquer pages/sections lues,
   absentes ou illisibles ; une annexe citée n'est pas réputée fournie/acceptée.
3. **Qualifier pour cet acte.** Qui achète et qui fournit, pour quel usage, où
   et quand ? Distinguer professionnel, consommateur ou non-professionnel à
   vérifier. Ne déduire le côté ni du statut du demandeur ni de l'auteur du
   modèle. Examiner secteur spécial, emploi possible, procédure et exécution
   selon la référence locale. Si un fait change le domaine, garder les branches
   conditionnelles et poser une ou deux questions à la fois. Aucun questionnaire
   complet ni approbateur d'entreprise inventé.
4. **Séparer les rattachements.** Restituer (a) loi indiquée et loi applicable
   à vérifier, (b) juge/arbitrage indiqué et compétence à vérifier, (c) préférence
   de négociation déclarée. Langue, adresse française et playbook ne prouvent
   aucune des deux premières. Relever territoires précis, établissements et
   dates utiles ; vérifier sources, versions et applicabilité selon BASE-005
   pour les propositions de droit nécessaires. Les repères locaux restent à
   recontrôler pour le dossier. Sans source, conserver les faits et pièces
   utiles, sans règle américaine de remplacement.
5. **Choisir le domaine et la tâche.** Expliquer en mots ordinaires la raison et
   l'état réel de la branche dans la table locale. Un complément données,
   emploi ou autre demande sa question, ses pièces minimales et son
   interlocuteur ; ne pas charger tous les plugins. **Ne lancer aucun skill
   hérité non adapté**, même avec profil complet ou `confirm_routing: false`.
   Une tâche proposée n'est pas une commande disponible. Fournir la préparation
   factuelle utile lorsque la revue métier reste indisponible.
6. **Rendre la fiche et s'arrêter.** Adapter langue et format à la personne.
   Aucun appel automatique de revue, escalade, résumé, redline, CLM ou registre.
   Pour une future branche adaptée, vérifier bilan et présence avant un appel
   distinct. `confirm_routing` concerne cet appel ultérieur : valeur explicite
   du profil, sinon `true`. Ne pas demander confirmation pour l'orientation
   déjà demandée. Cette préférence ne vaut ni adaptation ni autorisation externe.

## Fiche à rendre

Commencer par quelques phrases accessibles sans formation juridique :

- **Demande et pièces** : objectif, auteur de la demande, rôles, objet et
  engagements des deux parties, avec fichier/page/clause ou attribution au récit.
  Ne pas présumer un abus ni une somme juridiquement due.
- **Orientation et suite** : domaine principal, achat/vente si pertinent,
  tâche en mots courants, état adapté/hérité/proposé ou disponibilité inconnue,
  question et interlocuteur utile. L'orientation ne valide pas le contrat.
- **À vérifier** : distinguer faits manquants, clauses observées, hypothèses de
  droit et préférences. Séparer loi, juge et souhait. Citer les sources
  déterminantes avec version, date de lecture réelle et applicabilité motivée,
  ou préciser qu'elles n'ont pas été vérifiées et réserver la conclusion.
- **Pièces et prochaine étape** : extraits ciblés, utilité, données masquables,
  une ou deux questions décisives et à qui les poser. Dates écrites/déclarées/
  prouvées distinctes ; échéance juridique à déterminer sans régime/déclencheur
  vérifiés. Aucun envoi, signature, inscription, rappel ou protection par le
  secret professionnel annoncé sans preuve.

**Portée et interlocuteur** (section 8 de la méthode `1.3.0`). Si la demande
comporte délai, acte de procédure, convocation ou mesure pénale, signature
imminente ou enjeu irréversible, ouvrir la fiche par une ou deux phrases :
ce qui presse et qui contacter rapidement, sans calcul de délai. Terminer
toujours par une phrase courte : la fiche aide à comprendre la demande et à
préparer la suite ; elle ne remplace pas l'avis de l'interlocuteur compétent
nommé pour la branche retenue (référence locale, dernière colonne). En pénal,
nommer l'avocat ; l'officier de police judiciaire est une autorité, pas un
conseil. Pour les frais d'un notaire, nommer le notaire puis l'instance de la
profession ou un médiateur à identifier, sans avocat par défaut.

Livrer dans la conversation. Une conservation expressément demandée utilise
le helper et une destination isolée validée, jamais le paquet installé.
