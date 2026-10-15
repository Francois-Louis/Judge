---
name: form-generation
description: >
  Reference: DEPRECATED — use `/draft` instead. This skill has been folded into
  the draft skill, which handles practice-area document generation including
  form population. Kept as a redirect for migration.
user-invocable: false
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# [DEPRECATED] Form Generation → see `/draft`

This skill was folded into `${CLAUDE_PLUGIN_ROOT}/skills/draft/` during the v2 rebuild. The `/draft`
command handles first-draft generation for all clinic documents including form
population (asylum applications, eviction answers, protective order petitions,
etc.) with practice-area templates and jurisdiction-aware formatting.

**Use `/draft [document type]` instead.**

See `${CLAUDE_PLUGIN_ROOT}/skills/draft/SKILL.md` for the full workflow.
