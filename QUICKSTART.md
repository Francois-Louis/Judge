<!-- Modified by Judge FR/UE for BASE-008, 2026-10-15. -->

# Démarrer avec Judge FR/UE 0.1.0

Le marketplace du fork s'appelle `judge-fr-eu`. Cette version isole les
identifiants et les configurations. Les tâches juridiques héritées de Claude
for Legal / Anthropic restent à adapter à la France et à l'Union européenne.
Le fork est maintenu sur [Francois-Louis/Judge](https://github.com/Francois-Louis/Judge),
sans affiliation revendiquée à Anthropic. Voir [NOTICE](NOTICE) et [LICENSE](LICENSE).

Depuis un terminal, avec un chemin absolu vers une copie revue du fork :

```text
claude plugin marketplace add <chemin-absolu-vers-Judge>
claude plugin install judge-fr-eu-privacy-legal@judge-fr-eu --scope user
```

Dans `/plugin`, onglet Marketplaces, sélectionner `judge-fr-eu` et vérifier
que la mise à jour automatique est désactivée. Ne pas éditer à la main les
registres du client. Recharger les plugins ou redémarrer la session, puis :

```text
/judge-fr-eu-privacy-legal:cold-start-interview
/judge-fr-eu-privacy-legal:use-case-triage
```

Le nom publié est `judge-fr-eu-` suivi du répertoire de domaine existant.
Les noms des 150 skills restent les mêmes ; le [README](README.md) donne les
commandes qualifiées des douze domaines. CoCounsel est exclu du marketplace
du fork ; son installation relève de la distribution d'origine.

La portée `user` rend le plugin disponible dans tous les projets. Elle
n'accorde pas de permissions de fichiers supplémentaires et ne remplace pas
les contrôles d'accès du client. Choisir explicitement `project` ou `local`
si c'est la portée voulue ; les profils du fork gardent le même namespace.
La coexistence dans Cowork, Office et les autres clients reste à tester.

Python 3.12 ou ultérieur est requis pour les assistants de stockage embarqués.
Les profils vivent dans
`~/.claude/plugins/config/judge-fr-eu/<domaine>/CLAUDE.md`, le profil partagé
dans `~/.claude/plugins/config/judge-fr-eu/company-profile.md`. Dossiers,
archives, sorties et journaux restent sous la racine du domaine du fork.
Les accès passent par l'[assistant de stockage](references/isolation.md).

Un profil absent déclenche un entretien neuf. Un profil existant, ses réponses
et son état de pause sont conservés. Aucun profil, cache, dossier ou réglage
juridique d'une autre distribution n'est repris automatiquement. L'import
assisté nécessiterait une story distincte.

L'original conserve ses identifiants, par exemple
`employment-legal@claude-for-legal`, distincts de
`judge-fr-eu-employment-legal@judge-fr-eu`. Ne pas retirer son marketplace ni
remplacer son installation pour ajouter le fork. La [recette BASE-008](references/base008-validation.md)
distingue les vérifications hors ligne de la coexistence réelle restant à
exécuter dans un client jetable.

Mettre à jour uniquement le paquet du fork revu, à portée explicite. Profils et
dossiers durables sont hors du cache ; un retour au paquet précédent doit les
préserver. Garder les personnalisations dans le profil ou dans une branche/paquet
privé à identifiant distinct. Une modification directe du cache est remplaçable.

Le hub installe les skills communautaires dans
`~/.claude/skills/judge-fr-eu-<skill>/`, avec identité préfixée et journal du
fork. Ses opérations passent par l'assistant après les contrôles de confiance
et l'accord prévu par le workflow. Voir le [contrat du hub](legal-builder-hub/references/community-lifecycle.md).
