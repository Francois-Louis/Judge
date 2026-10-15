---
name: investigation-open
description: >
  Open a new internal investigation matter — runs intake, generates the sources
  checklist, and creates the persistent investigation log. Use when a complaint
  or allegation comes in and the attorney needs to stand up a privileged
  investigation workspace.
argument-hint: "[brief description of the allegation]"
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /investigation-open

Opens a new investigation matter — runs intake, generates the sources
checklist, and creates the persistent investigation log.

## Instructions

1. Load `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 1 (Open).
3. If a matter with the same slug already exists, warn before overwriting.

## Examples

```
/judge-fr-eu-employment-legal:investigation-open
Harassment complaint filed against a manager in the Austin office.
```

```
/judge-fr-eu-employment-legal:investigation-open
(skill will ask for details)
```

> Detailed intake, privilege-formation requirements, sources checklist, and log
> templates live in the `internal-investigation` reference skill — load it
> before doing substantive work.
