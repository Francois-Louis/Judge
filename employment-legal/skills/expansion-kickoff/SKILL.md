---
name: expansion-kickoff
description: >
  Kick off international expansion planning for a new country — gathers intake,
  runs EOR vs. entity framing, drafts cross-functional questions, surfaces
  country-specific flags, and creates a persistent tracker. Use when someone
  says "we're hiring in [country]", "expansion to [country]", or "first hire
  in [country]".
argument-hint: "[country name]"
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /expansion-kickoff

Starts an international expansion project for a new country — gathers intake,
runs EOR vs. entity framing, drafts cross-functional questions, surfaces
country-specific flags, and creates a persistent tracker.

## Instructions

1. Load `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md` → jurisdictional footprint, escalation table.
2. Load the `international-expansion` reference skill and run the full workflow.
3. If a tracker file already exists for this country (`~/.claude/plugins/config/judge-fr-eu/employment-legal/expansion-[slug].yaml`),
   flag it: "An expansion tracker for [country] already exists. Use
   `/judge-fr-eu-employment-legal:expansion-update [country]` to update it, or confirm
   you want to start over."
4. Create `~/.claude/plugins/config/judge-fr-eu/employment-legal/expansion-[slug].yaml` on completion.

## Examples

```
/judge-fr-eu-employment-legal:expansion-kickoff Germany
```

```
/judge-fr-eu-employment-legal:expansion-kickoff
(skill will ask which country)
```

> Detailed EOR vs. entity framework, cross-functional questions, briefing
> templates, and tracker schema live in the `international-expansion`
> reference skill — load it before doing substantive work.
