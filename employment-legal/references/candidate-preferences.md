<!-- Added by Judge FR/UE for PILOTE-004, 2026-10-15. -->

# Préférences candidat — parcours borné

Ce contrat commun à `cold-start-interview`, `customize` et `hiring-review`
concerne seulement la lecture d'une offre ou d'un contrat reçu. Il précise
l'exception candidat à la frontière de stockage BASE-008, sans changer le
helper ni adapter les parcours professionnels.

## Lire sans sauvegarder

Après chargement de `isolation.md`, lire uniquement `CLAUDE.md` du domaine
par le helper embarqué. `status: interview-required` et `content: null`
signifient ici : recueillir les faits utiles **en conversation**, puis
continuer la revue ; ils n'imposent ni entretien professionnel ni sauvegarde.
Un profil partiel, `[PLACEHOLDER]` ou `SETUP PAUSED AT` ne change pas ce choix.
Reprendre les réponses déjà confirmées, sans recommencer l'entretien pour
changer un format.

Sans exécuteur Python 3.12+, ne tenter aucune lecture ni écriture persistante
par un autre outil. Expliquer que les préférences enregistrées ne sont pas
accessibles et que la nouvelle préférence reste dans la conversation.
Continuer sur les pièces explicitement fournies et les faits donnés ; ne pas
prétendre que le profil est absent ou que la sauvegarde a réussi. En cas de
refus du helper, arrêter l'accès concerné, sans contournement ; la lecture des
pièces fournies reste possible.

## Mémoriser ou modifier une préférence demandée

1. Distinguer « pour cette réponse, en texte court » (conversation seulement)
   de « mémorise texte court » ou « modifie mon format enregistré en tableau »
   (sauvegarde demandée). Si cette intention est ambiguë, demander si elle doit
   être conservée, tout en poursuivant la lecture. Une demande explicite suffit ;
   ne pas redemander l'accord pour le même changement.
2. Montrer la préférence actuelle si elle existe, la valeur demandée et le
   chemin retourné par le helper :
   `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md`.
   Les faits confirmés en conversation restent dans la conversation à moins
   que leur conservation soit aussi demandée. Aucun champ juridique ou métier
   supplémentaire n'est nécessaire pour mémoriser un format.
3. Si le profil est absent, construire seulement le profil minimal ci-dessous
   avec la préférence demandée, puis `create CLAUDE.md` (création exclusive).
   Ne pas copier le modèle professionnel entier. Aucun champ inconnu n'a à
   être inventé ; les champs facultatifs peuvent rester absents.
4. Sinon, partir du **contenu complet relu**, modifier seulement la préférence
   visée, puis `replace CLAUDE.md --expected-sha256 <empreinte de cette lecture>`.
   Préserver les réponses, commentaires de pause, placeholders et sections
   hors demande, même si le profil contient des exemples US. Pour une ancienne
   ligne `Format / langue`, changer seulement le format et conserver la langue.
   S'il n'existe pas de préférence de lecture candidat identifiable, ajouter
   la section minimale sans réécrire les autres rubriques ; ne pas modifier un
   modèle de mémo professionnel pour changer la lecture d'une offre. En cas de
   valeurs contradictoires ou de champ ambigu, demander lequel est visé avant
   d'écrire. `--redo` ne remet pas les autres réponses à zéro.
5. Passer le contenu sur l'entrée standard comme donnée, conformément à
   `isolation.md`. Ne pas utiliser `append` pour accumuler des préférences
   contradictoires. Si `create` refuse un fichier apparu entre-temps ou si
   l'empreinte diffère, relire par le helper et comparer avant toute nouvelle
   proposition ; aucun écrasement forcé. Après succès, relire via le helper et
   comparer au contenu prévu ; ne confirmer la mémorisation qu'après ce contrôle.

Profil minimal illustratif pour la seule demande « mémorise texte court » :

```markdown
# Préférences de lecture d'embauche

## Faits et préférences de revue d'embauche

| Champ | Valeur confirmée |
|---|---|
| Format | texte court |
```

Il ne constitue pas un profil professionnel complet. Le modèle livré dans le
paquet reste un exemple de structure ; ne jamais y écrire de données privées.
Ne pas lire/créer le profil société, un registre, un journal, une archive ou
un dossier pour cette opération. Ne pas parcourir les dossiers d'autres
salariés ni chercher un profil d'une autre distribution. Ne pas activer les
dossiers ni modifier leur état existant.

## Retour à la lecture et fin de branche

Annoncer en mots courants ce qui a été mémorisé et où, ou que le format reste
limité à cette conversation. Revenir à `hiring-review` avec les faits déjà
donnés et le format demandé, sans réexiger les réponses ni une sauvegarde.
Si aucune pièce n'a encore été fournie, proposer le seul extrait utile.

Un ancien profil US reste conservé hors modification demandée, mais ni ses
exemples, ni ses règles, en-têtes ou formats professionnels ne s'appliquent
à la revue française. Le format mémorisé règle la présentation, jamais le
droit applicable. Les clauses, annexes, textes collectifs et sources qui
manquent restent à vérifier selon la méthode BASE-005 embarquée ; ne pas
annoncer le contrat conforme parce qu'une préférence est enregistrée.

Terminer explicitement la branche candidat après ce retour (ou après le bilan
si aucune revue n'est demandée). Ne pas poursuivre les étapes professionnelles
de `cold-start-interview` ou `customize` : ni profil société, ni handbook,
ni mémos de rupture, ni contrôle de portée déduit du répertoire courant.
Ne pas sonder de connecteur pour une préférence ; `--check-integrations`
n'autorise que les capacités expressément demandées, sans bilan général ni
passage à la partie 0 héritée. Sans demande précise, demander quelle capacité
vérifier et laisser les autres « non testées ».
