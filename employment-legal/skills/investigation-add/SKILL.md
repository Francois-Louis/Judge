---
name: investigation-add
description: >
  Add data to an open investigation — documents, interview notes, or
  observations. Processes batches against the documented pull criteria,
  surfaces significant items, and logs everything reviewed for coverage
  verification. Use when new evidence, interview notes, or document
  productions come in for an open investigation.
argument-hint: "[matter name or slug, then paste or attach data]"
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /investigation-add

Adds data to an open investigation log. Processes document batches using
documented pull criteria, surfaces significant items, logs everything
reviewed for coverage verification.

## Instructions

1. Load `~/.claude/plugins/config/judge-fr-eu/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 2 (Add data).
3. After processing, show the surface ratio and list of surfaced items.
4. Prompt to update the sources checklist if the data covers a checklist item.

## Examples

```
/judge-fr-eu-employment-legal:investigation-add [matter name]
[paste interview notes]
```

```
/judge-fr-eu-employment-legal:investigation-add [matter name]
[attach email export]
```

> Detailed needle-finding process, log entry format, surface-ratio rules, and
> sources-checklist tracking live in the `internal-investigation` reference
> skill — load it before doing substantive work.
