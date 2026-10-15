---
name: investigation-memo
description: >
  Draft or update the privileged investigation memo from the investigation log.
  Use when an investigation is far enough along to write the first memo cut, or
  when new data has been added and the existing draft needs updating.
argument-hint: "[matter name]"
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /investigation-memo

Drafts the first cut of the privileged investigation memo from the log,
or updates an existing draft when new data has been added.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 4 (Draft or update memo).
2. If drafting for the first time, warn if high-priority sources are still
   open on the checklist.
3. If updating, show what changed before rewriting.
4. All output is marked PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT.

## Examples

```
/judge-fr-eu-employment-legal:investigation-memo [matter name]
```

```
/judge-fr-eu-employment-legal:investigation-memo [matter name]
(updates existing memo if one exists)
```

> Detailed memo structure, credibility-assessment framework, and update rules
> live in the `internal-investigation` reference skill — load it before doing
> substantive work.
