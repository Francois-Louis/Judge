---
name: customize
description: >
  Guided customization of your Legal Builder Hub profile — change one thing
  without re-running the whole cold-start interview. Adjust practice profile,
  installed starter pack, watched registries, update preferences, or QA
  strictness. Use when the user says "change my [thing]", "add a registry",
  "update my profile", "edit my config", or "customize".
argument-hint: "[section name, or describe what you want to change]"
---

For every community lifecycle operation, first load `${CLAUDE_PLUGIN_ROOT}/references/community-lifecycle.md`. Its helper owns installation, updates, backups, rollback, disabling, enabling, uninstall and the fork journal.

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. BASE-009 (2026-10-15): updates are never applied automatically. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /customize

## When this runs

The user typed `/judge-fr-eu-legal-builder-hub:customize`. They want to change something
in their Builder Hub profile — a watched registry, update notification
preferences, a practice area for recommendations — without re-running the
whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/judge-fr-eu/legal-builder-hub/CLAUDE.md`
   (and `~/.claude/plugins/config/judge-fr-eu/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/judge-fr-eu-legal-builder-hub:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Your practice profile** — practice areas in scope, used to recommend
     community skills
   - **Installed starter pack** — which plugins and skills are installed via
     the hub, with install source
   - **Watched registries** — GitHub repositories / URLs the hub pulls
     community skills from
   - **Update preferences** — check cadence (daily / weekly / on demand),
     notification channel (Slack / in-session), notify vs. manual
     (there is no automatic-apply mode)
   - **QA strictness** — how aggressively `/skills-qa` flags issues on a candidate
     skill before install (lenient / middle / strict), and which
     failure-mode checks are on
   - **Skill install defaults** — install scope (user / project), whether
     to run `/skills-qa` automatically before install
   - **Integrations** — Slack / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new watched registry:* "`/registry-browser` will search this registry
     alongside the existing ones. `/auto-updater` will check it on its next run."
   - *QA strictness strict → middle:* "`/skills-qa` will report the same findings
     but not block install on the medium band unless you confirm."
   - *Update preference notify → manual:* "The hub will only list available
     updates. Each one still needs a diff review and your explicit approval."
   - *Request to enable auto-update:* refuse the setting and explain: "There
     is no automatic-apply mode. Every update shows its diff and needs your
     approval."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/judge-fr-eu/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/judge-fr-eu-legal-builder-hub:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a watched
  registry, offer to mark it `[Paused]` and explain that pausing keeps the
  install history but stops update checks.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., notify off + QA strictness off; or practice
  profile that doesn't match any installed plugin), flag the tension.
- **Flag guardrail degradation.** The Legal Skill Design Framework checks
  (nine design parameters, three legal failure modes, trust-surface check)
  are what `/skills-qa` exists to run — turning them off defeats the point. If the
  user wants to lower strictness, recommend the middle band rather than
  disabling the check.
- **One change at a time.** Don't re-ask the whole interview.
