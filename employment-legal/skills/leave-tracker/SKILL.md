---
name: leave-tracker
description: >
  Check open leaves for deadline alerts and required decisions. Surfaces only
  the leaves that require an action and explains why — not a status board.
  Use weekly, or whenever the attorney needs to know which leaves have
  upcoming designation, certification, or exhaustion deadlines.
argument-hint: "[no arguments — works from HRIS or leave-register.yaml]"
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /leave-tracker

Checks all open leaves with hard legal deadlines and surfaces only the ones
requiring a decision or action. Not a status board — tells you what you need
to do and why.

## Instructions

1. Load the `leave-tracker` agent and run the full workflow.

2. If no HRIS is connected and no `~/.claude/plugins/config/judge-fr-eu/employment-legal/leave-register.yaml` exists, prompt
   the attorney to upload a leave spreadsheet or use
   `/judge-fr-eu-employment-legal:log-leave` to add entries.

3. Alerts only for leaves requiring action. Clean leaves summarized one line each.

## Examples

```
/judge-fr-eu-employment-legal:leave-tracker
```

Run this weekly — set a Monday-morning reminder to invoke
`/judge-fr-eu-employment-legal:leave-tracker`. Automated scheduling requires a separate
integration (calendar reminder, cron job, etc.); Claude Code agents do not
self-schedule.
