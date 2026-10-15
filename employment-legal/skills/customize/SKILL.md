---
name: customize
description: >
  Guided customization of your employment practice profile — change one thing
  without re-running the whole cold-start interview. Adjust jurisdictional
  footprint, risk posture, escalation contacts, hiring review rules,
  termination review rules, handbook positions, investigation preferences,
  or matter workspace paths. Use when the user says "change my [thing]",
  "add a jurisdiction", "update my profile", "edit my config", or "customize".
argument-hint: "[section name, or describe what you want to change]"
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /customize

<!-- Modified by Judge FR/UE for PILOTE-002 (2026-10-15): hiring-only configuration. -->

## Champs du pilote revue d'embauche France

Pour un candidat/salarié ou une modification de `hiring-review`, appliquer
cette branche avant le parcours professionnel hérité : lire seulement le
profil du fork via le helper. Le profil société n'est pas requis. L'absence
de profil ou les champs professionnels non renseignés ne bloquent pas la
lecture du contrat : proposer le chemin court de `cold-start-interview` si
la personne veut conserver ses préférences, ou poursuivre en conversation.

Afficher uniquement les champs utiles de la section PILOTE-002 : rôle/besoin,
format, lieux/dates, contrat, fonctions, textes collectifs mentionnés et
interlocuteur. Modifier le champ demandé sur les faits confirmés, préserver
le reste et écrire via le helper avec l'empreinte relue. Ni APE ni titre de
poste ne détermine une CCN ; ni « cadre » ni salaire ne détermine un forfait.
Une règle annoncée dans le profil reste à vérifier selon la méthode locale.
Ne pas introduire at-will, exempt, barème ou en-tête américain, ni politique
maison obligatoire. Une modification de lieu peut nécessiter une orientation
hors du cas nominal. Aucun changement ne rend les autres skills adaptés.
Ne pas créer de profil société, de registre ou de suivi pour cette modification.

Les instructions suivantes concernent les autres parcours, hérités et non adaptés.

## When this runs

The user typed `/judge-fr-eu-employment-legal:customize`. They want to change something
in their practice profile — a jurisdiction, a risk posture, an escalation
contact, a handbook position — without re-running the whole cold-start
interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md`
   (and `~/.claude/plugins/config/judge-fr-eu/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/judge-fr-eu-employment-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, practice setting, jurisdictions
     *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Jurisdictional footprint** — states (and countries) where employees
     work, single-state vs. multi-state, and any upcoming expansion. This
     drives state-specific supplement logic.
   - **Risk posture** — conservative / middle / aggressive, what each means
     for flagging termination risk, restrictive covenant enforceability, and
     leave accommodation
   - **People** — HR partners, people team lead, outside counsel, escalation
     chain, investigation sponsor
   - **Hiring review** — utiliser la branche PILOTE-002 ci-dessus : faits,
     textes collectifs mentionnés et préférences de restitution, sans règle US
   - **Termination review** — severance framework, release language, final
     pay timing rules per state, high-risk flags
   - **Handbook** — handbook file path, state supplements approach, review
     cadence
   - **Investigation preferences** — privileged labeling, interview protocol,
     audience-specific summary templates
   - **Workflow** — matter workspaces, leave tracker cadence, expansion
     project paths
   - **Integrations** — HRIS / Slack / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding Washington to the jurisdictional footprint:* "`/wage-hour-qa`
     and `/termination-review` will start applying WA rules. `/handbook-
     updates` will prompt for a WA supplement. La revue d'embauche française
     orientera ce cas hors de son périmètre ; elle n'applique pas le droit de WA."
   - *Severance framework 2 weeks/year → 4 weeks/year:* "`/termination-
     review` will use the new baseline in severance calculations."
   - *Risk posture middle → conservative:* "I'll flag more terminations for
     escalation, recommend more protective release language, and be stricter
     on restrictive covenants."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/judge-fr-eu/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/judge-fr-eu-employment-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a jurisdiction,
  offer to mark it `[Not currently staffed — retain rules for re-entry]` and
  explain that going to `[Not configured]` will drop state-specific
  flagging.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., CA in the footprint + aggressive non-compete posture;
  or risk posture aggressive + "every termination goes to outside counsel"),
  flag the tension.
- **Flag guardrail degradation.** The pre-flight citation check, source
  attribution tags, and `[verify]` tags on cited statutes are load-bearing —
  do not remove. The `[review]` flag is load-bearing — explain the trade-off
  before adjusting.
- **One change at a time.** Don't re-ask the whole interview.
